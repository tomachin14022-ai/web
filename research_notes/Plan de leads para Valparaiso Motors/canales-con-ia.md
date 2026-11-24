# Canales y herramientas con IA para generar y convertir leads en una concesionaria argentina (Valparaiso Motors, Córdoba), noviembre de 2026

> Notas al 24/11/2026. Cada enlace es de una página que abrí en esta sesión, salvo que diga **"(resumen de búsqueda)"**: en ese caso el dato salió del resumen del buscador y no pude leer la página. **"(notas previas)"** quiere decir que el dato está verificado en `research_notes/Negocio innovador con IA sin competencia/` (sesión del 20/11/2026) y no lo volví a abrir. Marco como **"proveedor"** todo número que publica alguien que vende el producto. Lo que es deducción mía va en "Inferences" y lo que no pude confirmar, en "Gaps". Casi toda la evidencia con números es de EE. UU. o Europa: **no encontré ningún estudio independiente con datos de concesionarias argentinas.**

## 1. ChatGPT Ads en Argentina: formatos, segmentación, restricciones para autos y financiación, y primeros resultados

### Takeaway
ChatGPT Ads funciona en Argentina desde el 21/10/2026, en autoservicio y solo para usuarios Free y Go mayores de 18. Para una concesionaria tiene dos límites duros que salen de la política oficial (v1.7, 20/11/2026). Primero, **los anuncios de servicios financieros fuera de EE. UU. están prohibidos salvo que OpenAI los apruebe**, así que la financiación, la cuota y el CFT no pueden ser el mensaje. Segundo, **el anuncio no puede llevar directo a un chat de WhatsApp**: tiene que ir a una página web, que sí puede tener el botón de WhatsApp. OpenAI no publica benchmarks. Los pocos números que circulan (CTR de 0,6–1 %, CPM de USD 25–60) son de EE. UU. y de terceros, y **no encontré ningún resultado medido de una concesionaria**.

### Cited Findings
**Lanzamiento y quién ve los anuncios**
- Post oficial del 21/10/2026: ChatGPT Ads suma 26 países (89 en total), entre ellos Argentina, Chile, Colombia y Perú. Los anuncios aparecen solo en los planes Gratis y Go ("Las suscripciones Plus, Pro y Enterprise seguirán sin anuncios"). Se compra en autoservicio en ads.openai.com o por socios tecnológicos. "Más de 100 000 anunciantes han realizado campañas". El post no trae datos de rendimiento — [OpenAI](https://openai.com/es-ES/index/chatgpt-ads-expands-26-new-countries/)
- Facturación local con Aleph en LatAm (notas previas) — [ITSitio](https://www.itsitio.com/inteligencia-artificial/openai-expande-chatgpt-ads-a-14-paises-de-america-latina-y-abre-una-nueva-era-para-la-publicidad-con-ia/)
- Ayuda oficial:
  - no se muestran anuncios en Plus, Pro ni planes Business;
  - se excluyen las cuentas "identified as belonging to users under 18", por edad declarada o predicción de edad — [OpenAI Help, Ads basics](https://help.openai.com/en/articles/20001207-ads-in-chatgpt-the-basics)
- Una guía argentina (revisada el 05/11/2026) dice que la lista oficial de disponibilidad de Ads Manager "incluye a Argentina como disponible para autoservicio". Aclara que la entidad que factura tiene que estar en un país habilitado — [Ilari & Co](https://www.ilariandco.com.ar/chatgpt-ads-argentina-antes-de-anunciar/), citando [OpenAI Ads Manager availability](https://help.openai.com/en/articles/20001245-ads-manager-availability) (no la abrí). Otra nota anterior decía que Argentina no estaba habilitada en autoservicio; el post oficial del 21/10 la contradice (resumen de búsqueda) — [ID4YOU](https://www.id4you.com/blog/ecommerce/chatgpt-ads-en-argentina-guia-completa-2026/)

**Formato, compra y medición (ayuda oficial)**
- El anuncio va debajo de la respuesta de ChatGPT. Lleva nombre del anunciante, favicon, título, texto, imagen y página de destino — [OpenAI Help](https://help.openai.com/en/articles/20001207-ads-in-chatgpt-the-basics)
- **Compra:**
  - objetivos de Vistas, Clics o Conversiones;
  - se cobra por impresión o por clic válido; en oCPC se paga el clic, no la conversión;
  - hay puja inteligente con CPC o CPA objetivo para anunciantes elegibles;
  - para CPC manual, OpenAI recomienda "start with a maximum bid of $3–$5 USD per click" — misma fuente.
- **Selección del anuncio:** usa el contexto y la intención de la conversación, la página de destino, el texto y unas "context hints" que pone el anunciante, que "are not exact-match keywords and do not guarantee delivery". La medición de conversiones se configura en Ads Manager Beta, y se pueden agregar UTM fijos a la URL — misma fuente.
- **Lo que no dice la ayuda oficial:** la segmentación geográfica fina, las audiencias, el gasto mínimo ni si hay píxel o API de conversiones — misma fuente.
- **Una guía de un proveedor (EE. UU., actualizada el 28/09/2026) agrega:**
  - segmentación por país, estado/región, DMA y código postal de EE. UU.;
  - audiencias propias (la lista para incluir necesita 25.000 contactos);
  - sin segmentación demográfica, sin lookalikes y sin retargeting;
  - sin mínimo de gasto;
  - CPM máximo por defecto de USD 60 y CPM del piloto de USD 25–35 (Criteo);
  - "Sponsored Agents", un anuncio que abre una conversación, solo en prueba limitada en EE. UU.;
  - no hay formato de video ni carrusel en autoservicio.

  Varias de estas cifras no tienen fuente primaria. La guía es de Get My Auto, que vende otro producto para concesionarias — [Get My Auto](https://dealers.getmyauto.com/blog/chatgpt-ads-for-auto-dealers)

**Política de anuncios v1.7 (texto oficial, "Updated: November 20, 2026")**
- **Financiación:**
  - "Ads for financial products and services are restricted."
  - En EE. UU., "Auto loans/leasing" figura entre las categorías elegibles caso por caso.
  - "Ads for financial services outside of the US are currently prohibited unless approved by OpenAI."
  - Puede pedirse "proof of licensure".
- **Sin política propia de autos:** no hay una sección sobre vehículos. Lo único relacionado es el ítem de créditos prendarios y leasing.
- **Mensajería:** "Ads may not link directly to messaging chats or groups; a reviewable business website may offer messaging as a contact option."
- **Leads para terceros:** quien conecta usuarios con otro proveedor tiene que avisarlo "before collecting users' personal information".
- **Ubicación:** no se puede "misrepresent their business location, service area, or eligibility".

  Fuente de los cuatro puntos: [OpenAI Ad Policies](https://openai.com/policies/ad-policies/)
- **Contexto sensible:** OpenAI evita poner anuncios en conversaciones de "serious financial hardship" y de otros temas delicados. El lanzamiento se centró en verticales de consumo (incluye servicios locales) — [Relevant Audience, resumen de la v1.7](https://www.relevantaudience.com/ai/chatgpt-ad-policies-v1-7-november-2026/) (fuente secundaria)

**Resultados y benchmarks (todo de EE. UU., nada de concesionarias medido)**
- OpenAI no publica CTR, CPC, conversión ni ROAS por industria (resumen de búsqueda) — [Kompozy](https://kompozy.io/guides/chatgpt-ads-performance)
- **CTR:**
  - Similarweb, mayo de 2026: ~0,68 % de CTR, y ~1 % en el cuartil superior (resumen de búsqueda) — [Kompozy](https://kompozy.io/guides/chatgpt-ads-performance)
  - Una cuenta reportó 0,91 % en ChatGPT contra 6,4 % en Google Search en el mismo rubro, con un CPC real de ~USD 7 en una sola campaña (resumen de búsqueda) — [Inpromptads](https://www.inpromptads.com/chatgpt-ads-benchmarks/)
  - CPM de cierre de USD 25–45, contra ~USD 60 en el lanzamiento, como dato orientativo (resumen de búsqueda) — [Stratezik](https://www.stratezik.com/blog/chatgpt-ads-benchmarks)
  - Otra fuente estima un CTR de 3,8–4 %: **las cifras no coinciden** (resumen de búsqueda) — [SureThing](https://surething.io/blog/chatgpt-ads)
- Según Similarweb, ~26 % de las respuestas de ChatGPT llevan un anuncio (notas previas) — [Similarweb](https://aisearch.similarweb.com/blog/gen-ai-stats/)
- **Concesionarias:**
  - Cars.com fue visto con anuncios en ChatGPT, sin cifras — [Get My Auto](https://dealers.getmyauto.com/blog/chatgpt-ads-for-auto-dealers)
  - En Reino Unido, CMe Automotive prueba anuncios en ChatGPT con cuatro concesionarias (notas previas, resumen de búsqueda) — [AM Online](https://www.am-online.com/news/dealers-to-test-whether-chatgpt-ads-can-reach-researching-car-buyers)
  - Un consultor de EE. UU. dice que los anuncios de ChatGPT "no son ROI inmediato" (notas previas) — [Dealership Guy](https://news.dealershipguy.com/p/ai-search-hype-vs-dealer-reality-what-s-worth-acting-on-now)
- **Google AI Mode:** los anuncios se extendieron el 28/10/2026 a 10 países (Australia, Canadá, India, Kenia, Malasia, Nueva Zelanda, Nigeria, Pakistán, Filipinas y Singapur), con Brasil, México y Reino Unido para el 4.º trimestre. **Argentina no figura.** En México solo se lista el inglés (resumen de búsqueda) — [PPC Land](https://ppc.land/advertisers-in-10-more-countries-cant-opt-out-of-googles-ai-mode-ads/); [Unite.AI](https://www.unite.ai/google-rolls-out-ai-mode-ads-in-10-countries-multiturn-ads-in-u-s/)

### Inferences
- **Para Valparaiso, ChatGPT Ads es un experimento chico, no un canal principal.** No se puede hablar de financiación sin aprobación de OpenAI, y el lead no puede caer directo en WhatsApp. Lo que sí encaja:
  - creatividades sobre el beneficio y el modelo ("¿Cuánto gastás de nafta por mes?", "hasta 132 km sin nafta, dato NEDC");
  - página de destino por modelo en valparaisomotors.com.ar, con botón de WhatsApp y código de fuente ("Vengo de ChatGPT por el Eado").
- **Medición:** UTM fijos más la conversión de Ads Manager. Sin eso no se puede separar el efecto del canal.
- **Presupuesto de prueba (estimación propia):** con un CPC de USD 3–5 (la recomendación oficial), USD 300–500 dan ~60–170 clics. Alcanza para ver si llegan conversaciones, no para sacar conclusiones estadísticas.
- **Antes de gastar, confirmar en Ads Manager si se puede segmentar por Córdoba.** La ayuda oficial no lo dice. Si solo se puede todo el país, se repite el problema del reel de 150 mil vistas: curiosos de todo el país y ningún comprador local.
- **El CFT y el aviso legal van en la página de destino igual.** La regla argentina de publicidad de financiación (sección 6) no desaparece porque el anuncio no hable de cuotas.

### Gaps
- No pude abrir la página oficial de disponibilidad de Ads Manager por país ni la de medición, así que no sé si existe el píxel o la API de conversiones.
- No sé si en Argentina se puede segmentar por provincia o ciudad.
- No sé si OpenAI aprueba anunciantes de financiación de autos fuera de EE. UU., ni cómo se pide.
- No encontré ni un resultado publicado (CPL, costo por test drive, ventas) de una concesionaria con ChatGPT Ads, en ningún país.

## 2. Visibilidad en asistentes y búsqueda con IA (ChatGPT, Gemini/AI Mode, Perplexity, Meta AI): qué hace que citen a una concesionaria local

### Takeaway
El estudio más grande y transparente sobre concesionarias (A3 Brands, agosto de 2026, 661 concesionarias y 113.094 preguntas) encontró que **las páginas que responden preguntas (guías, comparativas, preguntas frecuentes) se citan 27 veces más que las fichas de stock** (21,1 % contra 0,8 %). Las páginas de financiación y ofertas se citan un 13,3 % y las de modelo o comparación un 11,1 %. En cambio, **el schema de vehículos, el puntaje de "preparación técnica para IA", las estrellas y la cantidad de reseñas no mostraron efecto medible en la cita**. Por fuera de las concesionarias, los asistentes citan sobre todo fuentes que el negocio controla: el sitio propio y las fichas de directorios, entre ellas Google Business Profile. Gemini y AI Mode se apoyan en Google Maps, y ChatGPT, mucho más en directorios y portales. El volumen de tráfico sigue siendo chico, pero el lead que llega desde la IA es bueno. Son estudios de proveedores, correlacionales y de EE. UU.

### Cited Findings
**Estudios específicos de concesionarias (2026)**
- **A3 Brands, publicado el 22/08/2026:**
  - **Muestra:** 661 concesionarias oficiales de EE. UU. (647 medibles), 113.094 preguntas, en AI Overview, AI Mode, ChatGPT y Gemini (Perplexity no se midió). Análisis con intervalos de confianza por bootstrap y corrección de Bonferroni.
  - **Proporción de páginas citadas según el tipo:**

    | Tipo de página | Citadas |
    |---|---|
    | Portada | 98,8 % |
    | Quiénes somos / contacto | 35,2 % |
    | Editoriales | 21,1 % |
    | Service / repuestos | 15,0 % |
    | **Financiación / ofertas** | **13,3 %** |
    | Modelo / comparación | 11,1 % |
    | **Stock (ficha de unidad)** | **0,8 %** |

    En el 89 % de las concesionarias con al menos 10 páginas de cada tipo, las editoriales se citaron más que las de stock.
  - **Señales:**
    - la cantidad de páginas editoriales (r = +0,362) es la única cuyo intervalo de confianza excluye el cero;
    - "preparación técnica" r = +0,068, estrellas r = −0,064 y volumen de reseñas r = +0,001;
    - el schema de vehículos lo usaba solo el 4,3 %, y no tenerlo no cambió la cita.
  - **Diferencias entre buscadores:** AI Overview cita una fuente en el 98 % de las respuestas donde aparece la concesionaria, pero la nombra en el 6 %. Gemini cita en el 61 % y nombra en el 51 %.
  - **Advertencias del propio estudio:** es una correlación, no un experimento; la mediana de las concesionarias era de 4,7 estrellas; "Finding nothing is not the same as proving there is nothing". El autor vende servicios de contenido y SEO a concesionarias, y lo aclara.
  - Fuente: [A3 Brands](https://a3brands.com/ai-search-study/)
- **Pied Piper PSI, 2026** (comprador incógnito, 3.290 concesionarias; prueba nueva de visibilidad en ChatGPT): cuando le preguntaron a ChatGPT por una concesionaria,
  - la buscada salió primera en el 77 % de los casos, no primera en el 14 % y no apareció en el 9 %;
  - ChatGPT confirmó la unidad en stock en el 70 %, la disponibilidad de test drive en el 36 % y dio el enlace directo a la unidad en el 30 % — [Auto Remarketing, 23/02/2026](https://www.autoremarketing.com/ar/analysis/study-finds-ai-raises-dealerships-internet-lead-responsiveness-but-creates-added-risks)
- **Otros estudios de concesionarias (resumen de búsqueda):**
  - en concesionarias CDJR, AI Overviews citó al 69 % al menos una vez y ChatGPT al 36 % (datos de Ahrefs de septiembre de 2026 según el resumen; estudio de correlación) — [Honest Digital](https://honestdigital.com/blog/one-store-6-ais)
  - Gemini nombró al mismo negocio principal el 8 % de las veces, contra el 90 % del mapa de Google — [Savvy Dealer](https://www.savvydealer.com/blog/gemini-8-percent-consistency-dealer-ai-visibility-report)
  - en las citas de ChatGPT sobre autos, siete de los ocho dominios principales son portales o sitios de reseñas: Autotrader 5 %, Cars.com 4,6 % — [Promptwatch](https://promptwatch.com/blog/ai-visibility-tool-for-automotive)
  - 84 de 100 sitios de concesionarias sacaron menos de 60 puntos en una prueba de recomendaciones de ChatGPT (notas previas) — [Dealership Guy](https://news.dealershipguy.com/p/84-out-of-100-dealership-websites-are-basically-invisible-to-ai-search-2026-01-15)

**Negocios locales en general (notas previas, abiertas el 20/11/2026)**
- **BrightLocal** (16/09/2026; ~200.000 preguntas locales y 1,97 M de citas):
  - Origen de las citas: sitios de los negocios 42 %, Google Business Profile 28,6 % (presente para el 94 % de los negocios) y Facebook 2,2 %.
  - "ChatGPT relies little on Google Business Profile".
  - Solo coincide el 20–33 % de los resultados entre una búsqueda y su repetición.
  - Radio del 90 % de las recomendaciones: ChatGPT ~287 km; los buscadores de Google, 39–64 km.
  - Fuente: [BrightLocal](https://www.brightlocal.com/research/local-ai-visibility-study/) (proveedor)
- **Yext** (09/10/2025): el 86 % de las citas viene de fuentes que maneja la marca (sitio 44 %, fichas de directorios ~42 %); los foros como Reddit, el 2 % — [Business Wire / Yext](https://www.businesswire.com/news/home/20251009106549/en/Yext-Research-86-of-AI-Citations-Come-from-Brand-Managed-Sources-Clarifying-How-Marketers-Can-Compete-in-the-AI-Search-Era) (proveedor; dato de 2025)
- **SOCi** (28/01/2026): recomendaron al 1,2 % de los locales ChatGPT, al 11 % Gemini y al 7,4 % Perplexity, contra el 35,9 % del mapa de 3 resultados de Google. La ficha del negocio era ~68 % exacta en ChatGPT y Perplexity y 100 % en Gemini, que usa Google Maps — [Search Engine Land](https://searchengineland.com/ai-local-visibility-report-2026-468085) (proveedor)
- **Fuentes que usa cada uno** (estudio de negocios locales, no de concesionarias; resumen de búsqueda, **no pude confirmar qué estudio es**: el resumen lo menciona junto al blog de A3 Brands):
  - Gemini: el 59,9 % de lo que cita es el sitio propio del negocio;
  - ChatGPT: 15,9 % sitios de negocios, 41,7 % redes y foros, 34,6 % directorios — [A3 Brands blog](https://a3brands.com/blog/ai-citations-for-dealerships/)

**Volumen y calidad del tráfico (notas previas)**
- Unos ~150 clics por mes desde ChatGPT contra ~10.000 orgánicos de Google por concesionaria en EE. UU. (un consultor, sin metodología) — [Dealership Guy](https://news.dealershipguy.com/p/ai-search-hype-vs-dealer-reality-what-s-worth-acting-on-now)
- Las llamadas que llegan desde ChatGPT tienen 49 % de tasa de lead, la más alta de 7 canales, pero con volumen bajo (Invoca, todas las industrias) — [Retail Dive / Invoca](https://www.retaildive.com/press-release/20260710-new-invoca-data-finds-the-best-leads-now-start-in-chatgpt/)
- Cox, 2.º trimestre de 2026: el 63 % de los compradores de EE. UU. "seguro o probablemente" usará IA en su próxima compra; solo el 29 % de las concesionarias empezó a adaptarse — [Cox Automotive](https://www.coxautoinc.com/press-releases/new-cox-automotive-ai-in-auto-retail-tracker/)

**Canales "formales" cerrados para Argentina (notas previas)**
- Businesses in ChatGPT (beta, 10/11/2026): la ficha local reclamable parece solo de EE. UU. — [Rankability](https://www.rankability.com/blog/how-to-claim-your-business-in-chatgpt/)
- Google retiró la documentación de datos estructurados de vehículos el 09/09/2025 — [Google Search Central](https://developers.google.com/search/docs/appearance/structured-data/vehicle-listing)
- Google vehicle ads no está en LatAm — [Google Merchant Center Help](https://support.google.com/merchants/answer/11189169?hl=en)

**Situación de Valparaiso Motors (verificado en notas previas, 20/11/2026)**
- **Sitio:** WordPress con Elementor y 58 unidades en el sitemap. No tiene JSON-LD. Las fichas no muestran CFT, TEA, cuotas ni anticipo, y la tasa de "Bancor – Línea UVA" está vacía. No hay turno de test drive — [ficha de ejemplo](https://valparaisomotors.com.ar/listing/changan-cs55-plus-1-5-phev-dht-2026-3/); [sitemap](https://valparaisomotors.com.ar/wp-sitemap-posts-listing-1.xml)
- **robots.txt (Cloudflare):** bloquea Google-Extended, que según Google también controla el grounding en las apps de Gemini, y GPTBot. Deja pasar OAI-SearchBot, ChatGPT-User y PerplexityBot — [robots.txt](https://valparaisomotors.com.ar/robots.txt); [Google, common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- **Prueba con un buscador con IA:** el sitio propio no apareció ni buscándolo por nombre. Las respuestas sobre Haval H6 y Eado Plus en Córdoba salieron de avisos de Mercado Libre y deRuedas, sin poder confirmar la financiación — notas previas (`validacion-concesionarias-ia.md`, sección 1)

### Inferences
- **Lo que más probablemente sirve para Valparaiso, en orden:**
  1. **Páginas que responden las preguntas de sus reels**, como "EV, PHEV o HEV: cómo funciona cada uno", "La cuota más baja puede ser la más cara: prendario, UVA, plan de ahorro y financiación de la marca" o "Cuánta nafta gastás por mes con 50 km por día". Es el único tipo de página con señal medible (A3), y el guion ya está escrito y aprobado.
  2. **Una página de financiación por modelo** con contado, anticipo, cuotas, TEA, CFT, precio total financiado, "vigente al" y el texto legal. Es la segunda categoría más citada después de las de contenido (13,3 %) y la que falta hoy.
  3. **Google Business Profile completo**, con horarios, marcas, fotos y respuestas a reseñas. Gemini y AI Mode leen Maps.
  4. **Revisar la decisión sobre Google-Extended en Cloudflare.** Es decisión del dueño, porque destrabarlo también acepta el uso para entrenamiento.
- **El schema (AutoDealer, Car, Offer, FAQPage) es barato y no hace daño, pero no hay evidencia de que mejore la cita** (A3). No hay que venderlo como la solución.
- **Mercado Libre y deRuedas van a seguir apareciendo en las respuestas.** Conviene tener los avisos con precio, versión y "entrega inmediata" bien cargados, porque ahí es donde la IA hoy encuentra a Valparaiso.
- **Expectativa realista:** decenas de visitas por mes desde IA, no cientos. Es un canal de calidad, no de volumen. Sirve más para que el comprador que ya está investigando encuentre la respuesta correcta (precio, CFT, stock) y no la de un competidor.
- **Herramientas a armar con Claude Code (inferencia):**
  - **Generador de páginas de modelo y financiación:** lee el stock de WordPress con un plugin chico que exponga el precio, arma la tabla de financiación con CFT y la fecha, y publica el JSON-LD.
  - **Monitor de visibilidad:** un panel fijo de ~30 preguntas en español ("concesionaria Changan en Córdoba con financiación", "¿conviene un híbrido enchufable en Córdoba?") que se corre cada semana contra las API de OpenAI con búsqueda web, Gemini con grounding y Perplexity, y registra si nombran o citan a Valparaiso. Ojo: las API pueden responder distinto que las apps.
  - **Analítica:** una vista de Google Analytics con las visitas desde chatgpt.com, gemini.google.com y perplexity.ai.

### Gaps
- Ningún estudio mide concesionarias de Argentina ni LatAm, ni preguntas en español.
- No hay evidencia sobre cómo elige fuentes Meta AI dentro de WhatsApp, ni de si recomienda negocios locales en Argentina (ya figuraba como gap en las notas previas).
- No hay estudio que separe "me citan" de "me eligen": A3 aclara que nombrar no es recomendar.
- No sé cuántas visitas desde IA recibe hoy valparaisomotors.com.ar. Hace falta acceso a su Analytics y Search Console.

## 3. Respuesta a leads con IA en WhatsApp (dentro de las reglas de Meta): Meta Business Agent, automatización permitida y resultados de concesionarias

### Takeaway
En Argentina hay dos caminos que cumplen las reglas de Meta:

| Camino | Qué es | Límites |
|---|---|---|
| **Business AI / Meta Business Agent** | Agente de Meta en la app WhatsApp Business, disponible en Argentina desde el 24/02/2026 y gratis por ahora | Exige un catálogo con al menos un producto; no inicia conversaciones; no entiende audios |
| **Bot propio por la API de WhatsApp** | Agente "de tarea específica" (atención, turnos, calificación) armado por la concesionaria | La regla del 15/01/2026 prohíbe solo los asistentes de IA de uso general; hay que ofrecer siempre la vía a un humano y usar opt-in y plantillas aprobadas |

La evidencia de resultados es casi toda de proveedores, sin grupo de control:
- **Impel:** +18 % de conversión de leads.
- **Matador:** 86 % de asistencia a las citas.
- **Kavak:** 1 de cada 3 conversaciones desde un anuncio pasa a lead calificado.
- **Kia Italia:** 5 ventas y −53 % de costo por auto vendido en 4 semanas.

Lo único independiente es el estudio de comprador incógnito de Pied Piper (2026). Dice que la automatización mejoró la velocidad de respuesta, pero que **cuando la consulta necesita a una persona el puntaje cae 9 puntos** y el cliente tiene el doble de probabilidad de no recibir ninguna respuesta personal. Cox agrega que el 82 % de las concesionarias de EE. UU. usa IA, pero **solo el 22 % vio crecer las ventas**.

### Cited Findings
**Meta Business Agent y Business AI**
- **Lanzamiento global, 03/06/2026:** el agente "Books appointments and qualifies incoming leads", responde preguntas, recomienda productos del catálogo, cierra ventas y "Lets you decide when a team member steps in". Responde en el idioma del cliente.
  - Lo usan "More than one million businesses".
  - "Getting started with the Business Agent is free"; en los próximos meses pasará a las suscripciones pagas.
  - Para empresas grandes hay una "Agent Platform" que conecta con Shopify y Zendesk. Las herramientas de calendario figuran como algo futuro.
  - No publica resultados de conversión.
  - Fuente: [WhatsApp Business Blog](https://whatsappbusiness.com/blog/introducing-meta-business-agent-ai/)
- **Argentina, 24/02/2026:** Business AI "estará disponible desde hoy en la Argentina y en otros 16 países de Latinoamérica", sin costo.
  - **Requisitos:** usar WhatsApp Business en español y tener al menos un producto en el catálogo (hasta 100). Se activa en Herramientas → "IA para empresas" y se puede entrenar con los chats previos.
  - **Funciones:** marca los mensajes como "IA" y deriva las consultas complejas a una persona.
  - **Límites:** "No es proactivo" y no entiende audios.
  - **Datos de Meta:** "El 68 % de los argentinos prefiere comunicarse con negocios a través de mensajes" (Tomás Picasso, Meta Argentina).
  - **Resultados:** el único que da es de un emprendedor mexicano, cuyo agente respondió el 60 % de las consultas.
  - Fuente: [La Nación](https://www.lanacion.com.ar/tecnologia/whatsapp-business-como-funciona-el-agente-de-ia-que-ahora-te-respondera-siempre-y-que-promete-nid24022026/)
- **Precio en la API (notas previas):** Meta Business Agent es una categoría propia desde el 01/07/2026, a USD 2 por millón de tokens (≈ 4–5 centavos por mensaje). Desde el 01/10/2026 se cobran los mensajes de servicio por encima de 1.000 por mes. Las respuestas a quien llega desde un anuncio de clic a WhatsApp siguen gratis durante la ventana de entrada — [Meta, Pricing](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing)

**Reglas de WhatsApp para bots propios (notas previas)**
- **Desde el 15/01/2026** se prohíben los asistentes de IA de uso general cuando "la IA es el producto principal". Se permiten los bots de soporte, reservas y notificaciones "auxiliares a un servicio legítimo". Meta decide qué es "general-purpose" — [TechCrunch](https://techcrunch.com/2025/10/18/whatssapp-changes-its-terms-to-bar-general-purpose-chatbots-from-its-platform/); [respond.io](https://respond.io/blog/whatsapp-chatbot-policy-2026)
- **WhatsApp Business Messaging Policy:**
  - opt-in previo de cada persona;
  - iniciar solo con plantillas aprobadas, y fuera de la ventana de 24 h, solo plantillas;
  - la automatización exige "prompt, clear, and direct escalation paths" a un humano;
  - no se puede pedir el número completo de tarjeta ni de cuenta — [WhatsApp Business Policy](https://whatsappbusiness.com/policy/)

**Casos de autos publicados por Meta (datos de la empresa, "no es posible replicarlos de manera idéntica")**
- **Kavak, es-LA, probablemente México:**
  - anuncios de clic a WhatsApp que llevan a una conversación con Meta Business Agent sobre la promo y la financiación;
  - mensajes de marketing a usuarios registrados e inactivos;
  - el agente de Meta pasa la conversación a los agentes propios de Kavak "con el contexto completo".
  - **Resultados:** "1 de cada 3" compradores que empezaron a hablar desde un anuncio pasó a lead calificado; captación de leads "8x" más eficiente que solo con mensajes salientes; 489 conversaciones en las primeras dos semanas. No explica la línea de base del 8x.
  - Fuente: [WhatsApp Business, caso Kavak](https://whatsappbusiness.com/es-la/resources/success-stories/kavak/)
- **Kia Italia, campaña de 4 semanas:**
  - anuncios de clic a WhatsApp con un agente de IA armado por Infobip; toma datos, responde sobre precio, equipamiento, disponibilidad y financiación, y deriva a la concesionaria más cercana para cotización o test drive.
  - **Resultados:** 144 leads calificados, 116 pedidos de cotización, **5 ventas directas**, "40x" de retorno sobre la inversión publicitaria y −53 % de costo por auto vendido frente a su clic a WhatsApp de siempre (datos de Ads Manager, Infobip y su CRM).
  - Fuente: [WhatsApp Business, caso Kia Italia](https://whatsappbusiness.com/es-la/resources/success-stories/kia-italia/)

**Evidencia independiente sobre automatización y respuesta**
- **Pied Piper PSI 2026** (3.290 concesionarias de 33 marcas; consulta incógnito por la web sobre una unidad en stock; respuestas medidas durante 24 h):
  - **Puntaje promedio:** 71/100, contra 65 en 2025.
  - **"Respuesta perfecta"** (por varios canales, en menos de 15 minutos): 51 % de las concesionarias.
  - **Canales:** el SMS se usó en el 54 % (38 % en 2025) y el teléfono en el 75 %.
  - **Cuando la consulta necesita a una persona:** 9 puntos menos, y el cliente tiene el doble de probabilidad de no recibir respuesta personal.
  - **Riesgo en los traspasos:** datos que no pasan entre DMS, sitio, CRM e IA, y vendedores que creen que "el sistema ya lo atiende".
  - "Automation and AI have improved dealer responsiveness… the greatest risk is in the handoffs between systems and from AI to dealership staff" (Cameron O'Hagan).
  - El estudio no vincula la velocidad con las ventas.
  - Fuente: [Auto Remarketing](https://www.autoremarketing.com/ar/analysis/study-finds-ai-raises-dealerships-internet-lead-responsiveness-but-creates-added-risks)
- **Cox Automotive** (11/08/2026; 483 concesionarias en el 2.º trimestre y 504 en el 1.º):
  - el 82 % usa IA; los usos principales son automatizar tareas (40 %), coordinar el seguimiento de clientes (40 %) y generar contenido (38 %);
  - **el 69 % espera más ventas por la IA, pero solo el 22 % lo vio**;
  - ~1 de cada 3 no mide el impacto o no sabe cómo medirlo;
  - con un socio externo, el 36 % reporta crecimiento de ventas, contra el 21 % sin socio — [Cox Automotive](https://www.coxautoinc.com/press-releases/new-cox-automotive-ai-in-auto-retail-tracker/)

**Casos de proveedores en EE. UU. (sin control, autorreportados)**
- **Impel en Elk Grove Buick GMC:**
  - resultados: +19 % de llamadas en vivo, +22 % de llamadas por lead, **+18 % de conversión de leads y de citas en el salón**, y más de USD 1 M en ventas "influenciadas" en 12 meses;
  - es un caso sin fecha y sin grupo de control, y "influenciado" quiere decir que la IA tocó el lead, no que generó la venta (análisis de un tercero) — [Position One](https://www.positionone.ai/insights/case-studies/ai-lead-follow-up-dealership)
- **Impel en Walter's Auto Group:** +33 % de citas y 27 % de las citas del salón generadas por la IA en 90 días (resumen de búsqueda) — [Impel](https://impel.ai/sales-ai/)
- **Matador:** 86,4 % de asistencia a las citas que agenda (con confirmaciones y recordatorios) y +20 % de citas tras una actualización del producto (proveedor, resumen de búsqueda) — [Matador AI Reply](https://matador.ai/ai-reply); [Matador, guía](https://matador.ai/ai-for-automotive)
- **Calldrip:** +33 % de citas atendiendo los leads fuera de horario (proveedor, resumen de búsqueda) — [Calldrip](https://www.calldrip.com/ai-sales-assistant-auto-dealership-case-study)
- **Fullpath:** no encontré resultados con números.

**LatAm y Argentina (proveedores, sin metodología)**
- **Volanti:** "+20 % de ventas" según iProfesional (junio de 2026). Contacta, hace seguimiento y agenda turnos por WhatsApp. No dice cómo se midió (resumen de búsqueda) — [iProfesional](https://www.iprofesional.com/negocios/456514-como-volanti-logra-que-las-concesionarias-vendan-mas-con-inteligencia-artificial)
- **Cliengo:** "40 % más test drives agendados, 2x leads calificados" con un agente de IA en WhatsApp; son cifras de marketing (resumen de búsqueda) — [Cliengo](https://guiawabusiness.cliengo.com/agente-ia-automotriz)
- **Kavak** usa agentes de IA por WhatsApp desde 2023 (notas previas) — [Letra P](https://www.letrap.com.ar/economia/kavak-consigue-us-300-millones-y-redobla-su-apuesta-argentina-n5421964)

**Velocidad de respuesta (dato viejo)**
- Una auditoría de HBR de 2011 sobre 2.241 empresas encontró que contactar dentro de la hora multiplica casi por 7 la probabilidad de calificar el lead. **Es de 2011 y no es específica de autos** — citado por [Position One](https://www.positionone.ai/insights/case-studies/ai-lead-follow-up-dealership)

### Inferences
- **Qué tiene evidencia:** responder rápido, por más de un canal, y que una persona tome el lead cuando hace falta. Lo dicen Pied Piper (independiente) y la lógica de todos los casos. La IA es un medio para eso; el resultado depende de que el vendedor tome la posta.
- **Qué es humo:** "la IA vende sola". Cox muestra que la mayoría no ve más ventas, y los casos de proveedores miden citas o ventas "influenciadas", no ventas incrementales.
- **Combinación que mejor encaja con lo que Valparaiso ya hace:** reel → anuncio de clic a WhatsApp promocionado solo en Córdoba → agente que califica → vendedor con turno de test drive. Es el patrón de Kavak y Kia Italia, que son los únicos casos de autos con números, aunque sean datos de la empresa publicados por Meta.
- **Qué preguntas debería hacer el agente para calificar:** modelo de interés, uso (km por día, si tiene cochera y dónde carga, que define EV/PHEV/HEV), forma de pago (contado o financiado, qué crédito), si entrega un usado, y día y hora para el test drive.
- **Camino A (rápido, gratis): Business AI en la app WhatsApp Business.** Pros: cero desarrollo. Contras: exige un catálogo (no confirmé que la política de comercio de Meta acepte vehículos), no inicia conversaciones, no entiende audios (en Argentina se usan muchísimo) y vive en la app, no en un CRM.
- **Camino B (Claude Code): bot propio por la API de WhatsApp Cloud,** de tarea específica para atención, calificación y turnos de Valparaiso, que cumple la regla del 15/01/2026.
  - **Fuentes de datos:** un JSON de stock y precios con su fecha, un calendario de test drives y una tabla de financiación con CFT.
  - **Reglas de seguridad:** no comprometer precios que no estén publicados; repetir el texto legal; nunca decir "sin interés" si el crédito ajusta por CER o UVA; avisar que es IA; pasar a un humano a pedido o ante cualquier negociación.
  - **Registro:** cada conversación queda guardada con su código de fuente (palabra clave del reel, "Vengo de ChatGPT…").
  - **Audios:** transcribirlos con Whisper (inferencia; no hay costo publicado comparable).
- **Para no caer en el problema de traspaso de Pied Piper:**
  - el turno agendado le llega al vendedor con un aviso;
  - una alarma salta si un lead calificado no tiene respuesta humana en X minutos dentro del horario;
  - un informe semanal compara leads, turnos, asistencias y ventas.

### Gaps
- No confirmé si la política de comercio de Meta permite cargar autos en el catálogo de WhatsApp Business, que es requisito de Business AI.
- No hay datos de Business AI en concesionarias argentinas, ni de su calidad en español rioplatense.
- No encontré ninguna evaluación independiente de un agente de IA para leads de autos con grupo de control. Todos los números de proveedores son autorreportados.
- No conseguí resultados de Fullpath, ni del informe completo de Pied Piper 2026 (solo la nota de prensa).
- No sé el costo real por conversación de un bot propio en Argentina con las tarifas de Meta de octubre de 2026 más el costo del modelo. Habría que calcularlo con la tabla de Meta en ARS.

## 4. Video personalizado a escala para concesionarias (videos de la unidad enviados al lead, videos automáticos del stock)

### Takeaway
La evidencia es floja y vieja. Lo más sólido son mediciones de interacción, no de ventas:
- **LESA y Vistadash (2021):** +44 % de tiempo en el sitio y −20 % de rebote con video en las fichas.
- **SpinCar e IHS Markit (anterior a 2021; solo lo vi en un repost):** +64 % de compra entre quienes miraron giros de 360°. Es correlación.
- **Cage Automotive / TradePending (sobre 2024, con conflicto de interés):** +25 % de ventas.

Sobre **avatares de IA** (HeyGen, Tavus), las cifras de "+500 % de conversión" no tienen fuente: **no hay ningún estudio controlado que muestre que un avatar sube las respuestas o las ventas**. La versión con más sentido para Valparaiso no es un avatar, sino:
1. un video corto grabado por el vendedor real con el celular, mandado por WhatsApp dentro de la ventana de 24 h;
2. fichas animadas automáticas por unidad o modelo, con su pipeline de HyperFrames, con precio, CFT y legal.

### Cited Findings
- **CDK Global, Friction Points 2026:**
  - el 72 % de los equipos de venta usa video de alguna forma;
  - solo el 49 % de las concesionarias tiene vendedores que mandan videos personalizados;
  - las que usan video tienen un 81 % de "lead-to-contact", sin grupo de control (proveedor, resumen de búsqueda) — [CDK Global](https://www.cdkglobal.com/insights/turn-sales-teams-video-stars)
- **LESA y Vistadash** (publicado el 21/09/2021; 100 concesionarias con al menos 65 % del stock con video; 3 meses; fichas comparadas antes y después del video):
  - tiempo en el sitio de 4,5 a 6,5 minutos (+44 %) y −20 % de rebote;
  - se miran en promedio 8 videos por visita;
  - **no reporta leads ni ventas**;
  - LESA vende el video — [Digital Dealer](https://digitaldealer.com/news/new-nationwide-study-walk-around-videos-increase-auto-dealership-consumer-engagement-nearly-50/145944/)
- **SpinCar e IHS Markit** (6 meses con datos de compra de Polk): quienes miraron fotos compraron un 45 % más y quienes además miraron el giro de 360°, un 64 % más. Lo encontré solo en un repost de foro, sin fecha confirmada y probablemente anterior a 2021 (resumen de búsqueda) — [DealerRefresh](https://forum.dealerrefresh.com/threads/7353/)
- **Cage Automotive / TradePending:** un grupo de menos de 5 concesionarias integró video durante un año y midió +25 % de ventas, +56 % de citas y −31 % de ciclo de venta. Sobre 2024, con el producto de la plataforma (proveedor, resumen de búsqueda) — [TradePending](https://tradepending.com/blog/car-dealership-video-case-study/)
- **VentaVid:** 81 % de respuesta a mensajes con video y ciclo 1,5 veces más rápido (proveedor, sin verificar, resumen de búsqueda) — [VentaVid](https://www.ventavid.com/blog/car-dealership-video-statistics-2026)
- **Avatares de IA:**
  - una página de HeyGen para autos dice "hasta 500 %" de conversión y un CTR 8 veces mayor en emails con video, sin estudio primario (resumen de búsqueda) — [HeyGen](https://www.heygen.com/vi-vn/video/ai-automotive-sales-video-generator)
  - otra comparación dice que en lo citado no hay ningún estudio controlado sobre el efecto de un avatar en respuestas o ingresos (resumen de búsqueda) — [GitHub, Tavus vs HeyGen TCO](https://github.com/webrtc-avatar-ops/tavus-vs-heygen-personalized-sales-video-tco)
- **Video interactivo:** AutoLeadStar habría triplicado y medio (×3,5) el volumen de leads con video interactivo de Blings (proveedor, resumen de búsqueda) — [Vidwave](https://vidwave.ai/ai-video-tools-for-automotive-marketing)
- **Velocidad de respuesta y cierre** (sin relación con el video): el cierre promedio de leads de internet es ~10–12 %, y Velocify habla de +391 % de cierre si se contacta en 60 segundos (fuentes secundarias, resumen de búsqueda) — [RingLead](https://www.ringlead.ca/blog/speed-to-lead/internet-lead-response-statistics-2026/)

### Inferences
- **No hay estudio que separe el efecto del video del de responder rápido y personalmente.** Lo más probable es que gran parte del efecto sea "una persona real que se tomó el trabajo". Por eso el video del vendedor real le gana al avatar.
- **El avatar de IA del vendedor tiene riesgo de confianza**, porque suena a deepfake en un rubro donde el cliente desconfía, y no tiene evidencia. Si se prueba, hay que avisar que es IA. No lo recomendaría para Valparaiso.
- **Lo que sí se puede escalar con Claude Code y HyperFrames (inferencia):**
  - **"Ficha animada" de 8–15 s por modelo:** precio de contado, cuota de ejemplo con CFT y legal, autonomía con su ciclo y "pedinos precio y financiación". Se regenera automáticamente cuando cambia el precio o la promo, y se usa en historias, en los avisos de Mercado Libre y como respuesta del bot.
  - **Video de respuesta al lead:** el bot le pasa al vendedor un guion de 30 s armado con lo que dijo el lead ("Hola Juan, te muestro el Eado Plus en gris que preguntaste; te dejo la cuota de ejemplo con CFT"). El vendedor lo graba en el salón con el celular.
  - **Prueba A/B barata:** a la mitad de los leads calificados se les manda video y a la otra mitad no, y se compara cuántos agendan test drive. Así se genera evidencia propia, que hoy no existe.

### Gaps
- No encontré ningún estudio de 2025–2026 independiente y con grupo de control sobre video personalizado para leads de autos.
- No pude abrir el informe original de SpinCar e IHS Markit ni el de Cage Automotive.
- No hay datos de LatAm sobre video por WhatsApp en ventas de autos.

## 5. IA para reactivar leads viejos y hacer seguimiento de ventas (reactivación de bases)

### Takeaway
Todos los casos con números son de proveedores, y el más detallado muestra un techo bajo: **una venta por cada ~1.000 interacciones** en un período. El único caso de autos con canal WhatsApp (Kavak, publicado por Meta) dice que el anuncio de clic a WhatsApp fue "8x" más eficiente que los mensajes salientes a usuarios inactivos, lo que sugiere que **la reactivación pura por mensaje rinde menos que la entrada por anuncio**. En Argentina la reactivación por WhatsApp tiene tres frenos: el opt-in de cada contacto, el **límite de mensajes de marketing por usuario** (dinámico, sin número publicado) y el **Registro Nacional No Llame, que según la AAIP también cubre WhatsApp**.

### Cited Findings
**Casos de reactivación (proveedores)**
- **Get My Auto (con Ava AI)**, grupo de concesionarias de EE. UU., marzo de 2025, dos períodos:
  - 1.046 y 1.009 interacciones con compradores;
  - **una venta en cada período**;
  - citas que pasaron de 12 a 11, con 3 asistidas en cada período;
  - 94 clientes dormidos y 952 leads viejos que volvieron a responder;
  - el proveedor reporta "+40 % de lead a cita" y −30 % de personal en el BDC — [VisQuanta, que cita a Get My Auto](https://www.visquanta.com/blog/automotive/how-car-dealerships-use-conversational-ai-to-re-engage-old-prospects)
- **Smith Auto Group (2024, VisQuanta):** 227 leads reactivados, "8,1 ventas adicionales" y +76 % de conversión de leads fríos, sin fuente de datos — misma página (proveedor)
- **Capitol Toyota:** un estudio de 120 días con ~64.000 personas en la base habría dado 20 ventas adicionales en 30 días y más de USD 20.000 de margen bruto. Viene del resumen de un webinar de un proveedor; la página que abrí no lo menciona (resumen de búsqueda) — [VisQuanta](https://www.visquanta.com/blog/automotive/ai-revives-dormant-crm-data)
- **Kavak:** mensajes de marketing a usuarios registrados e inactivos, que el agente continúa según lo que el usuario vio antes. El clic a WhatsApp fue "8x" más eficiente que solo mensajes salientes (datos de la empresa) — [WhatsApp Business, caso Kavak](https://whatsappbusiness.com/es-la/resources/success-stories/kavak/)
- **Volanti (Argentina)** detecta oportunidades a partir del historial de service y contacta por WhatsApp; dice "+20 % de ventas" sin metodología (resumen de búsqueda) — [iProfesional](https://www.iprofesional.com/negocios/456514-como-volanti-logra-que-las-concesionarias-vendan-mas-con-inteligencia-artificial)

**Seguimiento (EE. UU.)**
- Cox: "coordinar el seguimiento de clientes" es el 2.º uso de IA más común (40 %); solo el 22 % de las que usan IA vio más ventas — [Cox Automotive](https://www.coxautoinc.com/press-releases/new-cox-automotive-ai-in-auto-retail-tracker/)
- Pied Piper 2025: los clientes quedaron sin respuesta ("ghosted") el 20 % de las veces (resumen de búsqueda) — [OPE Plus](https://ope-plus.com/2025/02/03/pied-piper-releases-annual-internet-lead-effectiveness-study-results/24580/)

**Frenos para Argentina**
- **Límite por usuario de Meta:**
  - "The per-user marketing limit adapts automatically over time based on a person's recent engagement levels";
  - si el mensaje se bloquea, el webhook devuelve el error 131049, y hay que esperar 24 h para reintentar;
  - si el usuario responde, se abre una ventana de atención de 24 h;
  - los mensajes de marketing dentro de esa ventana no cuentan para el límite.

  Meta no publica un número fijo: "dos por día" es una estimación de terceros — [Meta, per-user limits](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/marketing-templates/per-user-limits.md); [Infobip](https://cdn-web.infobip.com/uploads/markdown-exports/www.infobip.com/blog/what-is-whatsapp-frequency-capping.md) (resumen de búsqueda)
- **Opt-in y plantillas:** solo se puede escribir a quien dio su número y aceptó recibir mensajes, y siempre arrancando con plantillas aprobadas (notas previas) — [WhatsApp Business Policy](https://whatsappbusiness.com/policy/)
- **Registro No Llame:** según las preguntas frecuentes de la AAIP, un celular inscripto queda protegido de llamadas publicitarias "y también mensajes de texto (SMS) o mensajería instantánea (WhatsApp)". Las empresas tienen hasta 30 días desde la inscripción para dejar de contactar, y se puede denunciar con 31 días de inscripción. Una guía de 2026 dice que el alcance sobre WhatsApp se discute (resumen de búsqueda) — [AAIP, No Llame FAQ](https://nollame.aaip.gob.ar/faqs.html); [El Destape, 12/11/2026](https://www.eldestapeweb.com/sociedad/registro-no-llame-inscribir-dejar-recibir-llamadas-numeros-desconocidos-20261112144246)

### Inferences
- **La reactivación "masiva con IA" es la táctica con más humo.** Los casos que muestran números finos (Get My Auto) dan una venta por cada ~1.000 interacciones. Igual puede ser rentable si la base es grande y el costo por mensaje es bajo, pero no hay que esperar milagros.
- **Para Valparaiso tiene sentido en versión chica y con algo nuevo que decir,** sobre la base de clientes y leads con consentimiento documentado. Por ejemplo:
  - "llegó el Eado Plus que consultaste, con entrega inmediata (si es cierto ese día)";
  - "cambió la promo de financiación: tasa y CFT";
  - "tu auto cumple 3 años: tasación para entregarlo".

  Un mensaje genérico de "¿seguís buscando auto?" quema el límite por usuario y la reputación del número.
- **Pasos con Claude Code (inferencia):**
  1. Limpiar la base y cruzarla con el registro No Llame, si la AAIP da acceso a la consulta para empresas.
  2. Segmentar por modelo de interés y fecha.
  3. Armar plantillas por segmento.
  4. **Dejar un 20 % de la base sin contactar como grupo de control,** así se mide la venta incremental de verdad.
  5. Pasar al vendedor a quien responde con intención.
- **El seguimiento con IA rinde más en lo "aburrido":** recordar el turno de test drive (la asistencia de Matador viene de confirmaciones y recordatorios), avisar al vendedor y reabrir los presupuestos sin respuesta a los 2–3 días. Ahí el riesgo legal es bajo y el beneficio, directo.

### Gaps
- No encontré ningún caso de reactivación de concesionaria auditado, ni ninguno de Argentina con números.
- No confirmé si las empresas pueden consultar la base del No Llame antes de mandar mensajes, ni con qué costo y procedimiento.
- No sé qué parte de la base actual de Valparaiso tiene consentimiento para recibir mensajes de marketing por WhatsApp.

## 6. Riesgos y cumplimiento (CFT, defensa del consumidor, políticas de WhatsApp y OpenAI, Ley 25.326)

### Takeaway
Hay seis riesgos concretos:
1. **El bot que inventa o se compromete.** El caso del Tahoe a USD 1 de 2023 no obligó a la concesionaria, pero la expuso.
2. **Publicidad de financiación sin CFT, o con "sin interés" en un crédito UVA o CER.**
3. **Datos personales** del lead sin consentimiento ni finalidad clara (Ley 25.326, todavía vigente; la reforma no se sancionó).
4. **Mensajes de WhatsApp sin opt-in o a números del No Llame.**
5. **Traspasos rotos entre la IA y el vendedor**, que Pied Piper identifica como el mayor riesgo operativo.
6. **Políticas de plataforma:** la de OpenAI prohíbe anuncios de financiación fuera de EE. UU. sin aprobación y el enlace directo a WhatsApp; la de Meta prohíbe los asistentes generales.

### Cited Findings
- **El bot que se compromete:** en diciembre de 2023, el chatbot de Chevrolet of Watsonville (basado en ChatGPT) "aceptó" vender una Tahoe 2024 por USD 1 y lo llamó vinculante. La concesionaria no lo cumplió y lo desactivó. GM aclaró que no es una práctica de toda la compañía. Un estudio jurídico sostiene que no era un medio razonable para contratar, pero que depende de qué dijo la concesionaria sobre su bot (**caso de 2023, EE. UU.**) — [GM Authority](https://gmauthority.com/blog/2023/12/gm-dealer-chat-bot-agrees-to-sell-2024-chevy-tahoe-for-1/amp/); [McDermott Will & Emery](https://www.mcdermottlaw.com/wp-content/uploads/2024/05/Can-Chatbot-Interactions-Lead-To-Enforceable-Contracts.pdf) (resumen de búsqueda)
- **Pruebas de ataque:** hubo más de 3.000 intentos de "hackear" el chatbot de una concesionaria en un fin de semana (resumen de búsqueda, misma época) — [The Autopian](https://theautopian.com/there-were-more-than-3000-attempts-to-hack-dealerships-ai-chatbot-this-weekend)
- **Traspasos IA → vendedor:** cuando la consulta necesita a una persona, el puntaje es 9 puntos más bajo y es el doble de probable que no haya respuesta personal. Las fallas "often don't show on CRM dashboards" — [Auto Remarketing / Pied Piper 2026](https://www.autoremarketing.com/ar/analysis/study-finds-ai-raises-dealerships-internet-lead-responsiveness-but-creates-added-risks)
- **Financiación en la publicidad (notas previas, normas de 2017, sin confirmar si siguen vigentes sin cambios):**
  - **Res. 51-E/2017:** el precio de contado es la base, y sobre él se informan el CFT, la TEA, el precio total financiado, el anticipo y la cantidad y el monto de las cuotas.
  - **Res. 240-E/2017:** limita la obligación del CFT al comercio electrónico y a la publicidad en medios masivos.
  - Fuentes: [Marval](https://www.marval.com/Publicacion/nueva-obligacion-de-diferenciar-los-precios-en-operaciones-al-contado-y-las-financiadas-a-traves-de-medios-de-pago-alternativos-12945?lang=es); [Res. 240-E/2017](https://www.argentina.gob.ar/normativa/nacional/norma-273071/texto)
- **OpenAI:** financiación fuera de EE. UU. prohibida salvo aprobación; prohibido el enlace directo a chats; quien capta leads para terceros tiene que avisarlo — [OpenAI Ad Policies](https://openai.com/policies/ad-policies/)
- **WhatsApp:**
  - asistentes de IA de uso general prohibidos desde el 15/01/2026 (notas previas) — [TechCrunch](https://techcrunch.com/2025/10/18/whatssapp-changes-its-terms-to-bar-general-purpose-chatbots-from-its-platform/)
  - opt-in, plantillas, vía de escalamiento a un humano y prohibición de pedir números completos de tarjeta (notas previas) — [WhatsApp Business Policy](https://whatsappbusiness.com/policy/)
  - si los catálogos se usan para bienes prohibidos por la Commerce Policy de Meta, Meta puede restringir el uso de WhatsApp (resumen de búsqueda) — [WhatsApp Business Policy](https://whatsappbusiness.com/policy/)
- **Datos personales:**
  - **Guía de la AAIP:** publicó una "Guía para entidades públicas y privadas en materia de Transparencia y Protección de Datos Personales para una IA responsable" (programa de la Res. 161/2023). La guía es orientativa y no tiene sanciones propias, pero las obligaciones de la Ley 25.326 sí (resumen de búsqueda) — [IAPP](https://iapp.org/news/a/la-autoridad-de-protecci-n-de-datos-personales-de-argentina-publica-su-gu-a-para-el-uso-responsable-de-la-inteligencia-artificial); [AAIP, guía (PDF)](https://argentina.gob.ar/sites/default/files/aaip-argentina-guia_para_usar_la_ia_de_manera_responsable.pdf); [Diario Judicial](https://www.diariojudicial.com/news-98782-una-guia-que-no-fue-hecha-por-ia)
  - **Reforma:** en 2026 hay varios proyectos para reformar o reemplazar la Ley 25.326 y uno de ley de IA, ninguno sancionado (resumen de búsqueda) — [IAPP, notas LatAm](https://iapp.org/news/a/notas-de-la-iapp-america-latina-avances-en-la-implementaci-n-de-normas-sobre-ia-y-protecci-n-de-datos)
- **Registro No Llame:** la AAIP dice que cubre llamadas, SMS y WhatsApp publicitarios — [AAIP, No Llame FAQ](https://nollame.aaip.gob.ar/faqs.html)
- **Precisión de la IA con negocios chicos (notas previas):** el 50 % de las pymes tuvo al menos un dato falso en las respuestas de IA, contra el 32 % de las grandes (Searchable, Londres) — [IT Brief UK](https://itbrief.co.uk/story/london-smes-suffer-ai-misinformation-in-search-tests). Además, ChatGPT puede inventar tasas o mostrar datos de inflación viejos — [iProfesional](https://www.iprofesional.com/tecnologia/468562-iadiccion-riesgos-de-pedirle-consejos-economicos-a-chatgpt)

### Inferences
- **Reglas de diseño para cualquier herramienta de Valparaiso (inferencia, coherentes con su CLAUDE.md):**
  1. **El bot solo dice precios, cuotas y CFT que estén publicados en una página con "vigente al".** Ante cualquier negociación o pedido de "reservá", deriva a un humano. Esto reduce el riesgo de oferta vinculante y de publicidad engañosa (hay que confirmar con un abogado el alcance del art. 7 de la Ley 24.240).
  2. **Cada respuesta sobre financiación lleva el CFT y el texto legal del dueño;** nunca "sin interés" ni "cuotas fijas" en un crédito UVA o CER.
  3. **Al iniciar la conversación se avisa que es una IA,** con un mensaje breve de privacidad: quién trata los datos, para qué y cómo pedir la baja.
  4. **Opt-in explícito** para mensajes de marketing, guardado con fecha y origen, y cruce con el No Llame antes de cualquier campaña.
  5. **Registro de conversaciones** y una revisión semanal de una muestra.
  6. **No usar la marca de Changan, GWM o Mitsubishi ni el nombre de bancos en anuncios** salvo que sea la promo de ellos (regla del dueño).
- **La política de OpenAI y la regla argentina empujan para el mismo lado:** el anuncio habla del auto y del beneficio, y la página de destino tiene la financiación completa con CFT.

### Gaps
- No leí el texto vigente de la Ley 24.240 (arts. 7 y 36), del DNU 274/2019 de lealtad comercial ni de las Res. 51-E y 240-E/2017 al día de hoy. Todo eso va con un abogado.
- No confirmé si una base de leads de una concesionaria tiene que inscribirse en el Registro Nacional de Bases de Datos de la AAIP, ni cómo trata la Ley 25.326 el uso de un proveedor de IA extranjero (transferencia internacional).
- No encontré jurisprudencia argentina sobre declaraciones de chatbots comerciales.

## 7. Síntesis: qué tiene evidencia, qué es humo y cómo lo implementaría Valparaiso con herramientas hechas con Claude Code

### Takeaway
Ninguna táctica "con IA" tiene evidencia independiente de ventas incrementales en concesionarias. Lo que más se acerca es:
1. **Responder rápido, por varios canales y con traspaso a una persona** (Pied Piper, independiente).
2. **El anuncio de clic a WhatsApp con un agente que califica** (Kavak y Kia Italia: datos de la empresa publicados por Meta, pero los únicos casos de autos con ventas o leads contados).
3. **Páginas que responden preguntas y páginas de financiación** para que la IA cite el sitio (A3: correlación, proveedor).

Lo que hoy es mayormente humo para una concesionaria argentina:
- ChatGPT Ads como fuente de leads (sin benchmarks y con la financiación prohibida fuera de EE. UU.);
- el schema o las "técnicas GEO" como solución;
- los avatares de IA;
- la reactivación masiva con promesas de muchas ventas.

### Cited Findings
| Táctica | Evidencia | Calidad | Fuente |
|---|---|---|---|
| Respuesta rápida y multicanal, con traspaso a una persona | 51 % de "respuesta perfecta"; el traspaso IA → vendedor es el punto débil | Independiente (comprador incógnito), sin dato de ventas | [Auto Remarketing / Pied Piper](https://www.autoremarketing.com/ar/analysis/study-finds-ai-raises-dealerships-internet-lead-responsiveness-but-creates-added-risks) |
| Clic a WhatsApp + agente de IA | Kavak: 1 de cada 3 conversaciones → lead calificado. Kia Italia: 5 ventas en 4 semanas y −53 % de costo por venta | Datos de la empresa, publicados por Meta | [Kavak](https://whatsappbusiness.com/es-la/resources/success-stories/kavak/); [Kia Italia](https://whatsappbusiness.com/es-la/resources/success-stories/kia-italia/) |
| Seguimiento y agenda con IA | +18 % de conversión (Impel); 86 % de asistencia (Matador) | Proveedor, sin control | [Position One](https://www.positionone.ai/insights/case-studies/ai-lead-follow-up-dealership); [Matador](https://matador.ai/ai-reply) |
| Contenido que responde preguntas | Páginas editoriales citadas 21,1 % contra 0,8 % de las fichas de stock | Correlacional, proveedor, metodología publicada | [A3 Brands](https://a3brands.com/ai-search-study/) |
| Schema de vehículos | Sin efecto medible | Ídem | [A3 Brands](https://a3brands.com/ai-search-study/) |
| ChatGPT Ads | Sin benchmarks oficiales; CTR de ~0,7–0,9 % reportado en EE. UU. | Terceros | [OpenAI Help](https://help.openai.com/en/articles/20001207-ads-in-chatgpt-the-basics); [Kompozy](https://kompozy.io/guides/chatgpt-ads-performance); [Inpromptads](https://www.inpromptads.com/chatgpt-ads-benchmarks/) |
| Video en las fichas | +44 % de tiempo en el sitio, sin datos de leads (2021) | Proveedor, viejo | [Digital Dealer](https://digitaldealer.com/news/new-nationwide-study-walk-around-videos-increase-auto-dealership-consumer-engagement-nearly-50/145944/) |
| Avatares de IA | "+500 %" sin fuente | Marketing | [HeyGen](https://www.heygen.com/vi-vn/video/ai-automotive-sales-video-generator) |
| Reactivación con IA | ~1 venta por cada ~1.000 interacciones en un período | Proveedor | [VisQuanta / Get My Auto](https://www.visquanta.com/blog/automotive/how-car-dealerships-use-conversational-ai-to-re-engage-old-prospects) |
| Adopción de IA en general | 82 % la usa; solo el 22 % vio más ventas | Encuesta Cox, EE. UU. | [Cox Automotive](https://www.coxautoinc.com/press-releases/new-cox-automotive-ai-in-auto-retail-tracker/) |

### Inferences
- **Orden de implementación sugerido para Valparaiso** (inferencia; los costos son estimaciones mías a confirmar):
  1. **Semanas 1–2: base de datos y medición.**
     - Un JSON de stock, precio y financiación con CFT y "vigente al", a partir de WordPress.
     - Códigos de fuente por reel y canal, más UTM.
     - Planilla o CRM simple de lead → turno → asistencia → venta.
     - Alarma si un lead no tiene respuesta humana a tiempo.

     Sin esto, nada de lo de abajo se puede evaluar.
  2. **Semanas 2–4: clic a WhatsApp desde los reels que funcionan,** promocionados en ~50 km de Córdoba. Primero con Business AI en la app WhatsApp Business, si acepta el catálogo de autos. Si no, con un bot propio de tarea específica por la API de WhatsApp Cloud y Claude, que califique, agende el test drive y pase al vendedor. Es lo que tiene los únicos casos de autos con números.
  3. **Semanas 3–8: páginas en valparaisomotors.com.ar.** Una por modelo con financiación y CFT, y 5–8 páginas de contenido que reusen los guiones de los reels (EV/PHEV/HEV, créditos, cuenta de la nafta, "¿necesito instalar algo en casa?"). Completar Google Business Profile, decidir lo de Google-Extended y correr el monitor semanal de visibilidad.
  4. **Semanas 6–10: video.**
     - Fichas animadas automáticas por modelo, con el pipeline de HyperFrames.
     - Video del vendedor real a los leads calificados, como prueba A/B.
  5. **Después: experimentos con control.**
     - ChatGPT Ads (USD 300–500, creatividades sin financiación, destino a la página del modelo), si se puede segmentar Córdoba.
     - Reactivación de la base con consentimiento, dejando un 20 % sin contactar como grupo de control.
- **Métricas que importan** (alineadas con el CLAUDE.md del dueño): leads por fuente, % que llega a turno de test drive, % de asistencia, ventas por fuente y tiempo hasta la primera respuesta humana. No vistas ni "menciones en IA" por sí solas.
- **Ventaja de hacerlo con Claude Code:** todo esto es integración a medida (WordPress, WhatsApp, calendario, planilla, HyperFrames). Los proveedores de EE. UU. (Impel, Matador, Fullpath) no operan en español rioplatense ni con CFT argentino.

  **Riesgo:** mantenimiento. Si el JSON de precios queda viejo, el bot y las páginas dicen cosas falsas, que es justo el problema que se quería resolver.

### Gaps
- No hay ninguna medición de línea de base de Valparaiso: leads por canal, tiempo de respuesta, cierre ni tráfico desde IA. Hay que pedírsela al dueño antes de prometer resultados.
- No hay costos verificados en Argentina para el bot propio (Meta en ARS más el modelo) ni para la promoción local de clic a WhatsApp en Córdoba.
- Todas las cifras de resultados vienen de EE. UU., Italia o México. Si se transfieren a una concesionaria de Córdoba, es una suposición.
