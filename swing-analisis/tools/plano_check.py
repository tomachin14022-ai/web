"""Over the top / plano de bajada desde atrás (DTL), con la regla asimétrica de la skill analisis-swing.

Uso: python -I plano_check.py SWING3D.json POSICIONES.json [--vp X,Y] [--video 1080x1920] [--f PX] [--zurdo] [--out SALIDA.json]

Pruebas (informe de investigación, sección "Over the top exige dos pruebas coincidentes"):
  0. Control de cámara: punto de fuga de la línea de tiro (--vp, de las varillas del piso) cerca del centro.
     Giro θ = atan(d/f). Si pasa de 5°, las pruebas contra líneas absolutas (slot) no valen: solo la relativa.
  1. Slot de TPI: línea A = varilla en P1; línea B = varilla en P3. En P5 y P6, la cabeza del palo
     por encima de B = over the top; por debajo de A = debajo del plano.
  2. Bajada contra subida (V1): a la misma altura, manos de bajada (P5→P7) contra manos de subida (P1→P3),
     y ángulo de la varilla en P5 contra P3.
  3. Pistas: cabeza del palo por fuera de las manos al empezar la bajada; varilla más empinada que el
     antebrazo de atrás en P6.
Regla: "over the top" si la prueba 1 o la 2 supera el margen Y coincide una pista (o el vuelo, que lo informa
el jugador). "En plano" solo si las dos pruebas quedan dentro del margen. Si no, "no evaluable".
Márgenes: manos ±4 cm, varilla ±5° (inferencias del informe, sin validar contra referencia).
P2 y P6 desde atrás: la varilla apunta casi a la cámara (escorzo), así que su ángulo en la imagen no se usa.
Salida: un veredicto que se copia tal cual al análisis; nunca decir "en plano" si el veredicto no lo dice.
"""
import argparse
import json
import math

import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("swing3d"); ap.add_argument("posiciones")
ap.add_argument("--vp", help="punto de fuga de la línea de tiro en px del video, X,Y")
ap.add_argument("--f", type=float, help="distancia focal en px (default 1400 × alto/1920)")
ap.add_argument("--video", default="1080x1920", help="ancho x alto del video en px")
ap.add_argument("--zurdo", action="store_true")
ap.add_argument("--out")
A = ap.parse_args()

S = json.load(open(A.swing3d)); PP = json.load(open(A.posiciones))
F = S["frames"]; cm = S["k_m_por_px"] * 100
MARGEN_CM, MARGEN_DEG = 4.0, 5.0
LEAD_W, TRAIL_E, TRAIL_W = (16, 13, 15) if A.zurdo else (15, 14, 16)

p2 = lambda t: np.array(F[t]["p2"], float)
head = lambda t: np.array(F[t]["h2"], float)
grip = lambda t: np.array(F[t]["g2"], float)
hands = lambda t: (p2(t)[15] + p2(t)[16]) / 2
P = {k: int(v) for k, v in PP.items()}

ball = head(P["P1"])
lado = 1.0 if ball[0] > (p2(P["P1"])[23][0] + p2(P["P1"])[24][0]) / 2 else -1.0  # +1: la pelota está a la derecha

def largo(t):
    """Largo aparente de la varilla respecto de P1 (desde atrás, en P1 está casi en el plano de la imagen)."""
    return float(np.linalg.norm(grip(t) - head(t)) / np.linalg.norm(grip(P["P1"]) - head(P["P1"])))

def ang_varilla(t):
    """Inclinación de la varilla respecto del horizontal de la imagen (0° plana, 90° vertical)."""
    d = grip(t) - head(t)
    return abs(math.degrees(math.atan2(-d[1], d[0] * lado)))

def lado_linea(pt, a, b):
    """Distancia con signo (cm) de pt a la recta a→b; + = por encima/afuera (lado de la pelota, arriba)."""
    d = (b - a) / np.linalg.norm(b - a); n = np.array([d[1], -d[0]])
    if n[1] > 0 or (abs(n[1]) < 1e-9 and n[0] * lado < 0):
        n = -n  # normal apuntando hacia arriba (y menor) y hacia la pelota
    return float(np.dot(pt - a, n) * cm)

def x_a_altura(frames, y):
    pts = [hands(t) for t in frames]
    for p, q in zip(pts, pts[1:]):
        if (p[1] - y) * (q[1] - y) <= 0 and p[1] != q[1]:
            return p[0] + (y - p[1]) / (q[1] - p[1]) * (q[0] - p[0])
    return None

res = {"margenes": {"manos_cm": MARGEN_CM, "varilla_deg": MARGEN_DEG}}

# 0. Cámara
cam_ok = None
if A.vp:
    vx, vy = map(float, A.vp.split(","))
    w_img, h_img = map(float, A.video.lower().split("x"))
    f = A.f or 1400.0 * max(w_img, h_img) / 1920
    cx, cy = w_img / 2, h_img / 2
    giro = math.degrees(math.atan((vx - cx) / f)); incl = math.degrees(math.atan((vy - cy) / f))
    cam_ok = bool(abs(giro) <= 5)
    res["camara"] = {"giro_deg": round(giro, 1), "inclinacion_deg": round(incl, 1), "pasa": cam_ok}

# 1. Slot de TPI
lA = (head(P["P1"]), grip(P["P1"])); lB = (head(P["P3"]), grip(P["P3"]))
slot = {}
for k in ("P5", "P6"):
    t = P[k]
    slot[k] = {"cabeza_vs_B_cm": round(lado_linea(head(t), *lB), 1),
               "cabeza_vs_A_cm": round(lado_linea(head(t), *lA), 1),
               "manos_vs_B_cm": round(lado_linea(hands(t), *lB), 1)}
peor_B = max(v["cabeza_vs_B_cm"] for v in slot.values())
debajo_A = min(v["cabeza_vs_A_cm"] for v in slot.values())
t1 = "over" if peor_B > MARGEN_CM else ("debajo" if debajo_A < -MARGEN_CM else "en_slot")
if cam_ok is not True:
    res["prueba1_slot_sin_validar"] = t1  # se informa, pero no decide
    t1 = "no_valida_camara" if cam_ok is False else "sin_control_camara"
res["prueba1_slot"] = {"detalle": slot, "resultado": t1}

# 2. Bajada contra subida
sube = range(P["P1"], P["P3"] + 1); baja = range(P["P5"], P["P7"] + 1)
y_lo = max(hands(P["P3"])[1], hands(P["P5"])[1]); y_hi = min(hands(P["P1"])[1], hands(P["P7"])[1])
filas = []
for y in np.arange(math.ceil(y_lo / 10) * 10, y_hi, 10):
    xs, xb = x_a_altura(sube, y), x_a_altura(baja, y)
    if xs is not None and xb is not None:
        filas.append((int(y), round((xb - xs) * lado * cm, 1)))
dif = [d for _, d in filas]
dP = round(ang_varilla(P["P5"]) - ang_varilla(P["P3"]), 1)
t2 = None
span_cm = (filas[-1][0] - filas[0][0]) * cm if dif else 0
if dif and span_cm < 15:
    t2 = "pocas_alturas"  # el tramo comparable es muy corto para concluir
elif dif:
    med = float(np.median(dif))  # mediana: un punto ruidoso no decide
    if med > MARGEN_CM or dP > MARGEN_DEG:
        t2 = "over"
    elif abs(med) <= MARGEN_CM and abs(dP) <= MARGEN_DEG:
        t2 = "en_plano"
    elif med < -MARGEN_CM:
        t2 = "debajo"
    else:
        t2 = "dudoso"
res["prueba2_relativa"] = {
    "manos_bajada_menos_subida_cm (+ = por encima/afuera)": {str(y): d for y, d in filas[::10]},
    "mediana_cm": round(float(np.median(dif)), 1) if dif else None,
    "rango_cm": [min(dif), max(dif)] if dif else None, "alturas_px": [filas[0][0], filas[-1][0]] if dif else None, "tramo_cm": round(span_cm, 1),
    "varilla_P3_deg": round(ang_varilla(P["P3"]), 1), "varilla_P5_deg": round(ang_varilla(P["P5"]), 1),
    "P5_menos_P3_deg": dP,
    "escorzo_varilla_P3_P5": [round(largo(P["P3"]), 2), round(largo(P["P5"]), 2)], "resultado": t2}

# 3. Pistas secundarias
afuera = [round((head(t)[0] - hands(t)[0]) * lado * cm, 1) for t in range(P["P4"], P["P5"] + 1)]
pistas = {"cabeza_afuera_de_manos_P4_P5_cm_max": max(afuera), "cabeza_afuera": bool(max(afuera) > MARGEN_CM)}
t6 = P["P6"]
if largo(t6) >= 0.5:  # varilla visible: se compara con el antebrazo de atrás
    ante = p2(t6)[TRAIL_W] - p2(t6)[TRAIL_E]
    ang_ante = abs(math.degrees(math.atan2(-ante[1], ante[0] * lado)))
    pistas.update({"P6": "varilla vs antebrazo de atrás", "varilla_P6_deg": round(ang_varilla(t6), 1),
                   "antebrazo_atras_P6_deg": round(ang_ante, 1),
                   "P6_empinada": bool(ang_varilla(t6) - ang_ante > MARGEN_DEG)})
else:  # varilla en escorzo (apunta a la cámara): solo vale de qué lado de las manos aparece la cabeza
    off = round((head(t6)[0] - hands(t6)[0]) * lado * cm, 1)
    pistas.update({"P6": f"varilla en escorzo ({largo(t6):.2f} del largo): cabeza vs manos",
                   "cabeza_vs_manos_P6_cm": off,
                   # en escorzo unos cm son proyección: solo cuenta una diferencia grande (pista débil)
                   "P6_empinada": bool(off > 2 * MARGEN_CM)})
res["pistas"] = pistas
hay_pista = pistas["cabeza_afuera"] or pistas["P6_empinada"]

# Regla asimétrica
if "over" in (t1, t2) and hay_pista:
    v = "OVER THE TOP"
elif "over" in (t1, t2):
    v = "OVER THE TOP PROBABLE: confirmar con el vuelo (pull / pull-slice / slice) antes de decirlo"
elif t1 == "en_slot" and t2 == "en_plano" and not hay_pista:
    v = "EN PLANO"
elif t2 == "en_plano" and not hay_pista:
    v = ("SIN SEÑALES DE OVER THE TOP EN LA PRUEBA RELATIVA (cámara sin verificar): "
         "decir eso, no 'en plano'")
elif "debajo" in (t1, t2):
    v = "DEBAJO DEL PLANO (palo atascado): revisar early extension"
else:
    v = "NO EVALUABLE"
res["veredicto"] = v

print(json.dumps(res, ensure_ascii=False, indent=1))
if A.out:
    json.dump(res, open(A.out, "w"), ensure_ascii=False, indent=1)
