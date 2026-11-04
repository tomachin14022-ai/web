"""Hojas con grilla en pixeles reales para marcar el palo a ojo (videos HD).
Uso: python -I grid_hd.py VIDEO SALIDA.jpg CUADROS X0 Y0 X1 Y1 [escala]"""
import sys
import cv2
import numpy as np
video, out, ids = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(",")]
x0, y0, x1, y1 = map(int, sys.argv[4:8]); sc = float(sys.argv[8]) if len(sys.argv) > 8 else 0.6
cap = cv2.VideoCapture(video); fr = []
while True:
    ok, f = cap.read()
    if not ok:
        break
    fr.append(f)
tiles = []
for i in ids:
    c = cv2.resize(fr[i][y0:y1, x0:x1], None, fx=sc, fy=sc, interpolation=cv2.INTER_AREA)
    for x in range((x0 // 50 + 1) * 50, x1, 50):
        X = int((x - x0) * sc); cv2.line(c, (X, 0), (X, c.shape[0]), (255, 255, 255) if x % 100 == 0 else (160, 160, 160), 1)
        if x % 100 == 0:
            cv2.putText(c, str(x), (X + 2, 14), cv2.FONT_HERSHEY_SIMPLEX, .42, (0, 0, 255), 1)
    for y in range((y0 // 50 + 1) * 50, y1, 50):
        Y = int((y - y0) * sc); cv2.line(c, (0, Y), (c.shape[1], Y), (255, 255, 255) if y % 100 == 0 else (160, 160, 160), 1)
        if y % 100 == 0:
            cv2.putText(c, str(y), (2, Y - 3), cv2.FONT_HERSHEY_SIMPLEX, .42, (0, 0, 255), 1)
    cv2.putText(c, f"f{i}", (c.shape[1] - 70, 30), cv2.FONT_HERSHEY_SIMPLEX, .9, (0, 255, 255), 2)
    tiles.append(c)
cv2.imwrite(out, np.hstack(tiles))
