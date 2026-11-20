# AI for Argentina's physical economy: unserved problems a solo builder can tackle (phone camera + multimodal AI + documents + cheap sensors)

Scope note: research done on 2026-11-20. About 26 searches and fetches. Sources are mostly 2025–2026; older data is marked. Several Argentine news pages (iProfesional, Ámbito) show page dates that look like crawl or update dates, not publication dates, so treat those dates with care. "Inference" means my own reasoning, not a sourced fact. Prices in USD are taken from the cited pages. Any per-client economics are illustrative and say so.

Ranking from this pass (strongest first):
1. **A. Energy contract and bill copilot for the ~6,000 mid-size electricity users (GUDI) pushed into the new wholesale market by Res. SE 400/2025 and 293/2026.** This is new, painful and growing until 2029, and I found no dedicated tool.
2. **B. Supplier invoice photo → live recipe and dish costing for Argentine gastronomy.** This is "MarginEdge for Argentina". It is proven abroad at USD 350/month, and I found no confirmed local equivalent.
3. **C. Trades quoting copilot (electricians, plumbers, gas fitters, painters).** It builds a quote from photos and a voice note, using local prices. US equivalents raised VC money; I found none for Argentine trades.
4. **D. Buyer-side used-car condition report for private sales.** The phone guides the buyer through photos, engine sound and a cheap OBD-II dongle. The market is huge, but the moat is weak and partial competitors exist.
5. (Weaker / to validate) **E. Proof-of-work and billing for contratistas rurales**, and **F. maintenance-compliance evidence for consorcios in CABA**.

Screened out as crowded, small or regulation-risky: livestock weighing by photo, solar sizing from roof photos, vehicle history reports, insurer photo self-inspection, and front-of-pack food labeling tools (details in the last questions).

---

## Q1. Candidate A: Is there an unserved gap in helping mid-size Argentine companies (GUDI, ≥300 kW) understand, reconcile and optimize electricity contracts and bills under the new wholesale-market rules?

### Takeaway
Yes, and it is the strongest candidate. Since November 2025 (Res. SE 400/2025), about 6,000 companies with ≥300 kW per supply point must manage energy contracting themselves. According to the pyme industry group IPA, only about 800 had signed contracts by September 2026. Some bills rose up to 4x, and contracted firms report final costs near 2x the agreed price because of extra charges. Res. 293/2026 (21 Oct 2026) adds more options and a rising contract schedule to 2029. I found no product that reads these bills and contracts and reconciles them. The work is document understanding (bills, CAMMESA settlements, generator invoices) plus optional cheap metering, and one person can build it.

### Cited Findings
- Res. SE 400/2025 approved the "Reglas para la Normalización del MEM y su Adaptación Progresiva". It was published 21 Oct 2025 and applies to wholesale market (MEM) transactions from 1 Nov 2025. It allows direct contracting of fuel and renewable costs and creates term markets for energy and power between generators, distributors and large users. — [Marval O'Farrell Mairal](https://www.marval.com/publicacion/mercado-electrico-mayorista-normalizacion-y-modernizacion-17371); [Res. 400/2025 official text](https://www.argentina.gob.ar/normativa/nacional/norma-413535/texto); [Cassagne / abogados.com.ar](https://abogados.com.ar/la-resolucion-se-4002025-y-la-normalizacion-del-mem/37804)
- Res. 400/2025 defines large distributor users (GUDI) as demand with ≥300 kW contracted power per supply point. Passing 300 kW does not automatically make a company a GUMA or GUME; it must meet further technical, commercial and administrative requirements. — [iProfesional, 21 Oct 2026](https://www.iprofesional.com/negocios/467105-el-gobierno-acelera-la-apertura-del-mercado-electrico-para-empresas)
- Res. 293/2026 (Boletín Oficial, 21 Oct 2026) gives a GUDI three options: (1) stay with the distributor's supply, (2) contract energy and power with one or more generators through the distributor acting as comercializadora or aggregator, or (3) become an MEM agent. Entry windows for GUMA/GUME become monthly from 1 Dec 2026. Generator contract limits in the term market rise to 60% on 1 Apr 2027, 80% on 1 Jan 2028 and 100% on 1 Jan 2029. CAMMESA must publish new forms, calendars and deadlines. — [iProfesional, 21 Oct 2026](https://www.iprofesional.com/negocios/467105-el-gobierno-acelera-la-apertura-del-mercado-electrico-para-empresas)
- Industriales Pymes Argentinos (IPA) said in September 2026:
  - about 6,000 companies are covered by the scheme, and only about 800 signed supply contracts;
  - some non-contracting firms saw bills multiply by up to 4;
  - some contracting firms report charges that pushed the final cost close to double the agreed price;
  - there are contract disputes with generators.
  
  IPA asks authorities to review cases where billed values differ a lot from contracted values. Quote: "Estamos obligando a una PyME a convertirse de un día para otro en especialista en contratación energética." — [El Economista, 29 Sep 2026](https://eleconomista.com.ar/energia/la-letra-chica-energia-pymes-denuncian-pagan-doble-lo-acordado-n98498)
- Headlines confirm the pain: "Las tarifas de la luz se multiplicaron por cuatro para la industria y asfixian a las PyMEs" — [Perfil](https://www.perfil.com/noticias/economia/tarifas-luz-multiplicaron-cuatro-industria-asfixia-pymes-a40.phtml); "Tarifas eléctricas cuadruplicadas desde noviembre asfixian a pymes" — [Mundo Empresarial](https://mundoempresarial.ar/?p=51767); IPA warns the new scheme "multiplica costos, endeuda a las PyMEs" — [Conclusión](https://www.conclusion.com.ar/?p=1457983)
- A September 2025 Secretaría de Energía resolution enabled term contracts in the MEM. — [Boletín Oficial, 26 Sep 2025](https://www.boletinoficial.gob.ar/detalleAviso/primera/331990/20250926?busqueda=1)
- A GIZ guide (published January 2026) explains to industrial users how to buy electricity in Argentina (Compras Conjuntas, MATER renewable term market, GUDI/GUME definitions). This shows the subject is complex enough to need explaining. — [GIZ guide](https://www.giz.de/sites/default/files/media/pkb-document/2026-01/giz2025-es-guide-guia-de-acceso-energia-electrica-para-la-industria-en-argentina.pdf)
- Older baseline: in 2018–2024, non-residential users under 300 kW spent on average 0.77% of revenue on electricity. This is older data from before the reform. — [UBA-IIEP report](https://www.economicas.uba.ar/iiep/wp-content/uploads/InformeEspecial_IncidenciaCosto-Electrico.pdf)
- Analog abroad: in Spain, SME bill-audit and comparator services are a mature category. They work on contracted power, reactive-energy penalties and tariff choice. For example, above 15 kW a penalty applies if reactive energy exceeds 33% of active energy, and a penalty applies if demand exceeds 105% of contracted power. — [tarifasgasluz.com](https://tarifasgasluz.com/pymes/energia-reactiva); [Selectra](https://selectra.es/energia/empresas/energia-reactiva); [comparadorluz.com](https://comparadorluz.com/empresas/reducir-factura)
- Competitor search: the queries "Resolución 400/2025 … asesoramiento consultora pymes" and "GUDI GUME contratos energía pymes asesoramiento gestión facturas CAMMESA comercializador 2026" found no company or software offering GUDI bill or contract reconciliation. The only intermediary named in the sources is the distributor acting as optional comercializadora or aggregator. — [iProfesional](https://www.iprofesional.com/negocios/467105-el-gobierno-acelera-la-apertura-del-mercado-electrico-para-empresas); [El Economista](https://eleconomista.com.ar/energia/la-letra-chica-energia-pymes-denuncian-pagan-doble-lo-acordado-n98498)

### Inferences
- **Product idea.**
  - The company uploads, or forwards by email or WhatsApp, its distributor bill, any generator or comercializador invoice, the contract PDF and its monthly demand data.
  - A multimodal model pulls out each charge and the contracted energy and power.
  - The software compares "contracted vs billed", flags demand peaks and penalties, simulates the three GUDI options from Res. 293/2026, and drafts a claim letter or a monthly report for the owner.
  - An optional cheap clamp-on meter would give the load curve.
  
  This is "document understanding + cheap sensor + software" with no hardware manufacturing.
- **Who pays and how much (illustrative, not sourced).**
  - A plant with 300 kW contracted at a 40% load factor uses about 300 × 730 h × 0.4 ≈ 87,600 kWh/month. Even at a few US cents per kWh, the bill is in the thousands of USD per month.
  - Saving 3–5% on that bill is worth hundreds of USD per month, so a fee of about USD 100–300 per supply point per month, or a share of verified savings, looks plausible.
  - About 10 clients would pass USD 1,000/month net. The addressable base is about 6,000 firms by IPA's count, plus smaller users who may follow.
- **Why it can last.**
  - The rules keep changing through 2029, and each new resolution brings new forms and calendars.
  - Each client builds up a history of bills and contracts, which makes switching away costly.
  - A library of tariff schedules and bill formats for each distributor is tedious to build. That is a real data moat for a first mover.
- **Confidence that nobody serves it: medium–high** for a self-serve AI product. **Medium** if you count human energy consultancies and law firms, which surely exist but did not appear in my searches. The distributors acting as comercializadoras could also bundle simple advice.
- **Feasibility in 3–6 months for one person: high** for bill and contract extraction, reconciliation and alerts. **Medium** for an optimizer of contract volumes, which needs domain knowledge; a partner engineer could help. This is not legally regulated professional judgment, but contract advice should carry disclaimers, and claims against generators may need a lawyer.
- **Risk:** the political direction could change, or the government could simplify the scheme. Today the documented trend points the other way (more bilateral contracting through 2029).

### Gaps
- No exact count of GUDI supply points from an official source. The 6,000 figure comes from IPA, an interest group.
- I did not obtain sample bills or CAMMESA settlement documents, so I could not check how messy the formats are.
- I did not find energy consultancies by name or their fees (a suggested next query is "consultoría energética grandes usuarios MEM"). I did not search Product Hunt, YC or app stores for this candidate.
- I did not find typical savings percentages for Argentina.

---

## Q2. Candidate B: Is there an unserved gap for automatic dish costing from supplier-invoice photos in Argentine restaurants, cafés and bakeries?

### Takeaway
Probably yes. Prices in Argentina change fast, so a dish costing from two months ago is already out of date, and small venues cost dishes by hand or not at all. The proven foreign product (MarginEdge) costs USD 350/month per location and does exactly "photo of invoice → updated recipe cost". Local POS systems such as Fudo track stock, but I could not confirm that they read invoices or update dish costs automatically. I found no Argentine product that does it. Confidence that nobody serves it: medium.

### Cited Findings
- Restaurant prices rose almost 68% year on year, according to INDEC as quoted by iProfesional. The page date (25/8/2026) may be a crawl date, so verify. — [iProfesional](https://www.iprofesional.com/negocios/360877-menu-complicado-como-pega-la-inflacion-en-los-restaurantes)
- An Argentine costing calculator warns that "con inflación, el costeo de hace 2 meses ya no sirve". It says indirect costs (gas, electricity, packaging) add 5–12% to the cost per portion, and that waste must be counted. — [hacecuentas.com](https://hacecuentas.com/calculadora-costo-receta-precio-por-porcion)
- A 2026 field study from Universidad Nacional de Tucumán (UNT) on pastry shops and cafés in Argentina says the sector faces significant difficulties in managing costs and contribution margins. — [UNT/FACE, Feb 2026](https://face.unt.edu.ar/web/iadmin/wp-content/uploads/sites/2/2026/02/24-Figueroa-Angeles-Fiorella-Trabajo-de-Campo_compressed.pdf)
- Sector stress (headlines): "Gastronomía rosarina en modo supervivencia: menos rentabilidad, más costos…" — [La Capital](https://www.lacapital.com.ar/negocios/gastronomia-rosarina-modo-supervivencia-menos-rentabilidad-mas-costos-y-una-receta-no-cerrar-n10270966.html/amp); "La batalla del ticket medio: ingeniería de costos…" — [Forbes Argentina](https://www.forbesargentina.com/negocios/la-batalla-ticket-medio-ingenieria-costos-previsibilidad-defender-rentabilidad-gastronomia-n99731)
- MarginEdge (US):
  - It takes a photo, email or EDI of each invoice; AI pulls out the data in 24–48 h, and recipe costs update with current prices.
  - The official site lists USD 350/month per location, with unlimited invoice processing.
  - Older reviews list USD 330, and a Freepour tier costs USD 480.
  
  — [MarginEdge](https://www.marginedge.com); [MarginEdge how it works](https://www.marginedge.com/how-it-works); [FitSmallBusiness review](https://fitsmallbusiness.com/marginedge-review/)
- xtraCHEF (Toast) also captures purchases from invoices and builds recipes, but it is tied to the Toast and US ecosystem. — [Toast support](https://support.toasttab.com/es-US/article/xtraCHEF-101)
- Kitchio is described as analyzing supplier invoices with AI, updating costs after confirmation, and computing cost per portion and a target price. It is listed on a Product Hunt-style site; its market and language are unclear. — [huntscreens](https://huntscreens.com/es/products/kitchio)
- Fudo, an Argentine restaurant POS, says it updates stock with each sale or expense. International plans are listed at USD 35 (Avanzado) and USD 45 (Pro) per month. Its recipe/escandallo module and any invoice reading were not confirmed, and one review complains about how recipes are defined. — [TrustRadius](https://www.trustradius.com/products/fudo/details); [Capterra AU](https://www.capterra.com.au/software/1023879/fudo); [ComparaSoftware](https://www.comparasoftware.com/fudo)
- Competitor search: "app costeo recetas gastronomía Argentina cargar facturas proveedores actualiza costo plato" found no Argentine app that confirms invoice upload with automatic dish-cost updates. The results were foreign (Kitchio, xtraCHEF, Recipe Costing, ChefPRO, Fillet, Control Receta). — [Capterra AR, Kitchen Porter alternatives](https://www.capterra.com.ar/alternatives/112109/kitchen-porter-tech); [Fillet App Store](https://apps.apple.com/us/app/fillet-%EC%9A%94%EB%A6%AC-%EC%82%AC%EC%9A%A9-%EB%A0%88%EC%8B%9C%ED%94%BC-%EB%B9%84%EC%9A%A9/id696313628?l=es-MX)

### Inferences
- **Product idea.**
  - The owner or chef photographs or forwards each supplier invoice (factura A/B/C or a remito) by WhatsApp.
  - The model pulls out each line item and matches it to the ingredient list. The owner confirms new matches once.
  - Every recipe re-costs automatically, and a weekly alert says "these 5 dishes fell below your target margin; suggested new price X".
  - A phone photo of the kitchen shelf could later be used for a rough inventory count.
- **Why Argentina is a good fit.**
  - Inflation makes the problem more urgent than in the US.
  - Argentine invoices are standardized electronic invoices (CUIT, tipo A/B/C, CAE), which makes extraction easier.
  - My understanding is that ARCA's "Mis Comprobantes" gives invoice totals but not line items. If so, a photo or PDF is still needed for ingredient-level prices, which is the opening for multimodal AI. This is not verified (see Gaps).
- **Pricing (illustrative):** local POS pricing is about USD 35–45/month and MarginEdge is USD 350, so USD 20–50 per location per month looks realistic. About 30–50 paying venues would reach USD 1,000/month net.
- **What makes it last:**
  - each venue's supplier-to-ingredient mapping and recipe library;
  - a city-level price history of gastronomic inputs built up across clients, a data asset no single venue has. Selling or benchmarking with it requires care with privacy and consent.
- **Risks:** Fudo or another local POS (for example Maxirest; not researched) could add the feature, or a foreign player like Kitchio could localize. The product needs to plug into the POS for real per-dish margins.
- **Feasibility in 3–6 months: high.** Invoice extraction from photos is a strong use case for current multimodal models. Matching items to ingredients needs a human-in-the-loop confirmation step.

### Gaps
- No count of gastronomic venues in Argentina (FEHGRA or CAME data was not found in this pass).
- I did not verify whether ARCA "Mis Comprobantes" exposes line items. My inference is that it does not; check before relying on it.
- Fudo's and Maxirest's current recipe-costing features and Argentine prices are unconfirmed. I did not search Portuguese or Brazilian equivalents.
- Willingness to pay among small venues was not measured; it needs interviews.

---

## Q3. Candidate C: Is there an unserved gap for an AI quoting copilot for Argentine tradespeople (electricians, plumbers, gas fitters, painters, small renovation firms)?

### Takeaway
There is a visible gap in LatAm. AI quotes from photos are funded and selling in the US (Handoff, YC-backed, USD 25M+ raised, from USD 149/month) and appear in Spain (Presugenix). The only LatAm tool I found (OneEstimate) targets civil-works cost breakdowns, not trades. Argentina has a large self-employed base and a shortage of skilled trades. Willingness to pay among informal tradespeople is the main risk, so a business-to-business route (renovation firms, building maintenance companies, or hardware stores paying for the tool) may work better. Confidence that nobody serves it: medium.

### Cited Findings
- Handoff:
  - It is an "AI estimator & agent for remodelers" and has raised USD 25M+ from Y Combinator, Initialized and Greycroft.
  - It builds estimates from a description, a scope document or photos.
  - The starting plan is USD 149/month (Software Advice), with other listed tiers at USD 199, 299 and 899.
  
  — [YC company page](https://ycombinator.com/companies/handoff); [YC jobs](https://www.ycombinator.com/companies/handoff/jobs); [Software Advice](https://www.softwareadvice.com/product/525070-Handoff/reviews/); [GetApp](https://www.getapp.com/construction-software/a/handoff/)
- SimplyWise does quick residential quotes from photos (US). Presugenix targets tradespeople in Spain who take a long time to write each quote by hand. — [ContractorPlus comparison](https://contractorplus.app/es/blog/estimatic-ai-vs-handoff-ai-vs-simplywise-which-is-best-for-growing); [Product Hunt: Presugenix](https://www.producthunt.com/p/presugenix)
- OneEstimate uses AI trained for construction in Latin America, but it focuses on civil-works cost breakdowns (APU), not trades. — [OneEstimate](https://oneestimate.ai/en/blog/inteligencia-artificial-presupuestos-construccion)
- Partial local competitor: servidos.ar has a free "estimador de presupuesto IA" that gives price ranges for trades in Buenos Aires. It is aimed at homeowners, and its page metadata looks odd, so verify it. — [servidos.ar](https://servidos.ar/estimador-presupuesto-ia)
- Labor-market size: in Q3 2025, 24.5% of employed people in the urban survey (EPH-INDEC) were self-employed, up from 2.3M (2016) to 3.3M (2025) self-employed workers. Informality was 63.3% among the self-employed in Q4 2025. — [El Economista](https://eleconomista.com.ar/economia/record-cuentapropismo-argentina-adaptacion-heroica-o-senal-alarma-mercado-laboral-n92856); [Letra P](https://www.letrap.com.ar/economia/el-mercado-laboral-la-argentina-milei-el-cuentapropismo-representa-el-245-los-empleos-urbanos-n5421972/amp); [La Gaceta](https://www.lagaceta.com.ar/nota/1134500/economia/alarma-laboral-cuentapropismo-volvio-niveles-pandemia-desplazo-al-empleo-calidad.html)
- A World Bank/INDEC report notes a 25% deficit of specialized workers, including plumbers and masons. The shortage raises the cost of household services. — [Infobae, 1 Feb 2026](https://www.infobae.com/economia/2026/02/01/la-escasez-de-trabajadores-tecnicos-calificados-eleva-los-costos-de-servicios-basicos-para-el-hogar/); [Crónica, Nov 2025](https://www.cronica.com.ar/sociedad/El-nuevo-mapa-del-empleo-informal-oficios-con-alta-demanda-y-buena-remuneracion-pero-sin-trabajadores-jovenes-20251106-0088.html)
- Competitor search: "presupuesto con IA desde fotos app electricistas plomeros oficios Latinoamérica" found no LatAm app for trades. The results were US or Spain tools, OneEstimate and servidos.ar. — sources above.

### Inferences
- **Product idea.**
  - The tradesperson sends 3–6 photos and a voice note on WhatsApp ("cambiar tablero, 8 bocas, cable de 2,5…").
  - The AI drafts a branded PDF quote with materials (quantities and current prices), labor, validity in days (important with inflation) and payment terms.
  - It follows up with the client, and turns the quote into a work report with before/after photos when the job is done.
- **Business-model twist (inference).** Hardware stores (corralones, ferreterías, casas de electricidad) could pay for the tool. The materials list links to their catalog and stock, so each quote becomes a materials order. That solves low willingness to pay among informal workers and gives a price feed.
- **Durability:** a database of local labor and materials prices built from many quotes, plus each tradesperson's history of quotes and clients. A generic chatbot could do part of this, so speed and a workflow on WhatsApp matter.
- **Licensed work.** Gas and some electrical work must be signed by a matriculado (gasista matriculado; electrician declarations in some jurisdictions). The tool supports the licensed professional and does not replace them, which fits the ethics constraint.
- **Feasibility in 3–6 months: high** for photo + voice → structured quote. **Medium** for accurate quantity estimates from photos; a human confirmation step is needed.

### Gaps
- No count of electricians, plumbers or gas fitters by trade (EPH tables by branch were not found). I did not verify registered-professional counts (e.g., APSE, ENARGAS registries).
- I did not search Brazilian Portuguese equivalents ("orçamento com IA eletricista") or Google Play. App-store search was limited to what surfaced in web search.
- Willingness to pay of Argentine tradespeople and hardware stores' interest are unknown and need interviews.

---

## Q4. Candidate D: Is there an unserved gap for a buyer-side, phone-guided condition report for private used-car sales in Argentina?

### Takeaway
The market is huge: a record 1,887,024 used-car transfers in 2025. Parts of the problem are served: vehicle-history reports (Datacar, Veraz Auto), insurers' photo self-inspections (B2B, done in-house) and in-person pre-purchase inspections (Autoficina, Kavak's 240-point check). I found no self-serve product where the buyer's phone guides a structured inspection and produces a report and a list of points to negotiate. The physical-condition gap is real, but competitors could copy it easily and liability needs careful framing. Confidence that nobody serves it: medium. Durability: medium–low.

### Cited Findings
- 2025 was a record year: 1,887,024 used-vehicle transfers (+8.12% vs 1,745,335 in 2024), beating the 2013 record (1,855,032), according to the CCA (Cámara del Comercio Automotor). There were 918,404 transfers in H1 2025 (+24.2%). Top models: VW Gol/Gol Trend (104,581) and Toyota Hilux (74,097). — [El Economista](https://eleconomista.com.ar/autos/la-venta-autos-usados-alcanzo-su-record-historico-2025-n91863); [Ámbito](https://www.ambito.com/economia/la-venta-autos-usados-cerro-2025-record-historico-que-modelos-lideraron-el-ranking-y-cuales-son-las-provincias-que-mas-operaciones-tuvieron-n6232950/amp)
- Vehicle history reports already exist in Argentina. Datacar ("el primer informe de historial automotor de autos usados de Argentina") reports more than 3 million reports. Veraz Auto pulls data from several verified sources. Autofact works in Chile only. — [Cronista: Datacar](https://www.cronista.com/infotechnology/entreprenerds/datacar-asi-no-vas-a-comprar-nunca-mas-un-auto-usado-con-sorpresa-la-idea-ya-vale-25-m/); [Forbes Argentina: Veraz Auto](https://www.forbesargentina.com/innovacion/como-funciona-verazauto-innovadora-solucion-minimiza-fraude-compra-autos-usados-n37717); [Autofact](https://www.autofact.cl/sobre-nosotros)
- Insurers already run photo self-inspections:
  - La Caja: photos uploaded online and reviewed by an inspector within 48 h;
  - iúnigo: app photos assessed with a digital system;
  - Provincia Seguros: digital inspection since 2020;
  - La Segunda: four photos to assess the vehicle body (2026 note).
  
  — [Mercado: La Caja](https://mercado.com.ar/protagonistas/la-caja-lanza-contratacion-de-seguro-automotor-100-online); [iProUP: iúnigo](https://www.iproup.com/innovacion/1742-iunigo-que-beneficios-traen-los-seguros-para-autos-4-0); [BAE Negocios: Provincia Seguros](https://www.baenegocios.com/amp/Provincia-Seguros-lanzo-un-nuevo-sistema-de-inspeccion-digital-para-el-ramo-Automotores-20201023-0031/); [Cronista: insurers using AI](https://www.cronista.com/infotechnology/innovacion-it/las-aseguradoras-argentinas-que-usan-ia-para-vender-prevenir-y-resolver-mas-rapido); a vendor named "Autoinspector" is listed on [CB Insights](https://www.cbinsights.com/company/autoinspector).
- In-person pre-purchase checks: Autoficina runs a 140-point mechanical and electronic inspection at home. Kavak offers a 240-point certified mechanical and legal evaluation at a physical location (Abasto Shopping) for private sellers. Prices were not published. — [La Capital](https://www.lacapital.com.ar/motores/control-mecanico-las-claves-una-inversion-segura-autos-usados-n10226500.html); [Kavak AR](https://www.kavak.com/ar/lp/autos-usados-particular)
- Global AI damage apps exist but say their results are informational only (e.g., Inspectrai). Avis Budget's AI inspection pilot found 22% more dents and scratches than manual inspection. — [Inspectrai App Store](https://apps.apple.com/app/id6760018980); [Digital Trends ES](https://es.digitaltrends.com/autos/alquiler-carros-inteligencia-artificial/)
- Decreto 196/2025 changed the national traffic law and the vehicle inspection (VTV) rules. — [La Nación](https://www.lanacion.com.ar/autos/cambios-en-la-vtv-que-modifico-el-gobierno-y-como-funciona-en-otros-paises-nid19032025/)
- Competitor search: "inspección vehicular con inteligencia artificial fotos app Argentina usados" found no Argentine buyer-side AI inspection app. — [search results summarized above](https://noticias.autocosmos.com.ar/2024/07/04/la-inteligencia-artificial-ya-hace-las-revisiones-vehiculares)

### Inferences
- **Product idea.** A guided capture: the buyer's phone walks them through about 30 shots, under-hood photos, a cold-start video with engine sound, tire tread, and odometer and document photos (cédula, VTV, título). An optional cheap ELM327 OBD-II dongle reads fault codes. The product:
  - cross-checks the documents with a history report (Datacar or the official dominio report);
  - outputs a risk score, "points to have a mechanic confirm", and a list of negotiation points with estimated repair costs.
- **Sell it as an assistant, not a peritaje.** That avoids professional-liability claims.
- **Business-to-business variant (inference).** Dealers and agencies (like a concesionario's used-car desk) attach a standardized condition report to their Mercado Libre listings to build trust. This is likely easier to monetize than one-off consumer reports.
- **Weak moat.** Mercado Libre, Kavak, Datacar or insurers' vendors could add this quickly. Durable value would need a large photo and outcome dataset (e.g., which defects later cost money), which takes years.
- **Feasibility:** **high** for guided capture, document checks and an OBD fault-code read. **Medium–low** for reliable detection of hidden damage from photos; paint-thickness gauges or a mechanic are still needed. That limits the "replace expensive manual work" promise.

### Gaps
- No published prices for pre-purchase inspections in Argentina (searched; none found). I could not size how much buyers pay today.
- I did not verify Datacar's or Veraz Auto's current prices, or whether they offer condition (not just history) reports.
- I did not search the Brazilian market (e.g., "vistoria cautelar app"), where pre-purchase inspection is a known category and could hold competitors that might move into Argentina.

---

## Q5. Secondary candidates (weaker evidence or partly served): contratistas rurales and consorcio compliance in CABA

### Takeaway
- **Contratistas rurales** do most field work in Argentina and are often paid in kind. Partial digital solutions exist (Malevo marketplace and payments, FinnApp/Finnegans work orders, Sima). An AI-native "parte de trabajo" from WhatsApp photos, voice and machine files is a possible niche, with low–medium confidence that it is unserved.
- **Consorcios in CABA** face growing compliance duties: an annual sworn statement, tank and water analysis, the "Edificio Seguro" certification and new 2026 sanctions. I could not verify competing software in this pass, so it remains a lead to validate.

### Cited Findings
- Contratistas:
  - A Bolsa de Comercio de Rosario (BCR) report by Julio Calzada, using 2016/17 data (old), attributes to contractors 90% of grain harvest, 70% of seeding and 70% of spraying.
  - FACMA (the contractors' federation) estimates at least 70% of farm work.
  - FACMA counts 10,000–11,000 contractors, about 4,100 of them members; another 2026 note says about 18,000 contractor firms.
  - Contractors often charge a percentage of the harvest.
  
  — [BCR](https://www.bcr.com.ar/es/print/pdf/node/72323); [Agrofy News](https://news.agrofy.com.ar/noticia/215080/argentina-hay-18000-empresas-contratistas-contratista-argentino-es-optimista-primera); [Sitio Andino, Aug 2026](https://www.sitioandino.com.ar/economia/contratistas-rurales-el-motor-silencioso-del-campo-argentina-n5719215); [Bichos de Campo](https://bichosdecampo.com/jorge-scoppa-representa-a-un-actor-clave-del-agro-tenemos-que-cuidar-al-contratista-porque-es-unico-en-el-mundo/)
- Existing tools for contractors:
  - Malevo connects producers and contractors and processes payments; it plans Brazil and Paraguay ("el Uber argentino de los contratistas").
  - FinnApp Agro handles work orders and integration with contractors.
  - Sima has generated more than 650,000 work orders and focuses on crop monitoring.
  - GesCon and GestAgro are academic prototypes.
  
  — [Infocampo](https://www.infocampo.com.ar/agtech-de-exportacion-el-uber-argentino-de-los-contratistas-planea-llegar-a-brasil-y-paraguay/); [iProfesional AgTech](https://www.iprofesional.com/tecnologia/436263-agtech-argentina-transforma-el-agro-y-se-expande-en-la-region); [FinnApp Agro](https://apps.apple.com/il/app/finnapp-agro/id6478776871); [Bichos de Campo: Sima](https://bichosdecampo.com/el-caso-sima-agro-agustin-rocha-explica-como-funciona-la-aplicacion-que-creo-para-ahorrar-tiempo-en-el-monitoreo-y-que-anos-despues-llego-a-asociarse-con-la-nasa); [UNLPam GesCon](https://cerac.unlpam.edu.ar/index.php/Vetec/article/download/6637/7252/27434)
- Consorcios (CABA):
  - Ley 941 requires registration in the public registry of building administrators.
  - Disposición 882/2025 set an annual sworn statement for each building (1 Mar–30 Nov 2025), with a certificate per building.
  - Disposición 1129/DGDYPC/26 (Feb 2026) covers deadlines, notices to owners, sanctions and a complaint channel.
  - Ley 6040 requires a tank cleaning and disinfection plan and at least one bacteriological and physical-chemical water analysis per year.
  - The "Edificio Seguro" certification (Disp. 5363/2010, modified 411/11) covers tanks, elevators, facade and fire protection.
  - Disp. 521/2025 requires attaching the manual of good practices to the expensas statements.
  
  — [Boletín Oficial CABA, Disp. 882/2025](https://boletinoficial.buenosaires.gob.ar/normativaba/norma/778884); [Liga del Consorcista, Disp. 1129/2026](https://ligadelconsorcista.org/caba-administradores-obligaciones-disposicion-1129-2026); [Liga del Consorcista, Edificio Seguro](https://ligadelconsorcista.org/legislacion/certificaci-n-edificio-seguro-los-consorcios-disp-53632010-defensa-del-consumidor-la); [Derecho en Zapatillas](https://www.derechoenzapatillas.com/amp/2025/consorcios-deberan-incluir-manual-y-reglamento-en-las-expensas/); [CABA manual de prácticas consorciales 2026](https://static.buenosaires.gob.ar/sites/default/files/2026-06/manual%20de%20practicas%20consorciales.pdf)

### Inferences
- **Contratistas.** The paperwork pain is in turning machine data and field notes into an invoice and a settlement in kind (grain and hectares). A WhatsApp agent that turns photos of the monitor or yield screen, voice notes and exported files into a signed work report and invoice is plausible. But Malevo and the farm ERPs are close, so the gap is narrower than candidates A–C.
- **Consorcios.** A "compliance evidence" app could work like this:
  - the encargado or provider photographs the tank cleaning, the fire extinguisher label or the elevator log;
  - the AI checks dates and certificates, keeps a calendar of due dates, and builds the yearly evidence pack for the sworn statement and for owners.
  
  Administrators would pay per building. Existing consorcio software (which I could not verify here) may already cover calendars, so the AI evidence check would be the difference.

### Gaps
- I did not verify consorcio software competitors or their features (suggested queries: "software administración de consorcios", "app consorcio vencimientos certificados"). I have no count of buildings or administrators in CABA.
- I have no pricing of Malevo or FinnApp, and no count of contractors using digital tools.

---

## Q6. Which commonly suggested ideas are already crowded, too small or too risky (screened out)?

### Takeaway
Livestock weighing by photo or drone already has several players operating in Argentina or the region. Solar sizing from roof photos targets a very small market (about 3,300 distributed-generation connections nationwide by Sept 2025). Vehicle history and insurer photo inspection are served. Tools for front-of-pack food labels face a government push to repeal the law. Hail-claim tooling in Argentina could not be evidenced in this pass.

### Cited Findings
- Livestock weighing and condition by image:
  - Beefie (Agroninja, Hungary) estimates weight from one side photo in about 40 s on Android, calibrated on Nelore cattle.
  - Tuul.ai (Brazil) estimates weight from a smartphone photo.
  - GanaderIA (Uruguay) "ya funciona en Uruguay y Argentina", using drone images with about 5% error, and reports head count and individual weight.
  - Ganader does automatic counting.
  - Young founders in the southwest of Buenos Aires province built an offline phone app for body-condition scoring (YOLOv8).
  
  — [Compre Rural](https://comprerural.com/app-permite-a-pesar-o-gado-pelo-celular-e-com-apenas-uma-foto-video/); [Agrolatam](https://www.agrolatam.com/tecnologia-latam/ganaderia-drones-inteligencia-artificial-pesaje-sudamerica/); [Infocampo](https://www.infocampo.com.ar/?p=604237); [Revista FAPESP](https://revistapesquisa.fapesp.br/es/el-peso-de-la-res/)
- Distributed generation (solar on rooftops):
  - 2,792 user-generators totaling 73.67 MW (May 2025);
  - 3,306 projects connected by end of Sept 2025, with 343 distributors or cooperatives registered on the national platform;
  - in Feb 2025: 1,426 residential and 970 commercial or industrial.
  - The regime was modified in July 2025 and extra charges were prohibited.
  
  — [MASE / LM Neuquén](https://mase.lmneuquen.com/energia/generacion-distribuida-mas-2700-usuarios-ya-producen-su-propia-energia-argentina-n1196215); [MASE map](https://mase.lmneuquen.com/renovables/generacion-distribuida-como-es-el-mapa-usuarios-la-patagonia-n1216445); [Secretaría de Energía, Feb 2025 report](https://argentina.gob.ar/sites/default/files/ppt_reporte_de_avance_febrero_2025.pdf); [Infobae, 4 Jul 2025](https://www.infobae.com/economia/2025/07/04/modificaron-el-regimen-de-usuarios-de-energias-renovables-y-prohibieron-cargos-extra/)
- Front-of-pack labeling (Ley 27.642):
  - ANMAT offers a free public calculator for the warning seals (2022 note);
  - in May 2026 the government sent a bill to repeal the law;
  - in July 2026 iProfesional described the "fin de la dictadura de sellos negros".
  
  — [Cronista tag page](https://www.cronista.com/tema/etiquetado-frontal/); [iProfesional](https://www.iprofesional.com/legales/455533-etiquetado-frontal-como-sera-la-nueva-gondola-tras-fin-de-dictadura-de-sellos-negros); [HCDN bill](https://rest.hcdn.gob.ar/web/proyectos/291968/adjuntos/105773)
- Hail and crop claims: my search returned only Spain (Agroseguro: about 113,000 agricultural claims handled in 2025; storm indemnities estimated at €446M), not Argentina. — [Agroseguro PDF](https://agroseguro.es/wp-content/uploads/2026/01/NP-Agroseguro_Siniestralidad-seguros-agrarios-en-2025-2.pdf)

### Inferences
- **Livestock weighing:** several regional players already exist, including one operating in Argentina. A solo builder would compete on accuracy against funded teams with field data. Reject.
- **Solar sizing:** about 3,300 connections nationally is too few installers and projects to support a SaaS. Free global tools such as OpenSolar likely cover sizing (not verified in this pass). Reject unless distributed generation grows sharply.
- **Front-of-pack labeling:** regulatory risk is high, and a free official calculator exists. Reject.
- **Insurer photo inspection and vehicle history:** served. Only a buyer-side condition report (Candidate D) remains.

### Gaps
- Pest detection by photo, grain quality by phone, and fleet expense or receipt processing were not researched in this pass. Global tools are widely believed to exist (e.g., Plantix for pests; Rindegastos, a Chilean expense app, for receipts), but I did not verify them here, so they stay unscored.
- Argentine hail-claim processes (La Segunda, Sancor rural) and how producers document losses were not found. This is worth a dedicated search ("granizo denuncia siniestro La Segunda app fotos").
- Kilimo, Auravant and Agrofy were not individually reviewed.

---

## Q7. How was the competitor search done, and how confident is the "nobody does it" claim for each candidate?

### Takeaway
I ran Spanish and English web queries per candidate. They also surfaced App Store, Product Hunt, Capterra and YC pages. I did not search Google Play, the YC directory or Portuguese queries systematically. The confidence ratings below should be read as preliminary, pending a second sweep.

### Cited Findings
- Exact queries run, with their result:

| Candidate | Query | Result |
|---|---|---|
| A | "Resolución 400/2025 Secretaría de Energía grandes usuarios distribuidor contratos MEM asesoramiento consultora pymes" | no service found |
| A | "GUDI GUME contratos energía pymes asesoramiento gestión facturas CAMMESA comercializador 2026" | no service found |
| A | "pymes factura de luz aumento 2025 potencia contratada penalidad energía reactiva ahorro" | Spain-only results |
| B | "Fudo costeo de recetas inflación restaurantes Argentina software" | — |
| B | "Fudo sistema gastronómico stock recetas costo plato planes precio" | — |
| B | "MarginEdge invoice photo recipe costing pricing per location" | — |
| B | "app costeo recetas gastronomía Argentina cargar facturas proveedores actualiza costo plato" | no Argentine invoice-to-cost app |
| C | "presupuesto con IA desde fotos app electricistas plomeros oficios Latinoamérica" | US and Spain tools, OneEstimate, servidos.ar |
| C | "Handoff AI contractor estimate app pricing per month Y Combinator" | — |
| D | "inspección vehicular con inteligencia artificial fotos app Argentina usados" | — |
| D | "autoinspección seguro auto app fotos Argentina aseguradora inspección previa digital" | — |
| D | "Autofact informe vehicular Argentina historial auto usado" | — |
| D | "revisión precompra auto usado mecánico a domicilio precio servicio Buenos Aires Córdoba" | — |
| Q5 | "app gestión contratistas rurales órdenes de trabajo hectáreas facturación Argentina" | — |
| Q5 | "administración de consorcios CABA obligaciones mantenimiento certificados tanques fachadas software app inspección 2025" | — |
| Q6 | "pesaje de ganado por foto app celular inteligencia artificial bovinos" | — |
| Q6 | "usuarios generadores generación distribuida Argentina cantidad 2025 informe" | — |
| Q6 | "etiquetado frontal pymes alimentos rotulado nutricional costo nutricionista calculadora sellos 2026" | — |
| Q6 | "granizo seguro agrícola tasación perito fotos app productores denuncia siniestro 2025" | Spain only |

  — sources cited in Q1–Q6.

### Inferences
- Confidence that nobody serves it as an AI-native self-serve product:

| Candidate | Confidence | Main threat |
|---|---|---|
| A. GUDI energy copilot | Medium–high | Human consultancies; distributors acting as comercializadoras |
| B. Invoice photo → dish cost | Medium | Fudo or other local POS adding it; Kitchio localizing |
| C. Trades quoting copilot | Medium | Handoff or Spanish tools localizing; servidos.ar for homeowners |
| D. Used-car buyer report | Medium (gap) / low (durability) | Mercado Libre, Kavak, Datacar |
| E. Contratistas | Low–medium | Malevo, FinnApp |
| F. Consorcios | Unknown | Not verified |

- Fit with the entrepreneur's skills (Claude Code, web and mobile web apps, WhatsApp automations, documents):
  - A and B are mostly document understanding plus dashboards and alerts, which fits very well;
  - C is WhatsApp + PDF generation, which fits very well;
  - D needs a careful mobile capture UX and an OBD integration, which is a medium fit.
- Path to USD 1,000/month net (illustrative):
  - A: about 10 clients at USD 100–300;
  - B: about 30–50 venues at USD 20–50;
  - C: about 100+ tradespeople at about USD 10, or a few hardware-store sponsors;
  - D: per-report sales or dealer subscriptions.

### Gaps
- A second competitor sweep should cover:
  - Google Play (Argentina) and the App Store (Argentina);
  - the YC company directory (keywords: "energy bill", "restaurant invoice", "contractor estimate", "LatAm");
  - Product Hunt;
  - Portuguese queries ("auditoria conta de energia mercado livre PME", "custo de receita foto nota fiscal restaurante", "orçamento IA eletricista");
  - Argentine AgTech and PropTech ecosystem maps (Endeavor, Glocal), which were not consulted.
- No customer interviews or willingness-to-pay data were collected for any candidate.
