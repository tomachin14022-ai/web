"""Detecta la pelota (en el address) y la varilla del palo en cada cuadro.

Uso: python -I club_detect.py VIDEO POSE.npz REF_CUADRO SALIDA.npz
La varilla se busca como una linea oscura que sale de las manos: para cada angulo se
mide el contraste a lo largo del rayo y despues se elige el recorrido de angulos mas
coherente en el tiempo (programacion dinamica). Donde la varilla no se ve (borrosa o
delante de la ropa) el angulo sale de la continuidad: marcarlo como estimado.
Guarda: ball (x,y) en el cuadro de referencia, ang (n,) en grados, conf (n,), grip (n,2), head (n,2).
"""
import sys

import cv2
import numpy as np

video, pose_path, ref, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
P = np.load(pose_path)
lm, masks = P["lm"], P["mask"]
cap = cv2.VideoCapture(video)
G = []
while True:
    ok, f = cap.read()
    if not ok:
        break
    G.append(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY).astype(np.float32))
n, (h, w) = len(G), G[0].shape

# Agarre: entre las munecas y los nudillos (indices).
grip = (lm[:, 15, :2] + lm[:, 16, :2] + lm[:, 19, :2] + lm[:, 20, :2]) / 4
body_h = np.linalg.norm(lm[ref, 0, :2] - (lm[ref, 27, :2] + lm[ref, 28, :2]) / 2) * 1.08
L = 0.62 * body_h  # largo aproximado de un driver en pixeles (se corrige con la pelota)

# Pelota: mancha blanca chica en la mitad de abajo del cuadro de referencia, fuera de la persona.
f = cv2.imread  # noqa (solo para que el lector vea que usamos gris)
g = G[ref]
cand = ((g > 200) & (masks[ref] < 60)).astype(np.uint8)
cand[: h // 2] = 0
num, lab, stats, cent = cv2.connectedComponentsWithStats(cand)
best, ball = 1e9, None
for k in range(1, num):
    a = stats[k, cv2.CC_STAT_AREA]
    if 4 <= a <= 120:
        d = np.linalg.norm(cent[k] - grip[ref])
        if d < best:
            best, ball = d, cent[k]
if ball is not None:
    L = float(np.linalg.norm(ball - grip[ref]))  # en el address el palo llega a la pelota
print("pelota", None if ball is None else ball.round(1), "largo palo px", round(L, 1))

ANG = np.arange(0, 360, 2.0)
rs = np.linspace(0.12, 0.55, 22) * L

def score_frame(i):
    gi, mi = G[i], masks[i]
    gx = cv2.GaussianBlur(gi, (3, 3), 0)
    sc = np.zeros(len(ANG))
    for k, a in enumerate(np.radians(ANG)):
        d = np.array([np.cos(a), np.sin(a)]); nrm = np.array([-d[1], d[0]])
        pts = grip[i] + rs[:, None] * d
        side1, side2 = pts + 3.5 * nrm, pts - 3.5 * nrm
        ok = (pts[:, 0] > 2) & (pts[:, 0] < w - 3) & (pts[:, 1] > 2) & (pts[:, 1] < h - 3)
        ok &= (side1[:, 0] > 2) & (side1[:, 0] < w - 3) & (side2[:, 0] > 2) & (side2[:, 0] < w - 3)
        ok &= (side1[:, 1] > 2) & (side1[:, 1] < h - 3) & (side2[:, 1] > 2) & (side2[:, 1] < h - 3)
        if ok.sum() < 6:
            continue
        p, s1, s2 = pts[ok].astype(int), side1[ok].astype(int), side2[ok].astype(int)
        on_body = mi[p[:, 1], p[:, 0]] > 120
        if (~on_body).sum() < 5:
            continue
        # linea fina: mas oscura que los DOS costados (un borde del horizonte no cuenta)
        c = np.minimum(gx[s1[:, 1], s1[:, 0]], gx[s2[:, 1], s2[:, 0]]) - gx[p[:, 1], p[:, 0]]
        c = np.clip(c[~on_body], 0, 60)
        sc[k] = c.mean() * min(1.0, (~on_body).sum() / 10)
    return sc

S = np.array([score_frame(i) for i in range(n)])
# Viterbi: maximiza contraste menos un costo por cambiar de angulo de golpe.
lam, maxstep = 0.25, 30
dif = np.abs(((ANG[:, None] - ANG[None, :]) + 180) % 360 - 180)
trans = -lam * dif - np.where(dif > maxstep, 1e3, 0)
V = S[0].copy(); back = np.zeros((n, len(ANG)), int)
for i in range(1, n):
    tot = V[None, :] + trans  # [actual, previo]
    back[i] = tot.argmax(1)
    V = tot.max(1) + S[i]
path = np.zeros(n, int); path[-1] = V.argmax()
for i in range(n - 1, 0, -1):
    path[i - 1] = back[i, path[i]]
ang = ANG[path]
conf = S[np.arange(n), path]
a = np.radians(ang)
head = grip + L * np.stack([np.cos(a), np.sin(a)], 1)  # punta si el palo se viera entero (sin escorzo)
np.savez(out, ball=np.array(ball if ball is not None else [np.nan, np.nan]), L=L, ang=ang, conf=conf,
         grip=grip, head=head, score=S)
print("confianza media %.1f; cuadros con varilla poco visible (<4): %d" % (conf.mean(), (conf < 4).sum()))

# --- Correcciones manuales y punta del palo -------------------------------------------
# Uso extra: python -I club_detect.py VIDEO POSE.npz REF SALIDA.npz CORRECCIONES.json
# CORRECCIONES.json: {"cuadro": angulo_grados, ...} marcado a ojo donde la varilla esta
# tapada por el cuerpo. Entre correcciones cercanas se interpola.
if len(sys.argv) > 5:
    import json
    fix = {int(k): float(v) for k, v in json.load(open(sys.argv[5])).items()}
    ks = sorted(fix)
    for k in ks:
        ang[k] = fix[k]; conf[k] = 99.0
    # interpolar entre correcciones consecutivas que esten a <= 8 cuadros
    for a0, a1 in zip(ks[:-1], ks[1:]):
        if a1 - a0 <= 8:
            d = ((fix[a1] - fix[a0] + 180) % 360) - 180
            for k in range(a0 + 1, a1):
                ang[k] = (fix[a0] + d * (k - a0) / (a1 - a0)) % 360; conf[k] = 50.0

# Punta: recorrer el rayo y quedarse con el ultimo tramo oscuro (varilla o cabeza del palo).
tip = np.full(n, np.nan)
for i in range(n):
    a = np.radians(ang[i]); d = np.array([np.cos(a), np.sin(a)]); nrm = np.array([-d[1], d[0]])
    rr = np.arange(4, 1.15 * L, 1.0)
    pts = grip[i] + rr[:, None] * d
    ok = (pts[:, 0] > 4) & (pts[:, 0] < w - 5) & (pts[:, 1] > 4) & (pts[:, 1] < h - 5)
    if ok.sum() < 10:
        continue
    gx = cv2.GaussianBlur(G[i], (3, 3), 0)
    prof = np.zeros(len(rr)); body = np.zeros(len(rr), bool)
    for k in np.where(ok)[0]:
        p = pts[k]; s1 = np.clip(p + 4 * nrm, 0, [w - 1, h - 1]); s2 = np.clip(p - 4 * nrm, 0, [w - 1, h - 1])
        prof[k] = min(gx[int(s1[1]), int(s1[0])], gx[int(s2[1]), int(s2[0])]) - gx[int(p[1]), int(p[0])]
        body[k] = masks[i][int(p[1]), int(p[0])] > 120
    prof = np.convolve(prof, np.ones(5) / 5, "same")
    good = (prof > 6) & ~body & ok
    if good.sum() >= 6:
        tip[i] = rr[np.where(good)[0].max()]
np.savez(out, ball=np.array(ball if ball is not None else [np.nan, np.nan]), L=L, ang=ang, conf=conf,
         grip=grip, tip=tip, score=S)
print("puntas detectadas:", int(np.isfinite(tip).sum()), "de", n)
