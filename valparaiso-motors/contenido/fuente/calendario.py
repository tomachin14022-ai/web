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
from guiones_comun import LEGAL  # noqa: E402

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


def render_guion(g, extra, corto=False):
    out = [f"[{g['id']}] {g['pieza'].upper()}",
           f"{g['objetivo']} · Para: {g['publico']} · {g.get('estructura', '')} · {g['formato']} · Aparece: {g['aparece']}",
           f"LA IDEA: {g['idea']}",
           f"GANCHO (escrito desde el cuadro 0): {g['gancho']}"]
    gb = extra.get("gancho_b") or g.get("gancho_b")
    if gb:
        out.append(f"GANCHO B (para probar): {gb}")
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
        candidatos = [x for x in (r + dt.timedelta(days=k) for k in range(1, (fecha - r).days)) if es_habil(x)]
        pref = [x for x in candidatos if x <= fecha - dt.timedelta(days=2)]
        pref = [x for x in pref if x not in P.MEDIO_DIA] or pref
        e = max(pref) if pref else (max(candidatos) if candidatos else r)  # nunca el mismo día de la grabación, salvo que no haya otro
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
        viernes.add(max(fs))
    return lunes, viernes


LUNES, VIERNES = semana_rutinas()


def rutina_lunes(f):
    t = ("Rutina del lunes (1 h): tablero de la semana anterior (alcance y % de Córdoba, salto a los 3 s, envíos por mensaje, comentarios con la palabra, "
         "chats con código, turnos, ventas) · escucha de 30 min (comentarios, mensajes y preguntas de Mercado Libre: anotar las preguntas textuales para 'Respuesta a @') · "
         "cambiar a 'Escribinos por WhatsApp (link en la bio)' el comentario fijado de las piezas de hace más de 7 días")
    if f >= dt.date(2027, 1, 4):
        t += " · anuncio A4: poner el reel de la semana con menos salto a los 3 s"
    t += (" · si salió una noticia que cambia la cuota (impuestos, una línea de crédito, una baja de precios): grabar 'Noticia de bolsillo' y publicarla dentro de las 48 h "
          "en lugar de la pieza de Educar de la semana (gancho '[la noticia en una línea]: ¿qué cambia para tu cuota?', la cuenta antes y después con un auto del salón, "
          "lo que todavía no se sabe, placa legal y el pedido de siempre)")
    return t + "."


RUTINA_VIERNES = ("Rutina del viernes: publicación en el Perfil de Google con la pieza de la semana · Mercado Libre: precio del día, video del modelo y preguntas pendientes · "
                  "dejar listas las tomas y los autos de la próxima grabación.")


def todos_los_dias(f, pubs, idx):
    out = []
    if pubs:
        for hora, formato, gid, extra in pubs:
            out.append(f"Historias: a las {hora}, compartir la pieza de hoy. Después: {extra.get('historia', 'una pregunta sobre el tema del video')}")
        out.append("Estado de WhatsApp: el mismo video + 'Si querés la cuenta con tu caso, escribime'.")
    elif f not in (P.VIP, P.DIA_D):
        i = P.DATOS_HISTORIAS[idx % len(P.DATOS_HISTORIAS)]
        _, mod, dato, frase, tipo, fte, url, fecha, ojo = DATO[i]
        out.append(f"Historia del día: foto o video corto del {mod} con el dato \"{frase}\" ({fte}) y una encuesta. Más una del día a día del equipo.")
    if f in P.FERIADOS or f.weekday() == 6:
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
        g = GUION[gid]
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
        graba.append(f"[{gid}] {g['pieza']}{cuando}\n   Aparece: {g['aparece']}\n   Tomas: {g['tomas']}" + (f"\n   Nota: {nota}" if nota else ""))
        quien.add("Contenido")
        for rol in ("Vendedor 1", "Vendedor 2", "Jefe de taller", "Técnico", "Dueño"):
            if rol.lower() in g["aparece"].lower():
                quien.add(rol)
    if graba and f.weekday() < 5:
        graba.insert(0, "Bloque de grabación 9 a 12 h (el de primer contacto no graba: sigue con WhatsApp). Vertical 4K, foco y exposición bloqueados, corbatero, 3 tomas de cada gancho.")
    edita = []
    for gid, pub in EDITA.get(f, []):
        g = GUION[gid]
        edita.append(f"[{gid}] {g['pieza']} · sale el {DIAS[pub.weekday()].lower()} {pub.strftime('%d/%m')}: editar (subtítulos palabra por palabra, un cambio grande cada 2–3 s y algo que aparece cada 0,3 s, voz ×1,15, música 8 dB debajo de la voz, placa final con el logo dentro de la zona segura) y mandar al dueño la hoja de cuadros; se publica con su OK.")
        quien.add("Contenido")
    tareas = []
    if f in LUNES:
        tareas.append(rutina_lunes(f))
    for resp, texto in P.T.get(f, []):
        tareas.append(f"{texto} ({resp})")
        quien.update(x.strip() for x in resp.replace("+", ",").split(","))
    if f in VIERNES:
        tareas.append(RUTINA_VIERNES)
    fila.update(publica="\n\n".join(publica), guion="\n\n══════════\n\n".join(guion), pegar="\n\n".join(pegar),
                antes="\n\n".join(antes), graba="\n\n".join(graba), edita="\n".join(edita), tareas="\n\n".join(tareas),
                diario=todos_los_dias(f, pubs, idx_hist), quien=", ".join(sorted(quien)) or "Primer contacto (WhatsApp)",
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
            g = GUION[gid]
            w(f"### Se publica: {hora} · [{gid}] {g['pieza']}\n")
            w(f"**{g['objetivo']}** · {formato} · {g['formato']} · Aparece: {g['aparece']}\n")
            w(f"**La idea:** {g['idea']}\n")
            gb = extra.get("gancho_b") or g.get("gancho_b")
            w(f"**Gancho (cuadro 0):** {g['gancho']}" + (f"  \n**Gancho B (para probar):** {gb}" if gb else "") + "\n")
            if extra.get("ajuste"):
                w(f"**Ajuste de hoy:** {extra['ajuste']}\n")
            for gg in [g] + ([GUION[extra["plan_b"]]] if extra.get("plan_b") else []):
                if gg is not g:
                    w(f"**Plan B: [{gg['id']}] {gg['pieza']}** · {gg['formato']} · Aparece: {gg['aparece']}  \n**Gancho:** {gg['gancho']}\n")
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
