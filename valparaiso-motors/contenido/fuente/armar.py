"""Arma la planilla del calendario de contenido de Valparaiso Motors.

Uso:  python3 armar.py  (escribe ../Calendario de contenido Valparaiso Motors.xlsx)
Los datos (piezas, tareas, guiones, anuncios, evento y fuentes) están en datos.py.
Todas las fechas relativas salen de la celda "Día D" de la hoja Inicio.
"""
import datetime as dt
import os
import sys
import urllib.parse

from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.worksheet.datavalidation import DataValidation

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import datos as D  # noqa: E402

SALIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Calendario de contenido Valparaiso Motors.xlsx")

BORDO = "801628"
TINTA = "151415"
PAPEL = "F6F3EE"
GRIS = "8A8580"
AMARILLO = "FFF2CC"
ROSA = "F7E3E6"
F = "Arial"

fino = Side(style="thin", color="D9D4CC")
borde = Border(left=fino, right=fino, top=fino, bottom=fino)


def fuente(**kw):
    kw.setdefault("name", F)
    kw.setdefault("size", 10)
    kw.setdefault("color", TINTA)
    return Font(**kw)


def encabezado(ws, fila, titulos, anchos):
    for i, (t, a) in enumerate(zip(titulos, anchos), start=1):
        c = ws.cell(row=fila, column=i, value=t)
        c.font = fuente(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor=BORDO)
        c.alignment = Alignment(wrap_text=True, vertical="center")
        c.border = borde
        ws.column_dimensions[get_column_letter(i)].width = a
    ws.row_dimensions[fila].height = 32
    ws.freeze_panes = ws.cell(row=fila + 1, column=3)


def celda(ws, fila, col, valor, fmt=None, negrita=False, color=TINTA, relleno=None, envolver=True):
    c = ws.cell(row=fila, column=col, value=valor)
    c.font = fuente(bold=negrita, color=color)
    c.alignment = Alignment(wrap_text=envolver, vertical="top")
    c.border = borde
    if fmt:
        c.number_format = fmt
    if relleno:
        c.fill = PatternFill("solid", fgColor=relleno)
    return c


def link_wa(mensaje):
    return '=HYPERLINK("https://wa.me/"&WhatsApp&"?text=' + urllib.parse.quote(mensaje, safe="") + '","Abrir WhatsApp")'


def lista(ws, opciones, rango):
    dv = DataValidation(type="list", formula1='"' + ",".join(opciones) + '"', allow_blank=True)
    dv.error = "Elegí una opción de la lista"
    dv.errorTitle = "Valor no válido"
    ws.add_data_validation(dv)
    dv.add(rango)


def fecha_formula(tipo, valor):
    """tipo 'D' = días desde el Día D (valor entero); 'F' = fecha fija (valor date)."""
    if tipo == "D":
        return "=DiaD" + ("+" if valor >= 0 else "-") + str(abs(valor))
    return valor


def armar():
    wb = Workbook()

    # ---------------- Inicio ----------------
    ws = wb.active
    ws.title = "Inicio"
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 3
    ws.column_dimensions["B"].width = 44
    ws.column_dimensions["C"].width = 34
    ws.column_dimensions["D"].width = 70
    t = ws.cell(row=1, column=2, value="Calendario de contenido · Valparaiso Motors")
    t.font = fuente(size=18, bold=True, color=BORDO)
    s = ws.cell(row=2, column=2, value=D.SUBTITULO)
    s.font = fuente(size=10, color=GRIS)

    ws.cell(row=4, column=2, value="Datos a completar (celdas amarillas)").font = fuente(size=12, bold=True)
    fila = 5
    for clave, etiqueta, valor, fmt, nota in D.DATOS_INICIO:
        celda(ws, fila, 2, etiqueta, negrita=True)
        c = celda(ws, fila, 3, valor, fmt=fmt, relleno=AMARILLO, color="0000FF")
        celda(ws, fila, 4, nota, color=GRIS)
        if clave:
            wb.defined_names[clave] = DefinedName(clave, attr_text=f"Inicio!$C${fila}")
        fila += 1

    fila += 1
    ws.cell(row=fila, column=2, value="Cómo se usa").font = fuente(size=12, bold=True)
    fila += 1
    for i, paso in enumerate(D.COMO_SE_USA, start=1):
        ws.merge_cells(start_row=fila, start_column=2, end_row=fila, end_column=4)
        c = ws.cell(row=fila, column=2, value=f"{i}. {paso}")
        c.font = fuente()
        c.alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[fila].height = max(15, 14 * (len(paso) // 135 + 1))
        fila += 1

    fila += 1
    ws.cell(row=fila, column=2, value="Quién hace qué").font = fuente(size=12, bold=True)
    fila += 1
    for i, t in enumerate(["Rol", "Horas por semana (estimado)", "Qué hace"], start=2):
        c = celda(ws, fila, i, t, negrita=True, color="FFFFFF", relleno=BORDO)
    fila += 1
    for rol, horas, que in D.ROLES:
        celda(ws, fila, 2, rol, negrita=True)
        celda(ws, fila, 3, horas)
        celda(ws, fila, 4, que)
        ws.row_dimensions[fila].height = max(15, 14 * (len(que) // 80 + 1))
        fila += 1

    fila += 1
    ws.cell(row=fila, column=2, value="Mezcla del embudo en el feed (se recalcula sola)").font = fuente(size=12, bold=True)
    fila += 1
    for i, t in enumerate(["Objetivo", "Piezas de feed (reels y carruseles)", "Para qué sirve"], start=2):
        celda(ws, fila, i, t, negrita=True, color="FFFFFF", relleno=BORDO)
    fila += 1
    primera = fila
    for obj, que in D.MEZCLA:
        celda(ws, fila, 2, obj, negrita=True)
        f = "+".join(f'COUNTIFS(Calendario!$J$2:$J$600,"{obj}",Calendario!$M$2:$M$600,"{fmt}")' for fmt in ("Reel", "Carrusel"))
        celda(ws, fila, 3, "=" + f, fmt="0")
        celda(ws, fila, 4, que)
        ws.row_dimensions[fila].height = 30
        fila += 1
    celda(ws, fila, 2, "Proporción", negrita=True)
    celda(ws, fila, 3, f'=IFERROR(TEXT(C{primera}/SUM(C{primera}:C{fila - 1}),"0%")&" / "&TEXT(C{primera + 1}/SUM(C{primera}:C{fila - 1}),"0%")&" / "&TEXT(C{primera + 2}/SUM(C{primera}:C{fila - 1}),"0%"),"")')
    celda(ws, fila, 4, D.MEZCLA_NOTA, color=GRIS)
    ws.row_dimensions[fila].height = 64
    fila += 1

    fila += 1
    ws.cell(row=fila, column=2, value="Palabras que se usan en este plan").font = fuente(size=12, bold=True)
    fila += 1
    for palabra, que in D.GLOSARIO:
        celda(ws, fila, 2, palabra, negrita=True)
        ws.merge_cells(start_row=fila, start_column=3, end_row=fila, end_column=4)
        c = ws.cell(row=fila, column=3, value=que)
        c.font = fuente()
        c.alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[fila].height = max(15, 15 * (len(que) // 95 + 1))
        fila += 1

    fila += 1
    ws.cell(row=fila, column=2, value="Hojas de este archivo").font = fuente(size=12, bold=True)
    fila += 1
    for hoja, que in D.HOJAS:
        celda(ws, fila, 2, hoja, negrita=True)
        ws.merge_cells(start_row=fila, start_column=3, end_row=fila, end_column=4)
        c = ws.cell(row=fila, column=3, value=que)
        c.font = fuente()
        c.alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[fila].height = max(15, 15 * (len(que) // 95 + 1))
        fila += 1

    # ---------------- Calendario ----------------
    publico_de = {g["id"]: g["publico"] for g in D.GUIONES}
    wc = wb.create_sheet("Calendario")
    cols = ["ID", "Fecha", "Día", "Día relativo", "Semana del", "Se graba o se arma", "Lo aprueba el dueño", "Aviso", "Etapa",
            "Objetivo", "Para quién", "Canal", "Formato", "Serie o tema", "Pieza", "Gancho o texto de portada", "CTA y código",
            "Responsable", "Aparece / graba", "Materiales y datos a confirmar", "Guion", "Hora", "Horas de trabajo",
            "Métrica principal", "Estado", "Link publicado", "Resultado", "Evidencia", "Tipo de fecha", "Días desde D", "Fecha fija"]
    C = {n: get_column_letter(i) for i, n in enumerate(cols, start=1)}
    anchos = [9, 11, 6, 10, 10, 11, 11, 16, 15, 11, 18, 18, 13, 16, 34, 36, 26, 14, 16, 34, 8, 7, 8, 26, 13, 20, 14, 10, 8, 8, 11]
    encabezado(wc, 1, cols, anchos)
    piezas = sorted(D.PIEZAS, key=lambda p: (D.fecha_estimada(p["cuando"]), p.get("hora", "")))
    producir = ("Reel", "Carrusel", "Video largo")
    for i, p in enumerate(piezas, start=2):
        tipo, valor = p["cuando"]
        B, E, M = f"B{i}", f"E{i}", f"M{i}"
        celda(wc, i, 1, p["id"], negrita=True)
        celda(wc, i, 2, f'=IF(${C["Tipo de fecha"]}{i}="D",DiaD+${C["Días desde D"]}{i},${C["Fecha fija"]}{i})', fmt="dd/mm/yyyy")
        celda(wc, i, 3, f'=CHOOSE(WEEKDAY({B},2),"lun","mar","mié","jue","vie","sáb","dom")')
        celda(wc, i, 4, f'=IF({B}=DiaD,"Día D","D"&TEXT({B}-DiaD,"+0;-0"))')
        celda(wc, i, 5, f"={B}-WEEKDAY({B},2)+1", fmt="dd/mm")
        if p["formato"] in producir and p["id"] in D.MISMA_SEMANA:
            celda(wc, i, 6, "Misma semana", color=BORDO)
            celda(wc, i, 7, "El día antes", color=GRIS)
        elif p["formato"] in producir:
            pg = D.PRIMERA_GRABACION
            martes = f"{E}-6"
            feriado_m = f"OR(AND(MONTH({martes})=12,DAY({martes})=8),AND(MONTH({martes})=2,DAY({martes})=9))"
            celda(wc, i, 6, f"=MAX({martes}+IF({feriado_m},1,0),DATE({pg.year},{pg.month},{pg.day}))", fmt="dd/mm")
            viernes = f"{E}-3"
            fiesta_v = f"OR(AND(MONTH({viernes})=12,DAY({viernes})=25),AND(MONTH({viernes})=1,DAY({viernes})=1))"
            celda(wc, i, 7, f"=MAX({viernes}-IF({fiesta_v},2,0),DATE({pg.year},{pg.month},{pg.day}))", fmt="dd/mm")
        else:
            celda(wc, i, 6, "—", color=GRIS)
            celda(wc, i, 7, "—", color=GRIS)
        feriado = f"OR(AND(MONTH({B})=12,OR(DAY({B})=8,DAY({B})=24,DAY({B})=25,DAY({B})=31)),AND(MONTH({B})=1,DAY({B})=1),AND(MONTH({B})=2,OR(DAY({B})=8,DAY({B})=9)))"
        if p.get("domingo_ok"):
            celda(wc, i, 8, f'=IF({feriado},"Feriado o fiesta: revisar","")', color="C00000")
        else:
            celda(wc, i, 8, f'=IF({feriado},"Feriado o fiesta: revisar",IF(AND(WEEKDAY({B},2)=7,OR({M}="Reel",{M}="Carrusel")),"Domingo: pasarla al sábado o al lunes",""))', color="C00000")
        publico = p.get("publico") or publico_de.get(p.get("guion", ""), "")
        valores = [p["etapa"], p["objetivo"], publico, p["canal"], p["formato"], p.get("serie", ""), p["pieza"],
                   p.get("gancho", ""), p.get("cta", ""), p["resp"], p.get("aparece", ""), p.get("materiales", ""),
                   p.get("guion", ""), p.get("hora", "")]
        for k, v in enumerate(valores, start=9):
            celda(wc, i, k, v, negrita=(k == 15))
        celda(wc, i, 23, p.get("horas", None), fmt="0.0")
        celda(wc, i, 24, p.get("metrica", ""))
        celda(wc, i, 25, "Pendiente", relleno=AMARILLO, color="0000FF")
        celda(wc, i, 26, None, relleno=AMARILLO)
        celda(wc, i, 27, None, relleno=AMARILLO)
        celda(wc, i, 28, p.get("evidencia", ""))
        celda(wc, i, 29, tipo, color=GRIS)
        celda(wc, i, 30, valor if tipo == "D" else None, color=GRIS)
        celda(wc, i, 31, valor if tipo == "F" else None, fmt="dd/mm/yyyy", color=GRIS)
        largo = max(len(str(p.get("materiales", ""))), len(str(p.get("gancho", ""))), len(p["pieza"]))
        wc.row_dimensions[i].height = min(160, max(48, 13 * (largo // 32 + 1)))
    ultima = len(piezas) + 1
    est, obj, tip = C["Estado"], C["Objetivo"], C["Tipo de fecha"]
    lista(wc, D.ESTADOS, f"{est}2:{est}{ultima + 200}")
    lista(wc, ["Entretener", "Educar", "Vender", "Operación"], f"{obj}2:{obj}{ultima + 200}")
    lista(wc, ["D", "F"], f"{tip}2:{tip}{ultima + 200}")
    wc.auto_filter.ref = f"A1:{C['Fecha fija']}{ultima}"
    rango = f"A2:{C['Evidencia']}{ultima}"
    wc.conditional_formatting.add(rango, FormulaRule(formula=["$B2=DiaD"], fill=PatternFill("solid", fgColor=ROSA), font=Font(name=F, bold=True, color=BORDO)))
    wc.conditional_formatting.add(rango, FormulaRule(formula=[f'OR(${est}2="Publicado",${est}2="Medido",${est}2="No va")'], font=Font(name=F, color=GRIS)))
    wc.conditional_formatting.add(f"B2:B{ultima}", FormulaRule(formula=[f'AND($B2<TODAY(),${est}2="Pendiente")'], font=Font(name=F, bold=True, color="C00000")))
    wc.conditional_formatting.add(f"F2:F{ultima}", FormulaRule(formula=[f'AND(ISNUMBER($F2),$F2<TODAY(),${est}2="Pendiente")'], font=Font(name=F, bold=True, color="C00000"), fill=PatternFill("solid", fgColor=ROSA)))
    colores = {"Entretener": "E8EEF7", "Educar": "EEF5E9", "Vender": "F7E3E6"}
    for o, color in colores.items():
        wc.conditional_formatting.add(f"{obj}2:{obj}{ultima}", FormulaRule(formula=[f'${obj}2="{o}"'], fill=PatternFill("solid", fgColor=color)))
    for nombre, texto in [("Tipo de fecha", "D = la fecha se calcula desde el Día D (hoja Inicio). F = fecha fija del calendario."),
                          ("Días desde D", "Días antes (negativo) o después (positivo) del Día D. Cambiá este número para mover la pieza."),
                          ("Fecha fija", "Solo para filas con tipo F."),
                          ("Objetivo", "Entretener a las masas (alcance), educar a los interesados (comparar y resolver dudas), vender a los comprometidos (precio, cuota, turno)."),
                          ("Para quién", "A quién le habla la pieza. Ver la hoja Público."),
                          ("Se graba o se arma", "El martes de la semana anterior. Filtrá esta columna por fecha y tenés la lista de lo que se graba ese día. En rojo: ya pasó y la pieza sigue pendiente."),
                          ("Lo aprueba el dueño", "El viernes anterior, con la hoja de cuadros."),
                          ("Aviso", "Avisa si la fecha cae en un feriado, una fiesta o un domingo. Si pasa, mové la pieza un día.")]:
        wc.cell(row=1, column=cols.index(nombre) + 1).comment = Comment(texto, "Valparaiso Motors")

    # ---------------- Tareas ----------------
    wt = wb.create_sheet("Tareas")
    cols = ["ID", "Fecha límite", "Día", "Día relativo", "Área", "Tarea", "Paso a paso (resumen)", "Guía",
            "Responsable", "Prioridad", "Estado", "Notas", "Evidencia", "Tipo de fecha", "Días desde D", "Fecha fija"]
    anchos = [8, 11, 6, 10, 16, 36, 70, 10, 16, 10, 13, 26, 12, 8, 8, 11]
    encabezado(wt, 1, cols, anchos)
    tareas = sorted(D.TAREAS, key=lambda p: D.fecha_estimada(p["cuando"]))
    for i, p in enumerate(tareas, start=2):
        tipo, valor = p["cuando"]
        celda(wt, i, 1, p["id"], negrita=True)
        celda(wt, i, 2, f'=IF($N{i}="D",DiaD+$O{i},$P{i})', fmt="dd/mm/yyyy")
        celda(wt, i, 3, f'=CHOOSE(WEEKDAY(B{i},2),"lun","mar","mié","jue","vie","sáb","dom")')
        celda(wt, i, 4, f'=IF(B{i}=DiaD,"Día D","D"&TEXT(B{i}-DiaD,"+0;-0"))')
        celda(wt, i, 5, p["area"])
        celda(wt, i, 6, p["tarea"], negrita=True)
        celda(wt, i, 7, p["pasos"])
        celda(wt, i, 8, p.get("guia", ""))
        celda(wt, i, 9, p["resp"])
        celda(wt, i, 10, p.get("prioridad", "Media"))
        celda(wt, i, 11, "Pendiente", relleno=AMARILLO, color="0000FF")
        celda(wt, i, 12, None, relleno=AMARILLO)
        celda(wt, i, 13, p.get("evidencia", ""))
        celda(wt, i, 14, tipo, color=GRIS)
        celda(wt, i, 15, valor if tipo == "D" else None, color=GRIS)
        celda(wt, i, 16, valor if tipo == "F" else None, fmt="dd/mm/yyyy", color=GRIS)
        wt.row_dimensions[i].height = max(45, 13 * (len(p["pasos"]) // 85 + 1))
    ultima = len(tareas) + 1
    lista(wt, D.ESTADOS_TAREA, f"K2:K{ultima + 200}")
    lista(wt, ["Alta", "Media", "Baja"], f"J2:J{ultima + 200}")
    wt.auto_filter.ref = f"A1:P{ultima}"
    wt.conditional_formatting.add(f"A2:M{ultima}", FormulaRule(formula=['$K2="Hecho"'], font=Font(name=F, color=GRIS)))
    wt.conditional_formatting.add(f"B2:B{ultima}", FormulaRule(formula=['AND($B2<TODAY(),$K2<>"Hecho")'], font=Font(name=F, bold=True, color="C00000")))
    wt.conditional_formatting.add(f"J2:J{ultima}", FormulaRule(formula=['$J2="Alta"'], font=Font(name=F, bold=True, color=BORDO)))

    # ---------------- Guiones ----------------
    en_calendario = {}
    for p in D.PIEZAS:
        en_calendario.setdefault(p["guion"], []).append(p["id"])
    wg = wb.create_sheet("Guiones")
    cols = ["Guion", "Pieza", "Objetivo", "Para quién", "Estructura", "La idea en una frase", "Por qué funciona", "Dificultad",
            "En el Calendario", "Formato y duración", "Quién aparece", "Gancho (texto del cuadro 0)", "Gancho B (para probar)",
            "Tomas a grabar", "Ojo: confirmar antes", "Descripción lista para pegar", "Hashtags (5)", "Comentario fijado", "Código",
            "Mensaje de WhatsApp ya escrito", "Link de prueba"]
    anchos = [7, 30, 11, 20, 20, 40, 40, 9, 16, 18, 18, 30, 26, 40, 40, 54, 26, 36, 11, 30, 14]
    encabezado(wg, 1, cols, anchos)
    for i, g in enumerate(D.GUIONES, start=2):
        usos = en_calendario.get(g["id"], [])
        vals = [g["id"], g["pieza"], g["objetivo"], g["publico"], g.get("estructura", ""), g["idea"], g.get("por_que", ""),
                g.get("dificultad", ""), ", ".join(usos) if usos else "Sin fecha (banco)", g["formato"], g["aparece"], g["gancho"],
                g.get("gancho_b", ""), g["tomas"], g.get("ojo", ""), g["descripcion"], g.get("hashtags", ""), g.get("fijado", ""),
                g.get("codigo", "")]
        for k, v in enumerate(vals, start=1):
            celda(wg, i, k, v, negrita=(k in (1, 2, 19)))
        msg = g.get("mensaje", "")
        celda(wg, i, 20, msg)
        celda(wg, i, 21, link_wa(msg) if msg else "", color="0563C1")
        largo = max(len(g["descripcion"]) * 1.0, len(g["tomas"]) * 1.3, len(g.get("ojo", "")) * 1.3, len(g["idea"]) * 1.4, len(g.get("por_que", "")) * 1.4)
        wg.row_dimensions[i].height = min(300, max(60, 13 * (largo // 50 + 1)))
    colores = {"Entretener": "E8EEF7", "Educar": "EEF5E9", "Vender": "F7E3E6"}
    ult = len(D.GUIONES) + 1
    for obj, color in colores.items():
        wg.conditional_formatting.add(f"C2:C{ult}", FormulaRule(formula=[f'$C2="{obj}"'], fill=PatternFill("solid", fgColor=color)))
    wg.conditional_formatting.add(f"I2:I{ult}", FormulaRule(formula=['$I2="Sin fecha (banco)"'], font=Font(name=F, bold=True, color=BORDO)))
    wg.auto_filter.ref = f"A1:U{ult}"

    # ---------------- Escenas ----------------
    we2 = wb.create_sheet("Escenas")
    cols = ["Guion", "Pieza", "Momento", "Qué se dice", "Qué se ve", "Texto en pantalla", "Sonido"]
    anchos = [8, 24, 14, 46, 52, 38, 18]
    encabezado(we2, 1, cols, anchos)
    fila = 2
    for g in D.GUIONES:
        for n, (t, dice, ve, texto, sonido) in enumerate(g["escenas"]):
            vals = [g["id"], g["pieza"] if n == 0 else "", t, dice, ve, texto, sonido]
            for k, v in enumerate(vals, start=1):
                celda(we2, fila, k, v, negrita=(k in (1, 2)), relleno=("F6F3EE" if n == 0 else None))
            largo = max(len(dice), len(ve), len(texto) * 1.2)
            we2.row_dimensions[fila].height = min(200, max(30, 13 * (largo // 44 + 1)))
            fila += 1
    we2.auto_filter.ref = f"A1:G{fila - 1}"
    we2.freeze_panes = "D2"

    # ---------------- Público ----------------
    wp = wb.create_sheet("Público")
    cols = ["Público", "Quién es", "Qué quiere", "Qué lo frena", "Modelos", "Piezas que le hablan", "Dónde está", "Evidencia"]
    anchos = [20, 40, 34, 34, 24, 34, 24, 34]
    encabezado(wp, 1, cols, anchos)
    for i, fila_p in enumerate(D.PUBLICO, start=2):
        for k, v in enumerate(fila_p, start=1):
            celda(wp, i, k, v, negrita=(k == 1))
        wp.row_dimensions[i].height = max(60, 13 * (max(len(x) for x in fila_p) // 36 + 1))
    n = len(D.PUBLICO) + 3
    for texto in D.PUBLICO_NOTAS:
        c = wp.cell(row=n, column=1, value=texto)
        c.font = fuente(color=GRIS)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        wp.merge_cells(start_row=n, start_column=1, end_row=n, end_column=8)
        wp.row_dimensions[n].height = 30
        n += 1

    # ---------------- Cómo escribir ----------------
    wx = wb.create_sheet("Cómo escribir")
    wx.sheet_view.showGridLines = False
    wx.column_dimensions["A"].width = 3
    wx.column_dimensions["B"].width = 34
    wx.column_dimensions["C"].width = 48
    wx.column_dimensions["D"].width = 48
    r = 1
    wx.cell(row=r, column=2, value="Cómo escribir para que lo entienda alguien de 15 años").font = fuente(size=16, bold=True, color=BORDO)
    r += 1
    wx.cell(row=r, column=2, value=D.ESCRIBIR_INTRO).font = fuente(color=GRIS)
    wx.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
    wx.cell(row=r, column=2).alignment = Alignment(wrap_text=True, vertical="top")
    wx.row_dimensions[r].height = 44
    for titulo, filas, encab in ((D.PRUEBA_15_TITULO, D.PRUEBA_15, None),
                                 (D.DICCIONARIO_TITULO, D.DICCIONARIO, ("En vez de…", "Decí…", "Y en letra chica, si hace falta…")),
                                 (D.RITMO_TITULO, D.RITMO, ("Regla", "Cómo se hace", "Por qué"))):
        r += 2
        wx.cell(row=r, column=2, value=titulo).font = fuente(size=12, bold=True)
        if encab:
            r += 1
            for k, t in enumerate(encab, start=2):
                celda(wx, r, k, t, negrita=True, color="FFFFFF", relleno=BORDO)
        for item in filas:
            r += 1
            if isinstance(item, str):
                wx.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
                c = wx.cell(row=r, column=2, value=item)
                c.font = fuente()
                c.alignment = Alignment(wrap_text=True, vertical="top")
                wx.row_dimensions[r].height = max(15, 14 * (len(item) // 120 + 1))
            else:
                for k, v in enumerate(item, start=2):
                    celda(wx, r, k, v, negrita=(k == 2))
                wx.row_dimensions[r].height = max(15, 13 * (max(len(x) for x in item) // 46 + 1))

    # ---------------- Códigos ----------------
    import re as _re
    from collections import Counter as _Counter
    objetivo_de = {}
    for p in D.PIEZAS:
        m = _re.search(r"comentá ([A-Z0-9\-]+)", p.get("cta", ""))
        if m:
            objetivo_de.setdefault(m.group(1), _Counter())[p["objetivo"]] += 1
    wk = wb.create_sheet("Códigos")
    cols = ["Código", "Objetivo", "Para qué pieza o anuncio", "Dónde se usa", "Mensaje ya escrito", "Link (usa el WhatsApp de Inicio)", "Consultas", "Leads calificados", "Turnos", "Ventas"]
    anchos = [16, 12, 36, 30, 50, 18, 11, 11, 9, 9]
    encabezado(wk, 1, cols, anchos)
    for i, (cod, para, donde, msg) in enumerate(D.CODIGOS, start=2):
        o = objetivo_de[cod].most_common(1)[0][0] if cod in objetivo_de else "Vender"
        celda(wk, i, 1, cod, negrita=True)
        celda(wk, i, 2, o)
        celda(wk, i, 3, para)
        celda(wk, i, 4, donde)
        celda(wk, i, 5, msg)
        celda(wk, i, 6, link_wa(msg), color="0563C1")
        for col in range(7, 11):
            celda(wk, i, col, None, fmt="0", relleno=AMARILLO)
        wk.row_dimensions[i].height = 40
    n = len(D.CODIGOS) + 1
    lista(wk, ["Entretener", "Educar", "Vender"], f"B2:B{n + 50}")
    r = n + 2
    wk.cell(row=r, column=1, value="Resultados por objetivo (se calculan solos)").font = fuente(size=12, bold=True)
    r += 1
    for k, t in enumerate(["Objetivo", "", "", "", "", "", "Consultas", "Leads calificados", "Turnos", "Ventas"], start=1):
        if t:
            celda(wk, r, k, t, negrita=True, color="FFFFFF", relleno=BORDO)
    for o in ("Entretener", "Educar", "Vender"):
        r += 1
        celda(wk, r, 1, o, negrita=True)
        for col in range(7, 11):
            L = get_column_letter(col)
            celda(wk, r, col, f'=SUMIF($B$2:$B${n},$A{r},{L}$2:{L}${n})', fmt="0", negrita=True)
    r += 1
    c = wk.cell(row=r, column=1, value="Es la cuenta que decide la mezcla el 11/1: el objetivo que trae más chats calificados con código gana 5–10 puntos.")
    c.font = fuente(color=GRIS)

    # ---------------- Anuncios ----------------
    wa = wb.create_sheet("Anuncios")
    cols = ["Campaña", "Objetivo", "Público y ubicación", "Creativos", "Destino", "USD por día", "Desde", "Hasta", "Días", "Total USD",
            "Métrica para decidir", "Regla de corte o de subida", "Tipo desde", "Días desde D (desde)", "Fecha fija (desde)", "Tipo hasta", "Días desde D (hasta)", "Fecha fija (hasta)"]
    anchos = [28, 18, 40, 26, 22, 10, 11, 11, 6, 10, 28, 40, 7, 8, 11, 7, 8, 11]
    encabezado(wa, 1, cols, anchos)
    for i, a in enumerate(D.ANUNCIOS, start=2):
        celda(wa, i, 1, a["nombre"], negrita=True)
        celda(wa, i, 2, a["objetivo"])
        celda(wa, i, 3, a["publico"])
        celda(wa, i, 4, a["creativos"])
        celda(wa, i, 5, a["destino"])
        celda(wa, i, 6, a["usd_dia"], fmt="0", relleno=AMARILLO, color="0000FF")
        celda(wa, i, 7, f'=IF($M{i}="D",DiaD+$N{i},$O{i})', fmt="dd/mm/yyyy")
        celda(wa, i, 8, f'=IF($P{i}="D",DiaD+$Q{i},$R{i})', fmt="dd/mm/yyyy")
        celda(wa, i, 9, f"=H{i}-G{i}+1", fmt="0")
        celda(wa, i, 10, f"=F{i}*I{i}", fmt="#,##0")
        celda(wa, i, 11, a["metrica"])
        celda(wa, i, 12, a["regla"])
        for base, clave in ((13, "desde"), (16, "hasta")):
            tipo, valor = a[clave]
            celda(wa, i, base, tipo, color=GRIS)
            celda(wa, i, base + 1, valor if tipo == "D" else None, color=GRIS)
            celda(wa, i, base + 2, valor if tipo == "F" else None, fmt="dd/mm/yyyy", color=GRIS)
        wa.row_dimensions[i].height = 75
    n = len(D.ANUNCIOS) + 1
    celda(wa, n + 1, 9, "Total", negrita=True)
    celda(wa, n + 1, 10, f"=SUM(J2:J{n})", fmt="#,##0", negrita=True)
    celda(wa, n + 2, 1, "Los montos son una asignación propuesta para medir, no un precio de mercado: no hay costo por lead publicado para autos en la Argentina. Cambialos en la columna F.", color=GRIS)
    wa.merge_cells(start_row=n + 2, start_column=1, end_row=n + 2, end_column=12)
    wa.row_dimensions[n + 2].height = 28

    # ---------------- Evento ----------------
    we = wb.create_sheet("Evento")
    cols = ["Momento", "Hora", "Qué pasa", "Responsable", "Qué se graba o publica", "Material y logística"]
    anchos = [22, 9, 56, 18, 44, 44]
    encabezado(we, 1, cols, anchos)
    for i, e in enumerate(D.EVENTO, start=2):
        es_titulo = e[1] == ""
        for col, v in enumerate(e, start=1):
            c = celda(we, i, col, v, negrita=es_titulo or col == 1, relleno=ROSA if es_titulo else None, color=BORDO if es_titulo else TINTA)
        we.row_dimensions[i].height = 18 if es_titulo else max(30, 13 * (max(len(x) for x in e) // 50 + 1))

    # presupuesto del evento
    r = len(D.EVENTO) + 3
    we.cell(row=r, column=1, value="Presupuesto del evento (completar con 2 o 3 cotizaciones)").font = fuente(size=12, bold=True)
    r += 1
    for k, t in enumerate(["Partida", "", "Cotización 1 ($)", "Cotización 2 ($)", "Cotización 3 ($)", "Elegida ($)"], start=1):
        if t:
            celda(we, r, k, t, negrita=True, color="FFFFFF", relleno=BORDO)
    primera = r + 1
    for partida in D.PRESUPUESTO_EVENTO:
        r += 1
        celda(we, r, 1, partida, negrita=True)
        we.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
        for col in (3, 4, 5, 6):
            celda(we, r, col, None, fmt="#,##0", relleno=AMARILLO)
    r += 1
    celda(we, r, 1, "Total", negrita=True)
    celda(we, r, 6, f"=SUM(F{primera}:F{r - 1})", fmt="#,##0", negrita=True)
    celda(we, r + 1, 1, "Pedirle a la importadora que ponga una parte (unidades, imagen, un directivo, una condición comercial). No hay presupuestos publicados de inauguraciones para comparar.", color=GRIS)
    we.merge_cells(start_row=r + 1, start_column=1, end_row=r + 1, end_column=6)

    # ---------------- Carga ----------------
    wl = wb.create_sheet("Carga")
    cols = ["Semana (lunes)", "Horas de piezas que se producen esa semana", "Horas fijas (plan, escucha, grabación, tablero)", "Horas de tareas (estimado)", "Total", "Capacidad", "Estado", "Horas del dueño con Claude"]
    anchos = [14, 16, 22, 18, 10, 11, 34, 16]
    encabezado(wl, 1, cols, anchos)
    for k in range(13):
        i = k + 2
        lunes = D.TABLERO_INICIO + dt.timedelta(days=7 * k)
        celda(wl, i, 1, lunes, fmt="dd/mm/yyyy", negrita=True)
        celda(wl, i, 2, f'=SUMIFS(Calendario!$W$2:$W$600,Calendario!$F$2:$F$600,">="&A{i},Calendario!$F$2:$F$600,"<"&(A{i}+7),Calendario!$R$2:$R$600,"Contenido")'
                         f'+SUMIFS(Calendario!$W$2:$W$600,Calendario!$E$2:$E$600,A{i},Calendario!$F$2:$F$600,"—",Calendario!$R$2:$R$600,"Contenido")'
                         f'+SUMIFS(Calendario!$W$2:$W$600,Calendario!$E$2:$E$600,A{i},Calendario!$F$2:$F$600,"Misma semana",Calendario!$R$2:$R$600,"Contenido")', fmt="0.0")
        celda(wl, i, 3, D.CARGA_FIJA_SEMANA.get(lunes, D.CARGA_FIJA), fmt="0.0", relleno=AMARILLO, color="0000FF")
        celda(wl, i, 4, D.CARGA_TAREAS.get(lunes, 1), fmt="0.0", relleno=AMARILLO, color="0000FF")
        celda(wl, i, 5, f"=B{i}+C{i}+D{i}", fmt="0.0", negrita=True)
        celda(wl, i, 6, "=Capacidad", fmt="0")
        celda(wl, i, 7, f'=IF(E{i}>F{i},"Se pasa: grabar antes, pedir ayuda o correr una pieza","OK")')
        celda(wl, i, 8, f'=SUMIFS(Calendario!$W$2:$W$600,Calendario!$E$2:$E$600,A{i},Calendario!$R$2:$R$600,"Dueño + Claude")', fmt="0.0")
    wl.conditional_formatting.add("G2:G14", FormulaRule(formula=['$E2>$F2'], font=Font(name=F, bold=True, color="C00000"), fill=PatternFill("solid", fgColor=ROSA)))
    nota = wl.cell(row=16, column=1, value="Las horas de piezas salen solas del Calendario: los reels, carruseles y videos largos cuentan en la semana en que se graban y editan (la anterior a la publicación), y las historias, Estados, vivos y piezas del momento cuentan en su semana. Las horas de tareas son una estimación: cambialas. El evento en sí (noche VIP y día abierto) no está sumado: por eso hay foto y video externos (T51) y se graba antes (T50).")
    nota.font = fuente(color=GRIS)
    nota.alignment = Alignment(wrap_text=True, vertical="top")
    wl.merge_cells("A16:H16")
    wl.row_dimensions[16].height = 42

    # ---------------- Reserva ----------------
    wr = wb.create_sheet("Reserva")
    cols = ["Guion", "Pieza", "Objetivo", "Se usa cuando…", "Cuándo dejarla grabada"]
    encabezado(wr, 1, cols, [8, 40, 12, 44, 30])
    for i, fila_r in enumerate(D.RESERVA, start=2):
        for k, v in enumerate(fila_r, start=1):
            celda(wr, i, k, v, negrita=(k == 1))
        wr.row_dimensions[i].height = 30
    c = wr.cell(row=len(D.RESERVA) + 3, column=1, value="Tener siempre 2 o 3 piezas de reserva grabadas y editadas. Cuando una pieza del Calendario no sale (falta un precio, no llegó la unidad, no llueve), se publica una de reserva del mismo objetivo y se graba otra para reponerla.")
    c.font = fuente(color=GRIS)
    c.alignment = Alignment(wrap_text=True)
    wr.merge_cells(start_row=len(D.RESERVA) + 3, start_column=1, end_row=len(D.RESERVA) + 3, end_column=5)
    wr.row_dimensions[len(D.RESERVA) + 3].height = 30

    # ---------------- Pruebas ----------------
    wpr = wb.create_sheet("Pruebas")
    cols = ["Prueba", "Cuándo", "Qué se compara", "Cómo", "Qué creemos que pasa", "Cómo se mide", "Resultado A", "Resultado B", "Qué se decide"]
    encabezado(wpr, 1, cols, [7, 14, 30, 40, 44, 26, 13, 13, 30])
    for i, fila_p in enumerate(D.PRUEBAS, start=2):
        for k, v in enumerate(fila_p, start=1):
            celda(wpr, i, k, v, negrita=(k == 1))
        for col in (7, 8, 9):
            celda(wpr, i, col, None, relleno=AMARILLO)
        wpr.row_dimensions[i].height = 45
    c = wpr.cell(row=len(D.PRUEBAS) + 3, column=1, value="Una prueba por vez y con una sola diferencia entre A y B. Con reels de prueba se mide el gancho, no los leads: esos llegan de lo que se promociona en Córdoba.")
    c.font = fuente(color=GRIS)
    wpr.merge_cells(start_row=len(D.PRUEBAS) + 3, start_column=1, end_row=len(D.PRUEBAS) + 3, end_column=9)

    # ---------------- Tablero ----------------
    wtb = wb.create_sheet("Tablero")
    cols = D.TABLERO_COLUMNAS
    anchos = [11] + [12] * (len(cols) - 1)
    encabezado(wtb, 1, [c[0] for c in cols], anchos)
    for j, (nombre, nota, formula, agregado) in enumerate(cols, start=1):
        if nota:
            wtb.cell(row=1, column=j).comment = Comment(nota, "Valparaiso Motors")
    inicio = D.TABLERO_INICIO
    for k in range(14):
        i = k + 2
        for j, (nombre, nota, formula, agregado) in enumerate(cols, start=1):
            if j == 1:
                celda(wtb, i, 1, inicio + dt.timedelta(days=7 * k), fmt="dd/mm/yyyy", negrita=True)
            elif formula:
                f = formula.replace("{i}", str(i))
                fmt = "0%" if "%" in nombre else ("#,##0.0" if "USD" in nombre else "0")
                celda(wtb, i, j, f, fmt=fmt)
            else:
                fmt = "0%" if "%" in nombre else ("0.0" if agregado == "PROMEDIO" else "#,##0")
                celda(wtb, i, j, None, fmt=fmt, relleno=AMARILLO)
    total = 16
    celda(wtb, total, 1, "Total", negrita=True)
    for j, (nombre, nota, formula, agregado) in enumerate(cols, start=1):
        if j == 1:
            continue
        L = get_column_letter(j)
        if formula:
            f = formula.replace("{i}", str(total))
            fmt = "0%" if "%" in nombre else ("#,##0.0" if "USD" in nombre else "0")
            celda(wtb, total, j, f, fmt=fmt, negrita=True)
        elif agregado == "PROMEDIO":
            fmt = "0%" if "%" in nombre else "0.0"
            celda(wtb, total, j, f"=IFERROR(AVERAGE({L}2:{L}15),0)", fmt=fmt, negrita=True)
        else:
            celda(wtb, total, j, f"=SUM({L}2:{L}15)", fmt="#,##0", negrita=True)
    wtb.freeze_panes = "B2"
    fila = 18
    wtb.cell(row=fila, column=1, value="Cómo se completa").font = fuente(bold=True, size=11)
    for texto in D.TABLERO_NOTAS:
        fila += 1
        c = wtb.cell(row=fila, column=1, value=texto)
        c.font = fuente(color=GRIS)
        wtb.merge_cells(start_row=fila, start_column=1, end_row=fila, end_column=12)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        wtb.row_dimensions[fila].height = 28

    # ---------------- Fuentes ----------------
    wf = wb.create_sheet("Fuentes")
    cols = ["ID", "Qué respalda", "Dato", "Fuente", "Link", "Tipo de evidencia"]
    anchos = [8, 30, 60, 28, 50, 22]
    encabezado(wf, 1, cols, anchos)
    for i, (fid, respalda, dato, fuente_txt, url, tipo) in enumerate(D.FUENTES, start=2):
        celda(wf, i, 1, fid, negrita=True)
        celda(wf, i, 2, respalda)
        celda(wf, i, 3, dato)
        celda(wf, i, 4, fuente_txt)
        c = celda(wf, i, 5, url, color="0563C1")
        if url.startswith("http"):
            c.hyperlink = url
        celda(wf, i, 6, tipo)
        wf.row_dimensions[i].height = max(30, 13 * (len(dato) // 55 + 1))

    for hoja in wb.worksheets:
        hoja.sheet_properties.tabColor = BORDO if hoja.title in ("Inicio", "Calendario", "Tareas", "Escenas", "Carga") else "C9C2B8"
        hoja.page_setup.orientation = "landscape"
        hoja.sheet_properties.pageSetUpPr.fitToPage = True
        hoja.page_setup.fitToWidth = 1
        hoja.page_setup.fitToHeight = 0
    wb.save(SALIDA)
    print("ok", os.path.abspath(SALIDA), len(D.PIEZAS), "piezas", len(D.TAREAS), "tareas", len(D.GUIONES), "guiones")


if __name__ == "__main__":
    armar()
