"""Genera el documento 'Banco de ideas y guiones' (Markdown) desde los datos.

Uso: python3 banco.py  → escribe ../Banco de ideas y guiones.md
Después: pandoc a .docx con ref_horizontal.docx y LibreOffice a .pdf.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import datos as D  # noqa: E402
from guiones_comun import LEGAL  # noqa: E402

SALIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Banco de ideas y guiones.md")
GRUPOS = [("E", "Entretener a las masas", "Juegos, desafíos, pruebas y detrás de escena. Buscan alcance y que lo manden por mensaje. La palabra clave va en la descripción y en el comentario fijado, no en la voz."),
          ("D", "Educar a los interesados", "Comparar, sacar dudas y responder objeciones. Buscan que lo guarden, que pregunten y que escriban con el código."),
          ("V", "Vender a los comprometidos", "El auto real, su precio y su cuota con el legal, la prueba de manejo y las entregas. Buscan chats de WhatsApp y turnos."),
          ("C", "Carruseles", "Una idea por placa, de la menos a la más importante. Se guardan y se comparten."),
          ("O", "Todos los días y piezas especiales", "Historias, Estados, vivos, YouTube, Google y mensajes de WhatsApp.")]


def limpio(t):
    t = (t or "").replace("|", "/").replace("\n", " ")
    return "Placa legal completa (ver arriba)" if t == LEGAL else t


def main():
    en_cal = {}
    for p in D.PIEZAS:
        en_cal.setdefault(p["guion"], []).append(p["id"])
    out = []
    w = out.append
    w('---\ntitle: "Banco de ideas y guiones"\nsubtitle: "Valparaiso Motors · 73 guiones listos para grabar, escritos para que los entienda alguien de 15 años"\nlang: es-AR\n---\n')
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
              "Clientes, invitados o chicos: solo con autorización firmada. Vendedores: 'Soy [nombre], vendedor de Valparaiso Motors'."]:
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
    with open(SALIDA, "w") as f:
        f.write("\n".join(out) + "\n")
    print("ok", os.path.abspath(SALIDA))


if __name__ == "__main__":
    main()
