"""Datos del calendario de contenido de Valparaiso Motors (30/11/2026 al 28/02/2027).

Fechas: ("D", n) = n días desde el Día D (día abierto de la inauguración); ("F", fecha) = fecha fija.
El Día D de ejemplo es el sábado 19/12/2026: se cambia en la hoja Inicio de la planilla.
"""
import datetime as dt

from guiones import GUIONES  # noqa: F401  (lo usa armar.py)

DIA_D = dt.date(2026, 12, 19)
d = dt.date
SUBTITULO = "Del 30/11/2026 al 28/02/2027 · inauguración del nuevo local a fin de diciembre · armado el 25/11/2026"


def fecha_estimada(cuando):
    tipo, valor = cuando
    return DIA_D + dt.timedelta(days=valor) if tipo == "D" else valor


ESTADOS = ["Pendiente", "Grabado", "Editado", "Para aprobar", "Aprobado", "Publicado", "Medido", "No va"]
ESTADOS_TAREA = ["Pendiente", "En curso", "Hecho", "Bloqueado", "No va"]

DATOS_INICIO = [
    ("DiaD", "Día D: día abierto de la inauguración", DIA_D, "dd/mm/yyyy",
     "Fecha de ejemplo (sábado 19/12). Escribí la real: se recalculan todas las fechas relativas. Si la obra no llega, la alternativa es del 28 al 30/12."),
    ("NocheVIP", "Noche VIP con lista cerrada", "=DiaD-1", "dd/mm/yyyy", "Por defecto, el día anterior al Día D. Podés escribir otra fecha."),
    (None, "Arranque de la promo de apertura", d(2027, 1, 4), "dd/mm/yyyy",
     "Lunes 4/1: empieza el pico de enero (enero de 2026 casi triplicó a diciembre de 2025 en patentamientos). Fecha fija."),
    (None, "Dirección nueva", "COMPLETAR", None, "Va en el Perfil de Google, la web, Mercado Libre, la bio y todas las piezas de la mudanza."),
    (None, "Dirección actual", "Av. Ciudad de Valparaíso 4380, Córdoba", None, "Según directorios públicos. Confirmar. Si el local viejo sigue abierto (por ejemplo, como taller), no es una mudanza: son dos ubicaciones en Google."),
    ("WhatsApp", "WhatsApp de ventas (solo números, con 549)", "5493510000000", "@",
     "Formato: 549 + característica sin el 0 + número sin el 15. Los links de las hojas Guiones y Códigos usan esta celda."),
    (None, "Web de condiciones de las ofertas", "www.valparaisomotors.com.ar/condiciones", None,
     "Toda pieza con precio, cuota o promo remite acá (Res. 446/2025). Confirmar la URL con Asofix."),
    (None, "Responsable de contenido", "COMPLETAR", None, "Planifica, graba, edita, publica y mide."),
    (None, "Vendedor en cámara 1", "COMPLETAR", None, "Especialidad sugerida: eléctricos e híbridos."),
    (None, "Vendedor en cámara 2", "COMPLETAR", None, "Especialidad sugerida: financiación y usados."),
    (None, "Responsable de primer contacto", "COMPLETAR", None, "Responde WhatsApp y mensajes en menos de 5 minutos en horario."),
    (None, "Seguidores de Instagram hoy", None, "#,##0", "Para elegir la referencia de vistas por reel (Socialinsider: ~580 con 1.000–5.000 seguidores; ~1.000 con 5.000–10.000)."),
]

COMO_SE_USA = [
    "Escribí en la celda amarilla 'Día D' la fecha real del día abierto, y completá la dirección nueva, el WhatsApp y los nombres. Las fechas de Calendario, Tareas y Anuncios se recalculan solas.",
    "Cada lunes, en Calendario filtrá la columna 'Semana del' por la semana que empieza, y en Tareas mirá las fechas de los próximos 7 días. Eso es todo lo que hay que hacer en la semana.",
    "Cada pieza tiene un guion (columna 'Guion'). En la hoja Guiones está el resumen: para quién es, la idea en una frase, el gancho, las tomas, la descripción para pegar, los hashtags, el comentario fijado y el código. En la hoja Escenas está escena por escena: qué se dice, qué se ve, el texto en pantalla y el sonido.",
    "Todo se escribe para que lo entienda alguien de 15 años: frases cortas, palabras de todos los días y cada cosa que se dice, se ve. Antes de grabar y antes de publicar, pasá la prueba de la hoja 'Cómo escribir'.",
    "Columna 'Objetivo': Entretener a las masas (alcance), Educar a los interesados (comparar y sacar dudas) y Vender a los comprometidos (precio, cuota, turno). Cada semana tiene de las tres; las historias, los Estados y los vivos venden todos los días.",
    "Al publicar: Estado = 'Publicado' y pegá el link. El lunes siguiente cargá el resultado en la fila y los números de la semana en la hoja Tablero.",
    "Lo que tenga precio, cuota, CFT, promo o 'entrega inmediata' lo confirma Administración el mismo día. Sin confirmación no se publica (se cambia por otra pieza del mismo objetivo).",
    "Si cambiás el Día D, revisá la columna 'Aviso' (feriados) y que las piezas de la inauguración no choquen con otras del mismo día: la de la inauguración gana y la otra se corre un día.",
    "La guía paso a paso (documento aparte) explica cómo grabar, editar, publicar, atender los mensajes, mudar el Perfil de Google, armar los anuncios y hacer el evento.",
]

ROLES = [
    ("Responsable de contenido", "20 a 25", "Planifica el lunes, graba con los vendedores el martes, edita, publica, responde comentarios en horario, carga códigos y arma el tablero. Es quien lleva esta planilla."),
    ("Vendedores en cámara (2)", "2 a 3 cada uno", "Graban el martes a la mañana (2–3 h), hacen el vivo del sábado en enero y atienden los leads de sus videos ('te escribe [nombre], el del video'). Siempre se presentan como vendedores."),
    ("Responsable de primer contacto", "Todo el horario comercial", "Guardia de WhatsApp y mensajes: responde en menos de 5 minutos, califica A/B/C con las 5 preguntas y carga la planilla de leads. De D-2 a D+7, dos personas."),
    ("Dueño o gerente", "1 a 2", "Aprueba el viernes las piezas de la semana siguiente (una sola pregunta), confirma la fecha, la importadora, la prensa y las promos. Hace las revisiones de D+30 y D+60."),
    ("Administración", "0,5", "Confirma precio, cuota, TNA, CFTEA, vigencia y stock el día que se publica cada pieza con números."),
    ("Gestor y abogado", "Puntual", "Permiso eventual del municipio, seguro, revisión del legal de las piezas (Res. 446/2025 y 4/2025), autorización de imagen y, si hay, sorteo."),
    ("Dueño con Claude", "2 a 3 por pieza", "Videos animados educativos (pipeline de CLAUDE.md), placas animadas de 6–8 s para anuncios y revisión de guiones."),
    ("Asofix (web)", "Puntual", "Arreglos del sitio, página de condiciones, banner y datos de la mudanza."),
]

MEZCLA = [
    ("Entretener", "A las masas: juegos, desafíos, series y detrás de escena. Buscan alcance y envíos por DM. Cierran con 'Mandáselo a…' y el CTA chico."),
    ("Educar", "A los interesados: comparativas, objeciones, posventa, financiación explicada. Buscan guardados, preguntas y chats con código."),
    ("Vender", "A los comprometidos: unidad real con precio y cuota con CFT, entregas, promos y vivos. Buscan chats de WhatsApp, turnos y ventas."),
]
MEZCLA_NOTA = ("Meta de partida: ~40/35/25 en el feed (propuesta sin estudio que la respalde: la frase es una regla de creadores). "
               "Además, las historias, los Estados de WhatsApp y los vivos venden todos los días, y la pauta paga va sobre todo a Educar y Vender en Córdoba. "
               "A las 6–8 semanas se ajusta según qué objetivo trae más chats con código, no según las vistas.")

HOJAS = [
    ("Calendario", "Todas las piezas de contenido, día por día, con objetivo, canal, guion, responsable, materiales y métrica."),
    ("Tareas", "Todo lo que no es una publicación: permisos, Google, web, WhatsApp, prensa, evento, anuncios y revisiones."),
    ("Guiones", "41 guiones: para quién es cada uno, la idea en una frase, gancho, tomas, descripción, hashtags, comentario fijado y código. El link de prueba abre WhatsApp con el mensaje."),
    ("Escenas", "Cada guion escena por escena: qué se dice, qué se ve, el texto en pantalla y el sonido. Es lo que usa el que graba y edita."),
    ("Público", "A quién le hablamos: 7 públicos con lo que quieren, lo que los frena, los modelos y las piezas para cada uno."),
    ("Cómo escribir", "La prueba de los 15 años, el diccionario de palabras difíciles y las reglas de ritmo y visuales."),
    ("Códigos", "Un código por pieza o canal para saber qué trajo cada consulta. Se cargan los resultados acá."),
    ("Anuncios", "Campañas de Meta y Google con fechas, público, presupuesto diario y regla de corte."),
    ("Evento", "Minuto a minuto de la noche VIP y del día abierto: quién hace qué y qué se graba."),
    ("Tablero", "Números de cada semana. Las tasas y los costos se calculan solos."),
    ("Fuentes", "La evidencia detrás de cada decisión, con su link y qué tan firme es."),
]

# ---------------------------------------------------------------- piezas
REELS = "IG Reels + FB + TikTok + Shorts"
M_ENT = "Tasa de salto 3 s · envíos por alcance · % del alcance en Córdoba"
M_EDU = "Guardados · comentarios con la palabra · chats con código"
M_VEN = "Chats de WhatsApp con código → leads calificados → turnos"
M_CAR = "Guardados · compartidos · comentarios con la palabra"
CTA_CORTO = "Pedinos precio y financiación · comentá {k}"
CONF = "Administración confirma precio, cuota, TNA, CFTEA, vigencia y stock el día de publicar. "

PIEZAS = []


def pz(id_, cuando, etapa, objetivo, canal, formato, pieza, guion, resp, **kw):
    fila = dict(id=id_, cuando=cuando, etapa=etapa, objetivo=objetivo, canal=canal, formato=formato, pieza=pieza, guion=guion, resp=resp)
    fila.update(kw)
    PIEZAS.append(fila)


def reel(id_, cuando, etapa, objetivo, pieza, guion, aparece, gancho, codigo, materiales="", serie="", hora="19:30", horas=1.5, evidencia="F01, F02", resp="Contenido", publico=""):
    metrica = {"Entretener": M_ENT, "Educar": M_EDU, "Vender": M_VEN}[objetivo]
    cta = CTA_CORTO.format(k=codigo) if codigo else "Mandáselo a… (sin pedido comercial)"
    pz(id_, cuando, etapa, objetivo, REELS, "Reel", pieza, guion, resp, aparece=aparece, gancho=gancho, cta=cta,
       materiales=materiales, serie=serie, hora=hora, horas=horas, metrica=metrica, evidencia=evidencia, publico=publico)


def carrusel(id_, cuando, etapa, objetivo, pieza, gancho, codigo, materiales="", guion="G33", evidencia="F10"):
    pz(id_, cuando, etapa, objetivo, "IG + FB", "Carrusel", pieza, guion, "Contenido", gancho=gancho,
       cta=CTA_CORTO.format(k=codigo), materiales=materiales, hora="12:30", horas=1.5, metrica=M_CAR, evidencia=evidencia, serie="Carrusel de la semana")


E1, E2, E3, E4, E5, E6 = ("1. Preparación", "2. Cuenta regresiva", "3. Inauguración", "4. Después de abrir", "5. Enero: el pico", "6. Febrero")

# --- Semana del 30/11
reel("S01-1", ("F", d(2026, 12, 1)), E1, "Educar", "¿Comprás ahora o esperás a enero?", "G01", "Vendedor 1",
     "¿COMPRÁS AHORA O ESPERÁS A ENERO?", "ENERO",
     materiales="Dato ACARA de noviembre (sale ~30/11). Bonificaciones de diciembre de cada marca (Administración). Cómo figura el año modelo de las unidades en stock.",
     evidencia="F24, F01")
carrusel("S01-2", ("F", d(2026, 12, 2)), E1, "Educar", "Antes de cambiar el auto: las 5 preguntas que te hace un buen vendedor",
         "¿SABÉS QUÉ TE VA A PREGUNTAR EL VENDEDOR?", "PREGUNTAS", guion="G35",
         materiales="Las 5 preguntas de calificación: uso y km por día; cochera con enchufe; usado; financiación y anticipo; para cuándo.")
reel("S01-3", ("F", d(2026, 12, 3)), E1, "Vender", "Llegó al salón: el auto con más stock (Eado Plus)", "G02", "Vendedor 1",
     "SE ENCHUFA EN TU CASA Y NO TE DEJA A PIE EN LA RUTA", "EADO", serie="Llegó al salón", publico="Muchos km por día",
     materiales=CONF + "Datos: hasta 132 km eléctricos (NEDC), 995 km de autonomía total declarada, batería con 8 años o 150.000 km de garantía. Verificar cómo se presenta el concesionario para Changan.",
     evidencia="F07, F08, F17")

# --- Semana del 7/12 (7 no laborable, 8 feriado)
reel("S02-2", ("F", d(2026, 12, 10)), E1, "Vender", "Llegó al salón: híbrido que se carga solo (Haval H6 PRO HEV)", "G02", "Vendedor 2",
     "UN HÍBRIDO QUE NO SE ENCHUFA: SE CARGA SOLO", "H6", serie="Llegó al salón", publico="Familia; Muchos km por día",
     materiales=CONF + "Sin especificaciones que no estén en la ficha oficial: buscarlas y citarlas.", evidencia="F07, F08, F17")
carrusel("S02-1", ("F", d(2026, 12, 9)), E1, "Educar", "¿Auto chino? 5 respuestas sobre garantía, service y repuestos",
         "¿AUTO CHINO? 5 PREGUNTAS QUE TODOS HACEN", "TALLER", guion="G36",
         materiales="Garantías exactas de cada modelo con su condición ('lo que ocurra primero'). Tiempo real de un repuesto común (posventa). Fotos del taller.")

# --- Semana del 14/12 (aguinaldo 18/12, terminan las clases)
reel("S03-1", ("F", d(2026, 12, 15)), E1, "Educar", "¿Con el aguinaldo te alcanza para empezar?", "G11", "Vendedor 2",
     "¿CON EL AGUINALDO TE ALCANZA PARA EMPEZAR?", "AGUINALDO",
     materiales=CONF + "Si no hay ejemplo confirmado, se reemplaza por G23.", evidencia="F26, F17")

# --- Semana del 21/12 (Navidad)
reel("S04-1", ("F", d(2026, 12, 22)), E4, "Vender", "Entregas antes de Navidad", "G19", "Clientes con autorización + vendedor",
     "ESTA SEMANA SE FUERON [N] AUTOS A [BARRIOS]", "ENTREGA", serie="Entregas",
     materiales="Autorizaciones de imagen firmadas. Número real de entregas.", evidencia="F23, F15")
reel("S04-2", ("F", d(2026, 12, 24)), E4, "Entretener", "Felices fiestas desde el nuevo local", "G30", "Todo el equipo",
     "FELICES FIESTAS DESDE EL NUEVO VALPARAISO", "", hora="12:00", horas=1.0, materiales="Horario de fiestas.")

# --- Semana del 28/12 (Año Nuevo)
reel("S05-1", ("F", d(2026, 12, 28)), E4, "Entretener", "¿Entra todo para las vacaciones?", "G14", "Vendedor 2",
     "¿ENTRA TODO PARA LAS VACACIONES?", "VALIJAS", serie="¿Entra todo?",
     materiales="2 valijas grandes, conservadora, cochecito y bolso. SUV con más stock.", evidencia="F02, F34")
reel("S05-2", ("F", d(2026, 12, 29)), E4, "Educar", "Antes de salir a la ruta: lo que revisa el taller", "G34", "Técnico",
     "¿SALÍS DE VACACIONES? ESTO REVISARÍA UN TÉCNICO", "RUTA", materiales="Técnico disponible 1 h. Turnos de service de enero.", evidencia="F28")
carrusel("S05-3", ("F", d(2026, 12, 30)), E4, "Entretener", "El año en 8 fotos (y el local nuevo)", "ASÍ FUE NUESTRO 2026",
         "ABRIMOS", materiales="Fotos propias del año: entregas con autorización, equipo, obra, inauguración.")

# --- Semana del 4/1 (pico de enero)
reel("S06-1", ("F", d(2027, 1, 4)), E5, "Vender", "Promo de apertura", "G12", "Vendedor 1",
     "SI ESPERASTE A ENERO PARA CAMBIAR EL AUTO, ESTO ES PARA VOS", "APERTURA",
     materiales=CONF + "Condición por escrito de la importadora o de la casa, con inicio, fin y stock (tarea T36). Bases en la web.",
     evidencia="F24, F17, F33")
reel("S06-2", ("F", d(2027, 1, 5)), E5, "Educar", "¿Enchufe o nafta? Dos vendedores, dos autos", "G16", "Vendedor 1 y vendedor 2",
     "¿ENCHUFE O NAFTA? ELLOS NO SE PONEN DE ACUERDO", "ENCHUFE",
     materiales="ORA 03 y ORA 05 HEV en el salón. Datos: 310 km WLTP y carga 20–80 % en 36 min (oficial); 5,1 L/100 km mixto (declarado).", evidencia="F08, F09")
carrusel("S06-3", ("F", d(2027, 1, 6)), E5, "Vender", "Placas de financiación de enero, un modelo por placa", "¿CUÁNTO QUEDA LA CUOTA DE CADA UNO?",
         "CUOTA", guion="G13", materiales=CONF + "Listas de enero (tarea T37).", evidencia="F17, F18")
reel("S06-4", ("F", d(2027, 1, 7)), E5, "Vender", "Llegó al salón: gastar menos nafta sin enchufar nada (ORA 05 HEV)", "G02", "Vendedor 2",
     "¿QUERÉS GASTAR MENOS NAFTA SIN ENCHUFAR NADA?", "ORA05", serie="Llegó al salón", publico="Muchos km por día",
     materiales=CONF + "Dato: 5,1 L/100 km de consumo mixto declarado.", evidencia="F07, F08")
reel("S06-5", ("F", d(2027, 1, 8)), E5, "Entretener", "Ida y vuelta a Jesús María: medimos lo que gasta", "G15", "Vendedor 1",
     "¿CUÁNTO GASTÁS PARA IR A JESÚS MARÍA Y VOLVER?", "RUTA", serie="Ida y vuelta medida",
     materiales="Festival de Jesús María del 7 al 17/1 (referencia, sin logo). Medir el 5 o 6/1: km, consumo, precio del litro o del kWh. PHEV o HEV en stock.", evidencia="F27, F02")
pz("S06-6", ("F", d(2027, 1, 9)), E5, "Vender", "TikTok + Instagram en vivo", "Vivo", "Vivo del sábado #1 desde el salón", "G20", "Contenido",
   aparece="Vendedor 1 + vendedor 2 en el chat", gancho="Preguntame lo que quieras de [2 modelos]", cta="Código VIVO-SAB en pantalla", hora="11:00", horas=1.5,
   metrica="Chats con VIVO-SAB en 24 h · turnos", materiales="Anunciarlo en historias jueves y viernes. Trípode, corbatero, wifi probado.", evidencia="F07", serie="Vivo del sábado")
pz("S06-7", ("F", d(2027, 1, 7)), E5, "Educar", "YouTube (+ 3 Shorts)", "Video largo", "Recorrido completo: Eado Plus", "G21", "Contenido",
   aparece="Vendedor 1", gancho="Eado Plus en Córdoba: recorrido completo y consumo real", cta="Link de WhatsApp con YT-EADO en la 1.ª línea", hora="18:00", horas=4.0,
   metrica="Retención media · clics al link", materiales="Se graba en la sesión del 5/1 junto con la prueba en ruta.", evidencia="F09", serie="YouTube cada 2 semanas")

# --- Semana del 11/1
reel("S07-1", ("F", d(2027, 1, 11)), E5, "Entretener", "Adiviná el 0 a 100", "G04", "Vendedor 2",
     "¿EN CUÁNTOS SEGUNDOS LLEGA A 100?", "JUEGO", serie="Adiviná",
     materiales="ORA 05 HEV: 7,7 s declarados por la marca. No medirlo en la calle.", evidencia="F02, F34")
reel("S07-2", ("F", d(2027, 1, 12)), E5, "Educar", "¿Cuánto dura la batería?", "G31", "Vendedor 2",
     "¿Y CUANDO LA BATERÍA SE GASTA, QUÉ?", "BATERIA", materiales="Garantías de batería exactas por modelo (Eado Plus: 8 años o 150.000 km).")
carrusel("S07-3", ("F", d(2027, 1, 13)), E5, "Educar", "Eléctrico, enchufable o híbrido: cuál te sirve para ir a las sierras",
         "¿CON CUÁL TE VAS A LAS SIERRAS?", "TIPO", guion="G37", materiales="Explicación de EV, PHEV y HEV del reel ya hecho (CLAUDE.md, sección 6). Sin especificaciones que no estén verificadas.")
reel("S07-4", ("F", d(2027, 1, 14)), E5, "Vender", "Entregas de la semana", "G19", "Clientes con autorización + vendedor",
     "ESTA SEMANA SE FUERON [N] AUTOS A [BARRIOS]", "ENTREGA", serie="Entregas", materiales="Autorizaciones firmadas.", evidencia="F23")
reel("S07-5", ("F", d(2027, 1, 15)), E5, "Entretener", "Así se prepara un auto antes de entregarlo", "G32", "Equipo",
     "ASÍ SE PREPARA UN AUTO ANTES DE ENTREGARLO", "ENTREGA", serie="Un día en Valparaiso", materiales="Una entrega programada para el día siguiente.")
pz("S07-6", ("F", d(2027, 1, 16)), E5, "Vender", "TikTok + Instagram en vivo", "Vivo", "Vivo del sábado #2 desde el salón", "G20", "Contenido",
   aparece="Vendedor 1 + vendedor 2 en el chat", gancho="Preguntame lo que quieras de [2 modelos]", cta="Código VIVO-SAB en pantalla", hora="11:00", horas=1.5,
   metrica="Chats con VIVO-SAB en 24 h · turnos", evidencia="F07", serie="Vivo del sábado")

# --- Semana del 18/1
reel("S08-1", ("F", d(2027, 1, 18)), E5, "Entretener", "¿Entra en una cochera de Nueva Córdoba?", "G14", "Vendedor 2",
     "¿ENTRA EN UNA COCHERA DE NUEVA CÓRDOBA?", "VALIJAS", serie="¿Entra todo?",
     materiales="Medidas oficiales del auto. Una cochera real medida con cinta (pedir permiso al edificio).")
reel("S08-2", ("F", d(2027, 1, 19)), E5, "Educar", "Lo que ve este auto que vos no ves (con lluvia)", "G17", "Vendedor 1",
     "CON ESTA LLUVIA, ¿VOS VES ESTO?", "LLUVIA",
     materiales="Publicarla una semana de lluvia (se puede mover dentro de enero). Asistencias según la ficha de la unidad.", evidencia="F28")
carrusel("S08-3", ("F", d(2027, 1, 20)), E5, "Vender", "Eado Plus en 10 placas (estilo 'focus' ya hecho, con precio y legal nuevos)",
         "¿Y SI VAS A TRABAJAR SIN CARGAR NAFTA?", "EADO",
         materiales=CONF + "Reusar el carrusel de 10 placas del Eado (CLAUDE.md, sección 6) con la placa de precio actualizada.", evidencia="F17")
reel("S08-4", ("F", d(2027, 1, 21)), E5, "Vender", "Llegó al salón: la cuenta de la nafta (Eado Plus)", "G02", "Vendedor 1",
     "HACÉ ESTA CUENTA CONMIGO", "EADO", serie="Llegó al salón", publico="Muchos km por día",
     materiales=CONF + "Guion MOF 'La cuenta de la nafta' del PDF de guiones. Las cuentas propias dicen 'estimado'.", evidencia="F07, F08")
reel("S08-5", ("F", d(2027, 1, 22)), E5, "Entretener", "Ida y vuelta a Cosquín en modo eléctrico", "G15", "Vendedor 1",
     "¿CUÁNTO GASTÁS PARA IR A COSQUÍN Y VOLVER?", "RUTA", serie="Ida y vuelta medida",
     materiales="Festival de Cosquín del 23 al 31/1 (referencia, sin logo). Medir el 19 o 20/1 con un PHEV: km en eléctrico y a nafta.", evidencia="F27")
pz("S08-6", ("F", d(2027, 1, 23)), E5, "Vender", "TikTok + Instagram en vivo", "Vivo", "Vivo del sábado #3 desde el salón", "G20", "Contenido",
   aparece="Vendedor 1 + vendedor 2 en el chat", gancho="Preguntame lo que quieras de [2 modelos]", cta="Código VIVO-SAB en pantalla", hora="11:00", horas=1.5,
   metrica="Chats con VIVO-SAB en 24 h · turnos", evidencia="F07", serie="Vivo del sábado")
pz("S08-7", ("F", d(2027, 1, 21)), E5, "Educar", "YouTube (+ 3 Shorts)", "Video largo", "Recorrido completo: Haval H6 PRO HEV", "G21", "Contenido",
   aparece="Vendedor 2", gancho="Haval H6 híbrida en Córdoba: recorrido completo y consumo real", cta="Link de WhatsApp con YT-H6", hora="18:00", horas=4.0,
   metrica="Retención media · clics al link", evidencia="F09", serie="YouTube cada 2 semanas")

# --- Semana del 25/1
reel("S09-1", ("F", d(2027, 1, 25)), E5, "Entretener", "Adiviná: ¿cuántos km hace con lo que sale un café?", "G04", "Vendedor 2",
     "¿CUÁNTOS KM HACE CON LO QUE SALE UN CAFÉ?", "JUEGO", serie="Adiviná",
     materiales="Tarifa de luz vigente (EPEC) y precio de un café en Córdoba ese día. Consumo ORA 03: 16,7 kWh/100 km WLTP. La cuenta va en la descripción ('estimado').")
reel("S09-2", ("F", d(2027, 1, 26)), E5, "Educar", "¿Cuánto pagás además del precio del auto?", "G41", "Vendedor 2",
     "¿CUÁNTO PAGÁS ADEMÁS DEL PRECIO DEL AUTO?", "TOTAL", serie="Cómo se compra",
     materiales="Montos reales de flete, patente y papeles, preparación y seguro, aprobados por Administración y el abogado.", evidencia="F50, F49")
carrusel("S09-3", ("F", d(2027, 1, 27)), E5, "Educar", "Cómo comparar créditos (sin nombrar bancos)",
         "LA CUOTA MÁS BAJA PUEDE SER LA MÁS CARA", "CREDITO", guion="G38",
         materiales="Contenido del reel de créditos ya hecho (CLAUDE.md, sección 6): prendario, UVA, plan de ahorro, financiación de marca; CFT.")
reel("S09-4", ("F", d(2027, 1, 28)), E5, "Vender", "Llegó al salón: si tenés cochera con enchufe (ORA 03)", "G02", "Vendedor 1",
     "SI TENÉS COCHERA CON ENCHUFE, MIRÁ ESTO", "ORA03", serie="Llegó al salón", publico="Curioso del eléctrico",
     materiales=CONF + "Datos: 310 km WLTP, carga 20–80 % en 36 min (oficial). Garantía del vehículo: verificar (5 o 7 años según la fuente).", evidencia="F07, F08")
reel("S09-5", ("F", d(2027, 1, 29)), E5, "Entretener", "Los autos más vendidos de enero", "G22", "Sin personas (voz del dueño)",
     "¿ADIVINÁS CUÁL FUE EL N.º 1 DE ENERO?", "DATO", resp="Dueño + Claude", horas=3.0,
     materiales="Dato de ACARA/DNRPA del 29/1 (último día hábil). Si el ranking es de otras marcas, revisar con el dueño la regla de no nombrarlas.", evidencia="F24")
pz("S09-6", ("F", d(2027, 1, 30)), E5, "Vender", "TikTok + Instagram en vivo", "Vivo", "Vivo del sábado #4 desde el salón (y evaluación)", "G20", "Contenido",
   aparece="Vendedor 1 + vendedor 2 en el chat", gancho="Preguntame lo que quieras de [2 modelos]", cta="Código VIVO-SAB en pantalla", hora="11:00", horas=1.5,
   metrica="Chats con VIVO-SAB en 24 h · turnos", materiales="Regla: si en 4 vivos no hubo ni 1 turno con VIVO-SAB, se dejan (tarea T39).", evidencia="F07", serie="Vivo del sábado")

# --- Semana del 1/2 (Cosquín Rock 6 y 7; fin de semana largo de Carnaval)
reel("S10-1", ("F", d(2027, 2, 1)), E6, "Entretener", "Adiviná: ¿qué hay debajo de este auto?", "G04", "Vendedor 2",
     "¿QUÉ HAY DEBAJO DE ESTE AUTO?", "JUEGO", serie="Adiviná",
     materiales="Haval H7 con la cámara que 've a través del piso': confirmar que la versión en stock la tiene.")
reel("S10-2", ("F", d(2027, 2, 2)), E6, "Educar", "Soy vendedor: haceme estas 3 preguntas", "G23", "Vendedor 2",
     "SOY VENDEDOR: ANTES DE COMPRAR, HACEME ESTAS 3 PREGUNTAS", "PREGUNTAS", serie="Cómo se compra", evidencia="F49")
carrusel("S10-3", ("F", d(2027, 2, 3)), E6, "Vender", "Placas de financiación de febrero", "¿CUÁNTO QUEDA LA CUOTA DE CADA UNO?", "CUOTA",
         guion="G13", materiales=CONF, evidencia="F17, F18")
reel("S10-4", ("F", d(2027, 2, 4)), E6, "Vender", "Entregas de la semana", "G19", "Clientes con autorización + vendedor",
     "ESTA SEMANA SE FUERON [N] AUTOS A [BARRIOS]", "ENTREGA", serie="Entregas", evidencia="F23")
reel("S10-5", ("F", d(2027, 2, 5)), E6, "Entretener", "Lo que pasa en el taller a las 8 de la mañana", "G32", "Técnicos",
     "LO QUE PASA EN EL TALLER A LAS 8 DE LA MAÑANA", "TALLER", serie="Un día en Valparaiso")
pz("S10-6", ("F", d(2027, 2, 6)), E6, "Vender", "TikTok + Instagram en vivo", "Vivo", "Vivo del sábado #5 (solo si la evaluación del 30/1 dio bien)", "G20", "Contenido",
   aparece="Vendedor 1 + vendedor 2 en el chat", gancho="Preguntame lo que quieras de [2 modelos]", cta="Código VIVO-SAB en pantalla", hora="11:00", horas=1.5,
   metrica="Chats con VIVO-SAB en 24 h · turnos", evidencia="F07", serie="Vivo del sábado")
pz("S10-7", ("F", d(2027, 2, 4)), E6, "Educar", "YouTube (+ 3 Shorts)", "Video largo", "Recorrido completo: ORA 03", "G21", "Contenido",
   aparece="Vendedor 1", gancho="ORA 03 en Córdoba: ¿te sirve un eléctrico? Recorrido completo", cta="Link de WhatsApp con YT-ORA03", hora="18:00", horas=4.0,
   metrica="Retención media · clics al link", evidencia="F09", serie="YouTube cada 2 semanas")

# --- Semana del 8/2 (Carnaval 8 y 9, San Valentín 14)
carrusel("S11-2", ("F", d(2027, 2, 10)), E6, "Educar", "¿Entendés el papel que te da el vendedor? Las 6 líneas que importan", "¿ENTENDÉS EL PAPEL QUE TE DA EL VENDEDOR?", "CREDITO", guion="G39",
         materiales="Modelo de cotización aprobado por el abogado (sin datos de clientes).")
reel("S11-1", ("F", d(2027, 2, 10)), E6, "Educar", "¿Auto chino? Repuestos y tiempos reales de un service", "G10", "Jefe de taller",
     "¿AUTO CHINO? ¿Y SI NECESITO UN REPUESTO?", "TALLER", serie="Mitos del auto chino", materiales="Tiempos reales de posventa de los últimos 3 meses.")
reel("S11-3", ("F", d(2027, 2, 11)), E6, "Vender", "Llegó al salón: [unidad Mitsubishi con stock]", "G02", "Vendedor 2",
     "[BENEFICIO PARA EL QUE MIRA]", "STOCK", serie="Llegó al salón", publico="Familia; Campo y pyme", materiales=CONF + "Datos de la ficha oficial con su fuente.")
reel("S11-4", ("F", d(2027, 2, 12)), E6, "Entretener", "Adiviná qué auto es por un detalle", "G04", "Vendedor 2",
     "¿QUÉ AUTO ES? ADIVINÁ POR EL DETALLE", "JUEGO", serie="Adiviná", materiales="5 primeros planos (llanta, faro, volante, tapa de carga, insignia tapada).")

# --- Semana del 15/2 (posible vuelta a clases el 24/2)
reel("S12-1", ("F", d(2027, 2, 15)), E6, "Entretener", "Desafío: un día entero sin nafta", "G15", "Vendedor 1",
     "¿SE PUEDE PASAR UN DÍA ENTERO SIN NAFTA?", "RUTA", serie="Ida y vuelta medida",
     materiales="Eado Plus cargado la noche anterior. Recorrido real de un día de trabajo en Córdoba. Números medidos.")
reel("S12-2", ("F", d(2027, 2, 16)), E6, "Educar", "Auto para la familia: lo que hay que mirar si llevás chicos", "G24", "Vendedor 1",
     "SI LLEVÁS CHICOS AL COLE, MIRÁ ESTO ANTES DE ELEGIR", "FAMILIA", materiales="Butaca infantil con ISOFIX. Sin chicos en cámara salvo autorización de los padres.")
carrusel("S12-3", ("F", d(2027, 2, 17)), E6, "Vender", "Placas de financiación: los 5 modelos con más stock", "ELEGÍ EL TUYO Y TE DECIMOS LA CUOTA", "CUOTA",
         guion="G13", materiales=CONF, evidencia="F17, F18")
reel("S12-4", ("F", d(2027, 2, 18)), E6, "Vender", "Llegó al salón: [unidad con más stock de febrero]", "G02", "Vendedor 1",
     "[BENEFICIO PARA EL QUE MIRA]", "STOCK", serie="Llegó al salón", publico="Según la unidad", materiales=CONF)
reel("S12-5", ("F", d(2027, 2, 19)), E6, "Entretener", "Adiviná cuánto mide la pantalla", "G04", "Vendedor 2",
     "¿CUÁNTO MIDE ESTA PANTALLA?", "JUEGO", serie="Adiviná", materiales="Medida oficial de la ficha (ej.: Eado Plus 13,2 pulgadas; H7 15,6 pulgadas, verificar).")
pz("S12-6", ("F", d(2027, 2, 18)), E6, "Educar", "YouTube (+ 3 Shorts)", "Video largo", "Recorrido completo: Haval H7 4x4", "G21", "Contenido",
   aparece="Vendedor 1", gancho="Haval H7 4x4 en Córdoba: recorrido completo y consumo real", cta="Link de WhatsApp con YT-H7", hora="18:00", horas=4.0,
   metrica="Retención media · clics al link", evidencia="F09", serie="YouTube cada 2 semanas")

# --- Semana del 22/2
reel("S13-1", ("F", d(2027, 2, 22)), E6, "Entretener", "Este sedán es más largo que esta SUV", "G16", "Vendedor 1 y vendedor 2",
     "¿CUÁL ES MÁS LARGO?", "LARGO", serie="Vs",
     materiales="Eado Plus (4,77 m) contra una SUV de la casa en el salón, medidas oficiales. Si el Deepal no está, usar otra SUV en stock.")
reel("S13-2", ("F", d(2027, 2, 23)), E6, "Educar", "Para el campo: lo que tiene que tener una 4x4", "G25", "Vendedor 1",
     "¿TE QUEDASTE ENCAJADO ALGUNA VEZ EN EL CAMPO?", "CAMPO",
     materiales="Haval H7 o Poer en stock. Confirmar bloqueo, modos y potencia de la toma de 220 V de la versión. Expoagro: 9 al 12/3.", evidencia="F27")
carrusel("S13-3", ("F", d(2027, 2, 24)), E6, "Educar", "Preguntas frecuentes del local nuevo: horario, service, prueba de manejo, usado",
         "TODO LO QUE NOS PREGUNTARON DESDE QUE ABRIMOS", "PREGUNTAS", materiales="Las 8 preguntas más repetidas en WhatsApp desde la inauguración.")
reel("S13-4", ("F", d(2027, 2, 25)), E6, "Vender", "Entregas de febrero", "G19", "Clientes con autorización + vendedor",
     "EN FEBRERO SE FUERON [N] AUTOS A [BARRIOS]", "ENTREGA", serie="Entregas", evidencia="F23")
reel("S13-5", ("F", d(2027, 2, 26)), E6, "Entretener", "Los autos más vendidos de febrero", "G22", "Sin personas (voz del dueño)",
     "¿ADIVINÁS CUÁL FUE EL N.º 1 DE FEBRERO?", "DATO", resp="Dueño + Claude", horas=3.0, materiales="Dato de ACARA/DNRPA del 26/2.", evidencia="F24")

# --- Inauguración (todas relativas al Día D)
reel("INA-01", ("D", -15), E1, "Entretener", "Se arma el nuevo Valparaiso, ep. 1: ¿adivinás dónde queda?", "G03", "Equipo",
     "¿ADIVINÁS DÓNDE QUEDA?", "", serie="Se arma el nuevo Valparaiso", horas=1.0,
     materiales="Permiso para filmar la obra. Pistas reales del lugar, sin la dirección.", evidencia="F02, F34")
pz("INA-02", ("D", -14), E1, "Vender", "WhatsApp (difusión)", "Mensaje de WhatsApp", "Invitación a la noche VIP (base con permiso)", "G29", "Primer contacto",
   aparece="", gancho="Invitación con botón para confirmar", cta="Respondé SÍ", hora="10:00", horas=1.0, metrica="Respuestas SÍ ÷ enviados",
   materiales="Lista de invitados (T21) cruzada con el Registro No Llame (T20). Texto en la guía, sección Plantillas.", evidencia="F31", serie="Mensajes de la inauguración")
reel("INA-03", ("D", -10), E2, "Entretener", "Se arma el nuevo Valparaiso, ep. 2: ¿cuántos autos entran?", "G03", "Equipo",
     "¿CUÁNTOS AUTOS ENTRAN ACÁ?", "", serie="Se arma el nuevo Valparaiso", horas=1.0, materiales="Timelapse del armado del salón o llegada de unidades.")
pz("INA-04", ("D", -10), E2, "Vender", "WhatsApp (difusión)", "Mensaje de WhatsApp", "Aviso de mudanza a clientes de taller y compradores", "G29", "Primer contacto",
   gancho="Último turno en el local viejo y primero en el nuevo, con el mapa", cta="Respondé para pedir turno", hora="10:00", horas=1.0,
   metrica="Turnos de service pedidos", materiales="Base de clientes de taller con permiso.", serie="Mensajes de la inauguración")
pz("INA-05", ("D", -10), E2, "Vender", "Perfil de Empresa de Google", "Publicación de Google", "Publicación de evento: inauguramos el [fecha]", "G26", "Contenido", publico="Los que ya nos buscan en Google",
   gancho="Inauguramos el [fecha]: te esperamos", cta="Botón WhatsApp con código GBP", hora="12:30", horas=0.5, metrica="Clics en el botón · cómo llegar",
   materiales="Foto del local nuevo. No cambiar todavía la dirección del perfil (eso es el Día D).", evidencia="F11", serie="Google semanal")
reel("INA-06", ("D", -8), E2, "Entretener", "Anuncio oficial: fecha, dirección y día abierto", "G05", "Dueño o vendedor 1",
     "¿CUÁNTO TARDÁS EN LLEGAR A [REFERENCIA]?", "ABRIMOS", horas=2.0,
     materiales="Dirección nueva confirmada. Horario del día abierto. Beneficio de inauguración si existe (con bases en la web). Se usa como anuncio (A2).", evidencia="F29, F30, F17")
for n, (dias, texto) in enumerate([
        (-7, "Falta una semana: fachada + sticker de cuenta regresiva"),
        (-6, "Detrás de escena + encuesta '¿qué querés ver primero?'"),
        (-5, "El equipo de ventas: una foto por vendedor con su nombre"),
        (-4, "Cómo llegar: mapa + sticker de enlace a Google Maps"),
        (-3, "Sticker de pregunta: '¿qué le querés preguntar al taller?'"),
        (-2, "La prueba de manejo es con turno: sticker a WhatsApp con TURNO"),
        (-1, "Cobertura de la noche VIP + 'mañana abrimos'")], start=1):
    pz(f"INA-CR{n}", ("D", dias), E2 if dias < -1 else E3, "Vender", "IG + FB Historias", "Historias", f"Cuenta regresiva D{dias}: {texto}", "G06", "Contenido",
       gancho="Sticker de cuenta regresiva 'Inauguración'", cta="Sticker de enlace a WhatsApp (TURNO) cuando corresponde", hora="11:00", horas=0.3,
       metrica="Toques en el sticker · respuestas", serie="Cuenta regresiva", evidencia="F02")
reel("INA-07", ("D", -5), E2, "Educar", "¿Auto chino? ¿Y si se rompe? (el taller nuevo)", "G10", "Jefe de taller + vendedor",
     "¿AUTO CHINO? ¿Y SI SE ROMPE?", "TALLER", serie="Mitos del auto chino",
     materiales="El taller nuevo armado. Garantías exactas con su condición. Tiempo real de un repuesto común.", evidencia="F02")
pz("INA-08", ("D", -3), E2, "Vender", "WhatsApp (difusión)", "Mensaje de WhatsApp", "Recordatorio a los que confirmaron la noche VIP", "G29", "Primer contacto",
   gancho="Recordatorio con fecha, hora y dirección", cta="", hora="10:00", horas=0.5, metrica="Asistencia ÷ confirmados", serie="Mensajes de la inauguración")
carrusel("INA-09", ("D", -3), E2, "Educar", "Lo que vas a encontrar en el nuevo local (8 placas)", "¿QUÉ CAMBIA PARA VOS CON EL LOCAL NUEVO?", "ABRIMOS", guion="G40",
         materiales="Fotos reales: salón, taller, entrega, estacionamiento, sala de espera, cargadores (si hay). Horario y dirección.")
pz("INA-10", ("D", -3), E2, "Vender", "Perfil de Empresa de Google", "Publicación de Google", "Publicación de evento: día abierto del sábado", "G26", "Contenido", publico="Los que ya nos buscan en Google",
   gancho="Sábado [fecha] · día abierto de [hora] a [hora]", cta="Botón WhatsApp con código GBP", hora="12:30", horas=0.5, metrica="Clics en el botón", serie="Google semanal", evidencia="F11")
reel("INA-11", ("D", -2), E2, "Vender", "Prueba de manejo con turno el sábado (y beneficio de inauguración si existe)", "G05", "Vendedor 1",
     "¿QUERÉS PROBARLO ANTES DE DECIDIR? EL SÁBADO TE LO PRESTAMOS", "TURNO",
     materiales="Recorrido, seguro y turnos de 30 min listos (T27). Beneficio con bases en la web si existe; 'Sin obligación de compra' si hay azar.", evidencia="F29, F17, F19")
pz("INA-12", ("D", -1), E3, "Vender", "WhatsApp (difusión)", "Mensaje de WhatsApp", "Mañana abrimos: ubicación, horario y estacionamiento", "G29", "Primer contacto",
   gancho="Ubicación en Google Maps + horario", cta="", hora="18:00", horas=0.5, metrica="Check-ins del día abierto", serie="Mensajes de la inauguración")
pz("INA-13", ("D", -1), E3, "Entretener", "IG + FB Historias", "Historias", "Noche VIP: historias cada 20–30 minutos", "G07", "Contenido",
   aparece="Dueño, importadora, invitados con autorización", gancho="Corte de cinta y palabras del dueño", cta="", hora="19:30", horas=3.0,
   metrica="Vistas y respuestas", materiales="Autorizaciones firmadas en la acreditación. Foto oficial para prensa a las 22:30.", serie="Inauguración", evidencia="F23")
pz("INA-14", ("D", 0), E3, "Vender", "TikTok + Instagram en vivo", "Vivo", "Día abierto: vivo de 30–45 min recorriendo el salón", "G07", "Contenido",
   aparece="Vendedor 1 + vendedor 2 en el chat", gancho="Estamos abiertos: te muestro el salón nuevo en vivo", cta="Código VIVO en pantalla", hora="11:00", horas=1.5,
   metrica="Chats con VIVO en 24 h · turnos", serie="Inauguración", evidencia="F07")
pz("INA-15", ("D", 0), E3, "Vender", "IG + FB Historias", "Historias", "Día abierto: historias cada hora", "G07", "Contenido",
   gancho="Lo que pasa en el salón", cta="Sticker de enlace a WhatsApp con INAUGURACION-QR", hora="10:00", horas=2.0,
   metrica="Toques en el sticker", serie="Inauguración", evidencia="F23")
pz("INA-16", ("D", 0), E3, "Vender", "Perfil de Empresa de Google", "Publicación de Google", "Publicación 'Nos mudamos' con fotos reales (el día que cambia la dirección)", "G26", "Contenido", publico="Los que ya nos buscan en Google",
   gancho="Nos mudamos: ahora estamos en [dirección nueva]", cta="Botón 'Cómo llegar'", hora="09:00", horas=0.5,
   metrica="Pedidos de 'cómo llegar' · llamadas", materiales="Va junto con la tarea T30 (mudanza digital).", serie="Google semanal", evidencia="F12, F14")
pz("INA-17", ("D", 0), E3, "Vender", "Estados de WhatsApp", "Estado de WhatsApp", "Hoy abrimos: dirección y horario", "G27", "Primer contacto",
   gancho="Hoy abrimos de [hora] a [hora]", cta="Respondé este estado", hora="09:00", horas=0.2, metrica="Respuestas al estado", serie="Inauguración")
reel("INA-18", ("D", 1), E4, "Entretener", "Así fue la inauguración", "G08", "Equipo e invitados con autorización",
     "[N] PERSONAS VINIERON A VER ESTO", "ABRIMOS", horas=2.0, materiales="Número real de check-ins. Clips de todo el equipo.", evidencia="F02")
reel("INA-19", ("D", 2), E4, "Educar", "Cómo llegar al nuevo local", "G09", "Sin personas",
     "DE [PUNTO CONOCIDO] AL NUEVO VALPARAISO EN [N] MINUTOS", "", horas=1.0, materiales="Recorrido grabado desde 2 puntos conocidos con el celular en soporte.")
pz("INA-20", ("D", 2), E4, "Vender", "WhatsApp (difusión)", "Mensaje de WhatsApp", "Gracias + turno de prueba (a los que vinieron) y pedido de reseña (a los que compraron o hicieron service)", "G29", "Primer contacto",
   gancho="Gracias por venir", cta="Link de reseña de Google (a todos los clientes, sin premio)", hora="10:00", horas=1.0,
   metrica="Reseñas nuevas · turnos", serie="Mensajes de la inauguración", evidencia="F15, F16")
carrusel("INA-21", ("D", 4), E4, "Entretener", "Así quedó: el nuevo local en 8 fotos", "ASÍ QUEDÓ EL NUEVO VALPARAISO", "ABRIMOS",
         materiales="Fotos del día abierto (con autorización) y del local vacío con buena luz.")

# --- Piezas que se repiten cada semana
SEMANAS = [d(2026, 11, 30) + dt.timedelta(days=7 * k) for k in range(13)]
ETAPA_SEMANA = [E1, E1, E2, E4, E4, E5, E5, E5, E5, E6, E6, E6, E6]
GOOGLE = [
    ("Oferta", "Unidad con más stock con cuota y legal"),
    None,  # semana de la publicación de evento (INA-05)
    None,  # semana del día abierto (INA-10)
    ("Novedad", "Horario de fiestas en el local nuevo"),
    ("Novedad", "Horario de enero y cómo llegar"),
    ("Oferta", "Promo de apertura (si está confirmada) con su legal"),
    ("Oferta", "Cuota de un modelo con su legal"),
    ("Novedad", "El taller y cómo pedir turno de service"),
    ("Oferta", "Cuota de un modelo con su legal"),
    ("Novedad", "Unidades que llegaron (cupo 2027, si llegaron)"),
    ("Oferta", "Cuota de un modelo con su legal"),
    ("Novedad", "Auto para la familia: vuelta a clases"),
    ("Oferta", "4x4 para el campo con su legal"),
]
FERIADOS = {d(2027, 2, 8): d(2027, 2, 10)}  # lunes de Carnaval: lo semanal arranca el miércoles
for k, lunes in enumerate(SEMANAS):
    n = f"{k + 1:02d}"
    etapa = ETAPA_SEMANA[k]
    semana, lunes = lunes, FERIADOS.get(lunes, lunes)
    pz(f"S{n}-H", ("F", lunes), etapa, "Vender", "IG + FB Historias", "Historias", "Historias de la semana (de lunes a sábado)", "G28", "Contenido",
       gancho="Lun stock · Mar detrás de escena · Mié encuesta · Jue pregunta · Vie entregas · Sáb horario o vivo", cta="Sticker de enlace a WhatsApp con HISTORIA",
       hora="11:00", horas=2.0, metrica="Toques en el sticker · respuestas", serie="Todas las semanas", evidencia="F02",
       materiales="En la semana de la cuenta regresiva se suman las de G06." if k in (1, 2) else "")
    pz(f"S{n}-W", ("F", lunes), etapa, "Vender", "Estados de WhatsApp", "Estado de WhatsApp", "Estados de WhatsApp de la semana (1–3 por día hábil)", "G27", "Primer contacto",
       gancho="La unidad del día", cta="Respondé este estado", hora="09:00", horas=0.5, metrica="Respuestas al estado", serie="Todas las semanas",
       materiales=CONF if k != 0 else CONF + "Primera semana: avisar en el estado que pueden guardar el número.")
    jueves = semana + dt.timedelta(days=3)
    if not (jueves.month == 12 and jueves.day in (24, 31)):
        pz(f"S{n}-ML", ("F", jueves), etapa, "Vender", "Mercado Libre", "Aviso de Mercado Libre",
           "Mercado Libre: video de la unidad en 2 avisos, fotos propias y preguntas respondidas en minutos", "G02", "Contenido",
           publico="Los que ya buscan en Mercado Libre",
           gancho="Primeros segundos con el auto real del salón", cta="'Consultá financiación' (confirmar si se puede derivar a WhatsApp)", hora="10:00", horas=1.0,
           metrica="Preguntas por aviso · tiempo de respuesta", serie="Todas las semanas",
           materiales="Semana de la mudanza: cambiar la ubicación de todos los avisos (T33)." if k == 3 else "Usar el tomas de apoyo de la grabación del martes.")
    if GOOGLE[k]:
        tipo, tema = GOOGLE[k]
        miercoles = semana + dt.timedelta(days=2)
        pz(f"S{n}-G", ("F", miercoles), etapa, "Vender" if tipo == "Oferta" else "Educar", "Perfil de Empresa de Google", "Publicación de Google",
           f"Publicación de Google ({tipo.lower()}): {tema} + 5 fotos nuevas", "G26", "Contenido",
           publico="Los que ya nos buscan en Google",
           gancho="Título en minúsculas normales, foto propia con texto", cta="Botón WhatsApp con código GBP", hora="12:30", horas=0.5,
           metrica="Clics en el botón · llamadas · cómo llegar", serie="Google semanal", evidencia="F11",
           materiales=CONF if tipo == "Oferta" else "")

# ---------------------------------------------------------------- tareas
TAREAS = []


def tarea(id_, cuando, area, tarea_, pasos, resp, prioridad="Media", guia="", evidencia=""):
    TAREAS.append(dict(id=id_, cuando=cuando, area=area, tarea=tarea_, pasos=pasos, resp=resp, prioridad=prioridad, guia=guia, evidencia=evidencia))


tarea("T01", ("F", d(2026, 11, 26)), "Decisiones", "Confirmar el Día D, la dirección nueva y la habilitación comercial",
      "1) Pedir al gestor el estado de la habilitación del local nuevo (final de obra, bomberos, cartel): sin habilitación no hay apertura. 2) Fecha de fin de obra. 3) Elegir: noche VIP el viernes 18/12 y día abierto el sábado 19/12, o del 28 al 30/12 si la obra no llega (o apertura silenciosa y evento grande en febrero o marzo). 4) ¿El local viejo cierra o sigue como taller? 5) Escribir todo en la hoja Inicio.",
      "Dueño", "Alta", "Sección 9", "F29")
tarea("T02", ("F", d(2026, 11, 27)), "Importadora", "Pedido por escrito a la importadora (Grupo Antelo)",
      "Pedir: unidades de exhibición y de prueba para el día abierto; presencia de un directivo; una condición comercial de lanzamiento para la promo del 4/1; manual de imagen del salón (si existe); cambio de dirección en los localizadores el Día D; bonificaciones de diciembre y enero por modelo; qué unidades del cupo 2027 llegan y cuándo.",
      "Dueño", "Alta", "Sección 9", "F29, F30, F38")
tarea("T03", ("F", d(2026, 11, 27)), "Decisiones", "Verificar Changan y Bancor antes de decirlo en cámara",
      "1) Cómo se presenta Valparaiso para Changan (¿'concesionario oficial'?): pedirlo por escrito a la marca. 2) Si la casa está adherida a Bancor 'De Una!' y qué parte de las ventas sale por ahí. 3) Si la red exige un CRM o portal de leads propio.",
      "Dueño", "Alta", "Sección 3")
tarea("T04", ("F", d(2026, 11, 27)), "Producción", "Primera sesión de grabación (para la semana del 30/11)",
      "Grabar en 2–3 h: G01 (patentar), G02 con el Eado Plus, G03 ep. 1 (obra), tomas de apoyo de 3 unidades con las tomas fijas del G02 y fotos para el carrusel del 2/12. 3 tomas de cada gancho; el resto una vez.",
      "Contenido", "Alta", "Sección 5")
tarea("T05", ("F", d(2026, 11, 30)), "Equipo", "Nombrar responsables y hacer la reunión de arranque",
      "1) Nombrar responsable de contenido, 2 vendedores en cámara y responsable de primer contacto; escribirlos en Inicio. 2) Reunión de 45 min con esta planilla y la guía: rutina semanal, reglas que no se negocian, qué no se dice en cámara (nada de bromas sobre precios, clientes ni autos de la casa).",
      "Dueño", "Alta", "Secciones 1 y 3")
tarea("T06", ("F", d(2026, 11, 30)), "Medición", "Tomar la línea de base",
      "Anotar hoy: seguidores de Instagram, TikTok y Facebook; alcance de los últimos 30 días; reseñas y calificación en Google; búsquedas y llamadas del Perfil de Google (últimos 3 meses); chats de WhatsApp por semana; tiempo de primera respuesta (hacer 3 consultas de prueba). Guardar captura de todo.",
      "Contenido", "Alta", "Sección 12", "F15")
tarea("T07", ("F", d(2026, 11, 30)), "Producción", "Comprar el kit de grabación",
      "2 micrófonos corbateros inalámbricos (para las piezas con dos vendedores), 1 luz LED con difusor, 1 estabilizador de mano, 1 trípode con soporte de celular, 1 batería externa, paño de limpieza de lente. Celular con cámara trasera en 4K a 30 o 60 fps.",
      "Contenido", "Alta", "Sección 5")
tarea("T08", ("F", d(2026, 12, 1)), "WhatsApp", "Configurar WhatsApp Business",
      "1) Catálogo con al menos un producto por modelo (lo pide el agente de IA de WhatsApp). 2) Mensaje de bienvenida y de ausencia. 3) Respuestas rápidas: cuota (con legal), turno de prueba, usado, cómo llegar, horario. 4) Etiquetas: una por código y A/B/C. 5) Link corto con mensaje ya escrito para la bio (código BIO).",
      "Primer contacto", "Alta", "Sección 7")
tarea("T09", ("F", d(2026, 12, 1)), "Medición", "Planilla de leads (o CRM)",
      "Columnas: fecha y hora, canal, código, nombre, teléfono, modelo, cómo paga (contado, financiado, usado), plazo, letra A/B/C, vendedor, etapa (consulta, calificado, turno, prueba, venta), próximo paso y fecha. Regla: primera respuesta humana en menos de 5 minutos en horario.",
      "Primer contacto", "Alta", "Sección 7", "F32")
tarea("T10", ("D", -18), "Decisiones", "Decidir beneficio directo o sorteo",
      "Recomendado: un beneficio directo sin azar (service bonificado o accesorio para quien compre en el período, con vigencia y stock). Si igual hay sorteo: gratis, sin compra ni prueba de manejo obligatoria, solo mayores de 18, bases en la web, 'Sin obligación de compra' en cada pieza, escribano y consulta previa a la Lotería de Córdoba.",
      "Dueño", "Alta", "Sección 9", "F19")
tarea("T11", ("D", -18), "Evento", "Cotizar el evento",
      "Pedir 2 o 3 cotizaciones de: sonido o DJ (con música con licencia comercial o pago de SADAIC y AADI-CAPIF para el día abierto); catering (sin alcohol el día abierto); cartelería del local nuevo y del viejo; fotógrafo o video (o equipo propio); personal extra de recepción; seguro de responsabilidad civil; área protegida o ambulancia.",
      "Dueño", "Media", "Sección 9", "F21")
tarea("T12", ("D", -18), "Google", "Preparar el Perfil de Google para la mudanza",
      "1) Confirmar quién es el propietario y que haya 2 administradores. 2) Exportar estadísticas y reseñas. 3) Buscar en Maps la dirección nueva y alrededores: si hay pines viejos, pedir que se marquen como cerrados o mudados. 4) Juntar pruebas para la reverificación: fotos del cartel instalado, interior y exterior, habilitación. 5) Mismo nombre, teléfono y web.",
      "Contenido", "Alta", "Sección 10", "F12, F13, F14")
tarea("T13", ("D", -17), "Legal", "Revisión del abogado: legales de las piezas y página de condiciones",
      "1) Modelo de legal para piezas con precio o cuota: en digital, cuotas y CFTEA dentro de la pieza (Res. 446/2025); precio final en pesos y precio sin impuestos nacionales (Res. 4/2025); frase 'PARA MÁS INFORMACIÓN…' al menos 5 s. 2) Leer la nota de Beccar Varela de julio de 2026 sobre la simplificación. 3) Página www.valparaisomotors.com.ar/condiciones con vigencia, CUIT, domicilio, condiciones y stock. 4) Plantilla de cotización con CFT.",
      "Abogado", "Alta", "Sección 3", "F17, F18")
tarea("T14", ("D", -17), "Legal", "Autorización de imagen (entregas y evento)",
      "Texto con alcance (redes y anuncios pagos), plazo y que se puede revocar. Versión en papel (50 copias), casilla en el check-in con QR y versión para padres de menores. Si alguien la revoca, se baja la pieza.",
      "Abogado", "Alta", "Sección 3", "F23")
tarea("T15", ("D", -17), "Web", "Arreglos del sitio (pedido a Asofix)",
      "Del Plan de leads: íconos a las redes propias, botón de WhatsApp flotante y uno por ficha con mensaje ya escrito, horario correcto, despublicar o llenar 'Puntos de carga', Google Tag Manager con píxel de Meta y 2 eventos (clic en WhatsApp y formulario). Página de condiciones (T13).",
      "Asofix", "Alta", "Sección 10")
tarea("T16", ("D", -16), "Evento", "Pedir el permiso eventual al municipio",
      "Dirección de Espectáculos Públicos (Ord. 11.684): un día abierto con música y actividades es espectáculo público aunque sea gratis. Presentar al menos 15 días antes: capacidad y plan de evacuación del local, seguro de responsabilidad civil con el Municipio como asegurado, cobertura de área protegida. Preguntar si piden policía adicional. Trámite aparte si hay estructuras en la vereda o la calle.",
      "Gestor", "Alta", "Sección 9", "F20")
tarea("T17", ("D", -16), "Instagram", "Ordenar el perfil de Instagram",
      "Bio: 'Concesionario Oficial · Córdoba' (con las marcas confirmadas en T03) + qué resolvés + link de WhatsApp con código BIO. Destacadas: Financiación, Stock por marca, Entregas, Taller, Cómo llegar, Preguntas y Nuevo local. 3 fijados: financiación vigente, el reel que más chats trajo y 'cómo comprar en Valparaiso'.",
      "Contenido", "Media", "Sección 6")
tarea("T18", ("D", -16), "Instagram", "Automatizar comentario → mensaje (ManyChat u otra)",
      "Una palabra por pieza (hoja Códigos). El único mensaje permitido (Meta: uno por comentario, dentro de 7 días) trae 2 botones que abren WhatsApp con el código. Probarlo desde una cuenta que no sigue (le llega a Solicitudes). A la semana de publicada cada pieza, cambiar el fijado a 'escribinos por WhatsApp (link en la bio)'.",
      "Contenido", "Alta", "Sección 7", "F05, F06")
tarea("T19", ("D", -16), "Producción", "Plantillas de edición y música",
      "1) Plantilla en CapCut o Edits: subtítulos palabra por palabra en la letra de la marca (palabra activa en bordó), placa final con el CTA y el logo, legal de 5 s, guía de zonas seguras. 2) Elegir 10 temas de la Sound Collection de Meta (Instagram y Facebook) y 10 de la Commercial Music Library de TikTok y anotarlos en un archivo de créditos. Nada de canciones de moda. 3) Exportar siempre el video final sin marca de agua.",
      "Contenido", "Media", "Sección 5", "F22, F39")
tarea("T20", ("D", -16), "WhatsApp", "Armar la base de clientes con permiso",
      "Juntar compradores de los últimos 2–3 años, clientes de taller y leads A y B. Dejar solo a quienes aceptaron recibir mensajes. Cruzar con el Registro No Llame. Segmentar: VIP, taller, leads.",
      "Primer contacto", "Alta", "Sección 9")
tarea("T21", ("D", -15), "Evento", "Lista de invitados de la noche VIP",
      "Clientes de los últimos 2–3 años, flotas y pymes, importadora, ACARA regional, prensa, referentes locales. Invitar autoridades con nota formal. Lista cerrada: es la que permite tratarlo como evento privado para la música (Decreto 765/2024).",
      "Dueño", "Alta", "Sección 9", "F21")
tarea("T22", ("D", -12), "Prensa", "Kit de prensa con un dato que sea noticia",
      "El patrón que funcionó en Córdoba: la apertura más un anuncio concreto (Autocity con su preventa; Familia Parra con un convenio con EPEC y ACARA). Elegir un dato real: unidades entregadas de un modelo, taller preparado para alta tensión, cargadores, una línea de financiación. Incluir m², servicios, marcas, horario, fotos reales, citas del dueño y de la importadora, dirección con mapa.",
      "Dueño", "Alta", "Sección 9", "F29, F30")
tarea("T23", ("D", -10), "Prensa", "Mandar el kit a la prensa",
      "Infonegocios, Cadena 3, La Voz y Córdoba Motor (CBA24N). Evaluar un espacio de marca o una alianza con una radio. Seguimiento por teléfono en D-3. Invitarlos a la noche VIP.",
      "Dueño", "Media", "Sección 9", "F29")
tarea("T24", ("D", -10), "Evento", "Check-in con QR y carteles de filmación",
      "QR en la entrada que abre WhatsApp con 'Vengo a la inauguración (INAUGURACION-QR)' y una casilla de consentimiento de imagen y de contacto. Cartel: 'Este evento se filma y fotografía para las redes de Valparaiso Motors'. Imprimir 3 QR grandes.",
      "Contenido", "Alta", "Sección 9", "F23")
tarea("T25", ("D", -8), "Mudanza", "Cartel 'Nos mudamos' en el local viejo",
      "Cartel grande con la dirección nueva y un QR a Google Maps, desde D-7 hasta al menos D+90. Alguien del equipo o seguridad deriva a la gente.",
      "Dueño", "Media", "Sección 10")
tarea("T26", ("D", -7), "Mudanza", "Avisar a marcas, bancos y directorios",
      "Pedir a GWM, Mitsubishi y Grupo Antelo (Changan, JMEV) el cambio en sus localizadores para el Día D. Avisar a Bancor, Banco Nación (+Autos) y financieras de marca. Preparar los cambios en Mercado Libre, Facebook, Instagram, TikTok, Apple Business Connect, Bing Places, Waze y directorios (elcerokm, Zona Auto, gtm.com.ar, greatwall.com.ar).",
      "Contenido", "Alta", "Sección 10", "F14")
tarea("T27", ("D", -5), "Evento", "Ensayo de las pruebas de manejo",
      "Recorrido fijo y corto, seguro de cada unidad, licencia del que maneja, turnos de 30 min, alcoholemia cero (Córdoba). El día abierto se maneja solo con turno, en franjas separadas del público (Familia Parra no hizo pruebas por la concurrencia). Nadie maneja en la noche VIP.",
      "Vendedores", "Alta", "Sección 9", "F29")
tarea("T28", ("D", -3), "Evento", "Brief con todo el equipo",
      "Roles de la hoja Evento, plantilla de cotización con CFT, las 5 preguntas para calificar A/B/C, cómo pedir reseñas, qué no se dice en cámara, quién responde WhatsApp en cada franja.",
      "Dueño", "Alta", "Sección 9")
tarea("T29", ("D", -2), "WhatsApp", "Guardia reforzada de WhatsApp",
      "De D-2 a D+7: dos personas en horario, primera respuesta en menos de 5 minutos, todo cargado en la planilla con su código.",
      "Primer contacto", "Alta", "Sección 7", "F32")
tarea("T30", ("D", 0), "Mudanza", "Mudanza digital (el primer día que se atiende en el local nuevo)",
      "En este orden: 1) Web: contacto, pie, mapa y 'nos mudamos' en la portada. 2) Perfil de Google: editar la dirección del perfil existente (no crear uno nuevo) y hacer la reverificación ese día. 3) Publicación 'nos mudamos' con fotos reales (INA-16). 4) No tocar el nombre ni la categoría hasta que Google publique el cambio. 5) Bio y ubicación de Instagram y Facebook.",
      "Contenido", "Alta", "Sección 10", "F12, F13, F14")
tarea("T31", ("D", 1), "Ventas", "Seguimiento de los leads de la inauguración en 72 horas",
      "Todos los contactos con código INAUGURACION: WhatsApp en menos de 5 minutos, llamada si dejaron teléfono y aceptaron, propuesta de turno de prueba. En EE. UU., cerca de 3 de cada 4 ventas pasan en los primeros 3 días del lead.",
      "Primer contacto", "Alta", "Sección 7", "F32")
tarea("T32", ("D", 1), "Medición", "Cargar el evento en la planilla",
      "Check-ins, leads (A/B/C), turnos de prueba tomados, notas de prensa. Contar los asistentes reales para el reel INA-18.",
      "Contenido", "Alta", "Sección 12")
tarea("T33", ("D", 2), "Mudanza", "Actualizar todos los directorios y Mercado Libre",
      "Todos los de T26 con la dirección nueva + ubicación de todos los avisos de Mercado Libre.",
      "Contenido", "Alta", "Sección 10", "F14")
tarea("T34", ("D", 3), "Prensa", "Juntar las notas publicadas",
      "Medio, fecha, si tiene dirección y link. Compartirlas en historias.",
      "Dueño", "Baja", "Sección 9")
for n, dias in enumerate((7, 14, 21, 30, 60), start=1):
    tarea(f"T35.{n}", ("D", dias), "Google", f"Control del mapa y de duplicados (D+{dias})",
          "Buscar en Google Maps 'concesionaria GWM Córdoba', 'Haval Córdoba', 'Changan Córdoba' y 'Mitsubishi Córdoba' desde 5 puntos de la ciudad y anotar la posición. Revisar si apareció un perfil duplicado en la dirección vieja o la nueva (si no tiene reseñas, pedir que se borre; si tiene, pedir la fusión a soporte).",
          "Contenido", "Media", "Sección 10", "F12, F14")
tarea("T36", ("F", d(2026, 12, 28)), "Promo", "Confirmar por escrito la promo de apertura",
      "Condición (de la importadora o de la casa), modelos, inicio 4/1, fin, stock. Subir las bases a la página de condiciones. Sin esto, la pieza S06-1 no sale.",
      "Dueño", "Alta", "Sección 3", "F17")
tarea("T37", ("F", d(2027, 1, 2)), "Promo", "Listas de precios de enero",
      "Antes del 4/1: actualizar placas, carrusel de financiación, avisos de Mercado Libre, respuestas rápidas de WhatsApp y el anuncio de retargeting.",
      "Administración", "Alta", "Sección 3")
tarea("T38", ("D", -1), "Reseñas", "Arrancar el pedido de reseñas en cada entrega y service",
      "QR en la carpeta de entrega + WhatsApp a las 48 h con el link directo, a todos los clientes (no solo a los contentos) y sin premio (Google lo prohíbe). Pedir que nombren al vendedor. Responder todas en 48 h. Meta: más de 20 reseñas recientes en 90 días con 4,5 o más.",
      "Primer contacto", "Alta", "Sección 7", "F15, F16")
tarea("T39", ("F", d(2027, 1, 30)), "Decisiones", "Evaluar los 4 vivos del sábado",
      "Si en 4 vivos no hubo ni 1 turno con el código VIVO-SAB, se dejan y esas horas van a más piezas de stock. Si hubo, siguen todos los sábados.",
      "Dueño", "Media", "Sección 12", "F07")
tarea("T40", ("F", d(2027, 1, 13)), "Importadora", "Cupo 2027: qué llega y cuándo",
      "Preguntar a la importadora qué unidades del cupo 2027 llegan a Córdoba y cuándo. Si llegan en febrero, preparar la pieza 'Llegó al salón' y la publicación de Google de la semana del 1/2.",
      "Dueño", "Media", "", "F38")
tarea("T41", ("D", 30), "Medición", "Revisión de 30 días de la inauguración",
      "Tablero del evento: check-ins, leads A/B, pruebas de manejo, ventas con código INAUGURACION, reseñas nuevas, búsquedas por nombre (Perfil de Google), posición en el mapa y notas de prensa, contra la línea de base (T06).",
      "Dueño", "Alta", "Sección 12")
tarea("T42", ("D", 60), "Medición", "Revisión de 60 días y decisión de marzo",
      "Lo mismo que a 30 días más: qué objetivo (Entretener, Educar, Vender) trajo más chats con código; ajustar la mezcla y el presupuesto; decidir si se hace un segundo evento en marzo.",
      "Dueño", "Alta", "Sección 12")
tarea("T43", ("F", d(2027, 2, 10)), "Producción", "Grabar de más para marzo",
      "Febrero baja: usar la sesión del martes para grabar 6–8 piezas MOF para marzo (comparativas y objeciones con vendedores).",
      "Contenido", "Media", "Sección 5", "F25")
tarea("T44", ("F", d(2027, 2, 15)), "Decisiones", "Expoagro (9 al 12/3)",
      "Decidir si se hace algo para H7, Poer y L200 (pieza G25, anuncio a productores). Pedir unidades a la importadora.",
      "Dueño", "Baja", "", "F27")
tarea("T45", ("F", d(2026, 12, 4)), "Anuncios", "Armar las campañas A1 (WhatsApp) y A5 (Google)",
      "Seguir la hoja Anuncios y la sección 11 de la guía. Probar que el anuncio abra WhatsApp con la bienvenida y las 3 respuestas rápidas.",
      "Contenido", "Alta", "Sección 11", "F33")
tarea("T46", ("D", -10), "Anuncios", "Armar la campaña A2 de la inauguración",
      "Público: personas que viven a 15–20 km de la dirección nueva. Creativo: INA-06 (anuncio oficial) y la historia de D-2.",
      "Contenido", "Media", "Sección 11")
tarea("T47", ("F", d(2026, 12, 30)), "Anuncios", "Preparar enero: retargeting y presupuesto",
      "Armar A3 (retargeting de quienes vieron el 50–95 % de los reels y viven a 50 km) y A4 (promoción del mejor reel de cada semana). Subir A1 al presupuesto de enero el 4/1.",
      "Contenido", "Alta", "Sección 11")
tarea("T48", ("F", d(2027, 1, 8)), "Anuncios", "Prueba de formularios contra WhatsApp (A6)",
      "Mismo creativo y mismo radio; formulario de 'mayor intención' con una sola pregunta: '¿Cuándo pensás cambiar el auto? 0–30 días / 1–3 meses / solo miro'. Comparar costo por turno que asiste el 8/2.",
      "Contenido", "Media", "Sección 11")
tarea("T49", ("F", d(2027, 2, 1)), "Anuncios", "Bajar el presupuesto de febrero",
      "Pasar A1 al presupuesto de febrero. Mover el dinero al canal con menor costo por turno que asiste.",
      "Contenido", "Media", "Sección 11", "F25")
for k, lunes in enumerate(SEMANAS):
    tarea(f"R{k + 1:02d}", ("F", FERIADOS.get(lunes, lunes)), "Rutina", "Rutina de la semana",
          "Lunes: 30 min de planificación (stock que entró, promos confirmadas) y tablero de la semana anterior. Lunes: 30 min de escucha: leer desde el navegador Reddit (r/argentina, r/Cordoba, r/RepublicaArgentina: 'Haval', 'Changan', 'GWM', 'auto chino', 'patentar enero', 'gastos de entrega'), los grupos de Facebook de dueños de Haval y Changan y las preguntas de Mercado Libre; anotar las preguntas textuales (sirven para 'El vendedor responde', G18). Martes a la mañana: grabación de 2–3 h; el responsable de primer contacto no graba y sigue con WhatsApp. Martes a jueves: edición. Viernes: el dueño aprueba con la hoja de cuadros las piezas de la semana siguiente. Todos los días: historias, Estados y respuestas en menos de 5 minutos.",
          "Contenido", "Media", "Sección 4")

# ---------------------------------------------------------------- anuncios
ANUNCIOS = [
    dict(nombre="A1a · WhatsApp: stock real (diciembre)", objetivo="Mensajes (WhatsApp)",
         publico="Personas que viven a 30–50 km del salón (hasta el Día D, la dirección actual; desde ahí, la nueva). 18+ años. Sin categoría especial (no es obligatoria en la Argentina).",
         creativos="S01-3, S02-2, INA-11 + placas de 6–8 s", destino="WhatsApp con bienvenida y 3 respuestas rápidas", usd_dia=12,
         desde=("F", d(2026, 12, 7)), hasta=("F", d(2027, 1, 3)), metrica="Costo por conversación · % calificado",
         regla="En la semana 3, apagar el creativo con mayor costo por lead calificado y duplicar el mejor. Si Meta ofrece optimizar por leads en los anuncios a WhatsApp en la Argentina, probarlo contra 'conversaciones' y quedarse con el de menor costo por turno que asiste."),
    dict(nombre="A1b · WhatsApp: stock real (enero, el pico)", objetivo="Mensajes (WhatsApp)", publico="Igual que A1a con la dirección nueva.",
         creativos="S06-1, S06-4, S08-4, S09-4 + placas", destino="WhatsApp", usd_dia=20, desde=("F", d(2027, 1, 4)), hasta=("F", d(2027, 1, 31)),
         metrica="Costo por turno que asiste", regla="Si el costo por turno que asiste es aceptable para el dueño, mantener; si no, bajar a 12."),
    dict(nombre="A1c · WhatsApp: stock real (febrero)", objetivo="Mensajes (WhatsApp)", publico="Igual que A1b.",
         creativos="S10-4, S11-3, S12-4 + placas", destino="WhatsApp", usd_dia=10, desde=("F", d(2027, 2, 1)), hasta=("F", d(2027, 2, 28)),
         metrica="Costo por turno que asiste", regla="Febrero cae ~37 % contra enero: pautar menos y producir más."),
    dict(nombre="A2 · Inauguración: alcance cerca del local nuevo", objetivo="Mensajes (WhatsApp) con código ABRIMOS",
         publico="Personas que viven a 15–20 km de la dirección nueva. 18+.", creativos="INA-06, INA-11", destino="WhatsApp (turno de prueba)",
         usd_dia=10, desde=("D", -8), hasta=("D", 0), metrica="Turnos de prueba tomados · check-ins", regla="Se apaga el Día D a las 18 h."),
    dict(nombre="A3 · Retargeting de los que vieron los reels", objetivo="Mensajes (WhatsApp)",
         publico="Vieron el 50–95 % de los reels o interactuaron con la cuenta en 30–90 días, y viven a 50 km. Excluir compradores.",
         creativos="Placas animadas de 6–8 s con precio, cuota y legal (G12, G13)", destino="WhatsApp", usd_dia=5,
         desde=("F", d(2027, 1, 4)), hasta=("F", d(2027, 2, 28)), metrica="Costo por conversación · % calificado",
         regla="Acá se puede nombrar el modelo: este público ya vio el video."),
    dict(nombre="A4 · Promoción del mejor reel de la semana", objetivo="Interacción o reproducciones",
         publico="Personas que viven a 50 km. 18+.", creativos="El reel de Entretener o Educar con mejor tasa de salto de la semana",
         destino="El reel (alimenta A3)", usd_dia=3, desde=("F", d(2027, 1, 4)), hasta=("F", d(2027, 2, 28)),
         metrica="Costo por reproducción al 50 %", regla="Se cambia el reel cada lunes."),
    dict(nombre="A5 · Google Search: modelo + Córdoba", objetivo="Búsqueda (clics a WhatsApp o a la ficha)",
         publico="Córdoba y 50 km. Palabras: 'Haval H6 híbrida Córdoba', 'concesionaria GWM Córdoba', 'Mitsubishi Córdoba 0km', 'Changan Córdoba'.",
         creativos="Anuncios de texto con extensiones de llamada y de ubicación", destino="WhatsApp o la página del modelo", usd_dia=5,
         desde=("F", d(2026, 12, 14)), hasta=("F", d(2027, 2, 28)), metrica="Costo por conversación",
         regla="Las búsquedas de modelos chinos en Córdoba son pocas: el gasto se autolimita."),
    dict(nombre="A6 · Prueba: formulario contra WhatsApp", objetivo="Clientes potenciales (formulario de mayor intención)",
         publico="Igual que A1b.", creativos="El mismo creativo que gane en A1b", destino="Formulario con una pregunta y pantalla de confirmación",
         usd_dia=6, desde=("F", d(2027, 1, 11)), hasta=("F", d(2027, 2, 7)), metrica="Costo por turno que asiste (formulario vs WhatsApp)",
         regla="El 8/2 gana el canal con menor costo por turno que asiste."),
]

# ---------------------------------------------------------------- evento
EVENTO = [
    ("Noche VIP (lista cerrada)", "", "", "", "", ""),
    ("Armado", "14:00", "Autos en posición, limpieza, prueba de sonido, carteles 'este evento se filma', QR de check-in, lista impresa, autorizaciones de imagen en papel.", "Contenido + vendedores", "Fotos del local vacío con buena luz (sirven para INA-21).", "Lista de invitados, 50 autorizaciones, cinta y tijera, baterías cargadas."),
    ("Recepción", "19:30", "Acreditación con la lista; firma de la autorización de imagen. Bebidas; alcohol solo para mayores de 18 que no manejan.", "Recepción (2–4 personas)", "Historias de la llegada (solo con autorización).", "Cartel de la Ley 24.788. Música: evento privado con lista cerrada."),
    ("Palabras", "20:15", "Dueño (3 min) y la importadora (3 min). Se anuncia el dato-noticia.", "Dueño", "Clip de 15 s para historias y prensa.", "Micrófono inalámbrico."),
    ("Corte de cinta", "20:30", "Corte de cinta y foto oficial con el dueño, la importadora y autoridades (si aceptaron).", "Dueño", "Foto oficial para prensa (se manda a las 22:30).", "Fotógrafo."),
    ("Recorrido", "20:45", "Recorrido en grupos: salón, taller, zona de entrega.", "Vendedores", "Historias del recorrido.", ""),
    ("Charla y turnos", "21:00", "Los vendedores toman turnos de prueba para los días siguientes. Nadie maneja esta noche.", "Vendedores", "", "Plantilla de cotización con CFT."),
    ("Cierre", "22:30", "Cierre. Mandar la foto y el texto a la prensa.", "Dueño", "", ""),
    ("Día abierto", "", "", "", "", ""),
    ("Brief del equipo", "08:30", "Roles: recepción con QR; 1 asesor cada 3–4 autos; 2–3 personas coordinan las pruebas de manejo; guardia de WhatsApp; 1 supervisor.", "Dueño", "", "Proporciones de una guía de personal para eventos de concesionarias (proveedor)."),
    ("Apertura", "10:00", "Check-in con QR → WhatsApp 'Vengo a la inauguración (INAUGURACION-QR)' con casilla de consentimiento.", "Recepción", "Historias cada hora (INA-15).", "Permiso eventual, seguro, área protegida, matafuegos, baños, estacionamiento señalizado."),
    ("Vivo", "11:00", "Vivo de 30–45 min recorriendo el salón (G07). Un segundo vendedor responde el chat y WhatsApp.", "Vendedor 1 + vendedor 2", "Vivo en Instagram y TikTok (INA-14).", "Trípode, corbatero, wifi probado."),
    ("Pruebas de manejo", "11:00–17:00", "Solo con turno, en franjas de 30 min, recorrido fijo, licencia y alcoholemia cero. El que llega sin turno, se agenda para otro día.", "Coordinadores de pruebas", "Clips cortos de autos saliendo (sin patentes legibles).", "Seguro de las unidades, planilla de turnos."),
    ("Actividad familiar", "12:00–15:00", "Actividad para chicos y comida, sin alcohol. Música con licencia comercial o con SADAIC y AADI-CAPIF pagos (el día abierto es ejecución pública).", "Contenido", "Fotos generales; primeros planos de chicos solo con firma de los padres.", "Catering, sonido."),
    ("Cierre", "18:00", "Cierre al público.", "Dueño", "", ""),
    ("Carga de leads", "18:30", "Cargar check-ins y leads con su letra A/B/C. Mensaje de gracias a todos los que dejaron contacto.", "Primer contacto", "", "Planilla de leads."),
    ("72 horas", "D+1 a D+3", "Seguimiento de todos los leads INAUGURACION (tarea T31).", "Primer contacto + vendedores", "", ""),
]

# ---------------------------------------------------------------- códigos
CODIGOS = [
    ("BIO", "Link de la bio de Instagram y TikTok", "Bio", "Hola, vengo de su perfil (BIO). Quiero precio y financiación."),
    ("HISTORIA", "Sticker de enlace en historias", "Historias", "Hola, vengo de las historias (HISTORIA). Quiero precio y financiación."),
    ("ESTADO", "Respuestas a los Estados de WhatsApp", "Estados", "(entra como respuesta al estado: etiquetar ESTADO a mano)"),
    ("GBP", "Botón de las publicaciones del Perfil de Google", "Google", "Hola, los encontré en Google (GBP). Quiero precio y financiación."),
    ("ML", "Consultas que vienen de Mercado Libre", "Mercado Libre", "(etiquetar ML a mano)"),
    ("INAUGURACION-VIP", "Respuestas a la invitación de la noche VIP", "WhatsApp (difusión)", "SÍ, voy a la inauguración (INAUGURACION-VIP)."),
    ("INAUGURACION-QR", "Check-in del día abierto", "QR en la entrada", "Vengo a la inauguración (INAUGURACION-QR)."),
    ("INAUGURACION-PRENSA", "Notas de prensa o radio", "Link en la nota", "Hola, los vi en la nota de la inauguración (INAUGURACION-PRENSA)."),
    ("TURNO", "Turnos de prueba de manejo de la inauguración", "Historias y reel INA-11", "Hola, vengo de las historias (TURNO). Quiero un turno de prueba de manejo."),
    ("ABRIMOS", "Anuncio y resumen de la inauguración", "INA-06, INA-18, INA-21, A2", "Hola, vengo del video de la inauguración (ABRIMOS). Quiero un turno de prueba de manejo."),
    ("VIVO", "Vivo del día abierto", "Vivo INA-14", "Hola, vengo del vivo (VIVO). Quiero precio y financiación."),
    ("VIVO-SAB", "Vivos de los sábados de enero", "Vivos", "Hola, vengo del vivo del sábado (VIVO-SAB). Quiero precio y financiación."),
    ("MUDANZA", "Aviso de mudanza a clientes de taller", "WhatsApp (difusión)", "Hola, quiero un turno de service en el local nuevo (MUDANZA)."),
    ("APERTURA", "Promo de apertura de enero", "S06-1, A3", "Hola, vengo del video de la promo de apertura (APERTURA). Quiero precio y financiación."),
    ("ENERO", "¿Comprás ahora o esperás a enero?", "S01-1", "Hola, vengo del video ENERO. Quiero precio y financiación."),
    ("PREGUNTAS", "5 preguntas / 3 preguntas / preguntas frecuentes", "S01-2, S10-2, S13-3", "Hola, vengo del video PREGUNTAS. Quiero precio y financiación."),
    ("EADO", "Stock y carrusel del Eado Plus", "S01-3, S08-3, S08-4", "Hola, vengo del video EADO. Quiero precio y financiación."),
    ("H6", "Stock del Haval H6 PRO HEV", "S02-2", "Hola, vengo del video H6. Quiero precio y financiación."),
    ("ORA05", "Stock del ORA 05 HEV", "S06-4", "Hola, vengo del video ORA05. Quiero precio y financiación."),
    ("ORA03", "Stock del ORA 03", "S09-4", "Hola, vengo del video ORA03. Quiero precio y financiación."),
    ("STOCK", "Otras unidades del 'Llegó al salón'", "S11-3, S12-4", "Hola, vengo del video STOCK. Quiero precio y financiación."),
    ("TALLER", "Taller, posventa y mitos del auto chino", "S02-1, INA-07, S10-5, S11-1", "Hola, vengo del video TALLER. Quiero precio y financiación."),
    ("AGUINALDO", "El aguinaldo como anticipo", "S03-1", "Hola, vengo del video AGUINALDO. Quiero precio y financiación."),
    ("ENTREGA", "Entregas y detrás de escena", "S04-1, S07-4, S07-5, S10-4, S13-4", "Hola, vengo del video ENTREGA. Quiero precio y financiación."),
    ("VALIJAS", "¿Entra todo? (baúl y cochera)", "S05-1, S08-1", "Hola, vengo del video VALIJAS. Quiero precio y financiación."),
    ("RUTA", "Ida y vuelta medida y taller antes de viajar", "S05-2, S06-5, S08-5, S12-1", "Hola, vengo del video RUTA. Quiero precio y financiación."),
    ("CUOTA", "Placas de financiación", "S06-3, S10-3, S12-3", "Hola, vengo del carrusel CUOTA. Quiero precio y financiación."),
    ("ENCHUFE", "¿Enchufe o nafta?", "S06-2", "Hola, vengo del video ENCHUFE. Quiero precio y financiación."),
    ("JUEGO", "Serie 'Adiviná'", "S07-1, S09-1, S10-1, S11-4, S12-5", "Hola, vengo del juego del video (JUEGO). Quiero precio y financiación."),
    ("BATERIA", "¿Cuánto dura la batería?", "S07-2", "Hola, vengo del video BATERIA. Quiero precio y financiación."),
    ("TIPO", "Carrusel EV, PHEV o HEV para las sierras", "S07-3", "Hola, vengo del carrusel TIPO. Quiero precio y financiación."),
    ("LLUVIA", "Asistencias con lluvia", "S08-2", "Hola, vengo del video LLUVIA. Quiero precio y financiación."),
    ("PREGUNTA", "El vendedor responde (plantilla G18, para cuando una pregunta se repite)", "Cualquier semana, en lugar de una pieza de Educar", "Hola, vengo del video PREGUNTA. Quiero precio y financiación."),
    ("TOTAL", "¿Cuánto pagás además del precio del auto?", "S09-2", "Hola, vengo del video TOTAL. Quiero el total por escrito."),
    ("CREDITO", "Carruseles de créditos y cotización", "S09-3, S11-2", "Hola, vengo del carrusel CREDITO. Quiero precio y financiación."),
    ("DATO", "Los autos más vendidos del mes", "S09-5, S13-5", "Hola, vengo del video DATO. Quiero precio y financiación."),
    ("FAMILIA", "Auto para la familia", "S12-2", "Hola, vengo del video FAMILIA. Quiero precio y financiación."),
    ("LARGO", "¿Cuál es más largo?", "S13-1", "Hola, vengo del video LARGO. Quiero precio y financiación."),
    ("CAMPO", "4x4 para el campo", "S13-2", "Hola, vengo del video CAMPO. Quiero precio y financiación."),
    ("YT-EADO", "YouTube: Eado Plus", "S06-7", "Hola, vengo del video de YouTube del Eado Plus (YT-EADO). Quiero precio y financiación."),
    ("YT-H6", "YouTube: Haval H6 PRO HEV", "S08-7", "Hola, vengo del video de YouTube de la H6 (YT-H6). Quiero precio y financiación."),
    ("YT-ORA03", "YouTube: ORA 03", "S10-7", "Hola, vengo del video de YouTube del ORA 03 (YT-ORA03). Quiero precio y financiación."),
    ("YT-H7", "YouTube: Haval H7", "S12-6", "Hola, vengo del video de YouTube de la H7 (YT-H7). Quiero precio y financiación."),
    ("ANUNCIO-WA", "Anuncios a WhatsApp (Meta pone el origen solo)", "A1, A2, A3", "(lo marca Meta: etiquetar ANUNCIO-WA)"),
    ("FORMULARIO", "Formularios de Meta", "A6", "(llega por el formulario: etiquetar FORMULARIO)"),
]

# ---------------------------------------------------------------- tablero
TABLERO_INICIO = d(2026, 11, 30)
TABLERO_COLUMNAS = [
    ("Semana (lunes)", None, None, None),
    ("Piezas de feed publicadas", "Reels + carruseles + videos largos de la semana", None, None),
    ("Reproducciones", "Suma de todas las redes", None, None),
    ("Cuentas alcanzadas en Córdoba", "Instagram Insights → ubicaciones principales: % de Córdoba × cuentas alcanzadas", None, None),
    ("Envíos por DM", "Instagram: compartidos de la semana", None, None),
    ("Tasa de salto 3 s (%)", "Promedio de los reels de la semana (Instagram Insights). Escribila como porcentaje, ej. 45%", None, "PROMEDIO"),
    ("Seguidores nuevos", None, None, None),
    ("Comentarios que nombran un modelo", None, None, None),
    ("Consultas (DM + WhatsApp + ML + formularios)", "Todas las conversaciones nuevas de la semana", None, None),
    ("Consultas con código", "Las que trajeron un código de la hoja Códigos", None, None),
    ("Leads calificados (A + B)", "Dio datos, modelo y forma de pago, y compra en menos de 3 meses", None, None),
    ("Turnos o pruebas de manejo", None, None, None),
    ("Turnos que asistieron", None, None, None),
    ("Ventas", None, None, None),
    ("Reseñas nuevas en Google", None, None, None),
    ("Calificación de Google", "La del perfil al final de la semana", None, "PROMEDIO"),
    ("Primera respuesta, mediana (min)", "En horario comercial", None, "PROMEDIO"),
    ("Gasto en anuncios (USD)", "Meta + Google de la semana", None, None),
    ("% consultas con código", None, "=IFERROR(J{i}/I{i},0)", None),
    ("% calificados", None, "=IFERROR(K{i}/I{i},0)", None),
    ("% asistencia a turnos", None, "=IFERROR(M{i}/L{i},0)", None),
    ("USD por consulta", None, "=IFERROR(R{i}/I{i},0)", None),
    ("USD por turno que asiste", None, "=IFERROR(R{i}/M{i},0)", None),
    ("USD por venta", None, "=IFERROR(R{i}/N{i},0)", None),
]
TABLERO_NOTAS = [
    "Se completa los lunes con los números de la semana anterior. Las celdas amarillas se escriben; las tasas y los costos se calculan solos.",
    "La que decide es 'Consultas con código' y lo que sigue (calificados, turnos, ventas). Una pieza con muchas vistas y pocos chats con código no se repite: es la lección del reel de 150 mil vistas sin leads.",
    "Referencias externas, solo para ver si la cuenta está muy lejos de lo normal: Emplifi (concesionarias, 3.er trimestre de 2026) da 25 interacciones medianas por reel y 22 por carrusel en Instagram. No hay referencias argentinas.",
    "Embudo de referencia de EE. UU. (Foureyes): 35–45 % de los contactados saca turno, asiste el 56–62 % y cierra ~42 %. A los 60–90 días, reemplazarlo por los números propios.",
]

# ---------------------------------------------------------------- fuentes
FUENTES = [
    ("F01", "Frecuencia de 3 a 5 publicaciones por semana", "2,1 millones de posts de ~102.000 cuentas: 3–5 por semana duplican el crecimiento de seguidores contra 1–2 (+0,26 % contra +0,12 % semanal) y las semanas en cero penalizan. Es correlación.", "Buffer, 13/08/2025", "https://buffer.com/resources/how-often-to-post-on-instagram/", "Estudio grande (correlación)"),
    ("F02", "Qué premia Instagram", "Mosseri: tiempo de visualización, 'me gusta' por alcance y envíos por alcance (los envíos pesan más para llegar a no seguidores). Cerca de la mitad mira sin sonido. Lo no original se muestra menos.", "Buffer, citando a Adam Mosseri", "https://buffer.com/resources/instagram-algorithms/", "Declaración de la plataforma"),
    ("F03", "Reels de prueba", "Se muestran primero a no seguidores; sirven para elegir el gancho, no para traer leads locales.", "Instagram Creators", "https://creators.instagram.com/blog/instagram-trial-reels", "Oficial"),
    ("F05", "Un solo mensaje por comentario", "La respuesta privada a un comentario se manda dentro de 7 días y es una sola; el seguimiento solo si la persona responde. En vivos, solo durante la transmisión.", "Meta for Developers", "https://developers.facebook.com/docs/instagram-platform/private-replies/", "Oficial"),
    ("F06", "ManyChat dispara con el primer comentario", "En Instagram, el disparador solo se activa con el primer comentario de cada persona en cada publicación.", "ManyChat Help", "https://help.manychat.com/hc/en-us/articles/14281316989724", "Oficial del proveedor"),
    ("F07", "Vivos con vendedores", "MG Chile vendió 30 autos a leads de TikTok entre el 8/10 y el 1/12/2024 con vivos de ~2 h, dos por día, de lunes a sábado.", "24 Horas (Chile), 13/02/2025", "https://www.24horas.cl/motores-24/ventas-de-autos-por-tiktok-esta-es-la-marca-que-esta-impulsando-esta-", "Dato de la marca"),
    ("F08", "Recorridos y comparativas", "Datos de TikTok (NADA Show 2026, sin metodología): 38 % compara autos en TikTok y 51 % arma ahí su lista corta; buscan recorridos, dueños reales y pros y contras.", "CBT News, 10/02/2026", "https://www.cbtnews.com/why-dealers-can-no-longer-ignore-tiktok-in-the-buying-journey/", "Dato de la plataforma"),
    ("F09", "YouTube para investigar", "1.022 compradores de la India (mayo de 2026): ~6 de cada 10 dicen que YouTube armó su lista inicial; usaron recorridos, pruebas, comparativas y guías por versión.", "Google y Kantar, vía Autocar Professional", "https://www.autocarpro.in/news/google-kantar-study-93-percent-of-car-buyers-use-ai-in-research-134885", "Encuesta (otro país)"),
    ("F10", "Benchmark de concesionarias", "Mediana de 25 interacciones por reel, 22 por carrusel y 9 por imagen en Instagram; ~3 publicaciones por semana.", "Emplifi, 3.er trimestre de 2026", "https://emplifi.io/resources/q3-2026-auto-dealership-worldwide-benchmarks/", "Benchmark del rubro"),
    ("F11", "Publicaciones del Perfil de Google", "Las de oferta promediaron 3,06 clics contra 0,76 las de novedades; sin fotos de stock rinden ~5,6 veces más. No mueven el ranking.", "Sterling Sky (datos de 2021)", "https://www.sterlingsky.ca/google-posts/", "Estudio viejo (EE. UU.)"),
    ("F12", "Mudanza sin perfil nuevo", "No crear un perfil nuevo por cambio de dirección; con el mismo nombre, las reseñas pasan.", "Google Business Profile Help", "https://support.google.com/business/answer/3098204?hl=en", "Oficial"),
    ("F13", "Reverificación", "Si el negocio se muda después de verificado, hay que verificarlo de nuevo; Google revisa el cambio antes de publicarlo.", "Google Business Profile Help", "https://support.google.com/business/answer/3039617?hl=en", "Oficial"),
    ("F14", "Orden de la mudanza", "Editar el perfil, revisar pines, web primero, no tocar nombre ni categoría mientras se verifica, después los directorios.", "Whitespark (2021)", "https://whitespark.ca/blog/best-practices-when-moving-your-business-gmb-listing/", "Práctica de especialistas"),
    ("F15", "Reseñas", "68 % exige al menos 4 estrellas, 47 % no usa un negocio con menos de 20 reseñas, 74 % mira las de los últimos 3 meses.", "BrightLocal, 2026", "https://www.brightlocal.com/research/local-consumer-review-survey/", "Encuesta (EE. UU.)"),
    ("F16", "Reseñas sin premio", "Google prohíbe las reseñas incentivadas.", "Google", "https://support.google.com/contributionpolicy/answer/16597558", "Oficial"),
    ("F17", "Legal de ofertas y financiación", "Res. 446/2025: en digital, cuotas y CFTEA dentro de la pieza; frase de remisión a la web al menos 5 s; 'Sin obligación de compra' en la pieza si hay sorteo.", "Boletín Oficial; abogados.com.ar", "https://www.boletinoficial.gob.ar/pdf/aviso/primera/333879/20260227", "Norma"),
    ("F18", "Precios en pesos", "Res. 4/2025: precio final en pesos (dólar solo como agregado) y precio sin impuestos nacionales.", "Secretaría de Industria y Comercio", "https://argentina.gob.ar/sites/default/files/exhibicion_de_precios_resolucion_4_2025_0.pdf", "Norma"),
    ("F19", "Sorteos y comparativas", "DNU 274/2019: art. 14 prohíbe sorteos atados a una compra; art. 15 fija las condiciones de la publicidad comparativa.", "argentina.gob.ar", "https://www.argentina.gob.ar/normativa/nacional/decreto-274-2019-322236/texto", "Norma"),
    ("F20", "Permiso del evento", "Ord. 11.684: un evento abierto al público en un local privado es espectáculo público aunque sea gratis; permiso eventual; 15 días de antelación como referencia.", "Municipalidad de Córdoba (texto 2014)", "https://documentos.cordoba.gob.ar/MUNCBA/AreasGob/CULTURA/OBSERVATORIO/legislaciones/musica/municipales/espectaculos-publicos/ordenanza-n-11684-codigo-de-espectaculos-publicos-texto-actualizado-online-2014.pdf", "Norma (verificar cambios)"),
    ("F21", "Música en el evento", "Con lista cerrada no hay ejecución pública (Decreto 765/2024); un día abierto paga SADAIC y AADI-CAPIF o usa una licencia comercial.", "Derecho en Zapatillas, 30/07/2026", "https://www.derechoenzapatillas.com/2026/musica-en-tu-local-que-se-paga-hoy-a-quien-cuando-y-cuanto/", "Fuente secundaria"),
    ("F22", "Música en TikTok", "Las empresas tienen que usar la Commercial Music Library en toda actividad comercial, también en lo orgánico.", "TikTok Ads Help", "https://ads.tiktok.com/help/article/commercial-music-library-creators?lang=en", "Oficial"),
    ("F23", "Imagen de clientes", "Art. 53 del Código Civil y Comercial: hace falta consentimiento para captar y reproducir imagen y voz. Una aerolínea fue condenada a pagar más de $24 millones por usar una imagen sin permiso.", "Marval O'Farrell Mairal", "https://www.marval.com/publicacion/condenan-a-una-aerolinea-por-uso-indebido-de-imagen-17415", "Norma y jurisprudencia"),
    ("F24", "Diciembre flojo, enero fuerte", "Dic. 2025: 23.997 patentamientos (−32 % contra noviembre). Ene. 2026: 66.080 (+174 %). Córdoba: 7.585 en enero.", "Ámbito (ACARA/DNRPA)", "https://www.ambito.com/autos/arranque-dispar-el-mercado-automotor-menos-patentamientos-que-2025-pero-suba-frente-diciembre-n6240858", "Dato oficial del sector"),
    ("F25", "Febrero baja", "Feb. 2026: 42.026 patentamientos, 36,8 % menos que enero.", "El Economista", "https://eleconomista.com.ar/autos/aparecieron-cifras-patentamientos-0-km-son-buenas-n93203", "Dato oficial del sector"),
    ("F26", "Aguinaldo", "Vence el viernes 18/12/2026.", "iProfesional", "https://www.iprofesional.com/actualidad/468457-aguinaldo-de-diciembre-cual-es-la-fecha-limite-para-cobrarlo", "Prensa"),
    ("F27", "Festivales y Expoagro", "Jesús María del 7 al 17/1/2027; Cosquín del 23 al 31/1; Cosquín Rock 6 y 7/2; Carnaval 8 y 9/2; Expoagro del 9 al 12/3.", "Perfil, Los Andes, Expoagro", "https://www.perfil.com/noticias/cordoba/jesus-maria-2027-cuando-es-quienes-actuan-y-cuando-salen-a-la-venta-las-entradas.phtml", "Prensa y sitio oficial"),
    ("F28", "Verano lluvioso", "El SMN anticipa para Córdoba un verano más fresco y lluvioso de lo normal, con tormentas más intensas.", "Meteored / SMN", "https://www.meteored.com.ar/noticias/prediccion/se-viene-un-verano-raro-que-anticipa-el-smn-para-noviembre-diciembre-y-enero-y-como-planificar-las-vacaciones.html", "Pronóstico oficial (promedio)"),
    ("F29", "Inauguraciones en Córdoba", "Familia Parra (BYD, dic. 2025): convenio con EPEC y ACARA en el acto, sorteo con un medio y sin pruebas de manejo por la concurrencia.", "Cadena 3", "https://www.cadena3.com/noticia/ahora-pais/familia-parra-inaugura-este-jueves-su-concesionario-oficial-byd-en-cordoba_496756", "Prensa (promocional)"),
    ("F30", "Un dato que sea noticia", "Autocity armó la noticia de su apertura BYD sobre la preventa: 450 unidades en Córdoba antes de abrir.", "Infonegocios, 10/11/2025", "https://infonegocios.info/plus/byd-llego-a-cordoba-autocity-inauguro-su-nuevo-salon-lider-en-la-preventa-de-la-marca-en-argentina", "Prensa"),
    ("F31", "Formato VIP + día abierto", "Formato de 1 a 3 días: preestreno VIP y prensa, día de público con pruebas de manejo y captura de leads; proporciones de personal.", "Air Fresh Marketing, 20/04/2026", "https://www.airfreshmarketing.com/blog/how-to-staff-auto-dealership-grand-opening", "Proveedor (sin resultados)"),
    ("F32", "Responder rápido y en 72 horas", "Embudo de EE. UU.: 35–45 % saca turno, asiste 56–62 %, cierra ~42 %; ~3 de cada 4 ventas pasan en los primeros 3 días del lead.", "Foureyes", "https://www.foureyes.io/blog/2025-automotive-dealer-benchmarks-report", "Proveedor con datos"),
    ("F33", "Anuncios a WhatsApp", "Kia Italia: 144 leads calificados, 5 ventas directas y 53 % menos de costo por auto vendido con un agente que calificaba.", "WhatsApp Business", "https://whatsappbusiness.com/resources/success-stories/kia-italia/", "Caso de la empresa"),
    ("F34", "Entretener y series", "El consumidor pide autenticidad y entretenimiento; 57 % pide series de contenido original; al 33 % le da vergüenza ver marcas en tendencias.", "Sprout Social Index 2025", "https://sproutsocial.com/insights/index/", "Encuesta"),
    ("F35", "Entretener, educar, vender", "La frase la difunde Adley Kinsman (Viralish) sin datos detrás; Binet y Field (IPA) dan ~60/40 entre marca y activación para marcas grandes, como pauta que varía.", "Russell Brunson Show ep. 25; IPA", "https://ipa.co.uk/initiatives/effworks/effworks-ft-reports/eggs-in-two-baskets", "Opinión + estudio con límites"),
    ("F38", "Cupo 2027", "Disposición 451/2026: 50.000 unidades electrificadas sin arancel; entran desde enero de 2027.", "iProfesional", "https://www.iprofesional.com/negocios/468526-importacion-de-autos-electricos-el-gobierno-cambia-el-cupo-para-2027", "Prensa sobre norma"),
    ("F39", "Música en Instagram", "Las cuentas de empresa usan la Sound Collection de Meta (libre de regalías, también para anuncios).", "Instagram Help", "https://help.instagram.com/ipad-app/402084904469945", "Oficial (no leído completo)"),
]

# ---------------------------------------------------------------- público
PUBLICO = [
    ("Todos (las masas)", "Cualquier cordobés que mira reels, de cualquier edad. Hoy no está por comprar, pero mira, comparte y se acuerda de nosotros cuando cambie el auto.",
     "Entretenerse y aprender algo en pocos segundos.", "Que parezca una publicidad.", "—",
     "Adiviná, ¿Entra todo?, Ida y vuelta medida, la obra, la inauguración, Un día en Valparaiso, los más vendidos del mes",
     "Reels de Instagram y TikTok", "Las vistas sin paso comercial no traen leads (reel de 150 mil vistas, 0 leads). Estas piezas se miden por envíos y por chats con código."),
    ("Muchos km por día", "Trabaja con el auto o viaja todos los días: al centro, a Carlos Paz, a Villa Allende, a Río Segundo. Visitadores, vendedores, profesionales.",
     "Gastar menos nafta sin cambiar su rutina.", "'¿Dónde lo cargo?' y '¿cuánto dura la batería?'.",
     "Eado Plus (se enchufa); ORA 05 HEV y H6 PRO HEV (se cargan solos)",
     "Llegó al salón, ¿Enchufe o nafta?, Ida y vuelta medida, ¿Cuánto dura la batería?, YouTube",
     "Instagram, YouTube, Google", "Córdoba depende del auto y tiene distancias largas (iProfesional, 2026). Con los que se enchufan y los que se cargan solos, la duda de dónde cargar casi desaparece."),
    ("Familia", "Padres con chicos: vacaciones en las sierras, el cole, los fines de semana.",
     "Espacio, seguridad y que entre todo.", "La cuota y cuánto pagan en total.", "Haval H6, Haval H7, Deepal S05, Outlander",
     "¿Entra todo?, Auto para la familia, Lluvia, Antes de salir a la ruta, carrusel de las sierras",
     "Instagram, Facebook, WhatsApp", "Inferencia por las fechas (vacaciones de enero, vuelta a clases) y el pronóstico de un verano lluvioso (SMN)."),
    ("Cambia su usado", "Tiene un auto de hace 5 a 10 años y quiere uno nuevo. Es el comprador típico: el 51 % de los que compran un 0 km tiene 50 años o más (SIOMAA, 2025); en los autos chinos, 52 años en promedio, ~40 % mujeres y casi todos particulares.",
     "Saber cuánto le toman su auto y cuánto queda la cuota.", "No entiende la financiación, le da miedo que la cuota suba, desconfía de los gastos que aparecen al final y duda del 'auto chino'.",
     "Todos", "¿Comprás ahora o en enero?, Aguinaldo, serie 'Cómo se compra' (3 preguntas, cuánto pagás además del auto, carruseles de créditos y de la cotización), ¿Auto chino?, placas de cuota",
     "Facebook, Instagram, WhatsApp, Mercado Libre", "SIOMAA 2025 (edades: más de 60 años 28,9 %, de 40 a 49 26 %, de 50 a 59 22 %, de 18 a 24 solo 1 %). Ámbito (autos chinos). Córdoba transfirió 81.699 usados en el primer semestre de 2026, más que la Ciudad de Buenos Aires (iProfesional)."),
    ("Campo y pyme", "Productor, contratista o empresa con camionetas.",
     "Una 4x4 que aguante, que cargue y que tenga enchufe para herramientas; factura.", "Repuestos y service lejos del campo.",
     "Haval H7 4x4, Poer, L200", "Para el campo, YouTube del H7, previa de Expoagro",
     "Facebook, WhatsApp, Google, Expoagro", "Solo ~1 de cada 10 autos chinos se patenta a nombre de una empresa (Ámbito): hay menos competencia. Grupo Antelo apunta al agro (Expoagro 2026)."),
    ("Curioso del eléctrico", "Vive en la ciudad y tiene cochera con enchufe.",
     "No cargar nafta nunca; la tecnología.", "Cuántos km hace y dónde cargar en la ruta.", "ORA 03",
     "¿Enchufe o nafta?, carrusel de las sierras, YouTube del ORA 03, Adiviná (el café)",
     "Instagram, TikTok, YouTube", "~70 % de los cargadores públicos del país está en el AMBA (El Economista, 2026): en Córdoba conviene hablarle al que carga en su casa."),
    ("Los que ya nos siguen", "Siguen la cuenta, tienen el número guardado o ya escribieron.",
     "Ver qué hay hoy, el precio y la cuota.", "Que no le contesten rápido.", "Todos",
     "Historias, Estados de WhatsApp, vivos, entregas, placas de cuota",
     "Historias, WhatsApp, Google, Mercado Libre", "Las historias no traen gente nueva: sirven para cerrar con los que ya siguen (Mosseri)."),
]
PUBLICO_NOTAS = [
    "Quién decide la compra: un adulto. El 51 % de los compradores de 0 km tiene 50 años o más y el grupo más grande es el de más de 60 (SIOMAA, 2025). En los autos chinos, 52 años en promedio y ~40 % mujeres (Ámbito). El tono es profesional y los argumentos son concretos: cuánto gasta, cuánto pagás en total, la garantía y la seguridad.",
    "Por qué se escribe para alguien de 15 años: si lo entiende un chico de 15 mirando sin sonido, lo entiende cualquiera, también el de 60 que mira apurado. No es hablarles a los chicos: es que a nadie le cueste entender. Nielsen Norman Group recomienda escribir para el público general al nivel de 11 a 14 años, y en la Argentina solo el 22 % sabe calcular un interés simple y el 41 % escuchó hablar del crédito prendario (BCRA–CAF): por eso las cuentas se muestran ya hechas y las palabras difíciles se explican.",
    "Cada pieza del Calendario dice a qué público le habla (columna 'Para quién'). A las 6–8 semanas, mirar qué público trae más chats con código y darle más piezas.",
]

# ---------------------------------------------------------------- cómo escribir
ESCRIBIR_INTRO = ("Todo lo que se publica (guiones, textos en pantalla, descripciones, placas y mensajes) se escribe para que lo entienda "
                  "alguien de 15 años en la primera mirada. No cambia a quién le vendemos: cambia cómo lo decimos. El tono sigue siendo profesional.")
PRUEBA_15_TITULO = "La prueba de los 15 años (antes de grabar y antes de publicar)"
PRUEBA_15 = [
    "1. Una sola idea por pieza. Si no la podés decir en una frase (columna 'La idea en una frase' de Guiones), el video no está listo.",
    "2. Frases cortas: hasta 12 palabras cada una, y una idea por frase.",
    "3. Palabras de todos los días. Si un chico de 15 no la usaría, cambiala (diccionario de abajo). Las siglas, solo en letra chica.",
    "4. Todo lo que se dice, se ve. Si decís 'baúl', se ve el baúl abriéndose. Si decís un número, el número aparece grande.",
    "5. Números redondos y comparados con algo conocido: un café, el celular, un tanque de nafta, ida y vuelta a Carlos Paz.",
    "6. Se entiende sin sonido: el gancho escrito desde el primer cuadro y subtítulos en todo.",
    "7. Lo difícil, con una imagen: el CFT es la barra del total; el crédito UVA es la cuota que sube; el híbrido son dos motores que empujan juntos.",
    "8. La prueba final: mostrale el video a alguien que no sabe de autos. Si te repite la idea en una frase, está listo. Si no, se simplifica.",
    "9. Lo que no cambia: el tono profesional, los datos con su fuente, el único CTA comercial y la letra chica legal.",
]
DICCIONARIO_TITULO = "Diccionario: palabras difíciles y cómo decirlas"
DICCIONARIO = [
    ("PHEV, híbrido enchufable", "Híbrido que se enchufa (se enchufa y también usa nafta)", "PHEV"),
    ("HEV, híbrido autorrecargable", "Híbrido que se carga solo (nunca se enchufa)", "HEV"),
    ("EV, BEV", "Eléctrico", "100 % eléctrico"),
    ("Autonomía", "Cuántos km hace", "Autonomía declarada (NEDC o WLTP)"),
    ("Ciclo NEDC o WLTP", "No se dice", "Medido en laboratorio (NEDC o WLTP)"),
    ("CFT, costo financiero total", "Lo que pagás en total, con todo incluido", "CFTEA [..] %"),
    ("TNA", "El interés por año (solo si hace falta)", "TNA [..] %"),
    ("Anticipo", "Lo que ponés al principio", ""),
    ("Crédito prendario", "Crédito con el auto de garantía", "Prendario"),
    ("Crédito UVA", "Crédito que sube con la inflación", "UVA"),
    ("Adjudicación", "Cuando te dan el auto (en el plan de ahorro)", "Derecho de adjudicación"),
    ("Tasación del usado", "Cuánto te tomamos tu auto", ""),
    ("Posventa", "El service y el taller", ""),
    ("ADAS, asistencias a la conducción", "Ayudas que te avisan y frenan solas", "ADAS"),
    ("Equipamiento, prestaciones", "Lo que trae", ""),
    ("Bonificación", "Descuento", ""),
    ("Patentar en enero", "Que el auto figure del año nuevo", "Año de patentamiento"),
    ("Vigencia", "Hasta cuándo vale", "Vigente del [..] al [..]"),
    ("Torque, Nm", "Tiene fuerza / arranca rápido (con un dato simple, como el 0 a 100)", "Nm según la ficha"),
    ("Unidad", "Auto", ""),
    ("Entrega inmediata", "Está acá: te lo llevás [plazo real] (solo si es cierto ese día)", "Sujeto a stock"),
]
RITMO_TITULO = "Ritmo y visuales: cómo hacerlo dinámico"
RITMO = [
    ("El primer cuadro con todo", "El primer cuadro ya muestra lo más fuerte y el gancho escrito. Nada de logo ni fundido desde negro.", "La mitad mira sin sonido (Mosseri) y el primer cuadro es también la portada."),
    ("Cambio de imagen cada 1–2 segundos, sobre la misma idea", "Corte, otro ángulo o un zoom del 110 % en la palabra clave, pero mostrando lo mismo de lo que se habla. El vendedor nunca más de 3 segundos quieto hablando: se intercala lo que dice.", "Los cortes que no tienen relación entre sí saturan, y con mucho ritmo se recuerda peor lo que se dice que lo que se ve (Lang, 1999): por eso cada corte muestra lo que se está diciendo."),
    ("El auto desde el primer cuadro, varias veces", "El auto se ve desde el primer segundo y vuelve a aparecer varias veces. El nombre puede ir tarde (regla del dueño).", "En los anuncios con más intención de compra, mostrar el producto más de una vez y decir beneficios concretos pesa mucho (Meta y Toluna, 2025). Vale probar con reels de prueba una versión con el nombre en los primeros 5 segundos."),
    ("Texto en pantalla corto", "En pantalla va la palabra o el número clave, no la frase entera. Los subtítulos van de 1 a 4 palabras.", "Repetir en pantalla toda la frase que se dice no ayuda a entender; el texto corto sí (Mayer, 2023)."),
    ("Las cuentas, ya hechas", "Cuando hay números, la cuenta aparece armada en pantalla: no se le pide al que mira que la haga.", "Solo el 22 % de los argentinos sabe calcular un interés simple (BCRA–CAF)."),
    ("Algo que aparece cada 0,3 segundos", "Subtítulos palabra por palabra, flechas, círculos que se dibujan, números que cuentan.", "Regla de la casa (CLAUDE.md)."),
    ("Mostrar, no solo decir", "Cada frase tiene su imagen, al mismo tiempo que se dice: un objeto real (valija, café, enchufe, cinta métrica, almanaque, sobre) o un gráfico simple (barra, balanza, mapa plano).", "Palabras con imágenes se entienden mucho mejor que palabras solas, sobre todo si aparecen al mismo tiempo (Mayer, 2023)."),
    ("Cámara que se mueve", "Caminar hacia el auto, abrir la puerta, entrar, ver desde el asiento. Celular en estabilizador.", "Ninguna escena sin movimiento (regla de la casa)."),
    ("Comparar en pantalla partida", "Eléctrico contra híbrido, antes y después, dos vendedores.", "La diferencia se ve de un vistazo."),
    ("Promesa al principio, respuesta al final", "'Al final te digo…' en los primeros 3 a 5 segundos, y el final lo cumple.", "TikTok pide presentar la propuesta en los primeros 3 segundos y el gancho en los primeros 6; retiene hasta el final (fórmula de retención)."),
    ("Hablale al que mira, de vos", "'Si llevás chicos…', 'tu auto', 'te muestro'. Una persona real a cámara.", "El estilo de conversación ayuda a entender (Mayer, 2023), y TikTok recomienda mostrar personas."),
    ("Re-gancho cada 5–8 segundos", "'Pero…', 'Entonces…', 'Y lo más importante…'.", "Cada parte abre la siguiente."),
    ("Sonido que acompaña", "Whoosh en los cortes grandes, pop cuando entra un número, impacto en la respuesta. Música baja, nunca en silencio.", "Marca el ritmo sin tapar la voz."),
    ("Final que vuelve al principio", "El último cuadro engancha con el primero.", "El video se vuelve a ver (loop)."),
    ("Corto y completo", "Reels de 20 a 45 segundos, nunca más de 90. Si algo no explica nada, se corta.", "Mejor corto y completo que largo y lento. En 2024 Instagram dijo que no recomienda reels de más de 90 s a quienes no siguen la cuenta (verificar si sigue)."),
    ("La palabra clave es para pedir precio", "Siempre 'Si querés precio y cuota, comentá EADO'. En los videos de Entretener, la palabra va en la descripción y el comentario fijado, no en la voz. Nunca 'comentá SÍ' o 'comentá un emoji'.", "Instagram no recomienda publicaciones que piden comentar una palabra para ganar alcance, pero aclaró que usarlo para generar contactos no es trampa (2024)."),
]

FUENTES += [
    ("F40", "Quién compra (edad)", "Ene.–sept. 2025: el 51 % de los compradores de 0 km tiene 50 años o más; más de 60, 28,9 %; de 18 a 24, 1 %.", "SIOMAA, vía Autoweb e Infonegocios", "https://www.autoweb.com.ar/2025/10/23/los-mayores-de-60-anos-son-los-que-mas-autos-0km-compran-en-argentina/", "Dato del sector"),
    ("F41", "Palabras + imágenes", "Experimentos de aprendizaje: palabras con imágenes (efecto 1,35), al mismo tiempo (1,31), estilo de conversación (1,00), sacar lo que sobra (0,86). Repetir en pantalla toda la frase dicha no ayuda.", "Mayer, APA, 2023", "https://www.unh.edu/teaching-learning-resource-hub/sites/default/files/media/2023-06/itow-research-based-principles-for-designing-multimedia-instruction-mayer.pdf", "Revisión de experimentos"),
    ("F42", "Lenguaje simple", "Para el público general, escribir al nivel de 11 a 14 años (6.º a 8.º grado de EE. UU.).", "Nielsen Norman Group, 2017", "https://www.nngroup.com/articles/plain-language-experts/", "Guía de especialistas"),
    ("F43", "Ritmo de cortes", "Los cortes sin relación saturan (10 o más en 30 s); con más ritmo se recuerda peor lo dicho que lo visto.", "Lang y otros, 1999 (fuente secundaria)", "", "Estudio académico viejo"),
    ("F44", "Primeros segundos", "Presentar la propuesta en los primeros 3 s y el gancho en los primeros 6 s; mostrar personas; texto en pantalla.", "TikTok Ads Help, 2025", "https://ads.tiktok.com/help/article/creative-best-practices?lang=en", "Guía de la plataforma"),
    ("F45", "Qué tienen los anuncios con más intención de compra", "Beneficios concretos (×5,3), marca en pantalla poco tiempo (×4,8), producto más de una vez (×2,7), marca y mensaje en los primeros 5 s (×1,7).", "Meta y Toluna, vía Social Media Today (02/12/2025)", "https://www.socialmediatoday.com/news/meta-shares-reels-tips-for-marketers/806808/", "Dato de la plataforma, sin muestra publicada"),
    ("F46", "Qué entienden los argentinos de finanzas", "91 % entiende la inflación; solo 22 % calcula un interés simple; 41 % escuchó hablar del crédito prendario.", "BCRA–CAF, 2017", "https://www.bcra.gob.ar/en/survey-on-the-measurement-of-financial-capabilities", "Encuesta oficial (vieja)"),
]

GLOSARIO = [
    ("Lead", "Una persona que escribió y dejó sus datos porque le interesa un auto."),
    ("Lead calificado", "Un lead que dijo qué auto quiere, cómo lo piensa pagar y para cuándo (letra A o B)."),
    ("CTA", "El pedido que cierra cada pieza. Hay uno solo: 'Pedinos precio y financiación de cualquiera de nuestros autos'."),
    ("Código", "Una palabra (EADO, CUOTA, RUTA…) que viaja en el mensaje de WhatsApp para saber qué pieza trajo la consulta."),
    ("Gancho", "Lo que se dice y se ve en los primeros 2 segundos para que la persona no pase de largo."),
    ("Re-gancho", "Una frase en el medio ('pero…', 'y lo más importante…') que da una razón nueva para seguir mirando."),
    ("Tomas de apoyo", "Imágenes de lo que se está diciendo (el baúl, la pantalla, el enchufe) que se intercalan con el vendedor."),
    ("Video final", "El video ya editado, sin marca de agua, que se sube igual a Instagram, TikTok, YouTube y Facebook."),
    ("Reel de prueba", "Un reel que Instagram muestra primero solo a gente que no nos sigue, para elegir el mejor gancho."),
    ("Tasa de salto", "El porcentaje de gente que pasa de largo un reel en los primeros 3 segundos. Cuanto más baja, mejor el gancho."),
    ("Loop", "Cuando el último cuadro engancha con el primero y el video se vuelve a ver solo."),
    ("Retargeting", "Mostrarle un anuncio a quien ya vio nuestros videos (por ejemplo, la cuota del auto que miró)."),
    ("Día D", "El día abierto de la inauguración. Todas las fechas de la inauguración se cuentan desde ahí (D-7 = 7 días antes)."),
    ("Entretener / Educar / Vender", "Para qué es cada pieza: atraer a mucha gente, explicarle al que está pensando en cambiar el auto, o cerrar con el que ya quiere precio."),
]

FUENTES += [
    ("F47", "Palabra clave y largo de los reels", "Instagram no recomienda publicaciones que piden comentar una palabra, número o emoji para ganar alcance; usar comentarios y mensajes para generar contactos 'no se considera cebo'. Tampoco recomienda reels de más de 90 s a no seguidores.", "Social Media Today, 05/06/2024", "https://www.socialmediatoday.com/news/instagram-clarifies-advice-single-word-ctas-longer-reels/718151/", "Declaración de la plataforma (2024, verificar)"),
    ("F48", "Vistas que no son compradores", "Foro de gerentes de concesionarias: 'la mayoría de esas vistas no está buscando comprar'; lo que funciona es lo pago y local, y atender rápido.", "DealerRefresh (EE. UU., 2023)", "https://forum.dealerrefresh.com/threads/any-dealers-using-tiktok-for-marketing-campaigns.7890/page-3", "Opiniones de un foro del rubro"),
    ("F49", "Explicar cómo se compra", "Una vendedora con ~480 mil seguidores mezcla entretenimiento con explicaciones del proceso de compra, los gastos y qué se negocia; le llegan compradores de otros estados (sin totales).", "CBT News, 19/11/2026", "https://cbtnews.com/used-car-week-2026-andrea-anderson", "Caso autorreportado"),
    ("F50", "Gastos además del precio", "Hay reclamos y un fallo judicial en la Argentina por flete, preentrega y patentamiento cobrados de más.", "Examedia; Unión de Consumidores (la nota ya no está online)", "https://examedia.com.ar/portada/post/88108648", "Prensa (sin fecha visible)"),
]

