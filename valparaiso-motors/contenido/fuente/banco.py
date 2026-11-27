"""Genera el documento 'Banco de ideas y guiones' (Markdown) desde los datos.

Uso: python3 banco.py  → escribe ../Banco de ideas y guiones.md
Después: pandoc a .docx con ref_horizontal.docx y LibreOffice a .pdf.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import datos as D  # noqa: E402
import datos_guiones as DG  # noqa: E402
from guiones_comun import LEGAL  # noqa: E402

SALIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Banco de ideas y guiones.md")
GRUPOS = [("E", "Entretener a las masas", "Juegos, desafíos, pruebas y detrás de escena. Buscan alcance y que lo manden por mensaje. La palabra clave va en la descripción y en el comentario fijado, no en la voz."),
          ("D", "Educar a los interesados", "Comparar, sacar dudas y responder objeciones. Buscan que lo guarden, que pregunten y que escriban con el código."),
          ("V", "Vender a los comprometidos", "El auto real, su precio y su cuota con el legal, la prueba de manejo y las entregas. Buscan chats de WhatsApp y turnos."),
          ("C", "Carruseles", "Una idea por placa, de la menos a la más importante. Se guardan y se comparten."),
          ("O", "Todos los días y piezas especiales", "Historias, Estados, vivos, YouTube, Google y mensajes de WhatsApp.")]


CAMBIOS = [
    "**Datos corregidos.** Se sacaron los '995 km' del Eado (no figuran en ninguna fuente oficial argentina), el '20 → 80 % en 36 min' del ORA 03 (es del 10 al 80 % en unos 40 min) y los '120 litros por mes' con 22 días (son 88 L: 120 L es con 30 días). La garantía del ORA 03 es de 7 años. La H7 tiene dos versiones: 228 CV (4x4 a nafta) y 243 CV (híbrida), y el bloqueo y los 8 modos son solo de la 4x4. La toma de 220 V de la H7 no se muestra con herramientas hasta saber su potencia.",
    "**Números de Córdoba con fórmula.** Nafta a $2.162, luz a $370 por kWh (EPEC), peajes de la RAC, distancias reales a Jesús María, Cosquín, Mendiolaza o Carlos Paz y la medida mínima de una cochera según el Código de Edificación. Están en la hoja 'Cuentas de Córdoba' y se recalculan cambiando dos celdas.",
    "**Lo honesto en cada pieza.** Cada guion de producto dice una limitación real: sin rueda de auxilio (Eado, CS55, Deepal), consumo de la 4x4, garantía de 3 años de la L200, 'si no tenés cochera, no es para vos'. Es lo que más credibilidad da en los videos argentinos que mejor funcionan ('lo recomendaría, pero ojo').",
    "**Formatos copiados de lo que ya funcionó en Argentina:** vendedor a cámara con el precio en la primera frase y 'te lo cuento' (V20), dúo frente a la unidad (D02), sketch de la objeción 'auto chino' (D03), 'Respuesta a @' con los comentarios reales (D19), reseña 'lo recomendaría, pero ojo' (D28), ranking de costo por km con veredicto (E27), noticia de bolsillo en 48 h (D30), colaboración con un creador cordobés (E28) y la serie del único video de la cuenta que pasó las 100.000 (D29).",
    "**Preguntas reales de compradores como guion:** tasa 0 y CFT (D21, con un ejemplo real de 43,72 %), ¿y si nunca lo enchufás? (D22), ¿tiene rueda de auxilio? (D23), el número del folleto contra el medido (D24), qué pedir antes de dejar una seña (D26), ¿y si la marca se va? (D27) y el precio del aviso contra el final (D13).",
    "**Modelos que faltaban:** CS55 Plus (el más medido por la prensa), JMEV Easy 3, Deepal S05, Jolion HEV, Tank 300 y Outlander, cada uno con su 'Llegó al salón' (V14 a V19).",
    "**Una primicia propia:** no encontramos ninguna medición publicada de la autonomía eléctrica real del Eado en Argentina. E25 la mide en Córdoba: es noticia, se guarda y nos pone como fuente.",
    "**Fuentes en cada guion.** La columna 'Fuentes' lleva los IDs de las hojas 'Datos de los autos' (EADO-1, ORA03-2…) y 'Cuentas de Córdoba' (C1, C5…). Lo que dice 'verificar' se confirma antes de grabar.",
]


def limpio(t):
    t = (t or "").replace("|", "/").replace("\n", " ")
    return "Placa legal completa (ver arriba)" if t == LEGAL else t


def main():
    en_cal = {}
    for p in D.PIEZAS:
        en_cal.setdefault(p["guion"], []).append(p["id"])
    out = []
    w = out.append
    w('---\ntitle: "Banco de ideas y guiones"\nsubtitle: "Valparaiso Motors · ' + str(len(D.GUIONES)) + ' guiones listos para grabar, con datos verificados de Córdoba y de cada modelo"\nlang: es-AR\n---\n')
    w("# Qué cambió en esta versión\n")
    w("Los guiones se reescribieron con una investigación propia del 26/11/2026: fichas oficiales y pruebas de la prensa argentina de cada modelo, precios de la nafta y la luz en Córdoba, los videos de autos que más se vieron en Argentina en 2025–2026 y las preguntas reales de compradores en comentarios y foros. Lo que cambió:\n")
    for r in CAMBIOS:
        w(f"- {r}")
    w("")
    w("**Cómo se usa.** Cada guion trae la idea en una frase, el gancho (y un gancho B para probar), las escenas una por una (qué se dice, qué se ve, el texto en pantalla y el sonido), las tomas que hay que grabar, lo que hay que confirmar antes, y la descripción, los hashtags, el comentario fijado y el código listos para pegar. Las fechas están en la planilla del calendario; las ideas que no tienen fecha dicen *Sin fecha (banco)* y se usan cuando quieras o cuando una pieza no puede salir.\n")
    w("**Las reglas de todos los guiones:**\n")
    for r in ["Una sola idea por pieza, que se pueda decir en una frase.",
              "El gancho habla de la vida del que mira y ya está escrito en el primer cuadro.",
              "Una promesa en los primeros segundos ('al final te digo…') que el final cumple.",
              "Frases de hasta 12 palabras y palabras de todos los días. Las siglas, solo en letra chica.",
              "Cada frase tiene su imagen, al mismo tiempo. Cortes cada 1–2 s, siempre sobre lo que se está diciendo.",
              "Estructuras distintas: juegos, pruebas, verdadero o falso, cuenta regresiva, punto de vista, antes y después. No siempre '3 cosas'.",
              "Un solo pedido comercial: 'Pedinos precio y financiación de cualquiera de nuestros autos'. La palabra clave siempre como pedido de precio.",
              "Datos con su fuente o 'estimado' con la cuenta en la descripción. Precio en pesos y la placa legal cuando hay números.",
              "Clientes, invitados o chicos: solo con autorización firmada. Vendedores: 'Soy [nombre], vendedor de Valparaiso Motors'.",
              "Una limitación real dicha en voz alta en cada pieza de producto ('lo honesto'): da credibilidad a todo lo demás.",
              "Plata o la duda del comprador en la primera frase, con sus palabras ('quedarte tirado', 'tomacorriente común', 'tasa 0, ¿y el resto?')."]:
        w(f"- {r}")
    w("\n**Placa legal** (va en toda pieza con precio o cuota, mínimo 5 segundos):\n")
    w("> " + LEGAL + "\n")
    w("Lo que está entre corchetes [..] se completa ese día con el dato real (precio, número medido, nombre).\n")

    w("# Las ideas de un vistazo\n")
    w("| ID | Pieza | Objetivo | Para quién | Estructura | Dificultad | En el calendario |")
    w("|---|---|---|---|---|---|---|")
    for g in D.GUIONES:
        usos = ", ".join(en_cal.get(g["id"], [])) or "Sin fecha (banco)"
        w(f'| {g["id"]} | {limpio(g["pieza"])} | {g["objetivo"]} | {limpio(g["publico"])} | {limpio(g.get("estructura", ""))} | {g.get("dificultad", "")} | {usos} |')
    w("")

    for letra, titulo, intro in GRUPOS:
        w(f"# {titulo}\n")
        w(intro + "\n")
        for g in [x for x in D.GUIONES if x["id"].startswith(letra)]:
            usos = ", ".join(en_cal.get(g["id"], [])) or "Sin fecha (banco)"
            w(f'## {g["id"]} · {g["pieza"]}\n')
            w(f'**{g["objetivo"]}** · Para: {g["publico"]} · Estructura: {g.get("estructura", "")} · {g["formato"]} · Aparece: {g["aparece"]} · Dificultad: {g.get("dificultad", "")} · Calendario: {usos}\n')
            w(f'**La idea:** {g["idea"]}\n')
            if g.get("por_que"):
                w(f'**Por qué funciona:** {g["por_que"]}\n')
            w(f'**Gancho:** {g["gancho"]}' + (f'  \n**Gancho B:** {g["gancho_b"]}' if g.get("gancho_b") else "") + "\n")
            w("| Momento | Qué se dice | Qué se ve | Texto en pantalla | Sonido |")
            w("|---|---|---|---|---|")
            for t, dice, ve, texto, sonido in g["escenas"]:
                w(f"| {limpio(t)} | {limpio(dice)} | {limpio(ve)} | {limpio(texto)} | {limpio(sonido)} |")
            w("")
            if g.get("honesto"):
                w(f'**Lo honesto (se dice en voz alta):** {g["honesto"]}\n')
            if g.get("fuentes"):
                w(f'**Fuentes de los datos:** {g["fuentes"]} (ver el anexo y las hojas Datos de los autos y Cuentas de Córdoba)\n')
            if g.get("tomas"):
                w(f'**Tomas:** {g["tomas"]}\n')
            if g.get("ojo"):
                w(f'**Ojo, confirmar antes:** {g["ojo"]}\n')
            if g.get("descripcion"):
                w("**Descripción para pegar:**\n")
                w("> " + g["descripcion"].replace("\n", "  \n> ") + "\n")
            extras = []
            if g.get("hashtags"):
                extras.append(f'**Hashtags:** {g["hashtags"]}')
            if g.get("fijado"):
                extras.append(f'**Comentario fijado:** {g["fijado"]}')
            if g.get("codigo"):
                extras.append(f'**Código:** {g["codigo"]}' + (f' · **Mensaje de WhatsApp:** "{g["mensaje"]}"' if g.get("mensaje") else ""))
            for e in extras:
                w(e + "\n")
    w("# Anexo 1 · Datos de los autos\n")
    w("Cada dato que usan los guiones, con la frase para decir y su fuente. **Marca** = lo declara el fabricante (decir 'según la marca'). **Medido** = prueba de la prensa. **Cuenta** = cuenta nuestra (decir 'estimado'). **Precio** = confirmar el día. **Sin fuente** = no decirlo. Los links están en la planilla (hoja Datos de los autos).\n")
    modelo = None
    for did, mod, dato, frase, tipo, fte, url, fecha, ojo in DG.DATOS:
        if mod != modelo:
            if modelo is not None:
                w("")
            w(f"## {mod}\n")
            w("| ID | Para decir | Tipo | Fuente | Ojo |")
            w("|---|---|---|---|---|")
            modelo = mod
        w(f"| {did} | {limpio(frase)} | {tipo.split(' (')[0]} | {limpio(fte)} ({fecha}) | {limpio(ojo)} |")
    w("")
    w("# Anexo 2 · Cuentas de Córdoba\n")
    w("Con los precios del 16/11/2026 (nafta súper YPF $2.162) y la tarifa de EPEC de noviembre ($370,24 por kWh con IVA). En la planilla (hoja Cuentas de Córdoba) se cambian esos precios y todas se recalculan. Siempre van como 'estimado'.\n")
    w("| ID | Qué calcula | Fórmula | Cómo se dice | Guiones |")
    w("|---|---|---|---|---|")
    for cid, para, que, formula, fmt, unidad, dice in DG.CUENTAS:
        w(f"| {cid} | {limpio(que)} | {limpio(formula[1:])} | {limpio(dice)} | {limpio(para)} |")
    w("")
    w("# Anexo 3 · Errores a corregir antes de publicar\n")
    w("Lo que la investigación encontró mal en la web, en Mercado Libre y en los guiones anteriores. Si un video habla de un dato que la web o el aviso dicen distinto, el comentario lo va a señalar.\n")
    w("| Dónde | Qué dice hoy | Qué tendría que decir |")
    w("|---|---|---|")
    for donde, dice, debe, url in DG.ERRORES:
        w(f"| {limpio(donde)} | {limpio(dice)} | {limpio(debe)} |")
    w("")
    with open(SALIDA, "w") as f:
        f.write("\n".join(out) + "\n")
    print("ok", os.path.abspath(SALIDA))


if __name__ == "__main__":
    main()
