"""Arma los datos 3D del swing para el maniqui (cuerpo + palo + pelota).

Uso: python -I build3d.py POSE.npz STAB.npz CLUB.npz ANCLAS_PALO.json REF IMPACTO SALIDA.json

Idea: x e y salen del video (estabilizado), asi el 3D visto desde la camara coincide con
el video. La profundidad sale del modelo de MediaPipe, suavizada, y se corrige para que
cada hueso tenga SIEMPRE el mismo largo (el maniqui no se estira ni se encoge).
El palo sale de la punta marcada a ojo en cuadros clave (ANCLAS_PALO.json:
{"cuadro": [x_px, y_px, profundidad_con_signo]}), interpolada entre anclas.
Todo en metros: x hacia la pelota, y hacia arriba, z hacia la camara.
"""
import json
import sys

import numpy as np
from scipy.signal import butter, filtfilt

pose_p, stab_p, club_p, anch_p, ref, impact, out = sys.argv[1:8]
ref, impact = int(ref), int(impact)
P = np.load(pose_p); A = np.load(stab_p)["A"]; C = np.load(club_p)
lm, wo = P["lm"], P["world"]
n = len(lm)
fps = float(P["fps"])

def stab(t, xy):
    return xy @ A[t][:, :2].T + A[t][:, 2]

P2 = np.array([stab(t, lm[t, :, :2]) for t in range(n)])  # (n,33,2) en coords del cuadro ref

def lowpass(x, wn):
    b, a = butter(2, wn)
    return filtfilt(b, a, x, axis=0, padlen=min(15, len(x) - 1))

P2s = lowpass(P2, 0.45)
Zw = lowpass(-wo[:, :, 2], 0.22)  # profundidad: + hacia la camara

# Escala metros/pixel con segmentos del tronco y las piernas.
segs = [(11, 23), (12, 24), (23, 25), (24, 26), (25, 27), (26, 28), (11, 12), (23, 24)]
ratios = []
for t in range(n):
    for a, b in segs:
        px = np.linalg.norm(P2s[t, a] - P2s[t, b])
        if px > 15:
            ratios.append(np.linalg.norm(wo[t, a, :2] - wo[t, b, :2]) / px)
k = float(np.median(ratios))
u0 = float((P2s[ref, 23, 0] + P2s[ref, 24, 0]) / 2)
v_floor = float(np.max(P2s[ref, [29, 30, 31, 32], 1]))
X = k * (P2s[:, :, 0] - u0)
Y = k * (v_floor - P2s[:, :, 1])
Z = Zw.copy()

# Largo fijo por hueso (mediana, con izquierda y derecha iguales).
BONES = [(23, 11), (24, 12), (11, 13), (13, 15), (15, 17), (15, 19), (15, 21), (12, 14), (14, 16), (16, 18),
         (16, 20), (16, 22), (23, 25), (25, 27), (27, 29), (27, 31), (24, 26), (26, 28), (28, 30), (28, 32)]
def L3(a, b):
    return np.sqrt((X[:, b] - X[:, a]) ** 2 + (Y[:, b] - Y[:, a]) ** 2 + (Zw[:, b] - Zw[:, a]) ** 2)
# Un hueso nunca se ve mas largo de lo que es: el largo real es al menos lo maximo que se
# ve en el video (percentil 95 para no tomar errores) y al menos la mediana del modelo 3D.
def L2(a, b):
    return np.sqrt((X[:, b] - X[:, a]) ** 2 + (Y[:, b] - Y[:, a]) ** 2)
blen = {bb: float(max(np.median(L3(*bb)), np.percentile(L2(*bb), 95))) for bb in BONES}
pairs = {(23, 11): (24, 12), (11, 13): (12, 14), (13, 15): (14, 16), (15, 17): (16, 18), (15, 19): (16, 20),
         (15, 21): (16, 22), (23, 25): (24, 26), (25, 27): (26, 28), (27, 29): (28, 30), (27, 31): (28, 32)}
for l, r in pairs.items():
    m = (blen[l] + blen[r]) / 2; blen[l] = blen[r] = m
for a, b in BONES:  # en orden: cada padre ya esta corregido
    dxy = np.sqrt((X[:, b] - X[:, a]) ** 2 + (Y[:, b] - Y[:, a]) ** 2)
    # profundidad del modelo, recortada solo si con ese largo de hueso es imposible
    # (no se agranda: agrandarla cuando el hueso esta casi de costado amplifica errores)
    dz_max = np.sqrt(np.clip(blen[(a, b)] ** 2 - dxy ** 2, 0, None))
    dzw = Zw[:, b] - Zw[:, a]
    Z[:, b] = Z[:, a] + np.sign(dzw) * np.minimum(np.abs(dzw), dz_max)
Z = lowpass(Z, 0.3)
# cabeza: misma posicion relativa a los hombros que en el modelo
shz_w = (Zw[:, 11] + Zw[:, 12]) / 2; shz = (Z[:, 11] + Z[:, 12]) / 2
for j in range(0, 11):
    Z[:, j] = shz + (Zw[:, j] - shz_w)
J = np.stack([X, Y, Z], -1)  # (n,33,3)

# --- Palo -------------------------------------------------------------------------------
anch = {int(kk): v for kk, v in json.load(open(anch_p)).items() if not kk.startswith("_")}
L_px = float(C["L"]); Lm = k * L_px
grip2 = (P2s[:, 15] + P2s[:, 16] + P2s[:, 19] + P2s[:, 20]) / 4
grip3 = (J[:, 15] + J[:, 16] + J[:, 19] + J[:, 20]) / 4
ks = sorted(anch)
# Pelota: x,y del video; la profundidad no se ve desde atras -> se asume a la altura del
# talon del pie adelantado (posicion habitual con driver). Es un supuesto: mostrarlo asi.
ball_px = stab(ref, np.array([[anch[ks[1]][0], anch[ks[1]][1]]]))[0]
ball = np.array([k * (ball_px[0] - u0), 0.045, float(np.mean(J[max(0, ref - 10):ref + 1, 29, 2])) + 0.04])
at_ball = lambda f0: np.hypot(anch[f0][0] - anch[ks[1]][0], anch[f0][1] - anch[ks[1]][1]) < 8
rel = {}
for f0 in ks:
    hx, hy, dzr = anch[f0]
    h = stab(f0, np.array([[hx, hy]]))[0]
    d = h - grip2[f0]
    if at_ball(f0):  # el palo apoyado en la pelota: profundidad = la de la pelota
        dzr = float((ball[2] - grip3[f0][2]) / Lm)
    rel[f0] = (np.degrees(np.arctan2(d[1], d[0])), np.linalg.norm(d), dzr)
ang = np.zeros(n); ln = np.zeros(n); dzr = np.zeros(n)
for t in range(n):
    if t >= ks[-1]:
        a0 = rel[ks[-1]]; ang[t], ln[t], dzr[t] = a0; continue
    i = max(x for x in ks if x <= t); j = min(x for x in ks if x > t)
    s = (t - i) / (j - i); (a1, l1, z1), (a2, l2, z2) = rel[i], rel[j]
    da = ((a2 - a1 + 180) % 360) - 180
    ang[t] = a1 + s * da; ln[t] = l1 + s * (l2 - l1); dzr[t] = z1 + s * (z2 - z1)
rad = np.radians(ang)
head2 = grip2 + np.stack([ln * np.cos(rad), ln * np.sin(rad)], 1)  # punta del palo en el video (px, cuadro ref)
vec = np.stack([k * ln * np.cos(rad), -k * ln * np.sin(rad), dzr * Lm], 1)
vec = vec / np.linalg.norm(vec, axis=1, keepdims=True)
vec = lowpass(vec, 0.5); vec /= np.linalg.norm(vec, axis=1, keepdims=True)
head3 = grip3 + Lm * vec
# en el address el palo esta apoyado en la pelota
for t in range(0, ref + 6):
    w = 1.0 if t <= ref else max(0.0, 1 - (t - ref) / 6)
    head3[t] = (1 - w) * head3[t] + w * (ball + np.array([-0.03, -0.02, 0]))
# en el impacto la cabeza del palo esta en la pelota: se corrige suave alrededor
for t in range(impact - 4, impact + 3):
    w = max(0.0, 1 - abs(t - impact) / 4)
    head3[t] = (1 - w) * head3[t] + w * (ball + np.array([-0.03, -0.02, 0]))
for t in list(range(0, ref + 1)):
    pass
butt3 = grip3 - 0.09 * (head3 - grip3) / np.linalg.norm(head3 - grip3, axis=1, keepdims=True)

# Momentos: tope = manos mas altas entre el inicio y el impacto.
hand_y = Y[:, [15, 16]].mean(1)
top = int(np.argmax(hand_y[ref:impact]) + ref)
speed = np.linalg.norm(np.diff(grip3, axis=0), axis=1)
start = ref + int(np.argmax(speed[ref:] > 0.004))
fin = impact + int(np.argmax(hand_y[impact:impact + 90]))
data = {
    "fps": fps, "k_m_por_px": k, "largo_palo_m": Lm, "piso_px": v_floor, "u0_px": u0,
    "eventos": {"address": ref, "inicio": start, "tope": top, "impacto": impact, "final": fin},
    "ball": ball.round(4).tolist(),
    "huesos_m": {f"{a}-{b}": round(v, 3) for (a, b), v in blen.items()},
    "frames": [{"j": J[t].round(4).tolist(), "grip": grip3[t].round(4).tolist(),
                "head": head3[t].round(4).tolist(), "butt": butt3[t].round(4).tolist(),
                "h2": head2[t].round(1).tolist(), "g2": grip2[t].round(1).tolist(),
                "p2": P2s[t].round(1).tolist()} for t in range(n)],
}
json.dump(data, open(out, "w"))
print(f"escala {k*1000:.2f} mm/px; palo {Lm:.2f} m; altura aprox {(Y[ref].max()-0)*1.0:.2f} m (nariz)")
print("eventos", data["eventos"])
print("huesos", {kk: v for kk, v in list(data["huesos_m"].items())[:8]})
