"""Extrae la pose (MediaPipe Pose Landmarker) de cada cuadro de un video de swing.

Uso: python -I pose_extract.py VIDEO MODELO SALIDA.json
Guarda, por cuadro: landmarks 2D normalizados (x, y, z, visibilidad) y
landmarks "world" 3D en metros (origen en el centro de la cadera).
"""
import json
import sys

import cv2
import mediapipe as mp
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
)

cap = cv2.VideoCapture(video)
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frames = []
with vision.PoseLandmarker.create_from_options(opts) as lm:
    i = 0
    while True:
        ok, bgr = cap.read()
        if not ok:
            break
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
        img = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        res = lm.detect_for_video(img, int(i * 1000 / fps))
        f = {"i": i, "t": i / fps, "lm": None, "world": None}
        if res.pose_landmarks:
            f["lm"] = [[p.x, p.y, p.z, p.visibility] for p in res.pose_landmarks[0]]
            f["world"] = [[p.x, p.y, p.z] for p in res.pose_world_landmarks[0]]
        frames.append(f)
        i += 1

found = sum(1 for f in frames if f["lm"])
json.dump({"video": video, "fps": fps, "w": w, "h": h, "frames": frames}, open(out, "w"))
print(f"{len(frames)} cuadros, pose encontrada en {found} ({100*found/max(1,len(frames)):.0f} %), {w}x{h} @ {fps:.2f} fps")
