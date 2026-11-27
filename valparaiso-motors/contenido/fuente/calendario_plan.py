"""Qué pasa cada día del calendario final (27/11/2026 al 28/02/2027).

Una sola fuente para la hoja única 'Calendario' y su versión para leer (PDF).
- PUBLICA: qué sale cada día (con el guion del banco y lo que cambia ese día).
- GRABA: qué se filma o se arma y cuándo.
- TAREAS: inauguración, anuncios, puesta a punto y revisiones.
- CONTEXTO: lo que pasa en Córdoba ese día.
La inauguración está puesta el sábado 19/12 (noche VIP el viernes 18/12), como en la investigación
(inauguracion-y-mudanza.md): antes de las fiestas y con el aguinaldo cobrado.
"""
import datetime as dt

from guiones_comun import CTA, FIN_ENT, LEGAL, KM, FAM, TODOS, ELEC, v

d = dt.date
INICIO = d(2026, 11, 27)
FIN = d(2027, 2, 28)
DIA_D = d(2026, 12, 19)
VIP = d(2026, 12, 18)

FERIADOS = {d(2026, 12, 7): "Día no laborable (lo decide cada empleador)", d(2026, 12, 8): "Feriado: Inmaculada Concepción",
            d(2026, 12, 25): "Feriado: Navidad", d(2027, 1, 1): "Feriado: Año Nuevo",
            d(2027, 2, 8): "Feriado: Carnaval", d(2027, 2, 9): "Feriado: Carnaval"}
MEDIO_DIA = {d(2026, 12, 24): "Nochebuena: se trabaja medio día", d(2026, 12, 31): "Fin de año: se trabaja medio día"}

REEL = "Reel (Instagram + Facebook + TikTok + YouTube Shorts, el mismo video sin marca de agua)"
CARRUSEL = "Carrusel (Instagram + Facebook)"

# ---------------------------------------------------------------- piezas que no están en el banco
CAR1 = v("CAR1", "¿Cuál se enchufa y cuál no? Los autos del salón", "Educar", TODOS, "Carrusel de clasificar",
         "Siete autos del salón en tres grupos: los que se enchufan, los que nunca se enchufan y los que solo se enchufan.",
         "Carrusel 1080x1350 · 10 placas", "Sin personas (fotos propias del salón)",
         "¿CUÁL SE ENCHUFA? 7 AUTOS, 3 RESPUESTAS", "",
         [("Placa 1", "", "Los 7 autos en fila en el salón, foto propia, fondo limpio.", "¿CUÁL SE ENCHUFA? 7 AUTOS, 3 RESPUESTAS · deslizá →", ""),
          ("Placa 2", "", "Ícono de enchufe grande en bordó.", "SE ENCHUFAN (HÍBRIDOS ENCHUFABLES): EL DÍA A DÍA EN ELÉCTRICO Y, SI SE ACABA LA BATERÍA, SIGUEN A NAFTA", ""),
          ("Placa 3", "", "Eado Plus recortado de foto propia.", "CHANGAN EADO PLUS · HASTA 132 KM SIN NAFTA* · *según la marca, ciclo NEDC (de laboratorio)", ""),
          ("Placa 4", "", "CS55 Plus y Deepal S05 juntos.", "CHANGAN CS55 PLUS · DEEPAL S05 · SE CARGAN EN TU CASA · S05: 100 KM O MÁS* (LEV2, según la marca)", ""),
          ("Placa 5", "", "Ícono de enchufe tachado.", "NUNCA SE ENCHUFAN (HÍBRIDOS): SE CARGAN SOLOS AL FRENAR · GWM ORA 05 · HAVAL H6 PRO HEV · HAVAL JOLION HEV", ""),
          ("Placa 6", "", "H6 en la ciudad.", "DATO: LA H6 GASTA 4,3 L CADA 100 KM EN CIUDAD Y 5,8 EN RUTA* · *según la marca", ""),
          ("Placa 7", "", "Ícono de rayo.", "SOLO SE ENCHUFAN (ELÉCTRICOS): CERO NAFTA · GWM ORA 03 · JMEV EASY 3 · LOS DOS HICIERON ~285 KM EN PRUEBAS DE LA PRENSA", ""),
          ("Placa 8", "", "Tres íconos: cochera, ciudad, ruta.", "¿CUÁL TE CONVIENE? COCHERA + CIUDAD → ENCHUFABLE O ELÉCTRICO · SIN COCHERA → HÍBRIDO", ""),
          ("Placa 9", "", "Fondo bordó, letras blancas.", "LO HONESTO: SI NO TENÉS DÓNDE CARGARLO, UN ENCHUFABLE NO TE CONVIENE", ""),
          ("Placa 10", "", "Logo chico, fondo papel.", "PEDINOS PRECIO Y FINANCIACIÓN · COMENTÁ TIPO", "")],
         "Fotos propias de los 7 autos (mismo encuadre de 3/4 de frente, fondo limpio, sin patentes) · íconos simples.",
         "¿Cuál se enchufa y cuál no? Se enchufan (híbridos enchufables): Changan Eado Plus, CS55 Plus y Deepal S05. Nunca se enchufan (híbridos): GWM ORA 05, Haval H6 PRO HEV y Jolion HEV. Solo se enchufan (eléctricos): GWM ORA 03 y JMEV Easy 3. Datos según las marcas y pruebas de Parabrisas. Guardalo para cuando cambies el auto. Si querés precio y cuota, comentá TIPO. Córdoba.",
         "#hibrido #autoelectrico #hibridoenchufable #autos #AutosCordoba", "TIPO",
         ojo="Usar solo los autos que estén en stock y ajustar las placas. Fotos propias, nunca generadas.",
         dificultad="Fácil", por_que="Contesta la confusión número uno del comprador ('¿cuál se enchufa?') y se guarda: los carruseles de referencia son los que más se guardan.",
         honesto="Si no tenés dónde cargarlo, un enchufable no te conviene.", fuentes="EADO-1, DEEPAL-3, H6-1, ORA03-2, JMEV-2, GEN-2")

CAR2 = v("CAR2", "Precios de enero: un modelo por placa", "Vender", f"{KM}; {FAM}", "Carrusel de precios con legal",
         "El precio y una cuota de ejemplo de cada modelo en stock, con el dato que lo hace distinto y el legal en cada placa.",
         "Carrusel 1080x1350 · 8–10 placas", "Sin personas (fotos propias)",
         "¿CUÁNTO SALE CADA UNO EN ENERO?", "",
         [("Placa 1", "", "4 autos del salón recortados, fondo papel.", "¿CUÁNTO SALE CADA UNO EN ENERO? · deslizá →", ""),
          ("Placa 2", "", "JMEV Easy 3, foto propia.", "JMEV EASY 3 · 1 TANQUE = ~8 CARGAS* · CONTADO $[..] · SIN IMP. NAC. $[..] · CUOTA $[..] · CFTEA [..] %", ""),
          ("Placa 3", "", "Changan Eado Plus.", "CHANGAN EADO PLUS · SE ENCHUFA: HASTA 132 KM SIN NAFTA* · CONTADO $[..] · SIN IMP. NAC. $[..] · CUOTA $[..] · CFTEA [..] %", ""),
          ("Placa 4", "", "Haval Jolion HEV.", "HAVAL JOLION HEV · HÍBRIDO, ~800 KM POR TANQUE* · CONTADO $[..] · SIN IMP. NAC. $[..] · CUOTA $[..] · CFTEA [..] %", ""),
          ("Placa 5", "", "Changan CS55 Plus.", "CHANGAN CS55 PLUS · 21,7 KM/L SIN CARGARLA* · CONTADO $[..] · SIN IMP. NAC. $[..] · CUOTA $[..] · CFTEA [..] %", ""),
          ("Placa 6", "", "GWM ORA 03.", "GWM ORA 03 · ELÉCTRICO, ~285 KM REALES* · CONTADO $[..] · SIN IMP. NAC. $[..] · CUOTA $[..] · CFTEA [..] %", ""),
          ("Placa 7", "", "Haval H6 PRO HEV.", "HAVAL H6 PRO HEV · NUNCA SE ENCHUFA · 7 AÑOS DE GARANTÍA* · CONTADO $[..] · SIN IMP. NAC. $[..] · CUOTA $[..] · CFTEA [..] %", ""),
          ("Placa 8", "", "Texto chico.", "*Datos según la marca o pruebas de la prensa (ver descripción). Placa legal completa en cada modelo.", ""),
          ("Placa final", "", "Logo chico.", "PEDINOS PRECIO Y FINANCIACIÓN · COMENTÁ CUOTA", "")],
         "Fotos propias de cada modelo · números de Administración del día.",
         "¿Cuánto sale cada uno en enero? JMEV Easy 3 (un tanque de 40 L de súper = ~8 cargas de su batería en casa, estimado), Changan Eado Plus (hasta 132 km eléctricos, NEDC), Haval Jolion HEV (~800 km por tanque, Autotest), Changan CS55 Plus (21,7 km/l en ciudad sin cargarla, Parabrisas), GWM ORA 03 (~285 km reales, Parabrisas) y Haval H6 PRO HEV (7 años de garantía). Si querés la cuenta de tu modelo, comentá CUOTA. Córdoba. [Legal completo por modelo.]",
         "#precios #0km #financiacion #enero #AutosCordoba", "CUOTA",
         ojo="Todos los números los da Administración el 4/1 (listas de enero). Precio en pesos y precio sin impuestos nacionales en cada placa. Si ajusta por UVA o CER: nunca 'cuota fija' ni 'sin interés'. Sacar las placas de los modelos sin stock.",
         dificultad="Fácil", por_que="En el pico de enero, el que ya decidió busca precio: el carrusel se guarda, se comparte y alimenta el anuncio de retargeting.",
         honesto="Las cuotas de ejemplo dependen del anticipo y del día: el CFT de cada una está en la placa.", fuentes="C15V, EADO-1, JOLION-3, CS55-1, ORA03-2, H6-7")

RESPUESTA_1 = v("D19a", "Respuesta a @: '¿y cuánto dura la batería?'", "Educar", f"{ELEC}; {KM}", "Respuesta a un comentario real",
                "El vendedor contesta en video, con el comentario arriba, la duda que más aparece en los videos de autos que se enchufan: cuánto dura la batería. La respuesta está en la garantía.",
                "Reel o TikTok con la función 'responder con video'", "Vendedor 1",
                "El comentario real en pantalla (lo pone la función de responder)", "¿CUÁNTO DURA LA BATERÍA? ME LO PREGUNTARON ACÁ",
                [("0–2 s", "Me preguntaron cuánto dura la batería.", "La burbuja del comentario real arriba; el vendedor al lado de la tapa de carga.", "[COMENTARIO REAL]", "Pop"),
                 ("2–5 s", "Te lo muestro en un papel. Al final, lo que tenés que pedir.", "El vendedor levanta el papel de la garantía.", "AL FINAL: QUÉ PEDIR", "Pop"),
                 ("5–11 s", "No es como la del celular: está hecha para durar más, y tiene refrigeración propia.", "Un celular viejo al 40 % contra el dibujo de la batería del auto con líneas de frío.", "NO ES LA DEL CELULAR", "Pop"),
                 ("11–18 s", "Por eso la garantía de la batería es de 8 años o 150.000 kilómetros. Lo que pase primero.", "El papel de la garantía en primer plano; '8 AÑOS' se marca en bordó.", "BATERÍA: 8 AÑOS O 150.000 KM*", "Impacto"),
                 ("18–23 s", "Ocho años es más de lo que mucha gente se queda con un auto.", "Un almanaque que pasa 8 años de golpe.", "8 AÑOS", "Tic"),
                 ("23–28 s", "Lo honesto: la garantía tiene condiciones. Pedilas por escrito antes de comprar.", "El vendedor a cámara.", "PEDÍ LAS CONDICIONES POR ESCRITO", "Golpe"),
                 ("28–33 s", CTA + " Dejame tu pregunta y te contesto en el próximo.", "Logo chico.", "¿TU PREGUNTA? COMENTALA", "")],
                "Vendedor al lado del auto que se enchufa · papel de garantía real del modelo · celular viejo · el comentario real (lo muestra la función de responder).",
                "Nos preguntaron cuánto dura la batería. La respuesta está en la garantía: 8 años o 150.000 km en la batería del GWM ORA 03, del ORA 05 y del Deepal S05, y en el sistema híbrido del Changan Eado Plus (lo que ocurra primero, según cada marca). Pedí las condiciones por escrito. Mandáselo a quien tiene miedo de que la batería se gaste. Dejá tu pregunta y la contestamos en el próximo video. Córdoba.",
                "#bateria #autoelectrico #hibridoenchufable #garantia #AutosCordoba", "PREGUNTA",
                ojo="El 28/11 se exportan y clasifican los 142 comentarios del video EV/PHEV/HEV. Si la pregunta más repetida no es la de la batería, se responde esa con las mismas escenas y una de estas respuestas: '¿Y si no tengo cochera?' → 'Entonces no te compres uno que se enchufa: comprate el híbrido que nunca se enchufa' (D22); '¿Cuánto sale?' → precio del día con la placa legal 5 s; '¿Y en la ruta?' → la del video de la batería en la ruta (D29). Usar un comentario real, con las palabras de quien lo hizo.",
                dificultad="Fácil", por_que="Convierte la duda real de un video que ya funcionó en otro video, con contexto desde el cuadro 0 (en Perú, un 'Respuesta a @' sobre Changan pasó las 750.000 reproducciones).",
                honesto="La garantía de la batería tiene condiciones: pedilas por escrito.", fuentes="ORA03-4, ORA05-7, DEEPAL-4, EADO-12")

RESPUESTA_2 = v("D19b", "Respuesta a @: la duda del verano", "Educar", f"{KM}; {FAM}", "Respuesta a un comentario real",
                "La pregunta que más se repitió en los comentarios de enero y febrero, contestada en video por el vendedor.",
                "Reel o TikTok 25–40 s con la función 'responder con video'", "Vendedor 2",
                "El comentario real en pantalla", "ME PREGUNTARON ESTO",
                [("0–2 s", "[Lee el comentario tal cual.]", "La burbuja del comentario real arriba.", "[COMENTARIO]", "Pop"),
                 ("2–5 s", "Te lo muestro, no te lo cuento.", "Camina hacia la prueba (auto, taller, cargador o papel).", "TE LO MUESTRO", "Whoosh"),
                 ("5–22 s", "[Respuesta corta, con un dato con fuente y mostrando la prueba.]", "Un corte cada 2 s sobre lo que prueba la respuesta.", "[DATO + FUENTE CHICA]", "Pop en el dato"),
                 ("22–27 s", "[Lo que no sabemos o depende.]", "El vendedor a cámara.", "LO QUE DEPENDE", "Golpe"),
                 ("27–32 s", CTA + " Dejame tu pregunta y te contesto en el próximo.", "Logo chico.", "¿TU PREGUNTA? COMENTALA", "")],
                "Vendedor al lado de la prueba de la respuesta.",
                "Nos preguntaron: '[comentario]'. [Respuesta con su fuente.] Dejá tu pregunta y la contestamos en el próximo video. Córdoba.",
                "#preguntas #0km #autos #concesionaria #AutosCordoba", "PREGUNTA",
                ojo="Solo preguntas reales. Elegir la que más se repitió en la escucha de los lunes de enero y febrero. Si es de autonomía, usar el número medido el 6/1 (E25); si es de repuestos, los días que tardó el repuesto (D04); si es de precio, la placa legal 5 s.",
                dificultad="Fácil", por_que="Cada pregunta real repetida es un video que ya tiene público esperando la respuesta.",
                honesto="Si la respuesta es 'depende', se dice de qué depende.", fuentes="Comentarios reales de la cuenta")

EXTRA = {g["id"]: g for g in (CAR1, CAR2, RESPUESTA_1, RESPUESTA_2)}

# ---------------------------------------------------------------- lo que sale cada día
# (fecha, hora, formato, id del guion, {ajuste, gancho_b, historia, plan_b})
PRECIO_PRIMERO = "Formato 'te lo cuento': el precio del día en la primera frase. Probarlo como reel de prueba (Instagram lo muestra a no seguidores) contra el gancho A y quedarse con el de menos salto a los 3 s."
PUBLICA = [
    (d(2026, 11, 30), "12:30", CARRUSEL, "CAR1", dict(historia="Encuesta: '¿Tu próximo auto: se enchufa o no?' (Sí / No / No sé). A los que digan 'No sé', mandarles el carrusel por mensaje.")),
    (d(2026, 12, 1), "19:30", REEL, "D26", dict(historia="Quiz: '¿Qué tenés que pedir por escrito antes de la seña? Fecha de entrega / Precio final / Las dos' (la correcta: las dos).")),
    (d(2026, 12, 9), "19:30", REEL, "D28", dict(historia="Encuesta: '¿Que no tenga rueda de auxilio te cambia la decisión?' (Sí / No). Responder a cada 'Sí' por mensaje con lo que trae en su lugar.")),
    (d(2026, 12, 3), "19:30", REEL, "V01", dict(gancho_b="[PRECIO EN PESOS]: UN AUTO QUE SE ENCHUFA. ¿CUÁL ES?",
                                                 historia="Pregunta: '¿Cuántos km hacés por día? Te hago la cuenta de la nafta' → contestar a cada uno por mensaje con su cuenta (km × 22 × 8 ÷ 100 × precio de la nafta).")),
    (d(2026, 12, 5), "19:30", REEL, "E16", dict(historia="Caja de preguntas: '¿Dónde creés que queda el nuevo Valparaiso?' + cuenta regresiva al sábado 19/12.")),
    (d(2026, 12, 7), "19:30", REEL, "D01", dict(
                                                 historia="Encuesta: '¿Cambiás el auto ahora o en enero?'")),
    (d(2026, 12, 2), "19:30", REEL, "D06", dict(historia="Pregunta: '¿Cuántos km hacés por mes? Te digo cuánto gastarías de luz' → responder por mensaje con la cuenta (km × 16,7 ÷ 100 × precio del kWh).")),
    (d(2026, 12, 10), "19:30", REEL, "V12", dict(ajuste="Faltan 9 días. Si la fachada todavía no está lista, se graba el equipo con el cartel y la calle, nunca imágenes generadas.",
                                                  historia="Sticker de cuenta regresiva al sábado 19/12 + sticker de enlace 'Pedí tu turno de prueba' (código TURNO).")),
    (d(2026, 12, 12), "19:30", REEL, "E08", dict(historia="Pregunta: '¿Cuánto mide tu cochera?' → responder qué auto entra.")),
    (d(2026, 12, 14), "19:30", REEL, "E17", dict(ajuste="Faltan 5 días: cerrar con 'el sábado te lo mostramos'. Plan B si el salón no está listo el fin de semana: se publica una cuenta regresiva con el equipo y el cartel, y el acelerado de vacío a lleno se filma el 19 a la mañana y va dentro de 'Así fue' (21/12).", historia="Cuenta regresiva + historias del armado (con el equipo, sin clientes).")),
    (d(2026, 12, 16), "19:30", REEL, "V13", dict(ajuste="Faltan 3 días: decir el día y el horario reales.", historia="Sticker de enlace 'Turno de prueba para el sábado' (código TURNO). Mostrar cuántos turnos quedan, si es real.")),
    (d(2026, 12, 17), "19:30", REEL, "D18", dict(cambios=[("Te adelanto: solo, no. Pero al final te muestro con qué sí.", "Te adelanto: solo, no. Pero si lo cobrás esta semana, al final te muestro con qué sí.")],
                                                  historia="Encuesta: '¿El aguinaldo va a: vacaciones / auto / ahorro?' A los que digan 'auto', mensaje con un ejemplo de anticipo y cuota con CFT.")),
    (d(2026, 12, 21), "19:30", REEL, "E18", dict(historia="Las mejores fotos del día abierto (solo con autorización) + 'Gracias, Córdoba'.")),
    (d(2026, 12, 23), "19:30", REEL, "D23", dict(cambios=[("Antes de viajar: aprendé a usar el kit", "Antes de salir a la ruta: aprendé a usar el kit")],
                                                  historia="Encuesta: '¿Sabés si tu auto tiene rueda de auxilio o kit? Sí / No sé'. A los 'No sé': 'pasá y te lo mostramos'.")),
    (d(2026, 12, 24), "10:00", REEL, "E19", dict(historia="Horario de fiestas fijo en una historia destacada.")),
    (d(2026, 12, 26), "19:30", REEL, "E06", dict(historia="Pregunta: '¿A dónde te vas de vacaciones?' (sirve para el próximo 'Respuesta a @').")),
    (d(2026, 12, 28), "19:30", REEL, "D11", dict(historia="Quiz: '¿Cuánto más pagás por pasada en la cabina que con TelePEAJE? $500 / $1.068 / $2.000' (la correcta: $1.068).")),
    (d(2026, 12, 30), "19:30", REEL, "E27", dict(historia="Encuesta: '¿Cuánto creés que gastás cada 100 km?' (menos de $10.000 / entre 10 y 17 mil / más).")),
    (d(2027, 1, 2), "19:30", REEL, "D29", dict(cambios=[("¿Conocés a alguien con miedo a quedarse tirado? Mandáselo.", "¿Conocés a alguien que se va de vacaciones con miedo a quedarse tirado? Mandáselo.")],
                                                historia="Encuesta: '¿Te da miedo quedarte sin batería en la ruta?' (Sí / No).")),
    (d(2027, 1, 4), "19:30", REEL, "V11", dict(ajuste="Primera semana del pico de enero. PLAN B si el 28/12 no hay condición confirmada por escrito (sin placa legal de promo): gancho 'SI ESPERASTE A ENERO PARA CAMBIAR EL AUTO' · 'Esta semana, en el local nuevo: te tasamos tu auto en el día, por escrito y con fecha' · 'y lo manejás antes de decidir, con turno de 30 minutos' · 'Pedinos precio y financiación de cualquiera de nuestros autos. Comentá APERTURA.'", historia="Sticker de enlace con APERTURA + cuenta regresiva al último día de la promo.")),
    (d(2027, 1, 6), "19:30", REEL, "E09", dict(ajuste="El festival de Jesús María arranca mañana (del 7 al 17/1): por eso el cuadro 0 y la descripción dicen 'si vas al festival' (la voz del gancho no cambia). No usar el nombre ni el logo del festival como si fueran socios.",
             cambios=[("¿CUÁNTO GASTÁS?", "SI VAS AL FESTIVAL: ¿CUÁNTO GASTÁS?"), ("¿Cuánto gastás para ir a Jesús María y volver?", "Si vas al festival: ¿cuánto gastás para ir a Jesús María y volver?")],
                                                historia="Quiz: '¿Cuánto sale ir a Jesús María y volver a nafta? $8.000 / $19.400 / $30.000'.")),
    (d(2027, 1, 7), "19:30", REEL, "V14", dict(gancho_b="[PRECIO EN PESOS]: UNA SUV FAMILIAR QUE SE ENCHUFA. ¿CUÁL ES? TE LO CUENTO",
                                                historia="Caja de preguntas: '¿Qué querés saber de esta SUV?' → las respuestas van a 'Respuesta a @'.")),
    (d(2027, 1, 8), "12:30", CARRUSEL, "CAR2", dict(historia="Sticker de enlace 'Tu cuota por WhatsApp' (código CUOTA).")),
    (d(2027, 1, 16), "19:30", REEL, "E02", dict(ajuste="Usar el precio del ticket real del café del video y rehacer las tres cuentas con ese número.", historia="Quiz: '¿Cuántos km hace un eléctrico con lo que sale un café? 23 / 36 / 65' (la correcta: 65).")),
    (d(2027, 1, 11), "19:30", REEL, "D19a", dict(historia="Caja de preguntas: 'Preguntame lo que quieras del auto que se enchufa'.")),
    (d(2027, 1, 13), "19:30", REEL, "D02", dict(historia="Encuesta: '¿Enchufe o nafta?' y después, en otra historia, el veredicto del video.")),
    (d(2027, 1, 14), "19:30", REEL, "V15", dict(gancho_b="[PRECIO EN PESOS]: UN 0 KM ELÉCTRICO PARA LA CIUDAD. TE LO MUESTRO",
                                                 historia="Encuesta: '¿Lo usarías solo para la ciudad?' (Sí / No).")),
    (d(2027, 1, 9), "19:30", REEL, "E25", dict(historia="Quiz antes de verlo: '¿Cuántos km eléctricos creés que hizo?' (3 opciones alrededor del número real). Al otro día, la respuesta.")),
    (d(2027, 1, 18), "19:30", REEL, "D21", dict(ajuste="Actualizar el ejemplo de CFT con una financiación vigente ese día (la del 26/11 ya venció).",
                                                 historia="Quiz: 'Tasa 0 %: ¿el costo total puede pasar el 40 %? Sí / No' (la correcta: sí).")),
    (d(2027, 1, 27), "19:30", REEL, "D24", dict(historia="Encuesta: '¿Creías que el número del folleto era el real?'")),
    (d(2027, 1, 21), "19:30", REEL, "E10", dict(ajuste="El festival de Cosquín arranca el sábado 23 (hasta el 31/1): por eso el cuadro 0 y la descripción dicen 'si vas este finde' (la voz del gancho no cambia). Sin usar el nombre ni el logo del festival como si fueran socios.",
             cambios=[("¿SIN NAFTA A COSQUÍN?", "SI VAS ESTE FINDE: ¿SIN NAFTA A COSQUÍN?"), ("¿Se puede ir a Cosquín y volver sin gastar nafta?", "Si vas este finde: ¿se puede ir a Cosquín y volver sin gastar nafta?")],
                                                 historia="Cuenta regresiva al sábado 23/1 + 'en Cosquín hay un cargador público de la provincia'.")),
    (d(2027, 1, 23), "19:30", REEL, "V19", dict(gancho_b="[PRECIO EN PESOS]: 7 ASIENTOS, HECHA EN JAPÓN. TE LA MUESTRO",
                                                 historia="Pregunta: '¿Cuántos son en tu familia?' → a los de 5 o más, mensaje con la Outlander.")),
    (d(2027, 1, 25), "19:30", REEL, "D13", dict(historia="Caja de preguntas: '¿Qué te cobraron aparte la última vez que compraste un auto?'")),
    (d(2027, 1, 20), "19:30", REEL, "D22", dict(historia="Encuesta: '¿Tenés cochera con enchufe?' (Sí / No). Sirve para saber a quién ofrecerle enchufable y a quién híbrido.")),
    (d(2027, 1, 28), "19:30", REEL, "V16", dict(gancho_b="[PRECIO EN PESOS]: UNA SUV QUE SE ENCHUFA Y TIENE PUERTAS SIN MARCO",
                                                 historia="Encuesta: '¿Puertas sin marco: te gustan?' (Sí / No).")),
    (d(2027, 1, 30), "19:30", REEL, "E01", dict(historia="Quiz: '¿En cuántos segundos llega a 100 este híbrido? 12 / 10 / menos de 8'.")),
    (d(2027, 2, 1), "19:30", REEL, "E12", dict(
                                                historia="Encuesta: '¿Le entendió al cordobés?' (Sí / No) y la toma del pedido que falló.")),
    (d(2027, 2, 3), "19:30", REEL, "D03", dict(historia="Caja de preguntas: '¿Qué te preocupa de comprar un auto chino?' → las respuestas van a 'Respuesta a @'.")),
    (d(2027, 2, 4), "19:30", REEL, "V21", dict(ajuste="Usar la financiación en pesos vigente ese día.", historia="Pregunta: '¿Cuánto podés poner de anticipo?' → responder por mensaje con un ejemplo con CFT.")),
    (d(2027, 2, 6), "19:30", REEL, "E07", dict(cambios=[("¿ENTRA EL ASADO PARA 15?", "FINDE LARGO: ¿ENTRA EL ASADO PARA 15?"), ("¿Entra el asado del domingo para 15?", "Finde largo: ¿entra el asado del domingo para 15?")], historia="Pregunta: '¿Qué no puede faltar en tu asado?'")),
    (d(2027, 2, 10), "19:30", REEL, "D04", dict(historia="Quiz: '¿Cuántos días creés que tardó el repuesto? 3 / 10 / 30' (al otro día, la respuesta real).")),
    (d(2027, 2, 11), "19:30", REEL, "V02", dict(gancho_b="[PRECIO EN PESOS]: UNA SUV HÍBRIDA QUE NUNCA SE ENCHUFA. TE LO MUESTRO",
                                                 historia="Encuesta: '¿Manejás más en ciudad o en ruta?'")),
    (d(2027, 2, 13), "19:30", REEL, "E03", dict(historia="Quiz: '¿Qué había debajo del auto?' (piedra / juguete / nada).")),
    (d(2027, 2, 15), "19:30", REEL, "D19b", dict(historia="Caja de preguntas nueva para el próximo 'Respuesta a @'.")),
    (d(2027, 2, 17), "19:30", REEL, "D05", dict(historia="Encuesta: '¿Tu casa es monofásica o trifásica?' (Mono / Tri / No sé). A los 'No sé': 'mirá tu factura o preguntale a un electricista'.")),
    (d(2027, 2, 18), "19:30", REEL, "V06", dict(gancho_b="[PRECIO EN PESOS]: 5 ESTRELLAS Y MÁS DE UNA TONELADA EN LA CAJA",
                                                 ajuste="Falta menos de un mes para Expoagro (9 al 12/3): si van, decirlo al final.",
                                                 historia="Pregunta: '¿Qué cargás en la chata?'")),
    (d(2027, 2, 20), "19:30", REEL, "E28", dict(plan_b="E15", ajuste="Si no se cerró la colaboración con el creador, sale el plan B (E15, 'Primera vez en un eléctrico').",
                                                 historia="Compartir la publicación en colaboración (o el plan B) con una encuesta: '¿Lo probarías?'")),
    (d(2027, 2, 22), "19:30", REEL, "V17", dict(gancho_b="[PRECIO EN PESOS]: ¿A BUENOS AIRES CON UN SOLO TANQUE? TE LO MUESTRO",
                                                 historia="Encuesta: '¿Ciudad o ruta?'")),
    (d(2027, 2, 24), "19:30", REEL, "D27", dict(historia="Encuesta: '¿Te frena pensar que la marca se puede ir?' (Sí / No).")),
    (d(2027, 2, 25), "19:30", REEL, "V08", dict(historia="Pregunta: '¿Cuántos autos tiene tu empresa?' → mensaje con la cuenta de su flota.")),
    (d(2027, 2, 27), "19:30", REEL, "E23", dict(ajuste="Cierra los tres meses: antes de publicar, armar en el perfil la historia destacada 'Mitos' con los videos de la batería (2/1), el folleto (27/1) y la trifásica (17/2).",
             cambios=[("¿Cuántas acertaste? Mandáselo", "¿Cuántas acertaste? Cada mito tiene su video en el perfil. Mandáselo"), ("¿Cuántas acertaste? Córdoba.", "¿Cuántas acertaste? Cada mito tiene su video en el perfil. Córdoba.")], historia="Quiz con uno de los mitos del video y link a los videos destacados.")),
]

PUBLICA.sort(key=lambda x: x[0])

# ---------------------------------------------------------------- qué se graba o se arma (fecha → [(id, nota)])
GRABA = {
    d(2026, 11, 28): [("CAR1", "Armado de las 10 placas en Canva, con las fotos de la mañana.")],
    d(2026, 11, 30): [("D26", ""), ("D06", "Pedir una factura de EPEC de muestra (sin datos personales)."), ("V01", "Además, 10 min de mapa: el recorrido Mendiolaza → centro para la animación.")],
    d(2026, 12, 1): [("D01", ""), ("D28", ""), ("E08", "Cochera real medida con cinta, con los tres autos (o los de largo conocido).")],
    d(2026, 12, 2): [("E16", "20 minutos en la obra: tomas con pistas reales, sin mostrar la dirección.")],
    d(2026, 12, 9): [("V12", "Fachada, salón y taller del local nuevo, de día."), ("V13", ""), ("D18", "")],
    d(2026, 12, 10): [("D23", "Abrir el baúl de cada auto del salón y anotar qué trae para un pinchazo."), ("E06", "")],
    d(2026, 12, 12): [("E17", "Cámara fija en trípode durante el armado del salón (sábado y domingo): de vacío a lleno.")],
    d(2026, 12, 18): [("E18", "Noche VIP: la llegada, las palabras, el corte de cinta y el recorrido (solo personas con autorización firmada).")],
    d(2026, 12, 19): [("E19", "A las 8:15, antes del brief: un plano de 1 s por persona del equipo, mismo encuadre, y un plano grupal."),
                      ("E18", "Día abierto: la apertura, las pruebas de manejo y la actividad de los chicos, un clip por hora (solo personas con autorización; chicos con firma de los padres).")],
    d(2026, 12, 22): [("D11", ""), ("E27", ""), ("D29", "El dueño graba la voz en ElevenLabs con el guion de 'Qué se dice' (sin números de línea). Se anima entre el 23 y el 30/12 con Claude Code y HyperFrames, en el estilo del explicador EV/PHEV/HEV.")],
    d(2026, 12, 29): [("V11", "Solo con la promo confirmada por escrito (28/12)."), ("V14", ""), ("E02", "Comprar el café antes y guardar el ticket: el precio del ticket manda."), ("D02", "")],
    d(2027, 1, 4): [("E09", "Viaje medido a Jesús María por la mañana: tablero en 0 al salir y foto del tablero al llegar, mismo encuadre.")],
    d(2027, 1, 5): [("V15", ""), ("D21", "Pedir a Administración una financiación con 'tasa 0' vigente y su CFT."), ("V19", "")],
    d(2027, 1, 7): [("CAR2", "Con las listas de precios de enero que confirma Administración.")],
    d(2027, 1, 6): [("E25", "Todo el día: Eado cargado al 100 % la noche anterior, recorrido mixto definido antes, foto del tablero cada 20 km y el momento exacto en que prende la nafta. Anotar temperatura y uso del aire.")],
    d(2027, 1, 11): [("D19a", "Se graba el mismo día, en una toma.")],
    d(2027, 1, 12): [("D24", ""), ("D13", "Administración arma el ticket real de un auto con todos los costos del día."), ("D22", "")],
    d(2027, 1, 19): [("E10", "Viaje a Cosquín con el Eado cargado al 100 % la noche anterior."), ("V16", ""), ("E01", "")],
    d(2027, 1, 26): [("D03", ""), ("V21", ""), ("E12", "Vendedor con tonada al volante del Eado; grabar 8 pedidos y usar los 4 mejores, incluido uno que falle.")],
    d(2027, 1, 27): [("D04", "Pedir el repuesto hoy y filmar 5 s del taller cada día hasta que llegue.")],
    d(2027, 2, 2): [("V02", ""), ("E03", ""), ("E07", "Los dos vendedores, la L200 y las cosas reales de un asado para 15 (sin fuego ni comida en el salón)."), ("D04", "Si ya llegó el repuesto: la caja que se abre y la etiqueta con la fecha.")],
    d(2027, 2, 10): [("D05", "Con un electricista matriculado (matrícula a la vista) en una cochera real."), ("V17", ""), ("E15", "Plan B de la colaboración del 20/2.")],
    d(2027, 2, 11): [("V06", "Salida aparte, por la mañana: un campo o corralón con permiso (no entra en el bloque del salón).")],
    d(2027, 2, 15): [("D19b", "Se graba el mismo día, en una toma.")],
    d(2027, 2, 16): [("D27", ""), ("V08", ""), ("E23", "Vendedor 2 con los carteles VERDADERO y FALSO; cortes cortos de los videos anteriores de cada mito.")],
    d(2027, 2, 23): [("—", "Grabación de banco para marzo (4 piezas, en el salón y el estacionamiento): D25 'En la ciudad gasta poquito' (se reusan las tomas de la H6 en el centro y en ruta grabadas el 2/2), V03 ORA 05, V04 ORA 03 y E13 'La prueba del silencio'. D10 'La prueba de la tierra' necesita un camino de tierra: va en una salida aparte en marzo.")],
}

# ---------------------------------------------------------------- tareas por día (fecha → [(responsable, tarea)])
T = {}


def tarea(fecha, resp, texto):
    T.setdefault(fecha, []).append((resp, texto))


# Puesta a punto (antes del primer reel)
tarea(d(2026, 11, 27), "Dueño", "Confirmar la fecha de la inauguración, la dirección nueva y si el local viejo cierra. Este calendario la pone el sábado 19/12 (noche VIP el viernes 18): si cambia, se corren juntas las filas marcadas 'Inauguración'.")
tarea(d(2026, 11, 27), "Dueño", "Pedido por escrito a la importadora (Grupo Antelo): unidades de exhibición y de prueba para la inauguración, un directivo en el acto, una condición comercial de lanzamiento para enero y el cupo 2027.")
tarea(d(2026, 11, 27), "Dueño", "Nombrar responsables: persona de contenido, vendedor 1 y vendedor 2 (los que aparecen en cámara), primer contacto de WhatsApp y Administración (precios y legal).")
tarea(d(2026, 11, 27), "Contenido", "Corregir lo que un comentario puede marcar: aviso del Eado en Mercado Libre ('215 cv' → motor a nafta de 101 HP y eléctrico de 212 HP; 'cámara de retroceso' → cámara 360 con dashcam; 'taller autorizado' → sacarlo hasta confirmarlo con Changan); ficha de la H6 en la web ('6 km/l' → 5,6 L/100 km mixto según la marca); fichas con '1.5 cc' → 1.5 L; ficha del ORA 03 vacía; Jolion cargado dos veces; fotos llamadas 'ChatGPT Image' (reemplazarlas por fotos reales); descripción del video EV/PHEV/HEV en TikTok ('Y uno de ellos nunca se enchufa').")
tarea(d(2026, 11, 27), "Contenido", "Comprar el kit: micrófono corbatero inalámbrico doble, trípode, luz LED con difusor y soporte de celular para auto.")
tarea(d(2026, 11, 28), "Primer contacto", "WhatsApp Business: catálogo con un producto por modelo, bienvenida y ausencia, respuestas rápidas (cuota con legal, turno de prueba, usado, cómo llegar, horario) y una etiqueta por palabra clave.")
tarea(d(2026, 11, 30), "Contenido", "Línea de base: seguidores, alcance de los últimos 30 días y % de Córdoba en Instagram y TikTok, y consultas por semana. Contra eso se mide todo.")
tarea(d(2026, 11, 28), "Contenido", "Exportar y clasificar los 142 comentarios del video EV/PHEV/HEV de TikTok y los de Instagram: precio, técnica, opinión, de Córdoba o no. La pregunta más repetida es el 'Respuesta a @' del 11/1.")
tarea(d(2026, 11, 28), "Contenido", "Perfil de Instagram: bio con 'Concesionario oficial en Córdoba', link de WhatsApp con el código BIO, historias destacadas (Modelos, Cómo comprar, Taller, Ubicación).")
tarea(d(2026, 11, 28), "Administración", "Planilla de consultas: fecha, nombre, palabra clave, modelo, A/B/C (A = quiere comprar en 30 días), vendedor, turno, venta.")
tarea(d(2026, 11, 30), "Administración", "Pedir al abogado la revisión de la placa legal (precio en pesos, precio sin impuestos nacionales, TNA, CFTEA, vigencia) y de la autorización de imagen para clientes e invitados.")
# Inauguración (Día D = sáb 19/12)
tarea(d(2026, 12, 1), "Dueño", "Inauguración: elegir un beneficio directo para quien compre en enero (service bonificado o un accesorio, con vigencia y stock). Recomendado en vez de un sorteo.")
tarea(d(2026, 12, 1), "Contenido", "Inauguración: preparar el Perfil de Google para la mudanza (2 administradores, exportar reseñas, fotos del cartel instalado para la reverificación).")
tarea(d(2026, 12, 2), "Contenido", "Plantillas de edición en CapCut: subtítulos palabra por palabra, colores de marca, placa legal y placa final con el logo.")
tarea(d(2026, 12, 3), "Dueño", "Inauguración: cotizar catering, sonido, fotógrafo y video para la noche VIP y el día abierto.")
tarea(d(2026, 12, 4), "Dueño", "Inauguración: lista cerrada de invitados VIP (clientes de los últimos 2–3 años, flotas y pymes, importadora, ACARA regional, prensa local, referentes).")
tarea(d(2026, 12, 4), "Contenido", "Anuncios: armar A1 (mensajes a WhatsApp, stock real, personas a 30–50 km del salón, USD 12 por día desde el lunes 7/12) con los reels del Eado. Armar A5 (Google, 'modelo + Córdoba', USD 5 por día desde el 14/12).")
tarea(d(2026, 12, 5), "Dueño", "Inauguración: mandar las invitaciones VIP por WhatsApp, una por una, con nombre (no difusión masiva).")
tarea(d(2026, 12, 7), "Contenido", "Anuncios: arranca A1 (USD 12 por día).")
tarea(d(2026, 12, 9), "Dueño", "Inauguración: mandar el kit de prensa a medios de Córdoba con un dato que sea noticia (unidades entregadas de un modelo, taller preparado para alta tensión, cargadores en el local o una financiación). 'Abrimos un local más grande' solo no es noticia.")
tarea(d(2026, 12, 9), "Contenido", "Inauguración: check-in con QR que abre WhatsApp con 'Vengo a la inauguración' y carteles de 'este evento se filma'.")
tarea(d(2026, 12, 11), "Contenido", "Anuncios: arranca A2 (inauguración, personas a 15–20 km del local nuevo, mensajes a WhatsApp con código ABRIMOS, USD 10 por día hasta el sábado 19 a las 18 h).")
tarea(d(2026, 12, 11), "Dueño", "Inauguración: cartel 'Nos mudamos' en el local viejo con la dirección nueva y un QR a Google Maps.")
tarea(d(2026, 12, 12), "Administración", "Inauguración: avisar la mudanza a marcas, bancos, aseguradoras y directorios.")
tarea(d(2026, 12, 14), "Vendedores", "Inauguración: ensayo de las pruebas de manejo (recorrido fijo de 30 min, licencia, alcoholemia cero, planilla de turnos).")
tarea(d(2026, 12, 14), "Contenido", "Anuncios: arranca A5 en Google (USD 5 por día).")
tarea(d(2026, 12, 16), "Dueño", "Inauguración: brief con todo el equipo (roles, horarios, qué se filma, quién atiende WhatsApp).")
tarea(d(2026, 12, 17), "Primer contacto", "Inauguración: guardia reforzada de WhatsApp desde hoy hasta el lunes 21.")
tarea(d(2026, 12, 18), "Todos", "NOCHE VIP (lista cerrada): 14:00 armado, autos en posición, prueba de sonido, QR y autorizaciones de imagen impresas · 19:30 recepción y firma de autorizaciones (alcohol solo para mayores que no manejan) · 20:15 palabras del dueño (3 min) y de la importadora (3 min), con el dato-noticia · 20:30 corte de cinta y foto oficial · 20:45 recorrido en grupos: salón, taller, entrega · 21:00 los vendedores toman turnos de prueba para los días siguientes (nadie maneja esta noche) · 22:30 cierre; foto y texto a la prensa.")
tarea(d(2026, 12, 18), "Primer contacto", "Recordatorio a los invitados por WhatsApp a las 10:00, con la dirección y un mapa.")
tarea(d(2026, 12, 19), "Contenido", "8:00 Mudanza digital, en este orden: web (contacto, pie, mapa y 'nos mudamos'), Perfil de Google (editar la dirección del perfil existente, NO crear otro, y reverificar), publicación 'nos mudamos' con fotos reales, bio y ubicación de Instagram y Facebook, dirección de los avisos de Mercado Libre.")
tarea(d(2026, 12, 19), "Todos", "DÍA ABIERTO: 8:30 brief (1 asesor cada 3–4 autos, 2–3 personas en las pruebas, guardia de WhatsApp, 1 supervisor) · 10:00 apertura con check-in por QR · 11:00 vivo de 30–45 min por el salón en Instagram y TikTok (otro vendedor contesta el chat) · 11 a 17 pruebas de manejo SOLO con turno, en franjas de 30 min; el que llega sin turno se agenda para otro día · 12 a 15 actividad para chicos y comida · 18:00 cierre · 18:30 cargar check-ins y consultas con su letra A/B/C y mandar un gracias a todos.")
tarea(d(2026, 12, 21), "Primer contacto + Vendedores", "Inauguración: seguimiento de cada consulta del evento (check-ins, turnos y mensajes), por teléfono o WhatsApp, hoy y mañana: que ninguna pase de 72 horas sin respuesta.")
tarea(d(2026, 12, 21), "Contenido", "Inauguración: actualizar directorios, Mercado Libre y WhatsApp Business con la dirección nueva.")
tarea(d(2026, 12, 21), "Vendedores", "Desde hoy, en cada entrega y service: QR para dejar una reseña en Google + WhatsApp a las 48 h con el link directo, a todos los clientes y sin premio. Responder todas en 48 h.")
tarea(d(2026, 12, 22), "Contenido", "Inauguración: juntar las notas de prensa publicadas y compartirlas en historias.")
for n, f in ((7, d(2026, 12, 26)), (14, d(2027, 1, 2)), (30, d(2027, 1, 18)), (60, d(2027, 2, 17))):
    tarea(f, "Contenido", f"Mudanza en Google (día {n} después): buscar el local en Maps, revisar que no haya un pin viejo o duplicado y que la dirección nueva esté publicada.")
# Enero y febrero
tarea(d(2026, 12, 28), "Dueño + Administración", "Confirmar por escrito la promo de apertura de enero (condición, modelos, inicio 4/1, fin y stock). Si no hay condición: el reel del 4/1 pasa a 'Enero en el local nuevo: tasación de tu auto en el día y prueba de manejo con turno', sin descuento.")
tarea(d(2026, 12, 30), "Administración", "Listas de precios de enero antes del 4/1: placas, carrusel del 8/1, avisos de Mercado Libre, respuestas rápidas de WhatsApp y anuncios.")
tarea(d(2026, 12, 30), "Contenido", "Anuncios de enero: preparar A1b (USD 20 por día), A3 (retargeting de los que vieron el 50–95 % de los reels o interactuaron, a 50 km, USD 5 por día, con placas de precio de 6–8 s) y A4 (promoción del mejor reel de la semana, USD 3 por día).")
tarea(d(2027, 1, 4), "Contenido", "Anuncios: arrancan A1b, A3 y A4. Se apaga A1.")
tarea(d(2027, 1, 11), "Contenido", "Anuncios: arranca A6, prueba de formulario contra WhatsApp (USD 6 por día, hasta el 7/2). Gana el canal con menor costo por turno que asiste.")
tarea(d(2027, 1, 13), "Dueño", "Cupo 2027: qué unidades llegan y cuándo (cambia qué modelos se empujan en febrero).")
tarea(d(2027, 1, 18), "Dueño + Contenido", "Revisión de 30 días de la inauguración: consultas, turnos, ventas por palabra clave y por canal. Si entretener trae vistas pero no consultas de Córdoba, pasar 5–10 puntos a educar y vender.")
tarea(d(2027, 2, 1), "Contenido", "Anuncios: A1b pasa a USD 10 por día (febrero cae ~37 % contra enero).")
tarea(d(2027, 2, 1), "Dueño", "Colaboración con un creador cordobés (por ejemplo, Mauro Osorio): contactarlo, preguntar si cobra y si trabaja con otra concesionaria. Si hay pago o canje, se marca como colaboración pagada. Si no se cierra antes del 13/2, el 20/2 sale el plan B.")
tarea(d(2027, 2, 10), "Contenido", "Anuncios: cerrar la prueba A6 y quedarse con el canal ganador.")
tarea(d(2027, 2, 15), "Dueño", "Expoagro (9 al 12/3): decidir si se va con la L200 y la H7.")
tarea(d(2027, 2, 17), "Dueño + Contenido", "Revisión de 60 días y plan de marzo: qué palabra clave trajo más ventas, qué formato retuvo más a 3 s y qué se repite en marzo.")
tarea(d(2027, 2, 26), "Contenido", "Dejar editadas las 4 piezas grabadas el 23/2, para la primera semana de marzo.")

# ---------------------------------------------------------------- lo que pasa en Córdoba
EVENTOS = {
    d(2026, 12, 18): "Vence el aguinaldo · terminan las clases en Córdoba · NOCHE VIP",
    d(2026, 12, 19): "INAUGURACIÓN: DÍA ABIERTO",
    d(2027, 1, 6): "Reyes (no es feriado) · mañana arranca el Festival de Jesús María (7 al 17/1)",
    d(2027, 1, 23): "Arranca el Festival de Cosquín (hasta el 31/1)",
    d(2027, 2, 6): "Cosquín Rock (6 y 7/2) · fin de semana largo de Carnaval (6 al 9/2)",
    d(2027, 2, 14): "San Valentín",
}


def contexto(f):
    partes = []
    if f in FERIADOS:
        partes.append(FERIADOS[f])
    if f in MEDIO_DIA:
        partes.append(MEDIO_DIA[f])
    if f in EVENTOS:
        partes.append(EVENTOS[f])
    if f < DIA_D and f != VIP:
        partes.append(f"Inauguración: faltan {(DIA_D - f).days} días")
    if d(2027, 1, 7) <= f <= d(2027, 1, 17):
        partes.append("Festival de Jesús María")
    if d(2027, 1, 24) <= f <= d(2027, 1, 31):  # el 23 ya dice 'Arranca el Festival de Cosquín'
        partes.append("Festival de Cosquín")
    if f.weekday() == 0 or f == INICIO or f.day == 1:  # la nota del mes, solo al empezar la semana o el mes
        if f.month in (11, 12) and f < DIA_D:
            partes.append("Diciembre es el mes más flojo del año: muchos pasan la compra a enero. Se construye público para la inauguración")
        elif f.month == 12 or (f.month == 1 and f.day < 4):
            partes.append("Fiestas y vacaciones: mucha gente en la ruta")
        elif f.month == 1:
            partes.append("Enero: el pico del año (casi el triple de patentamientos que diciembre)")
        elif f.month == 2:
            partes.append("Febrero: la venta cae ~37 % contra enero; menos pauta y grabar para marzo")
    return " · ".join(dict.fromkeys(partes))


# Datos para las historias de los días sin publicación (se rotan)
DATOS_HISTORIAS = ["EADO-3", "ORA05-4", "H7-1", "DEEPAL-6", "JMEV-1", "CS55-1", "H6-1", "ORA03-5", "TANK-1", "L200-1",
                   "EADO-7", "ORA05-6", "H7-7", "DEEPAL-1", "OUT-1", "JOLION-3", "EADO-9", "H6-4", "CS55-5", "JMEV-4"]


# ---------------------------------------------------------------- una palabra clave por publicación y su pedido de compartir
# (así se sabe qué video trajo cada consulta; el mensaje automático de la palabra se carga el 28/11)
CODIGO = {"CAR1": "TIPO", "D26": "PAPELES", "D28": "PLUS", "V01": "EADO", "D01": "ENERO", "D06": "LUZ", "V12": "ABRIMOS",
          "E08": "COCHERA", "V13": "TURNO", "D18": "AGUINALDO", "E18": "FIESTA", "D23": "AUXILIO", "E06": "VALIJAS", "D11": "RUTA",
          "E27": "COSTO", "D29": "BATERIA", "V11": "APERTURA", "E09": "JESUSMARIA", "V14": "CS55", "CAR2": "PRECIOS", "E02": "CAFE",
          "D19a": "PREGUNTA", "D02": "ENCHUFE", "V15": "EASY", "E25": "MEDIMOS", "D21": "TASA", "D24": "RINDE", "E10": "COSQUIN",
          "V19": "OUTLANDER", "D13": "TOTAL", "D22": "HIBRIDO", "V16": "S05", "E01": "ORA05", "E12": "CORDOBES", "D03": "CHINO",
          "V21": "PESOS", "E07": "ASADO", "D04": "REPUESTO", "V02": "H6", "E03": "H7", "D19b": "DUDA", "D05": "CARGA", "V06": "L200",
          "E28": "SIERRAS", "V17": "JOLION", "D27": "MARCA", "V08": "EMPRESA", "E23": "MITOS"}
COMPARTIR = {
    "D26": "Mandáselo a quien está por dejar una seña.",
    "D28": "Mandáselo a quien está mirando este auto.",
    "D01": "Mandáselo a quien no sabe si cambiar el auto ahora o en enero.",
    "D06": "Mandáselo a quien dice que la luz le va a salir más cara que la nafta.",
    "E08": "Mandáselo a quien vive en un departamento con cochera.",
    "D18": "Mandáselo a quien está por cobrar el aguinaldo.",
    "D23": "Mandáselo a quien sale de vacaciones con un auto nuevo.",
    "D11": "Mandáselo a quien sale a la ruta este verano.",
    "D02": "Mandáselo a quien no se decide entre enchufe y nafta.",
    "D21": "Mandáselo a quien está por sacar un crédito 'tasa 0'.",
    "D24": "Mandáselo a quien cree que va a hacer los kilómetros del folleto.",
    "D13": "Mandáselo a quien está comparando avisos de autos.",
    "D22": "Mandáselo a quien quiere un enchufable y no tiene cochera.",
    "D03": "Mandáselo a quien todavía dice '¿un auto chino?'.",
    "D04": "Mandáselo a quien tiene miedo de quedarse sin repuestos.",
    "D05": "Mandáselo a quien cree que para cargar un auto hay que hacer una obra.",
    "D27": "Mandáselo a quien tiene esta duda antes de comprar.",
}
for _i, (_f, _h, _fmt, _gid, _ex) in enumerate(PUBLICA):
    if _gid in CODIGO:
        _ex.setdefault("codigo", CODIGO[_gid])
    if _gid in COMPARTIR:
        _ex.setdefault("compartir", COMPARTIR[_gid])

PALABRAS_DEL_CALENDARIO = " · ".join(f"{_ex['codigo']} ({_f.strftime('%d/%m')})" for _f, _h, _fmt, _gid, _ex in PUBLICA if _ex.get("codigo"))
T.setdefault(d(2026, 11, 28), []).insert(0, ("Contenido", "Palabra clave → mensaje automático (ManyChat u otra): cada palabra del calendario manda un mensaje con 2 botones que abren WhatsApp con el mensaje ya escrito. Probarlo desde una cuenta que no sigue (llega a Solicitudes). Hay una palabra por publicación (la lista completa está al final de esta celda), así se sabe qué video trajo cada consulta. Cargar cada una antes de su día. PALABRAS: " + PALABRAS_DEL_CALENDARIO + "."))
