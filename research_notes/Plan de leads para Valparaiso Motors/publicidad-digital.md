# Canales digitales pagos y propios que generan leads y ventas para concesionarias (2025–2026), aplicado a Valparaiso Motors (Córdoba)

> Notas de investigación, 24/11/2026. Casi todos los benchmarks con números son de **EE. UU.** (LocaliQ, WordStream, NADA, Cox). **No encontré benchmarks confiables de costo por lead automotriz para Argentina ni para LatAm.** Los casos de Meta/WhatsApp están **reportados por las propias empresas**: Meta aclara en cada página que los resultados no necesariamente se repiten. Todo lo que dice "Inferencia" es razonamiento mío a partir de las fuentes, no un dato.
>
> Contexto interno (de `/home/user/web/CLAUDE.md`): un reel llegó a ~150 mil vistas y no trajo ningún lead. Las vistas eran de curiosos de todo el país, no de compradores locales. Ya existe una tienda oficial en Mercado Libre (GWM y Mitsubishi). Ideas ya planteadas: palabra clave por video, DM automático (ManyChat) con botón a WhatsApp, promoción local a ~50 km con objetivo de mensajes y placas de financiación en carrusel.

## 1. Meta (Facebook/Instagram): formularios vs. anuncios a WhatsApp vs. Messenger, catálogo automotor, Conversions API, radio local, calidad de leads y costos

### Takeaway
Los casos automotrices de Meta más recientes y concretos usan **anuncios que llevan a WhatsApp con un agente o bot que califica** (Kia Italia, Kavak). Para los formularios instantáneos, las palancas de calidad son el formulario de **mayor intención** (Higher Intent), una o dos preguntas de calificación y el objetivo **Conversion Leads** con el CRM conectado por Conversions API. Ese objetivo, según la documentación de Meta, **solo funciona con formularios instantáneos, no con WhatsApp**. Los anuncios de inventario automotor (catálogo de vehículos) existen en la API de Meta, pero **no pude confirmar que estén disponibles en Argentina**. No hay un costo por lead automotriz publicado para Argentina.

### Cited Findings
**Anuncios que llevan a WhatsApp (Click-to-WhatsApp), casos automotrices**
- **Kia Italia** (resultados reportados por la empresa, en 4 semanas). Usó anuncios en Facebook e Instagram que llevaban a WhatsApp, a un agente de IA hecho por Infobip, socio de Meta. El agente juntaba nombre, email, teléfono y código postal y contestaba sobre precio, equipamiento, disponibilidad, versiones y financiación. Después derivaba al cliente al concesionario más cercano para cotizar o hacer una prueba de manejo. — [WhatsApp Business: Kia Italia](https://whatsappbusiness.com/resources/success-stories/kia-italia/)
  - Resultados: **144 leads calificados**, **116 pedidos de cotización**, **40X de retorno sobre la inversión publicitaria**, 10,3 mensajes por conversación en promedio y **53 % menos de costo por auto vendido** que su esquema habitual de anuncios a WhatsApp sin agente. Fuentes de la medición: Ads Manager, Infobip y el CRM de Kia. — [WhatsApp Business: Kia Italia](https://whatsappbusiness.com/resources/success-stories/kia-italia/)
  - Ventas directas: la página que leí dice **5**, pero un resumen de búsqueda de la misma página decía **8**. Conflicto sin resolver: citar 5, que es lo que leí directamente. — [WhatsApp Business: Kia Italia](https://whatsappbusiness.com/resources/success-stories/kia-italia/); ver también [Infobip: Kia Italia](https://www.infobip.com/customer/kia-italia)
- **Kavak** (autos usados, LatAm; la página de Meta es de 2026 y apunta a México, aunque no lo confirma).
  - Combinó anuncios que llevan a WhatsApp con mensajes de marketing a clientes registrados que se habían enfriado, usando Meta Business Agent.
  - **1 de cada 3** personas que iniciaron una conversación desde un anuncio terminó como lead calificado y pasó a ventas.
  - Los anuncios a WhatsApp captaron leads con **8 veces más eficiencia** que los mensajes de marketing salientes solos.
  - El agente manejó 489 conversaciones en las primeras dos semanas.

  Resultados reportados por la empresa. — [WhatsApp Business: Kavak](https://whatsappbusiness.com/resources/success-stories/kavak/)
- **Arabian Automobiles (Nissan, Dubái):** en una prueba A/B, combinar anuncios a WhatsApp con anuncios al sitio web rindió más que usar un solo destino. Dato tomado del resumen de búsqueda; no leí la página entera. — [WhatsApp Business: Arabian Automobiles](https://business.whatsapp.com/resources/success-stories/arabian-automobiles-company)

**Formularios instantáneos: calidad del lead**
- El formulario de "mayor intención" (Higher Intent) agrega una pantalla donde la persona revisa y confirma sus datos antes de enviar. Baja los envíos accidentales y el volumen. Los especialistas recomiendan comparar la tasa de turnos o de ventas, no la cantidad de formularios, y esperar 2 o 3 semanas antes de sacar conclusiones. — [Jon Loomer: leads de calidad](https://www.jonloomer.com/how-to-get-high-quality-leads-from-facebook-lead-ads/); [Social Media Examiner](https://www.socialmediaexaminer.com/how-to-capture-more-qualified-leads-with-facebook-ads/)
- Recomendación práctica: 1 o 2 preguntas de calificación sobre el producto, el plazo o el presupuesto, no sobre la situación personal (las preguntas de finanzas o salud pueden traer problemas). — [Jon Loomer](https://www.jonloomer.com/how-to-get-high-quality-leads-from-facebook-lead-ads/); [Zapier](https://zapier.com/blog/facebook-lead-ads-best-practices)
- El "filtrado de leads" de Meta pone una pregunta de opción múltiple al principio del formulario y no deja enviarlo si la respuesta no califica. Advertencia: sumar muchas preguntas baja mucho el volumen. — [Jon Loomer: Lead Filtering](https://www.jonloomer.com/lead-filtering-quality-of-meta-lead-ads/amp/)
- Nota: todo lo anterior es consejo de especialistas (blogs), no documentación de Meta ni datos de concesionarias.

**Conversions API para CRM (objetivo "Conversion Leads")**
- Meta dice que integrar el CRM y usar el objetivo de rendimiento **Conversion Leads** "puede traer leads de mejor calidad, con más probabilidad de convertir". Ese objetivo **hoy solo es compatible con los formularios instantáneos de Facebook e Instagram** (Lead Ads). Página actualizada el 17/12/2025. — [Meta for Developers: Conversions API for CRM](https://developers.facebook.com/docs/marketing-api/conversions-api/conversion-leads-integration)
- La especificación de eventos aclara que esta optimización solo admite leads nativos de formularios generados en Facebook o Instagram. Actualizada el 26/04/2025. — [Meta: especificación de eventos](https://developers.facebook.com/documentation/ads-commerce/conversions-api/conversion-leads-integration/payload-specification)
- Hay un FAQ con un control previo para saber si el negocio es apto. Actualizado el 24/03/2026. — [Meta: FAQ Conversion Leads](https://developers.facebook.com/documentation/ads-commerce/conversions-api/conversion-leads-integration/faq)
- Make cita una prueba A/B interna con 1.031 anunciantes (28/07 al 11/08/2025): en promedio, **21 % menos de costo por lead de calidad** con Conversion Leads que con el objetivo Leads. Es un dato de un proveedor, no independiente. — [Make: Meta Conversions API for CRM](https://www.make.com/en/blog/meta-make-conversions-api-for-crm)
- Zapier recomienda optimizar hacia una etapa del CRM que anticipe la venta y que ocurra dentro de los 28 días desde que entra el lead. — [Zapier: guía de calidad de leads de Meta](https://zapier.com/blog/meta-guide-to-better-lead-quality/)

**Anuncios de inventario automotor (catálogo de vehículos)**
- La API de Meta documenta los "Automotive Ads": necesitan un catálogo de Facebook en el que cada producto es una oferta de vehículo única, con conjuntos de vehículos (subconjuntos filtrados; uno con todo el catálogo viene creado). — [Meta for Developers: Auto Ads](https://developers.facebook.com/docs/marketing-api/auto-ads); [Meta: crear un catálogo automotor](https://developers.facebook.com/docs/marketing-api/auto-ads/guides/catalog)
- También están los "Automotive Model Ads" (catálogo de modelos y ofertas), donde cada oferta registra los mercados o regiones en que vale. — [Meta: Automotive Model Ads](https://developers.facebook.com/docs/marketing-api/auto-ads/guides/aoa)
- **No encontré una lista oficial de países.** Un proveedor de feeds dice que son "mundiales" "al momento de escribir", sin fecha: no verificado. — [Feedoptimise](https://www.feedoptimise.com/blog/how-to-create-vehicle-ads-feed-for-google-meta-tiktok)

**Costos de referencia (no automotrices de Argentina)**
- WordStream/LocaliQ, Facebook 2025 (todas las industrias, EE. UU.): costo por lead promedio **USD 27,66** (+21 % interanual) y CTR de campañas de leads 2,59 %. — [WordStream: Facebook Ads Benchmarks 2025](https://www.wordstream.com/blog/facebook-ads-benchmarks-2025); [ppc.land](https://ppc.land/facebook-ad-costs-jump-21-as-lead-campaigns-struggle-while-traffic-ads-thrive/)
- WordStream 2026 (todas las industrias): costo por lead **USD 27,39** y tasa de conversión de campañas de leads **8,54 %**. La tabla por industria (fila automotriz) no se pudo leer: la página dio error 403. Las cifras salen del resumen de búsqueda. — [WordStream: Facebook Ads Benchmarks 2026](https://www.wordstream.com/blog/facebook-ads-benchmarks-2026); [Search Engine Land](https://searchengineland.com/facebook-ad-costs-fall-as-traffic-and-lead-performance-improvements-report-488433)
- Superads, **Argentina, todas las industrias** (sin rubro automotor), costo por lead en Meta:
  - **media ~110,65**, inflada por valores extremos;
  - **mediana ~36,05**, la que la propia página da como más típica.

  Problemas de la fuente: no aclara la moneda (usa "$"), el período es contradictorio (el encabezado dice nov. 2025–oct. 2026 y el texto, jul. 2025–jun. 2026) y no dice el tamaño de la muestra. **Confiabilidad baja.** — [Superads: CPL Argentina](https://www.superads.ai/facebook-ads-costs/cost-per-lead/argentina)

### Inferences
- **Canal principal para Valparaiso: anuncios que llevan a WhatsApp con objetivo "Mensajes"**, en un radio de ~30–50 km alrededor del concesionario (el dueño ya había pensado en ~50 km). La experiencia es la que ya usa la gente en Argentina, y los dos casos de LatAm y Europa más concretos (Kavak y Kia) califican dentro de la conversación.
  - Un mensaje de bienvenida con respuestas rápidas cumple el rol de las preguntas de calificación: modelo, forma de pago (contado, prendario, UVA, usado como parte de pago) y cuándo piensa comprar.
- **Formularios instantáneos como segundo canal, no el principal:** formulario de mayor intención, una sola pregunta de calificación ("¿Cuándo pensás cambiar el auto? 0–30 días / 1–3 meses / solo miro") y el teléfono de WhatsApp precargado.
  - Su ventaja: es el único formato que puede usar Conversion Leads con el CRM. Tiene sentido cuando el CRM marque qué leads llegaron a turno o a venta.
- **El caso de "150 mil vistas, 0 leads"** se explica por el objetivo (alcance o interacción), la segmentación nacional y que no había un destino de conversación. El cambio de fondo es pasar a objetivo **Mensajes o Leads con ubicación "personas que viven en"** el radio, no "personas que están en o viajaron a".
- **Catálogo automotor:** antes de armar un feed, probar en Ads Manager si la cuenta argentina deja crear un catálogo "Vehículos". Con pocas versiones de 0 km (Eado Plus, ORA 03, ORA 05, H6, H7, Deepal), un carrusel o colección manual probablemente alcanza.
- **Presupuesto de Meta:** como no hay un costo por lead automotriz local, el primer mes tiene que ser una prueba que mida el **costo por conversación calificada** y el **costo por venta** en el CRM propio. No conviene planificar con los benchmarks de EE. UU.

### Gaps
- Disponibilidad de Automotive Inventory Ads y Automotive Model Ads en Argentina: no confirmada. Hay que revisarlo en la cuenta publicitaria o preguntarle a un representante de Meta.
- Costo por lead o por conversación en Meta para concesionarias de Argentina o LatAm: ninguna fuente confiable.
- Benchmarks de Messenger para autos: no encontré nada.
- Fila automotriz de WordStream 2025 y 2026 (CTR, CPC, conversión, costo por lead): bloqueada (403).
- Tasa de leads de formulario que llegan a venta en autos: sin fuente confiable.

## 2. Google: Search por modelo + ciudad, Performance Max, Perfil de Empresa, YouTube, anuncios de vehículos y benchmarks

### Takeaway
Los **anuncios de vehículos de Google (vehicle ads) no están disponibles en Argentina**. Para concesionarias en Argentina, Google queda en **Search** con palabras de modelo y ciudad más el **Perfil de Empresa**. El único benchmark sólido es de EE. UU. (LocaliQ 2026): concesionarias de 0 km con CPC de USD 2,48, conversión de 6,73 % y costo por lead de USD 35,87.

### Cited Findings
- Los vehicle ads de Google están disponibles en **Australia, Canadá y EE. UU.**, y en beta abierta en Francia, Alemania, Italia, España, Países Bajos y Reino Unido. **Argentina no figura.** — [Google Ads Help: Vehicle ads overview](https://support.google.com/google-ads/answer/11189169?hl=en)
- LocaliQ, benchmarks automotrices de búsqueda 2026. Datos del 01/04/2025 al 30/06/2026, 1.983 campañas en EE. UU. (Google Ads y Microsoft Ads), con medianas. Actualizado el 29/09/2026. — [LocaliQ: 2026 Automotive Search Ad Benchmarks](https://localiq.com/blog/automotive-search-advertising-benchmarks/)

  | Rubro | CTR | CPC | Conversión | Costo por lead |
  |---|---|---|---|---|
  | Automotriz en general | 6,60 % | USD 3,49 | 9,21 % | USD 33,12 |
  | Concesionarias de 0 km en general | 8,23 % | USD 2,48 | 6,73 % | **USD 35,87** |
  | Usados en general | 8,33 % | USD 1,73 | 3,53 % | USD 59,74 |
  | Concesionarios Nissan | — | — | — | USD 25,03 |
  | Concesionarios Hyundai | — | — | — | USD 56,26 |
  | Concesionarios Toyota | — | — | — | USD 103,54 |

  - Variación interanual: CPC +12,58 %, costo por lead +4,09 %, conversión +2,56 %.
- Cox Automotive, Car Buyer Journey 2025 (EE. UU., 2.344 compradores). Fuentes online que usan los compradores: sitios de terceros 75 %, sitios de concesionarias 59 %, **buscadores 41 %**, minoristas online de usados 30 % y **redes sociales 26 %**. La tabla no define bien la métrica. — [Cox Automotive: resumen 2025 (PDF)](https://www.coxautoinc.com/wp-content/uploads/2026/03/2025-Cox-Automotive-Car-Buyer-Journey-Study-Summary.pdf); [Cox: 2025 Car Buyer Journey para concesionarias](https://www.coxautoinc.com/retail/resources/2025-car-buyer-journey-dealers/)
- Mismo estudio: el proceso total de compra fue de poco menos de 14 h y el **19 %** de los compradores usó IA (25 % en 0 km). — [Cox Automotive: resumen 2025 (PDF)](https://www.coxautoinc.com/wp-content/uploads/2026/03/2025-Cox-Automotive-Car-Buyer-Journey-Study-Summary.pdf)
- En EE. UU., el marketing en buscadores es la categoría más grande del gasto publicitario de las concesionarias: ~20–21 % del total en 2025, según datos de NADA. — [Car Dealership Guy](https://news.dealershipguy.com/p/dealer-ad-spend-nears-10-billion-as-digital-marketing-dominates)

### Inferences
- **Search local con poco presupuesto:** grupos por modelo con concordancia de frase o exacta. Por ejemplo "Changan Eado Plus precio", "Haval H6 híbrida Córdoba", "GWM ORA 03 Córdoba", "concesionaria GWM Córdoba", "Mitsubishi Córdoba 0km".
  - Ubicación por presencia, radio de 50 km, extensiones de llamada y de ubicación, y un destino que sea WhatsApp o una página del modelo con botón de WhatsApp.
  - Las búsquedas de modelos chinos nuevos probablemente tienen poco volumen en Córdoba, así que el gasto se autolimita. Es intención alta y barata de probar.
- **Performance Max** no tiene sentido sin conversiones bien medidas (llamada, clic a WhatsApp con etiqueta, formulario). Dejarlo para después de tener 30 o más conversiones por mes medidas. Esto es razonamiento mío, no un dato de las fuentes.
- **Perfil de Empresa de Google:** gratis y prioritario. Fotos reales de las unidades, publicaciones por modelo, respuesta a las reseñas, botón de WhatsApp o llamada, y categoría y horario correctos.
  - Recordatorio de CLAUDE.md: no inventar ni pedir reseñas falsas.
- **YouTube:** reutilizar los reels educativos como Shorts. Para campañas pagas de video con objetivo de leads no encontré benchmarks automotrices de 2025–2026.

### Gaps
- CPC y volumen de búsqueda de palabras de autos en Argentina o Córdoba: no encontré fuentes públicas. Se pueden estimar con el Planificador de palabras clave de la cuenta.
- Rendimiento de Performance Max o de las campañas locales en concesionarias de LatAm: sin datos.
- Benchmarks de YouTube para generar leads automotrices: no investigado a fondo (sin fuentes).

## 3. Mercado Libre Autos, deRuedas y Autocosmos: cómo llegan los leads, planes y costos, optimización y tiempo de respuesta

### Takeaway
Mercado Libre es el portal de referencia y ya tiene una red de **casi 5.000 concesionarias** (julio de 2026). Las concesionarias publican por **paquetes**, con **destaques** que mejoran la posición en el listado, pero **los precios de esos planes no son públicos**. En EE. UU., los sitios de terceros son la fuente online más usada por los compradores (75 %) y la segunda o tercera categoría de gasto de las concesionarias. No encontré datos sobre qué parte de los leads de las concesionarias argentinas viene de portales.

### Cited Findings
- Para particulares, publicar un vehículo en Mercado Libre Argentina es gratis. — [Mercado Libre Argentina: vender auto](https://www.mercadolibre.com.ar/l/vender-auto)
- Las concesionarias se registran como "profesional" (con el email del negocio) y publican sus vehículos con **paquetes**. Mercado Libre recomienda sumar **destaques** para posicionarse en el listado. Esto viene de las páginas "publicá como concesionario" de Colombia y Chile y del blog de Argentina, según el resumen de búsqueda; el blog de Argentina dio error 403. — [Mercado Libre Colombia: publicá como concesionario](https://www.mercadolibre.com.co/h/0km/publica-como-concesionario); [Mercado Libre Chile: publicá como concesionario](https://www.mercadolibre.cl/h/0km/publica-como-concesionario); [Mercado Libre Argentina: blog concesionaria](https://www.mercadolibre.com.ar/vehiculos/blog/concesionaria)
- Los listados de Argentina tienen filtros separados de "Concesionaria" y "Tiendas oficiales". Por ejemplo, el listado de autos 0 km 2026 de concesionarias en Córdoba. — [Mercado Libre: concesionarias, Córdoba, 2026](https://autos.mercadolibre.com.ar/nafta/automatica/concesionaria/2026/_PciaId_cordoba)
- En julio de 2026 Mercado Libre anunció un paso más en la compraventa de autos, con una red de **casi 5.000 concesionarias**. La nota se centra en los usados y en la alianza con Flash para inspecciones. — [iProfesional, 16/07/2026](https://www.iprofesional.com/autos/439160-como-es-vender-autos-en-la-nueva-plataforma-de-mercado-libre)
- En EE. UU., los "sitios de listados de terceros" son la categoría de gasto que sigue a los buscadores en el presupuesto de las concesionarias (NADA 2025). — [Car Dealership Guy](https://news.dealershipguy.com/p/dealer-ad-spend-nears-10-billion-as-digital-marketing-dominates)
- Cox 2025: el 75 % de los compradores usa sitios de terceros, la fuente online más usada (EE. UU.). — [Cox Automotive: resumen 2025 (PDF)](https://www.coxautoinc.com/wp-content/uploads/2026/03/2025-Cox-Automotive-Car-Buyer-Journey-Study-Summary.pdf)

**Tiempo de respuesta (en general, no de Mercado Libre)**
- Rework cita un estudio con clientes incógnitos de 2025: el **67 %** de las concesionarias oficiales no responde los leads de internet en la primera hora y otro **18 %** no responde nunca. No es de Argentina y es una fuente secundaria: no encontré el estudio original. — [Rework: tiempo de respuesta de leads](https://resources.rework.com/es/libraries/automotive-sales-growth/lead-response-time-optimization)
- Informe de Meta sobre mensajería (22 mercados, Argentina incluida): el **72,4 %** de los consumidores tiene más ganas de comprarle a una marca que responde rápido. La nota que lo cita es sobre gastronomía. — [Mercado (Ruta Digital)](https://mercado.com.ar/ruta-digital/responder-rapido-por-mensajeria-puede-aumentar-hasta-60-las-reservas-en-gastronomia)

### Inferences
- Mercado Libre es el canal de **inventario con intención de compra**, donde el comprador ya está comparando. Para Valparaiso, que ya tiene tienda oficial, lo que más rinde probablemente es:
  1. responder las preguntas en minutos, en horario extendido, con alguien asignado o un bot que derive a WhatsApp, siempre que las reglas de Mercado Libre lo permitan (verificar);
  2. publicaciones completas: fotos propias de la unidad real, precio o "consultar financiación", ficha técnica con las aclaraciones (NEDC/WLTP) y video;
  3. **destaques sobre el modelo con exceso de stock (Eado Plus)**;
  4. sumar la tienda o las unidades de Changan si corresponde (verificar cómo se presentan como concesionario Changan).
- Medir Mercado Libre aparte en el CRM, con el origen "ML pregunta" o "ML WhatsApp", para comparar su costo por venta con Meta.
- deRuedas y Autocosmos: no investigados con fuentes. No asignarles presupuesto hasta pedir tarifas y estadísticas de contactos.

### Gaps
- Precios vigentes de los paquetes y destaques de Mercado Libre para concesionarias en Argentina: no son públicos. Hay que pedírselos al ejecutivo de la tienda oficial.
- Qué parte de los leads de las concesionarias argentinas sale de portales: no encontré datos.
- Herramientas de Mercado Libre para leads (WhatsApp, llamadas, integración con CRM) y efecto del tiempo de respuesta en su ranking: no confirmado.
- Planes, costos y rendimiento de deRuedas y Autocosmos: sin datos.

## 4. TikTok y YouTube para concesionarias: ¿traen leads o solo alcance? Formatos que convierten

### Takeaway
El video corto trae leads **cuando lleva a un formulario o a un mensaje y el que habla es un vendedor**. El caso con números más claro es de TikTok: formularios instantáneos más CRM, con **8.000 leads y 40 % calificados** para un concesionario Ford en Arabia Saudita. Los casos de vendedores influencers de EE. UU. muestran que el formato que vende es el del vendedor mostrando **unidades reales e inventario nuevo** y los **casos de clientes aprobados**. Sus números son autodeclarados.

### Cited Findings
- **Mohamed Yousuf Naghi Motors** (Ford, Arabia Saudita): anuncios In-Feed de TikTok con formularios instantáneos integrados al CRM, **3,8 millones de impresiones, más de 8.000 leads y 40 % de calificación**. Publicado por TikTok, que aclara que los resultados pasados no garantizan los futuros. — [TikTok for Business: Mohamed Yousuf Naghi Motors](https://ads.tiktok.com/business/en-US/inspiration/mohamed-yousuf-naghi-motors-tiktok-success-story)
- **Andrea Anderson** (Andrews Cadillac, EE. UU.; "Andrea Sells Cadillacs"): ~500 mil seguidores en Instagram y 170 mil en TikTok. Vende usados con videos de las unidades recién ingresadas, antes de que aparezcan en el sitio del concesionario. — [CBT News: Used Car Week 2026](https://www.cbtnews.com/used-car-week-2026-andrea-anderson/)
- Hay notas del rubro sobre concesionarias que usan TikTok con millones de vistas para vender (un concesionario de Wisconsin con 8 millones de vistas). Solo vi el título: no leí el contenido. — [CBT News: concesionario de Wisconsin](https://www.cbtnews.com/how-this-wis-dealership-is-leveraging-8m-views-on-tiktok-to-sell-more-cars/)
- No encontré ningún caso independiente o auditado que una los videos de un vendedor de TikTok con una cantidad verificada de ventas en 2025–2026. Los números vienen de la plataforma, de medios del rubro o de los propios vendedores. (Esto es una conclusión de la búsqueda, no la afirmación de una fuente.)

### Inferences
- Coincide con lo que aprendió la cuenta: los **reels animados educativos** (TOF) traen alcance nacional pero no leads por sí solos. Para leads, el formato con más respaldo es el **vendedor en cámara con la unidad real**: recorrido por el auto, entrega del día o "llegó esta unidad", más una oferta concreta y un destino (WhatsApp o formulario) en el radio local.
  - Va en línea con los guiones MOF que ya existen (20 ideas, "Soy [nombre], vendedor de Valparaiso Motors").
- **Videos de entregas:** solo con permiso del cliente, sin testimonios inventados y sin que suene a reseña armada.
- **TikTok pago** para Córdoba: probar recién después de Meta. Tiene formularios instantáneos (según el caso anterior); no verifiqué si permite WhatsApp como destino en Argentina.
- **YouTube Shorts:** sirve para reciclar los reels sin costo extra. No hay evidencia de que traiga leads locales.

### Gaps
- Casos de concesionarias o vendedores de Argentina o LatAm en TikTok con resultados de leads o ventas: no encontré.
- Costos de TikTok Ads por lead automotriz en LatAm: sin datos.
- Un caso de vendedor estadounidense que arrancó en abril de 2025 y dice traer ~1.000 leads pagos y ~300 DMs orgánicos por mes apareció en un resumen de CBT News, pero no pude identificar la URL exacta. No usarlo como dato.

## 5. Automatización de WhatsApp y comentario con palabra clave → DM (ManyChat y otros): configuraciones y resultados

### Takeaway
La automatización con mejor evidencia en autos es la de **WhatsApp con un agente o bot que califica y deriva al vendedor**: Kia Italia, con 53 % menos de costo por auto vendido; Kavak, con 1 de cada 3 conversaciones calificada; y en **Argentina**, Toyota Zento en postventa. La de **comentario con palabra clave → DM** (ManyChat) es técnicamente simple y está permitida por la API oficial, pero **no encontré ningún caso con resultados en concesionarias**.

### Cited Findings
- **Toyota Zento (Argentina):** concesionario con tres sucursales en el sur del Gran Buenos Aires, datos de enero de 2025 a enero de 2026.
  - Configuración: mensajes de utilidad de WhatsApp con recordatorios de service predictivos y personalizados, hechos con un modelo de Volanti (proveedor de WhatsApp Business) sobre datos del CRM, para clientes que aceptaron compartir su kilometraje. Por WhatsApp se confirman turnos, se aprueban presupuestos y el taller manda fotos y videos.
  - Resultados (reportados por la empresa): **40X de retorno**; frente al email, 9,5X de apertura, 32,5X de respuesta y 50X de conversión; frente al call center, 2,1X de respuesta y 5X de conversión.
  - Es **postventa, no venta de 0 km**.

  — [WhatsApp Business: Toyota Zento](https://whatsappbusiness.com/resources/success-stories/toyota-zento/)
- **ACARA y RunOne (Argentina):** lanzaron un chatbot y un voicebot para extender a las **920 concesionarias** del país durante 2025.
  - Califican crédito con el DNI, tasan el usado, agendan fechas de entrega y hacen remarketing, 24 horas los 365 días.
  - Algunas concesionarias reciben pocos leads y otras **hasta 20.000 por mes**.
  - El 88 % de los posibles compradores busca información online y el 71 % espera una propuesta personalizada.

  — [Forbes Argentina, 06/01/2025](https://www.forbesargentina.com/negocios/las-concesionarias-40-ya-estan-marcha-acelerando-n65399)
- Kia Italia y Kavak: ver la sección 1. — [Kia Italia](https://whatsappbusiness.com/resources/success-stories/kia-italia/); [Kavak](https://whatsappbusiness.com/resources/success-stories/kavak/)
- Cliengo dice que las concesionarias que usan su herramienta de WhatsApp bajaron 45 % el tiempo de respuesta a las cotizaciones. Es un dato del proveedor, sin verificar. — [Cliengo: WhatsApp para autos](https://guiawabusiness.cliengo.com/whatsapp-autos)

**ManyChat: comentario → DM**
- El disparador puede ser una palabra clave puntual, cualquier comentario o los comentarios de un reel en particular, y se pueden excluir palabras. Funciona con la API oficial de Meta. — [ManyChat: guía de automatización de comentarios](https://manychat.com/blog/the-ultimate-guide-for-instagram-comment-automation/); [ManyChat: qué son las palabras clave](https://manychat.com/blog/what-are-keywords-ig/)
- Límite: el disparador de comentarios en publicaciones y reels de Instagram **solo se activa con el primer comentario** de cada usuario en esa publicación. Si vuelve a comentar la misma palabra, no se dispara de nuevo. — [ManyChat: ayuda](https://help.manychat.com/hc/en-us/articles/14281316989724); [ManyChat: guía](https://manychat.com/blog/the-ultimate-guide-for-instagram-comment-automation/)
- No encontré casos de concesionarias con resultados (las fuentes son el marketing de ManyChat).

### Inferences
**Flujo propuesto para Valparaiso**

1. **Orgánico (reel TOF/MOF):** "Comentá EADO". ManyChat manda un DM automático con 2 o 3 botones: "Precio y financiación", "Quiero verlo en el salón", "Solo estoy mirando". Los dos primeros llevan a WhatsApp con un mensaje ya escrito y un código por video ("Vengo del video EADO-NAFTA"). El tercero no se descarta: entra en una secuencia suave.
2. **Pago (anuncio a WhatsApp):** mensaje de bienvenida con preguntas frecuentes: "¿Qué modelo te interesa?", "¿Cómo pensás pagarlo? Contado / financiado / con mi usado", "¿Para cuándo?". Con 2 o 3 respuestas el lead ya queda calificado y pasa al vendedor con la etiqueta de origen.
3. **Tiempo de respuesta:** atención humana en minutos en horario comercial y respuesta automática fuera de horario que promete contacto a las 9 h. La única evidencia es general (Rework, Meta 72,4 %), pero empuja en esa dirección.
4. **Postventa (canal propio):** recordatorios de service por WhatsApp (modelo Toyota Zento). Fideliza y genera recompra o permuta, pero necesita opt-in y un CRM con kilometraje.

**Cuidados**
- Pedir el opt-in para mensajes de marketing.
- No prometer "sin interés" en las respuestas automáticas cuando la financiación ajusta por CER o UVA (sección 5 de CLAUDE.md).
- Que el bot no invente precios: que derive a una persona.

### Gaps
- Resultados medidos de comentario → DM en concesionarias: no hay casos.
- Precios actuales de ManyChat y de la API de WhatsApp para Argentina (costo por conversación de marketing o utilidad): no investigados.
- Cuánto rindió en la práctica el bot de ACARA y RunOne en 2025 (adopción, conversión): sin datos.

## 6. Retargeting y remarketing: visitantes del sitio, personas que vieron videos y secuencias para nutrir leads

### Takeaway
Encontré poca evidencia publicada y específica de autos sobre retargeting. Lo más concreto es Kavak: los anuncios a WhatsApp captaron **8 veces más** que los mensajes de marketing a clientes registrados que se habían enfriado, y las dos cosas funcionaron juntas. La propuesta para Valparaiso sale sobre todo de inferencias.

### Cited Findings
- Kavak combinó **mensajes de marketing de WhatsApp a clientes registrados que se habían enfriado** con anuncios a WhatsApp. Los anuncios fueron **8 veces más eficientes** captando leads que los mensajes salientes solos. — [WhatsApp Business: Kavak](https://whatsappbusiness.com/resources/success-stories/kavak/)
- El bot de ACARA y RunOne incluye remarketing a los interesados entre sus funciones. — [Forbes Argentina](https://www.forbesargentina.com/negocios/las-concesionarias-40-ya-estan-marcha-acelerando-n65399)
- Cox 2025: el 44 % de los compradores de 0 km hizo un recorrido mixto (online y en el salón), y los que hicieron más trámites online quedaron más satisfechos con el tiempo en la concesionaria. — [Cox Automotive: resumen 2025 (PDF)](https://www.coxautoinc.com/wp-content/uploads/2026/03/2025-Cox-Automotive-Car-Buyer-Journey-Study-Summary.pdf)

### Inferences
**Escalera de audiencias en Meta, todas limitadas al radio de Córdoba en el conjunto de anuncios**
1. **Personas que vieron el 50 % o el 95 % de los reels TOF** (el de EV/PHEV/HEV, el de créditos, el de "Hacé esta cuenta") e interacciones con el perfil en los últimos 30 a 90 días.
   - Así se recupera una parte útil de las ~150 mil vistas que no trajeron leads: los cordobeses que miraron casi todo el video.
2. Mostrarles **anuncios BOF** (placa animada de 6–8 s del modelo del video que vieron, con precio o financiación, CFT y aviso legal) que lleven a WhatsApp.
3. **Visitantes del sitio o de la página del modelo** (píxel y Conversions API web): carrusel de modelos y anuncio de prueba de manejo.
4. **Leads que no compraron:** secuencia por WhatsApp con opt-in, sin insistir. Por ejemplo, a la semana una comparativa de financiaciones, a las dos semanas el video del vendedor con la unidad y al mes una promo vigente verificada.
   - En paralelo, una audiencia personalizada de esos leads para excluirlos de la captación y mostrarles anuncios de cierre.
- Usar **exclusiones** (clientes que ya compraron) para no gastar de más, y suprimir a los que compraron hace poco salvo para postventa.

### Gaps
- Benchmarks de retargeting automotriz (CTR, costo por lead, tasa de cierre de las audiencias de video) de 2025–2026: no encontré fuentes.
- Datos de secuencias de nutrición por WhatsApp en concesionarias argentinas: no hay.

## 7. Presupuesto: gasto de marketing por auto vendido, reparto entre canales y medición (seguimiento de llamadas, UTM, atribución en el CRM)

### Takeaway
La única referencia firme es de EE. UU.: en 2025 las concesionarias oficiales gastaron **USD 739 en publicidad por auto 0 km vendido** (USD 705 en 2024), con **74,9 % en digital**. Los buscadores son la categoría más grande (~20 %), siguen los portales y las redes sociales tienen el 14,2 %. En Argentina no hay un dato equivalente publicado. Para medir, la evidencia apunta a conectar el CRM con las plataformas: Conversion Leads en Meta, y el CRM como fuente de los resultados en el caso Kia.

### Cited Findings
- **NADA 2025 (EE. UU.):** el gasto publicitario de las concesionarias llegó a **USD 9.960 millones**, récord. Fueron **USD 739 por vehículo vendido** (+USD 34) y el digital fue el **74,9 %** del total. Publicado el 07/05/2026. — [Car Dealership Guy](https://news.dealershipguy.com/p/dealer-ad-spend-nears-10-billion-as-digital-marketing-dominates)

  | Canal | Parte del gasto |
  |---|---|
  | Buscadores | ~20 % ("uno de cada cinco") |
  | Portales de terceros | justo detrás de buscadores (sin cifra) |
  | Redes sociales | 14,2 % (12,7 % el año anterior) |
  | TV | 10,5 % |
  | Radio | 6,9 % |
  | Correo postal | 5,6 % |
  | Diarios | 2,1 % |

- Otro resumen da para 2025 un presupuesto promedio de **USD 586.246 por concesionaria** (= USD 739 por 0 km según el cálculo de NADA) y para 2024 **USD 543.539 (USD 705 por 0 km)**, el **0,74 %** de las ventas. Dato del resumen de búsqueda; conviene contrastarlo con el PDF de NADA. — [TVB: datos de NADA 2024](https://www.tvb.org/news/industry-news/data-into-dollars-key-insights-from-2024-nada-data/); [NADA Data](https://www.nada.org/NADAdata)
- Primer semestre: **USD 791 por 0 km en 2026** contra **USD 722 en 2025**. Fuente secundaria; no la leí entera. — [Ritner Digital](https://www.ritnerdigital.com/blog/why-are-dealer-advertising-costs-per-vehicle-sold-rising-in-2026and-what-can-dealerships-do-about-it)
- **Medición:** Kia Italia midió sus resultados con Ads Manager, Infobip y su CRM, hasta el costo por auto vendido. — [Kia Italia](https://whatsappbusiness.com/resources/success-stories/kia-italia/)
- Meta: el objetivo Conversion Leads usa los eventos del CRM para optimizar por calidad, solo con formularios instantáneos. — [Meta: Conversions API for CRM](https://developers.facebook.com/docs/marketing-api/conversions-api/conversion-leads-integration)
- Contexto de Argentina: ~405.000 unidades vendidas en 2024 y una meta de más de 500.000 en 2025, "apostando a las ventas digitales". — [Forbes Argentina](https://www.forbesargentina.com/negocios/las-concesionarias-40-ya-estan-marcha-acelerando-n65399)

### Inferences
- **No conviene trasladar los USD 739 por auto a Argentina:** los costos de los medios, el volumen y el margen son distintos. Sirve solo como techo de referencia y para la idea de **presupuestar por auto vendido** y no por mes.
- **Fórmula para el presupuesto de prueba** (todas las tasas son supuestos que hay que reemplazar con datos propios):
  - **Presupuesto mensual = ventas extra buscadas × costo por venta aceptable.**
  - **Costo por venta = costo por conversación ÷ (tasa de calificación × tasa de cierre de los calificados).**
  - *Ejemplo ilustrativo, no un benchmark:* con USD 5 por conversación (supuesto), 1 de cada 3 calificada (dato de Kavak, en otro mercado) y 1 de cada 20 calificados que compra (supuesto), el costo por venta es 5 ÷ (1/3 × 1/20) = **USD 300**.
- **Reparto inicial sugerido para probar 4–6 semanas** (inferencia, sin fuente local):
  - ~60–70 % en Meta: anuncios a WhatsApp en el radio más retargeting de personas que vieron videos;
  - ~15–20 % en Google Search de modelo + Córdoba;
  - ~10–20 % en destaques de Mercado Libre para el Eado Plus;
  - después, mover el dinero según el **costo por venta del CRM**, no según el costo por lead.
- **Medición mínima viable**
  - Un código por anuncio o video en el mensaje de WhatsApp ya escrito ("EADO-01").
  - UTM en todos los enlaces.
  - Una etiqueta de origen en el CRM o en la planilla (Meta-WA, Meta-Form, Google, ML, orgánico-palabra clave, salón).
  - Etapas del lead: conversación → calificado → turno o prueba → venta.
  - Revisión semanal del costo por calificado y por venta.
  - Para las llamadas desde Google, usar el número de seguimiento de Google Ads o un número aparte.
- Medir también lo que pide CLAUDE.md: retención a 3 s, comentarios que nombran un modelo y mensajes que piden precio.

### Gaps
- Gasto de marketing por auto vendido en Argentina o LatAm y reparto por canal de las concesionarias argentinas: no hay fuentes públicas.
- Tasa de cierre de leads digitales en concesionarias argentinas: sin datos.
- Herramientas de seguimiento de llamadas disponibles en Argentina y su costo: no investigado.

## 8. Casos de Argentina y LatAm (lanzamientos de marcas chinas: BYD, GWM, Changan) y resultados publicados por agencias

### Takeaway
Encontré **pocos casos publicados de Argentina con métricas de ventas**. El más sólido es **Toyota Zento**, en postventa por WhatsApp. A eso se suma el contexto de ACARA y RunOne (bots en 920 concesionarias) y el caso LatAm de Kavak. **No encontré casos de lanzamientos de BYD, GWM o Changan en Argentina con resultados de leads**, ni agencias argentinas con métricas auditables.

### Cited Findings
- Toyota Zento (Argentina, 2025–2026): WhatsApp en postventa, con 40X de retorno y 5X de conversión frente al call center (reportado por la empresa). — [WhatsApp Business: Toyota Zento](https://whatsappbusiness.com/resources/success-stories/toyota-zento/)
- ACARA y RunOne: chatbot y voicebot para las 920 concesionarias en 2025. Argentina tiene 920 concesionarias, casi todas multimarca, de 540 empresarios. — [Forbes Argentina](https://www.forbesargentina.com/negocios/las-concesionarias-40-ya-estan-marcha-acelerando-n65399)
- Kavak (LatAm, 2026): 1 de cada 3 conversaciones desde un anuncio terminó en lead calificado. — [WhatsApp Business: Kavak](https://whatsappbusiness.com/resources/success-stories/kavak/)
- Mercado Libre: casi 5.000 concesionarias operan en la plataforma (julio de 2026). — [iProfesional](https://www.iprofesional.com/autos/439160-como-es-vender-autos-en-la-nueva-plataforma-de-mercado-libre)

### Inferences
- Valparaiso tiene la oportunidad de **generar su propio benchmark** en 6 semanas con la medición de la sección 7, porque no hay datos públicos del rubro en Córdoba.
- Los ejemplos de marcas chinas que lanzan en otros mercados con anuncios a WhatsApp y un bot que contesta sobre el auto (Hyundai Brasil con el HB20, según un resumen de búsqueda sin URL confirmada) sugieren el mismo patrón: el contenido educativo sobre una tecnología nueva (PHEV, HEV, EV) tiene que terminar en una **conversación**, no en un comentario.

### Gaps
- Resultados de lanzamientos de BYD, GWM o Changan en Argentina en canales digitales: no encontré nada publicado.
- Casos de agencias argentinas con costo por lead o por venta automotriz: no encontré fuentes confiables.
- Caso Hyundai Brasil (HB20 con chatbot): solo apareció en un resumen de búsqueda, sin la página leída ni métricas.

## 9. Playbook propuesto para Valparaiso Motors (síntesis de las secciones 1–8)

### Takeaway
Pasar de "reels virales nacionales" a un sistema de **conversación local medida**:
- el orgánico educativo atrae;
- el retargeting en el radio de Córdoba convierte a los que miraron;
- los anuncios a WhatsApp con 2 o 3 preguntas de calificación generan las conversaciones;
- Search y Mercado Libre captan la intención que ya existe;
- todo se mide hasta la venta con un código de origen.

### Cited Findings
- Los anuncios a WhatsApp con un agente que califica redujeron 53 % el costo por auto vendido en Kia Italia. — [Kia Italia](https://whatsappbusiness.com/resources/success-stories/kia-italia/)
- 1 de cada 3 conversaciones desde un anuncio terminó en lead calificado en Kavak. — [Kavak](https://whatsappbusiness.com/resources/success-stories/kavak/)
- El objetivo Conversion Leads con el CRM solo funciona con formularios instantáneos. — [Meta](https://developers.facebook.com/docs/marketing-api/conversions-api/conversion-leads-integration)
- No hay vehicle ads de Google en Argentina. — [Google](https://support.google.com/google-ads/answer/11189169?hl=en)
- Concesionarias de 0 km en Search en EE. UU.: costo por lead USD 35,87 y conversión 6,73 %. — [LocaliQ](https://localiq.com/blog/automotive-search-advertising-benchmarks/)
- En EE. UU. se gastan USD 739 por 0 km vendido y el 74,9 % va a digital. — [Car Dealership Guy / NADA](https://news.dealershipguy.com/p/dealer-ad-spend-nears-10-billion-as-digital-marketing-dominates)

### Inferences
**Estructura de campañas (inferencia)**

| Etapa | Campaña | Audiencia | Pieza | Destino | Métrica |
|---|---|---|---|---|---|
| TOF | Orgánico + reels promocionados con poco presupuesto | Córdoba, ~50 km ("vive en") | Reels educativos (EV/PHEV/HEV, "Hacé esta cuenta", créditos) | Comentá la palabra clave → DM → WhatsApp | Retención a 3 s, comentarios con modelo, DMs |
| MOF | Anuncios a WhatsApp | Radio de 50 km, amplia o Advantage+ dentro del radio | Vendedor con la unidad real (guiones MOF), comparativas | WhatsApp con mensaje ya escrito y código | Costo por conversación y por calificado |
| BOF | Retargeting | Vieron el 50–95 % de los videos, interactuaron con el perfil o visitaron el sitio (90 días) | Placas animadas de 6–8 s y carrusel de financiación por modelo (CFT + aviso legal) | WhatsApp o formulario de mayor intención | Costo por turno o prueba de manejo |
| Intención | Google Search | Modelo + Córdoba, concesionaria GWM/Mitsubishi | Anuncios de texto con precio "desde" verificado | WhatsApp, llamada o página del modelo | Costo por contacto |
| Intención | Mercado Libre | Compradores del portal | Publicaciones completas + destaques (Eado Plus) | Preguntas y contacto | Tiempo de respuesta, costo por venta |
| Propio | WhatsApp de postventa | Clientes con opt-in | Recordatorios de service | Turno | Turnos, recompra o permuta |

**Primeras 6 semanas (inferencia)**
1. **Semana 0:**
   - Ubicación "vive en" un radio de ~50 km.
   - WhatsApp Business con catálogo, mensaje de bienvenida y preguntas frecuentes.
   - ManyChat con palabra clave por video.
   - Planilla o CRM con origen y etapas.
   - UTM y códigos por anuncio.
   - Píxel y Conversions API en el sitio.
2. **Semanas 1–4:** prueba A/B de anuncios a WhatsApp contra formulario de mayor intención, con el mismo creativo y el mismo radio. Retargeting de los que vieron videos. Search por modelo.
3. **Semanas 5–6:** pasar el presupuesto al canal con menor **costo por venta**. Si los formularios tienen volumen y el CRM ya marca las ventas, activar Conversion Leads.

**Creativos (alineados con CLAUDE.md)**
- Un solo CTA: "Pedinos precio y financiación de cualquiera de nuestros autos".
- Vendedor real en cámara, unidades reales y entregas con permiso.
- Financiación con CFT y aviso legal. Nunca "sin interés" si ajusta por CER o UVA.

**Respuesta**
- Responsable asignado, objetivo de minutos en horario comercial y mensaje automático fuera de horario.
- Medir el tiempo de respuesta como un indicador más.

### Gaps
- Todo el reparto de presupuesto y los costos esperados para Córdoba son inferencias: no hay benchmarks locales. Hay que validarlos con la prueba de 6 semanas.
- Falta confirmar la disponibilidad de los anuncios de inventario automotor de Meta en Argentina, los precios de los destaques de Mercado Libre y los costos de la API de WhatsApp en Argentina.
