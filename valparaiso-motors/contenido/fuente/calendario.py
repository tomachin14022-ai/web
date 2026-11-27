"""Arma el calendario final de Valparaiso Motors: UNA sola hoja, una fila por día, con todo lo que hay que hacer.

Uso:
    python3 calendario.py [carpeta_temporal]
Escribe ../Calendario Valparaiso Motors.xlsx y, en la carpeta temporal (por defecto /tmp), el .md y el .docx
de la versión para leer; después se pasa a PDF con LibreOffice (ver LEEME.md).
"""
import datetime as dt
import math
import os
import re
import sys
import urllib.parse

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import calendario_plan as P  # noqa: E402
import datos_guiones as DG  # noqa: E402
import guiones as G  # noqa: E402
from guiones_comun import FIJADO, LEGAL, MSG  # noqa: E402
import copy  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, "..", "Calendario Valparaiso Motors.xlsx")
TMP = sys.argv[1] if len(sys.argv) > 1 else "/tmp"

BORDO, TINTA, GRIS, PAPEL = "801628", "151415", "8A8580", "F6F3EE"
F = "Arial"
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

GUION = {g["id"]: g for g in G.GUIONES}
GUION.update(P.EXTRA)
DATO = {x[0]: x for x in DG.DATOS}
CUENTA = {x[0]: x for x in DG.CUENTAS}
SUP = {x[0]: x[2] for x in DG.SUPUESTOS}
ETIQ = {"PrecioKWhNoche": "kWh de noche (${})", "PrecioKWh": "kWh (${})", "PrecioNafta": "nafta (${})", "PrecioCafe": "café (${})",
        "KmDia": "{} km por día", "DiasMes": "{} días", "LNaftero": "{} L", "LHibrido": "{} L", "KWhElectrico": "{} kWh",
        "KWhEnchufable": "{} kWh", "KmEnchufable": "{} km", "PeajeCabina": "cabina (${})", "PeajeTele": "TelePEAJE (${})"}


PALABRAS_POR_SEGUNDO = 2.7  # voz de ElevenLabs a ×1,15 o un vendedor hablando claro


def palabras_habladas(dice):
    """Palabras que se dicen de verdad: sin indicaciones entre paréntesis ni quién habla."""
    if not dice or dice.startswith("["):
        return len(re.findall(r"\w+", re.sub(r"\[.*?\]", "", dice or ""))) if dice and not dice.startswith("[") else 0
    limpio = re.sub(r"\(.*?\)|\b(V\d|Vendedor \d[^:']*|Jefe de taller|Jefe|Los dos|'Cliente'|Vendedor real): ", "", dice)
    return len(re.findall(r"\w+", limpio))


def retimar(escenas):
    """Los tiempos salen de lo que se dice: cada escena dura lo que tarda su voz (mínimo el tiempo pensado para la imagen)."""
    nuevas, t = [], 0
    for e in escenas:
        m = re.match(r"(\d+)\s*[–-]\s*(\d+)\s*s", e[0])
        if not m:
            nuevas.append(e)
            continue
        orig = int(m.group(2)) - int(m.group(1))
        necesita = math.ceil(palabras_habladas(e[1]) / PALABRAS_POR_SEGUNDO) if e[1] else 0
        dur = max(orig, necesita) if t > 0 else max(2, necesita)
        nuevas.append((f"{t}–{t + dur} s",) + tuple(e[1:]))
        t += dur
    return nuevas, t


def pieza_del_dia(gid, extra):
    """El guion del banco con lo que cambia ese día: la palabra clave única de la publicación."""
    g = copy.deepcopy(GUION[gid])
    if extra.get("escenas"):
        g["escenas"] = extra["escenas"]
    # cambios del día (fecha, feriado, festival): ya escritos en el guion y en la descripción, listos para pegar
    for viejo, nuevo in extra.get("cambios", []):
        antes = (list(g["escenas"]), g["descripcion"])
        g["escenas"] = [tuple(x.replace(viejo, nuevo) if isinstance(x, str) else x for x in e) for e in g["escenas"]]
        g["descripcion"] = g["descripcion"].replace(viejo, nuevo)
        assert (g["escenas"], g["descripcion"]) != antes, f"{gid}: no se encontró «{viejo}»"
    if not gid.startswith("CAR"):
        g["escenas"], total = retimar(g["escenas"])
        g["formato"] = re.sub(r"\d+\s*[–-]\s*\d+\s*s|\d+ s", f"~{total} s", g["formato"], count=1)
    if extra.get("compartir"):
        g["descripcion"] = g["descripcion"].rstrip() + " " + extra["compartir"]
    # El pedido va encima del pago (CLAUDE.md, fórmula de retención): sin placa final aparte, botón 1,5 s
    ult = g["escenas"][-1]
    if not gid.startswith("CAR") and ("Pedinos precio" in (ult[1] or "") or "PEDINOS PRECIO" in (ult[3] or "")):
        ve = re.sub(r"^Logo chico\.\s*", "", ult[2] or "").strip()
        ve = "Encima del pago: sigue a la vista la imagen de la escena anterior; el botón bordó 'PEDINOS PRECIO Y FINANCIACIÓN' entra 1,5 s y el logo chico va dentro de la zona segura." + (" " + ve if ve else "")
        g["escenas"][-1] = (ult[0], ult[1], ve, ult[3], ult[4])
    nuevo = extra.get("codigo")
    if nuevo and nuevo != g.get("codigo"):
        viejo = g.get("codigo") or ""
        rx = re.compile(rf"((?:comentá|Comentá|COMENTÁ|del video|DEL VIDEO) ){re.escape(viejo)}\b") if viejo else None

        def sub(t):
            return rx.sub(lambda m: m.group(1) + nuevo, t) if (rx and isinstance(t, str)) else t
        g["escenas"] = [tuple(sub(x) for x in e) for e in g["escenas"]]
        g["descripcion"] = sub(g["descripcion"])
        g["codigo"] = nuevo
        g["fijado"] = FIJADO.format(k=nuevo) if not extra.get("fijado") else extra["fijado"]
        if not g.get("mensaje") or "vengo del video" in g.get("mensaje", "") or viejo in g.get("mensaje", ""):
            base = g.get("mensaje") or MSG.format(k=nuevo)
            g["mensaje"] = re.sub(rf"\b{re.escape(viejo)}\b", nuevo, base) if viejo else MSG.format(k=nuevo)
    return g


def num(x, dec=0):
    s = f"{x:,.{dec}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def num_corto(v):
    if v == int(v):
        return num(v)
    return num(v, 2).rstrip("0").rstrip(",")


def cuenta_legible(cid):
    _, para, que, formula, fmt, unidad, dice = CUENTA[cid]
    expr = formula[1:]
    valor = eval(expr, {}, dict(SUP))  # fórmulas propias de datos_guiones.py
    texto = re.sub(r"(\d+)\.(\d+)", r"\1,\2", expr)
    texto = texto.replace("*", " × ").replace("/", " ÷ ").replace("-", " − ").replace("+", " + ")
    for nombre in sorted(ETIQ, key=len, reverse=True):
        texto = texto.replace(nombre, ETIQ[nombre].format(num_corto(SUP[nombre])))
    if "%" in fmt:
        res = f"{num(valor * 100)} %"
    elif "$" in fmt:
        res = "$" + num(valor)
    else:
        res = num_corto(round(valor, 1)) if "0.0" in fmt else num(valor)
    return f"{cid} ({que}): {texto} = {res} {unidad if '$' not in fmt else ''}".strip()


def ids_de(fuentes):
    return re.findall(r"\b([A-Z0-9]+-[0-9X]+|C\d+[A-Z]?)\b", fuentes or "")


def limpio_legal(t):
    return "PLACA LEGAL 5 s (el texto está en 'Antes de publicar')" if t == LEGAL else t


def ganchos(g, extra):
    """Lo que va en el cuadro 0 (el mismo texto de la primera escena) y la variante B para el reel de prueba."""
    t, dice, ve, texto, sonido = g["escenas"][0]
    if g["id"].startswith("CAR"):
        a = f"placa 1: «{texto}»"
    else:
        a = f"en pantalla «{texto}»" + (f" + voz «{dice}»" if dice else " (sin voz: solo música)")
    gb = extra.get("gancho_b") or g.get("gancho_b")
    b = f"en pantalla «{gb}» (cambia solo el texto del cuadro 0; la voz y el resto del video quedan igual)" if gb else ""
    return a, b


def render_guion(g, extra, corto=False):
    out = [f"[{g['id']}] {g['pieza'].upper()}",
           f"{g['objetivo']} · Para: {g['publico']} · {g.get('estructura', '')} · {g['formato']} · Aparece: {g['aparece']}",
           f"LA IDEA: {g['idea']}",
           f"GANCHO (cuadro 0): {ganchos(g, extra)[0]}"]
    gb = ganchos(g, extra)[1]
    if gb:
        out.append(f"GANCHO B (para probar en un reel de prueba): {gb}")
    if extra.get("ajuste"):
        out.append(f"AJUSTE DE HOY: {extra['ajuste']}")
    out.append("ESCENAS (DICE = lo que se dice · VE = lo que se ve · PANTALLA = texto en pantalla · SONIDO)")
    for t, dice, ve, texto, sonido in g["escenas"]:
        partes = [f"▸ {t}"]
        if dice:
            partes.append(f"DICE: {dice}")
        if ve:
            partes.append(f"VE: {ve}")
        if texto:
            partes.append(f"PANTALLA: {limpio_legal(texto)}")
        if sonido:
            partes.append(f"SONIDO: {sonido}")
        out.append(" · ".join(partes))
    if g.get("honesto"):
        out.append(f"LO HONESTO (se dice entero): {g['honesto']}")
    if g.get("por_que") and not corto:
        out.append(f"POR QUÉ FUNCIONA: {g['por_que']}")
    return "\n".join(out)


def para_pegar(g):
    desc = re.sub(r"\[Legal completo[^\]]*\]", "+ texto legal (ver 'Antes de publicar')", g["descripcion"])
    out = [f"DESCRIPCIÓN: {desc}"]
    if g.get("hashtags"):
        out.append(f"HASHTAGS: {g['hashtags']}")
    if g.get("fijado"):
        out.append(f"COMENTARIO FIJADO: {g['fijado']}")
    if g.get("codigo"):
        out.append(f"PALABRA CLAVE: {g['codigo']}")
    if g.get("mensaje"):
        out.append(f"MENSAJE DE WHATSAPP YA ESCRITO: \"{g['mensaje']}\"")
    return "\n".join(out)


def antes_de_publicar(g, extra):
    out = []
    if g.get("codigo"):
        out.append(f"· La palabra {g['codigo']} cargada en el mensaje automático y probada desde una cuenta que no sigue.")
    out.append("· El dueño aprobó la hoja de cuadros (gancho, mitad y final).")
    if g.get("ojo"):
        out.append(f"· Ojo: {g['ojo']}")
    if extra.get("gancho_b"):
        out.append(f"· Gancho B: {P.PRECIO_PRIMERO}")
    ids = ids_de(g.get("fuentes", ""))
    cuentas = [i for i in ids if i in CUENTA]
    datos = [i for i in ids if i in DATO]
    if cuentas:
        out.append("· Cuentas a rehacer con el precio del día (en pantalla dicen 'estimado'):")
        out += [f"   {cuenta_legible(c)}" for c in cuentas]
    if datos:
        out.append("· Datos y fuentes:")
        for i in datos:
            _, mod, dato, frase, tipo, fte, url, fecha, ojo = DATO[i]
            linea = f"   {i} · {dato}: {tipo.split(' (')[0].lower()} ({fte}, {fecha})"
            if ojo:
                linea += f". Ojo: {ojo}"
            out.append(linea)
    if any(e[3] == LEGAL for e in g["escenas"]) or "[Legal completo" in g.get("descripcion", ""):
        out.append(f"· {LEGAL}")
    return "\n".join(out)


# ---------------------------------------------------------------- calendario
def es_habil(f):
    return f.weekday() < 5 and f not in P.FERIADOS


def dias():
    f = P.INICIO
    while f <= P.FIN:
        yield f
        f += dt.timedelta(days=1)


GRABADO = {}
for f, items in P.GRABA.items():
    for gid, _ in items:
        GRABADO.setdefault(gid, []).append(f)

PUB_POR_DIA = {}
EDITA = {}
for fecha, hora, formato, gid, extra in P.PUBLICA:
    PUB_POR_DIA.setdefault(fecha, []).append((hora, formato, gid, extra))
    ids_edicion = [gid] + ([extra["plan_b"]] if extra.get("plan_b") else [])
    for i in ids_edicion:
        recs = [r for r in GRABADO.get(i, []) if r <= fecha]
        if not recs:
            continue
        r = max(recs)
        candidatos = [x for x in (r + dt.timedelta(days=k) for k in range(1, (fecha - r).days)) if es_habil(x) and x not in (P.VIP, P.DIA_D)]
        pref = [x for x in candidatos if x <= fecha - dt.timedelta(days=2)]
        pref = [x for x in pref if x not in P.MEDIO_DIA] or pref
        opciones = pref or candidatos
        # el día con menos ediciones ya asignadas; a igual carga, el más cercano a la publicación
        if i.startswith("CAR"):
            e = r  # el carrusel se arma y se revisa el mismo día
        elif candidatos:
            # 2 días antes si se puede; si ese día ya tiene 2 ediciones, el día anterior a la publicación
            e = min(candidatos, key=lambda x: (len(EDITA.get(x, [])) >= 2, x not in opciones, len(EDITA.get(x, [])), -x.toordinal()))
        elif es_habil(fecha) and r != fecha:
            e = fecha  # se edita a la mañana y se publica a la noche (nunca el día de la inauguración)
        else:
            e = r
        EDITA.setdefault(e, []).append((i, fecha))

PUBLICA_EN = {}
for fecha, hora, formato, gid, extra in P.PUBLICA:
    PUBLICA_EN.setdefault(gid, fecha)
    if extra.get("plan_b"):
        PUBLICA_EN.setdefault(extra["plan_b"], fecha)


def semana_rutinas():
    """Primer día hábil de cada semana → rutina del lunes; último día hábil → rutina del viernes."""
    lunes, viernes = set(), set()
    semanas = {}
    for f in dias():
        if es_habil(f):
            semanas.setdefault(f.isocalendar()[:2], []).append(f)
    for fs in semanas.values():
        if min(fs) != P.INICIO:  # el primer día (viernes 27/11) es de puesta a punto: no hay semana anterior que medir
            lunes.add(min(fs))
        cierre = [x for x in fs if x not in (P.VIP, P.DIA_D, P.INICIO)]  # la noche VIP no lleva la rutina de cierre: se adelanta
        if cierre:
            viernes.add(max(cierre))
    return lunes, viernes


LUNES, VIERNES = semana_rutinas()


def rutina_lunes(f):
    t = ("Rutina de inicio de semana (1 h): tablero de la semana anterior (alcance y % de Córdoba, salto a los 3 s, envíos por mensaje, comentarios con la palabra, "
         "chats con código, turnos, ventas) · escucha de 30 min (comentarios, mensajes y preguntas de Mercado Libre: anotar las preguntas textuales para 'Respuesta a @') · "
         "cambiar a 'Escribinos por WhatsApp (link en la bio)' el comentario fijado de las piezas de hace más de 7 días")
    if f >= dt.date(2027, 1, 4):
        t += " · anuncio A4: poner el reel de la semana con menos salto a los 3 s"
    t += (" · si salió una noticia que cambia la cuota (impuestos, una línea de crédito, una baja de precios): grabar 'Noticia de bolsillo' y publicarla dentro de las 48 h "
          "en lugar de la pieza de Educar de la semana (gancho '[la noticia en una línea]: ¿qué cambia para tu cuota?', la cuenta antes y después con un auto del salón, "
          "lo que todavía no se sabe, placa legal y el pedido de siempre)")
    return t + "."


RUTINA_VIERNES = ("Rutina de cierre de semana: publicación en el Perfil de Google con la pieza de la semana · Mercado Libre: precio del día, video del modelo y preguntas pendientes · "
                  "dejar listas las tomas y los autos de la próxima grabación.")


def estado_whatsapp(gid):
    """Lo que dice el estado de WhatsApp: ofrece lo que la pieza deja abierto para cada uno."""
    g = GUION[gid]
    texto = (g["pieza"] + " " + g["idea"]).lower()
    if gid == "E08":
        return "Si querés saber cuál entra en tu cochera, escribime"
    if gid.startswith("CAR2") or re.search(r"cuota|financ|tasa|crédito|precio del aviso|aguinaldo", texto):
        return "Si querés la cuota para tu caso, escribime"
    if re.search(r"\bC\d", g.get("fuentes", "")):
        return "Si querés la cuenta con tu caso, escribime"
    if gid in ("E16", "E17", "E18", "E19", "V12"):
        return "Te espero en el local nuevo: escribime y te paso la ubicación"
    if g["objetivo"] == "Vender" or re.search(r"\b(eado|ora 0[35]|h6|h7|deepal|s05|cs55|jolion|outlander|l200|easy 3|tank)\b", texto + " " + g["aparece"].lower()):
        return "Si querés verlo en persona, escribime y te paso un turno"
    return "Si tenés una duda con tu caso, escribime"


def todos_los_dias(f, pubs, idx):
    out = []
    if pubs:
        for hora, formato, gid, extra in pubs:
            out.append(f"Historias: a las {hora}, compartir la pieza de hoy. Después: {extra.get('historia', 'una pregunta sobre el tema del video')}")
        out.append(f"Estado de WhatsApp: el mismo video + '{estado_whatsapp(pubs[0][2])}'.")
    elif f not in (P.VIP, P.DIA_D):
        i = P.DATOS_HISTORIAS[idx % len(P.DATOS_HISTORIAS)]
        _, mod, dato, frase, tipo, fte, url, fecha, ojo = DATO[i]
        out.append(f"Historia del día: foto o video corto del {mod} con el dato \"{frase}\" ({fte}) y una encuesta. Más una del día a día del equipo.")
    if f == P.VIP:
        out.append("Historias de la noche (solo personas con autorización): la llegada, un clip de 15 s de las palabras, el corte de cinta y el recorrido. Guardia de WhatsApp toda la noche.")
        return "\n".join(out)
    if f == P.DIA_D:
        out.append("Historias cada hora: la apertura, las pruebas de manejo (sin patentes), la actividad de los chicos (con firma de los padres) y el aviso del vivo de las 11. Guardia de WhatsApp de 9 a 19 h.")
        return "\n".join(out)
    if f == P.DIA_D + dt.timedelta(days=1):
        out.append("Guardia reforzada de WhatsApp de 10 a 13 h: las consultas de la inauguración no esperan al lunes.")
    elif f in P.FERIADOS or f.weekday() == 6:
        out.append("Historias programadas; los mensajes se contestan a la mañana.")
    elif f.weekday() == 5:
        out.append("Guardia de WhatsApp de 9 a 13 h · responder comentarios.")
    else:
        out.append("Responder comentarios y mensajes en menos de 1 h (9 a 20 h) · cargar cada consulta en la planilla con su palabra clave y A/B/C · preguntas de Mercado Libre.")
    return "\n".join(out)


FILAS = []
idx_hist = 0
for f in dias():
    pubs = PUB_POR_DIA.get(f, [])
    fila = dict(fecha=f, dia=DIAS[f.weekday()], contexto=P.contexto(f))
    publica, guion, pegar, antes, link_msgs = [], [], [], [], []
    quien = set()
    for hora, formato, gid, extra in pubs:
        g = pieza_del_dia(gid, extra)
        publica.append(f"{hora} · {formato}\n{g['objetivo'].upper()} · [{gid}] {g['pieza']}\n{g['formato']} · Aparece: {g['aparece']}")
        bloque = render_guion(g, extra)
        if extra.get("plan_b"):
            bloque += "\n\nPLAN B (si no hay colaboración):\n" + render_guion(GUION[extra["plan_b"]], {}, corto=True)
        guion.append(bloque)
        pegar.append(para_pegar(g))
        antes.append(antes_de_publicar(g, extra))
        if g.get("mensaje"):
            link_msgs.append(g["mensaje"])
        quien.add("Contenido")
        for rol in ("Vendedor 1", "Vendedor 2", "Jefe de taller", "Técnico", "Administración", "Dueño"):
            if rol.lower() in g["aparece"].lower():
                quien.add(rol)
    if not pubs:
        idx_hist += 1
    graba = []
    for gid, nota in P.GRABA.get(f, []):
        if gid == "—":
            graba.append(nota)
            quien.add("Contenido")
            continue
        g = GUION[gid]
        pub = PUBLICA_EN.get(gid)
        cuando = f" · sale el {DIAS[pub.weekday()].lower()} {pub.strftime('%d/%m')}" if pub else ""
        verbo = "SE ARMA" if gid.startswith("CAR") else "SE GRABA"
        graba.append(f"{verbo} [{gid}] {g['pieza']}{cuando}\n   Aparece: {g['aparece']}\n   Tomas: {g['tomas']}" + (f"\n   Nota: {nota}" if nota else ""))
        quien.add("Contenido")
        for rol in ("Vendedor 1", "Vendedor 2", "Jefe de taller", "Técnico", "Dueño"):
            if rol.lower() in g["aparece"].lower():
                quien.add(rol)
    ESPECIALES = {"E17", "E18", "E19", "E25", "E09", "E10", "D04", "D19a", "D19b", "E28", "V06"}
    if graba and f.weekday() < 5 and any(gid not in ESPECIALES and not gid.startswith("CAR") and gid != "—" or gid == "—" for gid, _ in P.GRABA.get(f, [])):
        graba.insert(0, "Bloque de grabación 9 a 12 h (el de primer contacto no graba: sigue con WhatsApp). Vertical 4K, foco y exposición bloqueados, corbatero, 3 tomas de cada gancho.")
    edita = []
    for gid, pub in EDITA.get(f, []):
        g = GUION[gid]
        cuando = f" · sale el {DIAS[pub.weekday()].lower()} {pub.strftime('%d/%m')}"
        if gid.startswith("CAR"):
            como = ("revisar las placas en el celular (1080x1350, texto legible, nada importante en el borde de abajo, 'deslizá →' chico abajo a la derecha en todas menos la última, "
                    "logo sin caja en la última) y mandárselas al dueño; se publica con su OK.")
        else:
            animado = "elevenlabs" in g["aparece"].lower()  # 'animado con su voz' es la voz real del vendedor
            voz = "voz de ElevenLabs ×1,15 sin cambiar el tono" if animado else "cortar silencios y respiraciones (sin acelerar la voz real)"
            como = (f"editar (subtítulos palabra por palabra, {voz}, un cambio grande cada 2–3 s y algo que aparece cada 0,3 s, "
                    "música 8 dB debajo de la voz, placa final con el logo dentro de la zona segura) y mandar al dueño la hoja de cuadros; se publica con su OK.")
        edita.append(f"[{gid}] {g['pieza']}{cuando}: {como}")
        quien.add("Contenido")
    tareas = []
    if f in LUNES:
        tareas.append(rutina_lunes(f))
    for resp, texto in P.T.get(f, []):
        tareas.append(f"{texto} ({resp})")
        quien.update(x.strip() for x in resp.replace("+", ",").split(","))
    if f in VIERNES:
        tareas.append(RUTINA_VIERNES)
    if f in LUNES or f in VIERNES:
        quien.add("Contenido")
    fila.update(publica="\n\n".join(publica), guion="\n\n══════════\n\n".join(guion), pegar="\n\n".join(pegar),
                antes="\n\n".join(antes), graba="\n\n".join(graba), edita="\n".join(edita), tareas="\n\n".join(tareas),
                diario=todos_los_dias(f, pubs, idx_hist), quien=", ".join(sorted(quien | {"Primer contacto"})),
                mensaje=link_msgs[0] if link_msgs else "", gids=[p[2] for p in pubs])
    FILAS.append(fila)


# ---------------------------------------------------------------- planilla (una sola hoja)
def fuente(**kw):
    base = dict(name=F, size=9, color=TINTA)
    base.update(kw)
    return Font(**base)


def armar_xlsx():
    wb = Workbook()
    ws = wb.active
    ws.title = "Calendario"
    ws.sheet_view.showGridLines = False
    cols = [("Fecha", 11), ("Día", 10), ("Qué pasa ese día", 24), ("Hoy se publica", 30), ("Guion completo", 100),
            ("Para pegar al publicar", 46), ("Probar el link", 10), ("Antes de publicar", 64), ("Hoy se graba", 54),
            ("Hoy se edita", 34), ("Inauguración, anuncios y otras tareas", 60), ("Todos los días", 42), ("Quién", 18), ("¿Hecho?", 9)]
    for i, (_, ancho) in enumerate(cols, start=1):
        ws.column_dimensions[chr(64 + i)].width = ancho
    ws["A1"] = "Calendario Valparaiso Motors · del viernes 27/11/2026 al domingo 28/02/2027"
    ws["A1"].font = Font(name=F, size=16, bold=True, color=BORDO)
    ws.merge_cells("A2:N2")
    ws["A2"] = ("CÓMO SE USA: cada fila es un día y tiene todo lo de ese día. Lo que se publica está con su guion completo (qué se dice, qué se ve, el texto en pantalla y el sonido), "
                "lo que hay que pegar y lo que hay que confirmar antes. 'Hoy se graba' y 'Hoy se edita' dicen qué se prepara para los días siguientes. "
                "La inauguración está puesta el sábado 19/12 (noche VIP el viernes 18/12): si cambia la fecha, se corren juntas las tareas que dicen 'Inauguración'. "
                "Las cuentas usan la nafta súper a $2.162 y el kWh de EPEC a $370,24 (noviembre): en 'Antes de publicar' está cada cuenta para rehacerla con el precio del día.")
    ws.merge_cells("A3:N3")
    ws["A3"] = ("REGLAS DE TODAS LAS PIEZAS: Valparaiso sin tilde · un solo pedido comercial: 'Pedinos precio y financiación de cualquiera de nuestros autos' · la palabra clave siempre como pedido de precio · "
                "el nombre del auto llega tarde y se repite escrito al final · cada número con su fuente o 'estimado' · cada pieza de producto dice en voz alta lo honesto · "
                "sin otras marcas ni bancos · precio en pesos con el precio sin impuestos nacionales y la placa legal 5 s · nunca 'sin interés' ni 'cuota fija' si ajusta por UVA o CER · "
                "clientes, invitados y chicos solo con autorización firmada · fotos y autos reales, nunca generados con IA · zona segura: nada importante arriba de 260 px, abajo de 1440 px ni a la derecha de 900 px.")
    for c in ("A2", "A3"):
        ws[c].alignment = Alignment(wrap_text=True, vertical="top")
        ws[c].font = fuente(size=9)
    ws.row_dimensions[2].height = 52
    ws.row_dimensions[3].height = 52
    ws.merge_cells("A4:D4")
    ws["A4"] = "Número de WhatsApp del concesionario (549 + característica + número, sin espacios):"
    ws["A4"].font = fuente(bold=True)
    ws["A4"].alignment = Alignment(horizontal="right", vertical="center")
    ws["E4"].fill = PatternFill("solid", fgColor="FFF2CC")
    ws["E4"].font = fuente(color="0000FF", bold=True)
    ws["E4"].number_format = "@"
    ws.row_dimensions[4].height = 20
    fino = Side(style="thin", color="D9D4CC")
    borde = Border(left=fino, right=fino, top=fino, bottom=fino)
    for i, (titulo, _) in enumerate(cols, start=1):
        c = ws.cell(row=5, column=i, value=titulo)
        c.font = Font(name=F, size=10, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor=BORDO)
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        c.border = borde
    ws.row_dimensions[5].height = 30
    fila = 6
    for x in FILAS:
        vals = [x["fecha"], x["dia"], x["contexto"], x["publica"], x["guion"], x["pegar"], None, x["antes"], x["graba"],
                x["edita"], x["tareas"], x["diario"], x["quien"], "No"]
        for k, val in enumerate(vals, start=1):
            c = ws.cell(row=fila, column=k, value=val)
            c.font = fuente(bold=(k in (1, 2)), size=9)
            c.alignment = Alignment(wrap_text=True, vertical="top")
            c.border = borde
        ws.cell(row=fila, column=1).number_format = "DD/MM/YYYY"
        if x["mensaje"]:
            enc = urllib.parse.quote(x["mensaje"])
            c = ws.cell(row=fila, column=7, value=f'=IF($E$4="","",HYPERLINK("https://wa.me/"&$E$4&"?text={enc}","Probar"))')
            c.font = fuente(color="0563C1", bold=True)
            c.alignment = Alignment(vertical="top")
        f = x["fecha"]
        color = None
        if f in (P.VIP, P.DIA_D):
            color = "F7E3E6"
        elif f in P.FERIADOS:
            color = "E4E1DC"
        elif f.weekday() >= 5:
            color = PAPEL
        if color:
            for k in range(1, 15):
                ws.cell(row=fila, column=k).fill = PatternFill("solid", fgColor=color)
        if x["publica"]:
            ws.cell(row=fila, column=4).fill = PatternFill("solid", fgColor="FBEFF1")
        if x["graba"]:
            ws.cell(row=fila, column=9).fill = PatternFill("solid", fgColor="FFF6D6")
        lineas = 1
        for k, ancho in ((5, 100), (8, 64), (11, 60), (9, 54), (6, 46), (12, 42), (4, 30), (10, 34)):
            texto = str(vals[k - 1] or "")
            n = sum(max(1, math.ceil(len(t) / (ancho * 1.15))) for t in texto.split("\n"))
            lineas = max(lineas, n)
        ws.row_dimensions[fila].height = min(409, max(30, lineas * 11.5 + 6))
        fila += 1
    ult = fila - 1
    dv = DataValidation(type="list", formula1='"No,Sí,En curso"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"N6:N{ult}")
    ws.conditional_formatting.add(f"A6:N{ult}", FormulaRule(formula=['$N6="Sí"'], fill=PatternFill("solid", fgColor="E3F1DF")))
    ws.freeze_panes = "C6"
    ws.auto_filter.ref = f"A5:N{ult}"
    ws.page_setup.orientation = "landscape"
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.print_title_rows = "5:5"
    ws.sheet_properties.tabColor = BORDO
    wb.save(SALIDA)
    return ult


# ---------------------------------------------------------------- versión para leer (Markdown → Word → PDF)
def md_celda(t):
    return (t or "").replace("|", "/").replace("\n", " ")


def armar_md():
    out = []
    w = out.append
    w('---\ntitle: "Calendario Valparaiso Motors"\nsubtitle: "Del viernes 27/11/2026 al domingo 28/02/2027 · un día por sección, con todo lo que hay que hacer"\nlang: es-AR\n---\n')
    w("**Cómo se usa.** Cada día tiene lo que se publica (con su guion completo), lo que hay que pegar, lo que hay que confirmar antes, lo que se graba, lo que se edita, las tareas y lo de todos los días. "
      "Es lo mismo que la planilla *Calendario Valparaiso Motors.xlsx* (una sola hoja), pensado para leer en el celular o imprimir. "
      "La inauguración está puesta el sábado 19/12 (noche VIP el viernes 18/12). Las cuentas usan la nafta súper a $2.162 y el kWh de EPEC a $370,24 (noviembre de 2026): se rehacen el día que se publica.\n")
    w("**Placa legal** (en toda pieza con precio o cuota, mínimo 5 segundos):\n")
    w("> " + LEGAL + "\n")
    mes_actual = None
    meses = {11: "Noviembre de 2026", 12: "Diciembre de 2026", 1: "Enero de 2027", 2: "Febrero de 2027"}
    for x in FILAS:
        f = x["fecha"]
        if f.month != mes_actual:
            mes_actual = f.month
            w(f"# {meses[f.month]}\n")
        titulo = f"{x['dia']} {f.strftime('%d/%m/%Y')}"
        w(f"## {titulo}" + (f" · {x['contexto']}" if x["contexto"] else "") + "\n")
        for (hora, formato, gid, extra) in PUB_POR_DIA.get(f, []):
            g = pieza_del_dia(gid, extra)
            w(f"### Se publica: {hora} · [{gid}] {g['pieza']}\n")
            w(f"**{g['objetivo']}** · {formato} · {g['formato']} · Aparece: {g['aparece']}\n")
            w(f"**La idea:** {g['idea']}\n")
            ga, gb = ganchos(g, extra)
            w(f"**Gancho (cuadro 0):** {ga}" + (f"  \n**Gancho B (para probar en un reel de prueba):** {gb}" if gb else "") + "\n")
            if extra.get("ajuste"):
                w(f"**Ajuste de hoy:** {extra['ajuste']}\n")
            for gg in [g] + ([GUION[extra["plan_b"]]] if extra.get("plan_b") else []):
                if gg is not g:
                    w(f"**Plan B: [{gg['id']}] {gg['pieza']}** · {gg['formato']} · Aparece: {gg['aparece']}  \n**Gancho (cuadro 0):** {ganchos(gg, {})[0]}\n")
                w("| Momento | Qué se dice | Qué se ve | Texto en pantalla | Sonido |")
                w("|---|---|---|---|---|")
                for t, dice, ve, texto, sonido in gg["escenas"]:
                    w(f"| {md_celda(t)} | {md_celda(dice)} | {md_celda(ve)} | {md_celda(limpio_legal(texto))} | {md_celda(sonido)} |")
                w("")
                if gg.get("honesto"):
                    w(f"**Lo honesto (se dice entero):** {gg['honesto']}\n")
                if gg.get("por_que"):
                    w(f"**Por qué funciona:** {gg['por_que']}\n")
            w("**Para pegar al publicar:**\n")
            for linea in para_pegar(g).split("\n"):
                w(f"- {linea}")
            w("")
            w("**Antes de publicar:**\n")
            for linea in antes_de_publicar(g, extra).split("\n"):
                w(("    - " + linea.strip()) if linea.startswith("   ") else ("- " + linea.lstrip("· ")))
            w("")
        for etiqueta, clave in (("Hoy se graba", "graba"), ("Hoy se edita", "edita"), ("Inauguración, anuncios y otras tareas", "tareas"), ("Todos los días", "diario")):
            if x[clave]:
                w(f"**{etiqueta}:**\n")
                for bloque in x[clave].split("\n"):
                    if bloque.strip():
                        w(("    - " + bloque.strip()) if bloque.startswith("   ") else ("- " + bloque.strip()))
                w("")
        w(f"**Quién:** {x['quien']}\n")
    ruta = os.path.join(TMP, "Calendario Valparaiso Motors.md")
    with open(ruta, "w") as fh:
        fh.write("\n".join(out) + "\n")
    return ruta


if __name__ == "__main__":
    ult = armar_xlsx()
    md = armar_md()
    print("ok", os.path.abspath(SALIDA), ult - 5, "días ·", len(P.PUBLICA), "publicaciones ·", md)
