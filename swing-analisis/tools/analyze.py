"""Detecta los momentos del swing y calcula medidas aproximadas (vista desde atras, DTL).

Uso: python -I analyze.py POSE.json VIDEO CARPETA_SALIDA
Salidas: metrics.json, keyframes/*.png (con esqueleto), overlay/%04d.png (todos los cuadros).
Todas las medidas son 2D desde una sola camara: son aproximadas.
"""
import json
import math
import os
import sys

import cv2
import numpy as np

pose_path, video, outdir = sys.argv[1:4]
D = json.load(open(pose_path))
W, H, FPS = D["w"], D["h"], D["fps"]
F = D["frames"]
n = len(F)

# Landmarks en pixeles, suavizados (media movil de 5 cuadros) para quitar temblor.
P = np.array([[[p[0] * W, p[1] * H] for p in f["lm"]] for f in F])  # (n, 33, 2)
V = np.array([[p[3] for p in f["lm"]] for f in F])
k = 5
pad = np.pad(P, ((k // 2, k // 2), (0, 0), (0, 0)), mode="edge")
Ps = np.stack([pad[i:i + n] for i in range(k)]).mean(0)

NOSE, LSH, RSH, LEL, REL, LWR, RWR, LHI, RHI, LKN, RKN, LAN, RAN = 0, 11, 12, 13, 14, 15, 16, 23, 24, 25, 26, 27, 28
mid = lambda a, b: (Ps[:, a] + Ps[:, b]) / 2
hands, sh, hip = mid(LWR, RWR), mid(LSH, RSH), mid(LHI, RHI)
ank = mid(LAN, RAN)

# 1) Address: ultimo cuadro antes de que las manos se muevan > 3 % de la altura del cuerpo.
body_h = float(np.linalg.norm(Ps[0, NOSE] - ank[0])) * 1.08  # nariz->tobillo, + un poco por la cabeza
dist0 = np.linalg.norm(hands - hands[0], axis=1)
move = int(np.argmax(dist0 > 0.03 * body_h))
address = max(0, move - 1)

# 2) Tope: primer bloque con las manos por encima de los hombros; el punto mas alto.
above = hands[:, 1] < sh[:, 1]
blocks, start = [], None
for i in range(address, n):
    if above[i] and start is None:
        start = i
    if not above[i] and start is not None:
        blocks.append((start, i - 1)); start = None
if start is not None:
    blocks.append((start, n - 1))
b0 = blocks[0]
top = b0[0] + int(np.argmin(hands[b0[0]:b0[1] + 1, 1]))
# 3) Impacto: manos mas bajas entre el tope y el siguiente bloque alto (el final).
nxt = blocks[1][0] if len(blocks) > 1 else n - 1
impact = b0[1] + int(np.argmax(hands[b0[1]:nxt + 1, 1]))
# 4) Final: punto mas alto del segundo bloque, o el ultimo cuadro.
finish = (blocks[1][0] + int(np.argmin(hands[blocks[1][0]:blocks[1][1] + 1, 1]))) if len(blocks) > 1 else n - 1

def angle_deg(a, b, c):
    v1, v2 = a - b, c - b
    cos = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-9)
    return float(np.degrees(np.arccos(np.clip(cos, -1, 1))))

def spine_tilt(i):
    v = sh[i] - hip[i]  # inclinacion del tronco respecto de la vertical
    return float(np.degrees(math.atan2(abs(v[0]), -v[1])))

toward_ball = 1.0 if hands[address, 0] > hip[address, 0] else -1.0
pct = lambda px: round(100 * px / body_h, 1)
ev = {"address": address, "top": top, "impact": impact, "finish": finish}
m = {
    "eventos_cuadro": ev,
    "eventos_seg": {k2: round(v / FPS, 3) for k2, v in ev.items()},
    "ritmo_subida_bajada": round((top - move) / max(1, impact - top), 2),
    "subida_seg": round((top - move) / FPS, 2),
    "bajada_seg": round((impact - top) / FPS, 2),
    "precision_tiempo_seg": round(1 / FPS, 3),
    "inclinacion_tronco_grados": {k2: round(spine_tilt(v), 1) for k2, v in ev.items() if k2 != "finish"},
    "cadera_hacia_la_pelota_pct_altura": {
        k2: pct(toward_ball * (hip[v, 0] - hip[address, 0])) for k2, v in ev.items() if k2 != "address"},
    "cabeza_mov_pct_altura": {
        k2: {"horizontal": pct(Ps[v, NOSE, 0] - Ps[address, NOSE, 0]), "vertical_arriba": pct(Ps[address, NOSE, 1] - Ps[v, NOSE, 1])}
        for k2, v in ev.items() if k2 in ("top", "impact")},
    "flexion_rodilla_der_grados": {k2: round(angle_deg(Ps[v, RHI], Ps[v, RKN], Ps[v, RAN]), 1) for k2, v in ev.items()},
    "flexion_rodilla_izq_grados": {k2: round(angle_deg(Ps[v, LHI], Ps[v, LKN], Ps[v, LAN]), 1) for k2, v in ev.items()},
    "visibilidad_media": {k2: round(float(V[v].mean()), 2) for k2, v in ev.items()},
}
os.makedirs(outdir, exist_ok=True)
json.dump(m, open(os.path.join(outdir, "metrics.json"), "w"), indent=1, ensure_ascii=False)
print(json.dumps(m, indent=1, ensure_ascii=False))

# Dibujo del esqueleto sobre cada cuadro.
EDGES = [(11, 12), (11, 13), (13, 15), (12, 14), (14, 16), (11, 23), (12, 24), (23, 24), (23, 25), (25, 27), (24, 26), (26, 28), (27, 31), (28, 32), (27, 29), (28, 30)]
cap = cv2.VideoCapture(video)
os.makedirs(os.path.join(outdir, "overlay"), exist_ok=True)
os.makedirs(os.path.join(outdir, "keyframes"), exist_ok=True)
i = 0
s = 3  # escala para que el trazo se vea fino en un video chico
while True:
    ok, img = cap.read()
    if not ok:
        break
    img = cv2.resize(img, (W * s, H * s), interpolation=cv2.INTER_CUBIC)
    q = (Ps[i] * s).astype(int)
    # linea de referencia: cadera en el address (para ver si se acerca a la pelota)
    x0 = int(hip[address, 0] * s)
    cv2.line(img, (x0, int(sh[address, 1] * s) - 40), (x0, int(ank[address, 1] * s)), (90, 90, 255), 2, cv2.LINE_AA)
    for a, b in EDGES:
        cv2.line(img, tuple(q[a]), tuple(q[b]), (255, 255, 255), 5, cv2.LINE_AA)
        cv2.line(img, tuple(q[a]), tuple(q[b]), (40, 22, 128), 2, cv2.LINE_AA)
    for j in [0, 11, 12, 13, 14, 15, 16, 23, 24, 25, 26, 27, 28]:
        cv2.circle(img, tuple(q[j]), 6, (255, 255, 255), -1, cv2.LINE_AA)
    cv2.imwrite(os.path.join(outdir, "overlay", f"{i:04d}.png"), img)
    for name, fr in ev.items():
        if fr == i:
            cv2.imwrite(os.path.join(outdir, "keyframes", f"{name}.png"), img)
    i += 1
print("cuadros dibujados:", i)
