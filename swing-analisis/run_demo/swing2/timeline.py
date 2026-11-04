"""Edicion del reel del swing 2 (video HD subido por el dueno). Tiempos = palabras alineadas de la voz.
Uso: python -I timeline_s2.py SWING3D.json POSICIONES.json SALIDA.json"""
import json
import sys

S3 = json.load(open(sys.argv[1])); PP = json.load(open(sys.argv[2])); out = sys.argv[3]
FPS, DUR = 30, 97.6
P = PP
FULL = (40.0, 260.0, 900.0)
hl = S3["frames"][P["P5"]]["p2"][30]
FEET = (hl[0] - 190, min(hl[1] - 300, 1920 - 380 * 1030 / 760), 380.0)
g4 = S3["frames"][P["P4"]]["g2"]
TOP = (g4[0] - 230, g4[1] - 260, 520.0)
g2 = S3["frames"][P["P2"]]["g2"]
P2Z = (g2[0] - 330, g2[1] - 380, 700.0)

SEG = [  # (t0, t1, src0, src1, modo)
    (0.00, 2.90, 0, 81, "single"), (2.90, 6.10, "strip", "strip", "single"),
    (6.10, 11.00, P["P1"], P["P1"], "single"),
    (11.00, 13.40, P["P1"], P["P1"], "single"), (13.40, 14.80, P["P1"], P["P7"], "single"), (14.80, 18.25, P["P7"], P["P7"], "single"),
    (18.25, 19.60, P["P4"], P["P5"], "single"), (19.60, 22.00, P["P5"], P["P6"], "single"), (22.00, 23.15, P["P6"], P["P6"], "single"),
    (23.15, 25.60, P["P7"], P["P7"], "single"), (25.60, 26.60, P["P7"], P["P10"], "single"), (26.60, 28.30, P["P10"], P["P10"], "single"),
    (28.30, 32.10, P["P1"], P["P1"], "single"), (32.10, 35.10, P["P1"], P["P4"], "single"), (35.10, 39.10, P["P4"], P["P4"], "compare"),
    (39.10, 41.90, P["P4"], P["P5"], "single"), (41.90, 43.90, P["P5"], P["P5"], "single"), (43.90, 45.90, P["P5"], P["P6"], "single"),
    (45.90, 47.60, P["P6"], P["P7"], "single"), (47.60, 49.55, P["P7"], P["P7"], "single"),
    (49.55, 51.90, P["P1"], P["P2"], "single"), (51.90, 57.20, P["P2"], P["P2"], "single"),
    (57.20, 57.90, P["P2"], P["P4"], "single"), (57.90, 60.65, P["P4"], P["P4"], "single"),
    (60.65, 62.60, P["P4"], P["P6"], "single"), (62.60, 64.75, P["P6"], P["P6"], "single"),
    (64.75, 72.50, P["P1"], P["P1"], "single"), (72.50, 74.40, P["P1"], P["P4"], "single"),
    (74.40, 82.40, P["P2"], P["P2"], "single"),
    (82.40, 97.60, P["P1"], P["P10"], "single"),
]
VIEWS = [(0, FULL), (43.9, FULL), (44.2, FEET), (45.7, FEET), (46.0, FULL), (51.9, FULL), (52.3, P2Z), (56.9, P2Z), (57.2, FULL),
         (57.9, FULL), (58.2, TOP), (60.5, TOP), (60.8, FULL), (97.6, FULL)]
W = [
    ("skel", 0, 82.4),
    ("butt", 13.22, 18.25), ("butt_lime", 13.22, 18.25), ("lbl:sin_ee", 15.23, 18.25),
    ("plane", 19.70, 23.15), ("tracer", 19.70, 23.15), ("lbl:en_plano", 22.03, 23.15),
    ("knee_lead", 23.96, 25.60), ("lbl:firme", 24.78, 25.60), ("lbl:equilibrio", 26.21, 28.30),
    ("spine_ref", 28.30, 39.10), ("knee", 28.30, 35.10), ("spine_live", 32.10, 35.10), ("lbl:se_para", 32.53, 35.10),
    # comparacion P1 | P4 (lado b con prefijo b_)
    ("spine_ref", 35.10, 39.10), ("b_spine_ref", 35.10, 39.10), ("b_spine_live", 35.10, 39.10), ("knee", 35.10, 39.10), ("b_knee", 35.10, 39.10),
    ("headtop", 39.10, 43.90), ("lbl:vuelve_bajar", 39.94, 41.90), ("heel", 44.14, 45.90),
    ("spine_ref", 45.90, 49.55), ("spine_live", 45.90, 49.55),
    ("hands_line", 53.71, 57.20), ("behind_arrow", 53.71, 57.20), ("lbl:detras", 55.03, 57.20),
    ("top_arrows", 58.04, 60.65), ("lbl:cruzado", 58.04, 60.65),
    ("plane", 60.65, 64.75), ("tracer", 60.65, 64.75), ("lbl:vuelve_plano", 61.22, 64.75),
    ("knee", 66.45, 74.40), ("lbl:mantene", 66.89, 72.50), ("butt", 68.49, 74.40), ("butt_lime", 68.49, 74.40), ("wall", 71.76, 74.40),
    ("target_line", 77.41, 82.40), ("actual_shaft", 75.06, 82.40), ("ideal_shaft", 78.49, 82.40), ("ideal_head", 80.17, 82.40),
    ("lbl:ideal", 78.49, 82.40),
]
STRIP = [P["P1"], P["P2"], P["P3"], P["P4"], P["P5"], P["P6"], P["P7"], P["P8"], P["P9"], P["P10"]]

def on_windows(t):
    act, starts = [], {}
    for name, a, b in W:
        if a <= t < b:
            act.append(name); starts[name] = a
    return act, starts

def seg_at(t):
    for t0, t1, s0, s1, mode in SEG:
        if t0 <= t < t1:
            if s0 == "strip":  # 10 posiciones, 0,32 s cada una
                return STRIP[min(9, int((t - t0) / 0.32))], mode
            u = (t - t0) / (t1 - t0)
            if s0 != s1 and t1 - t0 < 0.8:
                u = u * u * (3 - 2 * u)
            return s0 + (s1 - s0) * u, mode
    return SEG[-1][3], SEG[-1][4]

def view_at(t):
    for (ta, va), (tb, vb) in zip(VIEWS, VIEWS[1:]):
        if ta <= t <= tb:
            u = (t - ta) / (tb - ta) if tb > ta else 1; u = u * u * (3 - 2 * u)
            return [round(a + (b - a) * u, 3) for a, b in zip(va, vb)]
    return list(FULL)

frames = []
for k in range(int(DUR * FPS)):
    t = k / FPS; src, mode = seg_at(t); L, st = on_windows(t)
    f = {"t": round(t, 4), "src": round(src, 3), "mode": mode, "view": view_at(t), "L": L, "starts": st}
    if mode == "compare":
        f["cmp"] = [P["P1"], P["P4"]]; f["cmp_labels"] = ["P1 · ADDRESS", "P4 · TOPE"]
    frames.append(f)
json.dump({"fps": FPS, "dur": DUR, "frames": frames, "P": PP}, open(out, "w"))
print(len(frames), "cuadros")
