"""Subtitulos sincronizados con alineacion forzada (no con los tiempos aproximados de Whisper).

Uso: python -I align_captions.py GUION.json SECCIONES.json CARPETA_VOZ SALIDA.json
- Necesita un venv con torch 2.9 + torchaudio 2.9 (modelo MMS_FA de Meta, multilingue).
- Alinea cada frase por separado (archivo segNN.wav = la frase tal cual quedo en la pista)
  contra el texto que DICE la voz ("cuarenta y seis", "te pe i") y despues pasa los tiempos
  al texto que se MUESTRA ("46", "TPI").
- Paginas de 1 a 4 palabras y hasta 20 letras, cortando en la puntuacion.
"""
import difflib
import json
import re
import sys
import unicodedata

import soundfile as sf
import torch
import torchaudio

guion_p, sec_p, vdir, out = sys.argv[1:5]
G = json.load(open(guion_p)); SEC = json.load(open(sec_p))["secs"]
bundle = torchaudio.pipelines.MMS_FA
model = bundle.get_model(with_star=False).eval()
tokenizer, aligner = bundle.get_tokenizer(), bundle.get_aligner()
VOC = set(bundle.get_dict().keys())

def norm(w):
    w = unicodedata.normalize("NFD", w.lower())
    w = "".join(c for c in w if unicodedata.category(c) != "Mn")
    return "".join(c for c in w if c in VOC and c not in ("-", "*"))

words = []
for k, (sec, g) in enumerate(zip(SEC, G)):
    a, sr = sf.read(f"{vdir}/seg{k:02d}.wav", dtype="float32")
    wav = torchaudio.functional.resample(torch.from_numpy(a)[None], sr, bundle.sample_rate)
    spoken = [w for w in g["voz"].split()]
    sp_norm = [norm(w) for w in spoken]
    keep = [i for i, w in enumerate(sp_norm) if w]
    with torch.inference_mode():
        em, _ = model(wav)
    spans = aligner(em[0], tokenizer([sp_norm[i] for i in keep]))
    ratio = wav.shape[1] / em.shape[1] / bundle.sample_rate
    t_sp = [None] * len(spoken)
    for i, s in zip(keep, spans):
        t_sp[i] = (sec["start"] + s[0].start * ratio, sec["start"] + s[-1].end * ratio)
    for i in range(len(t_sp)):  # palabras sin letras (raro): pegarlas a la anterior
        if t_sp[i] is None:
            t_sp[i] = t_sp[i - 1] if i else (sec["start"], sec["start"] + 0.1)
    shown = g["texto"].split()
    a_n = [norm(w) for w in spoken]; b_n = [norm(w) for w in shown]
    t_sh = [None] * len(shown)
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a_n, b=b_n, autojunk=False).get_opcodes():
        if tag == "equal":
            for q in range(i2 - i1):
                t_sh[j1 + q] = t_sp[i1 + q]
        elif tag in ("replace", "insert") and j2 > j1:
            s0 = t_sp[i1][0] if i1 < len(t_sp) else t_sp[-1][1]
            e0 = t_sp[i2 - 1][1] if i2 > i1 else s0 + 0.15
            for q in range(j2 - j1):
                t_sh[j1 + q] = (s0 + (e0 - s0) * q / (j2 - j1), s0 + (e0 - s0) * (q + 1) / (j2 - j1))
    for j, w in enumerate(shown):
        s, e = t_sh[j] if t_sh[j] else (t_sh[j - 1][1], t_sh[j - 1][1] + 0.1)
        words.append({"w": w, "s": round(s, 3), "e": round(e, 3), "sec": g["id"]})

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
for p, q in zip(pages, pages[1:]):
    if q["s"] - p["e"] < 0.6:
        p["e"] = q["s"]
json.dump({"words": words, "pages": pages}, open(out, "w"), ensure_ascii=False, indent=0)
print(len(words), "palabras,", len(pages), "paginas")
