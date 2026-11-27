"""Revisión con reglas fijas de las piezas del calendario final.

Uso: python3 revisar.py          → lista cada falla con la regla que rompe (sale con código 1 si hay fallas)
Las reglas salen del CLAUDE.md (secciones 0, 2, 4 y 5) y de la investigación (research_notes/Guiones con datos reales/).
Cada regla tiene un código: así se puede ver qué se corrigió entre una revisión y la siguiente.
"""
import re
import sys
from collections import Counter

import calendario as C
import calendario_plan as P
from guiones_comun import CTA, FIN_ENT, LEGAL

MODELOS = ["Eado", "CS55", "Deepal", "S05", "ORA 03", "ORA 05", "H6", "H7", "Jolion", "Tank", "Poer", "L200", "Outlander", "Easy 3", "JMEV"]
MARCAS_AJENAS = r"\b(Toyota|Ford|Corolla|Hilux|Ranger|Amarok|BYD|Santander|Bancor|Macro|Chery|Renault|Volkswagen|Peugeot|Fiat|Tesla|YPF|Shell|Axion|Puma)\b"
JERGA = r"\b(kWh|kW|NEDC|WLTP|CLTC|LEV2|TNA|CER|ADAS|PHEV|HEV|torque|Nm|diferencial|reductora|monofásica|trifásica|CFTEA)\b"
# Espacios para completar que no se pueden inventar: precio/cuota del día, mediciones propias, datos del evento, comentarios reales
PERMITIDOS = r"(?i)precio|cuota|anticipo|\bN\b|\.\.|total|monto|ticket|km|L/100|\$ ?real|%|comentario|respuesta|nombre|área|dirección|referencia|día|fecha|hora|beneficio|modelo|barrios?|lugar|pista|algo|lo que|creador|su |sus |por qué vino|dato|repuesto|pastillas|haval h6|tonada|pedido|comparación|frase|bici|conservadora|resultado|noticia|lo esencial|la cuenta|lo honesto|código|mes|unidades|falló|lo que sobró|lo que entró|lo que trae|l/100|\$|real|la más fácil|\[\.\.\]"


def segundos(t):
    m = re.match(r"(\d+)\s*[–-]\s*(\d+)\s*s", t)
    return (int(m.group(1)), int(m.group(2))) if m else None


def texto_voz(g):
    return " ".join(e[1] for e in g["escenas"] if e[1])


FALLAS = []


def falla(gid, regla, detalle):
    FALLAS.append((gid, regla, detalle))


def revisar_pieza(fecha, gid, g, extra):
    es_carrusel = gid.startswith("CAR")
    escenas = g["escenas"]
    voz = texto_voz(g)
    pantalla = " ".join(e[3] for e in escenas if e[3] and e[3] != LEGAL)
    todo = voz + " " + pantalla + " " + g["gancho"] + " " + (extra.get("gancho_b") or g.get("gancho_b") or "")
    producto = any(m.lower() in (g["pieza"] + g["idea"]).lower() for m in MODELOS)
    evento = gid in ("E16", "E17", "E18", "E19", "V12", "V13", "V11", "E28", "D19a", "D19b")

    # R01 · el gancho escrito está en el cuadro 0
    if not escenas[0][3]:
        falla(gid, "R01 gancho en cuadro 0", "la primera escena no tiene texto en pantalla")
    # R02 · una promesa en los primeros 5 s que se paga al final (reels de más de 20 s)
    tiempos = [segundos(e[0]) for e in escenas]
    if not es_carrusel and tiempos[-1] and tiempos[-1][1] > 20 and gid not in ("E19", "E18", "E17", "E28"):
        primeros = " ".join(e[1] + " " + e[3] for e, t in zip(escenas, tiempos) if t and t[0] < 6).lower()
        if not re.search(r"al final|la última|el último|la tercera|la n\.º 1|número uno|te digo|te muestro|te lo cuento|vamos a ver|lo medimos|te hago la cuenta|hay trampa|quién no|qué no|te lo muestro|la tercera es|la puerta, al final", primeros):
            falla(gid, "R02 promesa a los 5 s", "no hay una promesa que se pague al final en los primeros 5 s")
    # R03 · escenas seguidas, sin huecos ni solapes, y ninguna de más de 12 s sin cambio
    if not es_carrusel:
        fin = 0
        for e, t in zip(escenas, tiempos):
            if not t:
                falla(gid, "R03 tiempos", f"escena sin tiempo legible: {e[0]}")
                continue
            if t[0] != fin:
                falla(gid, "R03 tiempos", f"hueco o solape antes de {e[0]}")
            fin = t[1]
            if t[1] - t[0] > 12 and not re.search(r"acelerado|montaje|cortes|uno cada|un corte|reloj que avanza|almanaque|su recorrido|su montaje", e[2].lower()):
                falla(gid, "R03 re-gancho", f"escena {e[0]} de {t[1] - t[0]} s sin cambios marcados")
    # R04 · la voz entra en el tiempo de la escena (máx. ~3,2 palabras por segundo con la voz ×1,15)
    if not es_carrusel:
        for e, t in zip(escenas, tiempos):
            if t and e[1] and not e[1].startswith("["):
                dice = re.sub(r"\(.*?\)|V\d: |Vendedor \d[^:]*: |Jefe de taller: |Los dos: |'Cliente': ", "", e[1])
                palabras = len(re.findall(r"\w+", dice))
                dur = t[1] - t[0]
                if dur and palabras / dur > 3.0:
                    falla(gid, "R04 ritmo de voz", f"{e[0]}: {palabras} palabras en {dur} s ({palabras / dur:.1f}/s)")
    # R21 · el gancho hablado entra en 2–3 s (hasta 8 palabras) y la promesa termina antes del segundo 8
    if not es_carrusel and escenas[0][1] and not escenas[0][1].startswith("["):
        n0 = C.palabras_habladas(escenas[0][1])
        if n0 > 8:
            falla(gid, "R21 gancho largo", f"{n0} palabras en el gancho: «{escenas[0][1][:80]}»")
    # R05 · frases cortas (hasta ~16 palabras)
    for frase in re.split(r"(?<=[.?!:'])\s+|'\s|\s'", re.sub(r"\(.*?\)|\b(V\d|Vendedor \d[^:']*|Jefe de taller|Jefe|Los dos|Cliente|Vendedor real): ", "", voz)):
        n = len(re.findall(r"\w+", frase))
        if n > 18 and "[" not in frase:
            falla(gid, "R05 frase larga", f"{n} palabras: «{frase[:90]}…»")
    # R06 · texto en pantalla corto (se lee en un celular)
    for e in escenas:
        if e[3] and e[3] != LEGAL and len(e[3]) > (130 if es_carrusel else 62):
            falla(gid, "R06 texto en pantalla largo", f"{e[0]}: {len(e[3])} letras")
    # R07 · el nombre del auto llega tarde (no en el primer 40 % del video)
    if producto and not es_carrusel and tiempos[-1]:
        total = tiempos[-1][1]
        for e, t in zip(escenas, tiempos):
            if t and t[0] < 0.4 * total:
                for m in MODELOS:
                    if re.search(rf"\b{re.escape(m)}\b", e[1] + " " + e[3]):
                        falla(gid, "R07 nombre tarde", f"'{m}' aparece en {e[0]} (de {total} s)")
    # R08 · un solo pedido comercial, con la frase exacta (educar y vender); entretener no lo dice en la voz
    if g["objetivo"] in ("Educar", "Vender") and not es_carrusel and gid not in ("E28",):
        n = voz.count(CTA[:-1])
        if n != 1:
            falla(gid, "R08 un solo CTA", f"la frase del CTA aparece {n} veces en la voz")
    if g["objetivo"] == "Entretener" and "Pedinos precio" in voz and gid not in ("E18",):
        falla(gid, "R08 CTA en entretener", "el pedido comercial está en la voz")
    # R09 · marcas ajenas, tilde, frases prohibidas
    if re.search(MARCAS_AJENAS, todo):
        falla(gid, "R09 marca ajena", ", ".join(sorted(set(re.findall(MARCAS_AJENAS, todo)))))
    if re.search(r"Valpara[íÍ]so", todo + g["descripcion"] + g.get("fijado", "")):
        falla(gid, "R09 tilde", "Valparaiso con tilde")
    if re.search(r"sin inter[eé]s|el mejor|el más completo|995", todo, re.I):
        falla(gid, "R09 frase prohibida", re.search(r"sin inter[eé]s|el mejor|el más completo|995", todo, re.I).group(0))
    if re.search(r"\bsedán\b", " ".join(e[1] + e[3] for e, t in zip(escenas, tiempos) if t and t[0] < 10)) and "Eado" in g["pieza"]:
        falla(gid, "R09 sedán al principio", "dice 'sedán' en los primeros 10 s del Eado")
    # R10 · legal: si hay precio, cuota, tasa o CFT, va la placa legal
    if re.search(r"precio en pesos|\$\s?\[PRECIO|\d+ cuotas|cuotas de|TNA|CFT|tasa (fija )?0|tasa cero|\banticipo\b", voz + " " + pantalla, re.I) and g["objetivo"] != "Entretener":
        if not any(e[3] == LEGAL for e in escenas) and "Legal completo" not in g["descripcion"]:
            falla(gid, "R10 legal", "habla de precio o cuota sin placa legal")
    # R11 · lo honesto: las piezas de producto dicen una limitación en voz alta
    if producto and not evento and not es_carrusel:
        if not g.get("honesto"):
            falla(gid, "R11 honesto", "no tiene limitación honesta")
        elif not re.search(r"honesto|ojo|pero|la que no|no es para|no tiene|no se enchufa|no entra|no alcanza|faltan", voz, re.I):
            falla(gid, "R11 honesto", "la limitación no se dice en la voz")
    # R12 · números con fuente: si hay números en la voz o en pantalla, hay fuentes o 'estimado'
    nums = re.findall(r"\d[\d.,]*", re.sub(r"\[.*?\]", "", voz + " " + pantalla))
    nums = [n for n in nums if n not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "0", "100", "360", "4x4", "4x2", "14", "19", "30", "11", "12", "15", "20", "22")]
    if nums and not g.get("fuentes") or (nums and g.get("fuentes") in ("—", "")):
        falla(gid, "R12 números sin fuente", f"números {nums[:6]} sin fuentes")
    estimadas = [c for c in re.findall(r"\bC\d+[A-Z]?", g.get("fuentes", "")) if c not in ("C9", "C11", "C11L", "C12", "C13", "C14", "C17")]
    if estimadas and not re.search(r"estimad|ejemplo", (g["descripcion"] + pantalla).lower()):
        falla(gid, "R12 estimado", "usa una cuenta propia y no dice 'estimado'")
    # R13 · descripción: primera línea = gancho y no adelanta el nombre del auto; Córdoba; máx. 5 hashtags con #AutosCordoba
    primera = g["descripcion"].strip()[:125]  # lo que se ve antes del 'más'
    if producto and any(re.search(rf"\b{re.escape(m)}\b", primera) for m in MODELOS):
        falla(gid, "R13 descripción", f"la primera línea nombra el auto: «{primera[:80]}»")
    if "Córdoba" not in g["descripcion"]:
        falla(gid, "R13 descripción", "no nombra Córdoba")
    tags = g.get("hashtags", "").split()
    if len(tags) > 5 or (tags and "#AutosCordoba" not in tags):
        falla(gid, "R13 hashtags", f"{len(tags)} hashtags · #AutosCordoba: {'#AutosCordoba' in tags}")
    # R14 · compartir: entretener y educar piden mandarlo a alguien
    if g["objetivo"] in ("Entretener", "Educar") and not evento and not re.search(r"mandá(selo|melo)|compart|guardalo", (g["descripcion"] + voz).lower()):
        falla(gid, "R14 compartir", "no pide que lo manden o lo guarden")
    # R15 · espacios para completar: solo los que no se pueden inventar
    for e in escenas:
        for campo in (e[1], e[3]):
            for ph in re.findall(r"\[([^\]]*)\]", campo or ""):
                if not re.search(PERMITIDOS, ph.lower()):
                    falla(gid, "R15 espacio para completar", f"[{ph}] en {e[0]}")
    # R22 · el pedido va encima del pago (sin placa final aparte)
    ult = escenas[-1]
    if not es_carrusel and ("Pedinos precio" in (ult[1] or "") or "PEDINOS PRECIO" in (ult[3] or "")) and "Encima del pago" not in (ult[2] or ""):
        falla(gid, "R22 pedido encima del pago", "la última escena no dice que el pedido va encima del pago")
    # R24 · 'sedán' nunca en la voz de las piezas del Eado
    if "Eado" in (g["pieza"] + g["idea"] + g["aparece"]) and re.search(r"\bsedán\b", voz):
        falla(gid, "R24 sedán", "la voz dice 'sedán' en una pieza del Eado")
    # R25 · los ajustes del día no alargan la voz del gancho
    if re.search(r"en la primera frase", extra.get("ajuste", "")):
        falla(gid, "R25 ajuste", "el ajuste del día agrega texto a la voz del gancho")
    # R16 · palabras difíciles en la voz (se explican o se sacan)
    voz_sin_nombres = re.sub(r"H6 PRO HEV|PRO HEV|Jolion HEV|ORA 05 HEV", "", voz)
    explicado = re.search(r"luz común|la de tu casa|la de siempre", voz)
    for j in sorted(set(re.findall(JERGA, voz_sin_nombres))):
        if j in ("monofásica", "trifásica") and explicado:
            continue
        falla(gid, "R16 palabra difícil en la voz", j)


def revisar():
    vistos = Counter()
    codigos = Counter()
    temas = []
    for fecha, hora, formato, gid, extra in P.PUBLICA:
        g = C.pieza_del_dia(gid, extra)
        revisar_pieza(fecha, gid, g, extra)
        vistos[gid] += 1
        if g.get("codigo"):
            codigos[g["codigo"]] += 1
        temas.append((fecha, gid, g))
    # R17 · una palabra clave por publicación (para saber qué video trajo cada consulta)
    for k, n in codigos.items():
        if n > 1:
            falla("—", "R17 palabra clave repetida", f"{k} se usa en {n} publicaciones")
    # R18 · nada se publica dos veces
    for gid, n in vistos.items():
        if n > 1:
            falla(gid, "R18 repetida", f"se publica {n} veces")
    # R19 · el mismo tema no se repite en menos de 10 días
    claves = {"auxilio": r"rueda de auxilio|kit", "nafta vs luz": r"luz de (tu )?casa|kWh|de luz", "garantía": r"garantía"}
    for tema, rx in claves.items():
        fechas = [(f, gid) for f, gid, g in temas if re.search(rx, texto_voz(g), re.I)]
        for (f1, a), (f2, b) in zip(fechas, fechas[1:]):
            if (f2 - f1).days < 7:
                falla(f"{a}/{b}", "R19 tema repetido", f"'{tema}' el {f1:%d/%m} y el {f2:%d/%m}")
    # R23 · el mismo dato del mismo auto no se repite en menos de 7 días
    for (f1, a, g1), (f2, b, g2) in [(x, y) for i, x in enumerate(temas) for y in temas[i + 1:]]:
        if 0 < (f2 - f1).days < 7 and not (a.startswith("CAR") or b.startswith("CAR")):
            d1 = {t for t in re.findall(r"\b[A-Z0-9]+-[0-9X]+\b", g1.get("fuentes", "")) if not t.startswith("GEN")}
            d2 = {t for t in re.findall(r"\b[A-Z0-9]+-[0-9X]+\b", g2.get("fuentes", "")) if not t.startswith("GEN")}
            if d1 & d2:
                falla(f"{a}/{b}", "R23 dato repetido", f"{', '.join(sorted(d1 & d2))} el {f1:%d/%m} y el {f2:%d/%m}")
    # R30 · el gancho B no nombra el auto ni usa superlativos, y entra en el cuadro 0
    for fecha, hora, formato, gid, extra in P.PUBLICA:
        gb = extra.get("gancho_b") or C.GUION[gid].get("gancho_b") or ""
        if any(re.search(rf"\b{re.escape(m)}\b", gb, re.I) for m in MODELOS):
            falla(gid, "R30 gancho B", f"nombra el auto: «{gb}»")
        if re.search(r"\bm[áa]s (barat|accesib|complet|vendid|segur|rápid|eficien)|\bel mejor\b|\bla mejor\b", gb, re.I):
            falla(gid, "R30 gancho B", f"superlativo sin prueba: «{gb}»")
        if len(gb.replace("[PRECIO EN PESOS]", "$00.000.000")) > 70:
            falla(gid, "R30 gancho B", f"{len(gb)} letras: no entra grande en el cuadro 0")
    # R26 · una sola salida fuera del local por día de grabación
    for f, items in P.GRABA.items():
        fuera = [gid for gid, nota in items if gid != "—" and re.search(r"campo|corralón|viaje|cochera real|electricista", (nota + " " + C.GUION[gid]["tomas"]).lower())]
        if len(fuera) > 1:
            falla("—", "R26 salidas", f"{f:%d/%m} tiene {len(fuera)} grabaciones fuera del local: {', '.join(fuera)}")
    # R27 · la grabación de banco no repite piezas ya publicadas
    publicadas = {gid for _, _, _, gid, _ in P.PUBLICA}
    for f, items in P.GRABA.items():
        for gid, nota in items:
            if gid == "—":
                for otro in re.findall(r"\b([EDV]\d\d)\b", nota):
                    if otro in publicadas:
                        falla("—", "R27 banco", f"{f:%d/%m}: {otro} ya se publica en el calendario")
    # R28 · la lista de palabras del 28/11 va en orden de fecha y está completa
    fechas = [x[0] for x in P.PUBLICA]
    if fechas != sorted(fechas):
        falla("—", "R28 orden", "las publicaciones no están en orden de fecha")
    # R29 · ningún día edita más de 2 piezas
    for f, items in C.EDITA.items():
        if len(items) > 2:
            falla("—", "R29 carga de edición", f"{f:%d/%m} edita {len(items)} piezas")
    # R20 · cada grabación tiene a lo sumo 4 piezas y ningún día se edita más de 2
    for f, items in P.GRABA.items():
        if len([i for i in items if i[0] != "—"]) > 4:
            falla("—", "R20 carga", f"{f:%d/%m} graba {len(items)} piezas")
    return FALLAS


if __name__ == "__main__":
    fallas = revisar()
    por_regla = Counter(r for _, r, _ in fallas)
    for gid, regla, det in fallas:
        print(f"{gid:6} {regla:32} {det}")
    print(f"\n{len(fallas)} fallas", dict(por_regla))
    sys.exit(1 if fallas else 0)
