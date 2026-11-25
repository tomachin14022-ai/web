# Qué dice la gente en Reddit (y en foros parecidos) sobre comprar un 0 km, vender autos con video y convertir mensajes en leads, para validar el calendario de Valparaiso Motors

> Notas de investigación al 25/11/2026. No repiten lo que ya está en `CLAUDE.md`, en la *Guía paso a paso del calendario de contenido* ni en `publico-y-lenguaje.md`, `contenido-que-vende.md` o las notas del *Plan de leads*.
>
> **Aviso importante: no pude leer Reddit.** Probé todas las vías permitidas y todas fallaron:
> - API oficial (`/api/v1/access_token` a través del proxy): **401 Unauthorized**;
> - JSON público con un User-Agent honesto (`/r/askcarsales/search.json`): **403**;
> - WebFetch sobre `old.reddit.com`: bloqueado ("unable to fetch");
> - WebSearch con `allowed_domains: reddit.com`: el buscador responde que **reddit.com no es accesible** para su agente;
> - WebSearch con `site:reddit.com`, con "r/askcarsales" o con "usuario de Reddit": **cero resultados de Reddit** en 10 búsquedas (en español y en inglés).
>
> No usé espejos, archivos ni navegadores simulados. Por eso **en estas notas no hay ninguna cita textual de Reddit, ni votos de Reddit**. Lo reemplacé con lo más parecido que sí se podía leer:
> - **DealerRefresh**, el foro de gerentes y responsables de marketing de concesionarias de EE. UU. (lo más parecido a r/askcarsales o r/autodealers), con fechas y reacciones de cada mensaje;
> - el foro de **Edmunds** (compradores);
> - **notas de prensa que recogen voces de compradores** argentinos y de vendedores;
> - la **aclaración oficial de Instagram** sobre pedir comentarios con una palabra y sobre ManyChat (la pregunta 4 del encargo).
>
> Cómo leer las fuentes: "(resumen de búsqueda)" quiere decir que el dato sale del resumen del buscador y no abrí la página. "(foro)" es la opinión de una persona, no un dato. "(proveedor)" o "(plataforma)" es una empresa hablando de su propio producto.

## 1. Compradores en Argentina: autos chinos, posventa, reventa, precios, financiación, gastos ocultos y concesionarios

### Takeaway
Sin acceso a Reddit no hay voces directas de compradores argentinos en foros. Lo que sí aparece en la prensa de 2025–2026 coincide con las objeciones que el plan ya ataca (posventa, repuestos, reventa) y suma dos puntos que el calendario no trabaja: **los gastos de entrega y patentamiento** (flete, formularios, preentrega, gestoría), que generan reclamos y fallos judiciales, y la **diferencia de precio del plan de ahorro** durante la guerra de precios de 2026.

### Cited Findings
**Reventa de autos chinos**
- iProfesional (01/09/2026), con precios de Mercado Libre y datos de la Cámara de Comercio Automotor (CCA):
  - las marcas tradicionales "pierde[n] entre el 15 % y el 20 %" en el primer año; las chinas, **entre 25 % y 35 %**;
  - a los tres años, las tradicionales retienen 65–70 % y las chinas "ronda[n] el 60,7 %";
  - la causa, según la CCA, es que el comprador de usados argentino "es conservador" y desconfía de repuestos, red de concesionarios y posventa. En las transferencias de usados de ACARA "los chinos no aparecen";
  - la nota no da datos por modelo (ni Haval H6, ni Jolion, ni BYD) — [iProfesional, 01/09/2026](https://www.iprofesional.com/autos/463346-cuanto-se-deprecian-los-autos-chinos-usados-frente-a-otras-marcas)
  - **Ojo:** el 60,7 % es exactamente la cifra de **España** (Ganvam-DAT) que ya figura en `Plan de leads/marcas-y-objeciones.md`. Es muy probable que la nota mezcle un dato español con los argentinos. No usar el 60,7 % como dato argentino.

**Posventa y repuestos (voces del sector)**
- La Capital (Rosario) recoge a un referente del sector: el proveedor decide traer una pieza según cuántos autos de esa marca se vendieron. Un especialista opina que, "por cultura de fabricación", cada unidad no duraría más de 10 años. Es una opinión sin datos (resumen de búsqueda; sin fecha visible) — [La Capital](https://www.lacapital.com.ar/motores/boom-autos-chinos-rosario-que-riesgos-pueden-aparecer-despues-la-compra-n10271297.html)
- Noticias Argentinas (18/12/2025): el comprador de una SUV de una marca china (sin nombre) denunció fallas a los 7 meses y que el concesionario "no da con la solución". Es **un caso aislado** y la página solo muestra un resumen — [Ground News / Noticias Argentinas, 18/12/2025](https://ground.news/article/a-global-user-warns-of-the-risks-of-buying-a-chinese-car-brand-sold-in-argentina)

**Gastos de entrega y patentamiento**
- Unión de Consumidores (UCU): un comprador recibió un presupuesto de **$1.200.000 en gastos** ("flete, formularios, honorarios 0km y gastos preentrega"), con **$466.440 de flete** que consideró injustificado y sin comprobantes. Después del reclamo, el total bajó a $850.000, que igual le pareció excesivo (resumen de búsqueda; **la página hoy da error 404 y no tiene fecha visible**) — [UCU](https://ucu.org.ar/gastos-abusivos-en-la-compra-de-vehiculos-0-km/)
- Bariloche: la justicia condenó a un concesionario por cobrar de más el patentamiento de una Ford Ranger. Facturó ~$1,64 millones contra un valor mucho menor del estimador oficial, y atribuyó la diferencia a honorarios de gestoría (resumen de búsqueda; sin fecha visible) — [Examedia](https://examedia.com.ar/portada/post/88108648)
- Diario de Cuyo: los cargos de gestoría, flete y preentrega "los fija cada concesionaria" y varían de un negocio a otro (resumen de búsqueda; sin fecha) — [Diario de Cuyo](https://www.diariodecuyo.com.ar/noticias/a-cuanto-se-va-el-costo-de-inscribir-ahora-un-vehiculo-818939.html)

**Plan de ahorro en la guerra de precios de 2026**
- Infobae (13/06/2026, Diego Zorrero):
  - el que compara, aun en la misma marca, consigue **descuentos de 25 % a 30 %** sobre la lista;
  - el ahorrista paga la **lista oficial**, que hoy queda **~25 % arriba del precio real de contado**;
  - según un directivo de una terminal, en 2022 era al revés (había sobreprecios de 30–40 % y el plan "hizo negocio");
  - de enero a mayo de 2026 se entregaron por plan **52.289 de 232.815** autos (~22 %) — [Infobae, 13/06/2026](https://www.infobae.com/economia/2026/06/13/en-medio-de-la-guerra-de-precios-para-vender-mas-autos-surgio-una-polemica-con-los-planes-de-ahorro/)
- Derecho en Zapatillas (2026): muchos ahorristas llegan a la adjudicación sin el 30 % del capital y lo completan con préstamos personales caros o vendiendo su usado barato (resumen de búsqueda) — [Derecho en Zapatillas](https://www.derechoenzapatillas.com/2026/plan-de-ahorro-automotor-en-argentina-derechos-y-practica/)
- iProfesional recoge a una compradora que disfruta su auto pero "no elegiría nuevamente el plan de ahorro" (resumen de búsqueda) — [iProfesional](https://www.iprofesional.com/autos/383490-comprar-un-auto-con-plan-de-ahorro-por-que-conviene-hoy)

### Inferences
- **Los gastos de entrega son una objeción real y poco explicada.** Hay reclamos de consumidores y al menos un fallo por sobreprecio. Un concesionario que muestra **el precio para llevárselo, con cada gasto escrito**, se diferencia. Encaja con la regla de "precio final en pesos" del plan y con el "se ve, se entiende".
- **La reventa es la objeción del comprador mayor de 50** (ver `publico-y-lenguaje.md`): según la CCA, el comprador de usados es conservador. Se responde con hechos verificables: garantía y si se transfiere al segundo dueño, service en la casa con historial y tasación del usado. No con cifras de depreciación de origen dudoso.
- **El plan de ahorro está en su peor momento relativo** (2026). Respalda que el video de créditos muestre su desventaja. Si se usa el número, va con fecha y fuente ("según Infobae, junio de 2026") y sin nombrar marcas.

### Gaps
- **No pude leer ningún hilo de r/argentina, r/Cordoba, r/RepublicaArgentina, r/ArgentinaBenderStyle ni de subs de autos en español** (ver el aviso de arriba). Quedan sin respuesta, desde la voz del comprador: cómo eligen concesionario, qué piensan de GWM, Haval y Changan en particular, si esperan a enero para patentar, la experiencia con concesionarios que no contestan y menciones de concesionarios de Córdoba.
- Precio de usados de Haval, ORA o Changan en la guía InfoAuto o en ACARA: sigue sin datos por modelo.
- Una cita atribuida en el resumen del buscador a "un ex vendedor en Reddit" ("nuestro mayor miedo era tu celular") no tenía enlace verificable: **no la uso**.
- La nota de UCU ya no está publicada; el monto sale del resumen del buscador.

## 2. Vendedores y concesionarios: qué contenido trae compradores, velocidad de respuesta, seguimiento, reseñas, inauguraciones y lo viral

### Takeaway
En el foro de DealerRefresh (el equivalente profesional de r/askcarsales y r/autodealers) el patrón que más se repite es: **las vistas orgánicas no son compradores de la zona; lo que funciona localmente es lo pago, el retargeting y atender el teléfono**. Las cuentas personales de vendedores pueden traer compradores (hay casos), pero los que llegan de lejos no sirven para un concesionario regional. Es el diagnóstico del reel de 150 mil vistas sin leads. Sobre inauguraciones no hay ningún dato de resultados, ni en foros.

### Cited Findings
**Foro DealerRefresh, hilo "Any dealers using TikTok for marketing campaigns?"** (2023: **anterior a 2024**; las insignias de rol las elige cada usuario y no están verificadas)
- **Ryan Everson** (insignia "Car Dealer", 21/02/2023, **4 reacciones**, el mensaje más apoyado de la página):
  - "Most of those views probably aren't in the market to buy" (la mayoría de esas vistas probablemente no está por comprar);
  - "Don't waste a $30-50k salary on vanity metrics that will never influence someone in your local market to buy" (no gastes un sueldo en métricas de vanidad que nunca van a hacer comprar a alguien de tu zona);
  - aconseja **no** darle TikTok "para probar" al vendedor más joven.
  — [DealerRefresh, página 3](https://forum.dealerrefresh.com/threads/any-dealers-using-tiktok-for-marketing-campaigns.7890/page-3)
- **Gold Pony** (concesionario, 08/02/2023, 2 reacciones): "TikTok definitely does well with marketing to a local audience **when it's paid**" (funciona con público local cuando es pago). Usa los videos para mostrar la cara de los vendedores — [DealerRefresh, página 3](https://forum.dealerrefresh.com/threads/any-dealers-using-tiktok-for-marketing-campaigns.7890/page-3)
- **kevinfrye** (concesionario, 09/02/2023, 2 reacciones): "Our goal is branding, not direct selling" (el objetivo es la marca, no vender directo) — [DealerRefresh, página 3](https://forum.dealerrefresh.com/threads/any-dealers-using-tiktok-for-marketing-campaigns.7890/page-3)
- **Kelly Wilson** (proveedor y concesionario, 20/02/2023): muchos fallan con la "venta social" porque "they still think they are just selling a unit" (todavía creen que solo venden una unidad) — [DealerRefresh, página 3](https://forum.dealerrefresh.com/threads/any-dealers-using-tiktok-for-marketing-campaigns.7890/page-3)
- **DSmovingmetal** (proveedor, 21/02/2023): en TikTok "no real data behind claims of attribution" (no hay datos reales que respalden la atribución de ventas). Ryan Everson agrega que los anuncios de catálogo solo sirven para **retargeting** — [DealerRefresh, página 3](https://forum.dealerrefresh.com/threads/any-dealers-using-tiktok-for-marketing-campaigns.7890/page-3)
- **Todd Thompson** (concesionario, 08/10/2023, 2 reacciones): "I'm betting most could earn more by simply **picking up the phone** at a dealer when it rings" (la mayoría ganaría más atendiendo el teléfono cuando suena) — [DealerRefresh, página 4](https://forum.dealerrefresh.com/threads/any-dealers-using-tiktok-for-marketing-campaigns.7890/page-4)
- **Quality Motors / Jay** (concesionario, 09/10/2023): "I had better engagements and conversions from Facebook and Instagram" (le fue mejor con Facebook e Instagram) — [DealerRefresh, página 4](https://forum.dealerrefresh.com/threads/any-dealers-using-tiktok-for-marketing-campaigns.7890/page-4)
- Otras opiniones del mismo hilo (resumen de búsqueda; no las vi en las páginas que abrí):
  - las páginas personales crecen más rápido que las de la concesionaria;
  - "no hay correlación entre seguidores y ventas" (con el ejemplo de un Ferrari con 1,8 millones de seguidores);
  - los videos perfectos rinden menos que los que muestran a la gente real;
  - la oferta agresiva en video falla, salvo con gente que ya está muy cerca de comprar.
  — [DealerRefresh, hilo completo](https://forum.dealerrefresh.com/threads/7890/)

**Vendedores con marca personal (prensa del rubro, 2026)**
- **Andrea Anderson** (Andrews Cadillac, "Andrea Sells Cadillacs"; CBT News, 19/11/2026):
  - ~480.000 seguidores en Instagram y ~170.000 en TikTok, en un año y medio;
  - mezcla **entretenimiento** (sketches) con **educación**: equipamiento, cómo es el proceso de compra, **qué son los cargos del concesionario y qué se puede negociar**;
  - publica los **usados que entran antes de que aparezcan en la web**;
  - compradores viajaron desde Illinois y Oregon, y uno compró un auto de USD 180.000. **No da totales de leads ni de ventas**;
  - el cliente necesita "confidence that the salesperson understands the product and can guide them effectively" (confianza en que el vendedor conoce el producto y lo puede guiar), y hay que superar "the initial discomfort of being on camera" (la incomodidad inicial de estar en cámara).
  — [CBT News, 19/11/2026](https://cbtnews.com/used-car-week-2026-andrea-anderson)
- **Tianna Mick** (Dealer Synergy, un proveedor): los vendedores tienen éxito en TikTok con contenido divertido "que no se centra en vender directo", y la constancia es "lo número uno en lo que falla la industria" (resumen de búsqueda) — [CBT News](https://www.cbtnews.com/?p=213195)

**Velocidad de respuesta y precio por escrito**
- DealerRefresh (**2014, viejo**): un moderador defiende la velocidad ("Being fastest means you'll reply while they may still be online"; contestar primero te encuentra todavía en línea). Otros responden que un mail rápido "se hunde en la bandeja" y que importa lo que dice, no solo la velocidad — [DealerRefresh, 2014](https://forum.dealerrefresh.com/threads/internet-closing-percentage.4071/page-4)
- Foro de Edmunds (compradores): "most dealers will give you a verbal quote over the phone, but very few will give you a quote in writing by e-mail" (casi todos dan un precio de palabra por teléfono, muy pocos por escrito) (resumen de búsqueda; sin fecha) — [Edmunds Forums](https://forums.edmunds.com/discussion/comment/2254268)
- Motor1 recoge el caso de un vendedor de Mazda que se quejó en TikTok de un comprador que pidió "el mejor precio final" antes de ir. Es justo lo que recomienda Consumer Reports (resumen de búsqueda) — [Motor1](https://www.motor1.com/news/801365/buyer-catfishes-car-salesman/)

**Inauguraciones**
- La prensa solo publica asistencias (700 personas en un Lexus de Reno, más de 300 en un Hyundai de Louisville) y frases como "fue un éxito, tuvimos tres canales de TV". **Ninguna fuente publica ventas atribuibles** y no encontré discusiones de foro sobre resultados (resumen de búsqueda) — [Auto Dealer Today](https://www.autodealertodaymagazine.com/articles/quad-cities-suzukibrwhere-every-day-is-special-finance-show-and-tell); [WDRB](https://www.wdrb.com/news/new-oxmoor-hyundai-genesis-dealership-opens-with-community-celebration/article_1dea1107-f779-45f1-b63b-762cf3e1ab0e.html)

### Inferences
- **Confirma tres decisiones del plan:**
  1. medir con códigos y no con vistas;
  2. promocionar en Córdoba lo que funciona;
  3. poner la fuerza en la respuesta a los mensajes. "Atender el teléfono cuando suena" es la versión del foro de la guardia de 5 minutos.
- **Matiza las piezas de entretenimiento:** en el foro, nadie que vende autos defiende el alcance orgánico como fuente de compradores locales. El plan ya cierra cada pieza de entretenimiento con un paso comercial. Además conviene ponerle un **tope de horas** y moverlas a educar o vender si a las 6–8 semanas no traen chats con código.
- **El formato de Anderson suma uno que falta en el calendario:** explicar **los cargos y qué se negocia**. Encaja con la objeción argentina de los gastos de entrega (pregunta 1).
- **"Llegó al salón" antes que a la web** es un buen gancho para los que ya siguen la cuenta: da una razón para mirar las historias y los Estados.
- **Los vendedores en cámara no pueden quitarle tiempo a la respuesta.** La advertencia de no darle TikTok "al más joven" es sobre el costo de oportunidad: el vendedor que graba tiene que seguir contestando sus leads.

### Gaps
- No pude leer r/askcarsales, r/CarSalesTraining, r/Dealerships, r/autodealers ni r/sales. En particular, no tengo opiniones de vendedores sobre vivos de TikTok, Facebook Marketplace, pedidos de reseñas ni sobre la palabra clave en comentarios.
- El hilo de DealerRefresh es de 2023 y de EE. UU.: no es la Argentina ni 2024–2026.
- No encontré ningún dato, en foros ni en la prensa, de ventas atribuibles a una inauguración.

## 3. Marketing: anuncios a WhatsApp, palabra clave en comentarios (ManyChat), reels de prueba, ganchos, frecuencia y mezcla de contenido

### Takeaway
Lo más útil no viene de foros sino de **Instagram mismo**:
- pedir que comenten "una palabra, un número o un emoji" para ganar alcance puede hacer que **Instagram no recomiende el reel**;
- pero usar ManyChat para generar leads por mensaje privado **"no se considera cebo de interacción"**;
- y no recomienda Reels de más de 90 segundos.

Sobre anuncios a WhatsApp solo hay casos de Meta y de proveedores, que sugieren **optimizar por leads y no por conversaciones**.

### Cited Findings
**Instagram (plataforma), junio de 2024**
- Primero: Instagram no recomienda contenido que pide interacción de forma explícita, por ejemplo "asking people to comment with a specific word, number, or emoji" (pedir que comenten una palabra, un número o un emoji).
- Después aclaró:
  - las preguntas abiertas y los CTA siguen bien;
  - se pueden usar servicios como ManyChat ("can still use 3rd party services such as ManyChat to enhance how they engage with their audiences");
  - interactuar en comentarios y mensajes para conectar, **generar leads** o convertir "is not considered to be engagement bait" (no se considera cebo de interacción).
- Social Media Today aclara que **no se sabe cómo el sistema automático distingue** el uso aceptable del spam. Instagram no quiso dar ejemplos de palabras penalizadas.
- Además, Instagram "won't recommend Reels that are over 90 seconds long" (no recomienda Reels de más de 90 s a no seguidores).
- Fuente: [Social Media Today, 05/06/2024](https://www.socialmediatoday.com/news/instagram-clarifies-advice-single-word-ctas-longer-reels/718151/). **Dato de 2024: verificar si sigue igual**, porque Instagram amplió después el largo máximo de los Reels.

**Cansancio con "comentá X"**
- Analytics Insight (blog): el exceso de automatización "puede sentirse impersonal y reducir la confianza". Es opinión, sin datos — [Analytics Insight](https://www.analyticsinsight.net/digital-marketing/how-comment-for-link-helps-instagram-creators-increase-engagement-and-earnings)
- Molly White (24/11/2024) muestra una sección de comentarios de Instagram donde todos dicen solo "Pie". Lo vincula con las herramientas que empujan a inflar los comentarios. Es una observación — [Molly White](https://www.mollywhite.net/micro/entry/202411241337)

**Anuncios a WhatsApp (casos de Meta y de proveedores)**
- WhatsApp Business (casos informados por los mismos anunciantes):
  - **Nutryfit**: más leads calificados con un costo por lead 12 % menor al pasar de optimizar por conversaciones a **optimizar por leads**;
  - **Braip**: +45 % de leads calificados contra anuncios optimizados por mensajes.

  (resumen de búsqueda) — [WhatsApp Business: Nutryfit](https://whatsappbusiness.com/resources/success-stories/nutryfit/); [WhatsApp Business: Braip](https://whatsappbusiness.com/resources/success-stories/braip/)
- SleekFlow (proveedor), caso EcoWorld: el **21 %** de los leads de anuncios a WhatsApp fue de "alta calidad". Es decir, ~4 de cada 5 chats no lo eran (resumen de búsqueda) — [SleekFlow](https://sleekflow.io/blog/click-to-whatsapp-ads)
- No encontré discusiones de foro (ni de Reddit, ni de otros) con quejas de "leads basura" en anuncios a WhatsApp.

### Inferences
- **"Comentá EADO" no está prohibido, pero hay que escribirlo como pedido de precio, no como juego de interacción.** Según Instagram, lo penalizado es pedir comentarios para inflar el alcance. Lo aceptado es usar el comentario para iniciar una conversación comercial. Formulación segura: "Si querés precio y cuota, comentá EADO y te escribimos". No va "comentá EADO si te gustó" ni "comentá 🔥".
- **En los reels de entretener, el alcance a no seguidores es todo.** Ahí conviene que la palabra clave vaya en el comentario fijado y en la descripción, y que el video cierre con el CTA comercial. Se puede medir con reels de prueba: la misma pieza con y sin "comentá X" en el video.
- **Ningún reel de más de 90 s** si busca no seguidores (verificar la regla vigente). El largo va a YouTube, como ya prevé el plan.
- **Anuncios a WhatsApp:** que la mayoría de los chats no sea calificada (21 % en el caso de SleekFlow) respalda la regla del plan de decidir por **costo por turno que asiste**. Si en la Argentina está disponible la optimización por leads dentro de WhatsApp, vale probarla en A1.

### Gaps
- No pude leer r/socialmedia, r/marketing, r/InstagramMarketing, r/TikTokMarketing, r/PPC ni r/FacebookAds. No tengo experiencias de usuarios con reels de prueba, ManyChat (molestias, mensajes en "Solicitudes"), frecuencia de publicación ni mezcla de contenido en negocios locales.
- No pude confirmar si la regla de los 90 s sigue vigente en noviembre de 2026.
- No pude confirmar si la optimización por leads de los anuncios a WhatsApp está disponible para cuentas argentinas.

## 4. Lo que contradice o tensiona el plan

### Takeaway
No encontré nada que tire abajo el plan. Hay **cuatro tensiones concretas**:
1. pedir comentarios con una palabra puede reducir la recomendación del reel si suena a cebo;
2. el alcance orgánico casi no trae compradores locales, según los concesionarios del foro;
3. el comprador desconfía de los gastos ocultos más que del precio de lista;
4. los vendedores en video funcionan cuando explican y son constantes, no cuando venden fuerte.

### Cited Findings
- Instagram limita la recomendación de contenido que pide "una palabra, un número o un emoji", y aclara que usar ManyChat para generar leads no es cebo (2024) — [Social Media Today, 05/06/2024](https://www.socialmediatoday.com/news/instagram-clarifies-advice-single-word-ctas-longer-reels/718151/)
- "Most of those views probably aren't in the market to buy" (4 reacciones, el mensaje más apoyado del hilo) — [DealerRefresh, 21/02/2023](https://forum.dealerrefresh.com/threads/any-dealers-using-tiktok-for-marketing-campaigns.7890/page-3)
- Reclamos y fallos por flete, preentrega y gestoría inflados — [UCU](https://ucu.org.ar/gastos-abusivos-en-la-compra-de-vehiculos-0-km/); [Examedia](https://examedia.com.ar/portada/post/88108648)
- Los vendedores que crecen explican el proceso y los cargos, no venden fuerte — [CBT News, 19/11/2026](https://cbtnews.com/used-car-week-2026-andrea-anderson); la oferta agresiva en video falla (resumen de búsqueda) — [DealerRefresh](https://forum.dealerrefresh.com/threads/7890/)
- Casi ningún concesionario da el precio por escrito; los compradores lo piden (resumen de búsqueda) — [Edmunds Forums](https://forums.edmunds.com/discussion/comment/2254268); [Motor1](https://www.motor1.com/news/801365/buyer-catfishes-car-salesman/)

### Inferences
- **"Comentá X para el precio" contra "el precio en la pieza":** el plan ya pone precio, cuota y CFT dentro de las piezas de vender (Res. 446/2025). En las de educar y entretener, el "comentá X" no esconde un precio que el video podría mostrar: es un atajo a la conversación. Hay que cuidar que nunca parezca que el precio se esconde. En las piezas de vender, **el precio va en el video y la palabra clave es para la cuota a medida**.
- **Que la gente se queje de "comentá X para el precio"** (la duda del encargo) no la pude confirmar ni descartar, por falta de acceso a Reddit.

### Gaps
- Las molestias de los usuarios con "comentá X" y la opinión del público sobre los videos de vendedores eran justo las preguntas para Reddit, y quedaron sin respuesta.

## Qué cambiar en el calendario y los guiones

Ordenado por prioridad. Ninguno sale de Reddit (no se pudo leer). Cada uno indica su fuente.

1. **Reescribir todas las palabras clave como pedido de precio, nunca como juego de interacción.** En la hoja Guiones y en los comentarios fijados, usar siempre la forma "Si querés precio y cuota, comentá EADO y te escribimos". Sacar cualquier "comentá 🔥", "comentá SÍ si te gustó" o "comentá tu opinión con una palabra". En los reels de **entretener**, la palabra clave va en el comentario fijado y en la descripción, no dicha en la voz. Probarlo con un par de reels de prueba con y sin el pedido en el video. Fuente: Instagram, 2024.
2. **Ningún reel de más de 90 s** en Instagram si tiene que llegar a no seguidores (verificar si la regla sigue vigente). Revisar en la hoja Escenas los guiones largos y cortarlos o mandarlos a YouTube. Fuente: Instagram, 2024.
3. **Sumar un guion educativo: "¿Qué pagás además del precio de un 0 km?"** Flete, formularios, patentamiento, preentrega y seguro, con los montos reales de Valparaiso por escrito y la frase "te lo damos por escrito antes de que vengas". Agregar esa línea a la respuesta de "Cuota" de WhatsApp. Es la objeción con reclamos y fallos detrás, y casi nadie da el precio por escrito. Fuente: UCU, Examedia, Edmunds y el formato de Anderson. **Que lo apruebe Administración y el abogado.**
4. **Sumar al "¿Auto chino?" (y a la placa de garantía) la objeción de la reventa,** con hechos propios:
   - si la garantía pasa al segundo dueño (verificar con GWM, Changan y Mitsubishi);
   - el service con historial en la casa;
   - la toma del usado.

   No usar cifras de depreciación: la de iProfesional mezcla un dato español. Fuente: iProfesional y CCA.
5. **Ponerle un tope a lo viral.** Las piezas de entretener tienen un máximo de horas de producción por semana. En la lectura del 11/1, si no traen chats con código de Córdoba, se mueven 5–10 puntos hacia educar y vender (el plan ya lo prevé; con el foro es más firme). Fuente: DealerRefresh.
6. **Explicar el proceso de compra en una serie corta con el vendedor:**
   - qué se negocia y qué no;
   - cómo se toma el usado;
   - qué es cada papel.

   Es el formato que más confianza construye en el caso de Anderson y responde al "no entiende la financiación" del público "Cambia su usado". Fuente: CBT News, 2026.
7. **"Llegó al salón" primero en historias y Estados, antes que en la web y Mercado Libre,** y decirlo ("lo ves acá antes que en ningún lado"). Le da al que sigue la cuenta una razón para mirar. Fuente: CBT News, 2026.
8. **Que grabar no le quite tiempo a la respuesta.** El martes de grabación no puede dejar sin guardia los WhatsApp: el responsable de primer contacto no graba, y el vendedor en cámara no atiende la guardia ese bloque. Fuente: DealerRefresh, "atender el teléfono" y "no se lo des al más joven".
9. **En la campaña A1, probar la optimización por leads** (si Meta la ofrece en la Argentina para anuncios a WhatsApp) contra la de conversaciones, y decidir por costo por turno que asiste. Fuente: casos de Meta y SleekFlow, informados por las mismas empresas.
10. **Cubrir a mano lo que no se pudo investigar.** Que la persona de contenido dedique 30 minutos por semana a leer, desde su navegador, Reddit (r/argentina, r/Cordoba, r/RepublicaArgentina, buscando "Haval", "Changan", "GWM", "auto chino", "patentar enero", "gastos de entrega", "concesionaria Córdoba"), las preguntas de Mercado Libre y los grupos de Facebook de dueños de Haval y Changan. Que anote las preguntas textuales en la hoja de "El vendedor responde". Así esta investigación se completa con fuentes reales y las objeciones de los guiones salen de las palabras del público.
