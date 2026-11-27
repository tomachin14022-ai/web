"""Datos verificados para los guiones (investigación del 26/11/2026).

DATOS: un dato por fila, con la frase para decir en cámara, el tipo de dato y la fuente.
CUENTAS: las cuentas de Córdoba con sus supuestos. La planilla las arma con fórmulas, así se actualizan
cambiando el precio de la nafta o de la luz en la hoja "Cuentas de Córdoba".
ERRORES: lo que hay que corregir en la web, Mercado Libre y las redes antes de publicar.
Notas completas, con todos los links: research_notes/Guiones con datos reales/.
"""

# Tipos de dato (cómo se dice en pantalla)
MARCA = "Oficial (según la marca)"
MEDIDO = "Medido por la prensa"
PRENSA = "Declarado (dato de la marca en la prensa)"
CUENTA = "Cuenta propia (decir 'estimado')"
PRECIO = "Precio (confirmar el día que se publica)"
OTRO = "Otro mercado (no usar sin confirmar)"
FALTA = "Sin fuente: NO decirlo"

FT_EADO = "https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf"
FT_DEEPAL = "https://deepal.com.ar/s05/DEEPAL-FT.pdf"
FT_CS55 = "https://changan.com.ar/FT%20-%20Changan%20-%20CS55%20PLUS%20PHEV.pdf"
FT_L200 = "https://www.mitsubishi-motors.com.ar/Brochure_L200_digital.pdf"
LN_EADO = "https://www.lanacion.com.ar/autos/asi-anda-el-changan-eado-un-sedan-chino-que-promete-1000km-de-autonomia-nid19112026/"
PB_ORA03 = "https://parabrisas.perfil.com/noticias/test/chino-y-ciento-por-ciento-electrico-probamos-el-gwm-ora-03.phtml"
V16_ORA03 = "https://www.16valvulas.com.ar/lanzamiento-gwm-ora-03-100-electrico-desde-us-31-000/"
AC_ORA05 = "https://noticias.autocosmos.com.ar/2026/08/25/gwm-ora-5-hev-lanzamiento-y-precio-en-argentina"
PB_ORA05 = "https://parabrisas.perfil.com/noticias/autos/prueba-de-manejo-test-ora-5-hev-suv-chino-great-wall-motors.phtml"
AC_H6 = "https://noticias.autocosmos.com.ar/2026/06/12/haval-h6-pro-hev-lanzamiento-y-precio-en-argentina"
CAT_H6 = "https://www.autocosmos.com.ar/catalogo/2026/haval/h6-pro-hev/pro/169852"
V16_H6 = "https://www.16valvulas.com.ar/?p=247137"
AC_H7 = "https://noticias.autocosmos.com.ar/2026/09/24/gwm-haval-h7-lanzamiento-y-precio-en-argentina"
V16_H7 = "https://www.16valvulas.com.ar/?p=249901"
AT_JOLION = "https://autotest.com.ar/pruebas/haval-jolion-hev-test-drive/"
V16_JOLION = "https://www.16valvulas.com.ar/test-drive-gwm-haval-jolion-hev-supreme/"
V16_TANK = "https://www.16valvulas.com.ar/?p=239482"
AT_POER = "https://autotest.com.ar/noticias/pick-ups-chinas-en-argentina-2026-todas-las-marcas-modelos-versiones-y-precios/"
PB_CS55 = "https://parabrisas.perfil.com/noticias/test/como-es-el-suv-mediano-hibrido-encufable-mas-barato-de-la-argentina.phtml"
AT_CS55 = "https://autotest.com.ar/pruebas/changan-cs55-plus-suv-test-drive/"
PB_JMEV = "https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml"
WEB_JMEV = "https://jmevargentina.com.ar/"
WEB_L200 = "https://www.mitsubishi-motors.com.ar/vehicles/l200"
PB_L200 = "https://parabrisas.perfil.com/noticias/test/probamos-la-nueva-mitsubishi-l200.phtml"
FT_OUT = "https://www.mitsubishi-motors.com.ar/ft_outlander.pdf"
FIN_DEEPAL = "https://deepal.com.ar/financiacion"
IPRO_PHEV = "https://www.iprofesional.com/autos/463341-las-complejidades-de-autos-y-suv-hibridos-que-muchos-desconocen"
IPRO_CLAUSURA = "https://www.iprofesional.com/autos/468479-clausuran-concesionarias-de-autos-por-practicas-abusivas-los-argumentos"
LN_POSVENTA = "https://www.lanacion.com.ar/autos/como-sera-la-postventa-de-los-autos-chinos-en-la-argentina-nid23042026/"
V16_BRASIL = "https://www.16valvulas.com.ar/es-oficial-great-wall-inicio-la-produccion-en-la-planta-brasilena-de-iracemapolis-y-acelera-su-plan-industrial-para-la-region/"
AW_AUXILIO = "https://www.autoweb.com.ar/2025/09/24/sin-auxilio-el-problema-que-traen-varios-nuevos-modelos-chinos/"
V16_TRIFASICA = "https://www.16valvulas.com.ar/acelerando-la-electrificacion-general-motors-y-weg-amplian-su-alianza-para-impulsar-la-carga-de-vehiculos-electricos-en-argentina/"
CHANGAN_API = "https://changan.com.ar/api/config"
HOYDIA = "https://hoydia.com.ar/economia/combustibles-cordoba-nafta-gnc-4/"
EPEC = "https://www.epec.com.ar/docs/cuadro-tarifario/CT_Resumido_publicado-30102026-aplicacion-011126.pdf"
ERSEP = "https://ersep.cba.gov.ar/tarifas-peajes-de-la-rac-a-partir-del-08-10-2026-empresa-caminos-de-las-sierras/"
PMUS = "https://www.mobiliseyourcity.net/sites/default/files/2025-10/PMUS%20Cordoba.pdf"
CODIGO_EDIF = "https://documentos.cordoba.gob.ar/MUNCBA/AreasGob/Desurb/CodigodeEdificacion.pdf"
CAFE = "https://www.cadena3.com/noticia/desayuno-de-juntos/brecha-de-precios-tomar-un-cafe-en-cordoba-cuesta-lo-mismo-que-en-paris-y-el-doble-que-en-san-pablo_599565"
GEF = "https://www.gefinforma.com/los-punto-de-cargas-de-la-epec/"
ML_EADO = "https://auto.mercadolibre.com.ar/MLA-2276232041-changan-eado-plus-phev-2027-_JM"

# (id, modelo, dato, frase para decir en cámara, tipo, fuente, link, fecha de la fuente, ojo)
DATOS = [
    # ---------------- Changan Eado Plus PHEV ----------------
    ("EADO-1", "Changan Eado Plus PHEV", "Autonomía eléctrica", "Lo cargás en tu casa y, según la marca, hace hasta 132 km sin usar nafta.", MARCA, "Ficha técnica oficial", FT_EADO, "03/08/2026", "En pantalla: 'HASTA 132 KM · ciclo NEDC, de laboratorio'. Nadie en la prensa argentina lo midió: ver E25."),
    ("EADO-2", "Changan Eado Plus PHEV", "Motores", "Tiene dos motores: uno a nafta de 101 caballos y uno eléctrico de 212.", MARCA, "Ficha técnica oficial", FT_EADO, "03/08/2026", "No decir '215 cv' (error del aviso de Mercado Libre) ni sumar las dos potencias: la marca no declara la combinada."),
    ("EADO-3", "Changan Eado Plus PHEV", "Asistente de voz", "Le hablás en español y te abre las ventanillas, el techo y te prende el aire.", MARCA, "Ficha técnica oficial", FT_EADO, "03/08/2026", "Que entienda la tonada cordobesa no tiene fuente: se muestra lo que pase en la prueba (E12)."),
    ("EADO-4", "Changan Eado Plus PHEV", "Consumo a nafta medido", "Cuando anda a nafta, La Nación midió 5,7 litros cada 100 km en ciudad.", MEDIDO, "La Nación", LN_EADO, "19/11/2026", "Medición de uso mayormente urbano."),
    ("EADO-5", "Changan Eado Plus PHEV", "Largo", "Mide 4,77 metros: es más largo que la Deepal S05, que es una SUV (4,62 m).", MARCA, "Fichas oficiales Eado y Deepal", FT_EADO, "03/08/2026", "Decir 'más largo', no 'más espacio': el Deepal tiene más distancia entre ejes (2,88 contra 2,765 m)."),
    ("EADO-6", "Changan Eado Plus PHEV", "Baúl", "Tiene un baúl de 500 litros.", PRENSA, "Autotest", "https://autotest.com.ar/noticias/cuesta-menos-de-30-000-dolares-y-tiene-212-cv-asi-es-el-nuevo-sedan-hibrido-rival-de-toyota-corolla/", "29/09/2026", "No está en la ficha oficial: medirlo con valijas en el salón (E06)."),
    ("EADO-7", "Changan Eado Plus PHEV", "Cámara", "La cámara 360 también graba lo que pasa adelante, como una dashcam.", MARCA, "Ficha técnica oficial", FT_EADO, "03/08/2026", "No decir 'cámara de retroceso' (error del aviso de Mercado Libre): es 360."),
    ("EADO-8", "Changan Eado Plus PHEV", "Seguridad", "Si te distraés, frena solo: trae frenado autónomo de emergencia y 6 airbags.", MARCA, "Ficha técnica oficial", FT_EADO, "03/08/2026", "Nunca demostrar el frenado en la calle."),
    ("EADO-9", "Changan Eado Plus PHEV", "Detalles de confort", "El apoyabrazos de adelante enfría, y el auto se puede prender a distancia desde la llave.", MARCA, "Ficha técnica oficial", FT_EADO, "03/08/2026", "Probarlo en la unidad antes de filmarlo."),
    ("EADO-10", "Changan Eado Plus PHEV", "Rueda de auxilio", "No tiene rueda de auxilio.", MEDIDO, "La Nación (contra en la prueba)", LN_EADO, "19/11/2026", "Es la limitación honesta del Eado. Mostrar qué trae en su lugar (kit) y qué asistencia da la marca: verificar."),
    ("EADO-11", "Changan Eado Plus PHEV", "Carga", "Acepta carga en corriente alterna hasta 7,4 kW.", MARCA, "Ficha técnica oficial", FT_EADO, "03/08/2026", "La ficha no da el tiempo de carga ni si trae cargador para enchufe común: verificar con la unidad."),
    ("EADO-12", "Changan Eado Plus PHEV", "Garantía", "5 años o 150.000 km el auto, y 8 años o 150.000 km el sistema híbrido.", PRENSA, "16 Válvulas (preventa)", "https://www.16valvulas.com.ar/nuevo-changan-eado-plus-phev-preventa-en-argentina-desde-us-29-990/", "14/08/2026", "Confirmar con Changan antes de decirlo: no se reverificó en la web oficial."),
    ("EADO-13", "Changan Eado Plus PHEV", "Precio de lista", "Precio sugerido de la marca: USD 29.990.", PRECIO, "changan.com.ar y La Nación", "https://changan.com.ar/modelos/eado-plus", "26/11/2026", "Valparaiso lo publica a US$27.800 en Mercado Libre. En la placa va el precio en pesos del día."),
    ("EADO-X", "Changan Eado Plus PHEV", "Autonomía total '995 km'", "—", FALTA, "No aparece en la web ni en la ficha oficial argentina", "https://changan.com.ar/modelos/eado-plus", "26/11/2026", "Sacar '995 km' de todos los guiones. Si hace falta: 'si se acaba la batería, sigue a nafta como un híbrido'."),
    # ---------------- Deepal S05 ----------------
    ("DEEPAL-1", "Deepal S05 PHEV", "Cámara 540°", "Su cámara te muestra lo que hay debajo del auto, como si el piso fuera transparente.", MARCA, "Ficha técnica oficial", FT_DEEPAL, "30/09/2026", ""),
    ("DEEPAL-2", "Deepal S05 PHEV", "Motores", "El motor eléctrico tiene 218 caballos; el de nafta, 86.", MARCA, "Ficha técnica oficial", FT_DEEPAL, "30/09/2026", ""),
    ("DEEPAL-3", "Deepal S05 PHEV", "Autonomía y carga", "Según la marca, hace 100 km o más en eléctrico y se carga en 6 horas o menos.", MARCA, "Ficha técnica oficial", FT_DEEPAL, "30/09/2026", "En pantalla: 'ciclo LEV2, declarado · carga en corriente alterna de 6,6 kW'."),
    ("DEEPAL-4", "Deepal S05 PHEV", "Garantía", "7 años de garantía el auto y 8 años o 150.000 km la batería.", MARCA, "Ficha técnica oficial (p. 2 y 5)", FT_DEEPAL, "30/09/2026", "La ficha dice 200.000 km para el auto y la prensa dijo 150.000: confirmar con Deepal y decir los km del dato confirmado."),
    ("DEEPAL-5", "Deepal S05 PHEV", "Pantalla", "Tiene una pantalla de 15,4 pulgadas.", MARCA, "Ficha técnica oficial", FT_DEEPAL, "30/09/2026", "'Más grande que muchas notebooks' es una comparación nuestra."),
    ("DEEPAL-6", "Deepal S05 PHEV", "Diseño", "Las puertas no tienen marco y las manijas están escondidas.", MARCA, "Ficha técnica oficial", FT_DEEPAL, "30/09/2026", ""),
    ("DEEPAL-7", "Deepal S05 PHEV", "Auxilio", "Trae kit de reparación de pinchazos, no rueda de auxilio.", MARCA, "Ficha técnica oficial", FT_DEEPAL, "30/09/2026", "Limitación honesta del S05."),
    ("DEEPAL-8", "Deepal S05 PHEV", "Financiación de ejemplo", "La financiación dice 0 % de tasa, pero el costo financiero total arranca en 43,72 %, porque incluye el seguro.", PRECIO, "deepal.com.ar/financiacion", FIN_DEEPAL, "26/11/2026", "Válido 'para las operaciones solicitadas en el día de hoy'. Para el video D21, sin nombrar el banco; mostrar el legal."),
    ("DEEPAL-9", "Deepal S05 PHEV", "Tapizado", "El tapizado es de tela y el climatizador es de una zona.", MARCA, "Ficha técnica oficial", FT_DEEPAL, "30/09/2026", "Dato honesto para la reseña: no es cuero."),
    # ---------------- Changan CS55 Plus PHEV ----------------
    ("CS55-1", "Changan CS55 Plus PHEV", "Consumo medido sin cargar", "En ciudad, Parabrisas midió casi 22 km por litro sin cargarlo nunca.", MEDIDO, "Parabrisas", PB_CS55, "26/02/2026", "21,7 km/l en ciudad sin recargar."),
    ("CS55-2", "Changan CS55 Plus PHEV", "Aceleración medida", "Es una SUV familiar que llegó a 100 en 7,6 segundos.", MEDIDO, "Parabrisas", PB_CS55, "26/02/2026", "En modo Sport. Autotest midió 8,1–8,2 s."),
    ("CS55-3", "Changan CS55 Plus PHEV", "Consumo urbano medido", "Autotest midió 4,5 litros cada 100 km en ciudad.", MEDIDO, "Autotest", AT_CS55, "25/06/2026", "La nota no aclara el estado de la batería."),
    ("CS55-4", "Changan CS55 Plus PHEV", "Autonomía total", "La marca declara 1.215 km con el tanque y la batería llenos; La Nación hizo unos 870 km reales.", MEDIDO, "changan.com.ar y La Nación", "https://www.lanacion.com.ar/autos/suv-hibrido-enchufable-vs-naftero-cuanto-se-ahorra-en-tres-anos-de-uso-en-la-argentina-nid18062026/", "18/06/2026", "Decir los dos números: el declarado y el medido."),
    ("CS55-5", "Changan CS55 Plus PHEV", "Modo REEV", "Tiene un modo en el que el motor a nafta no mueve las ruedas: solo carga la batería.", MARCA, "Ficha técnica oficial", FT_CS55, "18/11/2025", ""),
    ("CS55-6", "Changan CS55 Plus PHEV", "Baúl", "Tiene un baúl de 475 litros.", PRENSA, "Autotest", AT_CS55, "25/06/2026", ""),
    ("CS55-7", "Changan CS55 Plus PHEV", "Auxilio y reventa", "No tiene rueda de auxilio, y la prensa marcó el valor de reventa como punto en contra.", MEDIDO, "Parabrisas y Autotest", AT_CS55, "2026", "Limitación honesta."),
    ("CS55-8", "Changan CS55 Plus PHEV", "Precio de lista", "Precio sugerido de la marca: USD 31.990.", PRECIO, "changan.com.ar", "https://changan.com.ar/modelos/cs55", "26/11/2026", "Valparaiso lo publica a US$29.399."),
    # ---------------- JMEV Easy 3 ----------------
    ("JMEV-1", "JMEV Easy 3", "Wallbox", "Viene con el cargador de pared de regalo; la instalación la pagás vos.", PRECIO, "jmevargentina.com.ar", WEB_JMEV, "26/11/2026", "Promo: confirmar el día."),
    ("JMEV-2", "JMEV Easy 3", "Autonomía real", "La marca dice 330 km, pero en una prueba real hizo unos 285.", MEDIDO, "Parabrisas", PB_JMEV, "09/07/2026", "330 km es ciclo CLTC (chino)."),
    ("JMEV-3", "JMEV Easy 3", "Consumo en ciudad", "En ciudad hace 11 km con cada kWh.", MEDIDO, "Parabrisas", PB_JMEV, "09/07/2026", "En avenidas y autopistas, 7,9 km por kWh."),
    ("JMEV-4", "JMEV Easy 3", "Tamaño", "Mide 3,72 metros: entra en cualquier cochera.", PRENSA, "Parabrisas", PB_JMEV, "09/07/2026", ""),
    ("JMEV-5", "JMEV Easy 3", "Arranque", "Sale de 0 a 50 en 4,5 segundos.", MARCA, "Ficha técnica", "https://www.16valvulas.com.ar/wp-content/uploads/2025/10/FT-Easy-3_compressed.pdf", "10/2025", "No hacer picadas en la calle."),
    ("JMEV-6", "JMEV Easy 3", "Cámara", "Trae cámara 360.", PRENSA, "Parabrisas", PB_JMEV, "09/07/2026", "'Algo raro a este precio' es opinión."),
    ("JMEV-7", "JMEV Easy 3", "Garantía", "3 años o 100.000 km el auto; 8 años o 120.000 km la batería.", PRENSA, "Parabrisas y La Nación", PB_JMEV, "2026", ""),
    ("JMEV-8", "JMEV Easy 3", "Para quién no es", "Es un auto de ciudad: atrás viajan cómodos 2, y en ruta se siente chico.", MEDIDO, "Parabrisas (contras de la prueba)", PB_JMEV, "09/07/2026", "Limitación honesta."),
    ("JMEV-9", "JMEV Easy 3", "Precio", "Valparaiso lo publica a US$17.899 o $27.899.000.", PRECIO, "Mercado Libre", "https://autos.mercadolibre.com.ar/jmev/_PciaId_cordoba", "26/11/2026", "'El 0 km más barato del país' cambia con cada lista: decir 'uno de los 0 km más baratos' o verificar el día."),
    # ---------------- GWM ORA 03 ----------------
    ("ORA03-1", "GWM ORA 03", "Autonomía", "Con la batería llena puede hacer hasta 310 km en el ensayo de laboratorio WLTP.", MARCA, "16 Válvulas (lanzamiento)", V16_ORA03, "16/05/2025", ""),
    ("ORA03-2", "GWM ORA 03", "Autonomía medida", "En la prueba de Parabrisas hizo unos 285 km por carga.", MEDIDO, "Parabrisas", PB_ORA03, "19/05/2026", ""),
    ("ORA03-3", "GWM ORA 03", "Carga rápida", "En un cargador rápido pasa del 10 al 80 % en unos 40 minutos.", MARCA, "Parabrisas e iProfesional", PB_ORA03, "2026", "Corrige el '20 → 80 % en 36 min' del guion anterior."),
    ("ORA03-4", "GWM ORA 03", "Garantía", "7 años o 150.000 km el auto; 8 años o 150.000 km la batería, lo que ocurra primero.", MARCA, "16 Válvulas y Parabrisas", V16_ORA03, "2025–2026", "Resuelve el 'verificar' del CLAUDE.md: 7 años. Confirmar que siga vigente."),
    ("ORA03-5", "GWM ORA 03", "Airbag central", "Tiene 7 airbags, uno entre los dos asientos de adelante.", MARCA, "16 Válvulas", V16_ORA03, "16/05/2025", "Para qué sirve el central es explicación nuestra."),
    ("ORA03-6", "GWM ORA 03", "Frenado", "Puede frenar solo si detecta un peatón, un ciclista o un auto que cruza en una esquina.", MARCA, "16 Válvulas", V16_ORA03, "16/05/2025", "Nunca demostrarlo en la calle."),
    ("ORA03-7", "GWM ORA 03", "Aceleración", "Llega de 0 a 100 en 8,6 segundos.", MARCA, "Parabrisas", PB_ORA03, "19/05/2026", ""),
    # ---------------- GWM ORA 05 HEV ----------------
    ("ORA05-1", "GWM ORA 05 HEV", "Potencia", "Tiene dos motores, uno a nafta y uno eléctrico, que juntos dan 223 caballos.", MARCA, "Autocosmos", AC_ORA05, "25/08/2026", ""),
    ("ORA05-2", "GWM ORA 05 HEV", "Aceleración", "Llega de 0 a 100 en 7,7 segundos según la marca; en la prueba de Parabrisas marcó 7,8.", MEDIDO, "Autocosmos y Parabrisas", PB_ORA05, "2026", ""),
    ("ORA05-3", "GWM ORA 05 HEV", "Consumo", "Gasta 5,1 litros cada 100 km en uso mixto según la marca; Parabrisas midió 17 km por litro.", MEDIDO, "Autocosmos y Parabrisas", PB_ORA05, "2026", ""),
    ("ORA05-4", "GWM ORA 05 HEV", "Frenado medido", "Yendo a 100 km/h, frenó por completo en 42,2 metros.", MEDIDO, "Parabrisas", PB_ORA05, "10/11/2026", "Mostrarlo con una animación, nunca en la calle."),
    ("ORA05-5", "GWM ORA 05 HEV", "No se enchufa", "No se enchufa nunca: su batería es chiquita (1,09 kWh) y se carga sola.", MARCA, "Autocosmos", AC_ORA05, "25/08/2026", ""),
    ("ORA05-6", "GWM ORA 05 HEV", "Techo", "El techo es de vidrio y mide 1,65 m², más que una puerta de casa.", MARCA, "Autocosmos", AC_ORA05, "25/08/2026", "La comparación con la puerta (~2 × 0,8 m) es nuestra."),
    ("ORA05-7", "GWM ORA 05 HEV", "Garantía", "7 años o 150.000 km el auto, y 8 años o 150.000 km la batería.", MARCA, "Autocosmos", AC_ORA05, "25/08/2026", ""),
    # ---------------- Haval H6 PRO HEV ----------------
    ("H6-1", "Haval H6 PRO HEV", "Consumo ciudad y ruta", "Según la marca, en la ciudad gasta menos que en la ruta: 4,3 litros cada 100 km contra 5,8.", MARCA, "Catálogo Autocosmos", CAT_H6, "2026", ""),
    ("H6-2", "Haval H6 PRO HEV", "Potencia", "Suma 243 caballos entre el motor a nafta y el eléctrico.", MARCA, "Autocosmos", AC_H6, "12/06/2026", ""),
    ("H6-3", "Haval H6 PRO HEV", "Batería", "Su batería es de 1,76 kWh, unas 27 veces más chica que la de un eléctrico como el ORA 03; por eso nunca se enchufa.", CUENTA, "Autocosmos (48 ÷ 1,76)", AC_H6, "12/06/2026", "Decir 'unas 27 veces' como estimado."),
    ("H6-4", "Haval H6 PRO HEV", "Butacas", "Las butacas de adelante calientan en invierno y ventilan en verano.", MARCA, "Autocosmos", AC_H6, "12/06/2026", ""),
    ("H6-5", "Haval H6 PRO HEV", "Head-up y pantalla", "Te proyecta la velocidad en el parabrisas y tiene una pantalla de 14,6 pulgadas.", MARCA, "Autocosmos y 16 Válvulas", V16_H6, "2026", ""),
    ("H6-6", "Haval H6 PRO HEV", "Marcha atrás", "Si das marcha atrás y viene un auto de costado, frena solo.", MARCA, "16 Válvulas", V16_H6, "2026", "Mostrarlo en el estacionamiento, con un auto del concesionario y sin riesgo."),
    ("H6-7", "Haval H6 PRO HEV", "Garantía", "7 años o 150.000 km el auto; 8 años o 150.000 km el sistema híbrido.", PRENSA, "16 Válvulas", "https://www.16valvulas.com.ar/nueva-haval-h6-pro-hev-lanzamiento-en-argentina-desde-us-35-500/", "12/06/2026", ""),
    ("H6-8", "Haval H6 PRO HEV", "CESVI", "CESVI eligió al H6 como el SUV grande más seguro de Argentina.", PRENSA, "Autocosmos", AC_H6, "12/06/2026", "Verificar año y versión antes de decirlo."),
    # ---------------- Haval H7 ----------------
    ("H7-1", "Haval H7", "Cámara", "Tiene una cámara que muestra lo que hay debajo del auto, como si el piso fuera transparente.", MARCA, "16 Válvulas", V16_H7, "24/09/2026", "Las dos versiones."),
    ("H7-2", "Haval H7", "4x4", "La 4x4 tiene un botón que traba las ruedas de atrás para salir del barro, y 8 modos para cada terreno.", MARCA, "Autocosmos y 16 Válvulas", AC_H7, "24/09/2026", "Solo la 2.0T 4WD. Confirmar la versión de la unidad."),
    ("H7-3", "Haval H7", "Toma de 220 V", "Tiene un enchufe de 220 V como el de tu casa.", MARCA, "16 Válvulas", V16_H7, "24/09/2026", "No decir ni mostrar qué se enchufa (nada de amoladoras) hasta tener la potencia de la toma."),
    ("H7-4", "Haval H7", "Precio 4x4 contra híbrida", "La 4x4 a nafta sale US$1.000 menos que la híbrida: US$36.900 contra US$37.900.", PRECIO, "Autocosmos", AC_H7, "24/09/2026", "Precio de lista del lanzamiento: confirmar el día."),
    ("H7-5", "Haval H7", "Consumo", "La híbrida gasta 4,3 litros cada 100 km en ciudad y la 4x4 a nafta 8,1 en uso mixto.", MARCA, "Autocosmos", AC_H7, "24/09/2026", "Decirlo de frente: 8,1 es lo honesto de la 4x4."),
    ("H7-6", "Haval H7", "Medidas", "Mide 4,80 m y tiene casi 3 metros (2,93 m) entre las ruedas de adelante y las de atrás.", MARCA, "16 Válvulas", V16_H7, "24/09/2026", ""),
    ("H7-7", "Haval H7", "Detalles", "Carga el celular sin cable a 50 W y lleva la rueda de auxilio colgada atrás, como los todoterreno.", MARCA, "Autocosmos", AC_H7, "24/09/2026", ""),
    ("H7-8", "Haval H7", "Potencia y garantía", "La 2.0 turbo 4x4 tiene 228 CV y la híbrida 243 CV; las dos con 7 años o 150.000 km de garantía.", MARCA, "Autocosmos y Parabrisas", AC_H7, "24/09/2026", "Corrige el '228 o 243, verificar' del CLAUDE.md: son dos versiones."),
    # ---------------- Haval Jolion HEV ----------------
    ("JOLION-1", "Haval Jolion HEV", "Precio", "Es el híbrido más barato de la marca: US$28.990 de lista en noviembre de 2026.", PRECIO, "Autotest", AT_JOLION, "18/11/2026", "Valparaiso aparece a US$28.450 en Mercado Libre. Confirmar el día."),
    ("JOLION-2", "Haval Jolion HEV", "Consumo en ruta", "En la prueba de Autotest gastó 6,5 litros cada 100 km a 100 km/h.", MEDIDO, "Autotest", AT_JOLION, "18/11/2026", ""),
    ("JOLION-3", "Haval Jolion HEV", "Autonomía", "Con un tanque de 55 litros, Autotest calculó unos 800 km.", MEDIDO, "Autotest", AT_JOLION, "18/11/2026", "Cálculo de la prensa."),
    ("JOLION-4", "Haval Jolion HEV", "Equipamiento", "Trae 6 airbags, cámara 360 y un crucero que frena y acelera solo según el auto de adelante.", MARCA, "Autotest", AT_JOLION, "18/11/2026", ""),
    ("JOLION-5", "Haval Jolion HEV", "Ciudad contra ruta", "En ciudad gastó 7 litros cada 100 km, más que en la ruta.", MEDIDO, "Autotest", AT_JOLION, "18/11/2026", "Limitación honesta: en otra prueba (16 Válvulas) dio 6,1 en ciudad y 6,6 a 100 km/h."),
    ("JOLION-6", "Haval Jolion HEV", "Auxilio", "No trae rueda de auxilio, ni siquiera temporal: trae kit de pinchaduras.", MEDIDO, "16 Válvulas", V16_JOLION, "20/10/2026", ""),
    # ---------------- Tank 300 y Poer ----------------
    ("TANK-1", "GWM Tank 300", "Garantía de motor y caja", "El motor y la caja tienen garantía por 10 años o un millón de kilómetros.", MARCA, "16 Válvulas y La Nación", V16_TANK, "09/2025", "Decir 'motor y caja', no 'el auto'. Confirmar que siga vigente."),
    ("TANK-2", "GWM Tank 300", "Todoterreno", "Tiene caja reductora y bloqueo de diferencial.", MARCA, "16 Válvulas", V16_TANK, "09/2025", ""),
    ("TANK-3", "GWM Tank 300", "Baúl", "El baúl pasa de 400 a 1.635 litros si bajás los asientos de atrás.", MARCA, "16 Válvulas", V16_TANK, "09/2025", ""),
    ("TANK-4", "GWM Tank 300", "Consumo medido", "En la prueba de Autotest gastó 13 litros cada 100 km de promedio.", MEDIDO, "Autotest", "https://autotest.com.ar/noticias/prueba-de-consumo-cuanto-gasta-el-gwm-tank-300/", "11/2025", "Limitación honesta: decirlo."),
    ("TANK-5", "GWM Tank 300", "Precio", "US$51.900 de lista (último dato publicado).", PRECIO, "16 Válvulas", V16_TANK, "04/09/2025", "Precio viejo: preguntarlo antes de decirlo."),
    ("POER-1", "GWM Poer", "Motor", "Tiene un motor 2.0 turbodiésel de 161 CV y 400 Nm.", MARCA, "Autotest", AT_POER, "28/07/2026", ""),
    ("POER-2", "GWM Poer", "Precios", "La Elite 4x2 manual salía US$28.730 y la Super Luxury 4x4 automática US$39.990 bonificada.", PRECIO, "Autotest", AT_POER, "28/07/2026", "Revisar el aviso de Mercado Libre a US$43.790."),
    ("POER-3", "GWM Poer", "Carga", "Carga 975 kg en la caja.", PRENSA, "La Nación", "https://www.lanacion.com.ar/autos/al-volante/como-es-la-pickup-china-que-quiere-competir-con-las-locales-nid20012023/", "01/2023", "Ficha de 2023: verificar en la versión 2026."),
    # ---------------- Mitsubishi ----------------
    ("L200-1", "Mitsubishi L200", "Carga", "En la caja le cargás más de una tonelada: 1.025 kilos.", MARCA, "Brochure oficial", FT_L200, "06/2025", "La web dice 1.030 kg. Nunca cargar de más para el video."),
    ("L200-2", "Mitsubishi L200", "Inclinación lateral", "Puede andar inclinada 45 grados de costado.", MARCA, "Brochure oficial", FT_L200, "06/2025", "Nunca demostrarlo en cámara."),
    ("L200-3", "Mitsubishi L200", "Modos", "Tiene 7 modos de manejo, de Eco a Roca, y bloqueo del diferencial trasero.", MARCA, "Brochure oficial", FT_L200, "06/2025", ""),
    ("L200-4", "Mitsubishi L200", "Seguridad", "5 estrellas en Latin NCAP y 7 airbags, uno para las rodillas del conductor.", MARCA, "Brochure oficial", FT_L200, "06/2025", ""),
    ("L200-5", "Mitsubishi L200", "Despeje", "Entre el piso y la panza hay 22 centímetros.", MARCA, "Brochure oficial", FT_L200, "06/2025", ""),
    ("L200-6", "Mitsubishi L200", "Consumo medido", "A 90 km/h, Parabrisas midió 13,3 km por litro.", MEDIDO, "Parabrisas", PB_L200, "09/05/2025", "Prueba de 2025."),
    ("L200-7", "Mitsubishi L200", "Garantía", "3 años o 100.000 km.", MARCA, "Brochure oficial", FT_L200, "06/2025", "Limitación honesta: la prensa la marcó como corta."),
    ("L200-8", "Mitsubishi L200", "Largo", "Mide 5,32 metros.", MARCA, "Brochure oficial", FT_L200, "06/2025", "No entra en una cochera de 5 m (E08)."),
    ("L200-9", "Mitsubishi L200", "Precio", "USD 54.000 de lista; USD 51.500 con la bonificación de la marca.", PRECIO, "mitsubishi-motors.com.ar", WEB_L200, "26/11/2026", "Valparaiso la publica a US$48.989."),
    ("OUT-1", "Mitsubishi Outlander", "Asientos y tracción", "Siete asientos y tracción integral con 6 modos de manejo, incluidos Barro y Nieve.", MARCA, "Ficha oficial", FT_OUT, "12/2024", ""),
    ("OUT-2", "Mitsubishi Outlander", "Origen", "Se fabrica en Japón.", PRENSA, "iProfesional", "https://www.iprofesional.com/autos/418833-mitsubishi-lanza-nuevo-suv-7-plazas-argentina-cuanto-sale", "12/2024", ""),
    ("OUT-3", "Mitsubishi Outlander", "Precio", "Se lanzó a USD 61.000; hoy la marca la ofrece a USD 51.500 con bonificación.", PRECIO, "mitsubishi-motors.com.ar", "https://www.mitsubishi-motors.com.ar/vehicles/outlander", "26/11/2026", "Valparaiso la publica a US$46.996."),
    ("OUT-4", "Mitsubishi Outlander", "Equipamiento", "Tiene 7 airbags, techo panorámico y butacas de adelante calefaccionadas.", MARCA, "Ficha oficial", FT_OUT, "12/2024", ""),
    # ---------------- Generales ----------------
    ("GEN-1", "Todos los enchufables", "Si no lo enchufás", "Un enchufable que no se carga gasta más que un auto común: lleva una batería de 200 a 250 kilos.", PRENSA, "iProfesional", IPRO_PHEV, "01/09/2026", ""),
    ("GEN-2", "Todos los híbridos", "Nombres comerciales", "Los nombres distintos de cada sistema híbrido son, en el fondo, lo mismo.", PRENSA, "iProfesional", IPRO_PHEV, "01/09/2026", ""),
    ("GEN-3", "Carga en casa", "Trifásica", "Un dueño cuenta que le dijeron que necesitaba trifásica y que no era cierto: 'la hace cualquier electricista'.", PRENSA, "16 Válvulas (comentario de un dueño)", V16_TRIFASICA, "13/10/2026", "Es la experiencia de una persona: decirlo así y confirmar con un electricista matriculado."),
    ("GEN-4", "Carga en casa", "Monofásica de 32 A", "7,4 kW es lo que da una línea monofásica de 230 V y 32 A.", CUENTA, "Cuenta propia: 230 × 32 = 7.360 W", "", "", "Verificar con un electricista matriculado y con el manual antes de decirlo en cámara."),
    ("GEN-5", "Muchos chinos nuevos", "Rueda de auxilio", "Muchos modelos chinos nuevos traen solo un kit de reparación, no rueda de auxilio.", PRENSA, "Autoweb", AW_AUXILIO, "24/09/2025", "El kit sirve para pinchaduras chicas en la banda de rodamiento (CESVI, vía resumen de búsqueda)."),
    ("GEN-6", "Comprar un 0 km", "Antes de la seña", "Defensa del Consumidor de Córdoba clausuró agencias por señas de 35 a 50 % sin papeles firmados ni fecha de entrega.", PRENSA, "iProfesional", IPRO_CLAUSURA, "05/11/2026", "No nombrar a las agencias clausuradas."),
    ("GEN-7", "Repuestos", "Si la marca se va", "Un fabricante de autopartes dijo: 'Estamos seguros de que sí podemos abastecer esos vehículos' aunque una marca se retire.", PRENSA, "La Nación", LN_POSVENTA, "23/04/2026", ""),
    ("GEN-8", "Repuestos", "Fábrica en Brasil", "GWM empezó a producir en Brasil en agosto de 2025.", PRENSA, "16 Válvulas", V16_BRASIL, "17/08/2025", ""),
    ("GEN-9", "Valparaiso", "Concesionario oficial Changan", "Changan lista a Valparaiso como concesionario oficial en Córdoba.", MARCA, "Localizador de Changan", CHANGAN_API, "26/11/2026", "Pero NO como taller oficial Changan (en Córdoba es City Drive). No decir 'taller oficial Changan'."),
    ("GEN-10", "Precio publicado", "Lo que falta sumar", "El patentamiento se paga aparte; en Córdoba la inscripción ronda el 1,1 a 1,2 % del valor.", PRENSA, "Mercado Libre (aviso de la marca) y notas de patentamiento", "https://auto.mercadolibre.com.ar/MLA-3623085564", "26/11/2026", "Las fuentes no coinciden: usar el presupuesto desglosado de Valparaiso del día."),
    ("GEN-11", "Córdoba", "Viaje promedio", "En Córdoba, el viaje promedio es de 6,3 km y 4 de cada 10 viajes se hacen en auto.", MARCA, "PMUS Córdoba (encuesta 2022)", PMUS, "12/2023", "Dato oficial publicado."),
    ("GEN-12", "Córdoba", "Cochera mínima", "Una cochera de edificio en Córdoba tiene que medir, como mínimo, 5 por 2,50 metros.", MARCA, "Código de Edificación de Córdoba, art. 3.1.1.9.1", CODIGO_EDIF, "Dec. 463/96", "Igual se mide la cochera real del video."),
    ("GEN-13", "Córdoba", "Carga pública", "EPEC tiene 30 puntos de carga públicos, por ahora gratis: 11 en la ciudad y otros en Carlos Paz, Cosquín, La Falda, Villa Allende, Alta Gracia y más.", MARCA, "GEF Informa / EPEC", GEF, "08/09/2026", "No hay en Jesús María, Villa General Belgrano ni Mina Clavero. 'Gratis' puede cambiar: confirmar."),
    ("GEN-14", "Córdoba", "Granizo", "El granizo en Córdoba cae sobre todo de octubre a marzo, entre las 16 y las 20 h.", PRENSA, "Notas de clima (ver numeros-de-cordoba.md, sección 8)", "", "2026", "Sin estadística oficial de días por año."),
    ("GEN-15", "Córdoba", "Patente de híbridos", "Pagás la mitad de patente por ser híbrido.", FALTA, "Ley Impositiva 2026: según dos fuentes, solo para autos fabricados en la provincia", "", "2026", "NO prometerlo hasta confirmarlo con Rentas."),
]

# Supuestos de las cuentas: (nombre definido, etiqueta, valor, formato, fuente)
SUPUESTOS = [
    ("PrecioNafta", "Nafta súper, Córdoba capital ($ por litro)", 2162, '"$"#,##0', "YPF, 16/11/2026 (Hoy Día Córdoba). Cambiar el día que se publica."),
    ("PrecioKWh", "Luz de casa ($ por kWh, con IVA)", 370.24, '"$"#,##0.00', "EPEC desde el 01/11/2026: $305,99 + 21 % de IVA (consumo de 121 a 500 kWh, sin subsidio)."),
    ("PrecioKWhNoche", "Luz de 23 a 5 h con la tarifa de movilidad eléctrica ($ por kWh, con IVA)", 268.08, '"$"#,##0.00', "EPEC: $221,56 + 21 % de IVA. Hay que pedir la tarifa a EPEC."),
    ("PrecioCafe", "Un café en Córdoba ($)", 4000, '"$"#,##0', "Cadena 3, 01/10/2026 ('desde 4.000 a 5.000'). Mejor: el ticket real del café del video."),
    ("KmDia", "Km por día del ejemplo", 50, "0", "Ejemplo de quien vive en el Gran Córdoba. El viaje promedio en la ciudad es de 6,3 km (PMUS)."),
    ("DiasMes", "Días de manejo por mes", 22, "0", "Días hábiles. Si el guion dice 'todos los días', usar 30."),
    ("LNaftero", "Consumo de un naftero compacto (litros cada 100 km)", 8, "0.0", "Supuesto de ejemplo, no es un modelo: decir 'un naftero común'."),
    ("LHibrido", "Consumo de un híbrido que no se enchufa (litros cada 100 km)", 5.1, "0.0", "ORA 05 HEV, mixto, según la marca."),
    ("KWhElectrico", "Consumo de un eléctrico (kWh cada 100 km)", 16.7, "0.0", "ORA 03, ciclo WLTP."),
    ("KWhEnchufable", "Batería del Eado Plus (kWh)", 18.4, "0.0", "Ficha oficial Changan."),
    ("KmEnchufable", "Autonomía eléctrica del Eado Plus (km)", 132, "0", "Ficha oficial, ciclo NEDC (optimista)."),
    ("PeajeCabina", "Peaje de la RAC pagando en la cabina ($)", 3000, '"$"#,##0', "ERSeP, desde el 08/10/2026."),
    ("PeajeTele", "Peaje de la RAC con TelePEAJE ($)", 1931.89, '"$"#,##0.00', "ERSeP, de la 1.ª a la 10.ª pasada del mes."),
]

# Cuentas: (id, para qué guiones, qué calcula, fórmula de Excel, formato, unidad, cómo se dice)
CUENTAS = [
    ("C1", "E27, D06, D22", "Nafta cada 100 km (naftero común)", "=LNaftero*PrecioNafta", '"$"#,##0', "$ cada 100 km", "Un auto naftero común gasta unos [resultado] cada 100 kilómetros (estimado)."),
    ("C2", "E27, V03", "Nafta cada 100 km (híbrido que no se enchufa)", "=LHibrido*PrecioNafta", '"$"#,##0', "$ cada 100 km", "Un híbrido que no se enchufa, unos [resultado] (estimado)."),
    ("C3", "E27, D06, V04", "Luz cada 100 km (eléctrico cargado en casa)", "=KWhElectrico*PrecioKWh", '"$"#,##0', "$ cada 100 km", "Un eléctrico cargado en tu casa, unos [resultado] (estimado)."),
    ("C3N", "D06", "Luz cada 100 km (eléctrico cargado de noche con la tarifa especial)", "=KWhElectrico*PrecioKWhNoche", '"$"#,##0', "$ cada 100 km", "Y si cargás de noche con la tarifa especial, unos [resultado] (estimado)."),
    ("C4", "E27, V01", "Luz cada 100 km (Eado en modo eléctrico, con el dato de laboratorio)", "=KWhEnchufable/KmEnchufable*100*PrecioKWh", '"$"#,##0', "$ cada 100 km", "Un enchufable andando en eléctrico, desde unos [resultado] (estimado, optimista)."),
    ("C4B", "E27, V01", "Luz cada 100 km (Eado, cuenta conservadora: 100 km con la batería llena)", "=KWhEnchufable*PrecioKWh", '"$"#,##0', "$ cada 100 km", "… hasta unos [resultado] (estimado, conservador)."),
    ("C5", "D06, D22", "Nafta por mes con los km del ejemplo (naftero)", "=KmDia*DiasMes*LNaftero/100*PrecioNafta", '"$"#,##0', "$ por mes", "50 kilómetros por día, 22 días: a nafta son unos [resultado] por mes (estimado)."),
    ("C5L", "D06", "Luz por mes con los km del ejemplo (eléctrico)", "=KmDia*DiasMes*KWhElectrico/100*PrecioKWh", '"$"#,##0', "$ por mes", "Con la luz de tu casa, unos [resultado] (estimado)."),
    ("C5A", "D06", "Lo que te ahorrás por mes", "=KmDia*DiasMes*(LNaftero/100*PrecioNafta-KWhElectrico/100*PrecioKWh)", '"$"#,##0', "$ por mes", "Te ahorrás unos [resultado] por mes (estimado)."),
    ("C5Y", "D06", "Lo que te ahorrás por año", "=12*KmDia*DiasMes*(LNaftero/100*PrecioNafta-KWhElectrico/100*PrecioKWh)", '"$"#,##0', "$ por año", "Más de [resultado] por año (estimado)."),
    ("C6", "Eado 'Hacé esta cuenta'", "Litros por mes si manejás 50 km TODOS los días (30 días)", "=KmDia*30*LNaftero/100", "0", "litros por mes", "Si manejás 50 kilómetros todos los días, se te van unos [resultado] litros de nafta por mes (estimado)."),
    ("C6P", "Eado 'Hacé esta cuenta'", "Esos litros en plata, por año", "=KmDia*30*LNaftero/100*PrecioNafta*12", '"$"#,##0', "$ por año", "Por doce meses: unos [resultado] (estimado)."),
    ("C7", "E02", "Km que hace un naftero con lo que sale un café", "=PrecioCafe/PrecioNafta/LNaftero*100", "0", "km", "Con lo que sale un café, un naftero hace unos [resultado] kilómetros (estimado)."),
    ("C7H", "E02", "Km que hace un híbrido con lo que sale un café", "=PrecioCafe/PrecioNafta/LHibrido*100", "0", "km", "Un híbrido, unos [resultado] (estimado)."),
    ("C7E", "E02", "Km que hace un eléctrico con lo que sale un café", "=PrecioCafe/PrecioKWh/KWhElectrico*100", "0", "km", "Y un eléctrico, unos [resultado] (estimado)."),
    ("C7J", "E02 (gancho B), V15", "Km que hace el JMEV Easy 3 en ciudad con lo que sale un café (11 km por kWh, medido)", "=PrecioCafe/PrecioKWh*11", "0", "km", "El eléctrico más chico, en ciudad, unos [resultado] (estimado con el consumo medido por Parabrisas)."),
    ("C8", "E09", "Ida y vuelta a Jesús María a nafta (112,4 km)", "=112.4*LNaftero/100*PrecioNafta", '"$"#,##0', "$", "Ida y vuelta a Jesús María son unos 112 km: a nafta, unos [resultado] (estimado, antes de medir)."),
    ("C8H", "E09", "Ida y vuelta a Jesús María en híbrido", "=112.4*LHibrido/100*PrecioNafta", '"$"#,##0', "$", "En un híbrido, unos [resultado] (estimado)."),
    ("C8E", "E09", "Ida y vuelta a Jesús María en eléctrico", "=112.4*KWhElectrico/100*PrecioKWh", '"$"#,##0', "$", "Y en un eléctrico, unos [resultado] (estimado). En Jesús María no hay cargador público."),
    ("C9", "E10", "Cosquín ida y vuelta contra la autonomía eléctrica del Eado", "=KmEnchufable-104.2", "0", "km de margen", "Cosquín, ida y vuelta, son unos 104 km: según la ficha, sobran [resultado] km eléctricos (en la subida y con aire va a rendir menos)."),
    ("C10", "D22, V01", "Nafta por mes viviendo en Mendiolaza y trabajando en el centro (53 km por día)", "=53*DiasMes*LNaftero/100*PrecioNafta", '"$"#,##0', "$ por mes", "Si vivís en Mendiolaza y trabajás en el centro, hacés unos 53 km por día: unos [resultado] de nafta por mes (estimado)."),
    ("C10C", "D22, V01", "Nafta por mes viviendo en Carlos Paz y trabajando en el centro (72,2 km por día, sin peajes)", "=72.2*DiasMes*LNaftero/100*PrecioNafta", '"$"#,##0', "$ por mes", "Desde Carlos Paz, unos [resultado] por mes, más los peajes (estimado)."),
    ("C10A", "D22", "Nafta por mes viviendo en Alta Gracia (76,2 km por día)", "=76.2*DiasMes*LNaftero/100*PrecioNafta", '"$"#,##0', "$ por mes", "Desde Alta Gracia, unos [resultado] por mes (estimado)."),
    ("C11", "E08", "Lo que sobra de largo con el Eado en una cochera de 5 m", "=5-4.77", "0.00", "m", "Este auto mide 4,77: le sobran [resultado] metros."),
    ("C11L", "E08", "Lo que sobra (o falta) con la L200 en una cochera de 5 m", "=5-5.32", "0.00", "m", "La pickup mide 5,32: le faltan 32 centímetros (no entra)."),
    ("C12", "D06, D05", "Cuánto más barato es el kWh de noche con la tarifa especial", "=1-221.56/305.09", "0%", "menos", "De 11 de la noche a 5 de la mañana, el kWh te sale cerca de un [resultado] menos."),
    ("C13", "E09, E10", "Cuánto más caro es el peaje en la cabina que con TelePEAJE", "=PeajeCabina-PeajeTele", '"$"#,##0', "$ por pasada", "Pagando en la cabina, cada pasada te cuesta [resultado] más."),
    ("C14", "D22, E27", "Llenar un tanque de 45 litros", "=45*PrecioNafta", '"$"#,##0', "$", "Llenar un tanque de 45 litros hoy en Córdoba cuesta unos [resultado]."),
    ("C15", "V15", "Llenar la batería del JMEV Easy 3 (30,24 kWh) en casa", "=30.24*PrecioKWh", '"$"#,##0', "$", "Llenar la batería en tu casa cuesta unos [resultado] (estimado)."),
    ("C15V", "V15", "Cuántas veces llenás la batería del JMEV con un tanque de 40 litros", "=40*PrecioNafta/(30.24*PrecioKWh)", "0", "veces", "Con lo que sale un tanque de 40 litros, cargás este auto unas [resultado] veces (estimado)."),
    ("C16", "D05", "Horas para llenar la batería del Eado en un enchufe común (~2,2 kW)", "=KWhEnchufable/2.2", "0.0", "horas", "En un enchufe común, unas [resultado] horas (estimado: verificar con el manual)."),
    ("C16W", "D05", "Horas para llenar la batería del Eado a 7,4 kW", "=KWhEnchufable/7.4", "0.0", "horas", "Con un cargador de pared de 7,4 kW, unas [resultado] horas (estimado)."),
    ("C17", "V02, D29", "Cuántas veces más chica es la batería de la H6 que la del ORA 03", "=48/1.76", "0", "veces", "Su batería es unas [resultado] veces más chica que la de un eléctrico (estimado)."),
    ("C18", "V08", "Nafta por mes de un auto de empresa que hace 100 km por día (naftero)", "=100*DiasMes*LNaftero/100*PrecioNafta", '"$"#,##0', "$ por mes", "Un auto de tu empresa que hace 100 km por día gasta unos [resultado] de nafta por mes (estimado)."),
    ("C18E", "V08", "Luz por mes del mismo auto en un enchufable andando en eléctrico (cuenta conservadora)", "=100*DiasMes*KWhEnchufable/100*PrecioKWh", '"$"#,##0', "$ por mes", "Andando en eléctrico, hasta unos [resultado] de luz (estimado, con la tarifa residencial: la de la empresa es otra)."),
    ("C18A", "V08", "Ahorro por auto por mes (cuenta conservadora)", "=100*DiasMes*(LNaftero/100*PrecioNafta-KWhEnchufable/100*PrecioKWh)", '"$"#,##0', "$ por mes", "Te ahorrás más de [resultado] por auto por mes (estimado)."),
]

# Errores encontrados (dónde, qué dice, qué tendría que decir, fuente)
ERRORES = [
    ("Mercado Libre · aviso del Eado Plus", "'Motor 1.5 híbrido enchufable de 215 cv'", "Motor a nafta de 101 HP y eléctrico de 212 HP (la marca no declara la potencia combinada).", ML_EADO),
    ("Mercado Libre · aviso del Eado Plus", "'Cámara de retroceso'", "Cámara 360° con dashcam integrada.", ML_EADO),
    ("Mercado Libre · aviso del Eado Plus", "'Servicio postventa oficial, repuestos y taller autorizado'", "Changan no lista a Valparaiso como taller oficial (en Córdoba figura City Drive). Confirmar con Changan antes de decirlo.", CHANGAN_API),
    ("Mercado Libre · aviso de la Poer Super Luxury", "US$43.790", "La lista de julio era US$39.990 bonificada: revisar el precio.", AT_POER),
    ("Mercado Libre · aviso del Deepal S05", "'Baúl de 462 litros'", "No hay fuente oficial argentina: confirmar o sacarlo.", FT_DEEPAL),
    ("Web · ficha H6 PRO HEV", "'Consumo promedio: 6 km/l'", "5,6 L/100 km mixto según la marca (unos 17,9 km/l).", "https://valparaisomotors.com.ar/listing/gwm-haval-h6-pro-hev-supreme-2wd/"),
    ("Web · fichas H6, ORA 05 y Jolion Pro", "'1.5 cc'", "1.5 L (o 1.497 cm³).", "https://valparaisomotors.com.ar/listing/gwm-ora-05-hev/"),
    ("Web · ficha ORA 05", "Tanque de 50 L", "La prensa dice 55 L: confirmar con la ficha oficial.", "https://valparaisomotors.com.ar/listing/gwm-ora-05-hev/"),
    ("Web · ficha ORA 03", "Sin batería, autonomía ni potencia; 'motor OTRO, 0 cc'", "Batería de 48 kWh, hasta 310 km WLTP, 169 CV.", "https://valparaisomotors.com.ar/listing/gwm-ora-03-sr/"),
    ("Web · Jolion", "Aparece dos veces ('Jolion Pro HEV Supreme' y 'Jolion HEV Supreme')", "La prensa de nov. 2026 habla de una sola versión: confirmar si son dos autos o uno cargado dos veces.", "https://valparaisomotors.com.ar/?filter-condition=0km"),
    ("Web · fotos del ORA 03 y del Jolion Pro", "Archivos llamados 'ChatGPT Image 2 sept 2026' y 'ChatGPT Image 22 sept 2026'", "Si son imágenes hechas con IA, reemplazarlas por fotos reales (regla de marca: no usar autos generados).", "https://valparaisomotors.com.ar/listing/gwm-ora-03-sr/"),
    ("Web · todas las fichas", "'Financiación destacada: Bancor – Línea UVA' con la tasa vacía", "Completar tasa, CFT y vigencia, o sacarlo. Nunca 'sin interés' ni 'cuota fija' en una línea UVA.", "https://valparaisomotors.com.ar/listing/gwm-ora-03-sr/"),
    ("Web · Nosotros", "'más de 20 años' y '25 años en el negocio' en la misma página", "Elegir un solo número.", "https://valparaisomotors.com.ar/nosotros/"),
    ("TikTok · descripción del video EV/PHEV/HEV", "Todavía dice 'Y uno de ellos nunca se enchufa'", "El dueño sacó esa frase del video: sacarla también de la descripción.", "https://www.tiktok.com/@valparaisomotors/video/7699958886920424711"),
    ("Guiones anteriores", "'995 km de autonomía total' (Eado)", "No hay fuente oficial argentina: sacarlo.", "https://changan.com.ar/modelos/eado-plus"),
    ("Guiones anteriores", "'120 litros por mes' con 50 km por día (Eado)", "120 L es con 30 días. Con 22 días hábiles son unos 88 L. Decir 'todos los días' o 'unos 90 litros'.", HOYDIA),
    ("Guiones anteriores", "ORA 03: 'del 20 al 80 % en 36 min' y garantía '5 o 7 años'", "Del 10 al 80 % en unos 40 min; garantía de 7 años o 150.000 km.", PB_ORA03),
]
