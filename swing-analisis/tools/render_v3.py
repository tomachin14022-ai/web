"""Panel del video para el reel profesional (sin 3D).

Uso: python -I render_v3.py CONFIG.json CARPETA_SALIDA [desde hasta]
CONFIG.json: {"video", "up_dir", "stab", "pose", "swing3d", "metrics", "fmetrics", "timeline"}
Dibuja a 2x (1520x2060) y entrega 760x1030. Modos: "single" (vista con zoom opcional) y
"compare" (P1 | P7 lado a lado). Todo lo que se dibuja vive en coordenadas del cuadro de
referencia (video estabilizado), asi las lineas quedan pegadas al piso.
"""
import json
import math
import os
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

C = json.load(open(sys.argv[1])); outdir = sys.argv[2]
rng = (int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else None
A = np.load(C["stab"])["A"]; PZ = np.load(C["pose"]); MASK = PZ["mask"]
S3 = json.load(open(C["swing3d"])); M = json.load(open(C["metrics"])); FM = json.load(open(C["fmetrics"]))
TL = json.load(open(C["timeline"]))
F3 = S3["frames"]; PP = FM["P"]; P1, P7 = PP["P1"], PP["P7"]
os.makedirs(outdir, exist_ok=True)
W2, H2 = 1520, 2060
SRC_W, SRC_H = 354, 492

cap = cv2.VideoCapture(C["video"]); raw = []
while True:
    ok, f = cap.read()
    if not ok:
        break
    raw.append(f)

_cache = {}
def hires(i):
    """Cuadro x4 (mejorado si existe; si no, bicubico)."""
    if i in _cache:
        return _cache[i]
    p = f"{C['up_dir']}/{i:04d}.png"
    im = cv2.imread(p) if os.path.exists(p) else cv2.resize(raw[i], (SRC_W * 4, SRC_H * 4), interpolation=cv2.INTER_CUBIC)
    if len(_cache) > 12:
        _cache.clear()
    _cache[i] = im
    return im

def view_mat(view, w_out, h_out):
    x0, y0, w = view; s = w_out / w
    return np.array([[s, 0, -x0 * s], [0, s, -y0 * s], [0, 0, 1.0]])

def frame_img(i, view, w_out, h_out):
    Ai = np.vstack([A[i], [0, 0, 1]])
    S4 = np.diag([0.25, 0.25, 1.0])  # x4 -> src
    Mx = view_mat(view, w_out, h_out) @ Ai @ S4
    im = cv2.warpAffine(hires(i), Mx[:2], (w_out, h_out), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return im

def mask_img(i, view, w_out, h_out):
    Mx = view_mat(view, w_out, h_out) @ np.vstack([A[i], [0, 0, 1]])
    return cv2.warpAffine(MASK[i], Mx[:2], (w_out, h_out), flags=cv2.INTER_LINEAR)

def grade(im):
    im = cv2.convertScaleAbs(im, alpha=1.07, beta=-8)
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV).astype(np.float32); hsv[..., 1] *= 1.12
    im = cv2.cvtColor(np.clip(hsv, 0, 255).astype(np.uint8), cv2.COLOR_HSV2BGR)
    h, w = im.shape[:2]; yy, xx = np.mgrid[0:h, 0:w]
    v = 1 - 0.10 * (((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2) ** 1.6
    return (im * np.clip(v, 0.82, 1)[..., None]).astype(np.uint8)

FONT_B = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
f_lbl = ImageFont.truetype(FONT_B, 50); f_big = ImageFont.truetype(FONT_B, 60); f_tag = ImageFont.truetype(FONT_B, 46)
WHITE, CYAN, LIME, RED, YEL, INK, WOOD = (255, 255, 255), (63, 208, 255), (201, 242, 107), (255, 77, 109), (255, 210, 63), (13, 19, 16), (138, 90, 59)
bgr = lambda c: (c[2], c[1], c[0])
ease = lambda x: 1 - (1 - min(1.0, max(0.0, x))) ** 3
EDGES = [(11, 12), (11, 13), (13, 15), (12, 14), (14, 16), (15, 17), (15, 19), (15, 21), (17, 19), (16, 18), (16, 20), (16, 22), (18, 20),
         (11, 23), (12, 24), (23, 24), (23, 25), (25, 27), (24, 26), (26, 28), (27, 29), (29, 31), (27, 31), (28, 30), (30, 32), (28, 32), (7, 0), (8, 0)]
JOINTS = [0, 7, 8, 11, 12, 13, 14, 15, 16, 19, 20, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]

cola = M["series"]["cola_x"]; c0 = M["linea_cola_address_x"]
ball = M["plano"]["pelota"]; hands0 = M["plano"]["manos_address"]; sh0 = M["plano"]["hombro_der_address"]
p2a = np.array(F3[P1]["p2"]); hip0 = (p2a[23] + p2a[24]) / 2; shm0 = (p2a[11] + p2a[12]) / 2
floor_y = S3["piso_px"]; k_cm = S3["k_m_por_px"] * 100
ear0 = (p2a[7] + p2a[8]) / 2

# silueta del address (contorno suave) en coords ref
m0 = cv2.warpAffine(MASK[P1], A[P1], (SRC_W, SRC_H))
m0b = cv2.GaussianBlur(cv2.resize(m0, (SRC_W * 4, SRC_H * 4), interpolation=cv2.INTER_LINEAR), (0, 0), 3)
cnts, _ = cv2.findContours((m0b > 128).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
GHOST = max(cnts, key=cv2.contourArea)[:, 0, :].astype(float) / 4.0
head_top0 = float(GHOST[:, 1].min())

def ext(a, b, k):
    return (a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k)

class Canvas:
    def __init__(self, img, view):
        self.img = img; self.view = view; self.s = img.shape[1] / view[2]; self.labels = []
    def P(self, x, y):
        return ((x - self.view[0]) * self.s, (y - self.view[1]) * self.s)
    def line(self, a, b, col, th, prog=1.0, dashed=False, outline=True, alpha=1.0):
        a, b = np.array(a, float), np.array(b, float); b = a + (b - a) * prog
        if dashed:
            L = np.linalg.norm(b - a); n = max(1, int(L / 28))
            for k in range(0, n, 2):
                self.line(a + (b - a) * k / n, a + (b - a) * min(1, (k + 1) / n), col, th, 1.0, False, outline, alpha)
            return
        pa, pb = tuple(np.round(a).astype(int)), tuple(np.round(b).astype(int))
        tgt = self.img if alpha >= 1 else self.img.copy()
        if outline:
            cv2.line(tgt, pa, pb, bgr(INK), th + 5, cv2.LINE_AA)
        cv2.line(tgt, pa, pb, bgr(col), th, cv2.LINE_AA)
        if alpha < 1:
            cv2.addWeighted(tgt, alpha, self.img, 1 - alpha, 0, self.img)
    def arrow(self, a, b, col, th=7):
        a = tuple(map(int, a)); b = tuple(map(int, b))
        if np.hypot(b[0] - a[0], b[1] - a[1]) < 6:
            return
        cv2.arrowedLine(self.img, a, b, bgr(INK), th + 6, cv2.LINE_AA, tipLength=0.3)
        cv2.arrowedLine(self.img, a, b, bgr(col), th, cv2.LINE_AA, tipLength=0.3)
    def ring(self, c, r, col, th=6):
        cv2.circle(self.img, tuple(map(int, c)), int(r), bgr(INK), th + 5, cv2.LINE_AA)
        cv2.circle(self.img, tuple(map(int, c)), int(r), bgr(col), th, cv2.LINE_AA)
    def fill(self, mask_bool, col, alpha):
        ov = self.img.copy(); ov[mask_bool] = bgr(col)
        cv2.addWeighted(ov, alpha, self.img, 1 - alpha, 0, self.img)
    def pill(self, text, x, y, bg, fg=INK, a=1.0, big=False):
        self.labels.append((text, x, y, bg, fg, a, big))
    def finish(self):
        if not self.labels:
            return self.img
        im = Image.fromarray(cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)).convert("RGBA")
        lay = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        for text, x, y, bg, fg, a, big in self.labels:
            if a <= 0.01:
                continue
            fnt = f_big if big else f_lbl
            bb = d.textbbox((0, 0), text, font=fnt); tw, th = bb[2] - bb[0], bb[3] - bb[1]
            px, py = 24, 15
            x = min(max(x, 14), im.size[0] - tw - 2 * px - 14); y = min(max(y, 14), im.size[1] - th - 2 * py - 20)
            d.rounded_rectangle([x, y, x + tw + 2 * px, y + th + 2 * py + 6], radius=(th + 2 * py) // 2, fill=bg + (int(240 * a),))
            d.text((x + px, y + py - bb[1] + 3), text, font=fnt, fill=fg + (int(255 * a),))
        im = Image.alpha_composite(im, lay)
        return cv2.cvtColor(np.array(im.convert("RGB")), cv2.COLOR_RGB2BGR)

def chair_poly():
    """Silla dibujada detras de la cola (coords ref)."""
    hy = hip0[1]; x = c0 + 1.0
    back = [(x - 8, hy - 30), (x, hy - 30), (x, hy + 62), (x - 8, hy + 62)]
    seat = [(x - 78, hy + 58), (x, hy + 58), (x, hy + 68), (x - 78, hy + 68)]
    legs = [[(x - 6, hy + 66), (x - 1, hy + 66), (x - 1, floor_y - 6), (x - 6, floor_y - 6)],
            [(x - 76, hy + 66), (x - 71, hy + 66), (x - 71, floor_y - 18), (x - 76, floor_y - 18)]]
    return [back, seat] + legs

def draw_scene(cv, i, t, Lset, starts, side="single"):
    """Dibuja las capas activas sobre un lienzo."""
    st = lambda n: (t - starts[n]) if n in starts else 0.0
    p2 = np.array(F3[i]["p2"]); P = cv.P
    H, W = cv.img.shape[:2]
    if "chair" in Lset:
        g = ease(st("chair") / 0.35)
        ov = cv.img.copy()
        for poly in chair_poly():
            pts = np.array([P(*q) for q in poly], np.int32)
            cv2.fillPoly(ov, [pts], bgr(WOOD)); cv2.polylines(ov, [pts], True, bgr((70, 44, 28)), 3, cv2.LINE_AA)
        base = cv.img.copy()
        cv2.addWeighted(ov, g, cv.img, 1 - g, 0, cv.img)
        # la persona va delante de la silla: se repinta encima con su silueta
        mk = cv2.GaussianBlur(mask_img(i, cv.view, W, H), (0, 0), 1.5).astype(np.float32)[..., None] / 255
        cv.img[:] = (base * mk + cv.img * (1 - mk)).astype(np.uint8)
    if "plane" in Lset:
        g = ease(st("plane") / 0.5)
        A1 = P(*ball); B1 = P(*ext(ball, hands0, 3.2)); B2 = P(*ext(ball, sh0, 2.6))
        ov = cv.img.copy(); cv2.fillPoly(ov, [np.array([A1, ext(A1, B1, g), ext(A1, B2, g)], np.int32)], bgr(CYAN))
        cv2.addWeighted(ov, 0.16, cv.img, 0.84, 0, cv.img)
        cv.line(A1, B1, CYAN, 5, g); cv.line(A1, B2, CYAN, 5, g)
    if "ghost" in Lset and i != P1:
        g = ease(st("ghost") / 0.4)
        pts = np.array([P(x, y) for x, y in GHOST], np.int32)
        ov = cv.img.copy(); cv2.fillPoly(ov, [pts], bgr(CYAN)); cv2.addWeighted(ov, 0.10 * g, cv.img, 1 - 0.10 * g, 0, cv.img)
        ov = cv.img.copy(); cv2.polylines(ov, [pts], True, bgr(CYAN), 5, cv2.LINE_AA); cv2.addWeighted(ov, 0.95 * g, cv.img, 1 - 0.95 * g, 0, cv.img)
    if "gapfill" in Lset and i != P1:
        g = ease(st("gapfill") / 0.4)
        m_a = cv2.warpAffine(mask_img(P1, (0, 0, SRC_W), SRC_W, SRC_H), np.eye(3)[:2], (SRC_W, SRC_H))
        m_c = cv2.warpAffine(MASK[i], A[i], (SRC_W, SRC_H))
        band = np.zeros_like(m_a, bool); band[int(hip0[1] - 45): int(hip0[1] + 75), : int(hip0[0] + 5)] = True
        gap = ((m_a > 128) & (m_c < 100) & band).astype(np.uint8) * 255
        Mv = view_mat(cv.view, W, H)
        gv = cv2.warpAffine(gap, Mv[:2], (W, H), flags=cv2.INTER_LINEAR) > 100
        cv.fill(gv, RED, 0.55 * g)
    if "butt" in Lset:
        g = ease(st("butt") / 0.45); col = LIME if "butt_lime" in Lset else RED
        cv.line(P(c0, floor_y), P(c0, hip0[1] - 100), col, 6, g)
    if "headline" in Lset:
        g = ease(st("headline") / 0.4)
        y = P(0, head_top0)[1]; xa = P(ear0[0] - 70, 0)[0]; xb = P(ear0[0] + 70, 0)[0]
        cv.line((xa, y), (xa + (xb - xa) * g, y), CYAN, 4, dashed=True)
    if "spine_ref" in Lset:
        g = ease(st("spine_ref") / 0.45)
        cv.line(P(*hip0), P(*ext(hip0, shm0, 1.55)), CYAN, 6, g)
    if "spine_live" in Lset:
        hp = (p2[23] + p2[24]) / 2; sm = (p2[11] + p2[12]) / 2
        cv.line(P(*hp), P(*ext(hp, sm, 1.45)), WHITE, 5, dashed=True)
    if "tracer" in Lset and i >= PP["P4"] - 2:
        pts = [P(*F3[j]["h2"]) for j in range(PP["P4"] - 2, i + 1)]
        for a, b in zip(pts, pts[1:]):
            cv2.line(cv.img, tuple(map(int, a)), tuple(map(int, b)), bgr(YEL), 8, cv2.LINE_AA)
        if pts:
            cv2.circle(cv.img, tuple(map(int, pts[-1])), 12, bgr(YEL), -1, cv2.LINE_AA)
    if "skel" in Lset:
        q = [P(*p2[j]) for j in range(33)]
        ov = cv.img.copy()
        for a, b in EDGES:
            cv2.line(ov, tuple(map(int, q[a])), tuple(map(int, q[b])), bgr(INK), 8, cv2.LINE_AA)
            cv2.line(ov, tuple(map(int, q[a])), tuple(map(int, q[b])), bgr(WHITE), 3, cv2.LINE_AA)
        for j in JOINTS:
            r = 7 if j in (0, 7, 8, 19, 20, 29, 30, 31, 32) else 9
            cv2.circle(ov, tuple(map(int, q[j])), r + 3, bgr(INK), -1, cv2.LINE_AA)
            cv2.circle(ov, tuple(map(int, q[j])), r, bgr(WHITE), -1, cv2.LINE_AA)
        cv2.addWeighted(ov, 0.92, cv.img, 0.08, 0, cv.img)
    if "knee" in Lset:
        g = ease(st("knee") / 0.3)
        hpj, kn, an = p2[24], p2[26], p2[28]
        a1 = math.degrees(math.atan2(hpj[1] - kn[1], hpj[0] - kn[0])); a2 = math.degrees(math.atan2(an[1] - kn[1], an[0] - kn[0]))
        c = P(*kn); r = 46
        lo, hi = sorted([a1, a2])
        if hi - lo > 180:
            lo, hi = hi, lo + 360
        cv2.ellipse(cv.img, tuple(map(int, c)), (r, r), 0, lo, lo + (hi - lo) * g, bgr(INK), 13, cv2.LINE_AA)
        cv2.ellipse(cv.img, tuple(map(int, c)), (r, r), 0, lo, lo + (hi - lo) * g, bgr(YEL), 7, cv2.LINE_AA)
        cv.pill(f"{FM['frames'][i]['rodilla_atras']}°", c[0] + 56, c[1] - 30, YEL, INK, g)
    if "heel" in Lset:
        g = ease(st("heel") / 0.3)
        hl = P(*p2[30]); fl = P(p2[30][0], F3[P1]["p2"][30][1])
        cv.line((fl[0] - 70, fl[1]), (fl[0] + 70, fl[1]), CYAN, 4, dashed=True)
        cv.arrow((hl[0] - 28, fl[1] - 4), (hl[0] - 28, hl[1] + 2), RED, 7)
        cv.pill(f"TALÓN +{FM['frames'][i]['talon_atras_cm']:.0f} cm", hl[0] - 330, hl[1] - 90, RED, WHITE, g)
    if "butt_arrow" in Lset:
        g = ease(st("butt_arrow") / 0.4)
        y = P(0, hip0[1] + 8)[1]; x0 = P(c0, 0)[0]; x1 = P(cola[i], 0)[0]
        cv.arrow((x0, y), (x0 + (x1 - x0) * g, y), RED, 8)
        cv.pill(f"+{FM['frames'][i]['cola_cm']:.1f} cm".replace(".", ","), x0 - 60, y + 36, RED, WHITE, g)
    if "target" in Lset:
        g = ease(st("target") / 0.5)
        y = P(0, hip0[1] + 8)[1]; x0 = P(c0, 0)[0]; x1 = P(cola[i], 0)[0]
        cv.arrow((x1, y + 34), (x1 + (x0 - x1) * g, y + 34), LIME, 8)
        cv.pill("COLA HACIA ATRÁS", x0 + 40, y + 150, LIME, INK, g)
    if "glute_ring" in Lset:
        g = ease(st("glute_ring") / 0.3); s_ = st("glute_ring")
        c = P(c0 + 9, hip0[1] + 10); cv.ring(c, (44 + 6 * math.sin(s_ * 8)) * (0.6 + 0.4 * g), LIME, 6)
        cv.pill("GLÚTEO IZQ. EN LA LÍNEA", c[0] + 30, c[1] - 250, LIME, INK, g)
    if "chair_gap" in Lset:
        g = ease(st("chair_gap") / 0.3)
        xa, xb = P(c0 + 1, 0)[0], P(cola[i], 0)[0]; ya, yb = P(0, hip0[1] - 25)[1], P(0, hip0[1] + 55)[1]
        if xb - xa > 4:
            ov = cv.img.copy(); cv2.rectangle(ov, (int(xa), int(ya)), (int(xb), int(yb)), bgr(RED), -1)
            cv2.addWeighted(ov, 0.65 * g, cv.img, 1 - 0.65 * g, 0, cv.img)
        cv.pill("SE DESPEGÓ", xa - 40, ya - 90, RED, WHITE, g)
    if "contact" in Lset:
        g = ease(st("contact") / 0.3)
        c = P(c0, hip0[1] + 10); cv2.circle(cv.img, tuple(map(int, c)), int(14 * g) + 1, bgr(LIME), -1, cv2.LINE_AA)
        cv.pill("✓ CONTACTO", c[0] + 30, c[1] - 30, LIME, INK, g)
    # etiquetas de "lo bueno"
    for name, text, anchor in [("ok_postura", "✓ POSTURA · 32°", "spine"), ("ok_subida", "✓ MANTIENE 30°", "spine"), ("ok_plano", "✓ EN PLANO · 50°", "plane"),
                               ("lbl_spine_imp", "24°  (P1: 32°)  −8°", "spine"), ("lbl_agacha", "SE AGACHA", "head"), ("lbl_sube", "SE LEVANTA", "spine")]:
        if name in Lset:
            g = ease(st(name) / 0.3)
            if anchor == "spine":
                c = P(*ext(hip0, shm0, 1.3)); x, y = c[0] - 380, c[1] - 60
            elif anchor == "plane":
                c = P(*ext(ball, hands0, 1.7)); x, y = c[0] + 10, c[1] - 140
            else:
                c = P(ear0[0], head_top0); x, y = c[0] + 60, c[1] - 90
            red = name in ("lbl_spine_imp", "lbl_agacha", "lbl_sube")
            cv.pill(text, x, y, RED if red else LIME, WHITE if red else INK, g)

frames = TL["frames"]
ks = range(len(frames)) if rng is None else range(rng[0], min(rng[1], len(frames)))
for k in ks:
    fr = frames[k]; t = fr["t"]; i = int(round(fr["src"])); Lset = set(fr["L"]); starts = fr["starts"]
    if fr["mode"] == "compare":
        half = W2 // 2; view = (55.0, 0.0, 354 * 0.5)
        out = np.zeros((H2, W2, 3), np.uint8)
        for side, fi in (("a", P1), ("b", P7)):
            im = grade(frame_img(fi, view, half, H2)); cv = Canvas(im, view)
            L2 = set(x for x in Lset if not x.startswith("b_")) if side == "a" else set(x[2:] for x in Lset if x.startswith("b_"))
            draw_scene(cv, fi, t, L2 | {"skel"}, {k2[2:] if k2.startswith("b_") else k2: v for k2, v in starts.items()})
            img = cv.finish()
            # titulo de cada mitad
            pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)); d = ImageDraw.Draw(pil)
            lab = "P1 · ADDRESS" if side == "a" else "P7 · IMPACTO"; bg = (12, 18, 15)
            bb = d.textbbox((0, 0), lab, font=f_tag); d.rounded_rectangle([24, 1700, 24 + bb[2] + 40, 1700 + bb[3] + 30], radius=34, fill=bg)
            d.text((44, 1710), lab, font=f_tag, fill=(201, 242, 107) if side == "a" else (255, 77, 109))
            img = cv2.cvtColor(np.array(pil), cv2.COLOR_RGB2BGR)
            out[:, (0 if side == "a" else half):(half if side == "a" else W2)] = img
        cv2.line(out, (half, 0), (half, H2), (16, 19, 13), 8)
        img = out
    else:
        view = tuple(fr["view"])
        im = grade(frame_img(i, view, W2, H2)); cv = Canvas(im, view)
        draw_scene(cv, i, t, Lset, starts)
        img = cv.finish()
    cv2.imwrite(os.path.join(outdir, f"{k:05d}.png"), cv2.resize(img, (W2 // 2, H2 // 2), interpolation=cv2.INTER_AREA))
print("listo", len(ks))
