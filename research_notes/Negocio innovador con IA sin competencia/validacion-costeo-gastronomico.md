# Validating "MarginEdge for Argentina": supplier invoice photo → live ingredient prices, dish costs and margin alerts for food service (WhatsApp-first, high inflation)

Research date: 20 November 2026. All prices are as published on the cited page on that date. ARS→USD conversions use the official retail rate of about ARS 1,565–1,570 per USD (Banco Nación, 2–5 Nov 2026), per [iProfesional](https://www.iprofesional.com/finanzas/468108-el-dolar-minorista-anota-un-nuevo-maximo-pero-sube-menos-que-la-inflacion) and [El Economista](https://eleconomista.com.ar/economia/dolar-hoy-cuanto-cotiza-jueves-5-noviembre-n99481). The conversions are mine.

**Bottom line up front:** the earlier note ([ia-mundo-fisico.md](ia-mundo-fisico.md), candidate B) said "probably unserved, medium confidence". That conclusion **does not survive this deeper check.**
- **Fudo has shipped most of the loop.** Fudo is the leading Argentine restaurant POS (35,000+ businesses; 13,400 Argentine venues in its July 2026 price survey). During 2026 it shipped:
  - AI invoice import from photo or PDF, reading line items;
  - automatic cost and inventory updates from expenses (on the Avanzado plan, about USD 30/month);
  - a cross-restaurant ingredient "Radar de Precios" (August 2026). This is the same data moat the earlier note proposed.
- **Small apps already do the core trick.** At least one Argentine micro-app, InstaCost, does "photo of supplier invoice → recipe cost updates" for USD 0–20/month.
- **Regional players exist.** COSTIQ (Panama/LatAm, USD 129+/month) does the same with AI alerts.
- **What is left is a narrow wedge, not a blank space:**
  - automatic matching and unit conversion (Fudo matches items to ingredients by hand);
  - proactive per-dish margin alerts with price suggestions (I found none in Fudo);
  - ingestion over WhatsApp itself (Fudo's is inside its own app);
  - venues that don't use Fudo;
  - done-for-you onboarding.

---

## Q1. How strong is the pain? Food-service inflation, supplier price swings, closures and margin pressure in Argentina (2025–2026)

### Takeaway
The pain is real but has changed shape. General restaurant inflation slowed to about 1–1.5% a month (33.6% year on year in October 2026). The acute problem now is (a) single inputs that jump (beef rose 73% year on year by January 2026, 10.6% in March alone, then was flat in October) and (b) owners who **cannot pass costs to the menu**, because demand fell 30–40% in two years. That makes knowing each dish's margin more valuable. It also makes owners less willing to spend on new software.

### Cited Findings
- **INDEC, restaurants and hotels, October 2026:** +1.5% month on month and **33.6% year on year**. September was +1.1% month on month and 34.6% year on year. January–October cumulative was 26.4%, against 26.3% for the general CPI, which was +2.2% in October. Data released 12 Nov 2026. — [Vinetur citing INDEC](https://www.vinetur.com/en/20261113111015/argentinas-restaurant-and-hotel-inflation-accelerated-to-15-in-october.html); [El Litoral](https://www.ellitoral.com/economia/inflacion-octubre-indec-ipc-argentina_0_FP9XmzuO1F.html)
- **Correction to earlier notes:** the "restaurant prices rose almost 68% year on year" figure, cited from iProfesional, is from an article dated **19 April 2022**. The 2026 date on the page is just the site's current-date display. The same article quotes Daniel Prieto (AHRCC): "a lo sumo aplicamos un 3 o 4 por ciento de retoque en la carta", against supplier increases of about 20%. Use it only as historical context. — [iProfesional, Apr 2022](https://www.iprofesional.com/negocios/360877-menu-complicado-como-pega-la-inflacion-en-los-restaurantes)
- **Beef, the key input for parrillas and bodegones, is very volatile:**
  - average cut prices were +73% year on year to January 2026 (IPCVA) while inflation was about 32%;
  - +10.6% in March 2026 alone, and +68.6% over 12 months;
  - by October 2026, +0.1% month on month and only +15.7% in the first 10 months.
  
  — [Chequeado](https://chequeado.com/el-explicador/la-carne-aumento-casi-el-doble-que-la-inflacion-y-cayo-el-consumo-las-razones-detras-de-este-fenomeno/); [Diario de Cuyo, Apr 2026](https://www.diariodecuyo.com.ar/economia/el-precio-la-carne-no-frena-y-escala-otro-106-marzo-n6570321); [Perfil](https://www.perfil.com/noticias/amp/economia/cae-el-consumo-y-el-precio-de-la-carne-va-detras-de-la-inflacion-pero-se-esperan-aumentos-en-noviembre-y-diciembre-amzPs1S7ghjY.phtml)
- **Demand collapse (July 2026, sector chambers):**
  - consumption in bars and restaurants down an estimated 30–40% over two years;
  - CABA rents above ARS 4,000,000 a month, and beef "aumentó 30% en 3 meses";
  - FEHGRA president Daniel Prieto said pizzerías and bodegones resist best and the average ticket fell.
  
  These are chamber estimates, not official data. — [Infomiba](https://infomiba.com.ar/nota/57214/crisis-en-la-gastronomia-bares-y-restaurantes-perdieron-hasta-40-de-clientes-en-2-anos-y-advierten-por-mas-cierres/); [Nexos Digital](https://nexosdigital.com.ar/2026/07/17/el-consumo-en-bares-y-restaurantes-cayo-40-en-los-ultimos-dos-anos/)
- FEHGRA asked the government for tax relief and a halt to embargoes and tax foreclosures to prevent more closures of hotel and restaurant SMEs. — [Ladevi](https://argentina.ladevi.info/actualidad/crisis-hoteles-y-restaurantes-fehgra-pidio-frenar-embargos-evitar-cierres-n100923)
- The Cámara Argentina de Comercio reported that empty storefronts on main downtown streets rose 43.4% in Jan–Feb 2026. In March 2026 the historic bar The New Brighton (City porteña) went bankrupt. — [El Nacional Noticias](https://www.elnacionalnoticias.com.ar/noticias/nacionales/las-mesas-vacias-el-cierre-de-bares-y-restaurantes-expone-la-caida-del-consumo/); [Diario de Cuyo, 18 Mar 2026](https://www.diariodecuyo.com.ar/argentina/uno-los-restaurantes-mas-emblematicos-la-city-portena-quiebra-tenia-mas-un-siglo-historia-n6568521)
- **Córdoba, 15 Oct 2026.** Alfredo Alberione (Cámara de Bares de Córdoba):
  - "Hace mucho tiempo no se veía tan feo, peor que en pandemia";
  - "Hoy los bares mantenemos las cartas bajas, no las estamos aumentando porque sabemos que está muy difícil la situación";
  - "Estamos aguantando, los proveedores con aumento y demás";
  - "Vos le aguantás, le aguantás, un mes fuiste para atrás".
  
  — [Perfil Córdoba](https://www.perfil.com/noticias/cordoba/el-representante-de-los-bares-de-cordoba-por-la-caida-del-consumo-hace-mucho-tiempo-no-se-veia-tan-feo-peor-que-en-pandemia.phtml)
- **Córdoba, all retail (not gastronomy-specific):** the Cámara de Comercio de Córdoba reported unit sales −21% in May 2026, −23% in September and −19% year on year in October. — [Perfil Córdoba](https://www.perfil.com/noticias/amp/cordoba/las-ventas-cayeron-23-en-cordoba-y-desde-la-camara-de-comercio-advierten-que-no-hay-mucho-margen-para-seguir-bajando.phtml); [America Retail](https://americaretail-malls.com/paises/argentina/el-comercio-de-cordoba-enfrenta-una-nueva-baja-en-ventas-y-rentabilidad-durante-octubre/)
- A Córdoba restaurant closure (Guaros de Lara, Centro, 5 Nov 2026) was reported. — [Vía País](https://viapais.com.ar/cordoba/cerro-restaurante-centro-cordoba-adios-definitivo-clasico-comida-internacional_0_KepGvPbXzX.html)
- **Owner behaviour quotes (dates unclear; probably 2022–2024):**
  - Germán Ousset of La Rosalía (San Telmo parrilla): "Si fuera por la inflación, semana por medio deberíamos tocar la carta."
  - Another owner: reprinting the menu costs about ARS 50,000, so "Esperamos y modificamos la carta completa."
  - A Paraná source: beef suppliers raised prices 30–40% in one week.
  
  — [iProfesional](https://www.iprofesional.com/actualidad/378376-efecto-inflacion-restaurantes-sin-precios-y-ropa-en-dolares); [La Nación](https://www.lanacion.com.ar/sociedad/comer-afuera-menos-y-mas-caro-nid1494511); [Infogastronómica](https://www.infogastronomica.com.ar/el-aumento-del-precio-de-la-carne-puso-contra-las-cuerdas-a-los-locales-gastronomicos/)
- An Argentine costing calculator warns that "con inflación, el costeo de hace 2 meses ya no sirve" and that indirect costs add 5–12% per portion. — [hacecuentas.com](https://hacecuentas.com/calculadora-costo-receta-precio-por-porcion)
- A University of Tucumán (UNT) field-work series (2024–2026) on gastronomic SMEs says decisions are made intuitively, without reliable integrated information systems. This is a search snippet; the PDF text could not be extracted. — [UNT/FACE](https://face.unt.edu.ar/web/iadmin/wp-content/uploads/sites/2/2026/02/24-Figueroa-Angeles-Fiorella-Trabajo-de-Campo_compressed.pdf)
- **Successful operators' practice (Forbes Argentina, 8 Oct 2026):**
  - Centro Restaurant "sistematizamos todos los procesos en un sistema", tracking stock control, cost of goods sold and weekly sales stats;
  - "Meternos al 100% en el proceso de compra fue clave";
  - they also worked on reducing waste.
  
  — [Forbes Argentina](https://www.forbesargentina.com/negocios/la-batalla-ticket-medio-ingenieria-costos-previsibilidad-defender-rentabilidad-gastronomia-n99731)

### Inferences
- The selling message has to change. "Inflation makes your costing stale" was strong in 2022–2024 (monthly restaurant inflation of 5–10%). At 1–1.5% a month it is weaker. The 2026 pitch is: **"single-ingredient shocks (beef, cheese, oil) silently kill specific dishes, and since you can't raise the whole menu, you need to know exactly which dishes to reprice, shrink, reformulate or drop."**
- Owners are freezing menu prices (Alberione). That raises the value of per-dish margin visibility. It also signals survival mode, where new monthly subscriptions are the first thing cut. Pain is high, and so is budget resistance.

### Gaps
- I found **no survey of how often Argentine owners update their costings** (weekly, monthly, never). It needs primary interviews.
- No 2026 number for restaurant closures in Argentina or Córdoba. The widely cited "35% closed in Córdoba" is from **July 2020 (lockdown)**, not 2026. — [Hoy Día Córdoba, 1 Jul 2020](https://hoydia.com.ar/informacion-general/70874-restaurantes-cerro-el-35)
- No published food-cost-% benchmarks for Argentine restaurants were found.

---

## Q2. How big is the market, and which segments are most likely to pay?

### Takeaway
There are about 67,000 gastronomic establishments nationally (FEHGRA), plus roughly 33,000 traditional bakeries (a 2010 estimate, since shrunk). Fudo alone has about 13,400 Argentine venues (≈20% of FEHGRA's count; my calculation). Córdoba province has at least about 1,900 *companies* (sociedades) registered in the two main restaurant codes, and more venues run by individual or monotributo owners. The market is big enough in theory. The constraint is reaching and onboarding venues, not market size.

### Cited Findings
- FEHGRA says it groups more than 84,000 companies: 17,000 hotel and **67,000 gastronomic establishments** (Hotelga 2025 press release; same figure in a 2024 regional meeting note). — [Hotelga 2025 PDF](https://hotelga.ar.messefrankfurt.com/content/dam/messefrankfurt-argentina/hotelga/press-releases/2024/12_HTG2025_AGO2025_Finalizó_Hotelga_2025.pdf); [Diario Jornada](https://diariojornada.com.ar/365237/economia/se_realizo_la_reunion_regional_de_la_fehgra_)
- **Fudo footprint:**
  - "Más de 35.000 negocios confían en Fudo" across Argentina, Chile, Colombia, Mexico and Brazil (plus Peru, Paraguay and Uruguay in the footer);
  - a July 2026 Fudo price survey covered **13,400 Argentine gastronomic venues** that work with Fudo.
  
  — [Fudo AR](https://fu.do/es-ar/); [Economis](https://economis.com.ar/del-cafe-a-la-pizza-comer-en-misiones-cuesta-hasta-51-menos-que-el-promedio-argentino/); [Descubre](https://www.descubre.vc/fudo)
- **Córdoba, AFIP/ARCA register via indicadores.ar** (companies only, which excludes individual owners and monotributistas):
  - **799** sociedades with main activity "Servicios de restaurantes y cantinas sin espectáculo" (CIIU 561011 and 552111);
  - **1,079** with 561019, "expendio de comidas y bebidas … con servicio de mesa y/o en mostrador n.c.p.";
  - a search snippet gave 682 for 561011 alone, so the definitions differ.
  
  Summing the other provinces listed on the page gives about 11,986 sociedades in 561011 nationally (my calculation). — [indicadores.ar 561011 Córdoba](https://indicadores.ar/empresas/sector/561011/cordoba); [indicadores.ar 561019 Córdoba](https://indicadores.ar/empresas/sector/561019/cordoba)
- **Bakeries:**
  - a Ministry of Agriculture publication estimated one traditional bakery per 1,100–1,200 inhabitants, about **33,000** in 2010;
  - closure claims conflict: "2.000 panaderías … en dos años" (La Gaceta, Mar 2026) vs "14.000 en 18 meses" (BAE Negocios, Aug 2025).
  
  — [MAGyP](https://alimentosargentinos.magyp.gob.ar/contenido/sectores/farinaceos/Productos/ProductosPanificados_2011_04Abr.pdf); [La Gaceta](https://www.lagaceta.com.ar/nota/1127992/economia/caida-consumo-dos-anos-cerraron-2000-panaderias-se-perdieron-16000-empleos.html); [BAE Negocios](https://www.baenegocios.com/economia/en-un-ano-y-medio-cerraron-14-000-panaderias-en-todo-el-pais-20250831-0058.html)
- Formats that resist best in 2026 are pizzerías and bodegones (Prieto, FEHGRA). — [Infomiba](https://infomiba.com.ar/nota/57214/crisis-en-la-gastronomia-bares-y-restaurantes-perdieron-hasta-40-de-clientes-en-2-anos-y-advierten-por-mas-cierres/)
- Maxirest is described as having more than 9,000 clients in Argentina, with "control de costos por receta" and analysis of supplier price lists. This came from a search-engine summary; I could not confirm it on Maxirest's own site. — [ITSitio](https://www.itsitio.com/?p=111781) (unverified); [Maxirest help, costs](https://maxirest.helpjuice.com/costos)

### Inferences
- **Most likely to pay:**
  1. independent full-service restaurants, bodegones, pizzerías and parrillas with 1–3 locations, many suppliers and protein-heavy menus (beef shocks);
  2. small chains or franchisees (3–10 locations), where one bad costing repeats at every location;
  3. food producers with wholesale customers (pastas, viandas, alfajores, catering). They must quote prices to B2B buyers, so knowing their margin is directly worth money.
- **Least likely to pay:** micro-bakers and home pastry makers. They are already served by apps costing USD 2–20 (see Q3), and they have the lowest budgets.
- **Rough reachable market in Córdoba city:** a few hundred venues with 10+ employees, many suppliers and enough revenue to care about 2–3 margin points. This is an estimate, not sourced. About 30 paying customers (needed for USD 1,000 net) means roughly 5–10% penetration of that core, which is plausible only with in-person selling.
- Fudo covers about 20% of FEHGRA's establishment count (13,400 / 67,000; my calculation, and the counts are not strictly comparable). The other ~80% use Maxirest, Bistrosoft, other POS systems, simple invoicing tools or nothing. That is where a standalone tool could live.

### Gaps
- No official count of gastronomic venues in Córdoba province or city (FEHGRA, AEHGC, the municipality or SIPA employers). indicadores.ar counts only sociedades.
- No data on POS penetration or software use among Argentine restaurants.
- No current FAIPA census of bakeries.

---

## Q3. Exhaustive competitor search: who already reads supplier invoices and updates dish costs (Argentina, LatAm, Spain, Brazil, US)?

### Takeaway
**The core feature is not unserved locally.** Fudo, the market-leading Argentine POS:
- reads supplier invoices from photo or PDF with AI, including line items (since May 2026);
- updates stock and costs from expenses (Avanzado and Pro plans);
- compares ingredient prices with other restaurants in the region (August 2026).

Argentine micro-apps (InstaCost) and LatAm tools (COSTIQ) already sell "photo of invoice → recipe re-cost". Brazil, Spain and the US have many mature equivalents.

**Differentiation still open:**
- automatic ingredient matching and unit conversion (Fudo's is manual);
- proactive per-dish margin alerts with price suggestions (I found none at Fudo);
- WhatsApp as the intake channel;
- coverage for non-Fudo venues;
- done-for-you onboarding.

### Cited Findings

**Argentina: POS and management suites**
- **Fudo (Argentina; 35,000+ businesses; seed USD 7.5M in Aug 2022 from a16z, Atlantico and MAYA):**
  - **Pricing (ARS, monthly):**
    - **Inicial ARS 23,900** (≈USD 15): expenses only, no recipes;
    - **Avanzado ARS 46,500** (≈USD 30): "Carga de recetas", "actualización automática de costos", automatic inventory update from expenses, low-stock alerts, supplier database and supplier current accounts, waste tracking, sub-ingredients, and "Gastos con IA desde la foto del comprobante (Avanzado: 10 por mes)";
    - **Pro ARS 93,500** (≈USD 60): unlimited AI receipt capture, valued inventory, income statement, cash flow, product and ingredient technical sheets;
    - add-ons: "Recepcionista IA" (ARS 60,000/month) answers WhatsApp and takes reservations.
  - **Changelog:**
    - May 2026: "Importación de facturas con IA … Cargás una factura subiendo una foto o PDF y la IA extrae los datos" (Pro; Argentina, Chile, Mexico, Colombia);
    - **August 2026: "Radar de Precios: comparativo de compras con IA"**, which compares ingredient prices with other restaurants in the region ("Te señala dónde estás por encima del mercado y cuánto puedes ahorrar con cada proveedor"; Pro 5 ingredients, Avanzado 2);
    - October 2026: the mobile app assistant records expenses from an invoice photo;
    - September 2026 (Chile only): the assistant can change menu prices from chat;
    - earlier: margin % and markup columns (Jan 2024), waste % per ingredient (Feb 2024), technical sheets (Jun 2024), 3-level sub-ingredients (Jul 2024), valued stock (Sep 2024).
  - **Support article (1 Jul 2026):** the AI reads date, total, supplier, taxes and "la IA reconoce los ítems de la factura y te muestra su cantidad y costo neto". Matching each item to an ingredient is done by the user with search ("Agregar"). The article does not mention recipe-cost recalculation or margin alerts.
  
  — [Fudo pricing AR](https://fu.do/es-ar/precios/); [Fudo changelog](https://tools.fu.do/novedades); [Fudo support: AI invoice import](https://soporte.fu.do/es/articles/15707806-como-importar-facturas-mediante-foto-o-pdf-con-ia); [Fudo support: expenses](https://intercom.help/fudoapp/es/articles/11730876-registro-de-gastos-y-compras-en-fudo); [Fudo blog, 12 Nov 2026](https://blog.fu.do/del-cuaderno-al-asistente-ia-la-nueva-etapa-de-la-gesti%C3%B3n-gastron%C3%B3mica); [TechCrunch 2022](https://techcrunch.com/2022/08/19/andreessen-atlantico-maya-capital-fudos-seed-restaurant-tech)
  - **Conflict:** the pricing page includes AI receipts in Avanzado (10/month). The May 2026 changelog lists invoice import for Pro, and an older note says Chile Pro gets 15 invoices a month. Limits may differ by country or have changed.
- **Maxirest (Argentina):**
  - the help center describes a cost module "desde la carga de insumos hasta la elaboración de recetas y gestión de inventario";
  - no AI invoice reading is mentioned;
  - no public prices.
  
  — [Maxirest help](https://maxirest.helpjuice.com/costos)
- **Bistrosoft (Argentina/Mexico; cloud POS with inventory):** no public pricing; Capterra India shows an unexplained "36,000" with no currency. No AI invoice reading found. — [Capterra](https://www.capterra.co.uk/software/1109312/Bistrosoft); [ComparaSoftware](https://www.comparasoftware.com/bistrosoft)
- **Other Argentine POS systems (no recipe-costing-from-invoice features found):**
  - Frambuesa: ARS 29,900–49,900/month with ARCA invoicing; no recipe costing or invoice AI mentioned;
  - OrdenApp: ARS 19,900–59,900/month, WhatsApp ordering, stock, ARCA; AI agent at ARS 290 per order;
  - Restoo: ARS 35,000–80,000;
  - Liveware: ARS 45,000–110,000;
  - Bsale: ARS 28,000–65,000;
  - Sispyme Gastro: USD 300–800 one-time.
  
  — [Frambuesa](https://www.frambuesa.app/software-para-restaurantes-argentina); [OrdenApp](https://ordenapp.com.ar/); [Develop Argentina, 25 Jun 2026](https://developargentina.com/blog/software-para-restaurantes-argentina-2026)
- Tento (Argentina, 100+ venues) covers reservations, ordering and delivery; no costing. — [Forbes Argentina](https://www.forbesargentina.com/negocios/del-salon-analogico-ecosistema-data-driven-como-una-startup-digitalizo-gastronomia-us-500000-ya-proyecta-us-15-millones-2027-n78738/amp)

**Argentina: standalone costing apps (direct substitutes)**
- **InstaCost (Argentina):**
  - targets bakeries, pastry shops, rotiserías, cafés, bars, caterers and burger shops;
  - "Fotografiá la factura de harina, aceite, huevos…": AI extracts ingredients, quantities and prices, and recipe costs update automatically;
  - also stock, production log, P&L, PDF quotes and "historial de inflación" per ingredient;
  - **Free** (3 scans, 2 recipes), **USD 10** (50 scans, 20 recipes), **USD 20** (100 scans, unlimited recipes, weekly email summary);
  - no company name, traction or WhatsApp mentioned.
  
  — [InstaCost](https://instacost.shop/)
- **wokito** (by PLIKY, Argentina): recipe costing, gross margin, alerts and AI price suggestions (beta). Free plan, **Pro USD 6.99/month** (a structured listing shows ARS 8,999). No invoice scanning. — [wokito](https://wokito.com/)
- **BakeData** (Argentina, pastry): recipes recalculate when an ingredient price changes. Free (12 recipes); "Plan Fundador" **ARS 3,500/month** (≈USD 2.2), "quedan 27 de 50 lugares". No invoice scanning. — [BakeData](https://bakedata.app/)
- Gigiad: free pastry cost calculator with quotes via WhatsApp. — [Gigiad](https://gigiad.com/)
- Costo Receta (Spain/Mexico/LatAm): technical sheets dictated by voice, from USD 5/month. — [Costo Receta](https://costoreceta.com/)
- An open-source "FoodCost" project on GitHub: AI recipe costing for small gastronomic businesses. — [GitHub](https://github.com/anacerro84/FoodCost)

**Spanish-speaking LatAm**
- **COSTIQ** (Broken Table Hospitality; WhatsApp number +507 Panama; "operadores en 5 países"):
  - "Una foto de la factura carga el inventario y recostea tus platos";
  - Serrano AI alerts (e.g. "Food cost subió 3.8% vs semana anterior"), menu engineering, upload of the POS sales report "aunque sea una foto", supplier orders "por WhatsApp";
  - **Esencial USD 129/month** (1 location, 10 AI scans), **Rentabilidad USD 219** (2 locations, 20 scans), **Grupo USD 537** (3 locations, unlimited);
  - optional implementation USD 290–490;
  - no customer testimonials on the site.
  
  — [COSTIQ](https://www.costiqapp.com/); [COSTIQ pricing](https://www.costiqapp.com/precios)
- **CostoPRO** (appears Peruvian; founder Héctor Valdivia):
  - recipes, purchases with weighted-average cost updating recipes, kardex, menu engineering;
  - **USD 20/month** or USD 190/year; Profesional USD 490/year; Premium USD 1,290/year;
  - no AI invoice reading.
  
  — [CostoPRO](https://www.costopro.lat/)
- **Toteat (Chile; ~2,000–2,600 clients, older figures):** inventory by recipe. Capterra lists USD 25 (Básico) and USD 53 (Avanzado) per month "per feature", possibly outdated. No AI invoice reading found. — [Capterra](https://www.capterra.com/p/252184/Toteat/); [Portal Innova](https://portalinnova.cl/software-gastronomico/)
- **Restaurant.pe (Peru), Parrot (Mexico), Loyverse, Resto.ar, Gastrosoft, Waiter:** my searches returned no evidence of invoice-to-recipe-cost AI. For Parrot, Capterra mentions only POS and delivery. This is **absence of evidence, not confirmed absence.** — [Capterra Parrot via search](https://www.capterra.es/directory/31837/food-costing/software)

**Brazil (Portuguese query)**
- NettoChef (AI reads items, quantities, prices and supplier from a photo; Pro €18.99/month), Gastrum by Helsen IA (photo of nota → stock; dish cost recalculated), Custo por Prato (nota reading on paid plans), Chef.IA, CostFi and Menup (NF-e XML import), Saipos (CMV real from supplier-note imports; plans "a partir de R$219"). — [NettoChef](https://play.google.com/store/apps/details?id=com.nettochef.app&hl=pt); [Gastrum](https://www.helsenia.com.br/produtos/gastrum); [Custo por Prato](https://www.custoporprato.com.br/); [CostFi](https://www.costfi.com.br/plans-pricing); [Saipos CMV](https://saipos.com/sistema/cmv-real)

**Spain (escandallo software)**
- tSpoonLab:
  - official docs: delivery-note OCR from photo or PDF via the tspoonFast app;
  - "registra automáticamente cualquier cambio de precio en la ficha del producto";
  - €95–110/month.
  
  — [tSpoonLab docs](https://www.tspoonlab.com/docs/en/articles/12569666-receiving-delivery-notes-with-ocr); [Qamarero ranking, 29 Oct 2026](https://qamarero.com/blog/mejores-software-escandallos-restaurantes-2026/)
- Others, from a vendor-written ranking:
  - Qamarero €249/month (a fixed price "una factura nueva no lo sobrescribe");
  - haddock €248–299;
  - Prezo €119.90–154.90 (mentions OCR);
  - gramo €29;
  - ChefExpenses €10–25;
  - Yurest from €79–99 per function;
  - Apicbase from €249;
  - Gstock on request.
  
  — [Qamarero ranking](https://qamarero.com/blog/mejores-software-escandallos-restaurantes-2026/); [Capterra Yurest](https://www.capterra.com/p/10047559/Yurest/); [Capterra Apicbase](https://www.capterra.es/software/171584/apicbase-restaurant-management)
- AI Chef Pro (Spain, €10/month credits) publishes "Buenos Aires" SEO guides; no invoice reading found. — [AI Chef Pro](https://aichef.pro/abrir-restaurante/buenos-aires)

**US / global benchmarks**
- **MarginEdge:** **USD 350 per location per month** (official), 10% off annually; the Freepour bundle adds USD 150 (USD 500 total); Toast users pay +USD 50. — [MarginEdge pricing](https://www.marginedge.com/pricing)
- **MarketMan:** USD 249/month (50 AI invoice scans), Growth USD 299 (unlimited), Enterprise from USD 449. — [MarketMan pricing](https://marketman.com/pricing)
- **xtraCHEF by Toast:** Essentials USD 179, Pro USD 279 per location per month. — [Toast](https://pos.toasttab.com/es-us/products/restaurant-invoice-processing); [Toast support](https://support.toasttab.com/es-US/article/xtraCHEF-101)
- **KitchenIQ:** AI invoice photo extraction, price tracking and alerts; Tracker plan USD 25/month. **meez:** free, paid from USD 19/month. — [GetApp KitchenIQ](https://www.getapp.com/all-software/a/kitcheniq/); [GetApp meez](https://www.getapp.com/hospitality-travel-software/a/meez/)
- **Supy** says it recalculates every recipe when an approved invoice changes a price, across locations. — [Supy blog](https://supy.io/blog/learn-keep-recipe-costs-current-supplier-price-sync)
- **YC:** Marble (YC S26, US/Canada) is building an AI back-office for restaurants including invoices. Plate IQ (2015–2017) did invoice photos. No YC company targets LatAm restaurants. — [YC Restaurant Tech](https://www.ycombinator.com/companies/industry/restaurant-tech); [Runtimewire, Marble](https://runtimewire.com/es/article/marble-ai-restaurant-back-office-yc-s26)

**ARCA data (relevant to differentiation)**
- ARCA's web service WSFEv1 is for comprobantes "A", "B", "C" and "M" **"sin detalle de ítem"**. Line items go to ARCA only through WSMTXCA (A/B "con detalle de items"). So ARCA generally holds totals, not line items, and a photo or PDF of the invoice is still needed for ingredient prices. — [ARCA web services](https://www.arca.gob.ar/ws/documentacion/ws-factura-electronica.asp)
- "Mis Comprobantes → Recibidos" can be exported (Excel/CSV) with header data (number, date, CAE, amount, issuer CUIT). — [Colppy help](https://intercom.help/Colppy/es/articles/3181130-importar-tus-facturas-desde-mis-comprobantes-recibidos-afip); [YoFacturo](https://yo-facturo.com/comprobantes-recibidos-arca/)

**Queries run** (this pass; earlier queries are listed in ia-mundo-fisico.md, Q7). Results as noted:

*Local and LatAm competitors (Spanish):*
1. "Fudo recetas costo de plato ingredientes": nothing on Fudo.
2. "software costeo recetas facturas proveedores IA restaurantes Argentina 2026" (extended): found InstaCost, COSTIQ, CostoPRO, Frambuesa, FoodCost.
3. "escandallo automático facturas proveedores inteligencia artificial restaurante" (extended): Spanish vendors.
4. "InstaCost app costos panadería facturas": BakeCost, CakeCost.
5. "Maxirest costo de recetas insumos compras proveedores precio abono"
6. "Bistrosoft recetas costos stock compras precio plan"
7. "Fudo \"gastos con IA\" foto comprobante" (extended): found Fudo's AI invoice import.
8. "Fudo ayuda costo de recetas actualización automática gasto insumo precio"
9. "Toteat costeo recetas inventario facturas proveedores precio"
10. "costos recetas gastronomía app Argentina facturas WhatsApp IA panadería" (extended): found wokito, InstaCost, BakeData, Gigiad, Costo Receta, OrdenApp.
11. "Maxirest precios planes mensual 2026"
12. "Fudo \"Radar de Precios\" ingredientes restaurantes"
13. "Bistrosoft precio plan mensual Argentina gestión gastronómica stock costos"
14. "site:play.google.com costo recetas gastronomía factura": old generic apps only.
15. "Restaurant.pe Parrot Software recetas costeo insumos facturas compras"
16. "Waiter OrdenApp Gastrosoft software gastronómico Argentina recetas costos compras"
17. "\"Agregar productos y/o ingredientes a un gasto\" Fudo"
18. "Fudo soporte costo ingrediente actualización automática gasto receta"
19. "Toteat inventario recetas costo insumos plan precio Chile"
20. "Fudo software gastronómico clientes Argentina inversión ronda 2025 2026"

*Brazil (Portuguese):*

21. "app custo ficha técnica nota fiscal foto restaurante IA atualiza custo prato" (extended)
22. "Saipos ficha técnica CMV entrada nota fiscal preço plano"

*Spain, US and YC (Spanish/English):*

23. "Gastrokaizen Yurest Apicbase escandallo precio mensual OCR facturas": nothing on Gastrokaizen.
24. "Tspoonlab precios escandallo lectura albaranes OCR"
25. "MarginEdge pricing per location 2026"
26. "Kitchio Marketman Galley Meez pricing recipe costing invoice scanning": no Kitchio or Galley pricing found.
27. "Y Combinator restaurant invoice AI food cost Latin America startup"

*ARCA data:*

28. "\"Mis Comprobantes\" ARCA detalle ítems factura recibida descargar"
29. "WSFEv1 no incluye detalle de ítems WSMTXCA factura electrónica ítems"

Pages fetched: fu.do/es-ar, fu.do/es-ar/precios, tools.fu.do/novedades, the Fudo support articles, the Fudo blog, instacost.shop, costiqapp.com, costiqapp.com/precios, costopro.lat, wokito.com, bakedata.app, aichef.pro, the qamarero.com ranking, developargentina.com and maxirest.helpjuice.com.

### Inferences
- **The "nobody does it locally" premise is false** for the core loop. The honest positioning is "a better and different version of something that exists", aimed at venues the incumbents don't serve well.
- **Fudo's remaining weaknesses, as of the evidence:**
  1. item-to-ingredient matching is manual;
  2. unit conversion and pack sizes ("caja x 12 de 1 L", "horma 4,2 kg") are not described;
  3. no proactive per-dish "this dish dropped below target margin, raise to $X" alert was found;
  4. invoice intake is inside the Fudo app or web, not a WhatsApp number;
  5. AI receipts are capped at 10 a month on Avanzado (or Pro only, per the changelog). A venue with 30–80 supplier invoices a month would need Pro (≈USD 60).
- **Fudo is clearly moving into this space** (AI invoice import in May, price radar in August, assistant photo expenses in October, chat price changes in Chile in September). Expect margin alerts and price suggestions within 6–12 months (my inference). A standalone product aimed at Fudo users would be crushed.
- **Micro-segment saturation.** Several Argentine indie apps (InstaCost, wokito, BakeData, Gigiad) sell to bakers and pastry makers at USD 2–20. This segment is crowded and price-anchored near zero.
- **ARCA has no line items** (WSFEv1). That confirms images or PDFs remain necessary for everyone, so it is no moat. It enables one differentiator: reconcile the ARCA "Recibidos" list against the invoices the venue has sent, and flag missing ones ("ARCA shows 14 supplier invoices this month; you've sent us 9"). I found no competitor advertising this.

### Gaps
- Not verified: Kitchio's current status (the earlier note found it on huntscreens); Galley's pricing; Gastrokaizen; Consumer and Goomer (Brazil); Loyverse's ingredient costing; LinkedIn, Product Hunt and Capterra ES directory pages (not fetched).
- I could not confirm whether Fudo's "actualización automática de costos" uses last cost or average cost, or whether it recalculates recipe margins immediately when an AI-imported invoice is saved. A Fudo Avanzado trial would answer this in a day.
- InstaCost's, wokito's and COSTIQ's real traction (customers, revenue) is unknown; none show testimonials.

---

## Q4. Willingness to pay: what do Argentine venues pay today, and what do comparable tools cost?

### Takeaway
Argentine venues pay about **USD 15–60/month for a whole POS-plus-management suite** (Fudo ARS 23,900–93,500). Standalone costing apps sell for **USD 2–20**. US invoice-to-cost tools charge USD 179–350 per location, and the LatAm "premium" COSTIQ asks USD 129–537. A standalone Argentine tool charging much above **USD 40–60 per location per month** would cost more than the full Fudo suite that already includes basic invoice AI. In a 2026 demand crisis, that is a hard sell unless the ROI is shown in pesos within the first month.

### Cited Findings
- **Fudo:**
  - Inicial ARS 23,900, Avanzado ARS 46,500, Pro ARS 93,500 per month (≈USD 15 / 30 / 60), with 10–15% off semiannual or annual billing;
  - add-ons: electronic invoicing ARS 13,500, delivery apps ARS 19,500, AI receptionist ARS 60,000 (≈USD 38).
  
  — [Fudo pricing](https://fu.do/es-ar/precios/)
- **Other Argentine POS:** Frambuesa ARS 29,900–49,900; OrdenApp ARS 19,900–59,900; Restoo ARS 35,000–80,000; Liveware ARS 45,000–110,000; Bsale ARS 28,000–65,000. — [Frambuesa](https://www.frambuesa.app/software-para-restaurantes-argentina); [OrdenApp](https://ordenapp.com.ar/); [Develop Argentina](https://developargentina.com/blog/software-para-restaurantes-argentina-2026)
- **Argentine costing apps:** InstaCost USD 0/10/20; wokito USD 6.99; BakeData ARS 3,500 "fundador" (≈USD 2.2). — [InstaCost](https://instacost.shop/); [wokito](https://wokito.com/); [BakeData](https://bakedata.app/)
- **LatAm and Spain:** COSTIQ USD 129/219/537 plus USD 290–490 implementation; CostoPRO USD 20/month or USD 190/year; tSpoonLab €95–110; Prezo €119.90–154.90; Qamarero €249; gramo €29; ChefExpenses €10–25. — [COSTIQ pricing](https://www.costiqapp.com/precios); [CostoPRO](https://www.costopro.lat/); [Qamarero ranking](https://qamarero.com/blog/mejores-software-escandallos-restaurantes-2026/)
- **US:** MarginEdge USD 350; MarketMan USD 249–299; xtraCHEF USD 179–279; KitchenIQ USD 25; meez from USD 19. — [MarginEdge](https://www.marginedge.com/pricing); [MarketMan](https://marketman.com/pricing); [Toast](https://pos.toasttab.com/es-us/products/restaurant-invoice-processing); [GetApp KitchenIQ](https://www.getapp.com/all-software/a/kitcheniq/)
- **Vendor claims (unverified):** a Spanish vendor claims AI escandallo cuts costing time by 60–80% and improves food cost by 2–5 points, "según proyectos de consultoría". — [Aivy](https://aivy.es/guias/ia-para-hosteleria/)
- **Consultants:** Argentine food-cost consultants are on LinkedIn and Fiverr, but **no public fees** were found. — [Fiverr mdgastrocontrol](https://www.fiverr.com/mdgastrocontrol)
- Córdoba bars are "aguantando" supplier increases without raising menus (Oct 2026). — [Perfil Córdoba](https://www.perfil.com/noticias/cordoba/el-representante-de-los-bares-de-cordoba-por-la-caida-del-consumo-hace-mucho-tiempo-no-se-veia-tan-feo-peor-que-en-pandemia.phtml)

### Inferences
- **ROI framing that could justify about USD 40–60/month** (all numbers illustrative, not sourced): a venue with ARS 30M/month in sales and 32% food cost buys about ARS 9.6M of inputs. Catching one supplier overcharge or one underpriced best-seller worth 1 point of food cost recovers ARS 300k/month, about 4–6× the fee. The product must prove a saving like this in the first 30 days, in pesos, or it will be cancelled.
- **A setup fee is more realistic than a high subscription.** COSTIQ already charges USD 290–490 for implementation. A local "we load your top 30 dishes in one visit" fee of about USD 100–200 matches how consultants are paid and filters out unserious leads.
- **Willingness to pay at USD 100+/month for costing alone in Argentina is not evidenced.** COSTIQ shows no customers. I would treat MarginEdge's USD 350 as irrelevant to local pricing.

### Gaps
- No Argentine survey of willingness to pay for costing software or services.
- No published honorarium rates for Argentine food-cost consultants.
- No churn data for Argentine restaurant SaaS.

---

## Q5. Channel: how to get the first 10–30 paying customers without social-media virality

### Takeaway
The channels that exist and are reachable from Córdoba:
- **direct visits**;
- **the local chambers**: Cámara de Restaurantes y Bares de Córdoba (FEHGRA), AEHGC, Cámara de Bares de Córdoba;
- **food-service distributors** such as Restoshop, and the beverage B2B app BEES (Quilmes);
- **accountants who serve restaurants**;
- **POS resellers and integrators of non-Fudo systems**.

I found no published example of a distributor–software partnership in Argentina. The channel economics need to be tested.

### Cited Findings
- **Córdoba chambers:**
  - the Asociación Empresaria Hotelera Gastronómica de la Provincia de Córdoba (AEHGC) has hotel, restaurant and pastry/alfajor chambers, belongs to FEHGRA's Región Centro and sits on the C20 business council;
  - a separate Cámara de Restaurantes y Bares de Córdoba belongs to FEHGRA;
  - Guillermo Natali was named AEHGC president (date unclear);
  - Alfredo Alberione speaks for the Cámara de Bares de Córdoba (Oct 2026).
  
  — [Infogastronómica](https://www.infogastronomica.com.ar/guillermo-natali-es-el-flamante-presidente-de-aehgc-cordoba/); [Infonegocios, C20](https://infonegocios.info/plus/nacio-el-c20-vamos-a-trabajar-por-la-rebaja-de-costos-pero-no-queremos-subsidios); [Perfil Córdoba](https://www.perfil.com/noticias/cordoba/el-representante-de-los-bares-de-cordoba-por-la-caida-del-consumo-hace-mucho-tiempo-no-se-veia-tan-feo-peor-que-en-pandemia.phtml)
- **Distributor example: Restoshop (Córdoba).** It supplies gastronomic businesses with grocery, dairy, cold cuts, beverages, disposables and sushi or Arabic-cuisine inputs, delivering across Córdoba city and to other provinces. The article is undated. — [Infonegocios](https://infonegocios.info/nota-principal/que-falta-en-el-negocio-restoshop-te-lleva-lo-que-necesitas-a-la-puerta-de-tu-local-desde-descartables-a-materia-prima)
- **BEES (AB InBev/Quilmes) B2B ordering app** for kiosks, grocers and restaurants:
  - "más de 200.000 puntos de venta registrados" and products from 35 other companies (older figures);
  - 95.5% of Quilmes orders go through BEES.
  
  This shows that venues already accept supplier-side apps. — [Infonegocios](https://infonegocios.info/plus/te-gustaria-que-tu-producto-tenga-la-misma-distribucion-que-quilmes-con-la-app-de-bees-ahora-es-posible); [Forbes Argentina](https://www.forbesargentina.com/lifestyle/quilmes-sigue-apostando-bees-su-app-ayudar-crecer-comerciantes-n8478)
- **Accountants:** Argentine accounting tools (e.g., Colppy) already import "Mis Comprobantes Recibidos" from ARCA, so accountants handle the same supplier invoices. — [Colppy help](https://intercom.help/Colppy/es/articles/3181130-importar-tus-facturas-desde-mis-comprobantes-recibidos-afip)
- **Fudo channel competition:** Fudo already offers a WhatsApp AI receptionist and sales agents. Its October 2026 changelog notes that "Desde el 1 de octubre Meta cobra por mensaje en WhatsApp Business API". That is a running cost for any WhatsApp-first product. — [Fudo changelog](https://tools.fu.do/novedades)

### Inferences
- **The best first channel is direct, in-person selling in Córdoba city.** Target 40–60 venues: bodegones, parrillas, pizzerías, cafés with kitchens, pasta and vianda producers, and small chains. Lead with a free "auditoría de margen" (bring last month's invoices; get a report on your 10 best-sellers' real margins). The audit is the demo, and it doubles as onboarding.
- **Chambers:** offer a talk or workshop ("cómo saber qué plato te hace perder plata cuando no podés subir la carta") with a member discount. Chambers want to show value to members in a crisis.
- **Distributors are a second-stage channel, with a conflict of interest.** A distributor will not promote a tool that tells restaurants they overpay that distributor. Better B2B angles:
  - (a) a distributor uses the tool to send structured price lists (a feed of current prices) that pre-fill costs;
  - (b) specialty producers (cheese, pasta, meat) who want to show their product is profitable.
- **Accountants** who serve 10–30 gastronomic clients each could resell or bundle the service with monthly reporting.
- **POS resellers of non-Fudo systems** (Maxirest, Bistrosoft, others): a white-label "invoice-to-cost" module could be sold to them, since they appear to lack AI invoice reading.

### Gaps
- No evidence of an Argentine distributor–software partnership, or of chamber member counts in Córdoba.
- Not found: Córdoba gastronomic accountants (count or names) and POS resellers (count or names) in Córdoba.

---

## Q6. Feasibility for one person in 3–6 months, durability (data moat), risks and kill criteria

### Takeaway
Technically feasible for one person with Claude Code in 2–3 months:
- **easy:** multimodal extraction of Factura A/B/C PDFs and photos;
- **medium:** handwritten remitos and receipts;
- **harder:** matching and unit conversion, which needs human-in-the-loop confirmation.

**The bottleneck is onboarding** (loading recipes) and sales, not code. Durability is weak: Fudo already owns distribution and launched a cross-restaurant price radar (the data moat). Indie apps keep appearing, and switching costs are low until a venue's recipe library is loaded.

### Cited Findings
- **Fudo's own support says** "La IA es una ayuda para agilizar la carga, no reemplaza la revisión final", and it flags empty or possibly wrong fields. Review is required even for the market leader. — [Fudo support](https://soporte.fu.do/es/articles/15707806-como-importar-facturas-mediante-foto-o-pdf-con-ia)
- **Unit and waste handling is table stakes:**
  - Fudo has gram, ml and fl oz units (Dec 2023), waste % per ingredient (Feb 2024) and 3-level sub-ingredients (Jul 2024);
  - COSTIQ costs each dish "con ingredientes, merma y rendimiento" and converts paper recipes from photos.
  
  — [Fudo changelog](https://tools.fu.do/novedades); [COSTIQ](https://www.costiqapp.com/)
- **Onboarding is monetized by competitors:** COSTIQ charges USD 290–490 for implementation and USD 390 per location on its Grupo plan. — [COSTIQ pricing](https://www.costiqapp.com/precios)
- **Data moat already started by the incumbent:** Fudo's "Radar de Precios" (Aug 2026) compares a venue's ingredient prices with other restaurants in the region. It surveyed menu prices of 13,400 Argentine venues in July 2026. — [Fudo changelog](https://tools.fu.do/novedades); [Economis](https://economis.com.ar/del-cafe-a-la-pizza-comer-en-misiones-cuesta-hasta-51-menos-que-el-promedio-argentino/)
- **Sales-mix input:** COSTIQ accepts a POS sales report "aunque sea una foto" to reconcile the Z close. Fudo has product-level margin and markup columns. — [COSTIQ](https://www.costiqapp.com/); [Fudo changelog](https://tools.fu.do/novedades)
- **ARCA:** most e-invoices carry no item detail (WSFEv1), so line-level prices must come from the document image or PDF. Header lists are exportable from Mis Comprobantes. — [ARCA](https://www.arca.gob.ar/ws/documentacion/ws-factura-electronica.asp); [Colppy](https://intercom.help/Colppy/es/articles/3181130-importar-tus-facturas-desde-mis-comprobantes-recibidos-afip)
- **WhatsApp Business API is charged per message by Meta** from 1 Oct 2026, according to Fudo's changelog. — [Fudo changelog](https://tools.fu.do/novedades)

### Inferences
- **Build plan for one person (realistic):**
  - weeks 1–3: WhatsApp intake (photo/PDF), LLM extraction to JSON, a review screen;
  - weeks 4–6: an ingredient catalog with pack-size and unit parser ("x12 1L", "kg", "horma"), fuzzy matching with one-tap confirmation, and a recipe model with waste/yield;
  - weeks 7–9: margin engine, weekly WhatsApp digest, price suggestions with "menu-friendly" rounding, and a CSV or photo import of POS sales;
  - weeks 10–12: ARCA "Recibidos" reconciliation (missing-invoice alerts) and a supplier price history per venue.
  
  Extraction quality on clean PDFs should be high. Handwritten remitos will need correction (inference; no Argentine benchmark found).
- **Onboarding cost is the real cost.** Loading 30 dishes with weights takes about 2–4 hours per venue (estimate). Without a done-for-you setup, self-serve apps see recipes never loaded. That is why a tech-enabled service model, with a paid setup visit plus a subscription, fits a solo founder in Córdoba better than pure self-serve SaaS.
- **Durability is weak:**
  - Fudo can extend its existing AI import to auto-matching and margin alerts;
  - the "city price index" moat is already being built by Fudo with far more data;
  - LLM invoice extraction is commoditized;
  - what does persist: each venue's loaded recipe library, supplier mappings and history (switching cost), plus local relationships and service.
- **Main risks:**
  1. Fudo ships per-dish margin alerts on Avanzado (high probability, in my view);
  2. the crisis cuts subscriptions;
  3. onboarding hours do not scale;
  4. WhatsApp message costs and Meta policy changes;
  5. a well-funded LatAm player (COSTIQ) or an Argentine indie app (InstaCost) moves upmarket.
- **Kill criteria (proposed):**
  - after 20 qualified in-person visits in Córdoba, fewer than **5 venues pay a setup fee**, or fewer than **3 convert** to a paid monthly plan after a 30-day pilot;
  - **more than half** of qualified prospects already use Fudo Avanzado/Pro and say Fudo's AI import is enough;
  - after 4 weeks of real invoices, **less than 90% of line items** are auto-matched correctly (by item count), or onboarding takes **more than 4 hours** per venue;
  - monthly logo churn **above 5%** after month 3;
  - Fudo launches automatic margin alerts with price suggestions on its mid tier before reaching 15 paying customers.

### Gaps
- No accuracy benchmark of LLM extraction on Argentine supplier invoices, remitos or handwritten tickets. It must be tested on 50–100 real documents.
- Fudo's roadmap and public API for exporting sales mix were not checked.
- Current Meta per-message prices for Argentina were not checked.

---

## Q7. Final verdict, scores (1–5), sharpest MVP and pricing hypothesis

### Takeaway
**Verdict: do not pursue this as "the unserved MarginEdge for Argentina". The gap is largely served (Fudo, InstaCost, COSTIQ) and the incumbent is actively closing the rest.** It is viable only as a narrow, service-heavy wedge, and it should be validated with pre-sales before building:
- a done-for-you "margin copilot on WhatsApp" for **non-Fudo, multi-supplier, protein-heavy independents and small chains in Córdoba**;
- or a white-label invoice-to-cost engine sold to **POS vendors that lack it**.

Compared with other candidates in the earlier notes, it should be **downgraded** from a top pick to a "maybe".

### Cited Findings
- The incumbent's feature set (AI invoice import with items, automatic cost updates, ingredient price radar, Avanzado ≈USD 30) — [Fudo pricing](https://fu.do/es-ar/precios/); [Fudo changelog](https://tools.fu.do/novedades)
- A local standalone with the exact core loop at USD 0–20 — [InstaCost](https://instacost.shop/)
- A LatAm standalone with AI alerts and WhatsApp supplier orders at USD 129+ — [COSTIQ](https://www.costiqapp.com/precios)
- **Pain and pricing context:**
  - restaurant inflation of 33.6% year on year (Oct 2026);
  - beef shocks;
  - Córdoba bars freezing menus while suppliers raise prices.
  
  — [Vinetur/INDEC](https://www.vinetur.com/en/20261113111015/argentinas-restaurant-and-hotel-inflation-accelerated-to-15-in-october.html); [Chequeado](https://chequeado.com/el-explicador/la-carne-aumento-casi-el-doble-que-la-inflacion-y-cayo-el-consumo-las-razones-detras-de-este-fenomeno/); [Perfil Córdoba](https://www.perfil.com/noticias/cordoba/el-representante-de-los-bares-de-cordoba-por-la-caida-del-consumo-hace-mucho-tiempo-no-se-veia-tan-feo-peor-que-en-pandemia.phtml)

### Inferences

**Scores (1 = poor, 5 = excellent), with reasons:**

| Dimension | Score | Why |
|---|---|---|
| Unserved / novelty | **1.5** | Core loop exists locally (Fudo AI import + auto cost update; InstaCost; COSTIQ). Only the wedge (auto-matching, margin alerts, WhatsApp intake, non-Fudo venues, ARCA missing-invoice check, done-for-you) is open. |
| Pain | **4** | Real and current: input shocks (beef), frozen menus, 30–40% demand drop. The general-inflation argument is weaker than in 2022–24 (now ~1.5%/month). |
| Willingness to pay | **2** | Suites cost USD 15–60 a month in total, and micro-apps USD 2–20. Crisis budgets. No evidence of Argentine venues paying USD 100+ for costing. A setup fee plus about USD 40–60 a month is plausible only with peso-denominated ROI. |
| Feasibility (solo, 3–6 months) | **4** | Tech is well within reach. Onboarding and in-person sales are the hard part. |
| Durability | **2** | Incumbent with distribution and data (Radar de Precios). Commoditized AI extraction. The moat is only the per-venue recipe library and service relationship. |
| Fit with entrepreneur | **3** | Fits the Claude Code, document-AI and WhatsApp skills and the Córdoba base. Requires heavy field sales and service work, and the market is in recession. |

**Sharpest MVP, if pursued anyway: "Margen al Día" (working name)**
- **Who:** independent restaurants, bodegones, parrillas, pizzerías and cafés with kitchens, plus pasta and vianda producers, in Córdoba city. 1–3 locations, at least 8 suppliers, not on Fudo Pro, and protein- or dairy-heavy menus.
- **Setup (done for you, one visit plus remote follow-up):** load the top 20–30 dishes by sales (Pareto) from the owner's notes or photos, with waste and yield. Map current suppliers. Import last month's sales mix from a POS export or a photo of the Z report.
- **Daily loop (WhatsApp only):**
  - the owner, manager or cashier forwards every supplier invoice or remito (photo or PDF);
  - the bot replies within minutes with changes only: "Muzzarella +12% vs. última compra (Lácteos X). Afecta 6 platos.";
  - new items get one-tap confirmation.
- **Weekly digest (Monday):**
  - the 5 dishes whose margin fell below the owner's target;
  - for each, a suggested new price (menu-rounded) or alternatives (portion, supplier, recipe tweak);
  - the supplier with the biggest increase;
  - an **ARCA "Recibidos" reconciliation**: invoices in ARCA but not sent to the bot (header list exported with the owner's consent).
- **Out of scope for the MVP:** stock counts, POS replacement, orders to suppliers.

**Pricing hypothesis to test:**
- **Setup:** ARS 150,000–250,000 one-time (≈USD 100–160), credited if the venue stays 6 months.
- **Monthly:** ARS 60,000–90,000 per location (≈USD 40–60). That is above Fudo Avanzado's whole suite (≈USD 30), so it must be sold as a service with a guaranteed peso saving. Fallback: ARS 35,000–45,000 for a WhatsApp-only "alerts" tier.
- **Unit economics to USD 1,000/month net:** about 25–30 venues at about USD 45 (after LLM, WhatsApp and hosting costs, estimated at under USD 5 per venue per month; not sourced), or fewer venues plus a steady flow of setup fees.

**Validation plan (6 weeks, before writing much code):**
1. Visit 20 qualified venues with a manual "auditoría de margen" (done with Claude plus a spreadsheet).
2. Record: POS used (especially Fudo tier), number of suppliers and invoices per month, current costing method and update frequency, and reaction to the price.
3. Pre-sell 5 setups. If the kill criteria in Q6 are hit, stop.

**Alternative wedge to test in parallel (B2B):**
- Offer the invoice-to-cost engine as a white-label or API module to non-Fudo POS vendors (Maxirest, Bistrosoft, OrdenApp, Restoo, Frambuesa), or to accountants with gastronomic clients.
- One signed POS partner could deliver more venues than months of door-to-door selling, and it avoids competing head-on with Fudo.
- This is an inference; it is not validated.

### Gaps
- No primary interviews yet. Every score on willingness to pay and fit is based on desk research.
- Fudo's real behaviour on its Avanzado plan (whether AI-imported items recalculate recipe margins and whether any alerting exists) should be checked hands-on with a trial before any build decision.
- The non-Fudo POS vendors' interest in a white-label module is untested.
