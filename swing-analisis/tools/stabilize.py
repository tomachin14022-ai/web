"""Compensa el zoom y el paneo de la camara usando el fondo (no la persona).

Uso: python -I stabilize.py VIDEO POSE.npz REF_CUADRO SALIDA.npz
Calcula, para cada cuadro, la transformacion (escala + giro + traslado) que lo lleva
a las coordenadas del cuadro de referencia (el address). Asi las lineas de referencia
quedan fijas al piso aunque la camara se mueva.
Guarda A (n,2,3): punto_ref = A @ [x, y, 1].
"""
import sys

import cv2
import numpy as np

video, pose_path, ref, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
P = np.load(pose_path)
masks = P["mask"]
cap = cv2.VideoCapture(video)
grays = []
while True:
    ok, f = cap.read()
    if not ok:
        break
    grays.append(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY))
n = len(grays)
kernel = np.ones((25, 25), np.uint8)

def bg_mask(i):
    person = cv2.dilate((masks[i] > 60).astype(np.uint8), kernel)  # persona + margen (y el palo cerca)
    m = (1 - person) * 255
    return m.astype(np.uint8)

# Transformacion de cada cuadro al anterior (flujo optico de puntos del fondo).
step = [np.eye(3)]
inl = [1.0]
for i in range(1, n):
    p0 = cv2.goodFeaturesToTrack(grays[i - 1], 400, 0.01, 6, mask=bg_mask(i - 1))
    p1, st, _ = cv2.calcOpticalFlowPyrLK(grays[i - 1], grays[i], p0, None, winSize=(21, 21), maxLevel=3)
    good = st.ravel() == 1
    M, inliers = cv2.estimateAffinePartial2D(p1[good], p0[good], method=cv2.RANSAC, ransacReprojThreshold=1.5)
    T = np.eye(3); T[:2] = M
    step.append(T)
    inl.append(float(inliers.mean()))

# Acumular: cuadro i -> cuadro ref.
A = [None] * n
A[ref] = np.eye(3)
for i in range(ref + 1, n):
    A[i] = A[i - 1] @ step[i]
for i in range(ref - 1, -1, -1):
    A[i] = A[i + 1] @ np.linalg.inv(step[i + 1])
A = np.array([a[:2] for a in A])
scale = np.sqrt(np.abs(np.linalg.det(A[:, :, :2])))
np.savez(out, A=A, inliers=np.array(inl))
print(f"cuadros {n}; escala min {scale.min():.3f} max {scale.max():.3f}; "
      f"traslado x {A[:,0,2].min():.1f}..{A[:,0,2].max():.1f} y {A[:,1,2].min():.1f}..{A[:,1,2].max():.1f}; "
      f"inliers medio {np.mean(inl):.2f}, min {np.min(inl):.2f}")
