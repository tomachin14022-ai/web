"""Mejora la definicion del video x4 (Real-ESRGAN general v3, corre en CPU).

Uso: python -I upscale.py VIDEO PESOS.pth CARPETA DESDE HASTA
Solo hace falta para videos chicos (como el de prueba). Con videos HD del espectador
no se usa. No cambia la forma del cuerpo: solo recupera nitidez.
"""
import os
import sys

import cv2
import numpy as np
import torch
from torch import nn
from torch.nn import functional as F

video, weights, out, a, b = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])

class SRVGGNetCompact(nn.Module):
    def __init__(self, nf=64, nc=32, up=4):
        super().__init__()
        self.up = up
        body = [nn.Conv2d(3, nf, 3, 1, 1), nn.PReLU(nf)]
        for _ in range(nc):
            body += [nn.Conv2d(nf, nf, 3, 1, 1), nn.PReLU(nf)]
        body += [nn.Conv2d(nf, 3 * up * up, 3, 1, 1)]
        self.body = nn.ModuleList(body)
        self.ps = nn.PixelShuffle(up)

    def forward(self, x):
        o = x
        for m in self.body:
            o = m(o)
        return self.ps(o) + F.interpolate(x, scale_factor=self.up, mode="nearest")

net = SRVGGNetCompact()
sd = torch.load(weights, map_location="cpu")
sd = sd.get("params_ema", sd.get("params", sd))
net.load_state_dict(sd); net.eval()
torch.set_num_threads(os.cpu_count())
os.makedirs(out, exist_ok=True)
cap = cv2.VideoCapture(video); i = 0
with torch.no_grad():
    while True:
        ok, f = cap.read()
        if not ok or i >= b:
            break
        if i >= a and not os.path.exists(f"{out}/{i:04d}.png"):
            x = torch.from_numpy(cv2.cvtColor(f, cv2.COLOR_BGR2RGB)).float().permute(2, 0, 1)[None] / 255
            y = net(x).clamp(0, 1)[0].permute(1, 2, 0).numpy()
            cv2.imwrite(f"{out}/{i:04d}.png", cv2.cvtColor((y * 255).round().astype(np.uint8), cv2.COLOR_RGB2BGR))
        i += 1
print("listo", a, b)
