#!/usr/bin/env python3
"""Genera la composición HyperFrames de un video "Lo barato sale caro" a partir de un JSON de datos.

Uso:  python3 generar.py datos/01-impresora.json 01-impresora
Escribe 01-impresora/index.html y 01-impresora/compositions/comparacion.html
"""
import json
import math
import sys
from pathlib import Path


def ars(n):
    """Formato de pesos argentinos: $1.080.000 o $5,6 para valores chicos."""
    if n < 10:
        return "$" + f"{n:.1f}".replace(".", ",")
    return "$" + f"{round(n):,}".replace(",", ".")


def calcular(d):
    a, b, uso, meses = d["a"], d["b"], d["usoMes"], d["meses"]
    for o in (a, b):
        o["porUso"] = o["consPrecio"] / o["rinde"]
        o["total"] = o["precio"] + uso * meses * o["porUso"]
    cruce = None
    if b["precio"] > a["precio"] and a["porUso"] > b["porUso"]:
        cruce = math.ceil((b["precio"] - a["precio"]) / (uso * (a["porUso"] - b["porUso"])))
    ratio = round(a["porUso"] / b["porUso"])
    ahorro = a["total"] - b["total"]
    return cruce, ratio, ahorro


def path_acumulado(o, uso, meses, x0, x1, y0, y1, vmax):
    pts = []
    for m in range(meses + 1):
        v = o["precio"] + uso * m * o["porUso"]
        x = x0 + (x1 - x0) * m / meses
        y = y1 - (y1 - y0) * v / vmax
        pts.append(f"{'M' if m == 0 else 'L'}{x:.1f} {y:.1f}")
    return " ".join(pts)


def main():
    datos = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    salida = Path(sys.argv[2])
    cruce, ratio, ahorro = calcular(datos)
    a, b, uso, meses = datos["a"], datos["b"], datos["usoMes"], datos["meses"]

    # Gráfico: área x 120–780, y 430–960 dentro del SVG de 1080x1920
    X0, X1, Y0, Y1 = 150, 760, 440, 950
    vmax = max(a["total"], b["total"]) * 1.12
    path_a = path_acumulado(a, uso, meses, X0, X1, Y0, Y1, vmax)
    path_b = path_acumulado(b, uso, meses, X0, X1, Y0, Y1, vmax)
    def xy(m, o):
        v = o["precio"] + uso * m * o["porUso"]
        return X0 + (X1 - X0) * m / meses, Y1 - (Y1 - Y0) * v / vmax
    cx, cy = xy(cruce, b) if cruce else (0, 0)
    ax_end = xy(meses, a)
    bx_end = xy(meses, b)

    reemplazos = {
        "HOOK1": datos["hook"][0], "HOOK2": datos["hook"][1], "HOOK3": datos["hook"][2], "HOOK4": datos["hook"][3],
        "A_NOMBRE": a["nombre"], "B_NOMBRE": b["nombre"],
        "A_PRECIO": ars(a["precio"]), "B_PRECIO": ars(b["precio"]),
        "A_CONS": a["consumible"], "B_CONS": b["consumible"],
        "A_CONS_PRECIO": ars(a["consPrecio"]), "B_CONS_PRECIO": ars(b["consPrecio"]),
        "A_RINDE": f"{a['rinde']:,}".replace(",", "."), "B_RINDE": f"{b['rinde']:,}".replace(",", "."),
        "UNIDAD": datos["unidad"], "UNIDAD_SING": datos["unidadSing"],
        "A_POR_USO": ars(a["porUso"]), "B_POR_USO": ars(b["porUso"]),
        "A_POR_USO_NUM": f"{a['porUso']:.4f}", "B_POR_USO_NUM": f"{b['porUso']:.4f}",
        "RATIO": str(ratio), "B_CORTO": b["corto"], "A_CORTO": a["corto"],
        "USO_MES": f"{uso:,}".replace(",", "."), "ANIOS": str(meses // 12),
        "A_TOTAL": ars(a["total"]), "B_TOTAL": ars(b["total"]), "AHORRO": ars(ahorro),
        "CRUCE": str(cruce or ""),
        "PATH_A": path_a, "PATH_B": path_b,
        "CX": f"{cx:.1f}", "CY": f"{cy:.1f}",
        "AXE_X": f"{ax_end[0]:.1f}", "AXE_Y": f"{ax_end[1]:.1f}", "BXE_X": f"{bx_end[0]:.1f}", "BXE_Y": f"{bx_end[1]:.1f}",
        "AXE_LY": f"{min(ax_end[1], bx_end[1] - 70) - 18:.1f}", "BXE_LY": f"{max(bx_end[1], ax_end[1] + 70) + 46:.1f}",
        "NOTA": datos["nota"],
        "PREGUNTA": datos["pregunta"],
        "HINT": datos["hint"],
        "CHART_TITULO": datos["chartTitulo"].replace("{USO}", f"{uso:,}".replace(",", ".")),
        "RATIO_HTML": " ".join('<span class="w">' + w + '</span>' for w in datos["frasePorUso"].replace("{RATIO}", str(ratio)).split()),
    }
    plantilla = (Path(__file__).parent / "plantilla-comparacion.html").read_text(encoding="utf-8")
    for k, v in reemplazos.items():
        plantilla = plantilla.replace("{{" + k + "}}", v)
    faltan = [l for l in plantilla.splitlines() if "{{" in l]
    if faltan:
        raise SystemExit("Faltan reemplazos: " + "; ".join(faltan[:3]))
    (salida / "compositions").mkdir(parents=True, exist_ok=True)
    (salida / "compositions" / "comparacion.html").write_text(plantilla, encoding="utf-8")
    raiz = (Path(__file__).parent / "plantilla-index.html").read_text(encoding="utf-8")
    (salida / "index.html").write_text(raiz, encoding="utf-8")
    # Texto para la publicación de Instagram (los links van en la bio, no son clicables en el texto)
    caption = (
        f"{' '.join(datos['hook']).capitalize()} 👀\n\n"
        f"{a['nombre']}: {ars(a['precio'])} al comprar, pero {ars(a['porUso'])} por {datos['unidadSing']}.\n"
        f"{b['nombre']}: {ars(b['precio'])} al comprar, y {ars(b['porUso'])} por {datos['unidadSing']}.\n\n"
        f"En {meses // 12} años: {ars(a['total'])} contra {ars(b['total'])}. Ahorrás {ars(ahorro)}.\n"
        + (f"Desde el mes {cruce}, la que cuesta más ya te salió más barata.\n" if cruce else "")
        + f"\n¿Cuál comprarías? Los links de las dos están en la bio.\n"
        f"Contiene links de afiliado de Mercado Libre. {datos['nota']}"
    )
    (salida / "caption.txt").write_text(caption, encoding="utf-8")
    print(json.dumps({"cruceMes": cruce, "ratio": ratio, "ahorro": round(ahorro),
                      "porUsoA": round(a["porUso"], 2), "porUsoB": round(b["porUso"], 2),
                      "totalA": round(a["total"]), "totalB": round(b["total"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
