"""Hoja de cuadros de prueba (vista desde atrás): P1, P3, P4, P5, P6 y P7 con las capas que prueban cada medida.

Uso: python -I hoja_prueba.py CONFIG.json SALIDA.jpg [--view X0,Y0,ANCHO]
CONFIG.json es el mismo de render_v4.py (no hace falta "timeline": se arma acá).
Se muestra antes de grabar la voz y renderizar: cada número del análisis tiene que verse dibujado en esta hoja.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image, ImageDraw, ImageFont

PANELES = [
    ("P1", "P1 · SETUP", ["skel", "spine_ref", "tush", "slot"]),
    ("P3", "P3 · LÍNEA B", ["skel", "slot"]),
    ("P4", "P4 · TOPE", ["skel", "spine_delta", "shoulder_plane", "shaft_ext", "target_line"]),
    ("P5", "P5 · BAJADA", ["skel", "hand_paths", "slot"]),
    ("P6", "P6 · MANOS", ["skel", "hand_paths"]),
    ("P7", "P7 · IMPACTO", ["skel", "spine_delta", "tush"]),
]
FONT = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"

ap = argparse.ArgumentParser()
ap.add_argument("config"); ap.add_argument("salida"); ap.add_argument("--view")
A = ap.parse_args()
C = json.load(open(A.config)); FM = json.load(open(C["fmetrics"])); S3 = json.load(open(C["swing3d"]))
PP = {k: int(v) for k, v in FM["P"].items()}

if A.view:
    view = list(map(float, A.view.split(",")))
else:  # todo el cuerpo y el palo de P1 a P8, con margen, en la proporción del panel (1520x2060)
    pts = np.array([q for t in range(PP["P1"], PP["P8"] + 1) for q in S3["frames"][t]["p2"] + [S3["frames"][t]["h2"]]])
    x0, y0 = np.nanmin(pts, 0); x1, y1 = np.nanmax(pts, 0); y1 = max(y1, S3["piso_px"])
    w = max(x1 - x0, (y1 - y0) * 1520 / 2060) * 1.12
    view = [float((x0 + x1) / 2 - w / 2), float((y0 + y1) / 2 - w * 2060 / 1520 / 2), float(w)]

tmp = tempfile.mkdtemp(prefix="hoja_")
tl = {"frames": [{"t": 10.0, "src": PP[p], "mode": "single", "view": view, "L": L, "starts": {n: 0 for n in L}}
                 for p, _, L in PANELES]}
json.dump(tl, open(os.path.join(tmp, "tl.json"), "w"))
C2 = dict(C, timeline=os.path.join(tmp, "tl.json")); json.dump(C2, open(os.path.join(tmp, "cfg.json"), "w"))
subprocess.run([sys.executable, "-I", os.path.join(os.path.dirname(os.path.abspath(__file__)), "render_v4.py"),
                os.path.join(tmp, "cfg.json"), os.path.join(tmp, "out")], check=True)

f = ImageFont.truetype(FONT, 40)
W, H = 760, 1030
hoja = Image.new("RGB", (3 * W, 2 * H), (12, 18, 15))
for k, (_, titulo, _) in enumerate(PANELES):
    im = Image.open(os.path.join(tmp, "out", f"{k:05d}.png")).convert("RGB")
    d = ImageDraw.Draw(im); bb = d.textbbox((0, 0), titulo, font=f)
    d.rounded_rectangle([16, 16, 16 + bb[2] + 36, 16 + bb[3] + 28], radius=26, fill=(12, 18, 15))
    d.text((34, 26), titulo, font=f, fill=(201, 242, 107))
    hoja.paste(im, ((k % 3) * W, (k // 3) * H))
hoja.resize((3 * W * 3 // 5, 2 * H * 3 // 5), Image.LANCZOS).save(A.salida, quality=90)
print("hoja:", A.salida, "· vista", [round(v) for v in view])
