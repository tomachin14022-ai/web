# Presupuestos por WhatsApp para gente de oficio: la idea que escala sin tus horas

**La respuesta corta.** De las 26 ideas de los dos informes anteriores, la más escalable que además resuelve un problema real, casi no tiene competencia en su forma exacta y se puede construir solo con Claude Code es **"Presupuesto al Toque"** (nombre provisorio). Es un asistente por WhatsApp para electricistas, plomeros, gasistas, instaladores de aire acondicionado y pintores. Le mandás fotos del trabajo y un audio, y en dos minutos te devuelve un presupuesto en PDF con tu nombre. El PDF trae materiales con cantidades y precio de referencia del día, mano de obra, validez en días (clave con inflación), forma de pago y link de seña a tu propia cuenta de Mercado Pago. Saca **78 sobre 100** en escalabilidad. Cuota Verificada, la idea que rechazaste, saca **38**. La diferencia de fondo es una sola. En Cuota Verificada, conseguir cada cliente cuesta **horas tuyas** (visitas, demos, verificar a mano la financiación de cada concesionaria todas las semanas), y tus horas no se multiplican. Acá, conseguir cada cliente cuesta **plata** (anuncios que abren WhatsApp, más un pie en cada presupuesto que lo ven otros), y la plata sí se multiplica. El mercado tampoco se termina en Córdoba: en la Argentina hay 3,3 millones de cuentapropistas ([El Economista](https://eleconomista.com.ar/economia/record-cuentapropismo-argentina-adaptacion-heroica-o-senal-alarma-mercado-laboral-n92856)), y el producto sirve igual en cualquier país de habla hispana.

**El podio.** Medimos con la misma vara las 26 ideas y les pusimos cuatro filtros: problema real, poca competencia, que lo puedas hacer solo y números que cierren con su canal. De las que pasan, las tres más escalables son:

| Puesto | Idea | Escalabilidad (de 100) | Durabilidad (de 5) | En una línea |
|---|---|---|---|---|
| 1 | **Presupuesto al Toque**: presupuestos con IA por WhatsApp para oficios | **78** | 3 | La recomendada. El riesgo es que la gente de oficio, en su mayoría informal, pague |
| 2 | **Catálogo para IA**: app de Tiendanube que mantiene el catálogo cargado en ChatGPT Ads, Google y Meta | **76** | 1 | La más pura en escala (tienda de apps, cero horas por cliente), pero dura poco: OpenAI ya hizo gratis la versión para Shopify |
| 3 | **Turnos en Casa**: tablero del cuidado de un padre mayor (turnos, horas para el recibo de ARCA y gastos entre hermanos) | **66** | 4 | La más durable de las tres y el plan B. Escala menos: la parte de sueldos es solo argentina y Google está dominado por los diarios |

**Las cuentas (estimaciones propias, explicadas en la sección 5).** En el escenario base, Presupuesto al Toque necesita **unos 195 usuarios pagos para dejar USD 1.000 netos por mes**, contando que hay que reponer los que se van. Para **USD 10.000 netos** necesita **unos 1.800**, que es el 0,05 % de los cuentapropistas argentinos.

**Lo que no está probado.** Nadie pagó todavía por esto en la Argentina. El informe anterior descartó esta idea justamente porque "los oficios, en su mayoría informales, pagan poco", y la informalidad entre cuentapropistas es del 63,3 % ([La Gaceta](https://www.lagaceta.com.ar/nota/1134500/economia/alarma-laboral-cuentapropismo-volvio-niveles-pandemia-desplazo-al-empleo-calidad.html)). Lo que cambió es la vara: si lo que pedís es escalabilidad, esta idea tiene el canal y el mercado que a las demás les faltan, y la duda de si pagan se contesta en cuatro semanas, con un corte claro. Hay dos señales a favor, pero ninguna es prueba. YoFacturo ya les cobra a electricistas y plomeros planes desde ARS 20.000 por mes, con presupuesto en PDF armado a mano ([YoFacturo](https://yo-facturo.com/electricistas/)). Y en EE. UU. más de 40.000 contratistas usaron Handoff, que arma presupuestos con IA desde fotos (dato de la empresa) ([Business Wire](https://www.businesswire.com/news/home/20250519029610/en)).

**Cómo leer este informe.** Todo lo que tiene enlace es un dato con fuente. Lo que dice "est." es una estimación propia, y mostramos la cuenta. Los puntajes son juicios nuestros sobre la evidencia, no mediciones. Fecha de la investigación: 22/11/2026. Los pesos se pasan a dólares a **ARS 1.560**, el mismo valor del informe anterior, entre el MEP y el mayorista de mediados de noviembre ([Rava](https://www.rava.com/cotizaciones/historico/dolar-mep/2026/11/11/)). Ninguna cifra reemplaza hablar con clientes.

**Palabras que usamos.**
- **CAC:** lo que cuesta conseguir un cliente que paga. Puede ser plata (anuncios) u horas tuyas (visitas).
- **LTV:** lo que te deja un cliente en toda su vida. Se calcula así: precio por mes × margen bruto ÷ bajas por mes.
- **Margen bruto:** lo que queda de cada peso cobrado después de pagar lo que cuesta atender a ese cliente (IA, mensajes de WhatsApp, comisiones).
- **Bajas (churn):** porcentaje de clientes que se van cada mes.
- **Repago:** cuántos meses tarda un cliente en devolver lo que costó conseguirlo.
- **K (coeficiente viral):** cuántos clientes nuevos trae, en promedio, cada cliente.
- **Motor de crecimiento:** el circuito que trae clientes nuevos, que según la metodología Lean Startup puede ser **pegajoso** (crece porque nadie se va), **viral** (los clientes traen clientes) o **pago** (cada cliente deja más de lo que costó conseguirlo).

---

## 1. Qué quiere decir "escalable", con números

Una idea es escalable si los ingresos pueden crecer diez veces, de USD 1.000 a USD 10.000 por mes, mientras tus horas crecen como mucho al doble. Lo traducimos en seis umbrales. Salen de las habilidades `lean-startup` y `startup-metrics-framework` y de tu propio rechazo a Cuota Verificada.

**Tabla 1. Los seis umbrales de escalabilidad**

| # | Umbral | Valor que usamos | Por qué |
|---|---|---|---|
| 1 | Costo marginal | Margen bruto de **70 % o más** (ideal 80 %), contando IA, mensajes de WhatsApp, cobro y comisión de la tienda de apps. Alta de un cliente nuevo: **menos de 1 hora tuya**, o automática | Si cada cliente nuevo cuesta casi lo mismo que el anterior, no hay escala |
| 2 | Horas tuyas por cliente | **15 minutos por mes o menos** por cliente cuando llegás a 100 clientes | Con 400 clientes son 100 h por mes: es el techo de una persona |
| 3 | Canal sin vos en cada venta | **70 % o más** de los clientes nuevos llegan sin una reunión con vos, por alguna de estas vías: autoservicio (se registra y paga solo); viralidad incorporada con K de 0,3 o más; tienda de apps; socios que traen **20 clientes o más por acuerdo**; o anuncios con LTV/CAC de 3 o más | Es la diferencia con Cuota Verificada: allá cada venta es una visita |
| 4 | Mercado alcanzable | La meta de USD 10.000 no debe exigir más del **5 %** del mercado al que llega ese canal. El mercado tiene que ir más allá de Córdoba: la Argentina entera como mínimo, mejor América Latina o España | Si la meta exige quedarse con la mitad del mercado, el techo es el mercado |
| 5 | Defensa a escala | Algo que mejora con cada cliente: efecto de red, datos acumulados o costo de cambio | Sin esto, el que llega después con más plata se queda con todo |
| 6 | Economía del canal | **LTV/CAC de 3 o más** y **repago en 12 meses o menos**, con un CAC hecho de plata, no de horas tuyas | Son los mínimos de la habilidad `startup-metrics-framework` |

**Cómo se calcula el puntaje.** Cada idea recibe de 0 a 5 puntos en cinco dimensiones, con pesos. El canal pesa triple, porque fue lo que te hizo rechazar Cuota Verificada. El máximo es 50 y lo pasamos a 100.

**Tabla 2. Escala de puntos de cada dimensión**

| Dimensión (peso) | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|
| **Canal (×3)** | Autoservicio con viralidad incorporada, o tienda de apps con demanda probada | Autoservicio más búsqueda o anuncios en una categoría probada | Contenido o búsqueda que tarda; o socios que traen de 10 a 50 clientes por acuerdo | Venta por cliente a distancia, o un solo canal orgánico | Venta tuya, en persona y local |
| **Costo marginal (×2)** | Margen de 90 % o más | 80 a 90 % | 70 a 80 % | 50 a 70 % | Menos de 50 %, o trabajo humano en cada alta |
| **Horas por cliente (×2)** | Menos de 5 min por mes y alta automática | Menos de 15 min | 15 a 30 min | 30 a 90 min | Más de 1,5 h, o visitas |
| **Mercado (×2)** | Global o todo el mundo hispanohablante, con más de 100.000 clientes posibles | Varios países, o más de 50.000 en la Argentina | Argentina, de 10.000 a 50.000 | Argentina, de 1.000 a 10.000 | Menos de 1.000, o solo Córdoba |
| **Defensa (×1)** | Efecto de red fuerte | Datos propios y costo de cambio alto | Costo de cambio moderado | Débil | Copiable en semanas, o las plataformas lo dan gratis |

**Los cuatro filtros para entrar al podio.**
1. **Problema real:** alguien ya paga por algo parecido, o el dolor está documentado.
2. **Poca o ninguna competencia:** nadie hace esa configuración exacta en el mercado elegido, y la categoría de al lado no está saturada.
3. **Factible solo:** se puede hacer con Claude Code en menos de tres meses, sin licencias ni socios obligatorios.
4. **Economía:** LTV/CAC de 3 o más con su canal principal.

La durabilidad no es un filtro para el podio, porque pediste escalabilidad ante todo, pero se informa al lado. La recomendación final sí exige una durabilidad de 3 o más.

**La lección que aparece antes de mirar ninguna idea.** Un LTV/CAC alto no alcanza. Cuota Verificada tiene buenos números: con un abono de USD 125, LTV/CAC de 6,1 y repago de 3,3 meses (est.), mejores que los de la idea recomendada. Pero su CAC está hecho de horas tuyas, valuadas a USD 25 la hora (supuesto). Para llegar a USD 10.000 netos harían falta unas 115 concesionarias. Eso es el 70 % de las 163 que tienen la línea de Bancor en Córdoba ([Infonegocios](https://infonegocios.info/y-ademas/bancor-financia-el-50-de-los-autos-vendidos-en-la-provincia-suma-creditos-prendarios)), o recorrer el país. Además, la verificación semanal de la financiación se lleva 1 o 2 horas por concesionaria: unas 170 h por mes solo en eso (est.). Por eso Cuota Verificada pasa los filtros y aun así saca 38. El problema no son sus números por cliente, sino de qué está hecho cada cliente.

---

## 2. Las 26 ideas, medidas con la misma vara

Son las 12 del primer informe, las 6 validadas del segundo y las 8 candidatas de la primera ronda que tenían forma de negocio. Partimos dos ideas que escalan muy distinto según la versión: talleres y membresía, y Cuota Verificada y su variante de marketplace.

**Tabla 3. Motor, canal, costo, mercado, competencia y horas.** Las columnas de margen y horas son estimaciones. La competencia sale de las notas de validación y de la búsqueda nueva.

| # | Idea | Motor | Canal: ¿escala sin vos? | Margen (est.) | Mercado alcanzable | Competencia | Tus horas por cliente (est.) |
|---|---|---|---|---|---|---|---|
| 1 | Recepcionista de WhatsApp para centros de salud | Pegajoso | Visitas y recomendaciones en Córdoba. **No** | ≈ 79 %, más un día de instalación | Centros de 2 a 8 profesionales en la Argentina | Alta: AgendaPro vende "Recepcionista IA" a +ARS 30.000 por mes ([AgendaPro](https://agendapro.com/ar/planes)); Cliengo; el agente de Meta | 8 h de alta + 1–2 h/mes |
| 2 | Software de alquileres | Pegajoso | Calculadora en Google + prueba gratis + demo. **A medias** | ≈ 85 % | Inmobiliarias chicas del país (sin conteo) | Alta: 7 o más productos locales ([YoFacturo](https://yo-facturo.com/blog/sistema-gestion-inmobiliaria-alquileres/)) | 3–5 h de migración + 0,5 h/mes |
| 3 | Consorcios | Pegajoso | Venta directa a administradores, lenta. **No** | ≈ 85 % | Administradores del país | Alta: CONSO ([Capterra](https://www.capterra.es/software/1111352/CONSO)), Simple Solutions, HomeApp | 10 h o más de alta + 1 h/mes |
| 4 | Cobro de cuotas para clubes | Pegajoso | Comisiones directivas, una por una. **No** | ≈ 80 % | Clubes de barrio | Media: CuotaQ, YoFacturo, GymAr | 5 h + 1 h/mes |
| 5 | Automatización para estudios contables | Pegajoso | Consejos profesionales, un estudio por vez. **No** | ≈ 70 % (trabajo a medida) | Estudios del país | Media-alta: Aconpy, bot gratis del CPCE de Córdoba ([CPCE](https://web.cpcecba.org.ar/?p=62762)) | 10–20 h + 2 h/mes |
| 6 | Alta de proveedor para Vaca Muerta | Ninguno (proyectos) | Venta consultiva. **No** | ≈ 60 % | Más de 1.000 pymes certificadas en Neuquén ([LM Neuquén](https://mase.lmneuquen.com/empresas/vaca-muerta-como-las-pymes-neuquinas-buscan-entrar-al-negocio-las-grandes-empresas-n1251195)) | Media: agencias gratis, consultoras | 10–20 h por legajo |
| 7 | Localización de cursos | Pago (demos por mail) | Trabajo por pedido. **No** | ≈ 70 % | Global, en dólares | Alta: YouTube dobla gratis desde febrero de 2026 ([Social Media Today](https://www.socialmediatoday.com/news/youtube-expands-auto-dubbing-to-all-creators/811375/)) | 2–4 h por curso |
| 8 | Catálogo de Mercado Libre como servicio | Ninguno | Programa de socios de Tiendanube. **No** | ≈ 60 % | Vendedores del país | Media: consultoras desde USD 480/mes ([Algoritmo Digital](https://algoritmodigital.com.ar/cuanto-cobra-un-consultor-de-mercado-libre-2026/)) | 4–8 h/mes |
| 9 | Plantillas de Framer | Tienda (orgánico) | Buscador del marketplace. **Sí** | ≈ 95 % | Global | Saturada: 10.288 plantillas ([Steal What Works](https://stealwhatworks.com/blogs/news/framer-templates-over-10k-month-now)) | ≈ 0 por venta |
| 10 | App de Shopify o extensión de Chrome | Tienda | **Sí** | ≈ 90 % | Global | Saturada: la mitad de las apps se reparte el 0,6 % de los ingresos ([Barn2](https://barn2.com/blog/shopify-app-store-saturation/)) | Poco soporte |
| 11 | Datos y alertas para concesionarias | Pegajoso | Venta por concesionaria. **No** | ≈ 90 % | Techo de 815 a 1.200 concesionarias ([iProfesional](https://www.iprofesional.com/autos/458459-inedito-mas-del-30-por-ciento-de-las-concesionarias-de-argentina-ya-venden-autos-chinos)) | Sin mapear | 0,5 h/mes |
| 12 | Talleres de IA | Ninguno | Tiempo por plata. **No** | Es tu tiempo | Pymes del país | Alta | 4 h + preparación por taller |
| 13 | Membresía de video con Claude Code | Viral (contenido) | YouTube: escala **solo si hay audiencia** | ≈ 90 % | Hispanohablantes | Alta en lo general: Imperio Agéntico, 4.400 miembros ([Skool](https://www.skool.com/imperio/about)) | 10–20 h/mes fijas de comunidad |
| 14 | **Cuota Verificada** (referencia) | Pegajoso | Venta en persona por concesionaria. **No** | ≈ 92 % en plata, con verificación humana semanal | 163 con línea Bancor en Córdoba; de 815 a 1.200 en el país | Nadie en la Argentina; afuera tiende a ser gratis | 10–15 h de alta + 1–2 h/mes |
| 15 | Variante marketplace: "0 km con cuota y CFT", con cobro por contacto | Red de dos lados | Búsqueda e IA + concesionarias que se suman. **A medias** | ≈ 70 % | Concesionarias y compradores de 0 km del país | Alta: El Cero KM (más de 150 concesionarias y agente propio) ([Diego Ceredi](https://www.diegoceredi.com/blog/caso-elcerokm-agente-ia-autos-argentina)), Mercado Libre, deRuedas, Kavak | 2 h por concesionaria + compra de tráfico |
| 16 | **Turnos en Casa** (cuidado de mayores) | Pegajoso | Herramientas gratis en Google + contadores y agencias + hermanos que viven afuera. **A medias** | ≈ 72 % (WhatsApp ≈ USD 3–4 por familia) | 600.000 relaciones laborales de casas particulares con recibo obligatorio ([ARCA](https://servicioscf.afip.gob.ar/publico/sitio/contenido/novedad/ver.aspx?id=5737)), sin desglose de cuántas son cuidadoras | Parcial: Cuidarlos, Recibo Asistido gratis de ARCA, Domésticas al Día; MyFamily afuera | 1 h de alta asistida + 10 min/mes |
| 17 | Monitor GUDI de energía | Pegajoso | Cámaras industriales, venta consultiva. **No** | ≈ 60 % (socio ingeniero) | ≈ 6.000 empresas GUDI ([El Economista](https://eleconomista.com.ar/energia/la-letra-chica-energia-pymes-denuncian-pagan-doble-lo-acordado-n98498)) | Media-alta: Latin Energy, Powermeter, Energeia | 3 h + 1 h/mes |
| 18 | Protección contra voz clonada, vía instituciones | Socios (cada institución trae a sus clientes) | Cada acuerdo trae cientos o miles de familias, pero la venta es larga. **A medias** | ≈ 75 % | Aseguradoras, bancos y mutuales de habla hispana | Parcial: palabras clave gratis (Trust Onion), Truecaller, WhatsApp | 40–60 h por institución |
| 19 | EUDR para microimportadores | Pegajoso | Contacto directo con importadores españoles. **No** | ≈ 80 % | Microimportadores de la UE que compran directo | Alta: Coolx ([Coolx](https://coolx.earth/es/importadores)), EUDRReady gratis | 3–6 h por proveedor |
| 20 | Costeo gastronómico | Pegajoso | Visitas, o marca blanca para sistemas de caja. **No** | ≈ 85 % | Restaurantes del país | Alta: Fudo ya lee facturas con IA ([Fudo](https://fu.do/es-ar/precios/)) | 4 h + 1 h/mes |
| 21 | **Catálogo para IA** (app de Tiendanube) | Tienda + pegajoso | Tienda de apps de Tiendanube. **Sí** | ≈ 67 % con el 30 % de la tienda (≈ 97 % sin) | Más de 180.000 tiendas activas ([Tiendanube](https://www.tiendanube.com/compania)) | **Ninguna app de feed para ChatGPT en la tienda** (22/11/2026). Al lado: Feed Vivo y Feed XML. OpenAI ya hizo la de Shopify | ≈ 0 |
| 22 | Monotributo dentro de ChatGPT y Claude | Tienda de asistentes (sin datos) | Directorio de ChatGPT: 15.120 apps y ningún dato de instalaciones ([FourWeekMBA](https://fourweekmba.com/ai-chatgpt-apps-top-15000-after-a-75-jump-in-just-23-days/)) | ≈ 85 % | Monotributistas del país | Alta: Facturitas, con 5.000 activos ([iProUP](https://www.iproup.com/startups/69692-app-monotributistas-iaemitir-facturas-whatsapp-mercado-pago-tienda-nube-facturitas)), Tramitito, ARCA gratis | ≈ 0 + soporte fiscal |
| 23 | Monitor normativo (Boletín Oficial, BCRA, ARCA) | Pegajoso + contenido | Resumen gratis que lleva al pago. **Sí** | ≈ 90 % | Pymes reguladas y estudios del país | **Ocupado:** Indicadores.ar ya filtra el Boletín por industria y jurisdicción, gratis ([Indicadores.ar](https://indicadores.ar/pro?motivo=recorte)) | ≈ 0 |
| 24 | **Presupuestos con IA para oficios** | Pago + viral incorporado | Todo por WhatsApp, sin reunión. **Sí** | ≈ 70 % (IA + WhatsApp + usuarios gratis) | 3,3 millones de cuentapropistas; después, el mundo hispanohablante | **Baja en la forma exacta**: YoFacturo arma el PDF a mano ([YoFacturo](https://yo-facturo.com/electricistas/)); BudgAI sin reseñas ([Product Hunt](https://www.producthunt.com/products/budgai/reviews)); ChatGPT genérico | ≈ 0 de alta; 5 min/mes |
| 25 | Informe de un auto usado para el comprador | SEO, compra única | Google. Escala, pero **sin recurrencia** | ≈ 90 % | 1,88 millones de transferencias en 2025 ([El Economista](https://eleconomista.com.ar/autos/la-venta-autos-usados-alcanzo-su-record-historico-2025-n91863)) | Media: Datacar, Veraz Auto, Kavak cerca | ≈ 0 |
| 26 | "¿Qué dice la IA de tu negocio?" | Viral (diagnóstico gratis) + agencias | Diagnóstico gratis + agencias en marca blanca. **Sí** | ≈ 75 % (consultas a los modelos) | Pymes hispanohablantes | Media: GEO Metrics ([Ecosistema Startup](https://ecosistemastartup.com/geo-metrics-3-000-marcas-ya-optimizan-para-chatgpt/)), Local Falcon en unos 225 países ([Capterra](https://www.capterra.co.uk/software/1060015/local-falcon)) | 0,5–1 h/mes si incluye arreglos |

**Tabla 4. Números por cliente. Todas las cifras son estimaciones propias.**

Los precios salen de las referencias publicadas que se citan en la Tabla 3 o en los informes anteriores. Las bajas parten del **8,2 % mensual** que se cita para el software por suscripción en la región ([Ecosistema Startup](https://ecosistemastartup.com/?p=59797)), ajustado por rubro. Las horas tuyas se valúan a USD 25.

| # | Idea | Precio/mes (USD) | Margen | Bajas/mes | LTV | CAC | LTV/CAC | Repago (meses) | De qué está hecho el CAC |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Recepcionista | 96 | 79 % | 8,2 % | 925 | 340 | 2,7 | 4,5 | Horas tuyas |
| 2 | Alquileres | 50 | 85 % | 4 % | 1.060 | 150 | 7,1 | 3,5 | Mitad horas |
| 3 | Consorcios | 192 | 85 % | 3 % | 5.440 | 500 | 10,9 | 3,1 | Horas tuyas |
| 4 | Clubes | 48 | 80 % | 6 % | 640 | 250 | 2,6 | 6,5 | Horas tuyas |
| 5 | Estudios contables | 200 | 70 % | 4 % | 3.500 | 500 | 7,0 | 3,6 | Horas tuyas |
| 6 | Vaca Muerta | 100 | 60 % | 8 % | 750 | 500 | 1,5 | 8,3 | Horas y viajes |
| 7 | Localización | ≈ 700 por proyecto | 70 % | Casi sin repetición | 490–980 | 150 | 3–6 | Cobro adelantado | Horas tuyas |
| 8 | Catálogo como servicio | 200 | 60 % | 15 % | 800 | 250 | 3,2 | 2,1 | Horas tuyas |
| 9 | Framer | Venta única de 50–100 | 95 % | — | 500–2.000 en total por plantilla (dato) | ≈ 0, pero 40–80 h de diseño por plantilla | — | — | Horas fijas, no por cliente |
| 10 | Shopify o Chrome | 15 | 90 % | 8 % | 170 | 30 | 5,6 | 2,2 | Plata |
| 11 | Datos para concesionarias | 22 | 90 % | 6 % | 330 | 100 | 3,3 | 5,1 | Horas tuyas |
| 12 | Talleres | ≈ 195 por taller | 80 % | — | — | 100 | — | — | Horas tuyas |
| 13 | Membresía | 40 | 90 % | 15 % | 240 | 60 | 4,0 | 1,7 | Plata y contenido |
| 14 | **Cuota Verificada** | 125 | 92 % | 5 % | 2.300 | 375 | 6,1 | 3,3 | **Horas tuyas** |
| 15 | Marketplace de 0 km | ≈ 80 por concesionaria | 70 % | 5 % | 1.120 | ≈ 370 (alta + tráfico) | 3,0 | 6,6 | Horas y plata |
| 16 | **Turnos en Casa** | 19 | 72 % | 6 % | 228 | 55 | 4,1 | 4,0 | Plata y socios |
| 17 | Monitor GUDI | 125 | 60 % | 4 % | 1.875 | 375 | 5,0 | 5,0 | Horas tuyas |
| 18 | Voz clonada | ≈ 600 por institución | 75 % | 3 % | 15.000 | 1.750 | 8,6 | 3,9 | Horas tuyas, pero por cada acuerdo de cientos de familias |
| 19 | EUDR | 55 | 80 % | 3 % | 1.470 | 200 | 7,3 | 4,5 | Horas tuyas |
| 20 | Costeo | 45 | 85 % | 8,2 % | 470 | 250 | 1,9 | 6,5 | Horas tuyas |
| 21 | **Catálogo para IA** | 10 (7 neto, después del 30 %) | 67 % | 9 % | 74 | 10 | 7,4 | 1,5 | Plata (tienda) |
| 22 | Monotributo en asistentes | 9,6 | 85 % | 8,2 % | 100 | 30 | 3,3 | 3,7 | Plata |
| 23 | Monitor normativo | 30 | 90 % | 5 % | 540 | 75 | 7,2 | 2,8 | Plata |
| 24 | **Presupuestos para oficios** | 12 | 70 % | 8 % | 105 | 25 | 4,2 | 3,0 | **Plata** (anuncios + pie viral) |
| 25 | Auto usado | 10 por informe, una vez | 90 % | — | ≈ 9 | 5–15 con anuncios | 0,6–1,8 | — | Plata |
| 26 | IA de tu negocio | 25 | 75 % | 8 % | 234 | 45 | 5,2 | 2,4 | Plata y socios |

**Tabla 5. Puntaje de escalabilidad y filtros, de mayor a menor.** El puntaje es un juicio propio con la escala de la Tabla 2. En los filtros, "✓" quiere decir que pasa, "✗" que no y "≈" que es dudoso.

| # | Idea | Canal ×3 | Costo ×2 | Horas ×2 | Mercado ×2 | Defensa ×1 | **Puntaje /100** | Problema | Competencia | Factible | Economía | ¿Al podio? | Durabilidad (de 5) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 | Framer | 4 | 5 | 5 | 5 | 1 | **86** | ✓ | ✗ saturada | ✓ | ✓ | No | 2 |
| 10 | Shopify o Chrome | 4 | 5 | 4 | 5 | 2 | **84** | ✓ | ✗ saturada | ✓ | ✓ | No | 3 |
| 24 | **Presupuestos para oficios** | 4 | 3 | 4 | 5 | 3 | **78** | ✓ | ✓ | ✓ | ✓ | **Sí (1.º)** | 3 |
| 21 | **Catálogo para IA** | 5 | 2 | 5 | 4 | 1 | **76** | ✓ | ✓ hoy | ✓ | ✓ | **Sí (2.º)** | 1 |
| 13 | Membresía | 3 | 5 | 3 | 5 | 2 | **74** | ✓ | ✗ | ✓ | ✓ | No (depende de audiencia) | 2 |
| 23 | Monitor normativo | 3 | 5 | 5 | 3 | 2 | **74** | ✓ | ✗ Indicadores.ar | ✓ | ✓ | No | 3 |
| 25 | Auto usado | 2 | 5 | 5 | 4 | 1 | **70** | ✓ | ≈ | ≈ | ✗ compra única | No | 1 |
| 26 | IA de tu negocio | 4 | 3 | 3 | 5 | 1 | **70** | ✓ | ✗ | ✓ | ✓ | No | 1 |
| 2 | Alquileres | 3 | 4 | 3 | 3 | 4 | **66** | ✓ | ✗ | ≈ | ✓ | No | 4 |
| 16 | **Turnos en Casa** | 3 | 3 | 4 | 3 | 4 | **66** | ✓ | ✓ | ✓ | ✓ | **Sí (3.º)** | 4 |
| 22 | Monotributo en asistentes | 3 | 4 | 4 | 3 | 2 | **66** | ✓ | ✗ | ✓ | ✓ | No | 2 |
| 18 | Voz clonada | 3 | 3 | 3 | 4 | 2 | **62** | ✓ | ✓ | ✓ | ✓ | Cuarta | 2 |
| 11 | Datos para concesionarias | 2 | 5 | 4 | 1 | 3 | **58** | ✗ nadie probó que paguen | — | ✓ | ✓ | No | 3 |
| 15 | Marketplace de 0 km | 3 | 3 | 3 | 2 | 4 | **58** | ✓ | ✗ El Cero KM, Mercado Libre | ≈ | ≈ | No | 2 |
| 3 | Consorcios | 2 | 4 | 2 | 3 | 4 | **56** | ✓ | ✗ | ≈ | ✓ | No | 4 |
| 4 | Clubes | 2 | 4 | 2 | 3 | 3 | **54** | ≈ | ≈ | ✓ | ✗ | No | 3 |
| 19 | EUDR | 2 | 4 | 2 | 3 | 2 | **52** | ✓ | ✗ | ✓ | ✓ | No | 3 |
| 20 | Costeo | 2 | 4 | 2 | 3 | 2 | **52** | ✓ | ✗ Fudo | ✓ | ✗ | No | 2 |
| 7 | Localización | 2 | 3 | 1 | 5 | 1 | **50** | ✓ | ✗ | ✓ | ✓ | No | 1 |
| 5 | Estudios contables | 2 | 3 | 1 | 3 | 3 | **46** | ✗ | ✗ | ≈ | ✓ | No | 4 |
| 17 | Monitor GUDI | 2 | 2 | 2 | 2 | 3 | **42** | ✓ | ✗ | ≈ | ✓ | No | 3 |
| 1 | Recepcionista | 1 | 3 | 1 | 3 | 2 | **38** | ✓ | ✗ | ✓ | ✗ | No | 3 |
| 8 | Catálogo como servicio | 2 | 2 | 1 | 3 | 1 | **38** | ✓ | ≈ | ✓ | ✓ | No | 2 |
| 14 | **Cuota Verificada** | 1 | 4 | 2 | 1 | 2 | **38** | ≈ | ✓ | ✓ | ✓ | Pasa, pero no escala | 2 |
| 12 | Talleres | 1 | 2 | 1 | 3 | 1 | **32** | ✓ | ✗ | ✓ | — | No | 1 |
| 6 | Vaca Muerta | 1 | 2 | 1 | 2 | 2 | **30** | ≈ | ≈ | ≈ | ✗ | No | 2 |

### Qué dicen los números

- **Las dos ideas con más puntaje están saturadas.** Framer y Shopify escalan perfecto, y por eso ya las ocupan miles de personas: la app que lanzó Barn2, una empresa grande del rubro, facturó USD 291 en todo 2025 ([Barn2](https://barn2.com/blog/2025-year-in-review/)). La escala estructural sin un hueco no te sirve.
- **Todo lo que se vende en persona queda debajo de 60**, aunque tenga muy buen LTV/CAC (consorcios 10,9, estudios contables 7, Cuota Verificada 6,1). Es la lección de la sección 1: cuando el CAC está hecho de tus horas, los buenos números por cliente no se multiplican.
- **WhatsApp es un costo escondido que crece con cada cliente.** Desde el 1/10/2026, Meta cobra cada mensaje de servicio después de los primeros 1.000 por mes, y ese cupo es **por número de teléfono** ([Meta](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing)). Un producto de autoservicio con miles de usuarios en un solo número los paga casi todos. No encontramos la tarifa de servicio para la Argentina. Un mensaje de utilidad cuesta unos USD 0,03 ([SleekFlow](https://help.sleekflow.io/en_US/pricing)). Por eso Turnos en Casa y Presupuestos tienen márgenes del 70 % y no del 90 %, y por eso los dos tienen que diseñarse para mandar pocos mensajes.
- **Pasan cuatro ideas por los cuatro filtros:** Presupuestos (78), Catálogo para IA (76), Turnos en Casa (66) y Voz clonada (62). Quedan las tres primeras. Voz clonada queda cuarta porque cada acuerdo exige una venta institucional larga hecha por vos, y porque las plataformas la están volviendo gratis.

**Tabla 6. Otras ideas de la primera ronda, descartadas sin puntaje completo**

| Idea | Filtro que no pasa |
|---|---|
| Expediente de ciudadanía española o italiana | No dura (la ventana cierra entre 2029 y 2031), es de un solo uso y es un rubro lleno de estafas, aunque haya unas 425.000 personas con trámite pendiente ([Catnoticias](https://www.catnoticias.es/articulo/espana/ley-nietos-consulado-buenos-aires-admite-que-tardara-130-anos-resolver-todas-solicitudes/20260716000001008549.html)) |
| Comunidades de generación distribuida | Mercado chico: unos 5.000 usuarios generadores en todo el país ([pv magazine](http://www.pv-magazine-latam.com/2026/10/14/argentina-informa-2237-mw-de-generacion-distribuida-pero-el-desglose-por-sectores-suma-181-mw/)) |
| Comprobantes de transferencia falsos | Competencia: ya existe Ezra Cobros ([Ezra](https://www.botezra.com/comprobante-de-transferencia-falso.html)) |
| Datos de emisiones de carbono (CBAM) para metalúrgicas | Competencia gratis (osapiens) y hace falta un verificador acreditado |
| Kit para exportar a la UE siendo micro | Poca disposición a pagar, y el arancel de 3 € es temporal |
| Etiquetado de contenido con IA, informes de sostenibilidad para proveedores | Sin un pagador claro |
| Candidatos falsos en entrevistas, uso de IA no autorizada en empresas, evaluaciones "a prueba de IA" | Pagadores débiles o muchas herramientas globales |
| Partes de trabajo de contratistas rurales | Competencia cercana (Malevo, FinnApp) |
| Ingreso neto para repartidores de apps | Casi imposible cobrarle a la persona |
| Turnos y presupuestos de servicios legibles por asistentes | Las agendas ya suman conectores para IA |
| Fichas de negocio en ChatGPT para pymes | Por ahora, solo para negocios de EE. UU. |
| Archivos "para que la IA te lea" (llms.txt) | Placebo: el 97 % no recibió visitas de robots ([Search Engine Journal](https://www.searchenginejournal.com/97-of-llms-txt-files-got-no-requests-ahrefs-data-shows/)) |

---

## 3. Lo que agregó la búsqueda nueva (22/11/2026)

Hicimos 20 consultas, todas listadas en la sección 6, para cubrir los huecos de escalabilidad de las candidatas al podio.

**Presupuestos para oficios.**
- **Hay quien les cobra software a los oficios en la Argentina.** YoFacturo tiene una página para electricistas, plomeros y gasistas con planes de ARS 20.000 a 150.000 por mes. Su presupuesto se arma a mano, con una lista de materiales precargada, y se manda en PDF por WhatsApp desde la obra. No lo arma desde fotos ni desde un audio. Vende aparte un "Asistente IA" a ARS 15.000 por mes ([YoFacturo](https://yo-facturo.com/electricistas/)). Es la referencia de precio más útil, y también el competidor que más fácil podría sumar lo nuestro.
- **El lado del cliente que busca un oficio está ocupado; el del que presupuesta, no.**
  - Para el que busca un oficio: Clickie (Córdoba) diagnostica con IA ([Forbes Argentina](https://www.forbesargentina.com/negocios/el-momento-uber-oficios-startup-cordobesa-usa-inteligencia-artificial-ordenar-negocio-arreglos-hogar-n92074)); Tegu publica pedidos para que ofrezcan presupuesto ([App Store](https://apps.apple.com/ar/app/tegu/id6757940653)); servidos.ar tiene un estimador gratis ([servidos.ar](https://servidos.ar/estimador-presupuesto-ia)).
  - Para el profesional que presupuesta solo aparecieron BudgAI, con 7 seguidores y ninguna reseña ([Product Hunt](https://www.producthunt.com/products/budgai/reviews)), y Cliengo, que recibe pedidos con foto por WhatsApp ([Cliengo](https://guiawabusiness.cliengo.com/whatsapp-para-servicios)).
  - En Brasil, una guía de 2026 les dice a los autónomos que armen el presupuesto a mano con ChatGPT ([Treinamentos AF](https://treinamentosaf.com.br/orcamento-whatsapp-ia-autonomos/)): la necesidad existe y la resuelven con herramientas genéricas.
- **El caso de afuera es grande, pero lo cuenta la propia empresa.** Más de 40.000 contratistas usaron Handoff según un comunicado de mayo de 2025 ([Business Wire](https://www.businesswire.com/news/home/20250519029610/en)), que cobra desde USD 149 por mes ([Software Advice](https://www.softwareadvice.com/product/525070-Handoff/reviews/)). Nadie publica cuántos usuarios tiene Joist, otra app de presupuestos para contratistas.
- **No encontramos programas de puntos de fabricantes para instaladores en la Argentina.** El canal de socios con proveedores sigue siendo una hipótesis.

**Catálogo para IA.**
- La integración de Tiendanube con ChatGPT Ads instala el píxel de OpenAI, pero "tampoco es posible sincronizar automáticamente tu catálogo de productos". Hay que subirlo a mano en CSV o TXT (XML no sirve), y solo funciona en Argentina, México, Colombia y Chile ([Tiendanube](https://ayuda.tiendanube.com/chatgpt-ads/que-es-chatgpt-ads-y-como-funciona-con-tiendanube)).
- En la tienda de apps de Tiendanube, la búsqueda "chatgpt" devuelve una sola app, de análisis y no de catálogo ([Tiendanube](https://www.tiendanube.com/tienda-aplicaciones-nube/busca?q=chatgpt)).
- La app de feeds Feed Vivo cuesta ARS 9.900 por mes, cubre Google y Meta, no ChatGPT, y tiene cero evaluaciones ([Feed Vivo](https://www.tiendanube.com/tienda-aplicaciones-nube/feed-vivo)). Esas cero evaluaciones son una mala señal sobre cuánto tráfico mueve esa tienda.
- En Shopify, OpenAI hizo su propia app gratis, que sincroniza el catálogo ([Shopify App Store](https://apps.shopify.com/chatgptads)). Las de terceros van de gratis a USD 12,90 por mes ([TrustShop](https://apps.shopify.com/ask2buy)), y una de USD 199 tiene 113 reseñas ([AISurfReady](https://apps.shopify.com/aisurfready)).
- Tiendanube dice tener más de 180.000 tiendas activas ([Tiendanube](https://www.tiendanube.com/compania)). Store Leads cuenta 206.195, con un 61,5 % en Brasil y un 28 % en la Argentina ([Store Leads](https://storeleads.app/reports/tiendanube); [eCommerce Guide](https://ecommerceguide.com/platforms/tiendanube/)).

**Plataformas de asistentes y otras.**
- El directorio de apps de ChatGPT tenía 15.120 apps al 16/11/2026, y no existe ningún dato público de instalaciones ni de tráfico ([FourWeekMBA](https://fourweekmba.com/ai-chatgpt-apps-top-15000-after-a-75-jump-in-just-23-days/)). Distribuir por ahí no está probado. Eso baja el canal de "Monotributo en asistentes" y de la variante marketplace de autos.
- Indicadores.ar ya ofrece gratis alertas del Boletín Oficial por industria y jurisdicción ([Indicadores.ar](https://indicadores.ar/pro?motivo=recorte)). Con eso el monitor normativo deja de estar libre.
- Para cobrar en otros países de la región, dLocal Go recibe pagos desde 12 países de América Latina ([dLocal Go](https://dlocalgo.com/en/coverage)), pero no pudimos confirmar si maneja suscripciones. Stripe no está disponible para empresas argentinas ([Stripe](https://stripe.com/global)). Lemon Squeezy paga a bancos argentinos ([Lemon Squeezy](https://docs.lemonsqueezy.com/help/getting-started/supported-countries)).

---

## 4. Las tres más escalables, en detalle

### 4.1 Presupuesto al Toque (1.º, 78/100)

**Qué es.** Un número de WhatsApp. El electricista le manda tres a seis fotos y un audio ("cambiar tablero, ocho bocas, cable de 2,5…"). En dos minutos recibe un PDF con su nombre y su logo. El PDF trae materiales con cantidades y precio de referencia del día, mano de obra, validez en días, forma de pago y un link de seña que cobra directo en su propia cuenta de Mercado Pago. Lo revisa con un toque y se lo reenvía al cliente. Si el cliente no contesta, a los dos días le llega un recordatorio para hacerle seguimiento. Cuando termina el trabajo, arma un parte con fotos de antes y después, y la lista de materiales lista para mandarle al proveedor. Es un bot de una tarea concreta, que es lo que permite WhatsApp desde que prohibió los asistentes de propósito general el 15/01/2026 ([TechCrunch](https://techcrunch.com/2025/10/18/whatssapp-changes-its-terms-to-bar-general-purpose-chatbots-from-its-platform/)).

**El trabajo que el cliente "contrata" (habilidad `jobs-to-be-done`).**
- **El trabajo:** "Cuando un cliente me pide precio desde la obra o por WhatsApp, quiero mandarle un presupuesto claro en minutos, para ganar el trabajo antes que otro y no perder plata si suben los materiales."
  - **Funcional:** cotizar rápido y sin errores.
  - **Emocional:** la tranquilidad de no perder plata, y no tener que hacer los presupuestos a la noche.
  - **Social:** que lo vean como un profesional serio, no como alguien que improvisa.
- **El competidor más grande es no hacer nada:** el precio de palabra, el audio, el "te paso precio a la noche".
- **Las cuatro fuerzas:**
  - **Empuje:** presupuestos que se hacen tarde, clientes que se enfrían, materiales que suben entre el presupuesto y la compra, y la falta de técnicos, que deja trabajo de sobra para el que contesta primero. El 25 % de déficit de trabajadores especializados es dato ([Infobae](https://www.infobae.com/economia/2026/02/01/la-escasez-de-trabajadores-tecnicos-calificados-eleva-los-costos-de-servicios-basicos-para-el-hogar/)); lo de contestar primero es inferencia.
  - **Atracción:** velocidad e imagen profesional.
  - **Miedo:** que la IA ponga mal un precio, quedar mal con el cliente, pagar otra suscripción.
  - **Costumbre:** el cuaderno y el audio.
- El diseño tiene que bajar el miedo: el precio siempre dice "de referencia, revisalo" y nada sale sin su toque.
- **La "gran contratación" y la "chica":** suscribirse pasa una vez; elegir la herramienta en cada presupuesto pasa todas las semanas. Esa segunda es la que define si se queda.

**Tabla 7. Startup Canvas de Presupuesto al Toque**

| Sección | Contenido |
|---|---|
| 1. Visión | Que cualquier persona de oficio de habla hispana mande un presupuesto profesional en dos minutos desde la obra y cobre lo que vale su trabajo, aunque los precios cambien cada semana |
| 2. Segmentos | **Primero:** electricistas, plomeros y gasistas, instaladores de aire acondicionado y pintores de la Argentina que trabajan solos o con 1 a 3 ayudantes, presupuestan 5 trabajos o más por mes y ya hablan con sus clientes por WhatsApp. Van primero porque presupuestan seguido, porque los materiales pesan mucho en el precio y porque se los encuentra en los mostradores de casas de electricidad y corralones. **Segundo:** empresas chicas de reformas y mantenimiento (2 a 10 personas), que pagan más. **Tercero, más adelante:** proveedores de materiales, como segundo lado que paga |
| 3. Costos relativos | Costo bajo: todo por WhatsApp, sin vendedores y sin app para instalar. Precio de referencia local, cerca del plan más barato de YoFacturo, sin caer en precios ridículos que traen usuarios que nunca pagan (la "trampa de los USD 9" de la habilidad `pricing`) |
| 4. Propuesta de valor | **Antes:** presupuesto a la noche o de palabra, sin validez ni condiciones, con precios de memoria. **Cómo:** fotos + audio → PDF en dos minutos, con materiales del día, validez, seña, seguimiento y parte de trabajo. **Después:** respondés primero, ganás más trabajos, recuperás las noches y no perdés plata con los aumentos. **Alternativas:** cuaderno o audio (gratis), ChatGPT (gratis, pero sin precios locales ni formato del rubro), YoFacturo (desde ARS 20.000, armado a mano), Handoff (EE. UU., en inglés, USD 149) |
| 5. Lo que no hace | No es un marketplace de clientes (no compite con Servidos, Clickie ni Tegu). No es un sistema de facturación completo al principio. No tiene app nativa. No hace obras grandes ni cómputo para arquitectos. No reemplaza la firma del matriculado: ayuda al gasista, no lo sustituye. Nunca toca la plata del cliente final. No promete precios exactos |
| 6. Métricas | **Estrella del norte:** presupuestos enviados a clientes reales por semana. **La métrica del trimestre:** porcentaje de usuarios activados que hacen 3 presupuestos o más en sus primeras dos semanas. Además: conversión a pago, bajas por cohorte, CAC por canal y K |
| 7. Crecimiento | Crece por el producto, no por vendedores. **1)** Anuncios de Meta que abren WhatsApp: el anuncio es la demostración, y Meta no cobra la conversación durante una ventana inicial (informe anterior, con fuente en [Meta](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing)). **2)** Viralidad incorporada: un pie chico en cada presupuesto ("hacé el tuyo gratis") y "pasáselo a un colega: un mes gratis para los dos". **3)** Mostradores de casas de electricidad y corralones, con un QR, a cambio de que les llegue la lista de materiales. **4)** Búsqueda en Google con una herramienta gratis de "cuánto cobrar por…", alimentada con datos propios (los diarios publican esa nota todos los meses, como [iProfesional](https://www.iprofesional.com/management/456087-cuanto-cobran-un-albanil-un-electricista-y-un-plomero-por-su-trabajo-en-junio-2026), lo que sugiere que se busca) |
| 8. Capacidades | API oficial de WhatsApp, lectura de fotos y audios con modelos de IA, generación de PDF, base de precios de materiales (listas públicas de proveedores, listas cargadas y correcciones de los propios usuarios), Mercado Pago (suscripciones y links de seña), anuncios de Meta (tu pipeline de video para las piezas). Construís vos el flujo y la base de precios; las listas de precios se consiguen con alianzas |
| 9. Por qué no lo copian | Handoff no va a venir: está en EE. UU., con remodeladores, en inglés y a USD 149. ChatGPT y la IA de WhatsApp no van a mantener precios de materiales por ciudad ni el formato del rubro. Los marketplaces atienden al que busca el oficio, no al oficio. YoFacturo **sí puede**: su negocio es la facturación, pero ya vende IA y llega a los oficios. La defensa real es una base de precios locales que mejora con cada presupuesto, el historial de clientes de cada usuario y la red de proveedores. En lo técnico se puede copiar; la ventaja es la velocidad y los datos |
| 10. Costos | **Fijos:** USD 250–400 por mes al principio (monotributo, contador, servidor y herramientas). **Variables por usuario pago (est.):** IA ≈ 0,5; WhatsApp ≈ 0,9–1,9; usuarios gratis que hay que sostener ≈ 1,4; cobro ≈ 0,6; servidor ≈ 0,2; en total ≈ USD 3,6. **Anuncios:** USD 300–1.500 por mes según la etapa. WhatsApp crece en línea recta con los usuarios: hay que diseñar para mandar pocos mensajes (un PDF y un link en vez de diez mensajes) |
| 11. Ingresos | **Gratis:** 3 presupuestos por mes, con el pie de la marca. **Pro:** ARS 15.000 por mes (≈ USD 9,6), ilimitado y sin pie. **Equipo:** ARS 45.000 por mes (≈ USD 28,8), hasta 5 usuarios. Plan anual con dos meses gratis. Con 85 % de Pro y 15 % de Equipo, el promedio da ≈ USD 12 (est.). **Más adelante, como hipótesis:** comisión o abono de los proveedores por los pedidos de materiales. Lo que más se mide es el presupuesto, así que los planes se arman por presupuestos por mes y por usuarios. **Incertidumbre principal:** si los informales pagan |

**Tabla 8. Modelo de negocio en nueve bloques (habilidad `business-model`)**

| Bloque | Contenido |
|---|---|
| Socios clave | Meta (WhatsApp y anuncios), Mercado Pago, proveedores de materiales con listas de precios |
| Actividades clave | Mantener la base de precios, el flujo de IA y la medición de cohortes |
| Recursos clave | Base de precios y de presupuestos, el número de WhatsApp verificado |
| Propuesta de valor | Presupuesto profesional en dos minutos, con precios del día |
| Relación | Autoservicio, con soporte del bot y escalado a una persona |
| Canales | Anuncios a WhatsApp, pie viral, mostradores, Google |
| Segmentos | Oficios que presupuestan seguido; después, empresas chicas de reformas |
| Costos | WhatsApp, IA, anuncios, fijos chicos |
| Ingresos | Suscripción Pro y Equipo; más adelante, proveedores |

Los nueve bloques se refuerzan entre sí, con un punto débil: el bloque de ingresos depende de una disposición a pagar que nadie probó.

**Motor de crecimiento (habilidad `lean-startup`).** La metodología pide elegir un motor y afinarlo. Elegimos el **pago** (anuncios que abren WhatsApp), porque se mide desde la primera semana y porque la ganancia para el que paga es fácil de explicar: ganar trabajos. Lo demás se suma para bajar el costo.
- **El circuito:** anuncio → conversación en WhatsApp → primer presupuesto real (activación) → 3 presupuestos en dos semanas (uso repetido) → pago → reenvíos y recomendaciones → nuevos usuarios.
- **Cuenta del CAC efectivo:** CAC efectivo = CAC de anuncios × (1 − K), si K es menor que 1. Con un CAC de anuncios de USD 30 y K = 0,2, el efectivo queda en USD 24.
- **Metas (decisiones nuestras, no datos):** CAC efectivo de USD 30 o menos, LTV/CAC de 3 o más, repago en 6 meses o menos, K de 0,2 o más y bajas de 8 % o menos.
- **Ojo con el pie viral:** el que recibe el presupuesto casi siempre es un cliente final, no otro oficio. El K del pie puede ser chico; el de "pasáselo a un colega" es el que importa.
- **Pegajoso de segunda:** el historial de clientes y la base de precios propia hacen que irse cueste. Se mide con la retención por cohorte de 30, 60 y 90 días.

**Tabla 9. Números por usuario en tres escenarios (estimaciones propias)**

Neto por usuario = aporte − bajas × CAC (lo que hay que gastar para reponer a los que se van). Usuarios necesarios = (meta + fijos) ÷ neto por usuario. Fijos de USD 250 para la meta de 1.000 y de USD 1.500 para la de 10.000, porque ahí ya incluyen soporte de medio tiempo.

| Escenario | Pesimista | **Base** | Optimista |
|---|---|---|---|
| Precio promedio por mes | USD 8 | **USD 12** | USD 18 (más planes Equipo) |
| Margen bruto | 65 % | **70 %** | 75 % |
| Aporte por usuario por mes | USD 5,2 | **USD 8,4** | USD 13,5 |
| Bajas por mes | 10 % | **8 %** | 5 % |
| CAC efectivo | USD 30 | **USD 25** | USD 25 |
| LTV | USD 52 | **USD 105** | USD 270 |
| LTV/CAC | 1,7 (no cierra) | **4,2** | 10,8 |
| Repago | 5,8 meses | **3,0 meses** | 1,9 meses |
| Neto por usuario, reponiendo bajas | USD 2,2 | **USD 6,4** | USD 12,25 |
| Usuarios pagos para USD 1.000 netos | ≈ 570 | **≈ 195** | ≈ 100 |
| Usuarios pagos para USD 10.000 netos | ≈ 5.200 | **≈ 1.800** | ≈ 940 |

Si las primeras cohortes se parecen al escenario pesimista, la idea no escala: es una señal de corte, no de ajuste.

**Tabla 10. Supuestos más riesgosos, ordenados por impacto × incertidumbre (habilidad `lean-startup`)**

| Orden | Supuesto | Tipo | Impacto (1–5) | Incertidumbre (1–5) | Prioridad |
|---|---|---|---|---|---|
| 1 | La gente de oficio, en su mayoría informal, paga unos ARS 15.000 por mes o paga por adelantado | Cobro | 5 | 5 | **25** |
| 2 | La usan de verdad: 3 presupuestos o más por mes en el segundo mes, en vez de volver al audio | Retención | 5 | 4 | **20** |
| 3 | Los anuncios que abren WhatsApp más el pie viral dan un CAC efectivo de USD 30 o menos | Crecimiento | 4 | 4 | **16** |
| 4 | La IA acierta materiales y cantidades con una sola revisión, y hay precios locales para cargar | Valor | 4 | 3 | **12** |
| 5 | Funciona fuera de Córdoba y de la Argentina, con precios y cobro locales | Crecimiento | 3 | 4 | **12** |
| 6 | WhatsApp cuesta USD 2 o menos por usuario pago por mes | Costo | 3 | 3 | **9** |
| 7 | YoFacturo o la IA de WhatsApp no sacan lo mismo en seis meses | Competencia | 3 | 3 | **9** |

**Experimento de cuatro semanas.**
- **Qué se prueba:** primero los supuestos 1 a 3. Como prueba mínima, un "mago de Oz": el usuario ve un bot, pero detrás estás vos. Él manda fotos y audio; Claude arma el borrador con un script; vos lo revisás y lo devolvés en menos de 10 minutos. Así se aprende antes de construir la automatización.
- **Cómo se consiguen los usuarios:**
  - 15 a 20 charlas en mostradores de casas de electricidad y corralones de Córdoba, entre las 7 y las 9, cuando compran;
  - USD 300 de anuncios que abren WhatsApp, apuntados a instaladores de aire acondicionado (diciembre y enero son su temporada alta: inferencia), electricistas, plomeros y pintores;
  - dos o tres grupos de Facebook o WhatsApp del rubro.
- **Qué se cobra:** en la cuarta semana, ARS 15.000 por mes, o un precio de "fundador" de ARS 10.000 por seis meses para el que pague tres meses por adelantado.

**Tabla 11. Criterios de corte del experimento.** Son reglas de decisión nuestras, no datos.

| Métrica (semanas 1–4) | Seguir | Ajustar | Abandonar |
|---|---|---|---|
| Personas que mandan al menos un trabajo real | 40 o más | 20 a 39 | Menos de 20 |
| Activados que hacen 3 presupuestos o más en 14 días | 40 % o más | 25 a 39 % | Menos de 25 % |
| Presupuestos que de verdad se reenvían al cliente | 60 % o más | 40 a 59 % | Menos de 40 % |
| Activados que pagan o prepagan | 15 % o más (al menos 8 personas) | 8 a 14 % | Menos de 8 % |
| Costo de anuncios por persona activada | USD 8 o menos | USD 8 a 15 | Más de USD 15 |
| Charlas en las que ya usan algo y están conformes | Menos de 5 de 20 | 5 a 9 | 10 o más |
| Contactos que llegan por el pie o por un colega | Al menos 5 | 1 a 4 | Ninguno (la viralidad no existe; no mata la idea, pero sube el CAC) |

**Charla con la gente de oficio (habilidad `mom-test`).** No se habla de la idea hasta el final. Se pregunta por cosas que ya pasaron, y que hable el otro el 80 % del tiempo.
1. "Contame del último presupuesto que hiciste. ¿Para qué trabajo era, cómo lo armaste y cuánto tardaste?"
2. "¿Lo ganaste? ¿Por qué creés que sí, o que no?"
3. "El mes pasado, ¿cuántos presupuestos hiciste y cuántos se hicieron trabajo?"
4. "¿Cuándo los hacés: en la obra, a la noche? ¿Qué pasó la última vez que tardaste en mandarlo?"
5. "¿Cómo sabés el precio de los materiales cuando presupuestás? ¿Te pasó de perder plata por un aumento entre el presupuesto y la compra? ¿Cuánto?"
6. "¿Qué usás hoy: cuaderno, audio, Excel, alguna app? ¿Qué probaste antes y por qué lo dejaste?"
7. "¿Pagás alguna herramienta todos los meses? ¿Cuál y cuánto?" (Saca el presupuesto real, en vez de preguntar "¿cuánto pagarías?".)
8. "¿A quién le comprás los materiales y cómo le pasás la lista?"
9. **Pedido de compromiso al final:** "Probalo con tu próximo presupuesto real. Si te sirve, el mes cuesta $15.000; si lo pagás hoy por adelantado, te queda a $10.000 por seis meses." O, como moneda de reputación: "¿Me presentás a dos colegas?"

Si la charla termina sin un pago, sin una presentación o sin un trabajo real mandado, cuenta como un "no", aunque haya habido elogios. Así, la charla cumple las siete filas del diagnóstico de la habilidad.

---

### 4.2 Catálogo para IA, app de Tiendanube (2.º, 76/100, durabilidad 1)

**Qué es.** Una app de la tienda de Tiendanube. Toma el catálogo de la tienda y lo mantiene listo para ChatGPT Ads, Google y Meta.
- **ChatGPT:** genera el archivo que pide OpenAI.
- **Google:** genera el feed con el precio de oferta y las cuotas. Según la ayuda de Tiendanube, hoy a Google le llega solo el precio original, y por eso le rechazan productos ([Tiendanube](https://ayuda.tiendanube.com/123352-google-shopping/como-configurar-mis-productos-para-los-canales-de-venta)).
- **Meta:** genera el feed de catálogo.
- **Además:** mejora títulos y atributos con IA para que los asistentes los entiendan, y avisa cuando un canal rechaza un producto.

**El trabajo que se contrata.** "Cuando prendo un canal de anuncios nuevo, quiero que mi catálogo esté cargado y al día sin tocar planillas, para no perder ventas ni horas." El empuje es concreto: hay que subir el archivo a mano y XML no sirve ([Tiendanube](https://ayuda.tiendanube.com/chatgpt-ads/que-es-chatgpt-ads-y-como-funciona-con-tiendanube)). La atracción también: en el CyberMonday de 2026, las compras que empezaron en un asistente subieron 180 % en Tiendanube ([iProfesional](https://www.iprofesional.com/tecnologia/468259-como-inteligencia-artificial-esta-cambiando-forma-comprar-cybermonday-2026)). El competidor más grande vuelve a ser no hacer nada: la mayoría de las tiendas todavía no anuncia en ChatGPT (inferencia).

**Tabla 12. Startup Canvas de Catálogo para IA**

| Sección | Contenido |
|---|---|
| 1. Visión | Que una tienda chica de América Latina aparezca bien en los asistentes de IA, con su precio real (cuotas, transferencia), sin tocar un archivo |
| 2. Segmentos | **Primero:** tiendas de Tiendanube de Argentina y México que ya anuncian o quieren anunciar en ChatGPT. **Segundo:** tiendas con productos rechazados en Google o Meta por el precio. **Tercero:** agencias que manejan muchas tiendas |
| 3. Costos relativos | Costo mínimo, precio bajo |
| 4. Propuesta de valor | **Antes:** CSV a mano, precios desparejos entre canales y rechazos. **Cómo:** conexión en un clic, archivos y feeds actualizados, mejora de títulos y avisos. **Después:** el catálogo al día en todos los canales. **Alternativas:** a mano (gratis), Feed Vivo (ARS 9.900, sin ChatGPT), Feed XML Nube, Pistacho (anunciado, sin lanzar) ([iProUP](https://www.iproup.com/startups/71842-startup-argentina-pistacho-app-emprendedores-vendan-chatgpt-comercio-agentico)) |
| 5. Lo que no hace | No maneja campañas ni es una agencia. Solo Tiendanube al principio |
| 6. Métricas | **Estrella del norte:** tiendas con el feed actualizado en las últimas 24 h. **La métrica del trimestre:** instalaciones por semana que llegan desde la tienda de apps y su paso a pago |
| 7. Crecimiento | Búsqueda dentro de la tienda de apps ("chatgpt", "feed", "google shopping"), agencias socias de Tiendanube, un tutorial en video de "cómo subir tu catálogo a ChatGPT" |
| 8. Capacidades | API de Tiendanube, especificación de feeds de OpenAI, Google Merchant Center y Meta, y la revisión de la app por Tiendanube |
| 9. Por qué no lo copian | **No pasa esta prueba.** OpenAI hizo su app gratis para Shopify y puede hacer la de Tiendanube; Tiendanube puede sumarlo; Feed Vivo puede agregar el formato en días. Lo único difícil de copiar es la semántica del precio argentino (cuotas, transferencia, promociones por banco), y eso no lo prioriza nadie, pero tampoco lo pide nadie todavía |
| 10. Costos | Casi nada por tienda (≈ USD 0,3). La tienda se queda con el 30 % (reparto 70/30 en el reglamento de Colombia ([Tiendanube](https://www.tiendanube.com/co/reglamento-tiendas-nube)); verificar el de Argentina). Fijos de USD 100–200 |
| 11. Ingresos | USD 10 por mes (≈ ARS 15.600) con 7 días gratis, y un plan para agencias. Incertidumbres: cuántas tiendas anuncian en ChatGPT; si pagan más que los ARS 9.900 de Feed Vivo; si OpenAI acepta cargar el catálogo por URL o solo a mano |

**Motor de crecimiento.** El canal es la tienda de apps y el motor es pegajoso: el feed tiene que seguir andando todos los días. Crece si las instalaciones nuevas superan a las bajas. Metas (decisiones nuestras): 20 instalaciones por semana o más, 30 % o más de paso de prueba a pago, y bajas de 9 % o menos.

**Tabla 13. Números por tienda en tres escenarios (estimaciones propias).** Fijos de USD 150 para la meta de 1.000 y de USD 800 para la de 10.000.

| Escenario | Pesimista | **Base** | Optimista |
|---|---|---|---|
| Precio de lista | USD 6 | **USD 10** | USD 19 (multicanal) |
| Aporte, después del 30 % y los costos | USD 3,9 | **USD 6,7** | USD 13,0 |
| Bajas por mes | 12 % | **9 %** | 6 % |
| CAC | USD 15 | **USD 10** | USD 10 |
| LTV / LTV/CAC | 32 / 2,2 | **74 / 7,4** | 217 / 21,7 |
| Tiendas para USD 1.000 netos | ≈ 550 | **≈ 200** | ≈ 95 |
| Tiendas para USD 10.000 netos | ≈ 5.100 | **≈ 1.860** | ≈ 870 |

Las 1.860 tiendas del escenario base son del 2,7 al 3,2 % de las tiendas argentinas de Tiendanube (entre 58.000, por Store Leads, y 70.000, por la propia Tiendanube), pero solo cuentan las que anuncian en IA, y no sabemos cuántas son.

**Tabla 14. Supuestos más riesgosos**

| Orden | Supuesto | Impacto | Incertidumbre | Prioridad |
|---|---|---|---|---|
| 1 | Hay suficientes tiendas anunciando en ChatGPT, o con ganas de hacerlo | 5 | 5 | **25** |
| 2 | OpenAI y Tiendanube no lo hacen gratis en los próximos 12 meses | 5 | 4 | **20** |
| 3 | La tienda de apps de Tiendanube trae 20 instalaciones o más por semana | 4 | 4 | **16** |
| 4 | Pagan USD 10 o más, contra alternativas gratis o de ARS 9.900 | 4 | 4 | **16** |
| 5 | OpenAI acepta el archivo generado, idealmente desde una URL que se actualiza sola | 3 | 3 | **9** |

**Experimento de dos semanas.**
- **Prueba de humo con una sola función:** una página que explica el servicio, más el generador del archivo de OpenAI y del feed de Google con precio de oferta y cuotas.
- **Charlas:** 15 dueños de tiendas que ya prendieron ChatGPT Ads. Se los busca por agencias socias de Tiendanube, LinkedIn y comunidades de emprendedores.
- **Publicación:** se sube la app a la tienda en cuanto esté (no sabemos cuánto tarda la revisión).
- **Corte:** se abandona si se cumple cualquiera de estas condiciones:
  - menos de 10 de 50 tiendas contactadas usan o planean usar ChatGPT Ads;
  - menos de 5 instalaciones por semana después de cuatro semanas publicada;
  - menos de 3 pagos en el primer mes;
  - OpenAI o Tiendanube anuncian la sincronización automática.
- **Preguntas para la charla:**
  - "¿Cuándo prendiste los anuncios de ChatGPT? ¿Qué hiciste con el catálogo y cuánto tardaste?"
  - "¿Cada cuánto lo actualizás? ¿Qué pasó la última vez que cambiaste precios?"
  - "¿Te rechazaron productos en Google o Meta por el precio? ¿Qué hiciste?"
  - "¿Qué apps pagás hoy en la tienda y cuánto?"
  - "¿Mostrás cuotas o precio con transferencia en los anuncios? ¿Cómo?"
  - Compromiso: "¿Lo instalamos ahora con tu tienda y lo dejamos andando?"

**Veredicto honesto.** Es la que mejor muestra qué es escalar de verdad: cero horas por cliente y distribución dentro de la plataforma. Pero el precio es bajo, la tienda se queda con el 30 % y, sobre todo, OpenAI ya demostró en Shopify que regala esta función. No la recomendamos como negocio. Si alguna vez querés aprender a vender en una tienda de apps, se puede hacer como prueba de dos semanas, pero no en paralelo con la recomendación: la metodología pide un solo motor por vez.

---

### 4.3 Turnos en Casa (3.º, 66/100, durabilidad 4)

**Qué es.** Lo que validó el informe anterior: un tablero para la familia que coordina a las cuidadoras de un padre o una madre mayor.
- **Para la familia:** quién está hoy, qué pasó en cada turno, horas por cuidadora, cuánto hay que pagar y cuánto puso cada hermano.
- **Para las cuidadoras:** solo WhatsApp: "llegué", "me voy" y un traspaso de turno con cinco preguntas.
- **A fin de mes:** las horas pasan a una hoja lista para cargar en el Recibo Asistido de ARCA, que exige que el empleador cargue las horas ([ARCA](https://servicioscf.afip.gob.ar/publico/sitio/contenido/novedad/ver.aspx?id=5978)).
- **Límites:** nunca toca plata ni da consejos médicos.

**El trabajo que se contrata.** "Cuando con mis hermanos tenemos que sostener el cuidado de mamá con dos o tres cuidadoras, quiero saber quién estuvo, cuánto se debe y quién puso qué, para dejar de pelearnos y cumplir con la ley sin pasar noches con planillas."
- **Lo emocional pesa más que lo funcional:** hay casos documentados como el de "me cansa, me preocupa, a veces me desespera" ([Infobae](https://www.infobae.com/sociedad/2026/03/29/envejecer-en-casa-una-decision-legitima-que-dispara-una-logistica-agotadora-y-carisima-y-no-resuelve-la-soledad-y-el-encierro/)).
- **El freno más fuerte es la costumbre:** el grupo de WhatsApp familiar y la planilla.
- **La "contratación chica" diaria la hace la cuidadora, no la familia.** Si ella no manda el "llegué", el producto muere.

**Tabla 15. Startup Canvas de Turnos en Casa**

| Sección | Contenido |
|---|---|
| 1. Visión | Que cuidar a un padre en casa no rompa a la familia: claridad de horarios, de plata y de cumplimiento, sin discusiones |
| 2. Segmentos | **Primero:** familias argentinas con dos cuidadoras o más y dos hermanos o más, uno de ellos coordinando. **Segundo:** el hermano que vive afuera y paga en dólares o euros (por ejemplo, el grupo "Argentinas en Madrid" tenía más de 5.000 miembros en 2023 ([MDZ](https://www.mdzol.com/sociedad/2023/10/28/tener-pasaporte-europeo-es-importante-pero-no-te-asegura-que-vas-vivir-como-en-disney-379066.html))). **Tercero:** contadores y agencias de cuidado, con un panel para muchas familias |
| 3. Costos relativos | Costo bajo (WhatsApp y web), precio menor al 1 % de lo que cuesta el cuidado: 24 horas de cuidado pasan los $3,2 millones por mes ([iProfesional](https://www.iprofesional.com/actualidad/463804-cuanto-cuesta-cuidar-adulto-mayor-las-24-horas-por-mes)) |
| 4. Propuesta de valor | **Antes:** grupo de WhatsApp, planilla, peleas, recibo hecho a mano. **Cómo:** registro del turno por WhatsApp, resumen diario, cierre mensual con horas y escala vigente, gastos en pesos, dólares o euros. **Después:** cero discusiones y el recibo en minutos. **Alternativas:** Cuidarlos (turnos, sin sueldos) ([App Store](https://apps.apple.com/ar/app/cuidarlos/id1458778617)), ARCA gratis (sin turnos), Domésticas al Día (liquidación a ≈ USD 32 por empleada) ([Domésticas al Día](https://domestica-al-dia.com.ar/)) |
| 5. Lo que no hace | No busca cuidadoras, no mueve plata, no da indicaciones médicas, no tiene app nativa |
| 6. Métricas | **Estrella del norte:** turnos registrados por semana. **La métrica del trimestre:** porcentaje de turnos con "llegué", "me voy" y traspaso en la semana 2. Además: bajas por cohorte y CAC por canal |
| 7. Crecimiento | Herramientas gratis en Google (calculadora del costo del cuidado de 24 horas y del aguinaldo de diciembre), contadores con panel para varias familias (cada uno puede traer de 5 a 20, según la validación), geriatras y agencias de Córdoba, y grupos de argentinos afuera |
| 8. Capacidades | API de WhatsApp, tabla de escalas de casas particulares, cuaderno de gastos en varias monedas, revisión legal (Ley 25.326 de datos personales) |
| 9. Por qué no lo copian | Cuidarlos tendría que entrar en sueldos y gastos; Domésticas al Día, en turnos. Hacerlo es posible pero no es su foco. El historial de cada familia retiene. Riesgo: ARCA sigue automatizando |
| 10. Costos | Fijos de USD 250 al principio. Variables ≈ USD 5 por familia: WhatsApp 3–4, IA 0,3, servidor 0,3 y cobro 1 |
| 11. Ingresos | Plan Familia ARS 29.900 por mes (≈ USD 19); Plan Exterior USD 199 por año; agregado de liquidación revisada por un contador. Todos son hipótesis de la validación |

**Motor de crecimiento.** Pegajoso: el cuidado dura años, y el negocio crece si las bajas quedan en 5 o 6 % o menos. La adquisición viene de las herramientas gratis y de los contadores. Hay dos advertencias:
- **Google está difícil.** Las notas de "cuánto cobra una cuidadora" las dominan los diarios ([Infobae](https://www.infobae.com/economia/2026/10/23/cuanto-cobraran-los-cuidadores-de-adultos-por-hora-en-noviembre-2026/)), y cuando aparece un resumen de IA el primer resultado pierde el 58 % de los clics ([Ahrefs](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/)).
- **La viralidad no trae clientes nuevos.** Los hermanos y las cuidadoras invitados están dentro de la misma familia que ya paga. Una cuidadora que trabaja en varias casas puede llevar el producto a otra familia, pero eso es una inferencia.

**Tabla 16. Números por familia en tres escenarios (estimaciones propias, mismos fijos que en la Tabla 9)**

| Escenario | Pesimista | **Base** | Optimista |
|---|---|---|---|
| Precio promedio por mes | USD 13 | **USD 19** | USD 25 (con Exterior y contador) |
| Margen | 68 % | **72 %** | 78 % |
| Bajas por mes / CAC | 9 % / USD 70 | **6 % / USD 55** | 4 % / USD 55 |
| LTV / LTV/CAC | 98 / 1,4 | **228 / 4,1** | 488 / 8,9 |
| Familias para USD 1.000 netos | ≈ 490 | **≈ 120** | ≈ 72 |
| Familias para USD 10.000 netos | ≈ 4.500 | **≈ 1.100** | ≈ 665 |

Las 1.100 familias del escenario base son el 0,18 % de las 600.000 relaciones de casas particulares. Si las cuidadoras de mayores fueran del 5 al 10 % de esas relaciones (supuesto sin fuente), serían del 2 al 4 % del segmento: dentro del umbral, pero cerca.

**Tabla 17. Supuestos más riesgosos**

| Orden | Supuesto | Impacto | Incertidumbre | Prioridad |
|---|---|---|---|---|
| 1 | Las familias pagan unos USD 19 por mes (el 71 % de esos hogares dice que no le alcanza la plata ([CELS](https://www.cels.org.ar/web/wp-content/uploads/2026/03/LDC-informe-7-final-final.pdf))) | 5 | 5 | **25** |
| 2 | Las cuidadoras registran el 60 % de los turnos o más en la semana 2 | 5 | 4 | **20** |
| 3 | Las herramientas gratis o los contadores traen familias con un CAC menor a tres meses de abono | 4 | 4 | **16** |
| 4 | Las bajas quedan en 6 % o menos | 4 | 3 | **12** |
| 5 | Lo legal cierra (recibo de ARCA, Ley 25.326) | 3 | 3 | **9** |

**Experimento de cuatro semanas.** Al plan de validación del informe anterior (30 charlas y un piloto manual pago con 5 a 10 familias) le sumamos una prueba del canal escalable:
- publicar en pocos días la "Calculadora del aguinaldo de diciembre de tu cuidadora" (es el momento justo: el aguinaldo se paga en diciembre);
- ponerle USD 150 de anuncios y medir el costo por familia que deja sus datos;
- sumar 5 contadores al piloto y contar cuántas familias trae cada uno.

**Corte:** se abandona si se cumple cualquiera de estas condiciones:
- menos de 15 de 30 familias cuentan peleas o pérdida de tiempo con hechos concretos;
- menos de 5 prepagan;
- menos del 60 % de los turnos se registran;
- el costo por familia que deja sus datos pasa los USD 5;
- menos de 2 contadores traen al menos una familia.

**Preguntas para la charla:**
- "Contame cómo se organizó la semana pasada: quién estuvo en cada turno y cómo te enteraste."
- "¿Cuándo fue la última discusión entre hermanos por plata o por horarios? ¿Qué pasó?"
- "¿Cómo calcularon el último sueldo o el aguinaldo? ¿Quién lo hizo y cuánto tardó?"
- "¿Le pagan a alguien por la liquidación? ¿Cuánto?"
- "¿Qué probaron para ordenarlo y por qué lo dejaron?"
- Compromiso: "¿Arrancamos un piloto de tres meses a mitad de precio, pagado hoy?", o una presentación al hermano que vive afuera.

---

## 5. La recomendación: Presupuesto al Toque

### Por qué escala más que Cuota Verificada

**Tabla 18. Las dos ideas, con los seis umbrales**

| Umbral | Cuota Verificada | Presupuesto al Toque |
|---|---|---|
| Costo marginal | Margen ≈ 92 % en plata, pero cada concesionaria necesita una verificación semanal humana de la financiación | Margen ≈ 70 %, todo automático. El costo que crece es WhatsApp, y se controla con el diseño |
| Horas por cliente | 10–15 h para cerrar una venta y 1–2 h por mes de mantenimiento | ≈ 0 de alta; unos 5 minutos por mes de soporte promedio (est.) |
| Canal | Visita en persona, una concesionaria por vez | Anuncio → WhatsApp → pago, sin reunión, más el pie viral |
| Mercado | 163 concesionarias con línea Bancor en Córdoba; de 815 a 1.200 en el país | 3,3 millones de cuentapropistas en la Argentina, más cualquier país de habla hispana |
| Cuántos clientes para USD 10.000 | ≈ 115 concesionarias: el 70 % de Córdoba | ≈ 1.800 usuarios: el 0,05 % de los cuentapropistas |
| Concentración | Tu primer cliente, Valparaiso, es también tu empleador y tu cliente más grande | Miles de clientes chicos: ninguno pesa |
| Defensa | Dato de financiación verificado (bueno, pero local) | Base de precios por ciudad que mejora con cada presupuesto (efecto de datos) |
| Puntaje | **38/100** | **78/100** |

Cuota Verificada gana en una sola cosa: el dinero por cliente (LTV de USD 2.300 contra 105). Pero para escalar, lo que importa es que el CAC sea plata y que las horas no crezcan con cada cliente, y ahí la diferencia es total.

### Cómo llega a USD 1.000 y después a USD 10.000

**USD 1.000 netos por mes ≈ 195 usuarios pagos** (escenario base de la Tabla 9). Con unos USD 1.500 de anuncios en los primeros 90 días (est.), un costo de USD 0,5 a 1,5 por conversación (est., sin dato para la Argentina), un 30 % de activación y un 15 % de pago, el día 90 deberías tener entre 50 y 130 usuarios pagos. La meta de 195 llegaría entre el **mes 5 y el mes 7** (est.). Es una estimación, no una promesa.

**USD 10.000 netos por mes ≈ 1.800 usuarios pagos**, entre el **mes 12 y el mes 24** (est.). Para eso tienen que cumplirse todas estas condiciones, que son las que hay que medir:

**Tabla 19. Lo que tiene que ser cierto para llegar a USD 10.000**

| Condición | Umbral | Cuándo se sabe |
|---|---|---|
| Paso de activado a pago | 15 % o más | Semana 4 |
| Bajas por mes | 8 % o menos (ideal 5 %) | Mes 3, con la primera cohorte completa |
| CAC efectivo (anuncios × (1 − K)) | USD 30 o menos, con anuncios de USD 3.000 a 5.000 por mes | Mes 4 a 6, cuando subís la inversión |
| Costo variable por usuario pago | USD 4 o menos (WhatsApp + IA + usuarios gratis) | Mes 2 |
| Que no sea solo de Córdoba | 40 % o más de los pagos nuevos desde otras provincias en el mes 6 | Mes 6 |
| Cobro fuera de la Argentina | Funcionando en al menos 2 países (México, Uruguay, Chile, Colombia o España) en el mes 12, con dLocal Go, Lemon Squeezy o Mercado Pago (verificar suscripciones en cada caso) | Mes 9 a 12 |
| Precios de referencia | Error promedio de materiales del 15 % o menos frente a lo que corrige el usuario | Mes 2 |
| Tus horas | 20 h por mes o menos de soporte con 1.000 usuarios (≈ 3 % de los usuarios escalan a una persona, 15 minutos cada uno, est.) | Mes 9 |
| Segundo ingreso (opcional, sube el precio promedio) | Al menos un proveedor paga por recibir pedidos de materiales | Mes 6 a 9 |

**Calidad de los ingresos (habilidad `unit-economics`).** Desde el mes 2, armá una tabla de cohortes por mes de alta, en pesos y en porcentaje del mes 0, con las bajas de clientes y de plata por separado. Llevá también el "quick ratio": ingresos nuevos ÷ ingresos perdidos por bajas. Tiene que dar 4 o más mientras crecés; si da menos de 2, hay un problema de bajas. Con unos USD 1.500 de quema neta en el primer trimestre y unos USD 14.400 de ingreso anual sumado (100 usuarios × USD 12 × 12 meses), el múltiplo de quema daría ≈ 0,1. Es muy eficiente (el umbral de la habilidad es menos de 1), pero es una cuenta sobre supuestos.

### Plan de 30, 60 y 90 días (desde el lunes 23/11/2026)

**Tabla 20. Plan de 30, 60 y 90 días**

| Tramo | Meta | Qué hacés |
|---|---|---|
| **Días 1–30: validar con un mago de Oz** | Decisión con la Tabla 11: 40 o más activados y 8 o más pagos | **Semana 1:** 15 a 20 charlas con el guion de la sección 4.1 en mostradores de Córdoba. Número de WhatsApp con la API oficial, verificación de Meta Business, política de privacidad. Flujo asistido: Claude arma el borrador y vos lo revisás en menos de 10 minutos. Una página simple y tres videos cortos del flujo con tu pipeline. **Semanas 2 y 3:** USD 300 de anuncios que abren WhatsApp, en Córdoba, para aire acondicionado, electricidad, plomería y pintura. Medís activación, presupuestos por persona y reenvíos. **Semana 4:** oferta de pago (ARS 15.000, o ARS 10.000 de fundador con tres meses adelantados) y decisión. Diciembre tiene fiestas: si las charlas se traban, corré el corte una semana, no más |
| **Días 31–60: automatizar lo repetido** | 40 a 60 usuarios pagos; bajas del primer mes menores al 15 % | Sacás la revisión humana de los trabajos comunes y la dejás solo para los raros. Armás la base de precios: listas públicas de 3 a 5 proveedores más las correcciones de los usuarios. Cobro con Mercado Pago Suscripciones. Pie viral y "un mes gratis para los dos" por cada colega que pague. Tablero de cohortes (Tabla 21). Anuncios a toda la Argentina (USD 500) |
| **Días 61–90: afinar el motor** | 80 a 120 usuarios pagos (≈ USD 1.000–1.400 de ingreso mensual bruto, est.); LTV/CAC de 3 o más en las primeras cohortes | Prueba de precio (ARS 12.000 contra 18.000; plan anual). Plan Equipo. Una prueba con un proveedor: QR en el mostrador a cambio de recibir la lista de materiales. Prueba chica en Uruguay o México (USD 100 de anuncios) para medir demanda y cobro afuera. Decisión de seguir o girar |

**Tabla 21. Tablero de seguimiento (habilidad `lean-startup`).** Nada de métricas de vanidad: ni "usuarios registrados" ni "mensajes recibidos".

| Métrica | Fórmula | Meta |
|---|---|---|
| Activación | Personas con un trabajo real ÷ conversaciones iniciadas | 30 % o más |
| Uso repetido | Activados con 3 presupuestos o más en 14 días ÷ activados | 40 % o más |
| Pago | Pagos ÷ activados | 15 % o más |
| Bajas por cohorte | Se van en el mes ÷ pagos al inicio del mes | 8 % o menos |
| CAC por canal | Gasto ÷ pagos nuevos de ese canal | USD 30 o menos |
| K | Pagos que llegan por un colega o por el pie ÷ pagos | 0,2 o más |
| Costo variable | Gasto de WhatsApp + IA ÷ pagos | USD 4 o menos |

**Inversión estimada de los 90 días.**
- Anuncios: USD 1.500.
- Mensajes de WhatsApp: USD 30–100.
- Modelos de IA: USD 50–150.
- Servidor y dominio: USD 30–90.
- Monotributo y contador: ≈ USD 165–225 en los tres meses. Los montos del monotributo son los publicados por ARCA ([ARCA](https://www.arca.gob.ar/monotributo/categorias.asp)).
- Abogado para términos de uso y política de datos (Ley 25.326): USD 150–400, una vez.
- **Total: ≈ USD 2.000–2.500**, sin contar tu tiempo ni tu suscripción a Claude.

**Cobro legal.** En la Argentina, monotributo de servicios, factura C y Mercado Pago Suscripciones, como en los informes anteriores. Si vendés afuera, factura E y cobro en dólares a una cuenta propia en un banco argentino, que desde la Comunicación A 8481 del BCRA no tiene tope anual ([Allende & Brea](https://allende.com/?p=22915)). La pasarela para cobrar suscripciones en otros países (dLocal Go, Lemon Squeezy) está sin confirmar: preguntáselo a cada una y a tu contador antes del mes 9.

**Si el experimento da "girar"** (habilidad `lean-startup`):
- **Cambio de cliente:** empresas chicas de reformas y mantenimiento, que pagan más.
- **Cambio de quién paga:** gratis para el oficio, y pagan los proveedores por los pedidos.
- **Achicar a una sola función:** solo el parte de trabajo con fotos y garantía.
- **Cambio de canal:** solo por mostradores de proveedores.

Si da "abandonar", el plan B es Turnos en Casa. Usa las mismas piezas (WhatsApp, PDF, Mercado Pago), así que lo construido no se pierde.

**Diagnóstico del plan con la habilidad `lean-startup`: 7 de 10.**
- Tiene nombrados y ordenados los supuestos riesgosos.
- Tiene una prueba mínima que los ataca.
- Tiene métricas que sirven para decidir.
- Tiene criterios de corte fijados antes de construir.
- La fila más baja es la evidencia: hoy está en el nivel 1 de la escala ("yo creo que lo quieren"). El experimento tiene que subirla al nivel 4 (pagos por adelantado) antes de automatizar nada.

### Lo que no está probado

1. **Nadie pagó.** La disposición a pagar de una población con 63,3 % de informalidad es la duda principal. El informe anterior descartó esta idea por eso mismo.
2. **No sabemos si la usan seguido.** Las herramientas para oficios pueden tener bajas altas y temporada (inferencia, sin dato).
3. **No hay una fuente pública de precios de materiales.** Hay que armarla con listas y correcciones de los usuarios. Un precio mal puesto le puede hacer perder plata al usuario; por eso dice "de referencia" y nada sale sin su revisión.
4. **ChatGPT gratis es el sustituto directo.** Si al electricista le alcanza con pedirle a ChatGPT un presupuesto, nuestro valor (velocidad, precios locales, formato, seña y seguimiento) no alcanza para cobrar.
5. **YoFacturo puede sumarlo rápido:** ya vende un asistente de IA y llega a los oficios.
6. **No encontramos la tarifa de WhatsApp para la Argentina.** Los mensajes de servicio se cobran desde el mensaje 1.001 del mes por número; si la tarifa es alta, el margen baja del 70 %.
7. **La viralidad puede ser casi cero**, porque el presupuesto lo recibe un cliente final, no otro oficio.
8. **El cobro fuera de la Argentina no está verificado**, y sin eso no se llega a USD 10.000 con un solo país en el escenario pesimista.
9. **Los números de Handoff los da la propia empresa**, y EE. UU. no es la Argentina.
10. **No sabemos cuántas personas de oficio hay.** Los 3,3 millones son todos los cuentapropistas; no encontramos el desglose por oficio.
11. **Los puntajes son juicios nuestros**, y la búsqueda de competidores fue limitada: un buscador con sede en EE. UU., sin revisar Google Play ni la App Store a mano.
12. **Puede existir algo chico que no apareció.** Revisá vos, desde la Argentina, Google Play y la App Store con "presupuesto", "presupuestos IA", "electricista" y "plomero".

---

## 6. Búsquedas hechas para este informe (22/11/2026)

**Tabla 22. Consultas y páginas abiertas**

| # | Tipo | Consulta o página | Para qué |
|---|---|---|---|
| 1 | Búsqueda | "Tiendanube ChatGPT Ads catálogo de productos sincronización automática" | Si Tiendanube ya sincroniza el catálogo |
| 2 | Página | ayuda.tiendanube.com/chatgpt-ads/que-es-chatgpt-ads-y-como-funciona-con-tiendanube | Confirmar el texto exacto y los países |
| 3 | Búsqueda | "Shopify app "ChatGPT" product feed sync pricing reviews installs 2026" | Precios y reseñas de apps parecidas |
| 4 | Búsqueda | "Tiendanube cantidad de tiendas activas 2026 Nuvemshop marcas América Latina" | Tamaño del mercado |
| 5 | Búsqueda | "Tiendanube tienda de aplicaciones feed Google Shopping Meta catálogo app precio mensual" | Competidores de feeds en Tiendanube |
| 6 | Página | tiendanube.com/tienda-aplicaciones-nube/feed-vivo | Precio y evaluaciones de Feed Vivo |
| 7 | Página | tiendanube.com/tienda-aplicaciones-nube/busca?q=chatgpt | Si existe una app de feed para ChatGPT |
| 8 | Búsqueda | "app presupuestos con inteligencia artificial para electricistas plomeros por WhatsApp Argentina México" | Competidores de presupuestos |
| 9 | Búsqueda | "app de presupuestos para oficios Google Play "presupuesto" descargas plomeros electricistas pintores app más usada Latinoamérica" | Apps de presupuestos y sus descargas |
| 10 | Búsqueda | "Budgai presupuestos IA Product Hunt" | Revisar un competidor |
| 11 | Búsqueda | "Handoff AI estimator remodelers number of contractors customers 2026 growth" | Tamaño del caso de EE. UU. |
| 12 | Búsqueda | "Joist app contractors estimates invoices number of users million downloads" | Señal de distribución por tiendas de apps |
| 13 | Página | yo-facturo.com/electricistas/ | Precio y funciones del competidor local |
| 14 | Búsqueda | "orçamento com IA pelo WhatsApp app para eletricista encanador prestador de serviço foto áudio" | Competidores en Brasil |
| 15 | Búsqueda | "programa club de instaladores electricistas plomeros gasistas Argentina beneficios app fabricante puntos 2026" | Canal de socios con fabricantes |
| 16 | Búsqueda | "herramienta gratis "qué dice ChatGPT" de tu negocio local auditoría IA pymes español precio mensual 2026" | Competencia de "¿Qué dice la IA de tu negocio?" |
| 17 | Búsqueda | "ChatGPT apps directory developer traffic installs discovery data Apps SDK 2026 how many users find apps" | Si el directorio de ChatGPT distribuye |
| 18 | Búsqueda | "alertas Boletín Oficial personalizadas por rubro suscripción resumen diario normativa Argentina servicio pago" | Competencia del monitor normativo |
| 19 | Página | developers.facebook.com/documentation/business-messaging/whatsapp/pricing | Costo marginal de WhatsApp |
| 20 | Búsqueda | "dLocal Go suscripciones cobrar clientes México Chile Colombia desde Argentina emprendedor SaaS 2026" | Cobro en otros países |

**Lo que no se pudo verificar con estas búsquedas:**
- la tarifa de los mensajes de servicio de WhatsApp en la Argentina;
- las descargas de apps de presupuestos en Google Play;
- las instalaciones en la tienda de Tiendanube, que no las publica;
- si dLocal Go cobra suscripciones;
- si OpenAI acepta cargar el catálogo por URL;
- el reparto de la tienda de Tiendanube en la Argentina (el 70/30 es del reglamento de Colombia).

---

## Conclusión

Escalar, para una persona sola, no es vender algo más caro ni con mejor margen. Es que **cada cliente nuevo cueste plata y no horas**, y que **atenderlo no te sume trabajo**. Con esa vara, casi todo lo que investigamos en las dos rondas anteriores cae por el mismo lado: concesionarias, centros de salud, consorcios y estudios contables tienen buenos números por cliente, pero se venden y se atienden de a uno. Las ideas que sí escalan solas están en tiendas saturadas (Framer, Shopify) o dependen de una plataforma que puede regalar la función mañana (el catálogo para ChatGPT). Presupuesto al Toque está en el medio que buscabas: un problema de todos los días, un canal que se compra con plata y se mide en una semana, un mercado que no se termina en Córdoba y una base de datos que mejora con cada presupuesto. Su punto débil está a la vista y se prueba primero: si la gente de oficio no paga en cuatro semanas, la evidencia habrá dicho que no, y pasás a Turnos en Casa habiendo perdido un mes, no un año.
