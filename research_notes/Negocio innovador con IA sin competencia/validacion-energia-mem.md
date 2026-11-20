# In-depth validation: energy contract and bill copilot for Argentina's ~6,000 GUDIs (Res. SE 400/2025 and 293/2026)

Scope note: research done 2026-11-20, about 50 searches and fetches, plus 3+3 queries from the earlier notes (`ia-mundo-fisico.md`, `cambios-sociales.md`). Sources are 2025–2026 unless marked. "Inference" means my own reasoning, not a sourced fact. Peso amounts are converted at the wholesale dollar of **ARS 1,551 per USD (16 Nov 2026)** — [Rava](https://www.rava.com/cotizaciones/historico/dolar-mayorista/2026/11/16/). Other press figures for November conflict (ARS 1,387–1,410), so treat conversions as approximate.

**Bottom line for the report writer.** The pain is real and well documented, and some companies already pay for help. But the gap is **not unserved**. At least six Argentine consultancies and comercializadoras already sell bill control or contract advice to GUDIs. One publishes a GUDI plan at ARS 250,000 per month (about USD 160). Two digital contracting platforms launched in 2026 (Enertoken by YPF Luz, and EVoltia), and an Argentine meter company (Powermeter) already sells AI reading of bill PDFs for USD 5–95 per month.

What I did **not** find is a self-serve tool built for GUDIs that does three things:
- forecasts the next bill, which arrives about 75 days after consumption;
- explains the "Cargo GUDI" charges;
- reconciles contract against bill across EPEC and Córdoba's roughly 150 electric cooperatives.

The opportunity is a narrower wedge than the original idea. My verdict is a **conditional go**, to be validated in 6 weeks with Córdoba GUDIs through the UIC, CLAUTO and the CIMCC (details at the end).

---

## Q1. What exactly do Res. SE 400/2025 and Res. SE 293/2026 require, what do the bills look like, and what confuses companies?

### Takeaway
Neither resolution forces a GUDI to contract or to join the MEM. The pain comes from **price exposure**. Since 1 Nov 2025, a GUDI that does not contract effectively pays the monthly spot cost. The charge arrives after the fact through the "Cargo Estabilizado GUDIs" and the "Ajuste Complementario de Potencia GUDIs" (Res. 976/2023). These lines exploded in winter 2026, and the bill arrives about 75 days after the energy is used.

The "60% / 80% / 100%" schedule to 2029 is often read as a contracting minimum. It is **not a minimum for users**. It is the **maximum share of spot thermal and hydro generation that can be sold under contract**, so it is a supply-side ceiling that opens up over time.

### Cited Findings
**Res. SE 400/2025 ("Normalización del MEM")**
- Published 21 Oct 2025 and applied to MEM transactions from 1 Nov 2025. It creates term markets for energy and power between generators, distributors and large users — [Marval](https://www.marval.com/publicacion/mercado-electrico-mayorista-normalizacion-y-modernizacion-17371); [official text](https://www.argentina.gob.ar/normativa/nacional/norma-419016/texto)
- GUDI means demand of **300 kW or more of contracted power per supply point**. GUDIs "no tendrán restricciones para el acceso al MEM como agentes" — [official text via search summary](https://www.argentina.gob.ar/normativa/nacional/norma-419016/texto); [Res. 293/2026 considerandos](https://www.boletinoficial.gob.ar/detalleAviso/primera/349363/20261021)
- Distributors must contract at least 75% of the energy for their end users, **"excluyendo los GUDIs"**. Two new reliability services are paid by "toda la demanda del MEM": Reserva de Confiabilidad (USD 1,000 per MW-month) and Reserva de Confiabilidad Adicional (USD 9,000 per MW-month for 10 years) — [Cassagne / abogados.com.ar](https://abogados.com.ar/la-resolucion-se-4002025-y-la-normalizacion-del-mem/37804). Whether GUDIs pay the reserve charges is not stated explicitly; that is my inference.
- "GUDI: Pagan precio spot mensual directo, sin estabilización." By contrast, T2/T3 users pay a seasonal price adjusted every quarter, and MEM large users pay a monomic price estimated at USD 80–95/MWh. The power charge now follows the highest 15-minute demand during Horas de Remuneración de Potencia (HRP), "so a single peak can set the month's cost" (opinion piece, 2 Aug 2026) — [Newstad, Martín Dapelo](https://www.newstad.com.ar/el-nuevo-costo-de-la-energia-para-las-industrias-por-que-las-pymes-deben-actuar-ahora)
- Mechanism as described in Córdoba: "Cammesa establece un precio de energía trimestral estabilizado… ese cargo de estabilización es ahora ultra caro… Antes, los GUDI estaban subsidiados" (José Manuali, UIC president, 27 Aug 2026) — [Puntal](https://www.puntal.com.ar/tarifas/gudi-la-nueva-preocupacion-industrial-un-salto-tarifas-que-afecta-350-empresas-cordobesas-n263782)

**Res. SE 293/2026 (signed 20 Oct 2026, Boletín Oficial 21 Oct 2026)**
- A GUDI has three options: (1) stay with the distributor's supply; (2) contract energy and power with one or more generators through the distributor acting as comercializadora or aggregator; (3) apply to become an MEM agent (GUMA or GUME). "Superar ese nivel de potencia no convierte automáticamente a una empresa en GUMA o GUME." The rule does not force anyone into the MEM — [iProfesional, 21 Oct 2026](https://www.iprofesional.com/negocios/467105-el-gobierno-acelera-la-apertura-del-mercado-electrico-para-empresas)
- **Entry windows** become monthly. The new procedure applies from 1 Dec 2026. The first "Mes de Aprobación" is **January 2027**. Requests go to CAMMESA (the OED) by the last business day of the month before. The entry date must be the first day of a month. Category changes between GUMA and GUME are also monthly, with a minimum stay of one year.
- **Approval steps:** CAMMESA checks the file in 10 business days. The Secretaría publishes it in the Boletín Oficial within 3 business days, for 2 days, so objections can be filed. ENRGE resolves objections in 20 calendar days, and an objection counts as valid if ENRGE does not answer in time. Approval requires an express resolution; tacit approval under Anexo 17 is removed.
- CAMMESA must "publicar y mantener actualizados en su sitio web los requisitos, formularios, calendarios y fechas límite" — [Boletín Oficial, Res. 293/2026](https://www.boletinoficial.gob.ar/detalleAviso/primera/349363/20261021)
- **Contract limits.** These cover contracting of spot thermal and hydro generation with GUMA/GUME and with distributors for GUDIs:
  - 20% until 31 Mar 2027;
  - 60% from 1 Apr 2027;
  - 80% from **1 Apr 2028**;
  - no percentage limit from 1 Jan 2029.

  — [Boletín Oficial, considerandos; the Anexos were not visible](https://www.boletinoficial.gob.ar/detalleAviso/primera/349363/20261021). **Conflict:** iProfesional gives 80% from **1 Jan 2028** and adds that this "no significa que toda esa energía vaya a quedar automáticamente contratada" — [iProfesional](https://www.iprofesional.com/negocios/467105-el-gobierno-acelera-la-apertura-del-mercado-electrico-para-empresas)
- **Before Dec 2026**, entry to the wholesale market opened only four times a year: "un problema visto en junio no podía corregirse para julio" (Alejandro Einstoss, Clarín, 26 Sep 2026) — [Nuevos Papeles](https://nuevospapeles.com/nota/energia-y-pymes-mismo-invierno-distinta-factura/)
- Earlier steps: Res. 27/2026 formalized new GUMA and GUME agents, and Res. 104, 108 and 112 authorized more — [iProfesional](https://www.iprofesional.com/negocios/467105-el-gobierno-acelera-la-apertura-del-mercado-electrico-para-empresas). Res. 112/2026 added GUMEs from 1 May 2026, for example Telefónica Móviles (Neuquén), Bodega Norton, Cirion Technologies, Frigorífico Soychú, and Video Drome S.A. with several supply points in the NOA — [AGUEERA monthly BO summary, May 2026](https://www.agueera.com.ar/wp-content/uploads/2026/06/MEM-BO-052026.pdf)
- Res. SE 379/2025 created a voluntary, **paid demand-reduction program** for large users, GUDIs included. Members get a fixed charge plus variable pay, and GUDIs and GUMEs pay distributors a technical management charge of USD 30 per MW-month. It runs December–March and June–August — [abogados.com.ar](https://abogados.com.ar/lanzamiento-del-programa-de-gestion-avanzada-de-demanda/37645); [EconoJournal](https://econojournal.com.ar/energia/crearon-programa-remunerara-industrias-corten-demanda-electrica-picos-consumo-verano/). On bills it appears as "Res SE 379/25-Gestión Demanda" — [AGUEERA BO summary](https://www.agueera.com.ar/wp-content/uploads/2026/06/MEM-BO-052026.pdf)

**Prices: why bills jumped**
- In November 2025, CAMMESA estimated the GUDI energy cost at **USD 56.1/MWh**. The spot price later reached **USD 186/MWh** — [Minuto de Cierre, 21 Oct 2026](https://www.minutodecierre.com/nota/2026-10-21-11-12-0-la-inflacion-que-el-indec-no-mide-el-cargo-a-grandes-consumidores-de-energia-que-aumento-sus-facturas-mas-del-50-entre-septiembre-y-octubre)
- Spot price vs programmed price, in USD/MWh: May 140 vs 78; June 189 vs 88; July 169 vs 104. GUDIs that kept buying from the distributor paid up to **180 USD/MWh in June**, while a firm with a contract paid about 60. "Para una planta que consume 100 MWh por mes, la diferencia supera los 10.000 dólares mensuales" — [Nuevos Papeles / Clarín](https://nuevospapeles.com/nota/energia-y-pymes-mismo-invierno-distinta-factura/)
- Other figures:
  - May spot above USD 105/MWh vs about 58 in April and a projected 65;
  - the GUDI power charge is about **USD 15–20/MWh**;
  - "las industrias reciben sus facturas con un delay de **75 días**";
  - many annual contracts signed in 2026 at below USD 60/MWh let generators **not deliver** when their variable costs rise, which pushes contracted users back to spot.
  
  — [EconoJournal, 4 Jun 2026](https://econojournal.com.ar/?p=128978)
- More figures (2 Sep 2026): June energy price USD 163/MWh with a system marginal cost of USD 203/MWh. Nadia Sager (GEINSA) projects about USD 75/MWh on average for 2026 and about **USD 62/MWh for 2027** — [Al Sur Noticias](https://alsurnoticias.com.ar/2026/09/02/electricidad-mas-de-800-grandes-industrias-dejaron-a-las-distribuidoras-y-buscan-comprar-energia-mas-barata/)
- **Conflict:** Newstad gives July spot at USD 189/MWh, the "highest in 30 years" — [Newstad](https://www.newstad.com.ar/el-nuevo-costo-de-la-energia-para-las-industrias-por-que-las-pymes-deben-actuar-ahora); Nuevos Papeles gives June 189 and July 169 — [Nuevos Papeles](https://nuevospapeles.com/nota/energia-y-pymes-mismo-invierno-distinta-factura/)

**What the bill looks like and what confuses people**
- **Res. 976/2023** created two charges, "Cargo Estabilizado GUDIs" and "Ajuste Complementario de Potencia GUDIs". CAMMESA bills them to distributors, which can pass them on, starting with February 2024 transactions — [Res. 976/2023](https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-976-2023-394390/texto); [ENRE Res. 197/2024](https://www.boletinoficial.gob.ar/detalleAviso/primera/305217/20240327)
  - The stabilized charge compares the MEM average energy price with the reference prices for power, energy and transport.
  - The complementary adjustment uses the monthly reserve price minus the reference power price, applied to the gap between maximum and average demand.
  
  — [Tavarone](https://tavarone.com/la-secretaria-de-energia-establece-nuevos-cargos-para-los-gudis/)
- CAMMESA settles these charges at the end of each month, once real cost is known. "No hay previsibilidad. Las empresas no saben cuánto les va a llegar en la factura siguiente" (Gustavo Puccini, Santa Fe production minister). Some bills went up to **7x**: ARS 1.4M to 8M, and ARS 4M to 28M, which is about USD 2,600 to 18,000 — [Rosario3, 3 Aug 2026](https://www.rosario3.com/-economia-negocios-agro-/la-provincia-pedira-a-nacion-revisar-un-cargo-que-disparo-las-facturas-de-electricidad-en-grandes-industrias-y-comercios-20260803-0056.html)
- The charges rose **491.9%** between the April and May 2026 bills. Santa Fe's provincial total for these charges: ARS 414M (March) → 1,271M (April) → 7,110M (May) → over 14,300M projected for the August bill. EPE says CAMMESA sets the charges and EPE, EPEC and Enersa only pass them on — [Urgente24, 3 Aug 2026](https://urgente24.com/actualidad/santa-fe-presiona-javier-milei-frenar-el-impacto-del-tarifazo-industrias-n629863)
- A real October 2026 example (an Edenor user served through Mercado Central):
  - the bill rose from ARS 3,384,412 (September) to ARS 5,243,235 (October), +55%;
  - the "Resolución 976/23 Cargo GUDIs" line went from ARS 314,238 to over ARS 1.4M;
  - the September charge was recovered in three monthly installments;
  - other lines: Recupero Otra Jurisdicción 6.43%, Tasa de Mantenimiento, Gastos Administrativos, IVA 27%.
  
  — [Minuto de Cierre](https://www.minutodecierre.com/nota/2026-10-21-11-12-0-la-inflacion-que-el-indec-no-mide-el-cargo-a-grandes-consumidores-de-energia-que-aumento-sus-facturas-mas-del-50-entre-septiembre-y-octubre)
- In Córdoba, the August, September and October bills each carry about an extra month of energy cost because of the billing lag. The June bill "roughly doubles" — [Puntal](https://www.puntal.com.ar/tarifas/gudi-la-nueva-preocupacion-industrial-un-salto-tarifas-que-afecta-350-empresas-cordobesas-n263782)
- Bills do not show which part of the energy is priced hourly at spot. Einstoss recommends showing it — [Nuevos Papeles](https://nuevospapeles.com/nota/energia-y-pymes-mismo-invierno-distinta-factura/)

**What industry groups say (IPA and others)**
- IPA: about 6,000 firms are covered and about 800 signed contracts. Some bills quadrupled, and contracted firms report extra charges that bring the cost close to double the agreed price. "Estamos obligando a una PyME a convertirse de un día para otro en especialista en contratación energética" — [El Economista, Daniel Barneda, 29 Sep 2026](https://eleconomista.com.ar/energia/la-letra-chica-energia-pymes-denuncian-pagan-doble-lo-acordado-n98498)
- IPA leadership: "Hacemos contratos y terminamos pagando la energía hasta el doble de lo que pactamos. Alguien tiene que intervenir"; "consideramos que estamos siendo estafados". It also complains of "falta de información y asistencia técnica" — [La Gaceta, 28 Sep 2026](https://www.lagaceta.com.ar/nota/1155827/economia/industriales-pymes-denunciaron-fuertes-aumentos-costo-energia-tras-liberacion-mercado.html)
- Industries in Misiones and Chaco claim a gap of more than 185% between the price passed to tariffs and the real wholesale cost — [Postenergético](https://postenergetico.com.ar/industrias-de-misiones-y-chaco-reclaman-a-nacion-por-un-cargo-electrico-que-duplica-sus-facturas/)
- Córdoba: CLAUTO (the automotive cluster) met EPEC on 26 Dec 2025. Options discussed: migrating to the wholesale market; tripartite or quadripartite contracts (generator, user, distributor or cooperative); direct contracts from EPEC, still "under study" — [CLAUTO, 5 Jan 2026](https://clauto.org.ar/reduccion-de-costos-en-energia-electricidad-y-gas/). EPEC has used tripartite contracts with renewable generators since November 2024 — [EPEC sustainability report](https://www.epec.com.ar/docs/transparencia/PDF%20Sexto%20Reporte%20de%20Sostenibilidad%20EPEC.pdf)

### Inferences
- The confusion has three layers, and each one maps to a product feature:
  1. **Timing:** a 75-day lag, ex-post true-ups and installment recoveries. The company cannot budget. → **Next-bill forecast.**
  2. **Opacity:** a single "Cargo GUDIs" line that hides the spot exposure. → **A line-by-line explanation of each charge.**
  3. **Contracts:** clauses that let generators not deliver, take-or-pay, and the gap between the contracted price and the final cost. → **Contract-vs-bill reconciliation and clause risk flags.**
- The user brief says "rising contract minimums 2027–2029". The primary source shows these are **ceilings on the supply side**, not obligations for users. The product should present them as "how much contracted supply will be available", not as a compliance deadline.
- The monthly windows from Dec 2026 create a **recurring decision** each month: "should I move to GUME next month?" This works better for a monitoring subscription than the old quarterly windows did.

### Gaps
- I could not read the Anexos of Res. 293/2026 (the BO page shows only the considerandos), or the full GUDI section of Res. 400/2025 (the official "texto actualizado" page returned HTTP 500).
- I did not see a real EPEC or cooperative GUDI bill, a generator invoice or a CAMMESA DTE. The format variety is unverified.
- I found no statement that Res. 293 sets penalties for GUDIs. The financial risk is spot exposure, not a fine.

---

## Q2. Exhaustive competitor search: who already serves this, what do they do, and at what price?

### Takeaway
The space has **human consultancies, comercializadoras, an industry association, two new contracting platforms and one cheap AI bill reader**. Nobody I found sells a **self-serve, GUDI-specific bill forecaster and contract-vs-bill auditor**, especially one that handles Córdoba's cooperative bills. The closest threats are:
- **Powermeter**: Argentine, already reads bill PDFs with AI, up to USD 95 per month;
- **Latin Energy Group**: a GUDI plan of about USD 160 per month that includes bill control;
- **Enertoken** (YPF Luz): plans a client portal with billing tracking.

### Cited Findings
**Argentina: consultancies and service firms**
| Firm | What it does | Price | GUDI focus? |
|---|---|---|---|
| **Latin Energy Group** (CABA) | "Comercialización profesional de energía". Plans include contract negotiation, renewables advice, **bill control (CAMMESA, generators, distributor)**, annual budget, regulatory updates and an online reports portal. Free "segunda opinión" meeting. | **GUMA ARS 350,000/mo; GUME 320,000/mo; GUDI 250,000/mo** (about USD 161). The GUDI plan excludes online reports and monthly cost provisioning. Footer © 2026; the page does not say whether IVA is included. | Yes, an explicit GUDI plan. — [lenergygroup.com](https://www.lenergygroup.com/servicios/asesoramiento-integral/) |
| **Energeia** (CABA) | Electricity, gas and oil commercialization; GUDI vs GUMA/GUME advice; handles the CAMMESA filing, monthly follow-up and savings reports. "Aplicamos IA para optimizar el abastecimiento." | **Free diagnosis** from the last 12 bills; contract fees not public. | Yes. — [energeia.ar](https://energeia.ar/servicios/) |
| **GEINSA** (Nadia Sager, CEO) | Comercializadora and consultancy; source of the "cercano a los 6.000 GUDIs" count. | Not public. | Yes. — [Al Sur Noticias](https://alsurnoticias.com.ar/2026/09/02/electricidad-mas-de-800-grandes-industrias-dejaron-a-las-distribuidoras-y-buscan-comprar-energia-mas-barata/); [EconoJournal](https://econojournal.com.ar/?p=128978) |
| **ITAndes** (San Isidro) | An assigned advisor checks: CAMMESA bills monthly; distributor bills against tariff schedule and power and power-factor penalties; generator bills against CAMMESA's DTE and the contract. | Quote form only. | Large users; GUDI not named. — [itandes.com.ar](https://itandes.com.ar/contratos-de-energia/) |
| **Optimizar SMEC S.R.L.** | Since 2004: SMEC commercial metering (700+ projects), MEM contract management, billing audit. Clients include Arcor, YPF, Pampa, Genneia, Aluar. | Not public. | GUMA/GUME; GUDI not named. — [optimizar.com.ar](https://optimizar.com.ar/servicios.html) |
| **Alpes Energy** (CABA) | Supply proposals for gas and electricity; has written for GUDIs since 2023. | Not public. | Yes (2023 post). — [alpesenergy.com](https://www.alpesenergy.com/blog/2023/12/11/importante-noticia-para-las-gudis-cambio-drastico-en-su-costo-energia/) |
| **AGUEERA** (large-users association, created under Law 24.065, 1992) | "Asesoramiento y Acompañamiento… en los temas Regulatorios, Normativos, de Precios" for members; monthly Boletín Oficial summaries. | Membership (fee not found). | Large users. — [AGUEERA BO summary](https://www.agueera.com.ar/wp-content/uploads/2026/06/MEM-BO-052026.pdf) |
| **Dynamic Energy** (dynamicenergy.com.ar) | Publishes GUDI guides ("Migración al MEM para GUDIs", "Ingreso al MEM: qué cambia para las empresas GUDI"). A company with that name is registered in Olivos (2019, 1–20 employees). | Unknown; site returned 503. | Yes (content). — [search result](https://dynamicenergy.com.ar/noticias/gudis-migracion-mem-compra-energia-industria/); [DunsGuide](https://www.dunsguide.com/company/6ac36dcf1572cbf8982800f315fda8d9/dynamic-energy-soluciones-energeticas-sas) |
| Individual consultants | LinkedIn profiles of ex-CAMMESA staff offering bill audits (not verified as firms). | — | — [example](https://www.linkedin.com/in/mat%C3%ADas-castro-06327822/) |

**Argentina: comercializadoras and generators selling to large users**
- **SAESA** (Juan Bosch, CEO): comercialization of gas and electricity for large users, renewable "Open Season" — [Mercado](https://mercado.com.ar/protagonistas/saesa-lanza-el-open-season-de-energias-renovables); [EconoJournal](https://econojournal.com.ar/?p=128978)
- Also selling to large users, or preparing to:
  - **Ayres/Aires Renewables** (Diego Werner) — [Al Sur Noticias](https://alsurnoticias.com.ar/2026/09/02/electricidad-mas-de-800-grandes-industrias-dejaron-a-las-distribuidoras-y-buscan-comprar-energia-mas-barata/);
  - **Enel Trading Argentina** — [enel.com.ar](https://enel.com.ar/es/enel-trading-argentina/a201903-una-comercializadora.html);
  - **Edison** (as comercializador) — [iProfesional](https://www.iprofesional.com/negocios/455858-edison-trading-y-el-poder-de-los-neuss-el-ultimo-paso-para-controlar-el-sistema-electrico);
  - **Genneia** (applied to be a comercializador) — [iProfesional](https://www.iprofesional.com/energia/461375-integracion-vertical-la-estrategia-de-genneia-para-liderar-el-mercado-entre-privados);
  - **CINERGIA** (comercializadora with a long record).
- **YPF Luz:** term-market contracts and PPAs; more than 70 industrial clients according to its site — [ypfluz.com](https://www.ypfluz.com/Servicios)
- **Distributors and cooperatives as comercializadoras:**
  - EPEC uses tripartite and quadripartite contracts and was studying direct contracts — [CLAUTO](https://clauto.org.ar/reduccion-de-costos-en-energia-electricidad-y-gas/);
  - Concordia's cooperative signed direct purchase contracts with YPF Luz and Central Puerto (10 Jun 2026) — [Coopelec](https://www.coopelec.com.ar/compra-directa-a-ypf-luz-y-central-puerto/)

**Argentina: digital platforms and software**
- **Enertoken** (YPF Luz + JusToken, launched Feb 2026). It calls itself "la mayor plataforma de la Argentina para la contratación y gestión de energía eléctrica":
  - a savings simulator from the declared consumption profile;
  - fully digital contracting with e-signature, on the XRP Ledger;
  - a planned client portal for YPF Luz's 90 corporate clients, with "consumption tracking, billing and real-time reports";
  - "cientos de pymes" named as a future benefit; no fees stated.
  
  — [InfoArenales, 14 Feb 2026](https://infoarenales.com/2026/02/14/inedito-ypf-luz-lanza-plataforma-con-tecnologia-blockchain-para-comprar-energia-electrica-online/)
- **EVoltia:** "Conectamos a empresas y PyMEs con comercializadoras y generadores". It offers:
  - closed bidding rounds;
  - a **bill-upload savings calculator**;
  - market data;
  - KYB and credit scoring;
  - PPA generation.
  
  No pricing, founders or minimum kW are stated, and it does not mention GUDI — [evoltiaenergy.com](https://www.evoltiaenergy.com/)
- **Licitar Energía:** a gas and electricity tender platform for service stations, free for the buyer — [Surtidores](https://surtidores.com.ar/una-nueva-plataforma-digital-promete-simplificar-la-compra-de-energia-para-estaciones-de-servicio/)
- **Powermeter / Powermate** (Argentine meter maker, manufacturing locally since 2012):
  - cloud monitoring every 5 minutes;
  - **bill audit where "la IA extrae los datos" from the PDF** and flags reactive-power and demand penalties and cost deviations;
  - "Compará consumo vs. facturación y gestioná contratos", plus dispute tracking with the distributor.
  
  Plans: Free; Plus USD 5/mo (1 AI bill); Profesional USD 40/mo (5 bills); **Experto USD 95/mo (30 bills, 20 devices)**. The page says nothing about MEM, GUDI, spot or CAMMESA — [powermeter.io/powermate](https://www.powermeter.io/powermate). The homepage claims more than 2,500 companies and 10,000 devices (search snippet; not checked on the page) — [powermeter.io](https://www.powermeter.io/)
- **Globalsyde Argentia:** back-office software for energy comercializadoras (billing reconciliation), aimed at sellers, not users — [globalsyde.com](https://globalsyde.com/soluciones/argentia/)

**Brazil (mercado livre: analogues)**
- **Clarke Energia:** a mix of "corretor e contador" (broker and accountant), run as a marketplace with about 60 suppliers. About 300 clients and 200 GWh/yr in March 2024, when **Energisa bought 70%**. Targets were 2,000 clients by end-2025 and 20,000 consumer units in four years — [Brazil Journal, 22 Mar 2024](https://braziljournal.com/energisa-compra-a-clarke-um-corretor-e-contador-do-mercado-livre-de-energia/). Fees: free-market consultancy **R$100/month**; demand-adjustment and tariff studies at **30% of savings for 12 months** (page updated Jun 2025) — [Clarke](https://clarke.com.br/post/como-a-clarke-ganha-dinheiro/). It groups small users into "condomínios virtuais" to reach 500 kW — [Clarke blog](https://blog.clarke.com.br/post/clarke-energia-ajuda-empresas-a-economizarem-ate-30-na-conta-de-luz/)
- **eGrid** (Porto Alegre): SaaS that integrates CCEE data with a digital certificate, downloads invoices automatically, sends demand-overrun alerts and monthly savings reports; for consumers, distributed generation and energy managers; no public price — [egrid.app](https://www.egrid.app/)
- Brazilian service firms:
  - **Solut-e**: free diagnosis, then a fixed fee or a share of savings, charged only once savings start;
  - **Edots**: audit plus telemetry;
  - **Ativvo**: success fee on recovered overcharges;
  - **Conta Justa** and **Energia Livre Brasil**: free one-off bill analysis.
  
  — [solut-e.com](https://solut-e.com/); [edots.com.br](https://edots.com.br/); [ativvo.com.br](https://ativvo.com.br/); [contajustaenergia.com.br](https://contajustaenergia.com.br/); [energialivrebrasil.com.br](https://energialivrebrasil.com.br/)
- Earlier notes also list **Lemon Energia**, **Digital Grid** and **Energiacooper** for distributed generation — see `cambios-sociales.md`.

**Chile (clientes libres: analogues)**
- **Plataforma Energía:** spun off from Efizity in 2016; supply tenders, **bill audit**, BESS and solar tenders; more than 230 tenders and 3,015 GWh/yr traded — [plataformaenergia.com](https://plataformaenergia.com/cl/)
- **Conergie:** digital tenders among associated generators, **only for clients of 300 kW or more** — [conergie.cl](https://conergie.cl/)
- **Tenssor:** SaaS with live data from the Coordinador Eléctrico Nacional, billing automation — [tenssor.cl](https://tenssor.cl/)
- **Energía Simple:** tender advice — [energiasimple.cl](https://energiasimple.cl/)

**US and global**
- **EnergyCAP:** utility bill management at **USD 2.17–4.28 per meter per month**, with a bill-audit add-on; third-party listings show a floor of about USD 5,000/yr — [EnergyCAP pricing](https://www.energycap.com/pricing/); [Software Advice](https://www.softwareadvice.com/utility-billing/energycap-profile/)
- **Gravity** (San Francisco) launched AI-agent utility bill management in June 2026. It flags billing errors and tariff mismatches and starts the recovery workflow — [VentureBeat](https://venturebeat.com/business/many-companies-overpay-on-utilities-gravity-just-launched-an-ai-product-to-fix-that)
- **Condor Energy** (YC): AI procurement optimization for commercial and industrial users and data centers, not in Latin America — [YC](https://www.ycombinator.com/companies/condor-energy)
- Product Hunt: bill analyzers for households only (Ohmbolt, Explain My Bill, PowerBill, Bill Negotiator) — [Ohmbolt](https://www.producthunt.com/posts/ohmbolt)

**Every query run (this pass, plus the earlier notes)**
- Spanish:
  1. "GUDI factura cuadruplicó precio spot Resolución 400/2025 pymes energía"
  2. "GUDI precio monómico CAMMESA noviembre 2025 demanda grandes usuarios distribuidor spot USD/MWh"
  3. "consultora energética grandes usuarios MEM GUDI asesoramiento contratos"
  4. "comercializadora energía eléctrica Argentina pymes GUDI contrato mercado a término 2026"
  5. "auditoría facturas energía eléctrica empresas Argentina software"
  6. "EPEC grandes usuarios GUDI Córdoba Resolución 400 contratos industrias 2026"
  7. "GEINSA consultora energía Nadia Sager grandes usuarios"
  8. "YPF Luz OR Genneia OR "Central Puerto" ofrece contratos pymes GUDI 300 kW mercado a término"
  9. "site:linkedin.com/company comercializadora energía eléctrica Argentina grandes usuarios"
  10. "plataforma digital licitación compra energía eléctrica pymes Argentina mercado a término marketplace"
  11. ""Dynamic Energy" Argentina energía grandes usuarios comercializadora"
  12. "AGUEERA grandes usuarios energía Resolución 400 GUDI 2026 reclamo"
  13. "Unión Industrial de Córdoba energía GUDI EPEC reunión 2026 costo eléctrico industrias"
  14. ""Cargo GUDI" OR "Ajuste Complementario de Potencia" factura grandes usuarios distribuidora"
  15. "cantidad nuevos grandes usuarios MEM 2026 GUME GUMA ingresos récord CAMMESA agentes"
  16. "Powermeter GUDI mercado eléctrico mayorista contrato energía empresas"
  17. "CAMMESA API datos públicos precios spot descarga web services"
  18. ""control de facturas" OR "auditoría de facturas" energía eléctrica grandes usuarios CAMMESA consultora Argentina"
  19. "Saesa energía comercializadora pymes industrias contratos electricidad GUDI oferta"
  20. "Resolución 379/2025 Programa de Gestión de Demanda grandes usuarios GUDI remuneración reducción de carga"
  21. "Industriales Pymes Argentinos IPA energía Res 400 mesa de diálogo noviembre 2026 Rosato"
  22. "Córdoba cooperativas eléctricas cantidad distribuidoras EPEC grandes usuarios 300 kW industrias parques industriales"
  23. "Chile clientes libres plataforma gestión energía licitación suministro software startup"
  24. "dólar oficial mayorista cotización noviembre 2026"
- Earlier notes: "Resolución 400/2025 … asesoramiento consultora pymes"; "GUDI GUME contratos energía pymes asesoramiento gestión facturas CAMMESA comercializador 2026"; "pymes factura de luz aumento 2025 potencia contratada penalidad energía reactiva ahorro"; plus three similar queries in `cambios-sociales.md`.
- Portuguese:
  1. "software gestão de faturas de energia auditoria conta de luz empresas mercado livre preço"
  2. "Clarke Energia gestora mercado livre de energia preço mensalidade PME"
  3. "gestora de energia mercado livre quanto cobra fee mensal percentual economia consultoria"
  4. "gestora de energia mercado livre honorários mensais "por unidade consumidora" OR "fee de gestão" valor médio"
- English:
  1. "utility bill audit software pricing per meter per month EnergyCAP Arcadia Urjanet"
  2. "Y Combinator startup energy procurement Latin America commercial electricity bills AI"
  3. "producthunt.com energy bill AI analyzer business electricity invoice audit"

### Inferences
- **The "nobody does it" claim fails for services and holds only for a specific product.** Human bill control for GUDIs exists and is priced (Latin Energy Group). Comercializadoras give free advice because they earn on supply (Energeia, Latin Energy's free second opinion).
- The open wedge is a product that is:
  - **self-serve and cheap**;
  - **neutral** (sells no energy);
  - **forecast-first** (it answers "what will my next bill be?");
  - **cooperative-aware** (EPEC plus about 150 cooperatives, with their own formats).

  None of the players above shows all four.
- **Powermeter is the most dangerous competitor.** It is local, has an industrial base, already sells AI bill extraction at USD 95, and owns meters. Adding a "Cargo GUDI" module would be easy for them. They may also be a **partner**, for example for the optional 15-minute load data.
- **Enertoken and EVoltia** compete for the "choose a contract" step. A neutral tool could feed them leads, or lose to them if they bundle billing tracking for free.

### Gaps
- I did not search the Google Play or App Store catalogs, Crunchbase or LAVCA directly (the YC and Product Hunt searches were indirect).
- No fees found for Energeia, GEINSA, ITAndes, Optimizar, AGUEERA membership or EVoltia.
- I did not confirm whether Powermeter's AI reads EPEC and cooperative GUDI bills or "Cargo GUDI" lines.
- Enerlogix (named in a search summary as an MEM consultancy) returned 404; country and offer unverified.

---

## Q3. Willingness to pay: what do companies pay today, and how big are the savings?

### Takeaway
Price anchors: about **USD 95/month** (Powermeter AI bill audit), about **USD 160/month** (Latin Energy Group's human GUDI plan), and **30% of savings for 12 months** (Brazilian model). On the other side is **free** advice from comercializadoras. Savings per GUDI are large in a bad winter (about USD 10,000+ per month in energy alone at 100 MWh per month), so a fee of USD 100–150 per month is well under 1% of energy spend. The willingness to pay is real but capped by free alternatives.

### Cited Findings
- Latin Energy Group: **ARS 250,000/month for GUDIs** (about USD 161), ARS 320,000 for GUMEs, ARS 350,000 for GUMAs — [lenergygroup.com](https://www.lenergygroup.com/servicios/asesoramiento-integral/)
- Powermeter Powermate: USD 5 / 40 / **95** per month — [powermeter.io/powermate](https://www.powermeter.io/powermate)
- Clarke (Brazil): R$100/month consultancy; 30% of savings for 12 months on demand and tariff studies — [Clarke](https://clarke.com.br/post/como-a-clarke-ganha-dinheiro/)
- Brazil service models: free diagnosis, then a fixed fee or a share of savings, charged only once savings start (Solut-e); success fee on recovered overcharges (Ativvo) — [solut-e.com](https://solut-e.com/); [ativvo.com.br](https://ativvo.com.br/)
- US software: EnergyCAP USD 2.17–4.28 per meter per month (a high-volume, low-touch model) — [EnergyCAP](https://www.energycap.com/pricing/)
- Free advice in Argentina: Energeia offers a "Diagnóstico energético inmediato y sin cargo" — [energeia.ar](https://energeia.ar/servicios/); Latin Energy offers a free second opinion — [lenergygroup.com](https://www.lenergygroup.com/servicios/asesoramiento-integral/)
- Size of savings:
  - contract at about USD 60/MWh vs GUDI spot of 180 in June: more than USD 10,000 per month for a 100 MWh/month plant — [Nuevos Papeles](https://nuevospapeles.com/nota/energia-y-pymes-mismo-invierno-distinta-factura/);
  - early contracting could have locked USD 60–70/MWh (Diego Werner) — [Al Sur Noticias](https://alsurnoticias.com.ar/2026/09/02/electricidad-mas-de-800-grandes-industrias-dejaron-a-las-distribuidoras-y-buscan-comprar-energia-mas-barata/)
- Bill sizes:
  - Edenor/Mercado Central user: ARS 5.24M in October 2026 (about USD 3,400) — [Minuto de Cierre](https://www.minutodecierre.com/nota/2026-10-21-11-12-0-la-inflacion-que-el-indec-no-mide-el-cargo-a-grandes-consumidores-de-energia-que-aumento-sus-facturas-mas-del-50-entre-septiembre-y-octubre);
  - Santa Fe examples: ARS 4M → 28M (about USD 2,600 → 18,000) — [Rosario3](https://www.rosario3.com/-economia-negocios-agro-/la-provincia-pedira-a-nacion-revisar-un-cargo-que-disparo-las-facturas-de-electricidad-en-grandes-industrias-y-comercios-20260803-0056.html)
- Spain: SME bill-audit services are mature (reactive-energy and excess-power penalties) — see `ia-mundo-fisico.md` ([tarifasgasluz.com](https://tarifasgasluz.com/pymes/energia-reactiva))

### Inferences
- Illustrative arithmetic, not sourced:
  - a 300 kW GUDI at a 50% load factor uses about 110 MWh per month, or about 1,300 MWh per year;
  - at an all-in USD 90–100/MWh, that is about **USD 120–130k per year**;
  - finding 2–5% of avoidable cost (peak-demand penalties, reactive power, wrong passthroughs, unclaimed contract deviations, a better contracting decision) is worth **USD 200–500 per month**.
  
  A fee of **USD 90–150 per month per supply point** is easy to justify on paper.
- The real constraints are **trust** (sharing bills and contracts) and **free substitutes**. So the price should start below Latin Energy's USD 160 and include a **paid one-off diagnosis**, for example USD 250–400 for "your 12 bills explained plus a GUDI vs contract vs GUME simulation". A success-fee option on recovered overcharges could follow.
- Brazil shows that a broker-and-accountant hybrid scales (Clarke reached a strategic sale). It also shows the winner was bought by a utility, so **bundling by incumbents is the normal outcome**.

### Gaps
- No public fee data for Argentine comercializadoras' commissions or consultancies' success fees.
- I did not confirm whether Latin Energy's ARS 250,000 includes IVA, or when the price was last updated (only the © 2026 footer).
- No survey of GUDI owners' stated willingness to pay. It must come from interviews.

---

## Q4. Market size and segmentation: how many, how many SMEs, how many in Córdoba, and where is the list?

### Takeaway
About **6,000 GUDIs** nationally (IPA, GEINSA and EconoJournal all repeat the number; it is not an official count), of which **800+** had contracts by September 2026. Córdoba has about **350** affected companies according to the UIC, and Santa Fe about **340**. The segment includes SMEs, large commercial users and multi-site chains. There is no public GUDI list, but there are good proxies.

### Cited Findings
- "Cercano a los 6.000 GUDIs"; more than 800 left distributor supply to contract in the term market (Nadia Sager, GEINSA, 2 Sep 2026) — [Al Sur Noticias](https://alsurnoticias.com.ar/2026/09/02/electricidad-mas-de-800-grandes-industrias-dejaron-a-las-distribuidoras-y-buscan-comprar-energia-mas-barata/)
- "Unas 6.000 industrias del país sufrirán la suba de costos" — [EconoJournal](https://econojournal.com.ar/?p=128978); about 6,000 per IPA — [El Economista](https://eleconomista.com.ar/energia/la-letra-chica-energia-pymes-denuncian-pagan-doble-lo-acordado-n98498)
- **Córdoba: "aproximadamente unas trescientas cincuenta empresas"** with the GUDI problem (Manuali, UIC) — [Puntal, 27 Aug 2026](https://www.puntal.com.ar/tarifas/gudi-la-nueva-preocupacion-industrial-un-salto-tarifas-que-afecta-350-empresas-cordobesas-n263782)
- Santa Fe: about 340 industries and cooperatives — [Urgente24](https://urgente24.com/actualidad/santa-fe-presiona-javier-milei-frenar-el-impacto-del-tarifazo-industrias-n629863). The affected users include "industrias, pymes y grandes comercios"; many plants run at 20–30% of capacity — [Rosario3](https://www.rosario3.com/-economia-negocios-agro-/la-provincia-pedira-a-nacion-revisar-un-cargo-que-disparo-las-facturas-de-electricidad-en-grandes-industrias-y-comercios-20260803-0056.html)
- Córdoba distribution: **EPEC plus about 150 cooperatives**, per a provincial document (undated) — [gestionabierta.cba.gov.ar](https://gestionabierta.cba.gov.ar/wp-content/uploads/2023/08/20.-Energías-Renovables-e-Infraestructura-Eléctrica.pdf). ERSeP groups cooperatives by whether they have large users (groups A, C and E have them) — [ERSeP hearing, Feb 2025](https://ersep.cba.gov.ar/wp-content/uploads/2025/02/AudienciaCooperativasElectricas13-02-25.pdf)
- The UIC publishes a quarterly **Índice de Precios de Energía**, splitting medium-voltage users above 300 kW from low-voltage users below 300 kW, and compares EPEC with other provinces — [UIC](https://www.uic.org.ar/portal/indice-de-precios-de-energia/)
- Sources for names:
  - GUMA/GUME entries are published in the Boletín Oficial and summarized monthly by AGUEERA — [AGUEERA](https://www.agueera.com.ar/wp-content/uploads/2026/06/MEM-BO-052026.pdf);
  - CAMMESA posts the resolutions, e.g. RESOL-2026-27 and RESOL-2026-112 — [CAMMESA](https://cammesaweb.cammesa.com/2026/05/06/resol-2026-112-apn-semec/);
  - CAMMESA also posts "Baja de grandes usuarios del MEM 2026" — [CAMMESA](https://cammesaweb.cammesa.com/2026/09/14/baja-de-grandes-usuarios-del-mem-2026-2/)
- Multi-site users exist: for example, Video Drome S.A. joined as a GUME with several supply points in the NOA — [AGUEERA](https://www.agueera.com.ar/wp-content/uploads/2026/06/MEM-BO-052026.pdf)

### Inferences
- **The 6,000 may count supply points, not companies.** The regulation counts per supply point. Multi-site retail chains, cold stores, hospitals and data centers hold several points, which favors per-point pricing.
- **SMEs vs large:** firms with 300 kW to about 1–2 MW are typically mid-size industrial SMEs. Large groups usually already have energy staff or consultants. The best target is a **single-plant SME with 300 kW to 1 MW**, no energy manager, and the owner or CFO reading the bill.
- **Where to build a list (inference):**
  1. UIC, CIMCC and CLAUTO members with medium-voltage supply;
  2. industrial parks in Córdoba (Expo Parques Industriales 2026, where EPEC attended — [El Periódico](https://el-periodico.com.ar/region/epec-participo-de-la-expo-parques-industriales-cordoba-2026_a6aaf2a99ade69350b5e1682a));
  3. cooperatives in ERSeP groups A, C and E;
  4. BO lists of GUMEs (firms that already moved, for the contract-audit module);
  5. LinkedIn searches for "jefe de mantenimiento" or "gerente de planta" at Córdoba industries.
- **The SAM is small:** about 6,000 nationally and about 350 in Córdoba. At USD 100–150 per month, capturing 1% nationally (60 points) is about USD 6–9k MRR. That is fine for a one-person target of USD 1,000/month net, but **not a venture-scale market** unless it grows into gas, the GUME/GUMA tiers, or the larger sub-300 kW T3 base.

### Gaps
- No official count of GUDI supply points (CAMMESA and distributors do not publish it).
- No split by size, sector or province beyond Córdoba (about 350) and Santa Fe (about 340).
- Not verified: how many Córdoba GUDIs are served by cooperatives vs EPEC.

---

## Q5. How to get the first 10 customers without social media?

### Takeaway
Go **through the institutions that already carry the complaint**:
- **UIC** (Manuali raised the GUDI cost issue at its executive committee and runs an energy price index);
- **CLAUTO** (organized the EPEC meeting);
- **CIMCC**;
- **IPA nationally** (asks for "asistencia técnica");
- the **Santa Fe government** (wants deferrals and data).

A second route is partnering with consultancies or comercializadoras as a white-label tool.

### Cited Findings
- UIC executive committee discussed the "costo de energía eléctrica para los GUDI" — [UIC](https://www.uic.org.ar/blog/noticias-gremiales-2/reunion-de-comite-ejecutivo-actividad-gremial-y-planificacion-estrategica-63). The UIC asked Governor Llaryora to take the issue to Nación and requested a meeting with Energy and Mining secretary Daniel González; it asks for financing or spreading of bills — [Puntal](https://www.puntal.com.ar/tarifas/gudi-la-nueva-preocupacion-industrial-un-salto-tarifas-que-afecta-350-empresas-cordobesas-n263782)
- The CLAUTO and EPEC meeting (26 Dec 2025) involved:
  - EPEC General Manager Lucas Gumierato;
  - EPEC Commercial Manager Juan Vallini;
  - firms Sogefi, Pascuale SRL and Pertrak;
  - Carolina Puig Pujol (UIC).
  
  A UIC virtual meeting was planned for mid-January 2026, and the work was done "en conjunto con la CIMCC, UIC y el Gobierno de la Provincia de Córdoba" — [CLAUTO](https://clauto.org.ar/reduccion-de-costos-en-energia-electricidad-y-gas/)
- IPA (president Daniel Rosato) asks for a dialogue table, more information and "herramientas que permitan a las empresas adaptarse" — [El Economista](https://eleconomista.com.ar/energia/la-letra-chica-energia-pymes-denuncian-pagan-doble-lo-acordado-n98498); [La Gaceta](https://www.lagaceta.com.ar/nota/1155827/economia/industriales-pymes-denunciaron-fuertes-aumentos-costo-energia-tras-liberacion-mercado.html)
- Einstoss recommends **group purchasing through chambers of commerce or industrial parks** — [Nuevos Papeles](https://nuevospapeles.com/nota/energia-y-pymes-mismo-invierno-distinta-factura/). Clarke's "condomínios virtuais" are the Brazilian equivalent — [Clarke blog](https://blog.clarke.com.br/post/clarke-energia-ajuda-empresas-a-economizarem-ate-30-na-conta-de-luz/)
- Industry events: EconoJournal's NODO meeting and Dínamo streaming, where Sager, Werner and Bosch spoke — [Al Sur Noticias](https://alsurnoticias.com.ar/2026/09/02/electricidad-mas-de-800-grandes-industrias-dejaron-a-las-distribuidoras-y-buscan-comprar-energia-mas-barata/); [EconoJournal](https://econojournal.com.ar/?p=128978). Expo Parques Industriales Córdoba 2026 — [El Periódico](https://el-periodico.com.ar/region/epec-participo-de-la-expo-parques-industriales-cordoba-2026_a6aaf2a99ade69350b5e1682a)

### Inferences
- **Fastest path (inference):**
  1. Offer the UIC or CLAUTO a free **"Clínica de facturas GUDI"**: members send their last 12 bills, and you return a one-page explanation and next-bill forecast to each.
  2. Publish an anonymous aggregate ("how much of your bill is Cargo GUDI, by month") that the chamber can use with EPEC and Nación. That gives the chamber a reason to promote you.
  3. Convert 10 of roughly 30 participants to a paid monthly monitor.
- **Partner route:** offer Latin Energy Group, ITAndes or a Córdoba electrical-engineering firm the extraction and forecasting engine as white-label software. They have clients and spend analyst hours on bill control.
- **Avoid early on:** taking commissions from comercializadoras. Neutrality is the selling point against the free advice.
- **Timing:** winter bills (May–August consumption) arrive from July to October, and the 60% contracting step starts on 1 Apr 2027. The product must be **live by March–April 2027** to ride the next wave of pain and decisions.

### Gaps
- Not verified: whether the UIC, CIMCC or CLAUTO already have an energy-advisory partner, or would accept a vendor-run clinic.
- No contact for IPA's energy commission was found.

---

## Q6. Can one person plus Claude build it in 3–6 months? (data, technical risks, licensed partner, liability)

### Takeaway
**Mostly yes for the software; partly no for the expertise.**
- CAMMESA data is publicly reachable. I tested a public CAMMESA API endpoint, which returned 5-minute demand data.
- Bills are PDFs that a multimodal model can read.
- The hard parts are: (a) modeling the "Cargo GUDI" and passthrough rules for each distributor and cooperative; (b) reading generator contracts and DTEs correctly; (c) credibility. An electrical-engineer or energy-economist partner is needed for the methodology and any metering (SMEC) work.

### Cited Findings
- I tested `https://api.cammesa.com/demanda-svc/demanda/ObtieneDemandaYTemperaturaRegionByFecha?fecha=2026-11-18&id_region=1002`. It returned HTTP 200 with 5-minute demand and temperature data. This is my own test, run on 2026-11-20 from this environment.
- CAMMESA data are also on datos.gob.ar — [datos.gob.ar](https://datos.gob.ar/dataset?tags=Electricidad). CAMMESA publishes the monthly **DTE (Documento de Transacciones Económicas)**, which consultancies use to check generator invoices — [ITAndes](https://itandes.com.ar/contratos-de-energia/)
- The charge formulas are public: Res. 976/2023 — [official text](https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-976-2023-394390/texto); [Tavarone summary](https://tavarone.com/la-secretaria-de-energia-establece-nuevos-cargos-para-los-gudis/). Seasonal programming resolutions are public, e.g. Res. 109/2026 (winter) — [AGUEERA](https://www.agueera.com.ar/wp-content/uploads/2026/06/MEM-BO-052026.pdf)
- Joining the MEM as GUMA/GUME requires CAMMESA's favorable report on **Anexo 17** and the **SMEC** commercial metering system. Optimizar has done more than 700 SMEC projects — [AGUEERA, Res. 108/2026](https://www.agueera.com.ar/wp-content/uploads/2026/06/MEM-BO-052026.pdf); [Optimizar](https://optimizar.com.ar/servicios.html)
- Bill formats: in Córdoba there are about 150 cooperatives plus EPEC — [provincial document](https://gestionabierta.cba.gov.ar/wp-content/uploads/2023/08/20.-Energías-Renovables-e-Infraestructura-Eléctrica.pdf). Billing systems are constrained (for example, the 30-character limit on line descriptions) — [AGUEERA](https://www.agueera.com.ar/wp-content/uploads/2026/06/MEM-BO-052026.pdf)
- Powermeter shows AI extraction of Argentine distributor bills is already practical — [powermeter.io](https://www.powermeter.io/powermate)

### Inferences
- **A 3–6 month build is realistic:**
  - Month 1: bill ingestion by email or WhatsApp; extraction to a normalized schema; per-distributor templates for EPEC, the top 10 Córdoba cooperatives, Edenor/Edesur and EPE.
  - Month 2: CAMMESA data pipeline (spot and monomic prices, seasonal prices) and a **next-bill forecaster**.
  - Month 3: contract reader (price, volumes, non-delivery and take-or-pay clauses, indexation), contract-vs-billed reconciliation, and a simulator of the 3 options with a calendar of the monthly windows.
  - Months 4–6: polish, multi-site, claim-letter drafts, optional meter integration.
- **Technical risks:**
  - forecasting the ex-post true-up accurately (CAMMESA's own estimate was off by more than 3x in 2026), so present ranges, not points;
  - the long tail of cooperative bill formats;
  - generator contracts that differ from each other.
- **Licensed partner:** I found no rule that requires a license to analyze bills or advise. But:
  - SMEC and GUME entry needs engineering work;
  - acting as a comercializador requires being an MEM agent;
  - claims against generators may need a lawyer.
  
  Position the business as **software plus partner engineer**, and add disclaimers ("información, no asesoramiento regulado").
- **Liability:** a wrong forecast or a wrong recommendation to sign a contract could cost a client tens of thousands of USD. Keep recommendations as scenarios, require the client's decision, and cap liability in the terms.

### Gaps
- I did not obtain sample bills from EPEC or cooperatives, a DTE, or a generator contract to measure extraction difficulty.
- I did not verify whether CAMMESA publishes the monthly "Cargo GUDI" values or the PESTGUDI price in machine-readable form.
- I did not research professional licensing rules for energy consultants in Córdoba (COPIME, the engineers' college).

---

## Q7. Unit economics, durability, risks and kill criteria

### Takeaway
About **10–12 paying supply points at USD 100–150 per month**, plus paid diagnoses, reach USD 1,000+ per month net. Durability comes from the reform running to 2029, monthly decisions from Dec 2026, and accumulated bill history. The **main risks** are:
- prices normalizing in 2027 (Sager projects about USD 62/MWh), which would shrink the urgency;
- incumbents bundling it for free (comercializadoras, Enertoken, Powermeter);
- a political fix (Santa Fe and the UIC are asking for deferrals and financing).

### Cited Findings
- 2027 average projected at about USD 62/MWh vs about 75 in 2026 (GEINSA) — [Al Sur Noticias](https://alsurnoticias.com.ar/2026/09/02/electricidad-mas-de-800-grandes-industrias-dejaron-a-las-distribuidoras-y-buscan-comprar-energia-mas-barata/). Former Energy Secretary Flavia Royón says the GUDI charge "se va a volver negativo" when real costs fall — [Minuto de Cierre](https://www.minutodecierre.com/nota/2026-10-21-11-12-0-la-inflacion-que-el-indec-no-mide-el-cargo-a-grandes-consumidores-de-energia-que-aumento-sus-facturas-mas-del-50-entre-septiembre-y-octubre)
- Requests for relief:
  - Santa Fe asks Nación to let CAMMESA defer the June–August balances into spring and summer — [Urgente24](https://urgente24.com/actualidad/santa-fe-presiona-javier-milei-frenar-el-impacto-del-tarifazo-industrias-n629863);
  - the UIC asks for financing or for spreading the amounts — [Puntal](https://www.puntal.com.ar/tarifas/gudi-la-nueva-preocupacion-industrial-un-salto-tarifas-que-afecta-350-empresas-cordobesas-n263782)
- The reform keeps opening until 2029, with monthly windows — [Res. 293/2026](https://www.boletinoficial.gob.ar/detalleAviso/primera/349363/20261021)
- Bundling signals:
  - Enertoken plans a client portal with billing tracking — [InfoArenales](https://infoarenales.com/2026/02/14/inedito-ypf-luz-lanza-plataforma-con-tecnologia-blockchain-para-comprar-energia-electrica-online/);
  - Energeia gives free diagnoses — [energeia.ar](https://energeia.ar/servicios/);
  - in Brazil, the leading broker-accountant was bought by a utility (Energisa and Clarke) — [Brazil Journal](https://braziljournal.com/energisa-compra-a-clarke-um-corretor-e-contador-do-mercado-livre-de-energia/)

### Inferences
- **Unit economics (illustrative):**
  - Price: USD 120 per month per supply point (Córdoba launch price), plus a one-off diagnosis of USD 300.
  - 12 clients: USD 1,440 MRR, plus about 2 diagnoses a month (USD 600).
  - Costs:
    - LLM extraction about USD 2–5 per client per month;
    - hosting about USD 30;
    - 20% revenue share to the partner engineer, about USD 290;
    - taxes (monotributo or IVA) and payment fees, about 10–20%.
  - Net: about **USD 1,100–1,400 per month**.
- **Churn risk is seasonal.** Clients may cancel in summer when the Cargo GUDI falls. Annual prepaid plans, or a "winter shield" pricing, would help.
- **Durability levers:**
  1. A bill-format and tariff library for EPEC plus about 150 cooperatives (slow to copy).
  2. Each client's history of bills, contracts and demand (switching cost).
  3. Moving up the funnel to contract reconciliation for the 800+ contracted GUDIs and new GUMEs, a problem that **persists even if prices fall**.
  4. Expanding to gas contracts (Latin Energy already bundles gas) and to the Res. 379 demand-response program.
- **Kill criteria (proposed):**
  1. In 6 weeks, fewer than 5 of about 25 Córdoba GUDIs contacted through the UIC or CLAUTO share 12 bills.
  2. After a free first report, fewer than 3 pay at least USD 80 per month by month 4.
  3. If you cannot explain at least 90% of the money on a sample of 10 bills with public data, or the forecast error exceeds ±25% on back-tests of 2026.
  4. If Powermeter, EPEC or a major comercializadora launches a free GUDI bill forecast before you have 10 clients.
  5. If a resolution restores a stabilized price for GUDIs without ex-post true-ups. That would remove the forecast pain; the contract audit would then have to carry the business alone.

### Gaps
- No data on churn or retention for energy-management services in Argentina.
- No information on how often contract disputes with generators are won, or what the recovered amounts are (IPA gives no details).

---

## Q8. Verdict, scores and the sharpest MVP

### Takeaway
**A real, painful, payable and still-growing problem, but not an empty market.** Score: about **3.3/5 overall**. Go ahead only as a **neutral, Córdoba-first, forecast-and-audit tool** sold through chambers, and only after a 6-week concierge test that hits the kill criteria above. If it fails, this is better as a feature you sell to a consultancy than as your own business.

### Cited Findings
- The evidence is in Q1–Q7. The key anchors are:
  - about 6,000 GUDIs, about 800 contracted, bills up to 4–7x, contracted firms paying "up to double" — [El Economista](https://eleconomista.com.ar/energia/la-letra-chica-energia-pymes-denuncian-pagan-doble-lo-acordado-n98498); [Rosario3](https://www.rosario3.com/-economia-negocios-agro-/la-provincia-pedira-a-nacion-revisar-un-cargo-que-disparo-las-facturas-de-electricidad-en-grandes-industrias-y-comercios-20260803-0056.html);
  - a priced GUDI service at ARS 250,000 per month — [Latin Energy Group](https://www.lenergygroup.com/servicios/asesoramiento-integral/);
  - AI bill reading at USD 95 per month — [Powermeter](https://www.powermeter.io/powermate);
  - a 75-day billing lag — [EconoJournal](https://econojournal.com.ar/?p=128978);
  - about 350 Córdoba GUDIs — [Puntal](https://www.puntal.com.ar/tarifas/gudi-la-nueva-preocupacion-industrial-un-salto-tarifas-que-afecta-350-empresas-cordobesas-n263782)

### Inferences
**Scores (1–5)**

| Criterion | Score | Why |
|---|---|---|
| Unserved / novelty | **2.5–3** | Human bill control and advice exist (Latin Energy, ITAndes, Optimizar, Energeia, GEINSA, AGUEERA). Contracting platforms exist (Enertoken, EVoltia). AI bill reading exists (Powermeter). Only the GUDI-specific self-serve forecast plus contract audit plus cooperative-bill angle looks new. |
| Pain | **4** | Bills up 4–7x, the "Cargo GUDI" rose 492% in one month, IPA uses the word "estafados", and no firm can predict its next bill. It is seasonal and may ease in 2027. |
| Willingness to pay | **3** | Clear anchors at USD 95–160 per month and a savings logic worth USD 10k+ per month in a bad winter. Capped by free comercializadora advice and SMEs' cash stress. |
| Feasibility (solo + Claude, 3–6 months) | **3–3.5** | Public data, PDFs and LLM extraction are doable. Forecasting true-ups, the long tail of cooperative formats and contract reading need a domain partner. |
| Durability | **3** | Reform to 2029, monthly windows and a data moat. Risk of price normalization, political fixes and incumbent bundling. |
| Fit (Córdoba, builder skills) | **3.5–4** | About 350 GUDIs locally, chambers already active on the issue, and the work is document AI plus data pipelines, which match the builder's skills. Needs B2B selling to industrial owners. |

**Sharpest MVP: "Monitor GUDI" (Córdoba first)**
1. **Input:** the company forwards its last 12 bills (EPEC or cooperative) and, if it has one, its supply contract and the generator's invoices, by email or WhatsApp.
2. **"Tu factura explicada":** each line is extracted and classified (energy, power, Cargo Estabilizado GUDIs, Ajuste Complementario, recoveries in installments, taxes, Res. 379 items), in pesos and in USD/MWh. A chart shows how much of the bill is spot exposure.
3. **"Tu próxima factura":** a monthly forecast range for the bill that has not arrived yet (75-day lag). It uses CAMMESA public prices and the company's own demand pattern. An alert goes out when the expected jump exceeds 30%.
4. **"Contrato vs factura"** (contracted clients): price and volume vs billed. Flags for non-delivery, take-or-pay and indexation clauses. A draft claim letter for the partner or lawyer to review.
5. **"¿Me conviene cambiar?":** a simulator of the three Res. 293 options (stay GUDI; contract through EPEC or the cooperative; become GUME/GUMA). It uses the contract ceilings (20% → 60% from 1 Apr 2027 → 80% → no limit in 2029), and adds a calendar alert for the monthly entry deadline (last business day of the month before).
6. **Deliverable:** a one-page monthly PDF for the owner or CFO, plus an anonymous aggregate for the chamber.
7. **Commercial setup:**
   - concierge pilot with 5–10 UIC, CLAUTO or CIMCC members during December 2026 to February 2027;
   - paid launch before 1 Apr 2027 (the 60% step) and before winter 2027;
   - price USD 100–150 per month per supply point, plus a USD 250–400 diagnosis;
   - partner electrical engineer on revenue share;
   - no commissions from energy sellers.

**Strategic alternative if the kill criteria trigger:** sell the extraction and forecasting engine as a white-label tool to consultancies such as Latin Energy Group or ITAndes, or to Powermeter. Another option is to merge the idea with the gas-contract and demand-response features for GUMEs.

### Gaps
- No direct interviews with GUDI owners or chambers. All demand evidence comes from press and chamber statements, which have advocacy bias (IPA calls it "estafa"; government sources were not found responding).
- The officially published GUDI count and the CAMMESA forecasting inputs (whether the Cargo GUDI values are published monthly in machine-readable form) still need verification before building.
