"""Chequeos medidos desde atrás (DTL), con margen y veredicto, según la skill analisis-swing.

Uso: python -I dtl_checks.py SWING3D.json METRICS.json POSICIONES.json [--vp X,Y] [--video 1080x1920]
                             [--zurdo] [--pose POSE.npz --velocidad-real] [--out SALIDA.json]

Solo mide lo que se ve y se puede dibujar sobre el cuadro, comparado con el address del mismo jugador.
Veredictos:
  "sí"                 la medida supera el margen en el sentido de la falla (se dice y se dibuja);
  "dentro del margen"  no se mide un cambio mayor que el error de medición (no es lo mismo que "perfecto");
  "no evaluable desde atrás" / "descripción"  no se afirma con números.
Márgenes (inferencias del informe de investigación, sin validar contra referencia): ángulos ±5°, cm ±3,
manos respecto del plano ±4 cm. La decisión de over the top sale de plano_check.analizar.
"""
import argparse
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plano_check import analizar as plano  # noqa: E402

M_DEG, M_CM = 5.0, 3.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("swing3d"); ap.add_argument("metrics"); ap.add_argument("posiciones")
    ap.add_argument("--vp"); ap.add_argument("--video", default="1080x1920")
    ap.add_argument("--zurdo", action="store_true")
    ap.add_argument("--pose", help="pose.npz con t_ms (tiempos reales de cada cuadro)")
    ap.add_argument("--velocidad-real", action="store_true", help="el video no tiene cámara lenta horneada")
    ap.add_argument("--out")
    A = ap.parse_args()
    S = json.load(open(A.swing3d)); M = json.load(open(A.metrics)); PP = json.load(open(A.posiciones))
    res = chequear(S, M, PP, A.vp, A.video, A.zurdo, A.pose if A.velocidad_real else None)
    texto(res)
    if A.out:
        json.dump(res, open(A.out, "w"), ensure_ascii=False, indent=1)


def chequear(S, M, PP, vp=None, video="1080x1920", zurdo=False, pose_ts=None):
    F = S["frames"]; cm = S["k_m_por_px"] * 100
    P = {k: int(v) for k, v in PP.items()}
    L = dict(sh=12, hip=24, knee=26, ank=28, heel=30, el=14, wr=16) if not zurdo else dict(sh=11, hip=23, knee=25, ank=27, heel=29, el=13, wr=15)
    Ld = dict(sh=11, hip=23, knee=25, ank=27, wr=15) if not zurdo else dict(sh=12, hip=24, knee=26, ank=28, wr=16)
    p2 = lambda t: np.array(F[t]["p2"], float)
    head = lambda t: np.array(F[t]["h2"], float); grip = lambda t: np.array(F[t]["g2"], float)
    hands = lambda t: (p2(t)[15] + p2(t)[16]) / 2
    mid = lambda t, a, b: (p2(t)[a] + p2(t)[b]) / 2
    lado = 1.0 if head(P["P1"])[0] > mid(P["P1"], 23, 24)[0] else -1.0

    def ang3(a, b, c):
        v1, v2 = a - b, c - b
        return math.degrees(math.acos(np.clip(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)), -1, 1)))

    def tronco(t):  # grados respecto de la vertical, + = inclinado hacia la pelota
        h, s = mid(t, 23, 24), mid(t, 11, 12)
        return math.degrees(math.atan2(lado * (s[0] - h[0]), h[1] - s[1]))

    def rod(t, Lx):
        p = p2(t); return ang3(p[Lx["hip"]], p[Lx["knee"]], p[Lx["ank"]])

    def varilla(t):  # misma definición que plano_check: 0° horizontal, 90° vertical
        d = grip(t) - head(t); d = d if d[1] < 0 else -d
        return math.degrees(math.atan2(-d[1], -d[0] * lado))

    def largo(t):
        return float(np.linalg.norm(grip(t) - head(t)) / np.linalg.norm(grip(P["P1"]) - head(P["P1"])))

    r1 = lambda x: round(float(x), 1)
    res = {"lado_pelota": "derecha" if lado > 0 else "izquierda", "zurdo": zurdo,
           "margenes": {"angulos_deg": M_DEG, "desplazamientos_cm": M_CM, "plano_cm": 4.0}}

    # 1. Setup (P1): referencias del propio jugador, sin norma absoluta
    t1 = P["P1"]
    res["P1_setup"] = {
        "tronco_deg": r1(tronco(t1)), "rodilla_atras_deg": r1(rod(t1, L)), "rodilla_adelante_deg": r1(rod(t1, Ld)),
        "varilla_linea_A_deg": r1(varilla(t1)),
        "manos_delante_de_la_cadera_cm": r1((hands(t1)[0] - mid(t1, 23, 24)[0]) * lado * cm),
        "nota": "Referencias del propio address. No se comparan en grados con profesionales (depende del método).",
    }

    # 2. Postura a lo largo del swing (contra P1)
    cola = M["series"]["cola_x"]; c0 = M["linea_cola_address_x"]
    ear0, hip0 = mid(t1, 7, 8), mid(t1, 23, 24)
    fil = {}
    for k in ("P2", "P3", "P4", "P5", "P6", "P7", "P8"):
        t = P[k]
        fil[k] = {"tronco_deg": r1(tronco(t)), "d_tronco_deg": r1(tronco(t) - tronco(t1)),
                  "d_rodilla_atras_deg": r1(rod(t, L) - rod(t1, L)), "d_rodilla_adelante_deg": r1(rod(t, Ld) - rod(t1, Ld)),
                  "cola_hacia_pelota_cm": r1((cola[t] - c0) * lado * cm),
                  "cabeza_baja_cm": r1((mid(t, 7, 8)[1] - ear0[1]) * cm),
                  "cabeza_hacia_pelota_cm": r1((mid(t, 7, 8)[0] - ear0[0]) * lado * cm),
                  "pelvis_baja_cm": r1((mid(t, 23, 24)[1] - hip0[1]) * cm),
                  "talon_atras_arriba_cm": r1(max(0.0, (p2(t1)[L["heel"]][1] - p2(t)[L["heel"]][1]) * cm))}
    res["posiciones"] = fil

    tpi = {}
    # Pérdida de postura: solo P4–P7 (TPI); el tronco manda, la rodilla acompaña
    dmax = max((fil[k]["d_tronco_deg"] for k in ("P4", "P5", "P6", "P7")), key=abs)
    kmax = [k for k in ("P4", "P5", "P6", "P7") if fil[k]["d_tronco_deg"] == dmax][0]
    if abs(dmax) > M_DEG:
        tpi["loss_of_posture"] = {"veredicto": "sí", "en": kmax, "valor": f"{dmax:+.0f}° de tronco contra P1",
                                  "sentido": "se para (pierde inclinación)" if dmax < 0 else "se agacha (más inclinación)",
                                  "dibujo": "spine_ref + spine_live"}
    else:
        tpi["loss_of_posture"] = {"veredicto": "dentro del margen", "valor": f"máx {dmax:+.0f}° (±{M_DEG:.0f}°)"}
    tpi["loss_of_posture"]["rodilla_atras_P4_deg"] = fil["P4"]["d_rodilla_atras_deg"]

    # Early extension: la nalga avanza hacia la pelota respecto de su línea del address (P4–P7)
    em = max((fil[k]["cola_hacia_pelota_cm"] for k in ("P4", "P5", "P6", "P7")))
    ek = [k for k in ("P4", "P5", "P6", "P7") if fil[k]["cola_hacia_pelota_cm"] == em][0]
    tpi["early_extension"] = ({"veredicto": "sí", "en": ek, "valor": f"la nalga se despega {em:.0f} cm de su línea",
                               "dibujo": "butt + butt_arrow + chair_gap"} if em > M_CM else
                              {"veredicto": "dentro del margen", "valor": f"máx {em:+.0f} cm (±{M_CM:.0f} cm)",
                               "dibujo": "butt (línea en contacto)"})

    # Plano de hombros (receta TPI): hombro líder en P4 respecto de la paralela a la línea del tronco de P1
    # que pasa por el hombro de atrás. + = por encima (plano de hombros plano). Aprox.: el hombro líder está tapado.
    hA, sA = mid(t1, 23, 24), mid(t1, 11, 12); d = (sA - hA) / np.linalg.norm(sA - hA)
    n = np.array([d[1], -d[0]]); n = -n if n[1] > 0 else n
    o = p2(t1)[L["sh"]]
    dist = float(np.dot(p2(P["P4"])[Ld["sh"]] - o, n) * cm)
    tpi["flat_shoulder_plane"] = ({"veredicto": "sí", "valor": f"hombro líder {dist:.0f} cm por encima de la línea",
                                   "dibujo": "shoulder_plane"} if dist > M_CM else
                                  {"veredicto": "no" if dist < -M_CM else "dentro del margen",
                                   "valor": f"hombro líder {dist:+.0f} cm respecto de la línea (+ = encima)", "dibujo": "shoulder_plane"})
    tpi["flat_shoulder_plane"]["nota"] = "aprox.: el hombro líder queda detrás del cuerpo desde atrás; verificar en el cuadro"

    # Over the top (protocolo completo)
    ott = plano(S, PP, vp, video, None, zurdo)
    v = ott["veredicto"]
    tpi["over_the_top"] = {"veredicto": "sí" if v == "OVER THE TOP" else ("probable: falta el vuelo" if v.startswith("OVER THE TOP PROBABLE")
                           else ("dentro del margen" if v.startswith(("EN PLANO", "SIN SEÑALES")) else v.lower())),
                           "valor": v, "dibujo": "hand_paths + slot"}
    res["plano"] = ott

    # Late buckle: la rodilla líder se flexiona de golpe después del impacto
    db = fil["P8"]["d_rodilla_adelante_deg"] - fil["P7"]["d_rodilla_adelante_deg"]
    tpi["late_buckle"] = ({"veredicto": "sí", "valor": f"rodilla líder {db:.0f}° más flexionada de P7 a P8"} if db < -2 * M_DEG else
                          {"veredicto": "dentro del margen", "valor": f"{db:+.0f}° de P7 a P8 (±{2 * M_DEG:.0f}°)"})

    for k in ("s_posture", "c_posture"):
        tpi[k] = {"veredicto": "descripción", "valor": "curvatura de la espalda en P1: se mira en el cuadro, no se mide con los puntos"}
    tpi["flying_elbow"] = {"veredicto": "descripción", "valor": "codo de atrás en P4: no es falla por sí solo (TPI)"}
    tpi["casting"] = {"veredicto": "dato", "valor": f"ángulo brazo líder–varilla en P5: {ang3(p2(P['P5'])[Ld['sh']], p2(P['P5'])[Ld['wr']], head(P['P5'])):.0f}° (±10°); se juzga de frente"}
    for k in ("sway", "slide", "reverse_spine_angle", "forward_lunge", "hanging_back", "scooping", "chicken_winging"):
        tpi[k] = {"veredicto": "no evaluable desde atrás", "valor": "necesita la toma de frente"}
    res["tpi"] = tpi

    # Plano del palo: descripciones medidas (no son fallas por sí solas)
    t2_, t4 = P["P2"], P["P4"]
    # P2: la cabeza está más cerca de la cámara que las manos (escorzo): solo vale el lado, no los cm.
    off2 = (head(t2_)[0] - hands(t2_)[0]) * lado * cm
    pal = {"P2": ("cabeza por dentro de las manos" if off2 < -4 else "cabeza por fuera de las manos" if off2 > 4
                  else "cabeza en línea con las manos") + " (solo el lado: en escorzo los cm no valen)",
           "P2_escorzo": round(largo(t2_), 2),
           "P3_linea_B_deg": r1(varilla(P["P3"])), "P1_linea_A_deg": r1(varilla(t1)),
           "P3_menos_P1_deg": r1(varilla(P["P3"]) - varilla(t1)),
           "P4": ("descripción visual: dibujar la varilla prolongada y la línea de tiro. Desde atrás no se puede separar "
                  "'cruzado' de 'por encima o por debajo de la horizontal' con un número. No es falla por sí solo"),
           "P4_escorzo": round(largo(t4), 2)}
    res["palo"] = pal

    # Ritmo: solo con video a velocidad real y tiempos reales
    if pose_ts:
        ts = np.load(pose_ts)["t_ms"]; ev = S.get("eventos", {}); t0 = ev.get("inicio", P["P1"])
        sub, baj = (ts[P["P4"]] - ts[t0]) / 1000, (ts[P["P7"]] - ts[P["P4"]]) / 1000
        res["ritmo"] = {"subida_s": round(sub, 2), "bajada_s": round(baj, 2), "ratio": round(sub / baj, 1),
                        "referencia": "profesionales: subida 0,7–0,8 s con hierro 5 [CONF]; el ratio no distingue niveles"}
    else:
        res["ritmo"] = "no evaluable: cámara lenta horneada o sin tiempos reales"

    # Candidatas a prioridad: fallas medidas, en el orden en que aparecen (la primera de la cadena va primero)
    orden = {"P1": 1, "P2": 2, "P3": 3, "P4": 4, "P5": 5, "P6": 6, "P7": 7, "P8": 8}
    fase = {"loss_of_posture": tpi["loss_of_posture"].get("en", "P4"), "early_extension": tpi["early_extension"].get("en", "P5"),
            "flat_shoulder_plane": "P4", "over_the_top": "P5", "late_buckle": "P8"}
    cand = [k for k, x in tpi.items() if x["veredicto"] == "sí"]
    res["candidatas_prioridad"] = sorted(cand, key=lambda k: orden.get(fase.get(k, "P8"), 9))
    res["regla_prioridad"] = ("Elegir la primera de la lista que además explique el vuelo informado; "
                              "si ninguna lo explica, decirlo y no forzar la cadena.")
    return res


def texto(res):
    print(f"Pelota a la {res['lado_pelota']} · márgenes ±{res['margenes']['angulos_deg']:.0f}° / ±{res['margenes']['desplazamientos_cm']:.0f} cm")
    s = res["P1_setup"]
    print(f"P1: tronco {s['tronco_deg']}° · rodilla atrás {s['rodilla_atras_deg']}° · adelante {s['rodilla_adelante_deg']}° · varilla {s['varilla_linea_A_deg']}°")
    print("     Δtronco  Δrod.atrás  cola→pelota  cabeza↓  pelvis↓  talón")
    for k, f in res["posiciones"].items():
        print(f"  {k}  {f['d_tronco_deg']:+6.1f}°  {f['d_rodilla_atras_deg']:+7.1f}°  {f['cola_hacia_pelota_cm']:+8.1f} cm"
              f"  {f['cabeza_baja_cm']:+5.1f}  {f['pelvis_baja_cm']:+5.1f}  {f['talon_atras_arriba_cm']:4.1f}")
    print("TPI:")
    for k, x in res["tpi"].items():
        print(f"  {k:22s} {x['veredicto']:26s} {x.get('valor', '')}")
    print("Palo:", {k: v for k, v in res["palo"].items()})
    print("Ritmo:", res["ritmo"])
    print("Candidatas a prioridad:", res["candidatas_prioridad"] or "ninguna medida por encima del margen")


if __name__ == "__main__":
    main()
