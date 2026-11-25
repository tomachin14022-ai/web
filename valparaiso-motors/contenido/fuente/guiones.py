"""Guiones de las piezas del calendario. Cada pieza del Calendario apunta a uno de estos por su ID."""

CTA = "Pedinos precio y financiación de cualquiera de nuestros autos."
LEGAL_CUOTA = (
    "LEGAL EN PANTALLA (mínimo 5 segundos seguidos, abajo, letra legible en el celular): "
    "Precio final de contado $[..] · Precio sin impuestos nacionales $[..] · [N] cuotas de $[..] · TNA [..] % · CFTEA [..] % · "
    "[Si ajusta por UVA o CER: 'Cuota ajustable por UVA/CER'] · Vigente del [..] al [..] en Córdoba · "
    "PARA MÁS INFORMACIÓN O LIMITACIONES APLICABLES CONSULTE EN www.valparaisomotors.com.ar/condiciones. "
    "Todos los datos los da Administración el día que se publica. Precio en pesos; el dólar, solo como agregado y con la misma letra."
)
FIJADO = "Pedinos precio y financiación: comentá {k} y te escribimos por mensaje 📩 (si no nos seguís, te llega a Solicitudes)."
MSG = "Hola, vengo del video {k}. Quiero precio y financiación."

GUIONES = [
    {
        "id": "G01",
        "pieza": "¿Patentás en diciembre o esperás a enero?",
        "formato": "Reel 40–50 s, vendedor a cámara en el salón",
        "aparece": "Vendedor 1",
        "gancho": "¿PATENTÁS AHORA O ESPERÁS A ENERO?",
        "gancho_b": "ESPERAR A ENERO PUEDE SALIRTE MÁS CARO… O NO",
        "guion": (
            "0–2 s (palabra por palabra): \"¿Estás por cambiar el auto y no sabés si patentarlo ahora o esperar a enero? Al final te digo cómo hacer la cuenta.\"\n"
            "2–8 s: \"Soy [nombre], vendedor de Valparaiso Motors.\" Por qué mucha gente espera a enero: que el auto figure patentado en el año nuevo. Enero de 2026 tuvo casi el triple de patentamientos que diciembre de 2025 (dato ACARA en pantalla).\n"
            "8–18 s (re-gancho: \"Pero…\"): lo que pasa en diciembre: las marcas suelen bonificar para cerrar el año. Solo decir una bonificación si Administración la confirma ese día.\n"
            "18–30 s (\"Entonces…\"): la pregunta que hay que hacer: cómo figura el año modelo de esa unidad en el certificado de fábrica (verificarlo antes de grabar) y cuánto vale la bonificación de hoy contra la diferencia al revenderlo.\n"
            "30–40 s (paga la promesa): \"La cuenta es simple: lo que te ahorrás hoy contra lo que vale de más un auto que figura 2027. Si te ahorrás más de lo que perdés, conviene ahora.\"\n"
            "40–45 s (CTA, palabra por palabra): \"" + CTA + " Comentá PATENTAR y te hacemos la cuenta con tu auto.\""
        ),
        "tomas": "Plano medio del vendedor junto a una unidad (3 tomas del gancho) · plano detalle del parabrisas con la oblea o el papel del certificado (sin datos personales) · calendario de pared o del celular pasando de diciembre a enero · B-roll del salón.",
        "texto": "Gancho fijo desde el cuadro 0 · 'Enero 2026: 66.080 patentamientos · Dic. 2025: 23.997 (ACARA/DNRPA)' · 'Bonificación de hoy vs. valor de reventa' · placa final con el CTA.",
        "descripcion": (
            "¿Patentás en diciembre o esperás a enero? 🗓️\n"
            "En enero de 2026 se patentaron 66.080 autos, casi el triple que en diciembre de 2025 (23.997, datos ACARA/DNRPA). Mucha gente espera para que el auto figure en el año nuevo.\n"
            "Pero en diciembre las marcas suelen bonificar para cerrar el año. La cuenta: lo que te ahorrás hoy contra lo que vale de más al revenderlo.\n"
            "Comentá PATENTAR y te hacemos la cuenta con tu caso. Estamos en Córdoba.\n"
            "Información general. No constituye oferta."
        ),
        "hashtags": "#0km #patentamiento #autosnuevos #financiacion #AutosCordoba",
        "fijado": FIJADO.format(k="PATENTAR"),
        "codigo": "PATENTAR",
        "mensaje": MSG.format(k="PATENTAR"),
    },
    {
        "id": "G02",
        "pieza": "Llegó al salón (serie de stock real)",
        "formato": "Reel 30–45 s, vendedor recorre una unidad real",
        "aparece": "Vendedor 1 o 2 (se turnan)",
        "gancho": "[BENEFICIO PARA EL QUE MIRA], EJ.: 'SE ENCHUFA EN TU CASA Y NO TE DEJA A PIE EN LA RUTA'",
        "gancho_b": "PREGUNTA SOBRE LA VIDA DEL QUE MIRA, EJ.: '¿CUÁNTOS KM HACÉS POR DÍA?'",
        "guion": (
            "Plantilla para todas las semanas: cambia la unidad, la estructura no.\n"
            "0–2 s (palabra por palabra): el beneficio escrito y dicho, con la unidad andando o abriéndose una puerta. Sin el nombre del modelo.\n"
            "2–6 s: \"Soy [nombre], vendedor de Valparaiso Motors, y esta unidad está hoy en el salón.\" Promesa: \"Al final te digo cuánto queda la cuota.\"\n"
            "6–25 s: 3 cosas que se ven, de la menos a la más importante (anunciar 'la tercera es la que más importa'). Solo datos verificados de la ficha (ver CLAUDE.md, sección 3) con su aclaración chica (NEDC, WLTP, 'declarado por la marca').\n"
            "25–35 s: el nombre del modelo recién acá + precio de contado y cuota con su legal (pagar la promesa).\n"
            "35–40 s (palabra por palabra): \"" + CTA + " Comentá [PALABRA] y te mando la cuota por mensaje.\"\n"
            "Reglas: 'entrega inmediata' solo si es verdad ese día; nada de 'el mejor' o 'el más completo'; si la unidad es Changan, verificar antes cómo se presenta el concesionario."
        ),
        "tomas": "Siempre las mismas, para armar plantilla: frente 3/4 · lateral con llanta · interior desde la puerta del conductor · pantallas encendidas · baúl abierto · tapa de carga o motor · vendedor a cámara (3 tomas del gancho) · vendedor señalando el detalle n.º 3.",
        "texto": "Gancho fijo · 3 etiquetas de detalle que entran con cada punto · nombre del modelo en el segundo 25 · " + LEGAL_CUOTA,
        "descripcion": (
            "[Gancho de la pieza, sin nombrar el modelo] 👀\n"
            "Esta unidad está hoy en nuestro salón de Córdoba. [3 datos con su aclaración: NEDC, WLTP o 'declarado por la marca'].\n"
            "Comentá [PALABRA] y te mandamos precio y cuota por mensaje.\n"
            "[Legal completo con precio, cuotas, TNA, CFTEA, vigencia y la frase de la web]."
        ),
        "hashtags": "#[modelo] #0km #financiacion #[tipo: hibrido / electrico / 4x4] #AutosCordoba",
        "fijado": FIJADO.format(k="[PALABRA]"),
        "codigo": "STOCK-[MODELO]",
        "mensaje": "Hola, vengo del video de la unidad [MODELO] (STOCK-[MODELO]). Quiero precio y financiación.",
    },
    {
        "id": "G03",
        "pieza": "Se arma el nuevo Valparaiso (serie de la obra)",
        "formato": "Reel 20–30 s, celular, sin vendedor o con una cara del equipo",
        "aparece": "Equipo (opcional)",
        "gancho": "EP. 1: '¿ADIVINÁS DÓNDE QUEDA?' · EP. 2: '¿CUÁNTOS AUTOS ENTRAN ACÁ?'",
        "gancho_b": "'ESTO EN [N] DÍAS VA A SER UN CONCESIONARIO'",
        "guion": (
            "Ep. 1 (D-15): 0–2 s plano que avanza hacia la obra con el texto del gancho. 2–12 s: 4 o 5 detalles que dan pistas del lugar sin decirlo (un cartel de calle tapado, la vista, un edificio conocido). 12–18 s: 'Te lo decimos el [fecha del anuncio]. Escribí en los comentarios dónde creés que es'. Sin CTA comercial: este video entretiene.\n"
            "Ep. 2 (D-10): 0–2 s el salón vacío con el gancho. 2–15 s: llegan las primeras unidades o se arma el taller (cortes cada 1–2 s). 15–20 s: la respuesta ('entran [N] autos en exhibición') y 'el [fecha] te mostramos todo'.\n"
            "Las pistas y los números tienen que ser reales. La dirección exacta se publica recién en el anuncio oficial (INA-03), cuando el Perfil de Google esté listo."
        ),
        "tomas": "Caminata hacia la obra (estabilizador) · 5 detalles cerrados (pistas) · timelapse de 20–30 min del armado · llegada de un auto (si coincide) · el cartel nuevo tapado o a medio poner.",
        "texto": "Gancho fijo · etiquetas cortas por pista · 'Ep. 1/2 · Se arma el nuevo Valparaiso' chico arriba (dentro de la zona segura) · 'Mandáselo a alguien que vive cerca'.",
        "descripcion": "¿Adivinás dónde va a estar el nuevo Valparaiso Motors? 👀 Dejá tu respuesta en los comentarios. Mandáselo a alguien que vive cerca. Córdoba.",
        "hashtags": "#Cordoba #concesionaria #0km #detrasdeescena #AutosCordoba",
        "fijado": "Te lo contamos el [fecha]. Mientras, comentá tu apuesta 👇",
        "codigo": "",
        "mensaje": "",
    },
    {
        "id": "G04",
        "pieza": "Adiviná (serie de juego)",
        "formato": "Reel 20–35 s, vendedor + unidad",
        "aparece": "Vendedor 2",
        "gancho": "EP. 1: '¿EN CUÁNTOS SEGUNDOS LLEGA A 100?' · EP. 2: '¿CUÁNTOS KM HACE CON LO QUE SALE UN CAFÉ?' · EP. 3: '¿QUÉ HAY DEBAJO DE ESTE AUTO?'",
        "gancho_b": "'NADIE ACIERTA ESTE NÚMERO'",
        "guion": (
            "0–2 s: la pregunta escrita y dicha, con la unidad en movimiento lento (sin maniobras en la calle).\n"
            "2–8 s: 3 opciones en pantalla (A/B/C), una cuenta regresiva corta y '¿cuál decís?'.\n"
            "8–15 s (re-gancho): una pista que enseña algo (ej.: 'tiene un motor naftero y otro eléctrico que empujan juntos').\n"
            "15–25 s: la respuesta con su fuente chica. Ep. 1: ORA 05 HEV, 7,7 s declarados por la marca (no medirlo en la calle). Ep. 2: estimado con la tarifa de luz vigente y el consumo declarado (ORA 03: 16,7 kWh/100 km WLTP); la cuenta completa va en la descripción. Ep. 3: Haval H7 con la cámara que 've a través del piso' (confirmar que la versión en stock la tiene).\n"
            "25–30 s: nombre del modelo y CTA corto: \"" + CTA + " Comentá [PALABRA].\""
        ),
        "tomas": "Unidad estática con luz lateral · pantalla o tablero con el dato · vendedor haciendo la pregunta (3 tomas) · reacción del vendedor 2 si está · placa de opciones (la hace el editor).",
        "texto": "Pregunta fija · opciones A/B/C con un 'pop' · respuesta grande en bordó · fuente chica ('declarado por la marca' / 'estimado: ver la cuenta en la descripción').",
        "descripcion": "[Pregunta del juego] 🤔 Dejá tu respuesta antes de que termine el video. [Si es una cuenta propia: la cuenta completa, ej.: '16,7 kWh cada 100 km × $[tarifa] el kWh = $[..] cada 100 km'.] Comentá [PALABRA] y te mandamos precio y financiación. Córdoba.",
        "hashtags": "#autos #0km #[hibrido o electrico] #juego #AutosCordoba",
        "fijado": FIJADO.format(k="[PALABRA]"),
        "codigo": "JUEGO-[N]",
        "mensaje": "Hola, vengo del juego del video (JUEGO-[N]). Quiero precio y financiación.",
    },
    {
        "id": "G05",
        "pieza": "Anuncio oficial de la inauguración",
        "formato": "Reel 25–35 s + misma pieza en Historias, Facebook, TikTok y Estados",
        "aparece": "Dueño o vendedor 1",
        "gancho": "'¿CUÁNTO TARDÁS EN LLEGAR A [REFERENCIA DE LA ZONA NUEVA]?'",
        "gancho_b": "'EL [DÍA] TE ESPERAMOS EN [REFERENCIA]'",
        "guion": (
            "0–2 s: imagen del local nuevo terminado (lo más fuerte primero) con el gancho escrito: una referencia que el cordobés conoce (avenida, rotonda, Circunvalación).\n"
            "2–8 s: \"Desde el [fecha] nos encontrás acá, en [dirección nueva].\" Qué gana el que viene: más unidades para ver y probar, taller, entrega (solo lo que sea cierto).\n"
            "8–18 s (re-gancho \"Y el sábado [fecha]…\"): el día abierto: horario, qué va a haber, que la prueba de manejo es con turno.\n"
            "18–25 s: cómo llegar en una frase y el mapa.\n"
            "25–30 s: \"Pedí tu turno de prueba de manejo por WhatsApp\" no es un CTA nuevo: el botón va dentro del chat. En el video se dice el CTA único: \"" + CTA + "\" y en pantalla 'Comentá ABRIMOS'."
        ),
        "tomas": "Fachada con cartel (de día) · el salón con las unidades · el taller · la entrada al estacionamiento · un plano desde la avenida para mostrar la referencia · dueño o vendedor a cámara.",
        "texto": "Gancho · 'Desde el [fecha] · [dirección nueva]' · 'Sábado [fecha] · día abierto · [horario]' · 'Prueba de manejo con turno' · mapa simple (dibujado plano, no 3D) · logo chico al final.",
        "descripcion": (
            "¿Cuánto tardás en llegar a [referencia]? 🚗\n"
            "Desde el [fecha] Valparaiso Motors atiende en [dirección nueva], Córdoba. El sábado [fecha] hacemos el día abierto de [hora] a [hora]: [lo que va a haber].\n"
            "La prueba de manejo es con turno: comentá ABRIMOS y te lo damos por mensaje.\n"
            "[Si hay beneficio de inauguración: condición breve + 'PARA MÁS INFORMACIÓN O LIMITACIONES APLICABLES CONSULTE EN www.valparaisomotors.com.ar/condiciones'. Si hay sorteo: 'Sin obligación de compra'.]"
        ),
        "hashtags": "#Cordoba #inauguracion #concesionaria #0km #AutosCordoba",
        "fijado": FIJADO.format(k="ABRIMOS"),
        "codigo": "ABRIMOS",
        "mensaje": "Hola, vengo del video de la inauguración (ABRIMOS). Quiero un turno de prueba de manejo.",
    },
    {
        "id": "G06",
        "pieza": "Cuenta regresiva en Historias (D-7 a D-1)",
        "formato": "Historias, 3–5 cuadros por día",
        "aparece": "Equipo",
        "gancho": "Sticker de cuenta regresiva de Instagram 'Inauguración' (el que lo toca recibe el recordatorio)",
        "gancho_b": "",
        "guion": (
            "D-7: foto de la fachada + sticker de cuenta regresiva + 'falta una semana'.\n"
            "D-6: detrás de escena (limpieza, llegada de unidades) + encuesta '¿qué querés ver primero? Salón / Taller'.\n"
            "D-5: el equipo de ventas, una foto por vendedor con su nombre ('Soy [nombre], vendedor').\n"
            "D-4: cómo llegar: captura del mapa + sticker de enlace a Google Maps.\n"
            "D-3: sticker de pregunta '¿qué le querés preguntar al taller?'.\n"
            "D-2: 'la prueba de manejo es con turno' + sticker de enlace a WhatsApp con el código TURNO.\n"
            "D-1: cobertura de la noche VIP (si los invitados firmaron la autorización de imagen) + 'mañana abrimos de [hora] a [hora]'.\n"
            "Repetir el sticker de cuenta regresiva todos los días. Guardar todo en la destacada 'Nuevo local'."
        ),
        "tomas": "Fotos y videos de 3–8 s con el celular, verticales, con luz natural. Nada de clientes sin autorización.",
        "texto": "Letra de la marca, texto corto, zona segura de Historias (nada arriba de 250 px ni abajo de 340 px).",
        "descripcion": "",
        "hashtags": "",
        "fijado": "",
        "codigo": "TURNO",
        "mensaje": "Hola, vengo de las historias (TURNO). Quiero un turno de prueba de manejo.",
    },
    {
        "id": "G07",
        "pieza": "Cobertura de la noche VIP y del día abierto",
        "formato": "Historias + vivo de 30–45 min el día abierto (Instagram y TikTok a la vez si hay dos celulares)",
        "aparece": "Dueño, vendedores, importadora",
        "gancho": "Vivo: 'Estamos abiertos: te muestro el salón nuevo en vivo'",
        "gancho_b": "",
        "guion": (
            "Noche VIP (lista cerrada): historias cada 20–30 min: llegada, palabras del dueño (1 clip de 15 s), corte de cinta, foto oficial. Solo personas que firmaron la autorización de imagen.\n"
            "Día abierto, vivo a las 11 h (30–45 min): 0–3 min saludo y qué se va a ver · 3–15 min recorrido del salón por marca · 15–25 min taller y entrega · 25–35 min preguntas del chat · cierre con el código VIVO en pantalla y 'escribinos por WhatsApp'. Un segundo vendedor responde el chat y el WhatsApp durante el vivo (el mensaje automático de Instagram solo funciona mientras dura el vivo).\n"
            "Historias cada hora con lo que pasa. Nada de primeros planos de chicos sin autorización de los padres."
        ),
        "tomas": "Celular en estabilizador con micrófono corbatero inalámbrico · un segundo celular para historias · batería externa.",
        "texto": "En el vivo: cartel físico o en pantalla con 'Código VIVO · WhatsApp [número]'.",
        "descripcion": "",
        "hashtags": "",
        "fijado": "",
        "codigo": "VIVO",
        "mensaje": "Hola, vengo del vivo (VIVO). Quiero precio y financiación.",
    },
    {
        "id": "G08",
        "pieza": "Así fue la inauguración (resumen)",
        "formato": "Reel 25–35 s",
        "aparece": "Equipo e invitados con autorización",
        "gancho": "'[N] PERSONAS VINIERON A VER ESTO'",
        "gancho_b": "'ASÍ QUEDÓ EL NUEVO VALPARAISO'",
        "guion": (
            "0–2 s: el plano más lleno del día con el número real de asistentes (sale del check-in con QR; si no se midió, usar el gancho B).\n"
            "2–20 s: cortes cada 1–1,5 s: corte de cinta, recorrido, taller, test drives con turno, familias (solo con autorización).\n"
            "20–28 s: 'Gracias, Córdoba' + dirección nueva + horario.\n"
            "28–32 s: \"" + CTA + "\" y 'Comentá ABRIMOS'."
        ),
        "tomas": "Todo lo grabado en la noche VIP y el día abierto (pedir a cada persona que filme 10 clips de 3–5 s).",
        "texto": "Número real o gancho B · 'Gracias, Córdoba' · dirección y horario · logo chico al final.",
        "descripcion": "Así fue la inauguración del nuevo Valparaiso Motors en [dirección nueva], Córdoba. Gracias a todos los que vinieron 🙌 Comentá ABRIMOS y te mandamos precio y financiación. Mandáselo a alguien que no pudo venir.",
        "hashtags": "#Cordoba #inauguracion #concesionaria #0km #AutosCordoba",
        "fijado": FIJADO.format(k="ABRIMOS"),
        "codigo": "ABRIMOS",
        "mensaje": "Hola, vengo del video de la inauguración (ABRIMOS). Quiero precio y financiación.",
    },
    {
        "id": "G09",
        "pieza": "Cómo llegar al nuevo local",
        "formato": "Reel 15–20 s + carrusel de 4 placas",
        "aparece": "Sin personas o vendedor al final",
        "gancho": "'DE [PUNTO CONOCIDO] AL NUEVO VALPARAISO EN [N] MINUTOS'",
        "gancho_b": "'¿VENÍS POR [AVENIDA]? DOBLÁ ACÁ'",
        "guion": (
            "0–2 s: el giro clave grabado desde el auto (con soporte, nunca con el celular en la mano del que maneja) y el gancho escrito.\n"
            "2–12 s: el recorrido acelerado con 3 referencias marcadas.\n"
            "12–16 s: la entrada y el estacionamiento.\n"
            "16–20 s: dirección, horario y 'buscanos en Google Maps como Valparaiso Motors'.\n"
            "Los minutos se miden ese día con el GPS: decir 'en un día normal, a la hora [..]'."
        ),
        "tomas": "Recorrido desde 2 puntos conocidos con el celular en soporte · fachada · entrada al estacionamiento · cartel.",
        "texto": "Gancho · 3 referencias · dirección y horario · mapa plano dibujado.",
        "descripcion": "Así se llega al nuevo Valparaiso Motors: [dirección nueva], Córdoba. Horario: [..]. Buscanos en Google Maps como Valparaiso Motors. Guardalo para cuando vengas.",
        "hashtags": "#Cordoba #comollegar #concesionaria #0km #AutosCordoba",
        "fijado": "Horario: [..] · WhatsApp en la bio.",
        "codigo": "",
        "mensaje": "",
    },
    {
        "id": "G10",
        "pieza": "¿Auto chino? ¿Y si se rompe? (taller y posventa)",
        "formato": "Reel 40–50 s con el jefe de taller o un vendedor",
        "aparece": "Jefe de taller o técnico + vendedor",
        "gancho": "'¿AUTO CHINO? ¿Y SI SE ROMPE?'",
        "gancho_b": "'LA PREGUNTA QUE TODOS HACEN Y NADIE CONTESTA'",
        "guion": (
            "0–2 s: la pregunta, escrita y dicha por el vendedor, con el taller detrás.\n"
            "2–6 s: \"Es la pregunta que más nos hacen. Te muestro tres cosas, y la tercera es la que más importa.\"\n"
            "6–18 s: 1) el taller y los técnicos (cuántos, qué marcas atienden). 2) los repuestos: el depósito, cuánto tarda un repuesto común (dato real de posventa).\n"
            "18–35 s (re-gancho \"Pero lo más importante…\"): 3) la garantía con su condición exacta ('5 años o 150.000 km, lo que ocurra primero'; batería 8 años o 150.000 km en el Eado Plus) y dónde se hace el service.\n"
            "35–45 s: \"" + CTA + " Comentá TALLER y te contamos cómo es el service de tu modelo.\"\n"
            "Ep. 2 (febrero): mismos pasos con repuestos y tiempos reales de un service."
        ),
        "tomas": "Técnico trabajando (sin caras de clientes ni patentes) · estanterías de repuestos · elevador · herramienta de diagnóstico · placa de garantía.",
        "texto": "Gancho · 1, 2, 3 que entran con cada punto · garantía con su condición en letra chica.",
        "descripcion": "¿Auto chino? ¿Y si se rompe? 🔧 Te mostramos el taller de Valparaiso Motors en Córdoba, los repuestos y cómo funciona la garantía (con sus condiciones: [garantía exacta de cada modelo, 'lo que ocurra primero']). Comentá TALLER y te contamos cómo es el service de tu modelo.",
        "hashtags": "#autoschinos #service #garantia #0km #AutosCordoba",
        "fijado": FIJADO.format(k="TALLER"),
        "codigo": "TALLER",
        "mensaje": MSG.format(k="TALLER"),
    },
    {
        "id": "G11",
        "pieza": "El aguinaldo como anticipo",
        "formato": "Reel 35–45 s, vendedor + placa con un ejemplo",
        "aparece": "Vendedor 2",
        "gancho": "'¿CON EL AGUINALDO TE ALCANZA PARA EL ANTICIPO?'",
        "gancho_b": "'TU AGUINALDO PUEDE SER LA PRIMERA CUOTA DE TU AUTO NUEVO'",
        "guion": (
            "0–2 s: el gancho con un sobre o un celular con la notificación de sueldo (sin datos reales).\n"
            "2–8 s: \"Soy [nombre], vendedor de Valparaiso Motors. Te muestro un ejemplo, y al final te digo qué tenés que mirar antes de firmar.\"\n"
            "8–25 s: ejemplo con números reales de Administración: anticipo de $[..], [N] cuotas de $[..], TNA y CFTEA. Si el crédito ajusta por UVA, decirlo ('la cuota se ajusta con la inflación').\n"
            "25–35 s (paga la promesa): 'No mires solo la cuota: mirá el CFT, que incluye gastos, seguros e impuestos'.\n"
            "35–42 s: \"" + CTA + " Comentá AGUINALDO y te armamos el ejemplo con tu auto.\"\n"
            "Si no hay números confirmados, no se publica: se cambia por G23."
        ),
        "tomas": "Vendedor a cámara · placa con el ejemplo (la arma el editor) · unidad de fondo.",
        "texto": "Gancho · 'EJEMPLO' en la placa · " + LEGAL_CUOTA,
        "descripcion": "¿Con el aguinaldo te alcanza para el anticipo? 💸 Ejemplo: [anticipo, cuotas, TNA, CFTEA]. No mires solo la cuota: pedí el costo financiero total. Comentá AGUINALDO y te armamos el ejemplo con tu caso. Córdoba. [Legal completo.]",
        "hashtags": "#aguinaldo #financiacion #0km #cuotas #AutosCordoba",
        "fijado": FIJADO.format(k="AGUINALDO"),
        "codigo": "AGUINALDO",
        "mensaje": MSG.format(k="AGUINALDO"),
    },
    {
        "id": "G12",
        "pieza": "Promo de apertura (enero)",
        "formato": "Reel 25–30 s con vendedor + placa animada de 6–8 s para anuncios",
        "aparece": "Vendedor 1",
        "gancho": "'SI ESPERASTE A ENERO PARA CAMBIAR EL AUTO, ESTO ES PARA VOS'",
        "gancho_b": "'[BENEFICIO CONCRETO] HASTA EL [FECHA]'",
        "guion": (
            "Solo se publica si la condición está confirmada por escrito (importadora o Administración) con fecha de inicio y de fin y stock.\n"
            "0–2 s: el gancho con la unidad en el salón nuevo.\n"
            "2–10 s: \"Soy [nombre], de Valparaiso Motors. Para arrancar el año en el salón nuevo tenemos [beneficio concreto: ej. service bonificado, accesorio o tasa de la marca].\"\n"
            "10–20 s: para qué modelos, hasta cuándo y con qué stock.\n"
            "20–28 s: \"" + CTA + " Comentá APERTURA y te mandamos las condiciones.\"\n"
            "Placa de 6–8 s para retargeting: unidad + beneficio + legal + botón 'Pedinos precio y financiación'."
        ),
        "tomas": "Vendedor junto a 2 o 3 unidades · detalle de la unidad · fachada del local nuevo.",
        "texto": "Gancho · beneficio en bordó · 'Válido del [..] al [..] · Stock: [N] unidades' · 'Sin obligación de compra' si hay azar · " + LEGAL_CUOTA,
        "descripcion": "Si esperaste a enero para cambiar el auto, esto es para vos. [Beneficio] para [modelos], del [..] al [..] o hasta agotar [N] unidades, en Valparaiso Motors Córdoba. Comentá APERTURA y te mandamos las condiciones. PARA MÁS INFORMACIÓN O LIMITACIONES APLICABLES CONSULTE EN www.valparaisomotors.com.ar/condiciones",
        "hashtags": "#0km #financiacion #enero #concesionaria #AutosCordoba",
        "fijado": FIJADO.format(k="APERTURA"),
        "codigo": "APERTURA",
        "mensaje": MSG.format(k="APERTURA"),
    },
    {
        "id": "G13",
        "pieza": "Placas de financiación por modelo (carrusel)",
        "formato": "Carrusel 1080x1350, 6–8 placas: portada + una placa por modelo + CTA",
        "aparece": "Sin personas (fotos propias de las unidades)",
        "gancho": "Portada: '¿CUÁNTO QUEDA LA CUOTA DE CADA UNO?'",
        "gancho_b": "Portada: 'ELEGÍ EL TUYO Y TE DECIMOS LA CUOTA'",
        "guion": (
            "Placa 1: portada con 3 autos recortados de fotos propias.\n"
            "Placas 2–7: un modelo por placa: foto propia, 1 beneficio, precio de contado en pesos, cuota de ejemplo, TNA, CFTEA y vigencia.\n"
            "Placa final: 'Pedinos precio y financiación de cualquiera de nuestros autos' + 'comentá CUOTA' + logo chico.\n"
            "'deslizá →' chico abajo a la derecha en todas menos la última. Fondo papel o estudio blanco; bordó solo como placa con letras blancas."
        ),
        "tomas": "Fotos propias de cada unidad en el salón nuevo (frente 3/4, misma luz y misma altura de cámara).",
        "texto": "En cada placa de modelo, el legal completo: " + LEGAL_CUOTA,
        "descripcion": "¿Cuánto queda la cuota de cada uno? Deslizá y elegí 👉 Comentá CUOTA y te mandamos la simulación de tu modelo. Córdoba. [Legal completo por modelo.]",
        "hashtags": "#financiacion #0km #cuotas #concesionaria #AutosCordoba",
        "fijado": FIJADO.format(k="CUOTA"),
        "codigo": "CUOTA",
        "mensaje": MSG.format(k="CUOTA"),
    },
    {
        "id": "G14",
        "pieza": "¿Entra todo? (desafío de baúl y medidas)",
        "formato": "Reel 25–35 s",
        "aparece": "Vendedor 2 (y vendedor 1 si hace de 'familia')",
        "gancho": "EP. 1: '¿ENTRA TODO PARA LAS VACACIONES?' · EP. 2: '¿ENTRA EN UNA COCHERA DE NUEVA CÓRDOBA?'",
        "gancho_b": "'NADIE CREE QUE ENTRE TODO ESTO'",
        "guion": (
            "Ep. 1: 0–2 s la pila de cosas al lado del baúl (2 valijas grandes, conservadora, cochecito, bolso) y el gancho. 2–20 s: se carga de a una, con un contador en pantalla. 20–28 s: el resultado real (si no entra todo, se dice: da credibilidad) + el nombre del modelo. 28–32 s: CTA corto.\n"
            "Ep. 2: medidas reales del auto (largo, ancho con espejos) contra una cochera medida con cinta. Mostrar la cinta. Cuenta propia: 'estimado' si corresponde.\n"
            "CTA: \"" + CTA + " Comentá VALIJAS.\""
        ),
        "tomas": "Plano fijo del baúl (trípode) · cenital de la pila · detalle de cada objeto al entrar · vendedor reaccionando.",
        "texto": "Gancho · contador '1, 2, 3…' · resultado grande · nombre del modelo al final · litros de baúl solo si están en la ficha oficial.",
        "descripcion": "¿Entra todo para las vacaciones? 🧳 Lo probamos en el salón de Córdoba con [lista]. Resultado: [real]. Comentá VALIJAS y te mandamos precio y financiación. Mandáselo a quien siempre lleva de más.",
        "hashtags": "#vacaciones #baul #0km #familia #AutosCordoba",
        "fijado": FIJADO.format(k="VALIJAS"),
        "codigo": "VALIJAS",
        "mensaje": MSG.format(k="VALIJAS"),
    },
    {
        "id": "G15",
        "pieza": "Ida y vuelta medida (Jesús María, Cosquín, un día sin nafta)",
        "formato": "Reel 40–55 s (o animado con Claude si no se puede grabar)",
        "aparece": "Vendedor 1 manejando con soporte de celular (o voz del dueño si es animado)",
        "gancho": "'¿CUÁNTO GASTÁS PARA IR A [DESTINO] Y VOLVER?'",
        "gancho_b": "'FUIMOS A [DESTINO] Y VOLVIMOS. ESTO GASTAMOS'",
        "guion": (
            "Prueba real, sin estimar lo que se puede medir.\n"
            "0–2 s: el tablero al salir del salón (km y batería o nafta) con el gancho.\n"
            "2–6 s: \"Fuimos de Valparaiso Motors a [destino] y volvimos. Al final te muestro cuánto gastamos de verdad.\"\n"
            "6–25 s: 3 momentos del viaje (salida, ruta, llegada), con el tablero en cada uno. Nada de grabar manejando: graba el acompañante o el soporte fijo.\n"
            "25–40 s (re-gancho \"Pero ojo…\"): lo que cambia el resultado: velocidad, aire acondicionado, subidas. Si es un PHEV: cuántos km hizo en eléctrico y cuántos a nafta.\n"
            "40–50 s (paga la promesa): el costo real del viaje con la cuenta en pantalla (km × consumo medido × precio del litro o del kWh de ese día).\n"
            "50–55 s: \"" + CTA + " Comentá RUTA.\" Línea chica: 'Mandáselo a quien va a [destino] este verano'."
        ),
        "tomas": "Tablero al salir, en la ruta y al volver (con fecha y hora) · ruta desde el acompañante · cartel del destino (sin logos del festival) · surtidor o cargador si se usó.",
        "texto": "Gancho · km y consumo de cada tramo · cuenta final en bordó · 'medido el [fecha], con [condiciones]'.",
        "descripcion": "¿Cuánto gastás para ir a [destino] y volver? Lo medimos el [fecha]: [km] km, [consumo] → $[..] (cuenta: [km] × [consumo] × $[precio] = $[..]). Mandáselo a quien va este verano. Comentá RUTA y te mandamos precio y financiación. Córdoba.",
        "hashtags": "#ruta #consumo #hibrido #verano #AutosCordoba",
        "fijado": FIJADO.format(k="RUTA"),
        "codigo": "RUTA",
        "mensaje": MSG.format(k="RUTA"),
    },
    {
        "id": "G16",
        "pieza": "¿Enchufe o nafta? Dos vendedores, dos autos",
        "formato": "Reel 45–60 s, debate entre dos vendedores (ORA 03 eléctrico vs ORA 05 HEV)",
        "aparece": "Vendedor 1 y vendedor 2",
        "gancho": "'¿ENCHUFE O NAFTA? ELLOS NO SE PONEN DE ACUERDO'",
        "gancho_b": "'NO TE COMPRES UN ELÉCTRICO SI…'",
        "guion": (
            "0–2 s: los dos vendedores, cada uno con su auto, y el gancho.\n"
            "2–6 s: \"Soy [nombre 1] y defiendo el eléctrico. Soy [nombre 2] y defiendo el híbrido. Al final te decimos cuál te conviene a vos.\"\n"
            "6–40 s: 3 rounds (ciudad, ruta, cochera). Cada uno con 1 dato verificado: ORA 03, 310 km WLTP y carga rápida 20–80 % en 36 min (oficial); ORA 05 HEV, 5,1 L/100 km mixto y no se enchufa.\n"
            "40–52 s (paga la promesa): el veredicto: 'depende de tu vida: ciudad y cochera con enchufe → el eléctrico; ruta seguido o sin cargador → el híbrido'.\n"
            "52–58 s: \"" + CTA + " Comentá ENCHUFE.\"\n"
            "Tono: discusión amable, sin bajar al otro auto (son los dos de la casa)."
        ),
        "tomas": "Plano de los dos con los autos · plano de cada uno por separado (3 tomas de cada línea clave) · enchufe · surtidor (sin marca de petrolera) · tablero de cada auto.",
        "texto": "Gancho · 'ROUND 1/2/3' · datos con su aclaración (WLTP, 'mixto declarado') · veredicto en dos líneas.",
        "descripcion": "¿Enchufe o nafta? ⚡⛽ Dos vendedores, dos autos y un veredicto: depende de tu vida. Ciudad y cochera con enchufe → eléctrico. Ruta seguido o sin cargador → híbrido. Comentá ENCHUFE y te ayudamos a elegir. Córdoba.",
        "hashtags": "#autoelectrico #hibrido #0km #GWM #AutosCordoba",
        "fijado": FIJADO.format(k="ENCHUFE"),
        "codigo": "ENCHUFE",
        "mensaje": MSG.format(k="ENCHUFE"),
    },
    {
        "id": "G17",
        "pieza": "Lo que ve este auto que vos no ves (asistencias con lluvia)",
        "formato": "Reel 35–45 s (animado con Claude o vendedor en el salón)",
        "aparece": "Vendedor 1 o animado",
        "gancho": "'CON ESTA LLUVIA, ¿VOS VES ESTO?'",
        "gancho_b": "'LO QUE VE ESTE AUTO Y VOS NO'",
        "guion": (
            "El SMN anticipa un verano más lluvioso y con tormentas más fuertes en Córdoba: esta pieza se publica una semana de lluvia.\n"
            "0–2 s: parabrisas con lluvia (grabado con el auto quieto) y el gancho.\n"
            "2–30 s: 3 asistencias, mostradas en la pantalla con el auto detenido: cámara 360, alerta de colisión, frenado autónomo, centrado de carril (las que tenga la unidad según su ficha).\n"
            "30–38 s: 'No reemplazan al que maneja: te avisan antes'.\n"
            "38–44 s: nombre del modelo + \"" + CTA + " Comentá LLUVIA.\"\n"
            "Nunca demostrar el frenado autónomo con personas ni en la calle."
        ),
        "tomas": "Lluvia sobre el parabrisas (manguera si no llueve, aclarándolo) · pantalla de la cámara 360 · luces de alerta en el espejo · vendedor explicando.",
        "texto": "Gancho · nombre de cada asistencia · 'no reemplaza al conductor'.",
        "descripcion": "Con esta lluvia, ¿vos ves todo? 🌧️ Te mostramos 3 asistencias que te avisan antes: [lista de la ficha]. No reemplazan al que maneja. Comentá LLUVIA y te mandamos precio y financiación. Córdoba.",
        "hashtags": "#seguridadvial #lluvia #0km #asistencias #AutosCordoba",
        "fijado": FIJADO.format(k="LLUVIA"),
        "codigo": "LLUVIA",
        "mensaje": MSG.format(k="LLUVIA"),
    },
    {
        "id": "G18",
        "pieza": "El vendedor responde (comentarios)",
        "formato": "Reel 30–45 s con la función 'responder comentario' de Instagram o TikTok",
        "aparece": "Vendedor 1 o 2",
        "gancho": "El comentario real en pantalla (con el permiso que da la función de responder)",
        "gancho_b": "'ME PREGUNTARON ESTO Y LA RESPUESTA SORPRENDE'",
        "guion": (
            "0–2 s: el comentario elegido de la semana (una objeción real: repuestos, reventa, carga, consumo).\n"
            "2–30 s: respuesta corta con 1 dato verificado o algo que se muestra (la unidad, el taller, el cargador).\n"
            "30–38 s: \"" + CTA + " Comentá PREGUNTA y te respondo por mensaje.\"\n"
            "Elegir el comentario el lunes. Nunca responder a un insulto ni ridiculizar al que pregunta."
        ),
        "tomas": "Vendedor a cámara al lado de la unidad o en el taller.",
        "texto": "Burbuja del comentario · dato con su fuente chica.",
        "descripcion": "Nos preguntaron: '[comentario]'. Te respondemos. Dejá tu pregunta y la contestamos en el próximo video. Comentá PREGUNTA y te escribimos por mensaje. Córdoba.",
        "hashtags": "#preguntas #0km #autos #concesionaria #AutosCordoba",
        "fijado": FIJADO.format(k="PREGUNTA"),
        "codigo": "PREGUNTA",
        "mensaje": MSG.format(k="PREGUNTA"),
    },
    {
        "id": "G19",
        "pieza": "Entregas de la semana",
        "formato": "Reel 15–25 s o Historias",
        "aparece": "Clientes que firmaron la autorización + vendedor",
        "gancho": "'ESTA SEMANA SE FUERON [N] AUTOS A [BARRIOS O CIUDADES]'",
        "gancho_b": "'EL MOMENTO QUE MÁS NOS GUSTA'",
        "guion": (
            "Solo con la autorización de imagen firmada (alcance: redes y anuncios; plazo; se puede revocar). Si un cliente la revoca, se baja.\n"
            "0–2 s: la entrega más linda de la semana con el gancho.\n"
            "2–18 s: 3 a 5 entregas cortas: llave, foto, auto saliendo. Sin patentes legibles.\n"
            "18–22 s: el cliente puede decir algo con sus palabras, nunca un texto escrito por la concesionaria. Si no quiere hablar, no habla.\n"
            "22–25 s: \"" + CTA + "\""
        ),
        "tomas": "Entrega de llaves · foto con el vendedor · auto saliendo del salón · moño o detalle (si se usa).",
        "texto": "Gancho con el número real · nombres de pila solo si el cliente lo autoriza · logo chico.",
        "descripcion": "Esta semana se fueron [N] autos a [barrios]. Gracias por elegirnos 🙌 Comentá ENTREGA y te mandamos precio y financiación. Córdoba.",
        "hashtags": "#entrega #0km #Cordoba #concesionaria #AutosCordoba",
        "fijado": FIJADO.format(k="ENTREGA"),
        "codigo": "ENTREGA",
        "mensaje": MSG.format(k="ENTREGA"),
    },
    {
        "id": "G20",
        "pieza": "Vivo del sábado desde el salón",
        "formato": "Vivo de 45–60 min en TikTok e Instagram (prueba de 4 sábados)",
        "aparece": "Vendedor 1 en cámara + vendedor 2 en el chat y el WhatsApp",
        "gancho": "Título del vivo: 'Preguntame lo que quieras de [2 modelos] · en vivo desde el salón'",
        "gancho_b": "",
        "guion": (
            "Modelo: vivos con vendedor desde el salón (caso MG Chile: 30 autos vendidos en 8 semanas con vivos, dato de la marca).\n"
            "Antes: anunciarlo en historias el jueves y el viernes. Celular en trípode, corbatero, wifi probado.\n"
            "0–5 min: saludo, qué se va a mostrar, código VIVO-SAB en pantalla.\n"
            "5–20 min: unidad 1 completa (por fuera, por dentro, cómo funciona, prueba corta en el estacionamiento si el lugar lo permite).\n"
            "20–35 min: unidad 2.\n"
            "35–50 min: preguntas del chat. Precios y cuotas solo los publicados con su vigencia; para el resto, 'te lo paso por WhatsApp'.\n"
            "Cierre: 'escribinos por WhatsApp con el código VIVO-SAB'.\n"
            "Después: el vendedor 2 escribe ese mismo día a todos los que dejaron contacto. Regla del 30/1: si en 4 vivos no hubo al menos 1 turno con el código, se deja."
        ),
        "tomas": "Plano general del vendedor con la unidad · detalles a mano · estacionamiento para la prueba corta.",
        "texto": "Cartel fijo: 'Código VIVO-SAB · WhatsApp [número]'.",
        "descripcion": "",
        "hashtags": "",
        "fijado": "",
        "codigo": "VIVO-SAB",
        "mensaje": "Hola, vengo del vivo del sábado (VIVO-SAB). Quiero precio y financiación.",
    },
    {
        "id": "G21",
        "pieza": "Video largo de YouTube: recorrido completo",
        "formato": "YouTube 6–10 min horizontal o vertical + 3 o 4 Shorts cortados de ahí",
        "aparece": "Vendedor 1",
        "gancho": "Título: '[Modelo] en Córdoba: recorrido completo y consumo real | Valparaiso Motors'",
        "gancho_b": "Título B: '¿Vale la pena el [modelo]? Lo que tenés que saber antes de comprarlo'",
        "guion": (
            "Capítulos (YouTube los muestra si están en la descripción):\n"
            "0:00 Para quién es este auto (la vida del que mira, no la ficha).\n"
            "0:40 Por fuera: medidas y llantas con la ficha.\n"
            "2:00 Por dentro: plazas, pantallas, baúl.\n"
            "4:00 Cómo funciona (modos EV, HEV, motor) con un dibujo simple.\n"
            "5:30 Manejo: prueba en ruta desde el acompañante, sin maniobras peligrosas, con consumo medido.\n"
            "7:30 Garantía (con su condición) y dónde se hace el service.\n"
            "8:30 Cómo pedir precio y financiación (sin cuotas en el video largo, salvo con el legal completo).\n"
            "Fuente: el estudio de Google y Kantar dice que los compradores usan recorridos, pruebas, comparativas y guías por versión."
        ),
        "tomas": "Las mismas del G02 en versión larga + prueba en ruta + 3 tomas del vendedor por capítulo.",
        "texto": "Capítulos · datos con aclaración · placa final con el CTA.",
        "descripcion": "Primera línea: 'Pedinos precio y financiación por WhatsApp: [link con el código YT-[MODELO]]'. Después: resumen, capítulos, datos con su aclaración (NEDC, WLTP, declarado) y 'Valparaiso Motors · Córdoba'.",
        "hashtags": "#[modelo] #Cordoba #0km (YouTube: hasta 3 en la descripción)",
        "fijado": "Pedinos precio y financiación: [link de WhatsApp con YT-[MODELO]]",
        "codigo": "YT-[MODELO]",
        "mensaje": "Hola, vengo del video de YouTube del [modelo] (YT-[MODELO]). Quiero precio y financiación.",
    },
    {
        "id": "G22",
        "pieza": "Lo más patentado del mes (dato ACARA)",
        "formato": "Reel 25–35 s animado (Claude) o placa animada",
        "aparece": "Sin personas (voz del dueño)",
        "gancho": "'ESTOS FUERON LOS AUTOS QUE MÁS SE PATENTARON EN [MES]'",
        "gancho_b": "'¿ADIVINÁS CUÁL FUE EL N.º 1?'",
        "guion": (
            "Se publica el día que sale el dato (ACARA publica el último día hábil del mes).\n"
            "0–2 s: el ranking tapado y el gancho.\n"
            "2–20 s: del 5.º al 1.º (dejar el n.º 1 para el final), con el dato de patentamientos y la fuente en pantalla.\n"
            "20–28 s: un dato de Córdoba si está publicado (en enero de 2026, Córdoba patentó 7.585).\n"
            "28–32 s: \"" + CTA + "\"\n"
            "Sin opinar sobre otras marcas: solo el dato con su fuente. Si el ranking es de otras marcas, revisar con el dueño (regla de no nombrar otras marcas en videos propios)."
        ),
        "tomas": "No hace falta grabar: se arma con el dato.",
        "texto": "Ranking con barras · 'Fuente: ACARA/DNRPA, [fecha]'.",
        "descripcion": "Estos fueron los más patentados de [mes] según ACARA/DNRPA ([link]). ¿Cuál te sorprendió? Comentá DATO y te mandamos precio y financiación de cualquiera de nuestros autos. Córdoba.",
        "hashtags": "#patentamientos #autos #0km #mercadoautomotor #AutosCordoba",
        "fijado": FIJADO.format(k="DATO"),
        "codigo": "DATO",
        "mensaje": MSG.format(k="DATO"),
    },
    {
        "id": "G23",
        "pieza": "Soy vendedor: haceme estas 3 preguntas",
        "formato": "Reel 35–45 s",
        "aparece": "Vendedor 2",
        "gancho": "'SOY VENDEDOR: ANTES DE COMPRAR, HACEME ESTAS 3 PREGUNTAS'",
        "gancho_b": "'LA TERCERA PREGUNTA ES LA QUE MÁS TE AHORRA'",
        "guion": (
            "0–2 s: el gancho.\n"
            "2–6 s: \"Soy [nombre], vendedor de Valparaiso Motors. La tercera es la que más plata te ahorra.\"\n"
            "6–15 s: 1) '¿Esta unidad está en el salón o hay que pedirla?' (y para cuándo).\n"
            "15–25 s: 2) '¿Cuánto me tomás mi usado y por cuánto tiempo vale esa tasación?'.\n"
            "25–36 s (paga la promesa): 3) '¿Cuál es el CFT?': el costo total, con gastos, seguros e impuestos, no solo la tasa.\n"
            "36–42 s: \"" + CTA + " Comentá PREGUNTAS.\""
        ),
        "tomas": "Vendedor a cámara caminando por el salón · detalle de una carpeta de cotización (sin datos reales).",
        "texto": "Gancho · 1, 2, 3 · 'CFT = costo financiero total'.",
        "descripcion": "Soy vendedor: antes de comprar un 0 km, haceme estas 3 preguntas. 1) ¿Está en el salón? 2) ¿Cuánto me tomás el usado y hasta cuándo vale? 3) ¿Cuál es el CFT? Comentá PREGUNTAS y te respondemos por mensaje. Córdoba.",
        "hashtags": "#0km #consejos #financiacion #usado #AutosCordoba",
        "fijado": FIJADO.format(k="PREGUNTAS"),
        "codigo": "PREGUNTAS",
        "mensaje": MSG.format(k="PREGUNTAS"),
    },
    {
        "id": "G24",
        "pieza": "Auto para la familia: lo que hay que mirar si llevás chicos",
        "formato": "Reel 35–45 s",
        "aparece": "Vendedor 1 (sin chicos en cámara salvo autorización de los padres)",
        "gancho": "'SI LLEVÁS CHICOS AL COLE, MIRÁ ESTO ANTES DE ELEGIR EL AUTO'",
        "gancho_b": "'3 COSAS QUE NADIE MIRA EN EL SALÓN Y IMPORTAN CON CHICOS'",
        "guion": (
            "0–2 s: el gancho con una butaca infantil al lado del auto.\n"
            "2–30 s: 3 cosas, la última la más importante: 1) espacio atrás y baúl para el cochecito; 2) ISOFIX, cómo se ve y cómo se engancha; 3) airbags y asistencias según la ficha de la unidad.\n"
            "30–36 s: nombre del modelo.\n"
            "36–42 s: \"" + CTA + " Comentá FAMILIA.\""
        ),
        "tomas": "Butaca infantil enganchándose al ISOFIX · plazas traseras · baúl con cochecito · pantalla de asistencias.",
        "texto": "Gancho · 1, 2, 3 · datos de la ficha.",
        "descripcion": "Si llevás chicos al cole, mirá esto antes de elegir el auto 👨‍👩‍👧 Espacio atrás, ISOFIX y [airbags y asistencias de la ficha]. Comentá FAMILIA y te mandamos precio y financiación. Córdoba.",
        "hashtags": "#familia #seguridad #vueltaalcole #0km #AutosCordoba",
        "fijado": FIJADO.format(k="FAMILIA"),
        "codigo": "FAMILIA",
        "mensaje": MSG.format(k="FAMILIA"),
    },
    {
        "id": "G25",
        "pieza": "Para el campo (4x4 antes de Expoagro)",
        "formato": "Reel 35–45 s en un camino de tierra (con permiso del lugar)",
        "aparece": "Vendedor 1",
        "gancho": "'¿TE QUEDASTE ENCAJADO ALGUNA VEZ EN EL CAMPO?'",
        "gancho_b": "'LO QUE TIENE QUE TENER UNA 4X4 PARA EL CAMPO DE VERDAD'",
        "guion": (
            "0–2 s: rueda en el barro o la tierra, con el gancho.\n"
            "2–30 s: 3 cosas según la ficha de la unidad en stock (verificar antes): bloqueo de diferencial trasero, modos de terreno, cámara que 've a través del piso', toma de 220 V (potencia a confirmar).\n"
            "30–36 s: consumo dicho de frente (H7: 8,1 L/100 km mixto declarado, verificar), porque da credibilidad.\n"
            "36–42 s: \"" + CTA + " Comentá CAMPO.\"\n"
            "Expoagro 2027 es del 9 al 12/3 en San Nicolás: sirve de referencia, sin usar su logo."
        ),
        "tomas": "Camino de tierra · selector de modos · pantalla de la cámara · toma de 220 V con una herramienta enchufada · vendedor a cámara.",
        "texto": "Gancho · 3 puntos · consumo con 'mixto declarado'.",
        "descripcion": "¿Te quedaste encajado alguna vez en el campo? [3 puntos de la ficha.] Consumo mixto declarado: [dato]. Comentá CAMPO y te mandamos precio y financiación. Córdoba.",
        "hashtags": "#4x4 #campo #agro #0km #AutosCordoba",
        "fijado": FIJADO.format(k="CAMPO"),
        "codigo": "CAMPO",
        "mensaje": MSG.format(k="CAMPO"),
    },
    {
        "id": "G26",
        "pieza": "Publicación semanal del Perfil de Google",
        "formato": "Publicación del Perfil de Empresa (oferta, novedad o evento)",
        "aparece": "Foto propia",
        "gancho": "Título en minúsculas normales (nada en mayúsculas sostenidas)",
        "gancho_b": "",
        "guion": (
            "Las publicaciones de oferta tuvieron más clics que las de novedades (Sterling Sky, datos de 2021 de pequeños negocios de EE. UU.). No mueven el ranking: sirven para convertir al que ya encontró el perfil.\n"
            "1) Elegir el tipo: Oferta (cuota o beneficio con su legal), Evento (inauguración, vivo) o Novedad (llegó una unidad).\n"
            "2) Foto propia con texto en la imagen (sin fotos de stock).\n"
            "3) Texto de 2–3 líneas con 'Córdoba' y el modelo.\n"
            "4) Botón: 'Llamar' o 'Más información' con el link de WhatsApp con código GBP.\n"
            "5) Subir además 5 fotos nuevas de unidades o del local."
        ),
        "tomas": "Foto horizontal 4:3 de la unidad o del local, de día.",
        "texto": "Texto en la imagen: 1 línea + logo chico.",
        "descripcion": "[2–3 líneas: qué es, para quién, hasta cuándo] + legal si hay precio o cuota.",
        "hashtags": "",
        "fijado": "",
        "codigo": "GBP",
        "mensaje": "Hola, los encontré en Google (GBP). Quiero precio y financiación.",
    },
    {
        "id": "G27",
        "pieza": "Estados de WhatsApp de la semana",
        "formato": "Estados de WhatsApp Business, 1–3 por día hábil",
        "aparece": "Fotos o videos propios",
        "gancho": "La unidad del día",
        "gancho_b": "",
        "guion": (
            "Los ven los contactos que guardaron el número (verificar). Cada respuesta a un estado abre el chat con el contexto.\n"
            "Lun: unidad que entró · Mar: detalle que nadie mira (baúl, enchufe) · Mié: placa de cuota con su legal · Jue: entrega (con autorización) · Vie: 'mañana abrimos de [..] a [..]' + cómo llegar · Sáb: lo que pasa en el salón.\n"
            "Texto: 'Respondé este estado y te mando precio y cuota'. Con cuota, el legal completo en la imagen."
        ),
        "tomas": "Fotos y videos verticales de 5–15 s.",
        "texto": "1 línea + legal si hay cuota.",
        "descripcion": "",
        "hashtags": "",
        "fijado": "",
        "codigo": "ESTADO",
        "mensaje": "",
    },
    {
        "id": "G28",
        "pieza": "Historias de la semana",
        "formato": "Historias de Instagram (y Facebook), 3–7 cuadros por día hábil",
        "aparece": "Equipo",
        "gancho": "",
        "gancho_b": "",
        "guion": (
            "Las historias no sirven para llegar a gente nueva (Mosseri): sirven para los que ya siguen y para cerrar. Por eso venden.\n"
            "Lun: stock que entró (foto + precio o cuota con legal) · Mar: detrás de escena de la grabación · Mié: encuesta '¿cuál te llevás?' entre 2 unidades · Jue: sticker de pregunta 'preguntale al vendedor' · Vie: entregas (con autorización) · Sáb: 'hoy abrimos hasta las [..]' + cómo llegar o el vivo.\n"
            "Siempre: un sticker de enlace a WhatsApp con el mensaje ya escrito y el código HISTORIA. Responder cada respuesta en menos de 5 minutos en horario.\n"
            "Compartir en historias cada reel nuevo del feed."
        ),
        "tomas": "Celular, vertical, sin edición.",
        "texto": "Zona segura de Historias: nada importante arriba de 250 px ni abajo de 340 px.",
        "descripcion": "",
        "hashtags": "",
        "fijado": "",
        "codigo": "HISTORIA",
        "mensaje": "Hola, vengo de las historias (HISTORIA). Quiero precio y financiación.",
    },
    {
        "id": "G29",
        "pieza": "Mensajes de WhatsApp de la inauguración (base con permiso)",
        "formato": "Mensaje de difusión de WhatsApp Business a clientes con permiso (opt-in)",
        "aparece": "",
        "gancho": "",
        "gancho_b": "",
        "guion": (
            "Antes: cruzar la base con el Registro No Llame y mandar solo a quien aceptó recibir mensajes. Textos listos en la guía (sección Plantillas).\n"
            "D-14 Invitación VIP: 'Hola [nombre], soy [vendedor] de Valparaiso Motors. El viernes [fecha] a las [hora] inauguramos el nuevo local en [dirección] y queremos que estés. ¿Te anotamos? Respondé SÍ y te mandamos la ubicación.'\n"
            "D-12 Aviso de mudanza a clientes de taller: último turno en el local viejo y primero en el nuevo, con el mapa.\n"
            "D-3 Recordatorio a los que dijeron SÍ.\n"
            "D-1 (mañana): ubicación, horario y estacionamiento.\n"
            "D+2 Gracias: a los que vinieron, con el link para pedir turno de prueba; a los que compraron o hicieron un service, el pedido de reseña (a todos, sin premio)."
        ),
        "tomas": "",
        "texto": "",
        "descripcion": "",
        "hashtags": "",
        "fijado": "",
        "codigo": "INAUGURACION-VIP",
        "mensaje": "",
    },
    {
        "id": "G30",
        "pieza": "Saludo de fin de año del equipo",
        "formato": "Reel 12–15 s",
        "aparece": "Todo el equipo en el local nuevo",
        "gancho": "'FELICES FIESTAS DESDE EL NUEVO VALPARAISO'",
        "gancho_b": "",
        "guion": (
            "0–2 s: el equipo completo en el salón nuevo, ya en cuadro (sin fundido desde negro).\n"
            "2–10 s: cada uno dice su nombre y área en 1 segundo (corte por persona).\n"
            "10–14 s: 'Gracias, Córdoba. Nos vemos en [mes]' + horario de las fiestas."
        ),
        "tomas": "Un plano por persona, mismo encuadre · plano grupal.",
        "texto": "Nombre y área de cada uno · horario de fiestas.",
        "descripcion": "Felices fiestas desde el nuevo Valparaiso Motors 🎄 Horario de fiestas: [..]. Córdoba.",
        "hashtags": "#felicesfiestas #Cordoba #concesionaria #equipo #AutosCordoba",
        "fijado": "Horario de fiestas: [..]",
        "codigo": "",
        "mensaje": "",
    },
    {
        "id": "G31",
        "pieza": "¿Cuánto dura la batería?",
        "formato": "Reel 35–45 s (vendedor o animado con Claude)",
        "aparece": "Vendedor 2",
        "gancho": "'¿Y CUANDO LA BATERÍA SE GASTA, QUÉ?'",
        "gancho_b": "'LA PREGUNTA QUE FRENA A TODOS LOS QUE QUIEREN UN HÍBRIDO'",
        "guion": (
            "0–2 s: el gancho con la tapa de carga o el tablero de batería.\n"
            "2–6 s: 'Al final te digo lo que dice la garantía, que es lo que importa'.\n"
            "6–25 s: cómo se cuida una batería (cargas, temperatura) en lenguaje simple, sin números que no estén en una fuente.\n"
            "25–35 s (paga la promesa): la garantía de batería con su condición exacta (ej.: Eado Plus, 8 años o 150.000 km, lo que ocurra primero).\n"
            "35–42 s: \"" + CTA + " Comentá BATERIA.\""
        ),
        "tomas": "Tapa de carga · cargador · pantalla de energía · vendedor a cámara.",
        "texto": "Gancho · garantía en grande con su condición en chico.",
        "descripcion": "¿Y cuando la batería se gasta, qué? 🔋 Te contamos cómo se cuida y qué cubre la garantía ([garantía exacta, 'lo que ocurra primero']). Comentá BATERIA y te mandamos precio y financiación. Córdoba.",
        "hashtags": "#bateria #hibridoenchufable #autoelectrico #garantia #AutosCordoba",
        "fijado": FIJADO.format(k="BATERIA"),
        "codigo": "BATERIA",
        "mensaje": MSG.format(k="BATERIA"),
    },
    {
        "id": "G32",
        "pieza": "Un día en Valparaiso (detrás de escena)",
        "formato": "Reel 25–35 s, estilo diario",
        "aparece": "Equipo",
        "gancho": "EP. 1: 'ASÍ SE PREPARA UN AUTO ANTES DE ENTREGARLO' · EP. 2: 'LO QUE PASA EN EL TALLER A LAS 8 DE LA MAÑANA'",
        "gancho_b": "'NADIE VE ESTA PARTE'",
        "guion": (
            "0–2 s: el momento más visual (el auto con lona, el lavado, el elevador) y el gancho.\n"
            "2–25 s: 6 a 10 pasos reales, uno por corte de 2–3 s, con una etiqueta por paso ('control de 100 puntos', 'carga de batería', 'tutorial de CarPlay').\n"
            "25–32 s: el auto listo y 'mañana se lo lleva [nombre de pila, con autorización]' o 'mañana se entrega'.\n"
            "CTA chico al final: \"" + CTA + "\""
        ),
        "tomas": "Cada paso de la preparación o del taller, 3–5 s, desde 2 ángulos.",
        "texto": "Gancho · etiqueta por paso · logo chico.",
        "descripcion": "Así se prepara un auto antes de entregarlo en Valparaiso Motors, Córdoba. [Pasos reales.] Comentá ENTREGA y te mandamos precio y financiación.",
        "hashtags": "#detrasdeescena #entrega #0km #taller #AutosCordoba",
        "fijado": FIJADO.format(k="ENTREGA"),
        "codigo": "ENTREGA",
        "mensaje": MSG.format(k="ENTREGA"),
    },
    {
        "id": "G33",
        "pieza": "Carrusel educativo (plantilla)",
        "formato": "Carrusel 1080x1350, 8 a 10 placas",
        "aparece": "Fotos propias o placas de texto",
        "gancho": "Portada para todo público: una pregunta sobre la vida del que mira (el tema de cada semana está en el Calendario)",
        "gancho_b": "Portada B: el número o la promesa ('5 preguntas…', 'lo que nadie te dice de…')",
        "guion": (
            "Placa 1: portada con la pregunta en Inter Black, foto propia, 'deslizá →'.\n"
            "Placas 2 a 8: un punto por placa, de lo menos a lo más importante (el último es el mejor y se anuncia en la portada). Una idea y una foto por placa; datos con su aclaración chica.\n"
            "Placa 9: resumen en 3 líneas (para guardar).\n"
            "Placa 10: CTA: 'Pedinos precio y financiación de cualquiera de nuestros autos' + 'comentá [PALABRA]' + logo chico (versión negra sobre claro).\n"
            "Estilo: fondo papel o estudio blanco; bordó como placa con letras blancas; 'deslizá →' en todas menos la última.\n"
            "Si muestra cuotas, cada placa con cuota lleva el legal completo."
        ),
        "tomas": "Fotos propias de las unidades y del local (mismo fondo, misma luz).",
        "texto": "Máximo 20 palabras por placa.",
        "descripcion": "[Primera línea = la pregunta de la portada, sin adelantar el final] Guardalo para cuando cambies el auto. Comentá [PALABRA] y te mandamos precio y financiación. Córdoba.",
        "hashtags": "#[tema] #0km #consejos #autos #AutosCordoba",
        "fijado": FIJADO.format(k="[PALABRA]"),
        "codigo": "[PALABRA]",
        "mensaje": "Hola, vengo del carrusel ([PALABRA]). Quiero precio y financiación.",
    },
    {
        "id": "G34",
        "pieza": "Antes de salir a la ruta: lo que revisa el taller",
        "formato": "Reel 30–40 s con un técnico",
        "aparece": "Técnico o jefe de taller",
        "gancho": "'¿SALÍS DE VACACIONES? ESTO ES LO QUE REVISARÍA UN TÉCNICO'",
        "gancho_b": "'5 COSAS QUE TENÉS QUE MIRAR ANTES DE IR A LAS SIERRAS'",
        "guion": (
            "0–2 s: el técnico con el capó abierto y el gancho.\n"
            "2–6 s: \"Soy [nombre], del taller de Valparaiso Motors. La quinta es la que más se olvida.\"\n"
            "6–30 s: 5 controles, de a uno, con la mano señalando: presión y estado de cubiertas (con la de auxilio), luces, frenos, líquidos, y la quinta: [la que el técnico diga que más se olvida, ej. escobillas o batería de 12 V].\n"
            "30–38 s: 'Si tu auto es de la casa, pedí turno de service antes de viajar' (botón dentro del WhatsApp) y el CTA único: \"" + CTA + "\""
        ),
        "tomas": "Manómetro en la cubierta · luces encendidas · disco de freno · varilla de aceite · el quinto control · técnico a cámara.",
        "texto": "Gancho · 1 a 5 con 'pop' · 'Mandáselo a quien sale a la ruta'.",
        "descripcion": "¿Salís de vacaciones? 5 cosas que revisaría un técnico antes de ir a las sierras: [lista]. Mandáselo a quien sale a la ruta. Si tu auto es de la casa, escribinos con el código RUTA y te damos turno de service. Córdoba.",
        "hashtags": "#vacaciones #ruta #service #Cordoba #AutosCordoba",
        "fijado": "Mandáselo a quien sale a la ruta este verano. Turnos de service por WhatsApp (link en la bio).",
        "codigo": "RUTA",
        "mensaje": "Hola, vengo del video del taller (RUTA). Quiero un turno de service.",
    },
]
