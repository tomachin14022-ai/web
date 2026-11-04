"""Edicion del reel v3 (sin 3D): que cuadro, que vista, que lineas en cada momento.
Tiempos tomados de las palabras de la voz (voice3/captions.json).

Uso: python -I timeline_v3.py SWING3D.json POSICIONES.json SALIDA.json
"""
import json
import sys

S3 = json.load(open(sys.argv[1])); PP = json.load(open(sys.argv[2])); out = sys.argv[3]
FPS, DUR = 30, 55.5
P1, P4, P5, P6, P7, P10 = PP["P1"], PP["P4"], PP["P5"], PP["P6"], PP["P7"], PP["P10"]
FULL = (0.0, 0.0, 354.0)
heel = S3["frames"][P5]["p2"][30]
FEET = (heel[0] - 70, min(heel[1] - 120, 492 - 150 * 1030 / 760), 150.0)  # zoom al pie de atras (sin salir del cuadro)
HIPS = (S3["frames"][P1]["p2"][23][0] - 95, S3["frames"][P1]["p2"][23][1] - 150, 220.0)  # zoom a la cadera

# (t0, t1, src0, src1, modo)
SEG = [
    (0.00, 2.20, P7, P7, "single"), (2.20, 2.45, P7, P1, "single"), (2.45, 4.25, P1, P10, "single"),
    (4.25, 6.00, P1, P1, "single"), (6.00, 7.00, P4, P4, "single"), (7.00, 8.50, 136, 136, "single"),
    (8.50, 10.85, P1, P1, "single"), (10.85, 11.95, P1, P7, "single"), (11.95, 16.10, P7, P7, "single"),
    (16.10, 23.00, P7, P7, "compare"),
    (23.00, 24.70, P4, P5, "single"), (24.70, 25.40, P5, P5, "single"), (25.40, 27.20, P5, 137, "single"),
    (27.20, 28.90, 137, 137, "single"), (28.90, 30.60, 137, P7, "single"), (30.60, 31.40, P7, P7, "single"),
    (31.40, 37.00, P7, P7, "single"),
    (37.00, 40.00, P1, P1, "single"), (40.00, 41.60, P1, P7, "single"), (41.60, 43.10, P7, P7, "single"),
    (43.10, 50.90, P1, P10, "single"), (50.90, 55.50, P1, P10, "single"),
]
# vistas (zoom): (t, vista) con transicion suave entre puntos
VIEWS = [(0, FULL), (25.40, FULL), (25.80, FEET), (27.00, FEET), (27.40, HIPS), (28.80, HIPS), (29.20, FULL), (55.5, FULL)]
W = [
    ("skel", 0, 16.10), ("skel", 23.0, 55.5),
    ("ghost", 0, 2.20), ("gapfill", 0, 2.20), ("butt", 0, 2.20),
    ("spine_ref", 4.33, 7.0), ("ok_postura", 5.42, 6.0), ("spine_live", 6.0, 7.0), ("ok_subida", 6.22, 7.0),
    ("plane", 7.0, 8.5), ("tracer", 7.0, 8.5), ("ok_plano", 7.48, 8.5),
    ("butt", 10.44, 16.10), ("butt_arrow", 12.18, 16.10), ("gapfill", 12.18, 16.10),
    ("spine_ref", 14.15, 16.10), ("spine_live", 14.15, 16.10), ("lbl_spine_imp", 15.11, 16.10),
    # comparacion: lado a = P1, lado b (prefijo b_) = P7
    ("butt", 16.10, 23.0), ("spine_ref", 16.10, 23.0), ("b_butt", 16.10, 23.0), ("b_spine_ref", 16.10, 23.0),
    ("b_spine_live", 16.10, 23.0), ("b_ghost", 16.31, 23.0), ("b_gapfill", 17.44, 23.0),
    # causa
    ("butt", 23.0, 31.40), ("headline", 23.0, 31.40), ("knee", 23.0, 31.40),
    ("lbl_agacha", 24.74, 25.40), ("heel", 25.48, 27.2), ("butt_arrow", 27.44, 31.40),
    ("spine_ref", 29.25, 31.40), ("spine_live", 29.25, 31.40), ("lbl_sube", 30.74, 31.40),
    # clave
    ("butt", 31.40, 37.0), ("target", 32.06, 37.0), ("glute_ring", 34.51, 37.0), ("butt_lime", 35.94, 37.0),
    # ejercicio
    ("chair", 38.04, 43.10), ("contact", 39.09, 40.0), ("chair_gap", 41.66, 43.10),
]

def on_windows(t):
    act, starts = [], {}
    for name, a, b in W:
        if a <= t < b:
            act.append(name); starts[name] = a
    return act, starts

def seg_at(t):
    for t0, t1, s0, s1, mode in SEG:
        if t0 <= t < t1:
            u = (t - t0) / (t1 - t0)
            if s0 != s1 and t1 - t0 < 0.6:
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
    frames.append({"t": round(t, 4), "src": round(src, 3), "mode": mode, "view": view_at(t), "L": L, "starts": st})
json.dump({"fps": FPS, "dur": DUR, "frames": frames, "P": PP}, open(out, "w"))
print(len(frames), "cuadros")
