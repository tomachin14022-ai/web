"""Medidas del swing (vista desde atras / down the line), con camara compensada.

Uso: python -I metrics.py POSE.npz STAB.npz CLUB.npz SWING3D.json SALIDA.json
Usa la silueta (mascara) para la linea de cola y la cabeza, y los puntos del cuerpo para
el angulo de columna y las rodillas. Todo en pixeles del cuadro de referencia y en %
de la altura del golfista. Son medidas 2D de una camara: aproximadas.
"""
import json
import sys

import cv2
import numpy as np
from scipy.signal import butter, filtfilt

pose_p, stab_p, club_p, s3d_p, out = sys.argv[1:6]
P = np.load(pose_p); A = np.load(stab_p)["A"]; C = np.load(club_p); S3 = json.load(open(s3d_p))
lm, masks = P["lm"], P["mask"]
n, h, w = masks.shape
ev = S3["eventos"]
ref, imp, top = ev["address"], ev["impacto"], ev["tope"]

def stab_pts(t, xy):
    return xy @ A[t][:, :2].T + A[t][:, 2]

def lp(x, wn=0.45):
    b, a = butter(2, wn); return filtfilt(b, a, x, axis=0, padlen=min(15, len(x) - 1))

P2 = lp(np.array([stab_pts(t, lm[t, :, :2]) for t in range(n)]))
M = np.array([cv2.warpAffine(masks[t], A[t], (w, h)) for t in range(n)])  # siluetas estabilizadas
ball = stab_pts(ref, C["ball"][None])[0]
hip_ref = (P2[ref, 23] + P2[ref, 24]) / 2
toward = 1.0 if ball[0] > hip_ref[0] else -1.0  # +1: la pelota esta a la derecha (+x) del jugador en la imagen
foot_y = float(np.max(P2[ref, [29, 30, 31, 32], 1]))
head_top = float(np.argmax(M[ref].max(1) > 128))
body_h = foot_y - head_top  # altura en pixeles (agachado, en el address)

def butt_x(t):
    """Punto mas atrasado de la silueta a la altura de la cola (cadera +- un poco)."""
    hy = int((P2[t, 23, 1] + P2[t, 24, 1]) / 2)
    band = M[t, max(0, hy - int(0.02 * body_h)): hy + int(0.07 * body_h)] > 128
    xs = np.where(band.any(0))[0]
    if not len(xs):
        return np.nan
    return float(xs.min()) if toward > 0 else float(xs.max())  # el punto mas alejado de la pelota

def head_box(t):
    """Caja de la cabeza: desde la silueta, arriba de los hombros."""
    sh_y = int(min(P2[t, 11, 1], P2[t, 12, 1]))
    ear = (P2[t, 7] + P2[t, 8]) / 2
    x0, x1 = int(ear[0] - 0.09 * body_h), int(ear[0] + 0.09 * body_h)
    reg = M[t, : sh_y, max(0, x0): x1] > 128
    ys, xs = np.where(reg)
    if len(ys) == 0:
        return None
    return [float(xs.min() + max(0, x0)), float(ys.min()), float(xs.max() + max(0, x0)), float(sh_y)]

bx = lp(np.array([butt_x(t) for t in range(n)]), 0.35)
ear = (P2[:, 7] + P2[:, 8]) / 2
sh = (P2[:, 11] + P2[:, 12]) / 2; hip = (P2[:, 23] + P2[:, 24]) / 2
spine = np.degrees(np.arctan2(toward * (sh[:, 0] - hip[:, 0]), hip[:, 1] - sh[:, 1]))  # + inclinado hacia la pelota

def ang(a, b, c):
    v1, v2 = a - b, c - b
    return float(np.degrees(np.arccos(np.clip(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)), -1, 1))))

heel = {"izq": P2[:, 29, 1], "der": P2[:, 30, 1]}
pct = lambda v: round(100 * v / body_h, 1)
moments = {"address": ref, "tope": top, "bajada_mitad": top + (imp - top) // 2, "impacto": imp, "despues": imp + 6}
res = {"altura_px": round(body_h, 1), "momentos": moments, "por_momento": {}}
for name, t in moments.items():
    res["por_momento"][name] = {
        "cola_hacia_pelota_pct": pct(toward * (bx[t] - bx[ref])),
        "cabeza_horizontal_pct": pct(toward * (ear[t, 0] - ear[ref, 0])),
        "cabeza_baja_pct": pct(ear[t, 1] - ear[ref, 1]),
        "columna_grados": round(float(spine[t]), 1),
        "rodilla_der_grados": round(ang(P2[t, 24], P2[t, 26], P2[t, 28]), 1),
        "rodilla_izq_grados": round(ang(P2[t, 23], P2[t, 25], P2[t, 27]), 1),
        "talon_der_arriba_pct": pct(heel["der"][ref] - heel["der"][t]),
        "talon_izq_arriba_pct": pct(heel["izq"][ref] - heel["izq"][t]),
    }
# Plano: linea de la varilla en el address (pelota -> manos) y linea pelota -> hombro de atras.
grip = (P2[:, 15] + P2[:, 16] + P2[:, 19] + P2[:, 20]) / 4
res["plano"] = {"pelota": ball.round(1).tolist(), "manos_address": grip[ref].round(1).tolist(),
                "hombro_der_address": P2[ref, 12].round(1).tolist()}
res["series"] = {"cola_x": bx.round(1).tolist(), "oreja": ear.round(1).tolist(), "columna": spine.round(1).tolist()}
res["caja_cabeza_address"] = head_box(ref)
res["linea_cola_address_x"] = round(float(bx[ref]), 1)
res["lado"] = toward  # +1 pelota a la derecha; las series en px no cambian de signo, los "_pct" ya van hacia la pelota
json.dump(res, open(out, "w"), indent=1)
for k2, v in res["por_momento"].items():
    print(k2, v)
print("plano", res["plano"], "cabeza", res["caja_cabeza_address"], "cola", res["linea_cola_address_x"])
