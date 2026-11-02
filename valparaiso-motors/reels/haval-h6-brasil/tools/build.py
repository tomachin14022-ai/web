"""Arma index.html a partir de la plantilla y de timing.json.

Uso: python3 tools/build.py   (desde la carpeta del proyecto)
Cuando llegue la voz definitiva: transcribir, correr align.py, mix.py y este script.
"""
import json

COLA = 1.3  # segundos despues de la ultima palabra (cierre corto para que el loop arranque rapido)

timing = json.load(open("timing.json", encoding="utf-8"))
dur = round(timing["tokens"][-1]["end"] + COLA, 2)
tpl = open("tools/index.template.html", encoding="utf-8").read()
html = tpl.replace("__DURATION__", str(dur)).replace("__TIMING__", json.dumps(timing, ensure_ascii=False))
open("index.html", "w", encoding="utf-8").write(html)
print(f"index.html listo · duracion {dur} s")
