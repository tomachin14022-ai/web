#!/usr/bin/env python3
"""Pasa los tiempos por palabra de Whisper (transcript.json) a src/datos/palabras-<id>.json.

Uso: python3 palabras.py <transcript.json> <id>
Separa las palabras que Whisper pegó ("doble.¿Cuál"), corrige el voseo que oye mal
("compras" → "comprás") y pone el signo $ en los precios, para que el subtítulo muestre
el texto correcto aunque Whisper haya oído otra cosa.
"""
import json
import re
import sys
from pathlib import Path

VOSEO = {"compras": "comprás", "mira": "mirá", "tomas": "tomás", "ahorras": "ahorrás"}
PRECIOS = {
    "impresora": {"214", "5", "500.000"},
    "cafetera": {"2.400", "703"},
    "aire": {"173", "121", "200.000"},
}

src, vid = sys.argv[1], sys.argv[2]
palabras = []
for w in json.loads(Path(src).read_text(encoding="utf-8")):
    partes = [p for p in re.split(r"(?=¿)", w["text"]) if p]
    total = sum(len(p) for p in partes)
    t = w["start"]
    for p in partes:
        fin = t + (w["end"] - w["start"]) * len(p) / total
        palabras.append({"texto": p, "desde": round(t, 3), "hasta": round(fin, 3)})
        t = fin

for p in palabras:
    m = re.match(r"^(¿?)(.*?)([.,?!]*)$", p["texto"])
    abre, base, cierra = m.groups()
    if base.lower() in VOSEO:
        nueva = VOSEO[base.lower()]
        base = nueva.capitalize() if base[0].isupper() else nueva
    if base in PRECIOS.get(vid, set()):
        base = "$" + base
    if abre == "¿" and not cierra:
        pass
    p["texto"] = abre + base + cierra

# "¿Mirá cuánto cuesta cada café?" → afirmación, como en el guion
for i, p in enumerate(palabras):
    if p["texto"] == "¿Mirá":
        p["texto"] = "Mirá"
        for q in palabras[i:]:
            if q["texto"].endswith("?"):
                q["texto"] = q["texto"][:-1] + "."
                break

Path(f"src/datos/palabras-{vid}.json").write_text(json.dumps(palabras, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(vid, " ".join(f"{p['texto']}@{p['desde']}" for p in palabras))
