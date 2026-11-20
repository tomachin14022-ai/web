# Plataformas y canales recién abiertos (2025–2026) donde un constructor solo puede llegar primero, con foco en español y LatAm

> Notas de investigación al 20/11/2026. Todo lo que tiene enlace salió de una fuente consultada en esta sesión. Lo que es deducción propia va en "Inferencias", y lo que no se pudo confirmar va en "Gaps". Cuando una fuente es secundaria, de marketing o anterior a 2025, se aclara.

## 1. ¿Qué tiendas de asistentes de IA se abrieron a terceros, cuándo, con qué alcance y cómo cobra el desarrollador?

### Takeaway
ChatGPT (ahora "plugins"), Claude (Marketplace/directorio) y Gemini (Connected Apps) abrieron directorios para terceros entre diciembre de 2025 y octubre de 2026, pero **ninguno le paga al desarrollador ni le deja cobrar dentro del asistente por bienes digitales**. Sirven como canal de distribución hacia un producto que se cobra afuera (en tu dominio, con suscripción B2B o comisión por lead). Gemini todavía está cerrado a desarrolladores fuera de EE. UU.

### Cited Findings
**ChatGPT (OpenAI): apps, después "plugins"**
- Las apps en ChatGPT y el Apps SDK se anunciaron en octubre de 2025 (DevDay) — [OpenAI, "Introducing apps in ChatGPT"](https://openai.com/index/introducing-apps-in-chatgpt/)
- OpenAI abrió los envíos de apps de terceros y lanzó el directorio dentro de ChatGPT (chatgpt.com/apps) en diciembre de 2025. Se envían desde la OpenAI Developer Platform con datos de conexión MCP, instrucciones de prueba, metadatos y países de disponibilidad — [VentureBeat](https://venturebeat.com/technology/openai-now-accepting-chatgpt-app-submissions-from-third-party-devs-launches); [Yahoo Tech](https://tech.yahoo.com/ai/chatgpt/articles/connector-era-over-now-submit-093446755.html)
- El 9 de julio de 2026 el directorio de apps pasó a ser el **directorio de plugins** (chatgpt.com/plugins), compartido entre ChatGPT y Codex — [Ayuda de OpenAI (es-419)](https://help.openai.com/es-419/articles/12503483-apps-in-chatgpt-and-the-apps-sdk); [Wikipedia, ChatGPT](https://en.wikipedia.org/wiki/ChatGPT) ("In July 2026, ChatGPT apps were renamed to plugins"); [issue de GitHub que lo resume](https://github.com/dnobj/mail-letter-irl/issues/476) (fuente secundaria)
- Alcance: **900 millones de usuarios semanales en febrero de 2026** — [Wikipedia, ChatGPT](https://en.wikipedia.org/wiki/ChatGPT)
- Publicidad en ChatGPT: pruebas anunciadas el 17/01/2026, anuncios visibles desde marzo de 2026 y US$1.000 millones de ingresos por anuncios en agosto de 2026 — [Wikipedia, ChatGPT](https://en.wikipedia.org/wiki/ChatGPT)
- **Reglas de cobro vigentes (guía de plugins, sin fecha de actualización):**
  - "Currently, plugins may conduct commerce only for physical goods."
  - "Selling digital products or services—including subscriptions, digital content, tokens, or credits—is not allowed."
  - No se pueden mostrar planes, iniciar suscripciones ni promover upgrades, aunque los suscriptores existentes sí pueden usar lo que ya pagaron.
  - El checkout tiene que ser externo, en el dominio propio.
  - Instant Checkout está en beta y "only to select marketplace partners".
  - No se puede embeber otro checkout de terceros.
  - No se puede cobrar un recargo por usar el servicio desde ChatGPT.
  - Los envíos tienen que venir de personas u organizaciones verificadas.
  - Los plugins con buena utilidad y satisfacción "may be eligible" para tener más distribución (lugar destacado en el directorio o sugerencias proactivas).
  - Fuente: [OpenAI, guía de plugins](https://developers.openai.com/apps-sdk/app-submission-guidelines)
- En marzo de 2026, CNBC informó que OpenAI terminaba Instant Checkout y pasaba a apps manejadas por los propios comercios — [CNBC, 20/03/2026](https://www.cnbc.com/2026/03/20/open-ai-agentic-shopping-etsy-shopify-walmart-amazon.html). La guía actual de plugins todavía lo menciona como beta para socios elegidos: las fuentes no coinciden del todo.
- En enero de 2026, un hilo del foro de desarrolladores decía que se rechazaban las apps con cobro por Stripe (por uso o suscripción) — [OpenAI Developer Community](https://community.openai.com/t/chatgpt-app-monetization-apps-sdk/1372343)

**Claude (Anthropic): Marketplace y directorio**
- Claude Marketplace salió el 23/09/2026 con **más de 2.000 conectores y plugins**, organizados en conectores/plugins, agentes/productos y socios de servicios — [Ghacks, 27/09/2026](https://www.ghacks.net/2026/09/27/anthropic-launches-claude-marketplace-with-more-than-2000-connectors-and-plugins/); [BleepingComputer](https://bleepingcomputer.com/news/artificial-intelligence/anthropic-turns-claude-into-an-ai-marketplace-with-2-000-plus-plugins-and-connectors). Las fechas vienen de prensa secundaria.
- El portal de envíos al directorio abrió el 25/09/2026 para usuarios con plan pago. Pasa por validación automática, revisión de seguridad y seguimiento del estado de revisión — [Unite.AI](https://www.unite.ai/anthropic-opens-directory-submission-portal-for-claude-plugins/)
- Docs oficiales:
  - Los conectores MCP remotos se envían desde claude.ai/directory/manage, y el formulario viejo de Console ya no se usa.
  - Hay conectores "verificados" (revisados por Anthropic) y "de la comunidad".
  - Los plugins son paquetes de conectores MCP y/o Agent Skills.
  - No hay un envío aparte para el Marketplace.
  - Fuentes: [claude.com/docs/directory/publish](https://claude.com/docs/directory/publish); [claude.com/docs/connectors/building/submission](https://claude.com/docs/connectors/building/submission)
- BleepingComputer **no menciona** ingresos para el desarrollador (ni listados pagos ni reparto de ingresos). Las empresas que venden software hecho con Claude pueden pedir que las listen — [BleepingComputer](https://bleepingcomputer.com/news/artificial-intelligence/anthropic-turns-claude-into-an-ai-marketplace-with-2-000-plus-plugins-and-connectors)

**Gemini (Google): Connected Apps Platform**
- Vista previa lanzada el 28/10/2026 para llevar apps a Gemini y a Search, por un servidor MCP en la nube o por Android MCP con las APIs de AppFunctions. Se registran y envían en Google Connected Console — [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/connected-apps-one-place/)
- **Solo para desarrolladores de EE. UU.** por ahora, con más regiones "soon" — [Android Authority](https://androidauthority.com/google-gemini-search-connected-apps-developer-platform-3729015)
- Catálogo de terceros: más de 50 (Adobe, Dropbox, Instacart, OpenTable, Ticketmaster) — [9to5Google, 28/10/2026](https://9to5google.com/2026/10/28/gemini-google-connected-apps-platform)
- En agosto de 2026, Zapier reportó que las apps conectadas de terceros no le funcionaron en sus pruebas — [Zapier](https://zapier.com/de/blog/gemini-apps/)

**Microsoft 365 Copilot: Agent Store**
- Presentado el 22/05/2025 (fuente de 2025): da acceso a usuarios de M365 Copilot, co-marketing y métricas de uso, y valida la seguridad de cada agente de terceros — [Microsoft devblog](https://devblogs.microsoft.com/microsoft365dev/introducing-the-agent-store-build-publish-and-discover-agents-in-microsoft-365-copilot/)
- Agent 365 está disponible para todos desde el 1/05/2026 — [Penta](https://penta.ch/insights/microsoft-365-agent-store-what-is-already-there-and-what-it-costs)

### Inferencias
- Con 900 M de usuarios semanales, ChatGPT es el canal más grande. Pero como no deja vender digital adentro, el modelo viable para una persona sola es: plugin gratis que conecta con una cuenta de un SaaS que se paga afuera, o comisión o cobro por lead al comercio (B2B, fuera de la plataforma).
- Claude Marketplace es más chico, pero su público son profesionales y empresas que pagan plan. Sirve para productos B2B (contadores, estudios jurídicos, pymes).
- Gemini va a ser una ventana de "primero en llegar" cuando se abra a desarrolladores de fuera de EE. UU. Hoy no se puede entrar desde Argentina.
- El cambio de nombre (de apps a plugins) y el fin o la limitación de Instant Checkout muestran reglas inestables: es riesgo de plataforma alto. No hay que depender de un solo directorio.

### Gaps
- No encontré la cantidad de plugins que tiene hoy el directorio de ChatGPT, ni datos de tráfico o instalaciones para desarrolladores de terceros. No hay evidencia pública de ingresos de terceros salidos del directorio.
- No encontré si Microsoft reparte ingresos o cobra comisión en el Agent Store.
- No investigué Perplexity ni las novedades de Apple (App Intents, Siri) por límite de tiempo.
- Los plugins de Claude Marketplace pueden ser de pago, pero el pago no pasa por Anthropic: no está confirmado en las docs oficiales.

## 2. WhatsApp y Meta: ¿qué puede hacer un tercero en 2026?

### Takeaway
Meta **cerró WhatsApp a los asistentes de IA de uso general** (desde el 15/01/2026) y está volviendo un producto propio y masivo el "chatbot para pymes" (Meta Business Agent, global desde junio de 2026). Para un constructor nuevo, WhatsApp es un canal hostil o ya cubierto, salvo como canal de un negocio vertical propio.

### Cited Findings
- Los nuevos términos de la WhatsApp Business API prohíben distribuir asistentes de IA de uso general desde el 15/01/2026. Siguen permitidos los bots de atención de un negocio — [TechCrunch, oct. 2025](https://techcrunch.com/2025/10/18/whatssapp-changes-its-terms-to-bar-general-purpose-chatbots-from-its-platform/?source_type=web); [9to5Mac](https://9to5mac.com/2025/10/20/whatsapp-bans-ai-chatbots-from-using-its-business-api/)
- Excepción temporal (1 año) para bots de terceros en Europa, por presión antimonopolio — [eWeek](https://www.eweek.com/news/meta-allows-rival-ai-chatbots-whatsapp-europe/)
- **Meta Business Agent**, global desde el 3/06/2026 (antes probado unos dos años en India y México):
  - responde preguntas, recomienda productos, reserva turnos y califica leads; también funciona en los DM de Instagram;
  - va a estar incluido en algunos niveles de WhatsApp Business Premium, y las empresas grandes pagan por tokens;
  - Meta arma una plataforma para que las empresas grandes conecten agentes con Shopify, Zendesk y Shopee.
  - Fuente: [TechCrunch, 3/06/2026](https://www.techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/)
- Nuvemshop/Tiendanube es la primera plataforma de e-commerce de LatAm conectada a Business AI de Meta, con su propio "MCP Storefront": el agente consulta el catálogo y sigue los pedidos por WhatsApp e Instagram. Se habilita de a poco — [Central do Varejo](https://centraldovarejo.com.br/meta-integra-business-ai-a-nuvemshop-e-torna-plataforma-a-primeira-de-e-commerce-da-america-latina-com-a-solucao/?amp=1)
- El 13/05/2026, Meta lanzó un asistente de IA para desarrolladores de mensajería empresarial — [Meta for Developers](https://developers.facebook.com/blog/post/2026/05/13/meta-ai-developer-assistant-now-live-for-business-messaging/)
- Pagos en Brasil:
  - los pedidos interactivos inician el pago (Pix con copiar y pegar, en la app del banco); WhatsApp "does NOT support payment reconciliations"; los links de pago abren en el navegador — [Meta docs, Brazil Payments](https://developers.facebook.com/documentation/business-messaging/whatsapp/payments/payments-br/overview);
  - según una sola fuente, en Brasil se cortaron los pagos con tarjeta dentro del chat para compras nuevas desde enero de 2026 — [Sinch](https://sinch.com/pt/blog/whatsapp-pay-noticias-estatisticas-desenvolvimento-pagamentos-moveis/) (sin confirmar con Meta).

### Inferencias
- El "bot de WhatsApp para pymes" ya es un commodity, y Meta lo regala dentro de su plan Premium. Coincide con que el emprendedor rechaza esa idea.
- La **conciliación de pagos** que WhatsApp no hace en Brasil es un hueco técnico. Pero es Brasil, no Argentina, y lo cubren integradores como Infobip o Sinch: no es prioridad.

### Gaps
- No encontré si Meta Business Agent ya funciona en español en Argentina ni con qué precio en ARS.
- No hay documentación pública de una API o MCP para que terceros sumen herramientas a Business Agent fuera de las empresas grandes.

## 3. Ecosistemas de comercio y fintech de LatAm (Mercado Libre/Pago, Tiendanube, MODO, Ualá, finanzas abiertas y protocolos agénticos)

### Takeaway
Los jugadores grandes de Argentina **ya están entrando solos a los asistentes**: Tiendanube (conectores oficiales para ChatGPT y Claude, Business AI de Meta y ChatGPT Ads), MODO (app en ChatGPT y compras con Frávega), Despegar (plugin en ChatGPT) y Mercado Libre/Pago (MCP para desarrolladores). Además, la capa de "MCP de una API latinoamericana" ya la está volviendo commodity CodeSpar, con más de 100 servidores. Finanzas abiertas en Argentina existe por decreto, pero **todavía no tiene estándares técnicos** (se espera para 2027).

### Cited Findings
**Mercado Libre / Mercado Pago**
- MCP oficial de Mercado Libre (`https://mcp.mercadolibre.com/mcp`), con OAuth 2.0 y actualizado el 20/05/2026. La herramienta documentada es `search_documentation` (busca en la documentación para desarrolladores), y el repositorio de GitHub tiene un commit y unas 6 estrellas — [developers.mercadolibre.com.ar/mcp-server](https://developers.mercadolibre.com.ar/en_us/mcp-server); [GitHub mercadolibre-mcp-server](https://github.com/mercadolibre/mercadolibre-mcp-server)
- El MCP de Mercado Pago (`mcp.mercadopago.com/mcp`, mayo de 2025) sirve para que los desarrolladores integren cobros — [Mercado Pago Developers, 30/05/2025](https://www.mercadopago.com.mx/developers/en/news/2025/05/30/Mercado-Pago-MCP-Server--Accelerate-Your-Integrations-with-Our-AI). Desde abril de 2026 publica `llms.txt` — [Mercado Pago Developers, 16/04/2026](https://www.mercadopago.com.br/developers/pt/news/2026/04/16/Feed-your-AI-with-our-full-documentation-via-llms-txt)
- Mercado Livre (Brasil) tiene agentes propios para vendedores: un Asistente de Ventas y un Asistente de Ads que manda recomendaciones por WhatsApp — [Ecosistema Startup, Mercado Libre Experience 2026](https://ecosistemastartup.com/mercado-libre-experience-2026-ia-y-datos-para-ecommerce/). En Mercado Libre Vehículos México, un agente hecho con Wonderful atendió el 99 % de las conversaciones sin intervención humana y generó unas 2.200 cotizaciones (datos del proveedor) — [Mobile Time, 21/08/2026](https://mobiletime.la/noticias/21/08/2026/venta-de-autos-usados-en-mexico/)
- Conectores alojados de terceros para usar Mercado Libre en Claude o ChatGPT:
  - AnythingMCP: genérico, en la nube, con prueba gratis — [AnythingMCP](https://anythingmcp.com/es/guides/connect-mercado-libre-to-claude);
  - Kondado: pago, sobre todo para Brasil, con 28 tablas del vendedor que incluyen pedidos, facturas, Ads, reclamos y stock — [Kondado](https://kondado.io/blog/en/a/mercado-libre-in-chatgpt-and-claude-mcp).

**Tiendanube / Nuvemshop**
- Tienda de apps con "más de 700 apps" y 10 categorías: Marketing, Canales de ventas, Recursos extras, Comunicación, Seguridad, Pagos, Envíos, Gestión, Estadísticas y Dropshipping. **No hay categoría de IA.** Las apps con IA están sueltas (Shoptic TiendaPop, TITANPush, NotChatbot, CrossUp, Size Grid, Clostech). La página no dice cómo se le paga al desarrollador — [Tiendanube, tienda de aplicaciones](https://www.tiendanube.com/tienda-aplicaciones-nube)
- Ventas que las tiendas de Tiendanube reciben desde ChatGPT: unos US$230.000 en el 1.er semestre de 2025 y más de US$2 millones en el 1.er semestre de 2026 (dato de Tiendanube a Infobae) — [Ecosistema Startup](https://ecosistemastartup.com/tiendanube-ventas-via-chatgpt-se-multiplican-por-10-en-argentina/)
- Tiendanube tiene **conectores oficiales para ChatGPT y Claude** para manejar la tienda conversando, y está conectada a ChatGPT Ads (el 15 % del tráfico agéntico es publicidad paga) — [iProUP](https://www.iproup.com/innovacion/69897-tiendanube-inteligencia-artificial-permite-gestionar-tienda-online-voz)
- Del tráfico que llega desde asistentes, solo compra entre el 3 % y el 5 %; el crecimiento del tráfico agéntico en México fue de 396 % interanual — [Expansión, 3/08/2026](https://expansion.mx/tecnologia/2026/08/03/chatgpt-quintuplico-visitas-tiendas-en-linea)
- Tiendanube proyecta unos US$4.000 millones transaccionados en LatAm en 2026, casi la mitad en Argentina — [Forbes Argentina](https://www.forbesargentina.com/negocios/comercio-agentico-implementacion-ia-us-4000-millones-transacciones-hoja-ruta-tiendanube-redefinir-e-commerce-n96737)
- Existe **Pistacho App**, que "prepara 10.000 tiendas argentinas para ChatGPT" — [Ecosistema Startup](https://ecosistemastartup.com/?p=114342) (solo el titular: la página dio 403).

**MODO, Ualá y otros jugadores argentinos en asistentes**
- MODO tiene una herramienta en ChatGPT para consultar promociones y beneficios — [Mercado](https://mercado.com.ar/finanzas/modo-suma-su-aplicacion-a-chatgpt-para-consultar-promociones-y-beneficios-vigentes). En septiembre de 2026 lanzó con Frávega la compra de productos desde ChatGPT, con comisión por transacción — [El Economista](https://eleconomista.com.ar/negocios/modo-apuesta-sacar-ventaja-ia-alianza-fravega-lanza-una-funcion-usuarios-puedan-comprar-productos-chatgpt-n98390)
- Despegar tiene plugin en ChatGPT (vuelos, hoteles, actividades y seguros; el checkout es en Despegar) — [ChatGPT plugins, Despegar](https://chatgpt.com/plugins/plugin_asdk_app_6ac55c1644408191967bb1caa4486e89)
- Rappi no tiene plugin: tiene un acuerdo para vender ChatGPT Go en 9 países, incluida Argentina — [Digital Trends ES](https://es.digitaltrends.com/computadoras/chatgpt-go-llega-a-latinoamerica-de-la-mano-de-rappi/)
- Ualá Bis tiene API de cobros online (links de pago, órdenes, reembolsos, webhooks) — [APIs.io](https://apis.io/providers/ual/) (directorio, no la documentación oficial)

**Finanzas abiertas en Argentina**
- El Decreto 353/2025 (mayo de 2025) creó el Sistema de Finanzas Abiertas, con el BCRA como autoridad junto a ARCA, CNV, SSN y ANSES. En 2026 **no se publicaron estándares técnicos ni cronograma** — [Fiskil](https://www.fiskil.com/es/open-finance-tracker/argentina)
- Un director del BCRA (Pedro Inchauspe, octubre de 2026) dijo que espera que se masifique hacia 2027 — [iProUP](https://www.iproup.com/finanzas/72141-open-finance-bcra-prepara-un-cambio-clave-para-el-credito-en-2027.amp)
- La API de Central de Deudores del BCRA existe desde septiembre de 2024 (fuente de 2024), y ya hay MCP de terceros: `mcp-bcra` en PyPI, `@codespar/mcp-bcra` y `mcp-datos-argentina` con 16 herramientas — [BCRA](https://www.bcra.gob.ar/noticias/nueva-api-del-bcra-que-mejora-la-accesibilidad-a-la-central-de-deudores/); [PyPI mcp-bcra](https://pypi.org/project/mcp-bcra/); [Claude Marketplaces, mcp-datos-argentina](https://claudemarketplaces.com/mcp/gonza28fq/mcp-datos-argentina)

**Protocolos agénticos y capa MCP en LatAm**
- UCP (Universal Commerce Protocol) es de Google, con Shopify, Etsy, Wayfair, Target y Walmart — [Shopify UCP](https://www.shopify.com/es/ucp); [Google Developers UCP](https://developers.google.com/pay/api/universal-commerce-protocol/overview?hl=es). No encontré evidencia de que Mercado Libre o Mercado Pago lo hayan adoptado.
- **CodeSpar, "MCP Dev LATAM":** un monorepo MIT de 109 a 127 servidores MCP (según la fuente) para Brasil, México, Argentina, Colombia, Chile y Perú. Incluye Mercado Pago, Andreani, AFIP, BCRA, Coordinadora, Shopee y bancos brasileños en alfa — [mcpservers.org](https://mcpservers.org/servers/codespar/mcp-dev-brasil); [Claude Marketplaces, codespar mcp-andreani](https://claudemarketplaces.com/mcp/io.github.codespar/mcp-andreani)

### Inferencias
- "Hacer el MCP de una API latinoamericana" **ya no es un hueco**: CodeSpar y varios proyectos sueltos lo cubren, y las empresas grandes (Tiendanube, Mercado Libre, MODO, Alegra) hacen el suyo. El valor se mueve a **productos verticales alojados, para el usuario final, en español**, con un flujo de trabajo completo (no solo el envoltorio de la API), listados en los directorios y cobrados afuera.
- Hay tráfico agéntico real en Argentina (Tiendanube pasó de US$0,23 M a más de US$2 M), pero convierte poco (3–5 %). Hay espacio en lo que pasa **después** del clic agéntico, pero Tiendanube lo está cubriendo para sus tiendas.
- Finanzas abiertas es una ventana de 2027 en adelante: hoy no hay API para construir, y ser proveedor regulado (TPP) le exigiría una estructura legal que una persona sola probablemente no tenga.

### Gaps
- No encontré el reparto de ingresos ni las comisiones de la tienda de apps de Tiendanube, ni la cantidad de apps por categoría.
- No encontré cambios de 2026 en la API de vendedores de Mercado Libre ni un programa de socios para agentes.
- No confirmé si Mercado Libre tiene su propio plugin en el directorio de ChatGPT.
- No pude abrir la nota de Pistacho App (403): faltan su precio y cobertura (si es solo Tiendanube o también WooCommerce u otras).

## 4. ¿Qué ya existe en español o para LatAm en esos catálogos? (mapa de saturación)

### Takeaway
Lo "obvio" ya está tomado o en camino: comercio electrónico (Tiendanube), viajes (Despegar), promos bancarias y compras (MODO), datos del BCRA, factura electrónica de ARCA a nivel desarrollador, conectores de Mercado Libre para vendedores y contabilidad de solo lectura (Alegra). Lo que no encontré listado son **flujos profesionales argentinos completos** (contador/monotributo con acciones, monitoreo del Boletín Oficial y la jurisprudencia) ni **verticales de bienes caros con financiación** (autos).

### Cited Findings
- **ARCA/AFIP, factura electrónica (MCP para desarrolladores, casi todos locales por stdio):**
  - `AMKRS3/keycae-mcp`: 10 herramientas; necesita delegar la factura electrónica en ARCA al representante KeyCAE; 0 estrellas — [GitHub](https://github.com/AMKRS3/keycae-mcp);
  - `@codespar/mcp-afip`: certificado, clave y CUIT por variables de entorno — [getdrio](https://www.getdrio.com/mcp/io-github-codespar-mcp-afip);
  - `ramide1/arca-mcp`: emite y consulta facturas y pide el CAE por WSFE — [Glama](https://images.glama.ai/mcp/servers/ramide1/arca-mcp);
  - ArcaMCP (Yoryoboy) — [Glama](https://glama.ai/mcp/servers/bb82w5lg7w);
  - **Velora**: MCP alojado; las notas de crédito y débito todavía solo funcionan en pruebas (sandbox) — [mcpservers.org](https://mcpservers.org/servers/crossi-dev/velora-mcp).
- **Monotributo:** "Monotributo GPT" de Tributo Simple es un asistente conversacional (un GPT), no un conector con datos — [Tributo Simple](https://tributosimple.com/inteligencia-artificial-y-chatgpt-como-estan-transformando-la-contabilidad/)
- **Contabilidad:** Alegra lanzó un servidor MCP para ChatGPT, Claude y Perplexity, **solo de lectura**; se agrega como conector personalizado — [Siempre al Día](https://siemprealdia.co/mexico/contabilidad/ia-conectada-al-software-contable/); [PR Newswire, Alegra México](https://www.prnewswire.com/mx/comunicados-de-prensa/alegra-revoluciona-la-gestion-contable-en-mexico-contadores-y-empresarios-ya-pueden-consultar-sus-finanzas-en-tiempo-real-usando-su-ia-favorita-302794164.html). No encontré conectores de Colppy ni Xubio.
- **Legal y normativa:**
  - InfoLeg MCP (`martindieser/infolegmcp`): busca normas, lee el texto vigente y el original y rastrea modificaciones; se conecta a Claude por SSE — [mcpservers.org](https://mcpservers.org/servers/martindieser/infolegmcp);
  - "Argentina Legal Law MCP": descripción vaga, depende de Azure Search y no se pudo comprobar qué indexa — [LobeHub](https://lobehub.com/es/mcp/your-org-argentina-legal-law-mcp-server);
  - **no encontré MCP del Boletín Oficial ni de jurisprudencia (SAIJ/PJN).**
- **Autos:** no encontré plugin de ChatGPT de Kavak ni de inventario de varios concesionarios en Argentina. Kavak usa agentes por WhatsApp desde 2023 — [WhatsApp Business, caso Kavak](https://whatsappbusiness.com/pt-br/resources/success-stories/kavak/). El agente de Mercado Libre Vehículos es de México y funciona dentro de la plataforma — [Mobile Time](https://mobiletime.la/noticias/21/08/2026/venta-de-autos-usados-en-mexico/)

### Inferencias
- El hueco no es "falta el conector": es "falta el producto terminado en español, que hace el trabajo de punta a punta, aprobado en el directorio y con alguien que responde". Los MCP para desarrolladores con 0 estrellas confirman que hay demanda técnica, pero no hay un producto de consumo.

### Gaps
- No pude navegar en vivo los directorios de ChatGPT (chatgpt.com/plugins) ni de Claude (claude.ai/directory) para filtrar por idioma o país. "No encontrado" significa "no apareció en buscadores ni en agregadores MCP (mcpservers.org, Glama, LobeHub, Claude Marketplaces)", no que se haya revisado el directorio entero.
- No revisé si elDial, Microjuris o La Ley (Thomson Reuters) ya tienen IA o conectores para jurisprudencia argentina: es la verificación pendiente más importante del candidato B.
- No tengo un número verificado de monotributistas ni de concesionarios en Argentina.

## 5. Huecos candidatos (3–5), con evidencia, búsqueda de competidores, confianza, viabilidad y durabilidad

### Takeaway
Los tres más defendibles para una persona con Claude Code son:
- **(A)** un "estudio contable en el asistente" para monotributistas y contadores argentinos, con acciones reales en ARCA, alojado y listado en ChatGPT y Claude;
- **(B)** un monitor normativo diario del Boletín Oficial, BCRA, ARCA y CNV que avisa qué cambió para cada rubro;
- **(C)** un plugin vertical de autos (inventario de concesionarios + financiación con CFT), cobrado por lead al concesionario.

Los tres se cobran fuera de la plataforma. La confianza de que nadie los cubre es **media** en A, **media-baja** en B y **media** en C.

### Cited Findings (base de cada candidato)
**A. ARCA/monotributo "de punta a punta" en ChatGPT y Claude**
- **Quién lo necesita:** monotributistas y estudios contables que hoy facturan y recategorizan a mano.
- **Lo que ya existe:**
  - muchos MCP de ARCA para desarrolladores, casi todos locales y con 0 estrellas — [keycae-mcp](https://github.com/AMKRS3/keycae-mcp); [codespar mcp-afip](https://www.getdrio.com/mcp/io-github-codespar-mcp-afip);
  - uno alojado (Velora), todavía incompleto — [Velora](https://mcpservers.org/servers/crossi-dev/velora-mcp);
  - Alegra, solo de lectura — [Siempre al Día](https://siemprealdia.co/mexico/contabilidad/ia-conectada-al-software-contable/);
  - Monotributo GPT, sin datos — [Tributo Simple](https://tributosimple.com/inteligencia-artificial-y-chatgpt-como-estan-transformando-la-contabilidad/).
- **Cómo cobrar:** ChatGPT exige que la suscripción se cobre afuera y deja que los suscriptores existentes usen lo que pagaron — [guía de plugins](https://developers.openai.com/apps-sdk/app-submission-guidelines). Claude no tiene un sistema de cobro — [BleepingComputer](https://bleepingcomputer.com/news/artificial-intelligence/anthropic-turns-claude-into-an-ai-marketplace-with-2-000-plus-plugins-and-connectors).
- **Datos de BCRA ya cubiertos:** Central de Deudores — [mcp-bcra](https://pypi.org/project/mcp-bcra/).
- **Búsquedas hechas:**
  - "github MCP server AFIP ARCA factura electrónica";
  - "Alegra Colppy Xubio ChatGPT app conector Claude contadores monotributo";
  - "MCP BCRA API central de deudores servidor".

**B. Monitor normativo argentino (Boletín Oficial + comunicaciones del BCRA + resoluciones de ARCA y CNV) como conector o plugin**
- **Lo que ya existe:** solo InfoLeg MCP (comunidad) y un "Legal Law MCP" que no se pudo verificar. No hay MCP del Boletín Oficial ni de jurisprudencia — [InfoLeg MCP](https://mcpservers.org/servers/martindieser/infolegmcp); [LobeHub](https://lobehub.com/es/mcp/your-org-argentina-legal-law-mcp-server).
- **Búsqueda hecha:** "MCP server Boletín Oficial Argentina InfoLEG normativa jurisprudencia".

**C. Plugin vertical de autos en ChatGPT (y en Gemini cuando abra): stock de concesionarios + financiación con CFT, con checkout o lead externo**
- **ChatGPT permite comercio de bienes físicos con checkout externo** — [guía de plugins](https://developers.openai.com/apps-sdk/app-submission-guidelines).
- **Ya hay marcas argentinas entrando al directorio:** MODO con Frávega — [El Economista](https://eleconomista.com.ar/negocios/modo-apuesta-sacar-ventaja-ia-alianza-fravega-lanza-una-funcion-usuarios-puedan-comprar-productos-chatgpt-n98390); Despegar — [plugin](https://chatgpt.com/plugins/plugin_asdk_app_6ac55c1644408191967bb1caa4486e89).
- **Hay evidencia de que un agente funciona en la venta de autos:** el de Mercado Libre Vehículos México atendió el 99 % de las conversaciones (dato del proveedor) — [Mobile Time](https://mobiletime.la/noticias/21/08/2026/venta-de-autos-usados-en-mexico/).
- **Lo que ya existe:** no encontré plugin de Kavak ni de varios concesionarios.
- **Búsqueda hecha:** "concesionarios autos app ChatGPT plugin inventario Latinoamérica Kavak 2026".

**D (más débil). Vendedores de Mercado Libre de Argentina: un asistente con acciones (preguntas, reclamos, precios)**
- **Ya está parcialmente cubierto:** AnythingMCP (genérico, alojado) — [AnythingMCP](https://anythingmcp.com/es/guides/connect-mercado-libre-to-claude); Kondado (pago, foco en Brasil) — [Kondado](https://kondado.io/blog/en/a/mercado-libre-in-chatgpt-and-claude-mcp); y los agentes propios de Mercado Libre en Brasil — [Ecosistema Startup](https://ecosistemastartup.com/mercado-libre-experience-2026-ia-y-datos-para-ecommerce/).

**E (de timing). Ser de los primeros con apps en español cuando Gemini Connected Apps se abra fuera de EE. UU.**
- Hoy está cerrado a desarrolladores que no son de EE. UU. y tiene más de 50 apps de terceros — [Android Authority](https://androidauthority.com/google-gemini-search-connected-apps-developer-platform-3729015); [9to5Google](https://9to5google.com/2026/10/28/gemini-google-connected-apps-platform).

### Inferencias (evaluación de cada candidato)
| Candidato | Confianza de que nadie lo cubre | Viable en 3–6 meses (1 persona) | Durabilidad / riesgo de plataforma | Modelo de USD 1.000/mes |
|---|---|---|---|---|
| A. ARCA/monotributo de punta a punta | **Media**: hay MCP crudos y Velora alojado, pero no apareció un producto de consumo listado | Alta en lo técnico (WSFE, padrón, delegación como KeyCAE). Lo difícil es el cumplimiento: certificados, responsabilidad si una factura sale mal y soporte | Media. Pueden entrar Xubio, Colppy o Alegra. Que ARCA cambie sus servicios web es un riesgo, pero también es lo que cuesta copiar. No depende de un solo asistente (sirve en ChatGPT, Claude y después Gemini) | Suscripción en tu dominio (ARS 10–20 mil por mes por monotributista, o un plan para estudios contables). Hacen falta unos 60–100 clientes pagos (inferencia, sin validar precio) |
| B. Monitor normativo | **Media-baja**: falta revisar a los proveedores de legaltech (elDial, Microjuris, La Ley) | Alta: fuentes públicas, scraping diario y resúmenes con IA | Media-alta: los datos son públicos, así que lo que defiende el negocio es la curaduría por rubro y la confianza. Poca dependencia de plataforma (también puede salir por email o WhatsApp de la empresa) | B2B a estudios y pymes reguladas (concesionarios, fintech, importadores) |
| C. Autos + CFT en ChatGPT | **Media**: no encontré competidores, pero Mercado Libre, que domina los avisos de autos, puede lanzar el suyo | Media: necesita stock de concesionarios (empezar con uno conocido) y aprobación del plugin, y no hay datos de descubrimiento en el directorio | Baja-media: depende del directorio de ChatGPT, con reglas que cambian (el paso de apps a plugins, Instant Checkout) | Cobro por lead o fijo mensual al concesionario, fuera de la plataforma |
| D. Vendedores de Mercado Libre | **Baja**: ya existen AnythingMCP, Kondado, Real Trends y Nubimetrics, y Mercado Libre hace sus propios agentes | Alta | Baja: depende de las API de Mercado Libre y de que Mercado Libre no lo haga | Suscripción |
| E. Gemini en español | No aplica (todavía no se puede entrar) | Preparar ahora el MCP en la nube es reutilizable para A, B o C | Depende de Google | Ninguno directo |

- **Recomendación como hipótesis:** A o B, porque son B2B, recurrentes, en español y con datos locales que un jugador global no va a priorizar, y porque funcionan en todos los asistentes a la vez. C aprovecha que el emprendedor ya tiene relación con un concesionario (Valparaiso Motors) para probarlo, pero tiene más riesgo de plataforma y un competidor obvio (Mercado Libre).
- **Estructura general:** construir **un solo servidor MCP remoto** (OAuth, alojado) y publicarlo en tres lugares (plugin de ChatGPT, directorio de Claude y Gemini cuando abra), con cobro y cuenta en el sitio propio.

### Gaps
- **Validación de demanda pendiente** en los tres candidatos: entrevistas con 10 contadores o monotributistas para A, con 5 estudios o pymes reguladas para B y con 3 concesionarios para C.
- **Verificar lo legal en A:** quién responde si una factura se emite mal y qué condiciones pone ARCA para delegar el servicio web a un tercero.
- No sabemos cuánto tráfico o cuántas instalaciones da un plugin nuevo en el directorio de ChatGPT o de Claude: no hay datos públicos.
- No investigué precios reales ni dispuestos a pagar en Argentina para ninguno de los candidatos.
