# Proceso de venta: de lead a entrega (Valparaiso Motors, Córdoba)

> Notas de investigación, 24/11/2026. Alcance: lo que tiene que pasar desde que entra un lead hasta la entrega y la posventa, y con qué métricas medirlo. Casi todos los benchmarks numéricos son de EE. UU. (Cox, Pied Piper, Foureyes, J.D. Power) y muchos vienen de proveedores de software con interés comercial: se marcan así. Las fuentes viejas (antes de 2024) están marcadas **[viejo]**. Lo que no tiene URL va en "Gaps". Restricciones del proyecto (CLAUDE.md, secciones 1, 4 y 5): mostrar CFT en financiación, nunca "sin interés" con CER/UVA, vendedores que se presentan como vendedores, nada de testimonios ni reseñas inventadas.

## 1. Velocidad de respuesta (speed to lead), fuera de horario y WhatsApp primero

### Takeaway
La evidencia académica sobre velocidad es vieja (2007–2011) y mide "calificar" el lead, no venderlo. Aun así, todos los datos de 2025–2026 apuntan a lo mismo: el ganador responde en minutos por más de un canal, y en las concesionarias el problema real es que una parte grande de los leads ni se registra ni recibe seguimiento. En Argentina el canal natural es WhatsApp. Desde el 1/10/2026 Meta volvió a cobrar los mensajes de servicio de la API, pero las conversaciones que entran por anuncios Click-to-WhatsApp siguen teniendo una ventana gratis.

### Cited Findings
**Estudios clásicos [viejo]**
- HBR, "The Short Life of Online Sales Leads" (Oldroyd, McElheran y Elkington, 2011) **[viejo]**:
  - auditó 2.241 empresas de EE. UU. mandándoles un lead web de prueba; 37 % respondió dentro de la hora y 23 % nunca respondió;
  - las que intentaron contactar dentro de la hora tuvieron casi 7 veces más probabilidad de **calificar** el lead (conversación útil con quien decide) que las que lo intentaron una hora después, y más de 60 veces más que las que tardaron 24 h o más;
  - mide calificación, no venta.
  - [BYU ScholarsArchive](https://scholarsarchive.byu.edu/facpub/9711)
- Las compilaciones de proveedores repiten dos cifras que no pude verificar en su fuente original, así que no conviene usarlas como dato duro [Ventavid, compilación 2026](https://www.ventavid.com/blog/dealership-lead-response-statistics-2026); [Demand Local](https://www.demandlocal.com/blog/lead-to-sale-conversion-statistics/):
  - "21 veces más probable calificar si respondés en 5 minutos que en 30", que suele atribuirse al estudio MIT/InsideSales Lead Response Management de 2007 **[viejo]**;
  - "+391 % de conversión respondiendo en 1 minuto", de Velocify **[viejo]**.
- Otra cifra de proveedor (Proactive Training Solutions), sin metodología publicada: los leads contactados dentro de los 5 minutos cierran 32 %, contra 12 % de los contactados 24 h después o más. [resultado de búsqueda, Maritz/Demand Local](https://www.demandlocal.com/blog/appointment-setting-show-rate-statistics/)

**Velocidad y calidad de respuesta en concesionarias (2025–2026)**
- DAS Technology, 2025 Lead Response Study: 1.700 concesionarias de EE. UU., leads del 3.º y 4.º trimestre de 2024. [DealershipGuy, 28/01/2025](https://news.dealershipguy.com/p/study-finds-many-dealers-fall-short-on-key-lead-processes-2025-01-28)
  - Velocidad:
    - 61 % respondió en 15 min o menos (55 % antes);
    - 19 % tardó más de una hora (33 % en 2023);
    - 4 % no respondió (9 % en 2023).
  - Calidad:
    - 74 % no incluyó precio;
    - 90 % no mandó varias fotos;
    - 26 % no dio información del auto consultado.
  - No informa ventas.
- Pied Piper ILE 2025: índice promedio de la industria 65 (+3); se respondió por varios canales (email, teléfono, texto) 49 % de las veces (44 % el año anterior). [Business Wire](https://www.businesswire.com/news/home/20250504671700/en); [DealershipGuy](https://news.dealershipguy.com/p/napleton-automotive-group-ranks-1-in-digital-lead-response-four-years-in-a-row-2025-05-06)
  - Los mejores grupos:
    - respondieron 90 % de las consultas por email o texto dentro de la hora;
    - llamaron 96 % de las veces;
    - 3 de cada 4 llamadas fueron dentro de los 15 min.
  - Otra nota da 87 % de llamadas dentro de los 15 min, así que las fuentes no coinciden en ese número.
- Pied Piper ILE 2026: 3.290 sitios de concesionarias. [DealershipGuy, 24/02/2026](https://news.dealershipguy.com/p/dealers-are-responding-faster-than-ever-to-web-leads-but-automation-risks-linger-2026-02-24)
  - Índice promedio 71 (+6).
  - 62 % usó llamada y texto (49 % en 2025).
  - Advierte que la IA puede tapar fallas:
    - datos que no pasan entre el sistema de gestión (DMS), la web, el CRM y la IA;
    - leads que se traban cuando el bot se los pasa a una persona poco entrenada;
    - cita: "Teams assume automation is working and that someone will step in if it fails".
- Foureyes, 2026 Automotive Dealer Benchmarks: datos de 2025, más de 22.900 sitios de concesionarias. [Foureyes, 22/04/2026](https://www.foureyes.io/blog/2026-automotive-dealer-benchmarks-report)
  - Leads sin atender:
    - **62,8 %** de los leads de venta que vuelven a consultar no tuvo respuesta de un vendedor en 24 h;
    - **42,7 %** de los leads calificados se gestionó mal;
    - **15,2 %** nunca se cargó en el CRM (14,1 % en 2024).
  - Compra:
    - **61,2 %** de los que compraron lo hicieron dentro de los 3 días de la primera consulta;
    - **11,7 %** de todos los leads de venta compró (10,2 % antes);
    - los canales pagos tuvieron la mayor tasa de compra.
  - Espera telefónica promedio: ~73 s.

**Argentina y WhatsApp**
- Zenvia, estudio de 64 grupos de concesionarias de Argentina y México (primer trimestre de 2016) **[viejo, proveedor]**. [Zenvia](https://zenvia.com/es/blog/el-impacto-de-la-inaccion-cuando-el-problema-no-es-llamar-rapido-a-tus-clientes-sino-llamarlos/)
  - 61 % de los que dejaron una consulta online nunca fue contactado.
  - Demora: más de 72 h por teléfono y 30 h por email (~6,5 h contando solo horario comercial).
  - Su escenario "contactar al 100 % duplica las ventas" es ilustrativo, no medido.
- ACARA, citada por Forbes Argentina (fecha de la nota no confirmada): el 88 % de los compradores potenciales busca información en internet y el 71 % espera una propuesta personalizada. [Forbes Argentina](https://www.forbesargentina.com/negocios/las-concesionarias-40-ya-estan-marcha-acelerando-n65399/amp)
- Cliengo, proveedor y sin metodología publicada: [Cliengo](https://guiawabusiness.cliengo.com/whatsapp-autos)
  - "el 85 % de los compradores de autos en LATAM investiga por WhatsApp antes de visitar una agencia";
  - sus concesionarias clientes bajan 45 % el tiempo de respuesta a cotizaciones.
- Tecnom (CRM automotor argentino):
  - Cada mensaje de WhatsApp que llega al número de la concesionaria se registra como lead en el CRM y se asigna en el momento a un vendedor. [Tecnom, conector WhatsApp](https://intercom.help/tecnom/es/articles/12956663-conector-whatsapp-tecnom)
  - Su bot "Tecna" madura leads por WhatsApp y agenda solo. [Tecnom, Tecna](https://intercom.help/tecnom/es/articles/12533236-primeros-pasos-para-configurar-tecna); [Tecnom, agendamiento](https://intercom.help/tecnom/es/articles/12752428-atencion-de-leads-por-tecnom-chat-y-agendamiento-automatico)
  - Limitación declarada: el bot no lee imágenes.

**Costos de WhatsApp (Meta, documentación oficial)** [Meta for Developers](https://developers.facebook.com/docs/whatsapp/pricing)
- Desde el 1/07/2025 se cobra por mensaje, y la ventana de atención es de 24 h desde el último mensaje del cliente.
- Mensajes de servicio: gratis desde el 1/11/2024; **se cobran otra vez desde el 1/10/2026**, con 1.000 gratis por mes por número.
- Mensajes "utility" dentro de la ventana abierta: también se cobran otra vez desde el 1/10/2026.
- La ventana gratis que abre un anuncio Click-to-WhatsApp ("free entry point") "may remain open for up to 7 days", y cubre todas las categorías de mensaje.
  - Cliengo dice 72 h, lo que contradice la documentación de Meta. [Cliengo](https://guiawabusiness.cliengo.com/precios)
- Argentina: Meta bajó las tarifas utility y de autenticación el 1/10/2025 y habilitó facturar en pesos (ARS) el 1/04/2026.
- Tarifas por mensaje en Argentina desde el 1/10/2026, según SleekFlow (proveedor): [SleekFlow](https://help.sleekflow.io/en_US/daftar-harga)
  - marketing USD 0,07107;
  - utility USD 0,02990;
  - servicio USD 0,0260.
  - Zernio publica otras cifras. [Zernio](https://zernio.com/blog/whatsapp-business-api-pricing)
- El cambio de octubre no alcanza a las respuestas desde la app WhatsApp Business: es solo para la API. [Cliengo](https://guiawabusiness.cliengo.com/calculadora-precios-whatsapp-2026)

### Inferences
- Meta de respuesta propuesta:
  - acuse automático por WhatsApp en menos de 1 minuto, las 24 horas;
  - primer contacto humano en menos de 5 min en horario comercial;
  - llamada dentro de la hora si el cliente dejó teléfono y la aceptó.
- Fuera de horario: que el bot califique (modelo, uso, si entrega usado, si financia, cuándo compra) y ofrezca turno; a primera hora un vendedor retoma con nombre y apellido.
- Que el 61 % compre dentro de los 3 días (Foureyes) sugiere concentrar el esfuerzo en las primeras 72 h. El dato es de EE. UU.; en Argentina, con financiación y entrega del usado de por medio, el ciclo probablemente sea más largo: medirlo.
- La primera respuesta tiene que traer valor. El punto débil de la industria es responder sin precio ni fotos (DAS: 74 % sin precio, 90 % sin fotos). La respuesta debería incluir:
  - un rango de precio o cuota, con CFT;
  - fotos o video del auto real;
  - una pregunta que califique.
- El volumen de las campañas de Instagram debería entrar por **anuncios Click-to-WhatsApp**: la ventana gratis de Meta (hasta 7 días) y la atribución automática de origen bajan el costo por conversación.

### Gaps
- No encontré un estudio de 2025–2026 que mida directamente tiempo de respuesta contra **venta** en concesionarias, ni datos argentinos recientes sobre tiempos de respuesta por WhatsApp. El único dato local (Zenvia) es de 2016.
- La tarifa vigente de Meta para Argentina en USD o ARS hay que mirarla en la tabla oficial: las cifras de los proveedores no coinciden.
- No investigué las políticas de Meta sobre consentimiento para mensajes de marketing ni la Ley 25.326 de datos personales aplicada a bases de WhatsApp. Conviene revisarlas.

## 2. Seguimiento: cantidad de contactos, canales, guiones que califican y puntaje de leads

### Takeaway
La evidencia firme apunta a **usar varios canales desde el principio** (texto o WhatsApp más llamada) y a **no abandonar el lead en las primeras 24–72 h**. No encontré un estudio confiable y reciente sobre "el número óptimo de contactos". En cambio hay datos útiles sobre qué califica: la mayoría llega sin decidir el modelo, y una parte grande compara nuevo con usado.

### Cited Findings
- Pied Piper 2025:
  - Napleton (n.º 1 entre los grupos) responde por texto o email y además llama dentro de la hora, lo que según el grupo conecta con el 82 % de los interesados. [DealershipGuy](https://news.dealershipguy.com/p/napleton-automotive-group-ranks-1-in-digital-lead-response-four-years-in-a-row-2025-05-06)
  - Los grupos que bajaron en el índice mandaron en promedio 12 % menos mensajes de texto que el año anterior. [Business Wire](https://www.businesswire.com/news/home/20250504671700/en)
- Pied Piper 2026: el uso combinado de llamada y texto subió a 62 %. [DealershipGuy](https://news.dealershipguy.com/p/dealers-are-responding-faster-than-ever-to-web-leads-but-automation-risks-linger-2026-02-24)
- Foureyes (datos 2025): 62,8 % de los leads que vuelven a consultar no recibió respuesta de un vendedor en 24 h; 61,2 % de los compradores compró dentro de los 3 días. [Foureyes](https://www.foureyes.io/blog/2026-automotive-dealer-benchmarks-report)
- Cox Automotive Car Buyer Journey 2025 (2.300 compradores, otoño boreal 2025, publicado el 13/01/2026): [Cox, comunicado (PDF)](https://www.coxautoinc.com/wp-content/uploads/2026/01/2025-Cox-Automotive-Car-Buyer-Journey-Press-Release.pdf)
  - El modelo:
    - 71 % empezó la búsqueda sin saber qué auto iba a comprar;
    - solo 29 % tenía el modelo decidido (37 % en 2020).
  - Nuevo o usado:
    - 66 % consideró nuevo y usado (57 % antes);
    - entre los compradores de 0 km, 43 %.
  - Costo: 62 % siente que tener un auto es demasiado caro.
  - Fuentes de información:
    - visitan en promedio 4,6 sitios;
    - 26 % usó redes sociales;
    - 12 % usó sitios de IA (17 % entre los compradores de 0 km).
- Cox 2025, uso de IA: 25 % de los compradores de 0 km usó herramientas de IA, y el 84 % de los compradores "mayormente digitales" que usaron asistentes de IA quedó muy satisfecho. [Cox, comunicado (PDF)](https://www.coxautoinc.com/wp-content/uploads/2026/01/2025-Cox-Automotive-Car-Buyer-Journey-Press-Release.pdf)
- DAS 2025: la falla más común en la respuesta es no dar precio (74 %). [DealershipGuy](https://news.dealershipguy.com/p/study-finds-many-dealers-fall-short-on-key-lead-processes-2025-01-28)
- Tecnom permite clasificar los leads por unidad de negocio (0 km, plan de ahorro, usados) y guarda el identificador del clic de Meta (fbclid). Los leads de la web sin parámetros UTM entran como "origen no identificado". [Tecnom, Tecna](https://intercom.help/tecnom/es/articles/12533236-primeros-pasos-para-configurar-tecna); [Tecnom, guía UTM](https://intercom.help/tecnom/es/articles/13514765-guia-de-parametros-utm)

### Inferences
- Cadencia propuesta (inferencia; a validar con datos propios):

  | Momento | Contacto |
  |---|---|
  | Día 0 | WhatsApp en menos de 5 min, con precio o cuota (CFT), fotos o video y una pregunta; llamada dentro de la hora si hay teléfono. |
  | Día 1 | WhatsApp con un video corto del vendedor junto al auto. |
  | Día 2 o 3 | Llamada, más una propuesta de turno o prueba de manejo. |
  | Días 5, 7 y 14 | Mensajes con información nueva (cotización del usado, simulación de financiación, stock). |
  | Día 30 en adelante | Pasa a "nutrición" mensual. Se cierra solo si pide no ser contactado. |

- Preguntas para calificar (pensadas para Valparaiso, por la evidencia de que el 71 % llega sin modelo decidido):
  1. ¿Para qué lo vas a usar? Ciudad o ruta, y cuántos km por día.
  2. ¿Tenés cochera con enchufe? Define EV, PHEV o HEV.
  3. ¿Entregás un usado? Marca, modelo, año y km.
  4. ¿Pensás financiar? En qué rango de cuota y con qué anticipo.
  5. ¿Para cuándo lo necesitás?
- Puntaje de leads simple (A/B/C):
  - **A:** compra en menos de 30 días y tiene forma de pago o usado definidos.
  - **B:** compra en 1 a 3 meses.
  - **C:** curioso o sin plazo.
  - La palabra clave del video (EADO, CUOTA…) define el origen.
- El equipo de ventas no debería llamar "lead" a todo comentario de Instagram. Conviene separar:
  - **consulta** (comentario o DM);
  - **lead calificado** (dio datos y modelo);
  - **oportunidad** (turno o prueba).
  Así el embudo se mide con denominadores comparables.

### Gaps
- No encontré evidencia reciente y con metodología sobre la cantidad óptima de intentos de contacto ni sobre su espaciado en ventas de autos. Las cifras "de 6 a 8 intentos" que circulan vienen de blogs sin fuente.
- No hay datos argentinos sobre qué combinación de WhatsApp, llamada y email funciona mejor. Hay que medirlo internamente.
- No encontré estudios públicos sobre puntaje de leads con resultados en concesionarias.

## 3. Turnos, asistencia, prueba de manejo y prueba a domicilio

### Takeaway
Los benchmarks de EE. UU. muestran que un lead de internet se convierte en turno ~40 % de las veces (contra ~74 % por teléfono). La asistencia sana es de 50 % o más, y la cita con prueba de manejo cierra bastante más que sin ella. Casi todos los compradores manejan el auto antes de comprar, sobre todo los de eléctricos. En Argentina, la prueba "a domicilio" aparece solo como acción puntual de marca, no como servicio habitual: es un espacio libre para diferenciarse.

### Cited Findings
- Foureyes: tasa de turno sobre leads contactados en abril de 2025. [Foureyes, tasa de turnos](https://www.foureyes.io/blog/dealership-appointment-set-rates)
  - Por canal: ~40 % en leads de internet (41 % en el 4.º trimestre de 2024 y el 1.º de 2025) y 74 % en leads telefónicos.
  - Usados contra 0 km: en usados, 44 % por internet y 78 % por teléfono; en 0 km, ~35 % por internet.
  - Un estudio de embudo más amplio da 40 % de promedio, con un rango de 30–59 % según el mercado. [Demand Local](https://www.demandlocal.com/blog/appointment-setting-show-rate-statistics/)
- Asistencia a la cita:
  - Maritz: la de internet debería estar "well over 40%". [Maritz](https://maritz.com/?p=14866)
  - Una tabla de Foureyes sin fecha clara da 56 % para 0 km y 50 % para usados. [Foureyes, benchmarks 2025](https://www.foureyes.io/blog/2025-automotive-dealer-benchmarks-report)
  - Otro proveedor considera realista 50–65 % y excelente más de 70 %. [Demand Local](https://www.demandlocal.com/blog/appointment-setting-show-rate-statistics/)
- Cierre:
  - Foureyes, misma tabla: ~42 % (0 km) y ~40 % (usados) **sobre citas**. [Foureyes](https://www.foureyes.io/blog/2025-automotive-dealer-benchmarks-report)
  - Maritz, cierre de leads de internet en un BDC (equipo que atiende leads): 10–15 % **sobre leads**. [Maritz](https://maritz.com/?p=14866)
  - Ojo: los denominadores son distintos.
- Prueba de manejo:
  - CDK Global (11/06/2025): 91 % de los compradores hace una prueba de manejo antes de comprar; 95 % en el caso de eléctricos. [CDK](https://www.cdkglobal.com/insights/why-dealerships-cant-afford-flub-test-drive)
  - Auto Dealer Today (fecha no confirmada, probablemente **[viejo]**): las citas cierran 44 %; con prueba de manejo, 58 %; con un gerente involucrado, 62 %. [Auto Dealer Today](https://www.autodealertodaymagazine.com/articles/increase-your-closing-ratio-by-20)
  - Una guía de la industria da 20–40 % de conversión de prueba a compra. [Rework, guía 2026](https://resources.rework.com/libraries/automotive-sales-growth/internet-close-rate-metrics)
- Cox 2025, lo digital: [Cox (PDF)](https://www.coxautoinc.com/wp-content/uploads/2026/01/2025-Cox-Automotive-Car-Buyer-Journey-Press-Release.pdf)
  - 53 % hizo todos los pasos en la concesionaria y solo 7 % compró todo online;
  - 63 % prefiere combinar online y presencial;
  - 48 % quiere pedir el crédito online, pero solo 33 % lo hace.
- Cox (resumen de 2024): los compradores valoran el tiempo en la concesionaria para la prueba de manejo, el trato con el vendedor y la entrega. [Autotrader B2B](https://b2b.autotrader.com/resources/top-takeaways-car-buyer-journey/)
- Cox 2025, tiempos: los compradores de 0 km dedicaron en total ~12 h 13 min a buscar y comprar; los que adelantaron pasos online ahorraron ~44 min en la concesionaria. [Autotrader B2B, 2025](https://b2b.autotrader.com/resources/2025-car-buyer-journey-trends/)
- J.D. Power China SSI 2025: los compradores citan la prueba de manejo como factor decisivo y se sugiere un contacto de satisfacción después de la prueba. Es otro mercado; no lo verifiqué en el informe completo. [J.D. Power](https://www.jdpower.com/business/press-releases/2025-china-sales-satisfaction-index-ssi-study)
- Argentina:
  - Renault hizo una "Business Week" en la que llevó autos al lugar de trabajo del cliente durante una jornada, en 15 concesionarias (acción puntual). [Autotest](https://autotest.com.ar/noticias/renault-ofrece-pruebas-de-manejo-para-clientes-profesionales/)
  - Dongfeng impulsa pruebas de manejo de híbridos y eléctricos en concesionarias. [Mercado](https://mercado.com.ar/movilidad/dongfeng-impulsa-test-drives-en-concesionarios-con-tres-modelos-hibridos-y-electricos)
  - Ford organizó un "Ranger Test Drive Day" con inscripción online. [MDZ](https://www.mdzol.com/mdz-autos/ford-invita-los-clientes-todo-el-pais-probar-la-ranger-toda-su-red-oficial-n1552429)
  - El CRM Tecnom tiene un módulo para cargar unidades de prueba y agendarlas. [Tecnom](https://intercom.help/tecnom/es/articles/13688279-como-cargar-unidades-de-prueba-de-manejo)

### Inferences
- Embudo de referencia para fijar metas iniciales (inferencia, a recalibrar con 60–90 días de datos propios):

  | Paso | Meta |
  |---|---|
  | Contacto | ≥ 80 % de los leads calificados |
  | Turno | ≥ 40 % de los contactados |
  | Asistencia | ≥ 60 % de los turnos |
  | Prueba de manejo | ≥ 80 % de los que asisten |
  | Cierre | ~35–40 % de los que asisten |
  | Venta total | ~8–12 % de los leads calificados |

  Los leads de comentarios de Instagram, con muchos curiosos de todo el país, van a convertir menos: medirlos aparte.
- Para los PHEV y EV (Eado Plus, Deepal S05, ORA 03), la prueba de manejo es clave: 95 % de los compradores de eléctricos maneja antes (CDK). Además se puede mostrar en vivo el modo EV y la carga.
- Una **prueba de manejo a domicilio o en el trabajo** en Córdoba Capital no parece ser práctica habitual en el país: sería un diferencial concreto, sobre todo para leads A. Requiere seguro y protocolo, y el que va es un vendedor identificado como tal.
- Para subir la asistencia: confirmación por WhatsApp el día anterior y 2 h antes, con el nombre del vendedor, la dirección (pin del mapa) y el auto preparado.

### Gaps
- No hay datos argentinos de tasa de turno, asistencia ni cierre por canal.
- La cifra de "58 % con prueba de manejo" no tiene fecha ni metodología verificada.
- No encontré estudios del efecto de la prueba a domicilio sobre el cierre.

## 4. El usado como parte de pago: imán de leads y palanca de cierre

### Takeaway
En Argentina 2026 la diferencia de precio entre un usado reciente y un 0 km se achicó mucho. Eso hace que tomar el usado (más la financiación) sea la palanca natural para pasar al cliente al 0 km. Los precios de referencia públicos (ACARA, Cámara del Comercio Automotor) permiten ofrecer una "tasación en el momento" como gancho de conversación. No encontré datos de conversión de las herramientas de tasación online en concesionarias argentinas.

### Cited Findings
- Brecha entre usado y 0 km:
  - Ámbito, citando a un referente del sector (fecha de la nota no confirmada): entre un 0 km y un usado de primer año ronda el 20–25 %, y en el segundo año 30–35 %. [Ámbito](https://www.ambito.com/autos/la-guerra-precios-0km-ya-impacta-el-mercado-usados-n6238547/amp)
  - iProfesional (14/07/2026): la brecha "se pulveriza". Ejemplo: un usado 2023 a ~$27.000.000 contra un 0 km a $38.318.000. Ante la poca diferencia, mucha gente elige el 0 km porque lo puede financiar. [iProfesional](https://www.iprofesional.com/autos/459549-se-pulveriza-brecha-precios-entre-autos-y-camionetas-cero-kilometro-y-usados-seminuevos)
- Perfil: [Perfil / Parabrisas](https://parabrisas.perfil.com/noticias/amp/autos/el-error-que-puede-hacerte-perder-miles-dolares-vender-tu-auto-que-esta-pasando-usados-argentina.phtml)
  - vender entre particulares y entregar el usado como parte de pago son operaciones distintas;
  - tasar solo con avisos parecidos lleva a pedir de más; conviene mirar también el precio del 0 km equivalente y sus promociones.
- Guías de precios:
  - ACARA publica todos los meses su guía de precios de usados y 0 km. [Kavak, blog](https://www.kavak.com/ar/blog/acara-autos-precios-al-dia)
  - La Cámara del Comercio Automotor (CCA) actualiza cada mes precios de referencia de más de 6.000 modelos. Son valores orientativos. [Kavak, blog](https://www.kavak.com/ar/blog/acara-autos-precios-al-dia)
  - Kavak ofrece cotización online del usado. [Kavak](https://www.kavak.com/ar/blog/guia-kavak-como-saber-cuanto-vale-mi-auto)
- Cox 2025: 66 % de los compradores consideró nuevo y usado. [Cox (PDF)](https://www.coxautoinc.com/wp-content/uploads/2026/01/2025-Cox-Automotive-Car-Buyer-Journey-Press-Release.pdf)
- Foureyes (abril de 2025): los leads de usados sacan turno más que los de 0 km (44 % contra ~35 % por internet). [Foureyes](https://www.foureyes.io/blog/dealership-appointment-set-rates)
- Autos chinos usados: iProfesional (31/08/2026) compara cuánto se deprecian frente a otras marcas. La baja reventa se asocia a la desconfianza en repuestos y posventa (según el resumen de la búsqueda). [iProfesional](https://www.iprofesional.com/autos/463346-cuanto-se-deprecian-los-autos-chinos-usados-frente-a-otras-marcas)

### Inferences
- **Gancho de conversación:** "Mandanos 4 fotos, el año y los km de tu auto y te decimos en el día cuánto te lo tomamos." Califica al lead, porque el que entrega un usado tiene intención real. Además da un segundo motivo para el seguimiento.
- Cotizar el usado en dos tiempos:
  1. rango por WhatsApp con guía ACARA o CCA más avisos;
  2. tasación firme en la concesionaria o a domicilio, con vigencia por escrito (por ejemplo, 7 días).
- Para marcas chinas, el miedo a la reventa puede frenar la compra. Hay que confirmar con GWM, Mitsubishi y Changan si existe algún programa de recompra o de usados certificados, y no prometer nada que no exista.
- Métricas: % de leads con usado; % de usados cotizados en 24 h; diferencia entre la cotización y la oferta firme; cierre de leads con usado contra leads sin usado.

### Gaps
- No encontré datos de conversión de herramientas online de "cotizá tu usado" en concesionarias argentinas, ni prácticas documentadas de concesionarias cordobesas.
- No verifiqué si Valparaiso tiene área de usados, ni las políticas de toma de las terminales (GWM, Mitsubishi, Changan).

## 5. Financiación (preaprobación y canales) y cómo mostrar el CFT sin incumplir

### Takeaway
La mitad de los 0 km del país se financia, y las financieras de las marcas ya superan a los bancos y a los planes de ahorro en el crédito prendario de 0 km. Ofrecer una simulación o preaprobación rápida por WhatsApp es probablemente la palanca de cierre más directa. La norma de publicidad vigente (Res. 446/2025) exige referir las cuotas y el CFT; el detalle tiene que estar en la web o en un canal alternativo. Detalles como el tamaño de letra conviene validarlos con un abogado.

### Cited Findings
**Mercado**
- ACARA, citada por El Economista (21/09/2026, datos de agosto de 2026). [El Economista](https://eleconomista.com.ar/autos/crecio-financiacion-0-km-alcanzo-50-patentamientos-n98310)
  - 22.439 prendas sobre 0 km (+0,4 % mensual, −14,2 % interanual), **49,9 % de los patentamientos**.
  - Acumulado 2026 en 0 km por canal:
    - financieras de marca 43,1 %;
    - planes de ahorro 41 %;
    - bancos 13,5 %.
  - En usados, los bancos cayeron de 61,5 % a 34,9 %.
- iProfesional (septiembre de 2026): 26.266 operaciones sobre 0 km, **52,3 %** de los patentamientos; "las marcas desplazan a bancos". [iProfesional](https://www.iprofesional.com/autos/467049-mas-del-50-de-las-ventas-de-autos-0km-fueron-financiadas)
- Patentamientos de octubre de 2026: 45.965 unidades (−12 % interanual, −8,4 % contra septiembre); de enero a octubre, 481.852 (−12,8 %). Sebastián Beato (ACARA) dijo que las marcas podrían profundizar bonificaciones y financiación. [Parabrisas](https://parabrisas.perfil.com/noticias/autos/patentamientos-de-octubre-2026-cayo-el-mercado-automotor-y-la-toyota-hilux-volvio-a-liderar-el-ranking.phtml)
  - Algunas notas usan otra base de comparación para octubre de 2025. Verificar contra el informe de ACARA.

**Bancos y promociones**
- Banco Nación (noviembre de 2026): [iProfesional](https://www.iprofesional.com/autos/468453-el-banco-nacion-bajo-la-tasa-de-los-prestamos-para-comprar-autos-0km-y-usados)
  - 25 % TNA preferencial, para quien cobra el sueldo en el banco, tiene su tarjeta y contrata el seguro ahí; 46 % TNA sin esas condiciones;
  - hasta el 100 % del valor, con tope de $50 millones;
  - ejemplo con $15 millones a 36 meses: primera cuota de $662.022 (25 %) contra $895.841 (46 %).
- Banco Ciudad: créditos para híbridos y eléctricos desde 20 % anual (23/07/2026). [iProfesional](https://www.iprofesional.com/autos/456510-banco-ciudad-ofrece-creditos-para-autos-hibridos-y-electricos-con-tasas-que-parten-del-20-por-ciento-anual)
- Tasa 0 % de marca en 12–24 cuotas (agosto de 2026). [Mundo Empresarial](https://mundoempresarial.ar/creditos-autos-tasa-0-agosto-2026/); análisis "¿es real la tasa 0?" [iProfesional](https://www.iprofesional.com/autos/452656-creditos-para-autos-es-real-la-tasa-0-o-es-solo-una-estrategia-de-marketing)
- Cox 2025: 48 % quiere pedir el crédito online y solo 33 % lo hace. Un comprador destaca "getting a quicker approval" online. [Cox (PDF)](https://www.coxautoinc.com/wp-content/uploads/2026/01/2025-Cox-Automotive-Car-Buyer-Journey-Press-Release.pdf)

**Normativa de publicidad**
- Resolución 446/2025 de la Secretaría de Industria y Comercio. [abogados.com.ar](https://abogados.com.ar/resolucion-4462025-secretaria-de-industria-y-comercio-ministerio-de-economia-una-nueva-regulacion-para-toda-publicidad-de-bienes-y-servicios/37857); [Marval O'Farrell Mairal](https://www.marval.com/publicacion/el-nuevo-regimen-de-la-publicidad-en-defensa-al-consumidor-17391); [texto oficial](https://www.argentina.gob.ar/normativa/nacional/resolución-446-2025-419693)
  - Vigencia: se publicó en el Boletín Oficial el 3/11/2025 y rige desde el 3/12/2025.
  - Reemplazos: deroga la Res. 12/2024 y remite a la Res. 4/2025 para la exhibición de precios.
  - Precio financiado en gráfica, radio, TV u otros medios: la cantidad y el monto de las cuotas y el CFT efectivo anual deben estar en la web o en un canal alternativo del anunciante. Según otro análisis, la referencia a esas condiciones va en la pieza principal.
  - Sanciones: las de la Ley 24.240 y el DNU 274/2019.
- Beccar Varela publicó el 27/07/2026 una nota sobre una "nueva simplificación sobre legales" en la Res. 446/2025. No la leí: puede haber un cambio posterior. [Beccar Varela](https://beccarvarela.com/novedades/resolucion-446-2025-nueva-simplificacion-sobre-legales-en-publicidades-que-ofrezcan-bienes-y-servicios/)
- Antecedente: la Res. 12/2024, ya derogada, exigía letra de 3 mm como mínimo y 4 s en pantalla para los legales en video. [abogados.com.ar](https://abogados.com.ar/la-publicidad-bajo-lupa-la-secretaria-de-industria-y-comercio-homogeniza-la-informacion/37904)

### Inferences
- **Paso a paso propuesto:** "simulación en el chat" con 3 opciones del mismo auto, cada una con cuota, anticipo, plazo, TNA y CFT, y el legal "Información general. No constituye oferta. Consultá CFT y condiciones vigentes":
  1. financiera de la marca (tasa 0 o baja, menos cuotas, más anticipo);
  2. banco (Banco Nación, Bancor u otro según el perfil);
  3. UVA o CER, con la aclaración de que la cuota se ajusta.
- Pedir enseguida los datos para la **preaprobación** (DNI, ingresos, tipo de empleo). Es lo que más acerca al cierre, y por WhatsApp es natural.
- El lead que pidió financiación y la vio preaprobada debería ser lead A.
- Cumplir con el proyecto: nunca "sin interés" ni "cuotas fijas" en promociones CER o UVA; CFT visible en cada placa o mensaje con cuotas; una landing o página con el detalle (exigencia de la Res. 446/2025).
- El vendedor necesita una **plantilla de cotización aprobada por legales** para no improvisar tasas por WhatsApp.

### Gaps
- **Bancor (Córdoba):** no encontré tasas vigentes de crédito prendario para 0 km ni convenios con concesionarias. Hay que consultarlo directo.
- Tampoco confirmé qué financieras de marca ofrecen hoy GWM, Mitsubishi y Changan en Argentina, ni sus tasas.
- Norma sobre el tamaño y el color del CFT: encontré menciones a una exigencia de "CFT destacado, al menos 3 veces más grande" (Res. 240-E/2017 o similar), pero no pude confirmar la fuente ni si sigue vigente después de la 446/2025. **Validarlo con un abogado** antes de diseñar placas.
- No leí la nota de La Nación del 21/06/2026 sobre la caída de las compras en cuotas. [La Nación](https://www.lanacion.com.ar/autos/las-razones-por-las-que-de-un-dia-para-el-otro-la-gente-dejo-de-comprar-autos-en-cuotas-nid21062026/)

## 6. CRM y herramientas usadas por concesionarias argentinas

### Takeaway
El CRM automotor local más documentado es **Tecnom** (La Plata). Tiene un conector de WhatsApp con varios agentes, un bot, módulo de pruebas de manejo, integración con la API de Conversiones de Meta (CAPI) y su precio no es público. **Kommo** es la alternativa general, más barata, centrada en WhatsApp e Instagram (USD 20–45 por usuario y por mes en 2026, contrato mínimo de 6 meses). Las funciones que más importan: que todo lead entre solo al CRM, asignación automática, registro del origen, recordatorios de seguimiento y devolver a Meta qué leads compraron.

### Cited Findings
- Tecnom:
  - Empresa: CRM con IA para la industria automotriz, con base en La Plata, Argentina. [ZoomInfo](https://www.zoominfo.com/c/tecnom/459203260)
  - Precio: no es público; depende del nivel de automatización y la cantidad de usuarios. [Capterra](https://www.capterra.com/p/10048698/Tecnom/)
  - Funciones:
    - conector de WhatsApp: cada mensaje se registra como lead y se deriva al vendedor; "todos los leads ingresan al CRM sin excepción" [Tecnom](https://intercom.help/tecnom/es/articles/12956663-conector-whatsapp-tecnom);
    - Tecnom Chat: varios agentes sobre una misma línea de WhatsApp, con asignación automática [Tecnom Chat](https://intercom.help/tecnom/es/articles/12634460-tecnom-chat);
    - plantillas de WhatsApp [Tecnom](https://intercom.help/tecnom/es/articles/12933394-plantillas-de-whatsapp);
    - integración con la API de Conversiones de Meta (CAPI) [Tecnom](https://intercom.help/tecnom/es/articles/16036153-integracion-con-la-api-de-conversiones-de-meta-capi);
    - parámetros UTM para identificar el origen [Tecnom](https://intercom.help/tecnom/es/articles/13514765-guia-de-parametros-utm).
- Kommo (2026): [Kommo, actualización de precios](https://www.kommo.com/es/blog/actualizacion-precios-kommo/); [Kommo, planes](https://www.kommo.com/es/precios/comparar-planes/); [SetSmart](https://setsmart.io/blog/kommo-precios)
  - Precios por usuario y por mes: Básico USD 20, Avanzado USD 30 y Pro USD 45. Desde el 1/09/2026 hay USD 5 de aumento para clientes nuevos y precio regional.
  - Condiciones:
    - suscripciones de 6, 9, 12 o 24 meses, sin pago mensual;
    - WhatsApp incluido en los planes pagos;
    - los créditos de IA se cobran aparte por encima de cierto volumen.
  - Varias fuentes de terceros todavía muestran USD 15 y 25 (desactualizado).
- Foureyes (2025): 15,2 % de los leads calificados nunca se cargó en el CRM. [Foureyes](https://www.foureyes.io/blog/2026-automotive-dealer-benchmarks-report)
- Pied Piper 2026: las fallas de integración entre el sistema de gestión (DMS), la web, el CRM, la IA y los canales de salida tapan leads perdidos. [DealershipGuy](https://news.dealershipguy.com/p/dealers-are-responding-faster-than-ever-to-web-leads-but-automation-risks-linger-2026-02-24)

### Inferences
- Funciones mínimas que el CRM tiene que tener:
  1. Entrada automática de WhatsApp, Instagram DM, formularios de Meta y Mercado Libre.
  2. Asignación por turnos y alerta si nadie responde en 5 min.
  3. Etapas del embudo (consulta → calificado → turno → asistió → prueba → propuesta → venta → entrega).
  4. Campos de calificación (usado, financiación, plazo, modelo, palabra clave).
  5. Tareas de seguimiento con fecha.
  6. Envío de "venta" a Meta por CAPI, para que Meta optimice por compradores y no por curiosos.
  7. Tablero semanal.
- Si la terminal (GWM o Mitsubishi) ya le impone un CRM o un portal de leads a la red, conviene usar ese y no duplicar. Hay que verificarlo.
- Para una concesionaria chica, Kommo con 5 usuarios cuesta del orden de USD 150–225 por mes más mensajes de WhatsApp (cuenta propia sobre precios publicados; verificar). Tecnom es más específico del rubro, pero hay que pedir cotización.

### Gaps
- No investigué DealerNet, Salesforce Automotive Cloud ni HubSpot para concesionarias argentinas: ni costos ni casos locales.
- No hay costos públicos de Tecnom.
- No sé qué CRM o portal de leads exigen GWM Argentina, Mitsubishi o Changan a su red.

## 7. Equipo dedicado a leads (BDC) o vendedores: dotación e incentivos

### Takeaway
Las guías de la industria de EE. UU. hablan de un agente de BDC (equipo dedicado a atender leads y sacar turnos) por cada ~80–200 leads de internet al mes. Para una concesionaria del tamaño probable de Valparaiso, lo práctico es un modelo híbrido: 1 persona (o el bot más 1 persona) que responde, califica y agenda, y vendedores que reciben al cliente, hacen la prueba y cierran. No encontré evidencia sólida sobre esquemas de pago.

### Cited Findings
- Rework (guía 2026): 1 agente de BDC cada 80–100 leads de internet por mes y 1 gerente cada 6–8 agentes. Sugiere empezar con unos 3 agentes. [Rework](https://resources.rework.com/libraries/automotive-sales-growth/bdc-operations-setup)
- Foro DealerRefresh: las respuestas van de 75 a 400 leads por agente según la estructura, y la mayoría de los experimentados dice 100–200 leads nuevos por mes. [DealerRefresh](https://forum.dealerrefresh.com/threads/how-many-leads-per-bdc-rep-each-month.4354/latest)
- Un proveedor cuenta que un grupo apuntaba a 150 leads o llamadas por agente y por mes y terminó cerca de 250. [Numa](https://numa.com/blog/how-to-structure-a-modern-dealership-bdc-team)
- Si un agente logra 75 % de asistencia y otro 45 % con leads parecidos, es un problema de entrenamiento, no de calidad del lead (proveedor). [Numa, métricas de BDC](https://numa.com/blog/bdc-metrics-dealerships-should-track-beyond-calls-made)
- Maritz: cierre de leads de internet en un BDC, 10–15 %. [Maritz](https://maritz.com/?p=14866)
- Pied Piper 2026: el riesgo está en el traspaso del bot a personas no entrenadas. [DealershipGuy](https://news.dealershipguy.com/p/dealers-are-responding-faster-than-ever-to-web-leads-but-automation-risks-linger-2026-02-24)

### Inferences
- Con menos de ~150 leads calificados por mes: una persona de "primer contacto" (puede ser un vendedor de guardia rotativo), más el bot fuera de horario.
- Con más de 150: una persona dedicada, con incentivo por **turno que asiste** y no por turno agendado (inferencia: evita llenar la agenda de turnos flojos).
- Metas por persona: tiempo de primera respuesta, % de leads contactados, % de turnos, % de asistencia, % con datos completos en el CRM.
- Los vendedores que aparecen en los videos (contenido MOF) deberían ser los que reciben esos leads. Así hay continuidad ("te escribe Juan, el del video del Eado"), y se presentan como vendedores según CLAUDE.md.

### Gaps
- No encontré datos confiables sobre esquemas de pago de BDC (fijo más bono por turno, asistencia o venta), ni datos argentinos sobre estructuras de BDC en concesionarias.

## 8. Reseñas (Google) y programas de referidos

### Takeaway
Casi todos los consumidores leen reseñas, y el factor que más aparece en las reseñas positivas de concesionarias es la persona que atendió. En las negativas domina la mala comunicación. Google prohíbe incentivar reseñas y pedirlas solo a los clientes contentos ("filtrar"). En Argentina, los concursos o sorteos condicionados a una compra están prohibidos por el DNU 274/2019, así que un programa de referidos debería ser un beneficio directo y no un sorteo atado a la compra. Validarlo con un abogado.

### Cited Findings
- BrightLocal, Local Consumer Review Survey 2026 (1.002 adultos de EE. UU., 11/02/2026): [BrightLocal](https://www.brightlocal.com/research/local-consumer-review-survey/); [PinMeTo, resumen](https://www.pinmeto.com/news/brightlocal-local-consumer-review-survey-2026/)
  - Lectura:
    - 97 % lee reseñas;
    - 41 % las lee "siempre" (29 % el año anterior).
  - Efecto:
    - 85 % es más propenso a elegir el negocio tras reseñas positivas;
    - a 77 % lo desaniman las negativas;
    - 54 % visita la web después de una reseña positiva;
    - 49 % confía en las reseñas tanto como en una recomendación personal.
  - Plataformas:
    - Google es el 71 % del uso de reseñas (83 % en 2025);
    - se usan en promedio 6 sitios;
    - las herramientas de IA subieron como fuente de recomendaciones locales.
- Widewail, reseñas de concesionarias en EE. UU.:
  - 5,5 millones de reseñas de Google en 2025 (+25 %). [DealershipGuy, 28/01/2026](https://news.dealershipguy.com/p/dealership-reviews-surge-in-2025-but-communication-issues-hit-sales-teams-hard-2026-01-28)
  - El personal aparece en el 82 % de las reseñas positivas de ventas y en el 65 % de las de servicio. [DealershipGuy, 28/01/2026](https://news.dealershipguy.com/p/dealership-reviews-surge-in-2025-but-communication-issues-hit-sales-teams-hard-2026-01-28)
  - La comunicación aparece en el 42 % de las reseñas negativas de Google. [DealershipGuy](https://news.dealershipguy.com/p/dealership-communication-issues-mentioned-in-42-of-negative-google-reviews)
- Google, política de contenido: prohíbe las reseñas incentivadas (pago, descuento, bienes o servicios gratis u otro beneficio). [Google](https://support.google.com/contributionpolicy/answer/16597558)
  - También prohíbe desalentar las negativas o pedir solo a clientes contentos ("review gating"). [Podium](https://www.podium.com/article/review-gating)
  - En 2022 se informó que Google sacó una línea explícita sobre el filtrado; las guías posteriores lo siguen dando como prohibido. [Search Engine Roundtable](https://www.seroundtable.com/google-removes-maps-review-gating-policy-34002.html)
- Argentina, DNU 274/2019 (Lealtad Comercial), art. 14: prohíbe concursos, certámenes o sorteos en los que participar dependa, en todo o en parte, de comprar un producto o contratar un servicio. Otras promociones con premios o regalos están permitidas salvo prohibición expresa. Las reglamenta la Res. 248/2019, modificada por la 538/2019. [abogados.com.ar](https://abogados.com.ar/dnu-2742019-el-tratamiento-de-las-promociones-de-venta-en-el-nuevo-regimen-de-lealtad-comercial/23403); [Marval](https://www.marval.com/publicacion/nuevo-regimen-de-lealtad-comercial-en-la-argentina-13349)

### Inferences
- **Pedido de reseña sistemático:**
  - **a todos** los clientes, sin filtrar, el día de la entrega (QR en la placa o carpeta de entrega, más un WhatsApp a las 48 h con el enlace directo a Google);
  - sin premio a cambio;
  - pedir que mencionen al vendedor ayuda a que la reseña sea concreta.
- Responder **todas** las reseñas en 48 h. Las negativas, con nombre y una solución.
- Las reseñas son reales: el contenido no puede inventar testimonios (CLAUDE.md). Se puede citar una reseña real de Google con el permiso del cliente.
- **Referidos:**
  - beneficio directo y documentado (por ejemplo, un service bonificado o accesorios para quien refiere cuando el referido compra), con bases escritas;
  - sin sorteos atados a la compra;
  - validar la forma legal y el tratamiento impositivo con un asesor.
  - Inferencia: es más seguro un beneficio de posventa que efectivo.
- Métrica: reseñas nuevas por mes y nota promedio en Google; % de entregas con reseña; leads por referido y su cierre.

### Gaps
- No hay datos argentinos ni cordobeses sobre el peso de las reseñas de Google en la elección de concesionaria.
- No pude confirmar el texto vigente de la Res. 248/2019 aplicado a referidos, ni el tratamiento impositivo de los premios por referir.

## 9. Posventa: retención, recompra y reputación (con foco en marcas chinas)

### Takeaway
La posventa es la objeción principal para las marcas chinas en Argentina: repuestos, continuidad de la marca y valor de reventa. Para una concesionaria oficial, un taller propio confiable y visible es argumento de venta, no solo de retención. Los estudios de J.D. Power muestran que reparar bien a la primera y hacer seguimiento después de la entrega sostienen la lealtad.

### Cited Findings
- J.D. Power:
  - CSI EE. UU. 2025: la satisfacción con el service se mantuvo; la frenan las esperas largas para turno, las fallas de comunicación y el 12 % de reparaciones que no quedan bien en la primera visita. [J.D. Power](https://jdpower.com/business/press-releases/2025-us-customer-service-index-csi-study)
  - CSI México 2025: [J.D. Power México](https://www.jdpower.com/business/press-releases/2025-mexico-customer-service-index-csi-study)
    - 63 % volvería para trabajos pagos si la reparación salió bien a la primera, contra 28 % si no;
    - 88 % vuelve al concesionario que le vendió el auto.
    - Es el mercado latinoamericano más comparable que encontré.
  - SSI EE. UU. 2025: 22 % de los compradores quiere un seguimiento sobre las funciones del auto después de la entrega, y según la cobertura al 53 % de ellos nunca le llega. La lectura del 53 % es ambigua entre las fuentes. [J.D. Power](https://www.jdpower.com/business/press-releases/2025-us-sales-satisfaction-index-ssi-study); [CarPro](https://www.carpro.com/blog/porsche-tops-j.d.-power-2025-u.s.-sales-satisfaction-study)
- La Nación (23/04/2026, entrevista a Frasle Mobility): [La Nación](https://www.lanacion.com.ar/autos/como-sera-la-postventa-de-los-autos-chinos-en-la-argentina-nid23042026/)
  - muchas marcas chinas llegan sin una posventa armada, y el comprador duda de los repuestos, del service a largo plazo y de qué pasa si la marca se va;
  - el mercado de repuestos independiente respondió más rápido que las terminales.
- Perfil: el abastecimiento de algunas piezas sigue siendo un desafío, y la posventa sería decisiva para el éxito de las marcas chinas. [Perfil](https://www.perfil.com/noticias/reperfilar/faltan-repuestos-advertencias-del-mercado-de-autos-chinos.phtml)
- iProfesional (31/08/2026): la baja reventa de los usados chinos se vincula con la desconfianza en repuestos y posventa. [iProfesional](https://www.iprofesional.com/autos/463346-cuanto-se-deprecian-los-autos-chinos-usados-frente-a-otras-marcas)
- iProfesional: más del 30 % de las concesionarias argentinas ya vende autos chinos (solo leí el título). [iProfesional](https://www.iprofesional.com/autos/458459-inedito-mas-del-30-por-ciento-de-las-concesionarias-de-argentina-ya-venden-autos-chinos.amp)
- Un directivo vinculado a GWM dice que su estrategia es "una posventa robusta: talleres propios, técnicos certificados". Lo vi en un resumen de búsqueda, no en la nota completa: verificar. [Mercado](https://mercado.com.ar/movilidad/autos-chinos-crecen-en-patentamientos-ganan-terreno-en-electrificacion-y-buscan-despejar-prejuicios-en-argentina)
- Widewail: el personal aparece en el 65 % de las reseñas positivas de service. [DealershipGuy](https://news.dealershipguy.com/p/dealership-reviews-surge-in-2025-but-communication-issues-hit-sales-teams-hard-2026-01-28)

### Inferences
- **La posventa como argumento de venta:** en la propuesta y en el contenido (MOF "¿Auto chino? ¿Y si se rompe?"), mostrar:
  - el taller propio;
  - el stock de repuestos;
  - los técnicos certificados;
  - la garantía con su letra chica (Eado 5 años o 150.000 km y batería 8 años; ORA 05 7 años; H7 7 años, según los datos de CLAUDE.md, a verificar).
- **Contacto después de la entrega:**
  - día 3: llamada del vendedor y tutorial de funciones por WhatsApp (video corto de CarPlay, modos EV/HEV, carga);
  - día 30: control;
  - primer service agendado desde la entrega;
  - pedido de reseña y de referido en los momentos de satisfacción alta.
- Métricas de posventa: % de clientes que vuelven al primer service en la concesionaria; % de reparaciones bien hechas a la primera; nota del service en Google; recompra o referidos a 12 y 24 meses.

### Gaps
- No hay encuestas argentinas de 2025–2026 con números sobre la confianza en la posventa de marcas chinas.
- No hay datos de retención de service en concesionarias argentinas.
- No verifiqué la red de service ni la disponibilidad de repuestos de GWM, Haval, Changan y Mitsubishi en Córdoba.

## 10. Casos con números de concesionarias que mejoraron la conversión de leads

### Takeaway
Hay pocos casos públicos con números de punta a punta, y los que hay son de EE. UU. o de proveedores. El caso más sólido es Napleton (EE. UU.): primero en respuesta a leads cuatro años seguidos, con mensaje más llamada dentro de la hora y 82 % de conexión. No encontré un caso argentino verificado que vaya de lead a venta.

### Cited Findings
- Napleton Automotive Group (EE. UU.):
  - n.º 1 en el ranking de grupos de Pied Piper cuatro años seguidos (2025), con índice 91, el primero en superar 90;
  - modelo: responder por texto o email y llamar dentro de la hora, que según el grupo conecta con el 82 % de los interesados.
  - [DealershipGuy](https://news.dealershipguy.com/p/napleton-automotive-group-ranks-1-in-digital-lead-response-four-years-in-a-row-2025-05-06)
- Subaru: la marca con mejor índice en Pied Piper ILE 2025. Sus concesionarias usaron varios canales el 71 % de las veces, contra 49 % de promedio. [Business Wire](https://www.businesswire.com/news/home/20250302920512/en/subaru-dealers-rank-highest-in-2025-auto-industry-study-measuring-response-to-website-customers)
- Pied Piper 2026: Infiniti lidera con 82, Cadillac 77, Honda 76. No informa ventas. [DealershipGuy](https://news.dealershipguy.com/p/dealers-are-responding-faster-than-ever-to-web-leads-but-automation-risks-linger-2026-02-24)
- Ford Argentina duplicó los leads con Instagram Direct (caso de Sinch, proveedor; mide leads, no ventas). [Sinch](https://sinch.com/es/blog/concesionarios-de-autos-apps-de-mensajeria/)
- Cliengo dice que sus concesionarias clientes bajan 45 % el tiempo de respuesta a cotizaciones (proveedor, sin metodología). [Cliengo](https://guiawabusiness.cliengo.com/whatsapp-autos)
- Foureyes (2025): la tasa de compra sobre leads de venta subió de 10,2 % a 11,7 % en un año, y los canales pagos tuvieron la mejor tasa. [Foureyes](https://www.foureyes.io/blog/2026-automotive-dealer-benchmarks-report)

### Inferences
**Tablero semanal propuesto para Valparaiso Motors.** Todas las metas son inferencias de los benchmarks citados; hay que ajustarlas con una línea de base de 60–90 días.

**1. Volumen y origen**
- Consultas totales y leads calificados, por video, palabra clave, anuncio, Mercado Libre y entradas sin cita.
- % con origen identificado: meta 100 %.

**2. Velocidad**

| Métrica | Meta | Base |
|---|---|---|
| Primera respuesta automática | < 1 min | |
| Primera respuesta humana en horario | mediana < 5 min | |
| Leads con respuesta humana < 15 min | ≥ 90 % | DAS: 61 % de la industria |
| Leads sin seguimiento en 24 h | 0 % | Foureyes: 62,8 % de la industria |

**3. Embudo**

| Paso | Meta | Base |
|---|---|---|
| Contacto logrado | ≥ 80 % | Napleton: 82 % |
| Turno | ≥ 40 % de los contactados | Foureyes |
| Asistencia | ≥ 60 % | |
| Prueba de manejo | ≥ 80 % de los que asisten | CDK: 91–95 % de los compradores prueba |
| Cierre | ~35–40 % de los que asisten | Foureyes |
| Venta total | 8–12 % de los leads calificados | Foureyes 11,7 %; Maritz 10–15 % |
| Tiempo de lead a venta | medirlo | |

**4. Palancas**
- % de leads con simulación de financiación enviada y con CFT.
- % con preaprobación.
- % con usado cotizado en 24 h.
- Cierre con y sin usado o financiación.

**5. Calidad del dato:** % de leads cargados en el CRM, con meta 100 % (base Foureyes: 15,2 % sin cargar), y % con todos los campos de calificación.

**6. Después de la venta**

| Métrica | Meta |
|---|---|
| Entregas con reseña en Google | ≥ 30 % (inferencia; sin benchmark encontrado) |
| Clientes que vuelven al primer service | medirlo |
| Leads por referido | medirlo |

**Cierre del circuito:** mandar las ventas a Meta por CAPI. Así se compara el costo por venta de cada video (por ejemplo, el reel de 150 mil vistas y 0 leads contra los reels con CTA) y no solo el costo por lead.

### Gaps
- No encontré casos argentinos ni latinoamericanos verificados con números de lead a venta antes y después de cambiar el proceso.
- Los casos de proveedores (Cliengo, Sinch, Zenvia) no publican metodología.
- Tampoco encontré datos del tamaño de Valparaiso: volumen mensual de leads, cantidad de vendedores, ventas por mes. Sin esos datos las metas de dotación y conversión son orientativas.
