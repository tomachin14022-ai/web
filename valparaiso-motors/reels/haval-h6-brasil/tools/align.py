"""Alinea el guion de pantalla con los tiempos por palabra de Whisper.

Uso:
  python3 tools/align.py audio/<voz>/transcript.json guion/guion-pantalla.txt timing.json

Los subtitulos muestran el texto del guion (con numeros y siglas bien escritos),
aunque Whisper haya oido otra cosa. Cada palabra del guion se expande a como se
pronuncia ("44.020" -> "cuarenta y cuatro mil veinte", "H6" -> "hache seis"),
se alinea con difflib contra lo que oyo Whisper y lo que no coincide se interpola.
"""
import difflib
import json
import re
import sys
import unicodedata

UNI = ("cero uno dos tres cuatro cinco seis siete ocho nueve diez once doce trece catorce quince "
       "dieciseis diecisiete dieciocho diecinueve veinte veintiuno veintidos veintitres veinticuatro "
       "veinticinco veintiseis veintisiete veintiocho veintinueve").split()
DEC = {3: "treinta", 4: "cuarenta", 5: "cincuenta", 6: "sesenta", 7: "setenta", 8: "ochenta", 9: "noventa"}
CEN = {1: "ciento", 2: "doscientos", 3: "trescientos", 4: "cuatrocientos", 5: "quinientos",
       6: "seiscientos", 7: "setecientos", 8: "ochocientos", 9: "novecientos"}


def num_es(n: int) -> str:
    if n < 30:
        return UNI[n]
    if n < 100:
        d, u = divmod(n, 10)
        return DEC[d] + ("" if u == 0 else " y " + UNI[u])
    if n < 1000:
        c, r = divmod(n, 100)
        if n == 100:
            return "cien"
        return CEN[c] + ("" if r == 0 else " " + num_es(r))
    if n < 1_000_000:
        m, r = divmod(n, 1000)
        head = "mil" if m == 1 else num_es(m) + " mil"
        return head + ("" if r == 0 else " " + num_es(r))
    return str(n)


SPECIAL = {"h6": "hache seis", "suv": "suv", "hev": "hache e ve"}


def strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def spoken_units(token: str) -> list[str]:
    """Palabras pronunciadas (normalizadas) para un token del guion o de Whisper."""
    t = strip_accents(token.lower())
    t = re.sub(r"[^\w.]", "", t).strip(".")
    if not t:
        return []
    if t in SPECIAL:
        return SPECIAL[t].split()
    if re.fullmatch(r"\d{1,3}(\.\d{3})+|\d+", t):
        return num_es(int(t.replace(".", ""))).split()
    t = t.replace(".", "")
    return [t] if t else []


def split_whisper(words):
    """Separa tokens pegados ("mes.¿Como?") repartiendo el tiempo por largo."""
    out = []
    for w in words:
        parts = [p for p in re.split(r"[.,;:!?¿¡]+", w["text"]) if p.strip()]
        if len(parts) <= 1:
            out.append({"text": w["text"], "start": w["start"], "end": w["end"]})
            continue
        total = sum(len(p) for p in parts)
        t = w["start"]
        for p in parts:
            d = (w["end"] - w["start"]) * len(p) / total
            out.append({"text": p, "start": t, "end": t + d})
            t += d
    return out


def main(transcript_path, script_path, out_path):
    words = json.load(open(transcript_path, encoding="utf-8"))
    if isinstance(words, dict):
        words = words.get("words", [])
    words = split_whisper(words)

    # Unidades de Whisper con su tiempo (una palabra numerica se reparte entre sus unidades)
    w_units, w_times = [], []
    for w in words:
        us = spoken_units(w["text"])
        if not us:
            continue
        d = (w["end"] - w["start"]) / len(us)
        for k, u in enumerate(us):
            w_units.append(u)
            w_times.append((w["start"] + k * d, w["start"] + (k + 1) * d))

    # Tokens del guion de pantalla
    text = open(script_path, encoding="utf-8").read().strip()
    tokens = []
    for si, line in enumerate([l for l in text.splitlines() if l.strip()]):
        for raw in line.split():
            tokens.append({"text": raw, "sentence": si, "units": spoken_units(raw)})

    s_units, owner = [], []
    for ti, tk in enumerate(tokens):
        for u in tk["units"]:
            s_units.append(u)
            owner.append(ti)

    times = [None] * len(s_units)
    sm = difflib.SequenceMatcher(a=s_units, b=w_units, autojunk=False)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            times[a + k] = w_times[b + k]

    # Interpolar las unidades sin coincidencia entre sus vecinas
    known = [i for i, t in enumerate(times) if t]
    for i in range(len(times)):
        if times[i]:
            continue
        prev = max((k for k in known if k < i), default=None)
        nxt = min((k for k in known if k > i), default=None)
        if prev is None:
            t0, t1 = 0.0, times[nxt][0]
            span = (t0, t1)
            gap_units = nxt
            pos = i
        elif nxt is None:
            t0 = times[prev][1]
            span = (t0, t0 + 0.3 * (len(times) - prev))
            gap_units = len(times) - prev - 1
            pos = i - prev - 1
        else:
            span = (times[prev][1], times[nxt][0])
            gap_units = nxt - prev - 1
            pos = i - prev - 1
        d = (span[1] - span[0]) / max(gap_units, 1)
        times[i] = (span[0] + pos * d, span[0] + (pos + 1) * d)

    for ti, tk in enumerate(tokens):
        idx = [k for k, o in enumerate(owner) if o == ti]
        if idx:
            tk["start"] = round(times[idx[0]][0], 3)
            tk["end"] = round(times[idx[-1]][1], 3)
        else:  # signos sueltos
            tk["start"] = tk["end"] = tokens[ti - 1]["end"] if ti else 0.0
        del tk["units"]

    matched = sum(1 for a, b, n in sm.get_matching_blocks() for _ in range(n))
    json.dump({"tokens": tokens, "voiceEnd": round(words[-1]["end"], 3)}, open(out_path, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"{len(tokens)} palabras del guion, {matched}/{len(s_units)} unidades coinciden con Whisper")


if __name__ == "__main__":
    main(*sys.argv[1:4])
