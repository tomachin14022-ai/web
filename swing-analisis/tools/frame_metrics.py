"""Medidas cuadro por cuadro para mostrar en pantalla (datos "en vivo") y posiciones P1-P10.

Uso: python -I frame_metrics.py SWING3D.json METRICS.json P_JSON SALIDA.json
P_JSON: {"P1": 64, "P2": 80, ..., "P10": 200} cuadros de cada posicion (verificados a ojo).
"""
import json
import math
import sys

import numpy as np

s3d, met, pj, out = sys.argv[1:5]
S3 = json.load(open(s3d)); M = json.load(open(met)); PP = json.load(open(pj))
k_cm = S3["k_m_por_px"] * 100
F = S3["frames"]; n = len(F); a = PP["P1"]
P = lambda t: np.array(F[t]["p2"])
cola = M["series"]["cola_x"]; c0 = M["linea_cola_address_x"]; lado = M.get("lado", 1.0)  # + = hacia la pelota

def ang(p, j1, j2, j3):
    v1, v2 = p[j1] - p[j2], p[j3] - p[j2]
    return math.degrees(math.acos(np.clip(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)), -1, 1)))

rows = []
ear0 = (P(a)[7] + P(a)[8]) / 2
for t in range(n):
    p = P(t); hp = (p[23] + p[24]) / 2; sh = (p[11] + p[12]) / 2; ear = (p[7] + p[8]) / 2
    rows.append({
        "cola_cm": round((cola[t] - c0) * lado * k_cm, 1),
        "incl": round(math.degrees(math.atan2(lado * (sh[0] - hp[0]), hp[1] - sh[1])), 1),
        "rodilla_atras": round(ang(p, 24, 26, 28)),
        "rodilla_adelante": round(ang(p, 23, 25, 27)),
        "talon_atras_cm": round(max(0.0, (P(a)[30][1] - p[30][1]) * k_cm), 1),
        "cabeza_baja_cm": round((ear[1] - ear0[1]) * k_cm, 1),
    })
json.dump({"P": PP, "frames": rows}, open(out, "w"))
for name, t in PP.items():
    print(name, t, rows[t])
