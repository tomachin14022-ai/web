"""Subtitulos palabra por palabra: texto del guion + tiempos de Whisper.

Uso: python -I captions.py GUION.json TRANSCRIPT.json SECCIONES.json SALIDA.json
- Alinea las palabras del guion (texto correcto, con "3D", "TPI", numeros) con las que
  oyo Whisper (difflib), y les pasa los tiempos. Las que no matchean se interpolan.
- Arma paginas de 1 a 4 palabras y hasta 20 letras, cortando en la puntuacion.
"""
import difflib
import json
import re
import sys
import unicodedata

guion_p, tr_p, sec_p, out = sys.argv[1:5]
G = json.load(open(guion_p)); T = json.load(open(tr_p)); SEC = json.load(open(sec_p))
tw = T if isinstance(T, list) else T["words"]

def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]", "", s)

script = []  # (palabra_original, seccion_idx)
for k, sec in enumerate(G):
    for wd in sec["texto"].split():
        script.append((wd, k))
a = [norm(w) for w, _ in script]
b = [norm(x["text"]) for x in tw]
times = [None] * len(script)
sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
for blk in sm.get_matching_blocks():
    for i in range(blk.size):
        times[blk.a + i] = (tw[blk.b + i]["start"], tw[blk.b + i]["end"])
# pares reemplazados 1 a 1 (ej. "y en" -> "quien") -> repartir el tiempo
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "replace":
        s0, e0 = tw[j1]["start"], tw[j2 - 1]["end"]
        for q, i in enumerate(range(i1, i2)):
            times[i] = (s0 + (e0 - s0) * q / (i2 - i1), s0 + (e0 - s0) * (q + 1) / (i2 - i1))
# huecos: interpolar dentro de la seccion
for i in range(len(script)):
    if times[i] is None:
        k = script[i][1]
        prev = next((times[j][1] for j in range(i - 1, -1, -1) if times[j]), SEC[k]["start"])
        nxt = next((times[j][0] for j in range(i + 1, len(script)) if times[j]), SEC[k]["end"])
        times[i] = (prev, max(prev + 0.12, nxt))
words = [{"w": w, "s": round(t[0], 3), "e": round(t[1], 3), "sec": G[k]["id"]} for (w, k), t in zip(script, times)]

pages, cur = [], []
def flush():
    if cur:
        pages.append({"s": cur[0]["s"], "e": cur[-1]["e"], "words": list(cur)}); cur.clear()
for wd in words:
    txt = " ".join(x["w"] for x in cur + [wd])
    if cur and (len(cur) >= 4 or len(txt) > 20 or wd["sec"] != cur[-1]["sec"]):
        flush()
    cur.append(wd)
    if re.search(r"[.,:;?!]$", wd["w"]):
        flush()
flush()
for p, q in zip(pages, pages[1:]):  # cada pagina queda hasta que entra la siguiente (sin huecos cortos)
    if q["s"] - p["e"] < 0.6:
        p["e"] = q["s"]
json.dump({"words": words, "pages": pages}, open(out, "w"), ensure_ascii=False, indent=0)
print(len(words), "palabras,", len(pages), "paginas; mas larga:", max(len(" ".join(x["w"] for x in p["words"])) for p in pages), "letras")
