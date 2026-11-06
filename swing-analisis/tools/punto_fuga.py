"""Punto de fuga de la línea de tiro y control de la cámara de atrás.

Uso: python -I punto_fuga.py "X1,Y1 X2,Y2" "X3,Y3 X4,Y4" [--video 1080x1920] [--f PX]
Cada argumento son dos puntos (en px del video) sobre uno de los palos o varillas del piso, paralelos a la línea de tiro.
Los puntos se leen en una hoja con grilla (grid_hd.py). Devuelve el punto de fuga para --vp y si la cámara pasa el control
(giro ≤ 5°: θ = atan(d/f), con f ≈ 1.400 px en 1080x1920).
"""
import argparse
import math

import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("linea1"); ap.add_argument("linea2")
ap.add_argument("--video", default="1080x1920"); ap.add_argument("--f", type=float)
A = ap.parse_args()
pts = lambda s: [np.array(list(map(float, p.split(","))) + [1.0]) for p in s.split()]
(a1, a2), (b1, b2) = pts(A.linea1), pts(A.linea2)
v = np.cross(np.cross(a1, a2), np.cross(b1, b2))
if abs(v[2]) < 1e-9:
    raise SystemExit("Las líneas son paralelas en la imagen: la cámara apunta perfecto o los puntos están mal marcados.")
vx, vy = v[0] / v[2], v[1] / v[2]
w, h = map(float, A.video.lower().split("x")); f = A.f or 1400.0 * max(w, h) / 1920
giro = math.degrees(math.atan((vx - w / 2) / f)); incl = math.degrees(math.atan((vy - h / 2) / f))
print(f"--vp {vx:.0f},{vy:.0f}")
print(f"giro de la cámara {giro:+.1f}° ({'pasa' if abs(giro) <= 5 else 'NO pasa: el slot de TPI no vale, solo la prueba relativa'})")
print(f"inclinación {incl:+.1f}° (punto de fuga {'arriba' if incl < 0 else 'abajo'} del centro)")
