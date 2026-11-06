"""Extrae la pose (MediaPipe Pose Landmarker heavy) y la silueta de cada cuadro.

Uso: python -I pose_extract.py VIDEO MODELO SALIDA.npz
Guarda por cuadro:
  lm    (n,33,4) puntos 2D en pixeles + profundidad relativa + visibilidad
  world (n,33,3) puntos 3D en metros (origen en el centro de la cadera, y hacia abajo)
  mask  (n,h,w)  silueta de la persona (0-255)
"""
import sys

import cv2
import mediapipe as mp
import numpy as np
from mediapipe.tasks.python import BaseOptions
from mediapipe.tasks.python import vision

video, model, out = sys.argv[1:4]
opts = vision.PoseLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model),
    running_mode=vision.RunningMode.VIDEO,
    num_poses=1,
    min_pose_detection_confidence=0.5,
    min_pose_presence_confidence=0.5,
    min_tracking_confidence=0.5,
    output_segmentation_masks=True,
)
cap = cv2.VideoCapture(video)
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
w, h = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
LM, WO, MK, OK, TS = [], [], [], [], []  # TS: tiempo real de cada cuadro (ms); la cámara lenta del iPhone tiene fps variable
with vision.PoseLandmarker.create_from_options(opts) as det:
    i = 0
    while True:
        ok, bgr = cap.read()
        if not ok:
            break
        ts = cap.get(cv2.CAP_PROP_POS_MSEC)
        ts = ts if ts > 0 or i == 0 else i * 1000 / fps
        TS.append(ts)
        img = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB))
        r = det.detect_for_video(img, i)  # MediaPipe solo necesita un número creciente
        if r.pose_landmarks:
            LM.append([[p.x * w, p.y * h, p.z * w, p.visibility] for p in r.pose_landmarks[0]])
            WO.append([[p.x, p.y, p.z] for p in r.pose_world_landmarks[0]])
            MK.append((r.segmentation_masks[0].numpy_view() * 255).astype(np.uint8).reshape(h, w))
            OK.append(True)
        else:
            LM.append(np.full((33, 4), np.nan)); WO.append(np.full((33, 3), np.nan))
            MK.append(np.zeros((h, w), np.uint8)); OK.append(False)
        i += 1
np.savez_compressed(out, lm=np.array(LM, float), world=np.array(WO, float), mask=np.array(MK),
                    ok=np.array(OK), fps=fps, w=w, h=h, t_ms=np.array(TS, float))
print(f"{i} cuadros, pose en {sum(OK)} ({100*sum(OK)/max(1,i):.0f} %), {w}x{h} @ {fps:.2f} fps")
