# Huecos en tiendas de apps de Latinoamérica: qué se vende en Shopify y falta en Tiendanube y Mercado Libre

**La respuesta corta.** Revisamos las 1.005 apps de las tiendas de Tiendanube (Argentina) y Nuvemshop (Brasil), una por una, y las comparamos con 48 categorías de la tienda de Shopify y con el ecosistema de herramientas para vendedores de Mercado Libre. El hueco más claro es el de **los videos y las publicaciones automáticas para redes, armados con el catálogo de la tienda**. En Shopify, esa categoría tiene apps con años de ventas: Outfy, desde 2015, con 583 reseñas y planes de USD 19 a 55 por mes; Minta, con 324; y Predis, con 183. En Tiendanube (Argentina, México, Colombia y Chile) no hay ninguna. En Nuvemshop (Brasil) hay una sola, SpellPost, que todavía no tiene reseñas y cobra desde R$ 149 por mes. Es justo donde tu fuerte, el video hecho con código a partir de datos, cuesta 100 veces menos que el video generado con IA, y donde el precio argentino (cuotas, transferencia, promos que cambian todas las semanas) le da ventaja a un producto local.

**El podio** (puntajes y estimaciones nuestros, explicados en las secciones 4 y 5):

| Puesto | Hueco | Producto (nombre provisorio) | Demanda probada en Shopify | Qué hay en Tiendanube / Nuvemshop | Ventaja del video hecho con código | Tiendas que pagan para USD 1.000 / 10.000 netos (escenario base) |
|---|---|---|---|---|---|---|
| **1** | Videos y publicaciones automáticas para redes | **Vidriera**: tu catálogo se publica solo en Instagram, Facebook y TikTok, con precio y cuotas al día | Outfy 583 reseñas, Minta 324, Predis 183 | AR/MX: nada. BR: SpellPost (0 reseñas, R$ 149–697,90) | **Máxima** | ≈ 67 / ≈ 640 |
| 2 | Catálogo para anuncios con creatividades | **Catálogo con Cuotas**: feeds para Meta, Google, TikTok y ChatGPT, con imágenes y videos que muestran cuotas y precio por transferencia | Simprosys 4.976 reseñas; Socioh cobra USD 250–5.000 por mes | Feed XML (114 reseñas, R$ 49); Feedom y otras 4 apps con 0 | Alta, pero Meta regala overlays de precio | ≈ 78 / ≈ 745 |
| 3 | Mayorista y revendedoras | **Kit Revendedora**: cada revendedora recibe todas las semanas videos e imágenes con *su* precio y *su* WhatsApp | Apps B2B de 700 a 1.200 reseñas | Tablas de precios nativas; apps de contenido para revendedoras: ninguna con reseñas | Alta (personalización masiva) | ≈ 26 / ≈ 245 |

**La recomendación (sección 6): Vidriera.** De las tres, es la única que junta todo lo que pediste. La demanda está probada hace diez años en otro mercado. En la región no tiene competencia con tracción. No te suma horas por cliente: se instala sola desde la tienda de apps. La pagan comercios formales que ya pagan Tiendanube. Además, el motor que vas a construir (producto + precio + plantilla → video) es el mismo que necesitan los productos 2 y 3, que quedan como segundo y tercer paso, no en paralelo.

**Lo que no está probado.** Ningún comercio de Tiendanube pagó todavía por esto. SpellPost muestra que alguien más vio el hueco en Brasil, pero sin reseñas no sabemos si vende. Tiendanube ya tiene una IA propia, Lumi, que hace imágenes y banners, y puede sumar la publicación en redes. Para llegar a USD 10.000 hacen falta unas 640 tiendas pagando, lo que te pone entre las 20 apps más usadas de Tiendanube. Por eso el plan arranca con un experimento de tres semanas y con condiciones claras para abandonarlo.

**Cómo leer este informe.** Todo lo que tiene enlace es un dato con fuente. Lo que dice "est." es una estimación nuestra, con la cuenta a la vista. Las reseñas de una tienda de apps no son instalaciones: en Tiendanube encontramos que hay más o menos **una reseña cada 2 a 9 tiendas que usan la app** (sección 1.2). Fecha de la investigación: 22/11/2026. Tipos de cambio: **ARS 1.560 por dólar**, el mismo valor de los informes anteriores ([Rava](https://www.rava.com/cotizaciones/historico/dolar-mep/2026/11/11/)), y **R$ 5,87 por dólar**, el cierre del 19/11/2026 ([O Povo](https://mais.opovo.com.br/jornal/economia/2026/11/19/dolar-tem-5-alta-sobe-145-no-dia-e-atinge-rs-586.html)).

**Palabras que usamos.**
- **Tienda de apps:** el catálogo de aplicaciones que el comerciante instala desde su panel (la de Tiendanube, la de Nuvemshop o la de Shopify).
- **Arbitraje de tiendas de apps:** copiar una categoría que ya funciona en una tienda grande (Shopify) en una tienda donde todavía no existe o es débil.
- **Feed:** el archivo con todos los productos, precios y stock que se le manda a Google, Meta, TikTok o ChatGPT para los anuncios.
- **Homologación:** la revisión que hace Tiendanube antes de publicar una app.
- **NubeSDK:** el kit obligatorio de Tiendanube para que una app muestre cosas en la tienda o en el checkout.
- **Costo marginal:** lo que cuesta atender a un cliente más.
- **Aporte:** lo que queda de cada cliente por mes después de la comisión de cobro y del costo de atenderlo.
- **Bajas (churn):** porcentaje de clientes que se van cada mes.

---

## 1. Tiendanube y Nuvemshop: el mapa

### 1.1 Tamaño y categorías

**Tabla 1. Las dos tiendas de apps, contadas el 22/11/2026** (recorrimos todas las páginas de cada categoría; ver sección 7)

| | Tiendanube (Argentina, en español) | Nuvemshop (Brasil, en portugués) |
|---|---|---|
| Apps publicadas | **707** | **700** |
| Apps distintas entre las dos | **1.005** (402 están en las dos) | |
| Categorías (apps en cada una) | Recursos extras 201 · Marketing 195 · Gestión 72 · Envíos 71 · Comunicación 57 · Estadísticas 42 · Seguridad 26 · Canales de venta 20 · Pagos 15 · Dropshipping 8 | Marketing 244 · Recursos extras 188 · Comunicação 59 · Gestão 49 · Logística 43 · Segurança 33 · Estatísticas 27 · Dropshipping 23 · Canais de vendas 19 · Pagamentos 15 |
| Cómo cobran | "Compras en la app" (el desarrollador cobra por su cuenta) 525 (74 %) · "Pago" (cobra Tiendanube) 115 (16 %) · Gratis 67 (9 %) | Compras no app 517 · Pago 119 · Grátis 64 |
| Apps con 100 reseñas o más | 48 | 58 |
| Apps con 0 reseñas | 246 (35 %) | 231 (33 %) |

Fuentes: [Tienda de Aplicaciones de Tiendanube](https://www.tiendanube.com/tienda-aplicaciones-nube) y sus categorías (por ejemplo, [Marketing](https://www.tiendanube.com/tienda-aplicaciones-nube/categorias/marketing)); [Loja de Aplicativos de Nuvemshop](https://www.nuvemshop.com.br/loja-aplicativos-nuvem).

- **Tiendas activas:** 209.254 tiendas, según Store Leads (13/11/2026). Brasil tiene 127.271 (61 %), Argentina 59.214 (28 %), México 6.974, Colombia 2.334 y Chile 1.836. Crecieron 32 % en un año ([Store Leads](https://storeleads.app/reports/tiendanube)). Tiendanube dice "más de 180.000" ([Tiendanube](https://www.tiendanube.com/tienda-aplicaciones-nube)). Shopify tiene **3.298.869** tiendas, unas 16 veces más ([Store Leads](https://storeleads.app/reports/shopify)).
- **Tecnologías instaladas en las tiendas de Tiendanube:** el píxel de Facebook está en 106.485, el de Google Ads en 60.689 y el de TikTok en 23.335 ([Store Leads](https://storeleads.app/reports/tiendanube)). Es decir, la mitad de las tiendas ya hace (o hizo) publicidad en Meta.
- **Subcategorías que Tiendanube prepara:** el código de las páginas trae 38 subcategorías que todavía no se muestran, entre ellas "Turnos y reservas", "B2B y mayorista", "Redes sociales y social commerce", "Google y comparadores de precios" e "Internacionalización" (visto en el código de [la ficha de Shoptic](https://www.tiendanube.com/tienda-aplicaciones-nube/shoptic)). Además, se puede ordenar por "Recomendados" o "Más evaluados".

### 1.2 Las apps con más reseñas, y qué significa una reseña

**Tabla 2. Las 20 apps con más reseñas en Tiendanube y Nuvemshop** (las reseñas de una app publicada en los dos países se suman en una sola cifra)

| Reseñas | App | País | Qué hace |
|---|---|---|---|
| 4.475 | AliExpress by Dropi | AR, BR | Dropshipping |
| 1.655 | Drop Nacional by Dropi | BR | Dropshipping nacional |
| 1.013 | WhatsApp Marketing | AR, BR | Carritos y campañas por WhatsApp |
| 729 | JivoChat | BR | Chat multicanal |
| 674 | Marketplaces by HubNoov | BR | Shopee, Magalu, Mercado Livre |
| 634 | Manda Bem | BR | Envíos |
| 572 | Melhor Envio | BR | Envíos |
| 514 | Cashing | AR, BR | Reseñas, kits, cashback |
| 498 | Appmax | BR | Pagos |
| 472 | Mercado Pago | AR, BR | Pagos |
| 471 | Bling | BR | ERP |
| 412 | Lily Reviews | AR, BR | Reseñas con fotos y videos |
| 401 | Super Frete | BR | Envíos |
| 393 | Correo Argentino | AR | Envíos |
| 342 | Smartbis | AR, BR | Cashback y fidelización |
| 341 | Marketing Nube (ex Perfit) | AR, BR | Email marketing (es de Tiendanube) |
| 332 | Pinterest | AR, BR | Catálogo en Pinterest |
| 315 | FForder by Dropi | AR, BR | Dropshipping |
| 314 | Andreani | AR | Envíos |
| 304 | iCortex | AR, BR | Recupero de pedidos |

Lo que más se usa es la infraestructura (envíos, pagos, ERP, dropshipping). En marketing, lo que más se usa son WhatsApp, reseñas, cashback y kits.

**¿Cuántas tiendas hay detrás de una reseña?** Tiendanube no publica instalaciones, pero tres apps dan su número en la ficha:
- Llegué (aviso de reposición): 109 reseñas y "más de 1.000 tiendas lo usan" ([ficha](https://www.tiendanube.com/tienda-aplicaciones-nube/cheguei-avise-me));
- CrossUp (recomendador): 265 reseñas y "más de 1.000 tiendas ya instalaron" ([ficha](https://www.tiendanube.com/tienda-aplicaciones-nube/crossup-flowy));
- Feed XML: 114 reseñas y "más de 200 tiendas conectadas" ([ficha](https://www.tiendanube.com/tienda-aplicaciones-nube/feed-xml)).

De ahí sale la regla práctica de **una reseña cada 2 a 9 tiendas** (est., con solo tres casos).

### 1.3 Lo que pagan hoy los comercios (disposición a pagar)

**Tabla 3. Precios publicados de apps pagas de Tiendanube** (ARS por mes, sin IVA salvo aclaración)

| App | Para qué | Precio | En USD | Reseñas |
|---|---|---|---|---|
| Lily Reviews | Reseñas | ARS 17.916 a 166.718 según pedidos (fijado en reales) | 11,5–107 | 412 |
| CrossUp | Recomendaciones con IA | ARS 49.999 + 7,49 % de lo extra vendido, hasta ARS 124.999 + 1,29 % | 32–80 + % | 265 |
| Notificaciones de Stock / Trusty | Aviso de reposición / reseñas | ARS 13.990 a 199.990 | 9–128 | 40 / 96 |
| Precios cuotas y promos | Mostrar cuotas, transferencia y promos bancarias en la tienda | ARS 34.990 | 22,4 | 177 |
| Cashback & Loyalty | Fidelización | ARS 34.990 | 22,4 | 111 |
| Shop the Look | Looks | ARS 49.990 | 32 | 124 |
| Feed XML | Feed para Google y Meta | R$ 49 (ARS 13.009,71) | 8,3 | 114 |
| Mayorista Pro | Precios para revendedoras | ARS 19.990 a 34.990 | 12,8–22,4 | 0 |
| Atacarejo | Precio por cantidad | R$ 69,99 | 11,9 | 0 |
| SpellPost (Brasil) | Publicaciones automáticas en redes | R$ 149 / 279,90 / 697,90 | 25 / 48 / 119 | 0 |

Fuentes: fichas de [Lily Reviews](https://www.tiendanube.com/tienda-aplicaciones-nube/lily-reviews), [CrossUp](https://www.tiendanube.com/tienda-aplicaciones-nube/crossup-flowy), [Notificaciones de Stock](https://www.tiendanube.com/tienda-aplicaciones-nube/notificaciones-de-stock), [Precios cuotas y promos](https://www.tiendanube.com/tienda-aplicaciones-nube/multipricing), [Cashback & Loyalty](https://www.tiendanube.com/tienda-aplicaciones-nube/loyalty-cashback), [Shop the Look](https://www.tiendanube.com/tienda-aplicaciones-nube/shop-the-look), [Feed XML](https://www.tiendanube.com/tienda-aplicaciones-nube/feed-xml), [Mayorista Pro](https://www.tiendanube.com/tienda-aplicaciones-nube/mayorista-pro), [Atacarejo](https://www.tiendanube.com/tienda-aplicaciones-nube/next-atacarejo), [SpellPost](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/spellpost-oficial).

- **Para comparar:** Tiendanube cobra en la Argentina ARS 27.999 por mes el plan Esencial, ARS 79.999 el Impulso ("el más elegido") y ARS 244.999 el Escala (USD 18, 51 y 157) ([Tiendanube, planes](https://www.tiendanube.com/planes-y-precios)).
- **Lo que pagan los vendedores de Mercado Libre:** a Real Trends le pagan de ARS 61.000 a 245.000 por mes más IVA (USD 39–157) ([Real Trends](https://www.real-trends.com/ar/precios)).
- **Conclusión:** una app que cobra entre USD 15 y 35 por mes está en el rango normal de lo que una tienda argentina ya paga por una sola función. Una app que pasa de USD 50 tiene que mostrar ventas atribuidas, como hace CrossUp.

### 1.4 Cómo cobra el desarrollador

- **Dos caminos.** La forma de cobro se elige por país en el Portal de Socios. Las opciones son tres:
  - "Gratuito", que incluye el caso en que **el socio cobra por fuera de la plataforma**;
  - "Valor único";
  - "Valor mensual" con la Billing API de Tiendanube.

  "Publicar una app no genera automáticamente una comisión sobre el volumen de ventas de la tienda" ([Tiendanube Devs, Precios y cobro](https://tiendanube.dev/apps/publish/pricing-billing), act. 07/10/2026).
- **Si cobra Tiendanube:**
  - el cargo se suma a la factura del plan del comerciante ([Ayuda Tiendanube](https://ayuda.tiendanube.com/es_AR/134373-pagos-a-tiendanube/como-pagar-las-aplicaciones-instaladas-en-mi-tiendanube));
  - el reparto es **70 % para el desarrollador y 30 % para Tiendanube**;
  - Tiendanube **paga en pesos argentinos "independientemente de dónde se haya realizado la venta"**. Con factura A se transfiere el 70 % más el impuesto; con factura C, el 70 % ([Reglamento, versión Colombia](https://www.tiendanube.com/co/reglamento-tiendas-nube)). La página de ayuda que lo detalla para la Argentina pide iniciar sesión; los resultados de búsqueda repiten el mismo 70 % con factura A más 21 % de IVA. **Verificar** con socios@tiendanube.com.
- **La Billing API** permite planes, cambios de plan y **cobros adicionales por uso**, por ejemplo créditos de video. El ciclo se alinea con el día 16 de cada mes ([Billing API](https://tiendanube.dev/api/resources/2025-03/billing.md)).
- **Lo que hace la mayoría:** el 74 % de las apps argentinas cobra por su cuenta ("Compras en la app"), es decir, se queda con el 100 % y paga solo la comisión del medio de pago.
- **Qué conviene (est.):**
  - en la Argentina, cobrar por fuera con Mercado Pago;
  - en Brasil, usar la Billing API de Tiendanube, que cobra en reales y te paga en pesos, para no tener que abrir una empresa en Brasil para cobrar.

  Ese 30 % es el precio de no tener empresa allá. Verificar el tipo de cambio que usa Tiendanube para pagar.

### 1.5 Qué deja hacer la API, y sus límites

**Tabla 4. Capacidades técnicas que importan para estos productos**

| Tema | Qué se puede | Límite o detalle | Fuente |
|---|---|---|---|
| Productos | Leer y escribir productos, variantes, precios, stock, categorías, etiquetas y campos SEO (título hasta 70 caracteres y descripción hasta 320). Subir imágenes por URL | El campo `video_url` acepta solo enlaces https (por ejemplo, YouTube). Los videos nativos (`videos`) aparecen como lista de solo lectura, "vacía para tiendas sin la funcionalidad" | [Product](https://tiendanube.dev/api/resources/2025-03/product.md), [Product Image](https://tiendanube.dev/api/resources/2025-03/product-image.md) |
| Pedidos y clientes | Leer pedidos para atribuir ventas | Las estadísticas de sesiones del panel no se exponen | [FAQ de la API](https://tiendanube.dev/api/faq.md) |
| Webhooks | Aviso en JSON cuando cambia un producto, entra un pedido o se desinstala la app | Hay tres webhooks de privacidad obligatorios | [Webhook](https://tiendanube.dev/api/resources/2025-03/webhook.md) |
| Límite de uso | 40 pedidos de golpe y 2 por segundo, por tienda y por app | ×10 en los planes Next y Evolución; hasta 200 ítems por página | [Control de uso](https://tiendanube.dev/apps/erp-guide/api-usage.md) |
| Mostrar cosas en la tienda | Hay que usar **NubeSDK**, que corre en un Web Worker y dibuja en "slots" | No tiene acceso al DOM ni slot en el `<head>` (no se puede inyectar JSON-LD) y no corre GTM. Cronograma: desde el 05/06/2026 la homologación exige NubeSDK; el 30/09/2026 salieron de la tienda las apps que no migraron; desde el 30/10/2026 se desinstalan de a poco | [FAQ NubeSDK](https://tiendanube.dev/apps/nube-sdk/faq.md) |
| Video en la tienda | Componentes `Video` y `VideoStories` (tarjeta vertical 9:16 con lista de videos MP4/HLS) | Las URL tienen que ser https absolutas | [VideoStories](https://tiendanube.dev/apps/nube-sdk/components/video-stories.md) |
| Precios mayoristas | API de tablas de precios | La función es nativa desde el plan Impulso | [Price Tables](https://tiendanube.dev/llms.txt) |
| IA y agentes | Admin MCP, Storefront MCP, documentación en `llms.txt` y en Markdown | | [Tiendanube Devs](https://tiendanube.dev/llms.txt) |
| Storefront API | API pública para tiendas *headless*: búsqueda, carrito y checkout | Versión 2026-11 | [Storefront API](https://tiendanube.dev/storefront-api/getting-started.md) |

Para Vidriera alcanza con la Admin API (leer catálogo y pedidos) y los webhooks de producto. No hace falta tocar la tienda; si se quiere mostrar los videos en la ficha, se usa `VideoStories`.

### 1.6 Cómo se publica una app (homologación)

1. En el Portal de Socios, habilitás "Tienda de Aplicaciones" y pedís la homologación ([Visión general](https://tiendanube.dev/apps/publish/homologation/overview.md)).
2. Mandás:
   - un diagrama de secuencia;
   - un **video demo** con la instalación desde `tiendanube.com/apps/(app_id)/authorize`, el registro, la reinstalación y lo que pasa al dar de baja la app;
   - una cuenta demo;
   - la prueba de uso de NubeSDK si la app inyecta scripts ([FAQ de publicación](https://tiendanube.dev/apps/publish/faq.md)).
3. **El equipo tiene hasta 30 días hábiles para responder.** Si no contestás en 5 días cuando te piden algo, la app sale de la fila ([Directrices](https://tiendanube.dev/apps/publish/guidelines.md)).
4. Mientras está "En aprobación", el precio y los países quedan bloqueados.
5. **Las apps privadas ("Para tus clientes") no pasan por homologación** ([FAQ](https://tiendanube.dev/apps/publish/faq.md)). Eso permite hacer un piloto con comercios reales sin esperar 30 días hábiles.
6. No se permiten apps que no usen las APIs de Tiendanube ni que esquiven el checkout ([Directrices](https://tiendanube.dev/apps/publish/guidelines.md)).

### 1.7 ¿Tiendanube promociona apps? ¿Compite con ellas?

- **Promoción (visto el 22/11/2026):**
  - la portada tiene un carrusel destacado (ese día: Rapiboy, CaaS, Loybox, Releasit, Alerti, Odoo by Devoo, Dux) y las secciones "Más populares" y "Aplicaciones destacadas";
  - hay sellos de calidad ("Integrado al panel", "Compatible con Multi CD"), un filtro "Exclusivo Evolución" y una app que se presenta como "oficial y certificada por Tiendanube" (Gifty);
  - el programa de socios tecnológicos promete "mostrarte a cientos de potenciales clientes" y reportes de uso, pero no dice cómo se entra al carrusel ni si se paga ([Socios tecnológicos](https://www.tiendanube.com/mx/socios/tecnologicos)).

  **No encontramos una regla pública para salir destacado.**
- **Competencia de la propia plataforma: es fuerte y va rápido.** Solo en 2026:
  - **suscripciones nativas** (solo con Pago Nube y un producto por carrito) ([Ayuda](https://ayuda.tiendanube.com/es_AR/ventas/como-vender-productos-por-suscripcion-en-tiendanube));
  - **tablas de precios mayoristas** (1 en Impulso, 3 en Escala, ilimitadas en Evolución) ([Tiendanube](https://www.tiendanube.com/soluciones/ventas-mayoristas));
  - **Lumi**, la IA propia, que hace descripciones masivas, texto alternativo y, con **Lumi Studio**, "imágenes de producto o banners". Entre los países de habla hispana, por ahora está solo en México y la Argentina ([Blog de Tiendanube](https://www.tiendanube.com/blog/lumi/)); en Brasil también existe ([Nuvemshop IA](https://www.nuvemshop.com.br/ia));
  - quitar fondos con IA en beta ([Ayuda](https://ayuda.tiendanube.com/es_AR/fotos-del-producto/editar-imagenes-para-tus-productos-tiendanube-usando-inteligencia-artificial));
  - **Nuvem Chat**, un agente que atiende WhatsApp e Instagram ([Nuvemshop IA](https://www.nuvemshop.com.br/ia)).
  - En septiembre de 2026, Nuvemshop lanzó descuentos progresivos y regalos en el carrito **"sem precisar de app externo"**, además de visibilidad por tabla mayorista y la integración con ChatGPT Ads, que usa los eventos de compra (la página no menciona el catálogo) ([Novidades setembro 2026](https://www.nuvemshop.com.br/novidades-setembro-2026)).

  **Lección:** todo lo que sea un widget simple o una función de catálogo termina siendo nativo. Lo que dura es lo que necesita un motor propio caro de copiar (el render de video), datos de muchas tiendas o integraciones con terceros.

---

## 2. Mercado Libre: un ecosistema cerrado y ya ocupado

**Tabla 5. Herramientas para vendedores de Mercado Libre**

| Qué resuelve | Quién | Precio y tamaño | Fuente |
|---|---|---|---|
| Gestión, respuestas con IA, control de calidad de fotos, precios automáticos y competencia | Real Trends | ARS 61.000 a 245.000 por mes + IVA según ventas; "+25.000 vendedores" | [Real Trends](https://www.real-trends.com/ar/precios) |
| Inteligencia de mercado y competencia, con conector MCP para chatear con la IA | Nubimetrics | "Consultar precio". La prueba exige 10 ventas y USD 300 en 90 días | [Nubimetrics](https://www.nubimetrics.com/precios) |
| Sincronizar con Tiendanube y multicanal | Astroselling (167 reseñas en Tiendanube), HubNoov (674 en Nuvemshop), Base, AnyMarket, Producteca, UpSeller, Bling, Olist | — | Tienda de apps de Tiendanube y Nuvemshop |
| Videos cortos en las publicaciones | **Mercado Libre Clips, nativo y gratis**, con un asistente de IA "gratuito e ilimitado" que arma el clip con voz, subtítulos y música (la voz, con acento mexicano) | Videos verticales de 10 a 61 s | [Merca2.0](https://www.merca20.com/?p=12519915); [Marketing4eCommerce](https://marketing4ecommerce.mx/mercado-clips-ventas-con-inteligencia-artificial/); [Mercado Libre Developers, Clips](https://global-selling.mercadolibre.com/devsite/working-with-clips) |

- **No hay tienda de apps que distribuya.** Para entrar al Developer Partner Program, los vendedores que usan tu herramienta tienen que facturar **USD 1.500.000 por mes en la Argentina**, 2.500.000 en Brasil y 1.000.000 en México. Además:
  - hay que aprobar una evaluación de seguridad con 65 % o más;
  - las postulaciones se revisan cada tres meses;
  - los cambios obligatorios se implementan en 15 días ([Developer Partner Program](https://developers.mercadolibre.com.ar/es_ar/developer-partner-program), act. 14/10/2026).

  Una app nueva no tiene cómo llegar a los vendedores desde adentro de Mercado Libre.
- **Clips por API:** la documentación oficial permite subir clips **solo a ítems de Global Selling (CBT)**, con un tope de moderación de 1.000 clips por día ([Working with Clips](https://global-selling.mercadolibre.com/devsite/working-with-clips), act. 09/06/2026). Para el vendedor local, la carga se hace a mano desde el centro de vendedores ([UpSeller, 24/03/2026](https://upseller.com/es/help-doc-article-411)).
- **Conclusión:** en Mercado Libre, lo útil (analítica, respuestas con IA, precios, sincronización) ya está tomado, y la capa de video la regala la plataforma. **Mercado Libre sirve como canal de exportación** (bajar el video y subirlo como Clip), **no como lugar donde vender la app.**

---

## 3. Shopify: dónde está la demanda probada

Recorrimos las 48 categorías de último nivel que importan para este análisis. De cada una, tomamos la cantidad de apps y las que tienen más reseñas en la primera página. Después abrimos unas 70 fichas.

**Tabla 6. Categorías de Shopify con tracción** (reseñas al 22/11/2026)

| Categoría | Apps en la categoría | Líderes (reseñas) | Precios típicos |
|---|---|---|---|
| Reseñas de producto | 499 | Judge.me 50.591 · Loox 10.166 · Yotpo 4.625 · Okendo 1.456 · Junip 1.178 | Gratis a USD 299 |
| Bundles y venta cruzada | 548 / 1.259 | Kaching Bundles 6.833 · BOGOS 4.785 · Fast Bundles 3.695 · Pumper 3.674 | USD 15–60 |
| Aviso de reposición y preventa | 343 | Kbite 4.473 · Notify Me! 4.053 · STOQ 3.973 · Timesact 2.144 | USD 5–19 |
| Suscripciones | 169 | Appstle 9.332 · Seal 3.188 · Recharge 3.162 | USD 10–500 |
| Fidelización | 480 | Smile 4.698 · BON 2.005 · Joy 1.784 | USD 15–199 |
| SEO | 1.265 | Booster 5.480 · Avada 4.689 · SEOLab 2.977 · Tapita 2.637 | USD 39–69 |
| Blog y contenido con IA (incluye "AEO/GEO") | 268 | SEOWILL 1.807 · StoreSEO 775 · Tapita AEO/GEO 494 | |
| Feeds de catálogo | 328 | Simprosys 4.976 · Multifeed 1.125 · Mulwi 629 · DataFeedWatch 343 · Product Feed for ChatGPT Ads 16 (salió el 09/07/2026) | USD 5–50 |
| Creatividades dinámicas de catálogo | — | Socioh 67 · CustomPix 15 · Marpipe 7 · Feedom 3 | **Socioh USD 250–5.000**, CustomPix USD 19–89 |
| **Videos y publicaciones automáticas desde el catálogo** | dentro de "Video" (336) | **Outfy 583 (desde 2015) · Minta 324 (desde 2020) · Predis 183 (desde 2022)** | **USD 5–79** |
| Video comprable y UGC | 336 | Whatmore 407 · Moast 356 · Sauce 345 · ReelUp 294 · Tolstoy 289 · Videowise 255 | USD 9–200 |
| Traducción y moneda | 211 | Transcy 2.553 · Translate & Adapt 1.378 | |
| Tablas de talles | 280 | Kiwi 1.246 · MP Size Chart 878 | USD 8–145 |
| Opciones de producto | 599 | Globo 5.331 · Easify 3.275 | |
| Chat y atención con IA | 1.119 / 301 | Shopify Inbox 5.828 · Chatty 1.892 · Tidio 1.358 · Gorgias 709 | |
| Mayorista y B2B | 236 / 384 | BSS B2B 1.204 · Wholesale Pricing 761 · QS Request a Quote 717 · B2B Wholesale Hub 701 | USD 9–99 |
| Afiliados | 295 | UpPromote 3.949 · Referral Candy 1.486 · BixGrow 1.337 | |
| Cambios y devoluciones | 296 | AfterShip Returns 1.547 · Redo 883 · Return Prime 777 | |
| Turnos y reservas | 129 | Cowlendar 2.271 · Appointly 1.693 · Appointo 957 | |
| Descripciones con IA | 550 | AI Product Description 527 · AI‑ChatGPT Description 374 | |
| **Fotos de producto con IA** | 430 | Reframe 7 · Bria 4 · ProdShot 2 · el resto, 0 a 1 | USD 15–249 |
| **Videos generados con IA desde fotos** | — | Vidify 12 · OmniGen 2 · AnimateImage 1 · ShowcaseAI 1 · VidsyAI, Vigenfy, Reeporter, VEOit, Adify: 0 | USD 5–199 |

Fuentes: categorías de la tienda de Shopify, por ejemplo [reseñas](https://apps.shopify.com/categories/marketing-and-conversion-social-trust-product-reviews/all), [feeds](https://apps.shopify.com/categories/sales-channels-selling-online-product-feeds/all), [video](https://apps.shopify.com/categories/store-design-images-and-media-video-and-livestream/all), [aviso de reposición](https://apps.shopify.com/categories/marketing-and-conversion-upsell-and-bundles-stock-alerts/all), [cotizaciones y mayorista](https://apps.shopify.com/categories/selling-products-pricing-pricing-quotes/all); fichas de [Outfy](https://apps.shopify.com/outfy), [Minta](https://apps.shopify.com/minta), [Predis](https://apps.shopify.com/predisai), [Socioh](https://apps.shopify.com/orangetwig), [CustomPix](https://apps.shopify.com/custompix-product-catalog), [Marpipe](https://apps.shopify.com/marpipe), [Vidify](https://apps.shopify.com/vidify), [Reframe](https://apps.shopify.com/reframe), [Product Feed for ChatGPT Ads](https://apps.shopify.com/product-feed-for-chatgpt-ads).

**Tres cosas que salen de esta tabla:**
1. **Lo "de IA" no es lo que más vende.** Las apps que generan fotos o videos con IA tienen casi 0 reseñas, tanto en Shopify como en Tiendanube. Lo que tiene años de tracción son funciones aburridas y bien resueltas: reseñas, bundles, avisos de reposición, suscripciones, SEO y feeds.
2. **Hay una excepción con video que sí vende:** los productos que **toman el catálogo, arman videos y publicaciones con plantillas, y los publican solos** en las redes. Outfy lleva diez años y cobra de USD 19 a 55. Minta, de USD 5 a 55. Predis, de USD 32 a 79, y está en español y portugués. Las fichas de Outfy y Predis muestran el sello "Built for Shopify". **Ninguno de los tres se conecta con Tiendanube** ([soporte de Outfy](https://www.outfy.com/help/docs/supported-e-commerce-platforms/); búsqueda sobre Predis en la sección 7).
3. **Las creatividades de catálogo** (la foto del producto con el precio y la promo encima) tienen pocas reseñas pero precios altos: Socioh cobra de USD 250 a 5.000 por mes. Es una señal de plata por cliente, no de volumen.

---

## 4. El análisis de huecos

### 4.1 Cómo medimos

Para cada categoría sumamos las reseñas de las 5 apps líderes de Tiendanube y Nuvemshop y las dividimos por las de las 5 líderes de Shopify. En promedio, Tiendanube tiene el **2,57 %** de las reseñas de Shopify. El **índice de cobertura** compara cada categoría con ese promedio:
- **1** quiere decir "tan cubierta como el promedio";
- **0,1** quiere decir "diez veces menos cubierta de lo normal".

Es una estimación nuestra, con sus problemas: en Shopify se piden más reseñas y las reseñas no son instalaciones. Sirve para ordenar, no para medir.

**Tabla 7. Categoría por categoría** (TN = Tiendanube + Nuvemshop; ML = Mercado Libre)

| Categoría | Índice | Qué hay en Tiendanube / Nuvemshop | ¿Es nativo? | Mercado Libre | ¿El video hecho con código da ventaja? | Veredicto |
|---|---|---|---|---|---|---|
| **Videos y publicaciones automáticas desde el catálogo** | **≈ 0** | AR/MX: ninguna. BR: SpellPost (0 reseñas, R$ 149+), Glowketing (0, "copiloto" de estrategia, no publica solo). Shoptic (24) y Atlas (7) generan piezas sueltas, pero no las publican | No (Lumi Studio hace imágenes y banners, no publica) | Clips con IA gratis, solo dentro de Mercado Libre | **Sí, es el núcleo** | **Hueco 1** |
| Mayorista / B2B | 0,08 | Tabla de Precios (5), Solicitar Cotización (2), Catálogo PDF (1), Mayorista Pro (0), Atacarejo (0) | **Sí, los precios** (tablas desde Impulso, visibilidad por grupo desde sept. 2026) | — | Sí, para el contenido de cada revendedora | **Hueco 3** (el contenido, no los precios) |
| Suscripciones | 0,00 | Ninguna app | **Sí, desde 2026** | — | No | La plataforma ya la hizo |
| Traducción y moneda | 0,01 | Casi nada | Parcial | — | No | Poca demanda en tiendas de un solo país |
| SEO y visibilidad en IA | 0,12 | 14 apps, 57 reseñas en total. Siete nuevas con 0 en 2026 (SEO by Sacu "visibilidad en ChatGPT", Katal, SEOpilot, Dondo, Ascendly, CreatvIA, Trustify) | Parcial (Lumi hace descripciones y alt masivos) | ML bloquea a los bots de IA en su [robots.txt](https://www.mercadolibre.com.ar/robots.txt) | No (la IA sí) | Hueco con límite técnico (no hay `<head>` para JSON-LD) y riesgo nativo |
| Descripciones con IA | 0,31 | Casi nada | **Sí (Lumi)** | — | No | Nativo |
| Opciones de producto | 0,52 | Campo Personalizado 129, Personalize 91 | Sí (campos personalizados) | — | No | Cubierta |
| Reseñas con fotos y video | 0,60 | 42 apps: Lily 412, Google Reviews 214, AVALA 199 (**ya tiene "Review Reels": tus mejores reseñas en videos para Instagram y TikTok**), Revie 122 (por WhatsApp) | No | Las reseñas son de ML; Lily las importa | El giro de video ya existe | **Parecía hueco y no es** |
| Feeds de catálogo | 0,65 | Feed XML 114 (R$ 49); Feed Vivo, Feedr, Feedom, Feed PRO: 0 | Canales nativos con Google, Meta y TikTok. A Google le llega solo el precio original y le rechazan productos ([Ayuda](https://ayuda.tiendanube.com/123352-google-shopping/como-configurar-mis-productos-para-los-canales-de-venta)). En ChatGPT Ads, el catálogo se sube a mano ([Ayuda](https://ayuda.tiendanube.com/es_CO/chatgpt-ads/que-es-chatgpt-ads-y-como-funciona-con-tiendanube)) | — | Sí, si suma creatividades | **Hueco 2** (feed + creatividades) |
| Creatividades de catálogo | ≈ 0 | Feedom (0) | Meta regala overlays de precio y descuento | — | Sí | Parte del hueco 2 |
| Pop-ups y contadores | 0,83 | Popup Timer 227, Counti 94 | Parcial | — | No | Cubierta |
| Cambios y devoluciones | 0,84 | Boris 51, Undo 43 | No | — | No | A medias |
| Aviso de reposición y preventa | 0,85 | Frete Hero 142, Llegué 109 (más de 1.000 tiendas), Notificaciones de Stock 40 | No | — | Poco | A medias, sin ventaja tuya |
| Afiliados | 0,92 | Ovni 116 (BR), Parceirando 47 | No | — | Poco | Cubierta |
| Bundles y venta cruzada | 2,04 | Cashing 514, CrossUp 265, Super Checkout 123 y más | **Sí** (descuentos progresivos y regalos desde sept. 2026) | — | No | Saturada |
| Fidelización | 2,05 | Smartbis 342, Cashback & Loyalty 111 | No | — | No | Cubierta |
| Talles y probador | 2,37 | Guía de Tallas 79, Sizebay 23, Size Grid 22, Clostech 17, Tallín 12, más ocho probadores con IA nuevos | No | Tablas de talles nativas | No | Cubierta |
| Chat y atención con IA | 4,89 | JivoChat 729, Sak 181, WhatsPRO 103, Whatsplaid 99 | **Sí (Nuvem Chat)** | Real Trends y otros | No | Saturada |
| Video comprable y UGC | 9,37 | Replay 141, Widde 115, iShorts 94 | No | — | El reproductor ya está; falta contenido | Cubierta |
| Fotos de producto con IA | sin demanda en Shopify | Shoptic 24, Atlas 7 y al menos 8 nuevas con 0 | **Sí (Lumi Studio)** | — | — | Llena de recién llegados |
| Videos generados con IA | sin demanda en Shopify | Shoptic, Atlas, Vidget (1) | No | **Sí (Clips con IA gratis)**; Meta y TikTok también regalan | — | Lo regalan las plataformas |
| Turnos y reservas | ≈ 0 | Agendaqui (0), Turnos en checkout (0) | No | — | No | Hueco, pero Tiendanube es para productos, no servicios |

### 4.2 Lo que parecía hueco y no es

- **"Fotos y videos de producto con IA."** Es lo primero que se le ocurre a cualquiera, y por eso hay al menos diez apps nuevas en Tiendanube con 0 a 24 reseñas: DropStudio AI, Atelier AI, Estudio Creativo, Limonadz, Polara IA, DELFI, CatalogIA, Vidget, Shoptic y Atlas. En Shopify, las equivalentes tampoco despegaron, y Lumi Studio ya hace imágenes. El video generado con IA, además, cuesta caro: unos **USD 0,07 por segundo** a 720p con el modelo de video de Google ([Google AI Studio, precios](https://aistudio.google.com/docs/pricing)), es decir, alrededor de USD 1 por cada clip de 15 segundos.
- **"Reseñas en video."** AVALA ya convierte reseñas en Reels ([ficha de AVALA](https://www.tiendanube.com/tienda-aplicaciones-nube/avala)), Lily y Revie juntan fotos y videos por WhatsApp, y hay 42 apps en la categoría.
- **"Suscripciones" y "precios mayoristas".** Tiendanube las hizo nativas en 2026.
- **"Herramientas para vendedores de Mercado Libre."** Real Trends (más de 25.000 vendedores), Nubimetrics y los integradores cubren lo importante, y la entrada al ecosistema está cerrada.

---

## 5. Los tres huecos elegidos

Los tres comparten un mismo motor: **producto + precio real (cuotas, transferencia, promo) + marca → plantilla → imagen o video vertical, renderizado con código.**
- **Costo de render (dato):** un video corto en Remotion Lambda cuesta entre USD 0,001 y 0,02 de cómputo (1 minuto de video, USD 0,017) ([Remotion, ejemplos de costo](https://www.remotion.dev/docs/lambda/cost-example)).
- **Licencia (dato):** Remotion es gratis para personas y empresas de hasta 3 personas. Si crecés, la licencia para automatizadores cuesta USD 0,01 por render con un mínimo de USD 100 por mes ([Remotion, licencia](https://www.remotion.dev/license)).
- **Comparación:** con video generado por IA, cada clip cuesta unas 100 veces más.

Supuestos comunes de las cuentas (est.):
- **Comisión de cobro combinada: 18,5 %.** Sale de mitad de las tiendas en la Argentina, que pagan por Mercado Pago (≈ 7 %, verificar), y mitad en Brasil, que pagan por la Billing API de Tiendanube (30 %).
- **Costos fijos:** USD 200 por mes para la meta de 1.000 y USD 1.500 para la de 10.000 (servidores, herramientas, contador y soporte de medio tiempo).

### 5.1 Hueco 1: Vidriera, tu catálogo se publica solo en las redes

**El trabajo que se contrata.** "Tengo que publicar todos los días en Instagram para vender, pero no tengo tiempo ni diseñador. Además, los precios me cambian cada semana y los posteos viejos quedan con el precio equivocado."
- En la encuesta NubeCommerce México 2026 de Tiendanube, **el 81,9 % de las marcas usa Instagram** para contenido orgánico, el 79,5 % Facebook y el 48,2 % TikTok. El 64,2 % no subcontrata ningún servicio y el 10,7 % subcontrata la gestión de redes ([NubeCommerce México 2026, PDF](https://site.tiendanube.com/hubfs/%5BMX%5D%20Descargables%20Evoluci%C3%B3n/NubeCommerce_Mexico_2026.pdf)).
- No encontramos el informe equivalente de la Argentina.

**El producto y el MVP (4 a 6 semanas de construcción, est.)**
1. **App de Tiendanube integrada al panel.** Lee productos, fotos, precio, precio promocional, stock y ventas. Escucha los cambios de producto por webhook.
2. **Doce plantillas, todas en 9:16 y hechas con código, sin IA que deforme el producto:**
   - Reel de 8 a 15 s con producto, precio, "6 cuotas sin interés" y "15 % off con transferencia";
   - "Volvió el stock";
   - "Nuevo ingreso";
   - "Últimas unidades";
   - "Los 5 más vendidos de la semana", con datos de pedidos;
   - cuenta regresiva para Hot Sale y CyberMonday;
   - combos;
   - carrusel e historia diaria.

   El kit de marca (logo, colores y tipografía) sale de la tienda. Los textos y subtítulos se escriben con IA, en español rioplatense, mexicano o portugués según la tienda.
3. **Piloto automático.** Elige qué publicar según reglas (novedades, stock, más vendidos, promos), arma un calendario y publica en Instagram y Facebook por la API oficial: hasta 100 publicaciones por día por cuenta, que sobra ([Meta, Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/)). El comerciante elige entre aprobar cada pieza o dejar que se publique sola.
4. **Re-render cuando cambia el precio.** Ningún video queda con un precio viejo. Esto es lo que una herramienta global no prioriza.
5. **Ventas atribuidas.** Cada publicación lleva un link con UTM y la app cruza esos clics con los pedidos de la API. El panel muestra "ventas que trajeron tus publicaciones", que es lo que retiene clientes.
6. **Exportar** para Estados de WhatsApp y para Clips de Mercado Libre (descarga en un clic).
7. **TikTok después.** Hasta que la app pase la auditoría de TikTok, todo lo que se publique por API queda privado y solo pueden publicar 5 usuarios por día ([TikTok, Direct Post](https://developers.tiktok.com/doc/content-posting-api-reference-direct-post)). Arrancar solo con Meta.

**Evidencia.**
- **Shopify:** Outfy (583 reseñas, desde 2015, USD 19–55), Minta (324, USD 5–55) y Predis (183, USD 32–79).
- **Tiendanube Argentina y México:** no hay nada igual.
- **Nuvemshop Brasil:** SpellPost, con 0 reseñas, hace casi exactamente esto y cobra R$ 149, 279,90 y 697,90 (agencia, 3 tiendas). **Es la mejor prueba de que alguien más ve la demanda, y también es el competidor a mirar.**

**Precio propuesto.**

| Plan | Argentina | Brasil | México y otros (USD) | Incluye |
|---|---|---|---|---|
| Inicial | ARS 24.990 (USD 16) | R$ 99 (USD 17) | USD 16 | 12 Reels + 20 posts o historias por mes, Instagram y Facebook |
| Pro | ARS 49.990 (USD 32) | R$ 189 (USD 32) | USD 32 | Publicación diaria, re-render por precio, ventas atribuidas, TikTok cuando esté aprobado |
| Agencia | ARS 129.990 (USD 83) | R$ 490 (USD 83) | USD 83 | 5 tiendas y marca blanca |

**Anclas:** Lily (ARS 17.916–166.718), CrossUp (ARS 49.999 + %), Shop the Look (ARS 49.990), SpellPost (R$ 149 en adelante), Outfy (USD 19–55). Los planes de Brasil quedan por debajo de SpellPost a propósito.

**Distribución.**
- Las tres tiendas de apps: Argentina, Brasil, y México, Colombia y Chile, con fichas y precios separados por país.
- Búsquedas en la tienda: "instagram", "redes", "reels", "contenido", "posteos".
- Agencias socias de Tiendanube, con el plan Agencia.
- Un tutorial en video ("cómo publicar todos los días sin diseñador"), hecho con la misma herramienta.
- El sello "Integrado al panel", que da la sección "Recursos avanzados".

No hay evidencia de que Tiendanube destaque apps nuevas.

**Escala y costo marginal (est.).**

| Rubro | Cuenta | Costo por tienda por mes |
|---|---|---|
| Videos | 60 renders por mes (incluye re-renders) × USD 0,01 | ≈ USD 0,60 |
| Imágenes | 100 × USD 0,001 | ≈ USD 0,10 |
| Textos con IA | ≈ 200 llamadas | ≈ USD 0,40 |
| Almacenamiento y entrega de videos | | ≈ USD 0,20 |
| Margen para imágenes con IA opcionales | | hasta USD 1 |
| **Total** | | **USD 1,5 a 3** |

Atender una tienda más no suma horas: se instala sola. El soporte se escala con preguntas frecuentes y un chat con IA.

**Números (est.).**

| Escenario | Pesimista | **Base** | Optimista |
|---|---|---|---|
| Precio promedio | USD 16 | **USD 25** | USD 35 |
| Costo variable | USD 3 | **USD 2,5** | USD 2,5 |
| Aporte por tienda (después del 18,5 % de cobro) | USD 10,0 | **USD 17,9** | USD 26,0 |
| Bajas por mes | 12 % | **8 %** | 5 % |
| Lo que deja una tienda en toda su vida | USD 84 | **USD 223** | USD 520 |
| **Tiendas pagas para USD 1.000 netos** | ≈ 120 | **≈ 67** | ≈ 46 |
| **Tiendas pagas para USD 10.000 netos** | ≈ 1.145 | **≈ 643** | ≈ 442 |
| Instalaciones por semana para sostener la meta de 10.000 (pasan de prueba a pago 20 / 30 / 35 %) | ≈ 159 | **≈ 40** | ≈ 15 |

Las 643 tiendas del escenario base son el **0,3 % de las 209.254 tiendas** y el 0,4 % de las que usan Instagram (est., con el 81,9 % de México aplicado a todas). Pero estar en 643 tiendas pagas te deja al nivel de CrossUp o Llegué ("más de 1.000 tiendas"), las apps de marketing más usadas. **La meta de USD 1.000 está a la mano. La de USD 10.000 es posible, pero exige estar entre las mejores de la tienda en los tres países.**

**Durabilidad (3 de 5).**
- **Lo que protege:**
  - el motor de render y la biblioteca de plantillas, que son caros de copiar bien;
  - los datos de qué formato vende en cada rubro de Latinoamérica, que mejoran con cada tienda;
  - el precio local (cuotas, transferencia, promos bancarias);
  - las integraciones con Meta, TikTok y YouTube, cada una con su auditoría;
  - tres países y dos idiomas;
  - el calendario y el kit de marca ya armados, que hacen que irse cueste.
- **Lo que no protege:**
  - Tiendanube puede sumar "publicar en redes" a Lumi Studio;
  - Meta regala herramientas de IA para anuncios;
  - SpellPost puede bajar a la Argentina.

**Riesgos principales.**

| Riesgo | Probabilidad | Qué hacer |
|---|---|---|
| Tiendanube suma la publicación automática a Lumi | Media | Competir con lo que Lumi no hace: video con precio real, ventas atribuidas, multipaís y TikTok |
| Meta cambia permisos o pide revisión de la app para publicar | Media | Pedir la revisión de Meta desde el día 1 y ofrecer modo "descargar y publicar" |
| Videos poco atractivos frente a CapCut o Canva | Media | Plantillas con calidad de motion design (tu fuerte) y prueba con comercios reales antes de lanzar |
| SpellPost llega a la Argentina | Media-baja | Llegar primero a AR/MX y competir por precio en Brasil |
| Bajas altas ("lo probé y lo dejé") | Alta | Medir ventas atribuidas desde la primera semana |

**Experimento de 3 semanas con condiciones para abandonar.**
- **Semana 1:**
  - armar una **app privada "Para tus clientes"** (no necesita homologación) con 5 plantillas y publicación en Instagram;
  - pedir la homologación pública el mismo día, porque tarda hasta 30 días hábiles;
  - armar una página simple con un ejemplo de video de una tienda real.
- **Reclutamiento:** 40 tiendas argentinas de Tiendanube con Instagram activo (se ven por el dominio mitiendanube.com y el link en la bio), por mensaje directo y en comunidades de emprendedores. La oferta: "14 días gratis, te publicamos 3 Reels por semana con tus productos y tu precio; vos aprobás".
- **Semanas 2 y 3:** medir cuántas piezas se aprueban sin tocar, cuántas tiendas dejan el piloto automático prendido, el alcance comparado con sus publicaciones anteriores, los pedidos atribuidos y, al día 14, la preventa a ARS 24.990.
- **Se abandona (o se replantea) si pasa cualquiera de estas cosas:**
  - menos de 10 de las 40 tiendas aceptan el piloto;
  - menos del 50 % de las piezas se aprueban sin cambios;
  - menos de 5 de las 10 tiendas dejan la publicación automática prendida en la semana 2;
  - **menos de 3 pagan al día 14**;
  - Meta no aprueba la publicación de Reels desde la app.
- **Preguntas para las charlas (sin vender):**
  - "¿Cuántas veces publicaste la semana pasada? ¿Quién lo hizo y cuánto tardó?"
  - "¿Qué pasó con los posteos cuando cambiaste los precios?"
  - "¿Pagaste alguna vez a alguien por las redes? ¿Cuánto?"
  - "¿Qué apps pagás hoy en la tienda?"

### 5.2 Hueco 2: Catálogo con Cuotas, feeds con creatividades y precio argentino

**El trabajo que se contrata.** "Mis anuncios de catálogo en Meta y Google muestran el precio de lista, sin cuotas ni el descuento por transferencia. Google me rechaza productos. ChatGPT Ads me pide subir el catálogo a mano."
- Tiendanube reconoce que a Google le llega solo el precio original ([Ayuda](https://ayuda.tiendanube.com/123352-google-shopping/como-configurar-mis-productos-para-los-canales-de-venta)).
- En ChatGPT Ads, el catálogo se sube a mano en CSV o TXT ([Ayuda](https://ayuda.tiendanube.com/es_CO/chatgpt-ads/que-es-chatgpt-ads-y-como-funciona-con-tiendanube)).
- La app "Precios cuotas y promos" (177 reseñas, ARS 34.990) muestra que pagan por mostrar cuotas *en la tienda*. Este producto lo hace *en los anuncios*.

**El producto y el MVP.**
- Un feed vivo para Meta, Google, TikTok y ChatGPT, con el precio de oferta bien cargado.
- Una capa de creatividades: la foto del producto con la marca, "6 cuotas sin interés", "−15 % transferencia" y "envío gratis".
- Videos verticales para los 50 productos que más se venden. Meta permite mostrar videos del catálogo junto a las imágenes, como opción que hay que activar ([Meta, Advantage+ creative for catalog](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-creative-for-catalog)).
- Todo se re-renderiza cuando cambia el precio.
- Es la idea "Catálogo para IA" del informe anterior más una capa creativa que la hace menos fácil de copiar.

**Evidencia.**
- **Shopify:** Simprosys (4.976 reseñas), Multifeed (1.125), Mulwi (629), Socioh (67 reseñas pero USD 250–5.000 por mes), CustomPix (15, USD 19–89) y las dos apps de feed para ChatGPT (16 y 3, de julio y septiembre de 2026).
- **Tiendanube:** Feed XML (114 reseñas, "más de 200 tiendas", R$ 49); Feedom, que hace creatividades dinámicas de catálogo, con 0 reseñas, y otras tres apps de feed con 0.

**Precio propuesto.**
- Feed: ARS 18.990 (USD 12) o R$ 69.
- Feed + creatividades + video: ARS 39.990 (USD 26) o R$ 149.
- Agencia: ARS 119.990 (USD 77) o R$ 449.

**Escala y costo (est.).** Imágenes a USD 0,001 y videos a USD 0,01 por render. Con 300 productos y dos cambios de precio por mes, solo en imágenes son unos USD 0,6. Si se limita el video a los 50 más vendidos, el costo total queda en USD 1–3 por tienda.

**Números (est.).**

| Escenario | Pesimista | **Base** | Optimista |
|---|---|---|---|
| Precio promedio / costo variable | USD 12 / 2 | **USD 22 / 2,5** | USD 35 / 3 |
| Aporte / bajas por mes | USD 7,8 / 10 % | **USD 15,4 / 7 %** | USD 25,5 / 5 % |
| Tiendas para USD 1.000 | ≈ 154 | **≈ 78** | ≈ 47 |
| Tiendas para USD 10.000 | ≈ 1.478 | **≈ 745** | ≈ 451 |

**Por qué no es el primero.**
- **Meta ya regala "dynamic overlays"** (precio y descuento encima de la foto) y un generador de video a partir de imágenes ([Search Engine Land](https://searchengineland.com/meta-dynamic-overlays-advantage-catalog-ads-454657); [Search Engine Land](https://searchengineland.com/meta-generative-ai-tools-automated-video-branding-creative-ads-457221)).
- **Los presupuestos de publicidad son chicos:** en México, el 43,5 % de las marcas de Tiendanube no invierte en campañas y el 47,2 % gasta hasta MXN 5.000 por mes ([NubeCommerce México 2026](https://site.tiendanube.com/hubfs/%5BMX%5D%20Descargables%20Evoluci%C3%B3n/NubeCommerce_Mexico_2026.pdf)). Una app de USD 22 es una parte grande de esa inversión.
- **Hay competidores sin tracción pero presentes** (Feed XML, Feedom), y vos ya descartaste ideas así.

**Durabilidad:** 2 de 5. **Mejor como función de Vidriera** (los mismos videos, para anuncios) que como app aparte.

**Experimento (2 semanas) y condiciones para abandonar.**
- 10 tiendas que ya hacen anuncios de catálogo en Meta.
- Se les genera un catálogo con cuotas y video de los 30 productos más vendidos.
- Prueba A/B de 14 días en su propia cuenta.
- **Se abandona si:** menos de 6 de 10 mejoran el CTR un 10 % o más, o menos de 3 pagan ARS 18.990.

### 5.3 Hueco 3: Kit Revendedora, contenido personalizado para cada revendedora

**El trabajo que se contrata.** "Tengo 80 revendedoras. Todas las semanas les mando fotos por WhatsApp, cada una les pone su precio a mano, se equivocan, y las que no saben hacer contenido venden poco."

**El producto y el MVP.**
- Una app para la marca mayorista de Tiendanube que **complementa las tablas de precios nativas, no compite con ellas.**
- Cada revendedora tiene un link y una mini web instalable en el celular.
- Todas las semanas recibe un paquete de videos e imágenes 9:16 de los productos nuevos, con **su** precio (el mayorista más su margen), **su** nombre y **su** WhatsApp.
- Los textos se escriben con IA y las piezas salen listas para Estados de WhatsApp e Instagram.
- Los videos se renderizan solo cuando la revendedora toca "compartir", así no se paga por piezas que nadie usa.
- La marca ve quién comparte y quién compra.

**Evidencia.**
- **Shopify:** apps B2B con 700 a 1.200 reseñas (BSS 1.204, Wholesale Pricing Discount 761, B2B Wholesale Hub 701) y apps de afiliados (UpPromote 3.949).
- **Tiendanube:** las apps mayoristas tienen 0 a 5 reseñas (índice 0,08), porque los precios ya son nativos. Para contenido de revendedoras no hay nada: el único parecido es Catálogo PDF (1 reseña), que arma catálogos en PDF ([ficha](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/elunalab-catalogo-pdf)).
- **Mercado:**
  - en Brasil hay **3,1 millones de revendedores activos** y la venta directa facturó R$ 50.000 millones en 2024 ([Times Brasil, ABEVD](https://timesbrasil.com.br/brasil/adriana-colloca-da-abevd-venda-direta-esta-mais-digital-mais-jovem-e-cada-vez-mais-feminina/));
  - el 80 % de las transacciones del sector pasa por WhatsApp ([Times Brasil](https://timesbrasil.com.br/brasil/economia-da-mensagem-whatsapp-vira-principal-canal-das-vendas-diretas-no-brasil/));
  - en la Argentina hay entre 750.000 y 820.000 revendedores, según la cámara del sector (CAVEDI), con datos de años no confirmados ([Vía País](https://viapais.com.ar/rumbos/1097031-emprendedurismo-un-fenomeno-llamado-venta-directa/));
  - Natura lanzó en septiembre de 2025 "Minha Loja" y un programa para convertir a sus consultoras en creadoras de contenido ([Mercado & Consumo](https://mercadoeconsumo.com.br/30/09/2025/noticias-varejo/natura-lanca-programa-para-transformar-consultoras-em-criadoras-de-conteudo/)).

  **Las grandes ya pagan por resolverlo; las marcas chicas no tienen con qué.**

**Precio propuesto.**

| Plan | Argentina | Brasil |
|---|---|---|
| Hasta 30 revendedoras | ARS 54.990 (USD 35) | R$ 199 (USD 34) |
| Hasta 150 | ARS 109.990 (USD 70) | R$ 399 (USD 68) |
| Hasta 600 | ARS 189.990 (USD 122) | R$ 699 (USD 119) |

**Anclas:** Mayorista Pro (ARS 19.990–34.990, pero solo precios), apps B2B de Shopify (USD 25–99), Real Trends (ARS 61.000–245.000). Además, quien vende por mayor en Tiendanube ya paga al menos el plan Impulso (ARS 79.999).

**Escala y costo (est.).** Unos 10 renders por revendedora por mes, a USD 0,01 cada uno, más la mini web: entre USD 0,1 y 0,2 por revendedora. Con 100 revendedoras, unos USD 10–20 por mes. **No usar la API de WhatsApp para mandar** (un mensaje de marketing cuesta ≈ USD 0,07 en la Argentina según un proveedor, [SleekFlow](https://help.sleekflow.io/es_/pricing); verificar en la [tabla oficial de Meta](https://developers.facebook.com/docs/whatsapp/pricing)). La revendedora comparte desde su propio teléfono.

**Números (est.).**

| Escenario | Pesimista | **Base** | Optimista |
|---|---|---|---|
| Precio promedio / costo variable | USD 35 / 8 | **USD 70 / 10** | USD 120 / 15 |
| Aporte / bajas por mes | USD 20,5 / 7 % | **USD 47 / 4 %** | USD 82,8 / 3 % |
| Marcas para USD 1.000 | ≈ 58 | **≈ 26** | ≈ 14 |
| Marcas para USD 10.000 | ≈ 560 | **≈ 245** | ≈ 139 |

**Durabilidad (4 de 5).** Es el más difícil de copiar. Una vez que 80 revendedoras usan su link, la marca no cambia de herramienta. Cada revendedora, además, muestra la herramienta a otras marcas. **El punto débil es la demanda: no sabemos cuántas tiendas de Tiendanube venden por mayor** (la plataforma no lo publica). Las apps mayoristas con 0 reseñas pueden significar "lo nativo alcanza" o "no hay tantas".

**Riesgos.**
- Tiendanube sigue ampliando lo nativo para mayoristas (por ejemplo, en septiembre de 2026).
- Las revendedoras no comparten.
- Las marcas mayoristas más chicas venden por fuera de Tiendanube.

**Experimento (3 a 4 semanas).**
- 15 charlas con marcas de Tiendanube que venden por mayor (moda, cosmética, bijou), encontradas por "mayorista" en el nombre o en el dominio.
- Piloto con 3 marcas y 20 revendedoras cada una.
- **Se abandona si:**
  - menos de 5 de 15 marcas confirman que mandan contenido a mano todas las semanas;
  - menos del 25 % de las revendedoras comparte 3 piezas o más por semana;
  - ninguna de las 3 marcas paga ARS 54.990 al terminar.

---

## 6. La recomendación: Vidriera

**Arrancá por Vidriera, la app que publica sola en Instagram y Facebook, con videos armados con el catálogo y el precio real de cada tienda de Tiendanube.**

**Por qué esta y no las otras dos:**
1. **Es la única con demanda probada durante años en otra tienda de apps y sin competencia con tracción en la región.**
   - Outfy vende esto desde 2015, Minta desde 2020 y Predis desde 2022.
   - En Tiendanube Argentina y México no hay nada.
   - En Brasil hay una sola, sin reseñas, que cobra R$ 149 o más.
   - Las otras dos ideas tienen o un competidor presente que la plataforma puede pisar (feeds: Feed XML, Feedom y los overlays gratis de Meta), o una demanda que todavía no se ve (mayoristas).
2. **Usa tu ventaja de verdad.** Plantillas con calidad de motion design, renderizadas a USD 0,01 el video y re-renderizadas cada vez que cambia un precio. Eso le gana a la IA generativa en costo (cien veces menos), en fidelidad al producto (no lo deforma) y en precio local.
3. **Escala sin tus horas.** Se instala desde la tienda de apps de tres países y no necesita visitas ni carga manual. Lo pagan comercios que ya pagan Tiendanube.
4. **El motor que construís es el de las otras dos.** Cuando Vidriera llegue a 60 tiendas pagas (≈ USD 1.000 netos), los mismos videos se venden para anuncios (el producto 2, como plan "Pro + anuncios"). Cuando pase de 300, se suma Kit Revendedora como segunda app sobre el mismo motor. **Uno por vez:** la metodología Lean Startup pide un solo motor de crecimiento a la vez.

**Lo primero, desde el lunes 23/11/2026:**
- **Semana 1:**
  - app privada con 5 plantillas;
  - pedir a Meta la revisión de los permisos para publicar;
  - pedir la homologación pública en Tiendanube;
  - escribir a 40 tiendas.
- **Semanas 2 y 3:** piloto de 14 días con preventa.
- **Corte (día 21):** si pagan menos de 3, o si menos de la mitad de las piezas se aprueban sin cambios, se abandona y se pasa a probar Kit Revendedora, que es la de mayor durabilidad. En ese caso habrás perdido tres semanas, y el motor de render sirve igual.

---

## 7. Registro de búsquedas y páginas revisadas (22/11/2026)

**Tabla 8. Páginas descargadas o abiertas**

| # | Página | Para qué |
|---|---|---|
| 1 | tiendanube.com/tienda-aplicaciones-nube (portada) | Cantidad de apps, destacadas y populares |
| 2 | Las 10 categorías de la tienda argentina, todas sus páginas (64 páginas: Marketing 17, Recursos extra 17, Gestión 7, Envíos 6, Comunicación 5, Estadísticas 4, Seguridad 3, Canales de venta 2, Pagos 2, Dropshipping 1) | Inventario de 707 apps con reseñas, puntaje y forma de cobro |
| 3 | nuvemshop.com.br/loja-aplicativos-nuvem y sus 10 categorías, todas las páginas (63 páginas) | Inventario de 700 apps de Brasil |
| 4 | Fichas de Tiendanube: shoptic, estudio-atlas, replay, widde-video-commerce, feed-xml, multipricing, lily-reviews, smartbis, crossup-flowy, cheguei-avise-me, loyalty-cashback, notificaciones-de-stock, abejita-price-table, mayorista-pro, next-atacarejo, size-guides-size-chart, trustyar, shop-the-look, avala, revie, feedom, feed-vivo, feedr, glowketing | Precios, funciones e instalaciones declaradas |
| 5 | Fichas de Nuvemshop: tiktok-shop-by-base, spellpost-oficial | Competencia en TikTok Shop y en redes |
| 6 | tiendanube.dev (portada, llms.txt, sitemap) y 22 documentos en Markdown: pricing-billing, billing, publish/faq, homologation (overview, requirements, async, guidelines), publish/guidelines, app-publication (requirements, publication), erp-guide/api-usage, api/faq, webhook, script, product, product-image, nube-sdk (overview, faq, video, video-stories), storefront-api/getting-started, docs-for-agents | Cobro, API, límites y publicación |
| 7 | ayuda.tiendanube.com: cómo pagar las apps; "qué alternativa tengo si no puedo cobrar directamente" (pide iniciar sesión, no se pudo leer, dos intentos) | Reparto de ingresos |
| 8 | tiendanube.com/co/reglamento-tiendas-nube | 70/30 y pago en pesos |
| 9 | tiendanube.com/mx/socios/tecnologicos | Beneficios para socios |
| 10 | tiendanube.com/planes-y-precios | Precios de los planes en la Argentina |
| 11 | tiendanube.com/soluciones/ventas-mayoristas | Función mayorista nativa |
| 12 | tiendanube.com/blog/lumi/; nuvemshop.com.br/ia; nuvemshop.com.br/novidades-setembro-2026; tiendanube.com/blog/ecommerce-informe/ | IA nativa y lanzamientos de la plataforma |
| 13 | NubeCommerce México 2026 (PDF); intento de bajar el de Argentina (3 URL, 404) | Uso de redes y gasto en anuncios |
| 14 | storeleads.app/reports/tiendanube; /shopify; /shopify/BR (404) | Tamaño de las plataformas |
| 15 | apps.shopify.com/search (carga con JavaScript, sin resultados) | Prueba de búsqueda |
| 16 | Shopify: 7 categorías principales, 18 intermedias y 48 de último nivel (ordenadas por reseñas) | Cantidad de apps y líderes por categoría |
| 17 | Unas 70 fichas de Shopify: judgeme, loox, yotpo-social-reviews, okendo-reviews, junip, outfy (y sus reseñas), minta, predisai, orangetwig, custompix-product-catalog, marpipe, facebook-ads (Feedom), dynamic-catalog-factory, image-booster-for-dpa-ads, save-budget, google-shopping-feed, chatgpt-ads-product-feed-sync, product-feed-for-chatgpt-ads, tolstoy, videowise, whatmore-live, reelup, vidify, animate-image, ai-video-generator, showcaseai, adcreator-ai, adcreator, adify-ai, vidsyai, vigenfy, reeporter-ai, veoit-ai-bulk-videos-generator, creaitive-ai-meta-ad-creative, reframe, bria, prodshot, ecomwiz, plinth, productshots-ai, shopstudio-ai, snapclick-ai, ai-images, picsart, removebg-1, kiwi-sizing, chatty, tidio-chat, helpdesk, smile-io, subscriptions-by-appstle, bundle-deals, cartbite, b2b-solution-custom-pricing, wholesale-pricing-discount, wholesale-hub, transcy-multiple-languages, booster-apps-seo-optimizer, automated-description-writing, klaviyo-email-marketing, sizebay. Probadas sin éxito (404): photoroom, pebblely, pixelcut, claid-ai, mokker, hypotenuse-ai, vimotia, creatify, booth-ai, flair-ai, pixc, magic-studio, easysize, fit-finder, confect, hunch-dynamic-creative, pulsecast, socialwidget-autopost, postfy, vista-social-auto-post, simplified-social-posts y otras | Reseñas, precios y fecha de lanzamiento |
| 18 | global-selling.mercadolibre.com/devsite/working-with-clips | API de Clips |
| 19 | developers.mercadolibre.com.ar/es_ar/developer-partner-program (por WebFetch dio 403; se leyó descargándola) | Requisitos para ser socio |
| 20 | real-trends.com/ar/precios; nubimetrics.com/precios | Precios de herramientas para vendedores |
| 21 | outfy.com/help (resultado de búsqueda) | Plataformas que soporta Outfy |
| 22 | remotion.dev/docs/lambda/cost-example; remotion.dev/license | Costo de render y licencia |
| 23 | aistudio.google.com/docs/pricing | Costo del video generado con IA |
| 24 | developers.facebook.com/docs/whatsapp/pricing | Tarifa de WhatsApp (el valor por país está en la tabla aparte) |

**Tabla 9. Búsquedas web**

| # | Consulta | Para qué |
|---|---|---|
| 1 | Tiendanube apps desarrolladores cobro "Billing" API comisión socios tecnológicos 2026 | Cobro del desarrollador |
| 2 | Tiendanube socio aplicación "70%" del valor cobro app "Factura A" IVA desarrollador | Reparto e IVA |
| 3 | Nuvemshop parceiros tecnológicos níveis benefícios destaque loja de aplicativos app partners 2026 | Si Nuvemshop destaca apps |
| 4 | apps.shopify.com AI product photo background generator app reviews | Fotos con IA en Shopify |
| 5 | apps.shopify.com AI product video generator from product images TikTok ads app | Videos con IA en Shopify |
| 6 | Tiendanube venta mayorista tablas de precios nativo 2026 precios mayoristas clientes | Función mayorista nativa |
| 7 | Tiendanube suscripciones pagos recurrentes productos por suscripción app 2026 Nuvemshop assinatura recorrente | Suscripciones nativas |
| 8 | Tiendanube inteligencia artificial nativa fotos de productos generar imágenes descripciones IA lanzamiento 2026 | IA nativa |
| 9 | Nuvemshop novidades 2026 IA nativa imagens de produto vídeo gerado por IA lojistas | IA nativa en Brasil |
| 10 | Mercado Libre Clips vendedores API subir videos publicaciones developers 2026 | API de Clips |
| 11 | Mercado Libre partners certificados herramientas para vendedores Real Trends Nubimetrics lista socios tecnológicos 2026 | Programa de socios |
| 12 | Real Trends Mercado Libre precio plan mensual vendedores cantidad usuarios 2026 | Precios (sin resultado útil; se abrió la página de precios) |
| 13 | "Clips" Mercado Libre Argentina vendedores videos cortos publicaciones cómo subir 2026 ventas aumentan | Uso de Clips |
| 14 | Mercado Libre asistente de inteligencia artificial "Crear Clips" vendedores gratis videos generados con IA | Si ML regala el video con IA |
| 15 | apps.shopify.com dynamic catalog ads templates price overlay Meta product feed creative app Socioh Confect reviews | Creatividades de catálogo |
| 16 | Meta Advantage+ catalog ads dynamic overlays price discount free shipping video from catalog images generative AI 2026 | Riesgo de Meta |
| 17 | Tiendanube reseñas de productos nativas calificaciones función propia sin app 2026 "reseñas" | Si hay reseñas nativas (no hay) |
| 18 | venta directa revendedoras Argentina cantidad 2025 CAVEDI cámara venta directa revendedores millones | Mercado de revendedoras en la Argentina |
| 19 | ABEVD 2025 número de revendedores venda direta Brasil milhões empreendedores | Mercado de revendedoras en Brasil |
| 20 | app para revendedoras catálogo digital con su propio precio y WhatsApp marcas mayoristas Argentina Brasil "revendedoras" plataforma | Competencia del Kit Revendedora |
| 21 | Nuvemshop atacado revendedores lojistas vendem no atacado percentual lojas Nuvemshop tabela de preço 2026 NuvemCommerce | Cuántas tiendas venden por mayor (sin dato) |
| 22 | Vendizap catálogo atacado revendedores preço revenda link próprio revendedora app Brasil quantos lojistas | Competencia en Brasil |
| 23 | Natura consultoras "Minha Loja" link personalizado conteúdo pronto para divulgar redes sociais app consultora digital | Señal de demanda de las grandes |
| 24 | WhatsApp Business API tarifa Argentina 2026 mensaje utility marketing USD por mensaje Brasil | Costo de WhatsApp |
| 25 | Nuvemshop TikTok Shop integração oficial 2026 lojistas sincronizar catálogo TikTok Shop Brasil | TikTok Shop en Nuvemshop |
| 26 | TikTok Shop Brasil 2026 vendedores número GMV crescimento México TikTok Shop lançamento | Tamaño de TikTok Shop |
| 27 | cotação dólar real hoje novembro 2026 fechamento | Tipo de cambio en Brasil |
| 28 | Mercado Libre vendedores respuestas a preguntas con inteligencia artificial nativa asistente de ventas Argentina 2026 | IA nativa de ML (sin confirmación oficial) |
| 29 | apps.shopify.com social media auto post product videos Instagram TikTok scheduler app reviews Outfy alternative | Competidores de Outfy |
| 30 | Outfy integrations platforms supported Shopify Etsy WooCommerce BigCommerce Wix Tiendanube Nuvemshop | Si Outfy soporta Tiendanube (no) |
| 31 | Predis.ai Tiendanube OR Nuvemshop integración generar posts videos productos automáticamente | Si Predis soporta Tiendanube (no se encontró) |
| 32 | Instagram Graph API content publishing Reels limit posts per 24 hours business account 2026 developers.facebook.com | Límite de publicación en Instagram |
| 33 | TikTok Content Posting API direct post audit unaudited clients private only SELF_ONLY requirement developers | Auditoría de TikTok |
| 34 | NubeCommerce 2026 informe Tiendanube redes sociales Instagram canal de ventas porcentaje emprendedores contenido | Uso de redes por tiendas |

**Búsquedas dentro del inventario descargado** (1.005 apps, por palabras en el nombre y la descripción, en español y portugués): reseñas, video, foto o imagen con IA, IA en general, talles, feed, upsell y kits, aviso de stock, mayorista, suscripción, traducción, SEO, fidelización, chat y soporte, descripciones, TikTok, cambios y devoluciones, preventa, personalización, influencers, anuncios, turnos y reservas, quiz, buscador, gift cards, seguimiento, carga masiva, velocidad, moneda, cookies, probador, video con IA y publicación en redes.

**Lo que no se pudo verificar:**
- las instalaciones reales de las apps de Tiendanube, que no se publican (usamos tres casos declarados para estimar la relación reseñas/instalaciones);
- el reparto 70/30 para la Argentina en una página abierta (la de ayuda pide iniciar sesión; el reglamento leído es el de Colombia) y el tipo de cambio con el que Tiendanube paga en pesos;
- si Tiendanube cobra o elige qué apps destaca en la portada;
- cuántas tiendas de Tiendanube venden por mayor;
- la tarifa oficial de WhatsApp por país (el valor de la Argentina es de un proveedor);
- el informe NubeCommerce 2026 de la Argentina (usamos el de México);
- las ventas reales de SpellPost, Outfy, Minta y Predis (las reseñas no son ventas);
- la comisión exacta de Mercado Pago para cobros recurrentes.

---

## Conclusión

La tienda de Shopify enseña algo incómodo: lo que se vende no es "IA" sino trabajo resuelto de punta a punta. En Tiendanube, casi todo lo que funciona en Shopify ya tiene una app local o se volvió función nativa en 2026. Ese fue el caso de las suscripciones, los precios mayoristas, los descuentos del carrito, las imágenes con IA y el chat. Quedan pocos huecos de verdad. El más grande, y el que mejor encaja con lo que sabés hacer, es que una tienda chica pueda publicar todos los días videos buenos, con su precio real, sin tocar nada. Outfy demostró durante diez años que eso se paga. En la Argentina y México nadie lo ofrece dentro de Tiendanube, y en Brasil hay uno solo, todavía sin reseñas. La ventana existe, pero es corta. Por eso el plan no es construir durante meses: es mostrar en tres semanas si 3 tiendas de 40 pagan. Si pagan, tenés un motor que después sirve para anuncios y para revendedoras. Si no pagan, la evidencia habrá hablado a tiempo.
