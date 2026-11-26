# Fichas verificadas para guiones: Changan, Deepal, JMEV y Mitsubishi (Argentina, noviembre de 2026) · Valparaiso Motors

> **Método.** Investigación del 26/11/2026. Leí las páginas y fichas técnicas oficiales (changan.com.ar, deepal.com.ar, jmevargentina.com.ar y mitsubishi-motors.com.ar) y los datos que alimentan sus localizadores de concesionarios. Bajé los avisos de Mercado Libre de Córdoba y el sitio de Valparaiso, y abrí pruebas de prensa argentina.
>
> **Etiquetas de cada dato:**
> - **oficial:** página o ficha de la marca.
> - **medido por prensa:** prueba con números propios del medio.
> - **declarado (prensa):** dato de la marca repetido por un medio.
> - **promo:** precio o financiación con vigencia.
> - **aviso:** publicación de un vendedor.
> - **otro mercado:** dato de Chile, México, Uruguay o España (no vale para Argentina sin verificar).
> - **resumen de búsqueda:** frase del buscador; no pude abrir la nota.
>
> **Fecha de las fichas PDF** (metadatos del archivo):
> - Eado Plus: 03/08/2026.
> - CS55 Plus: 18/11/2025.
> - Deepal S05: 30/09/2026.
> - L200: brochure modificado el 09/06/2025.
> - Outlander: 10/12/2024.
>
> **Ojo:** los precios en USD son "sugeridos según cotización oficial del BNA" y cambian seguido. Confirmarlos el día que se publica.

---

## 1. ¿Valparaiso es concesionario oficial Changan? ¿Qué lista hoy en su sitio y en Mercado Libre?

### Takeaway
- **Changan sí lo lista como concesionario oficial en Córdoba.** Lo verifiqué el 26/11/2026 en los datos de su localizador. Con esto se puede cerrar el "verificar" de la sección 1 del CLAUDE.md: el vendedor puede decir "concesionario oficial Changan".
- **Valparaiso NO figura como taller oficial (posventa) de Changan.** En Córdoba, el único taller listado es City Drive.
- Los localizadores de Deepal y JMEV usan **la misma lista de 42 puntos** que Changan, con Valparaiso incluido.
- Mitsubishi lo lista en su propio localizador.
- **Precios de Valparaiso en Mercado Libre hoy (todos "0 km", modelo 2027):**

| Modelo | Valparaiso (ML) | Precio sugerido de la marca |
|---|---|---|
| Changan Eado Plus | US$27.800 | US$29.990 |
| Changan CS55 Plus | US$29.399 | US$31.990 |
| Deepal S05 | US$33.900 | US$34.000 (preventa) |
| JMEV Easy 3 | US$17.899 | US$17.900 |
| Mitsubishi L200 | US$48.989 | US$51.500 (con bonificación) |
| Mitsubishi Outlander | US$46.996 | US$51.500 (con bonificación) |

### Cited Findings
**Localizadores oficiales (oficial)**
- **Changan.** El localizador oficial (página `/concesionarios`) carga su lista de `/api/config`, actualizada el 26/11/2026 según el campo `_dex_fetched_at`. Ahí figura:
  - "Valparaiso Motors · tipo: concesionario · Av. Valparaiso 4380, Cordoba", con enlace a `https://changan.valparaisomotors.com.ar/`;
  - en el selector de sucursales, "Córdoba (Valparaíso Motors)" y "Córdoba (Tagle)".
  - [Changan Argentina, concesionarios](https://changan.com.ar/concesionarios); [datos del localizador](https://changan.com.ar/api/config)
- **Talleres en Córdoba.** En la misma lista, el único "taller" de Córdoba es **City Drive**: Colectora Av. de Circunvalación Agustín Tosco 3371. Valparaiso no aparece como taller — [datos del localizador Changan](https://changan.com.ar/api/config)
- **Deepal y JMEV.** Sus localizadores devuelven la misma lista de 42 puntos, con Valparaiso como "concesionario" y City Drive como único taller de Córdoba — [Deepal, datos del localizador](https://deepal.com.ar/api/config); [JMEV, datos del localizador](https://jmevargentina.com.ar/api/config)
- **Mitsubishi.** El localizador oficial lista "Valparaiso Motors, Av. Ciudad de Valparaiso 4380, Córdoba" (verificado el 24/11/2026 en notas previas) — [Mitsubishi Argentina, concesionarios](https://www.mitsubishi-motors.com.ar/dealers)

**Lo que dice Valparaiso de sí mismo**
- **Subsitio Changan** (el enlace que da la marca):
  - dice "Concesionario oficial Changan";
  - muestra solo **CS55 Plus PHEV** y **EADO Plus PHEV**;
  - publica el CS55 Plus "desde USD 31.990" (sin impuestos nacionales: USD 26.438).
  - [changan.valparaisomotors.com.ar](https://changan.valparaisomotors.com.ar/)
- **"Nosotros" del sitio:** "Representamos las marcas internacionales Mitsubishi Motors, GWM (HAVAL, ORA, POER y TANK), Changan, Deepal y JMEV. Próximamente sumaremos XPENG y SOUEAST" — [valparaisomotors.com.ar/nosotros](https://valparaisomotors.com.ar/nosotros/)
- **Fichas del sitio** (bajadas el 26/11/2026):
  - **Eado** ([ficha](https://valparaisomotors.com.ar/listing/changan-eado-phev-plus/)):
    - "PHEV PLUS", colores Dark Grey, Silver Grey y White Pearl;
    - sin precio ("Consultar").
  - **CS55 Plus 2026 con km:**
    - 700 km: USD 28.999 ([ficha](https://valparaisomotors.com.ar/listing/changan-cs55-plus-1-5-phev-dht-2026-3/));
    - 1.000 km: USD 30.500 ([ficha](https://valparaisomotors.com.ar/listing/changan-cs55-plus-1-5-phev-dht-2026/));
    - 10.000 km: USD 31.295 tachado → USD 28.447 ([ficha](https://valparaisomotors.com.ar/listing/changan-cs55-plus-1-5-phev-dht-2026-2/)).
  - **JMEV Easy 3:**
    - 2026 con 1.800 km: $25.900.000 → $23.543.100 ([ficha](https://valparaisomotors.com.ar/listing/jmev-easy-easy-3-2026/));
    - otra ficha sin precio ([ficha](https://valparaisomotors.com.ar/listing/jmev-easy-easy-3/)).
  - **Mitsubishi:** solo usados (L200 2017 y 2019, Outlander 2012).
  - Todas las fichas dicen "Financiación destacada: Bancor – Línea UVA" con la tasa vacía.

**Mercado Libre, Córdoba (aviso, 26/11/2026)**
- **Changan.** Valparaiso publica ([ML Changan Córdoba](https://autos.mercadolibre.com.ar/changan/_PciaId_cordoba)):
  - Eado Plus PHEV 2027 0 km: **US$27.800** (3 avisos);
  - CS55 Plus 2027 0 km: **US$29.399** (varios avisos; uno dice "Hev", parece un error de carga);
  - CS55 Plus 2026: US$28.999 (700 km) y US$28.450 (11.900 km).
- **Eado Plus en otros vendedores de la provincia:**
  - DG Automotores (Carlos Paz): US$32.900;
  - Grupo Tutu (Córdoba): US$30.900;
  - Grupo Le Parc (Villa María): US$33.300.
- **Deepal S05** ([ML Deepal Córdoba](https://autos.mercadolibre.com.ar/deepal/_PciaId_cordoba)):
  - Valparaiso, 2027 0 km: **US$33.900** (2 avisos);
  - Grupo Tutu: US$35.500;
  - Le Parc: US$36.900;
  - particular: US$34.900.
- **JMEV Easy 3** ([ML JMEV Córdoba](https://autos.mercadolibre.com.ar/jmev/_PciaId_cordoba)):
  - Valparaiso, 2027 0 km: **US$17.899** y otro aviso en **$27.899.000**;
  - Grupo Tutu: US$18.900;
  - Le Parc: US$18.900 y US$19.900.
- **Mitsubishi 0 km** ([ML Mitsubishi 0 km Córdoba](https://autos.mercadolibre.com.ar/mitsubishi/0-km/_PciaId_cordoba)):
  - Valparaiso: L200 2.4 GLS 6AT 4WD Full 2027 **US$48.989**; Outlander 2.5 GLS AT Full 2027 **US$46.996**;
  - Le Parc: L200 US$49.900 y Outlander US$51.500.
- **Aviso del Eado de Valparaiso** ([MLA-2276232041](https://auto.mercadolibre.com.ar/MLA-2276232041-changan-eado-plus-phev-2027-_JM)):
  - precio US$27.800;
  - se presenta como "Concesionario Oficial Changan / Deepal / GWM / Ora / Tank / Poer";
  - dice "Al valor publicado falta agregarle gastos de flete y formularios" y "Entrega inmediata";
  - "Motor 1.5 híbrido enchufable de **215 cv**" y "Cámara de **retroceso** y faros antiniebla" **no coinciden con la ficha oficial** (ver sección 2);
  - "Baúl de 500 litros";
  - "Servicio postventa oficial, repuestos y taller autorizado".
- **Aviso del Deepal de Valparaiso** ([MLA-4180273754](https://auto.mercadolibre.com.ar/MLA-4180273754-changan-deepal-2027-_JM)):
  - US$33.900;
  - "Entrega inmediata a todo el país";
  - "Sistema híbrido enchufable de 218 cv";
  - "Baúl de 462 litros" (no encontré fuente oficial argentina);
  - "Financiación prendaria Santander".

### Inferences
- La frase **"Concesionario oficial Changan"** queda respaldada por la marca. Para decir **"service oficial Changan"** en Córdoba habría que confirmarlo con Changan o el Grupo Antelo, porque el localizador solo lista a City Drive como taller. Lo mismo vale para los avisos de Mercado Libre que dicen "postventa oficial, taller autorizado".
- Que Deepal y JMEV devuelvan la misma lista sugiere una red compartida del Grupo Antelo, no una confirmación separada por marca. Igual, en las tres webs Valparaiso aparece como "concesionario".
- **Corregir los avisos propios de Mercado Libre del Eado:**
  - el auto no tiene "215 cv": son 101 HP a nafta + 212 HP eléctrico, y la marca no declara potencia combinada;
  - trae cámara 360°, no "cámara de retroceso".
- El precio de Mercado Libre del Eado (US$27.800) está US$2.190 debajo del sugerido. Antes de ponerlo en un video, confirmar si incluye flete, formularios y bonificaciones.

### Gaps
- No confirmé si Valparaiso hace service oficial de Changan, Deepal o JMEV (puede ser un acuerdo que el localizador no muestra).
- No abrí la tienda oficial de Mercado Libre de Valparaiso entera, solo las búsquedas por marca en Córdoba (la tienda estaba en notas previas del 24/11/2026).
- Las ubicaciones de los avisos ("Tejas del Sur", "Cerro de las Rosas") no coinciden con la dirección del local. Ya se había marcado en notas previas.

---

## 2. Changan Eado Plus PHEV: precio, ficha, mediciones y veredicto

### Takeaway
- **El precio sugerido oficial sigue en USD 29.990 en noviembre de 2026** (no subió al terminar la preventa de agosto). Valparaiso lo publica a US$27.800 en Mercado Libre.
- **La ficha oficial argentina confirma** casi todo lo del CLAUDE.md: 101 HP + 212 HP, 330 Nm eléctricos, 18,4 kWh LFP, 132 km NEDC, AC 7,4 kW, 6 airbags y ADAS, y **voz en español para ventanillas, techo, climatizador y multimedia**.
- **No pude confirmar** ningún dato de autonomía total (995 km), carga DC, V2L, tiempo de carga, cargador incluido ni despeje.
- **No hay una medición de autonomía eléctrica de la prensa argentina** que pude abrir. La Nación midió 5,7 L/100 km a nafta en ciudad.

### Cited Findings

| Dato | Valor | Fuente | Fecha | Tipo |
|---|---|---|---|---|
| Precio sugerido | USD 29.990* ("según cotización oficial del BNA") | [changan.com.ar/modelos/eado-plus](https://changan.com.ar/modelos/eado-plus); [financiación](https://changan.com.ar/financiacion) | vista 26/11/2026 | oficial |
| Precio de lista en noviembre | "US$29.990 en noviembre" | [La Nación](https://www.lanacion.com.ar/autos/asi-anda-el-changan-eado-un-sedan-chino-que-promete-1000km-de-autonomia-nid19112026/) | 19/11/2026 | declarado (prensa) |
| Precio Valparaiso | US$27.800 (2027, 0 km) + flete y formularios | [ML aviso](https://auto.mercadolibre.com.ar/MLA-2276232041-changan-eado-plus-phev-2027-_JM) | 26/11/2026 | aviso |
| Financiación Changan | "Tasa Fija 0% en 18 cuotas y Tasa UVA desde 0%", "planes de 12 a 60 meses", Santander (la página no muestra el CFT) | [changan.com.ar/financiacion](https://changan.com.ar/financiacion) | 26/11/2026 | promo |
| Motor a nafta | 1.5 L 4 cil., **101 HP / 75 kW, 136 Nm** | [Ficha técnica oficial (PDF)](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Motor eléctrico | **212 HP / 158 kW, 330 Nm** | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Potencia combinada | No declarada por la marca | [Autotest](https://autotest.com.ar/noticias/cuesta-menos-de-30-000-dolares-y-tiene-212-cv-asi-es-el-nuevo-sedan-hibrido-rival-de-toyota-corolla/) | 29/09/2026 | declarado (prensa) |
| Transmisión / tracción | "Triple embrague electrificada", delantera | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Batería | LFP **18,4 kWh** | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Autonomía eléctrica | **132 km (NEDC)** | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Autonomía total | La web oficial muestra "0 km" (marcador vacío); la ficha no la da | [changan.com.ar](https://changan.com.ar/modelos/eado-plus) | 26/11/2026 | oficial (dato faltante) |
| Carga | "Soporta carga en AC – **7,4 kW**" (no menciona DC) | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Modos | EV, HEV, iDD Sport | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Medidas | 4.770 × 1.840 × 1.460 mm; entre ejes **2.765 mm** | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Peso | 1.555 kg en vacío; 1.965 kg de peso bruto | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Neumáticos | 225/45 R18, llantas bitono | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Rueda de auxilio | **No tiene** | [La Nación](https://www.lanacion.com.ar/autos/asi-anda-el-changan-eado-un-sedan-chino-que-promete-1000km-de-autonomia-nid19112026/) | 19/11/2026 | prensa |
| Baúl | **500 litros** | [Autotest](https://autotest.com.ar/noticias/cuesta-menos-de-30-000-dolares-y-tiene-212-cv-asi-es-el-nuevo-sedan-hibrido-rival-de-toyota-corolla/) | 29/09/2026 | declarado (prensa); no está en la ficha |
| Pantallas | Instrumentos 12,25" + táctil 13,2" | [La Nación](https://www.lanacion.com.ar/autos/asi-anda-el-changan-eado-un-sedan-chino-que-promete-1000km-de-autonomia-nid19112026/) | 19/11/2026 | declarado (prensa) |
| Conectividad | CarPlay y Android Auto inalámbricos | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Asistente de voz | "Sistema de control por voz inteligente **en español** (opera ventanillas, techo solar, climatizador y funciones multimedia)" | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Asistente de voz (otro mercado) | Se activa con "Hola Changan" | [Changan Chile](https://www.changan.cl/vehiculo/eado-plus-idd/) | vista 26/11/2026 | otro mercado |
| Airbags | 6 (frontales, laterales delanteros, cortina) + ISOFIX | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| ADAS | IACC (crucero adaptativo inteligente), TJA (asistente en tránsito), LKC (centrado de carril), FCW (alerta de colisión), AEB (frenado autónomo) | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Cámaras | Cámara 360° HD + **dashcam integrada** | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Otros controles | ABS+EBD, BA/EBA, ESP, TCS, EPB + Auto-Hold, TPMS | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Confort | Techo solar panorámico eléctrico antipinzamiento; cuero ecológico microperforado; butaca del conductor eléctrica; climatizador automático con salidas atrás; filtro PM2.5 con ionizador; **apoyabrazos delantero refrigerado**; manijas con sensor de proximidad; **arranque remoto del motor** desde la llave; USB adelante y atrás | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Colores | White Pearl, Silver Grey, Dark Grey | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Importador / origen | CHAN-ONE S.A. (Tortuguitas); origen China. La ficha aclara que los datos "podrán estar sujetos a validación y/o ajustes finales al momento del arribo" | [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf) | 03/08/2026 | oficial |
| Garantía | 5 años o 150.000 km (vehículo) | resumen de búsqueda sobre notas de preventa ([Automundo](https://automundo.com.ar/changan-eado-plus-phev-preventa-argentina/); [16 Válvulas](https://www.16valvulas.com.ar/nuevo-changan-eado-plus-phev-preventa-en-argentina-desde-us-29-990/)) | 08/2026 | declarado (prensa), sin abrir la nota |
| Consumo medido | **5,7 L/100 km** con el motor a nafta funcionando, uso mayormente urbano | [La Nación](https://www.lanacion.com.ar/autos/asi-anda-el-changan-eado-un-sedan-chino-que-promete-1000km-de-autonomia-nid19112026/) | 19/11/2026 | medido por prensa |
| 0–100 km/h | 7,5 s | resumen de búsqueda de la [crítica de Autoblog](https://autoblog.com.ar/critica-changan-eado-plus-phev-2026/) (la página devolvió 403) | 2026 | medido por prensa, sin poder abrirlo |
| Autonomía eléctrica real | Autoblog: "un poco menos, pero no tanto" que la declarada (sin número en el fragmento) | resumen de búsqueda de [Autoblog](https://autoblog.com.ar/critica-changan-eado-plus-phev-2026/) | 2026 | sin número |
| Autonomía eléctrica (otros mercados) | Chile y México: 120 km NEDC; total 1.042 km (Chile) | [Changan Chile](https://www.changan.cl/vehiculo/eado-plus-idd/) | 2026 | otro mercado |
| Autonomía eléctrica (otros mercados) | Uruguay: 125 km CLTC / 108 km WLTP | resumen de búsqueda de [Autoblog Uruguay](https://www.autoblog.com.uy/2025/07/lanzamiento-changan-eado-plus-idd.html) | 07/2025 | otro mercado |
| Prueba de la marca | 170 km solo eléctrico a 80 km/h promedio, en una ruta de prueba de la marca | resumen de búsqueda de [Revista Magazzine](https://revistamagazzine.com/ligeros/changan-puso-a-prueba-su-nueva-gama-hibrida-enchufable-idd/) | ~2025 | otro mercado, dato de marca |

**Veredicto de la prensa**
- **La Nación (19/11/2026)** — [nota](https://www.lanacion.com.ar/autos/asi-anda-el-changan-eado-un-sedan-chino-que-promete-1000km-de-autonomia-nid19112026/):
  - a favor: "ágil" por el torque instantáneo; buen andar en ciudad y ruta; acceso sin llave; salidas de aire atrás; USB atrás; apoyabrazos refrigerado; cámara 360 con dashcam "de buena calidad";
  - en contra: no tiene rueda de auxilio.

### Inferences
- **Los dos números del CLAUDE.md se sostienen:** 132 km NEDC y 330 Nm.
- **"995 km de autonomía total"** no aparece en ninguna fuente oficial argentina que pude leer: la web muestra "0 km" y la ficha no lo da. Hasta confirmarlo, en pantalla conviene usar "casi mil kilómetros (declarado)" con la fuente de prensa, o no usarlo.
- **E12 "Le hablamos en cordobés al auto":** la ficha oficial respalda los pedidos "poné el aire" y "abrime el techo" (comandos de climatizador y techo solar). Que entienda tonada o modismos no tiene fuente: se muestra lo que pase.
- **MOF n.º 10 "Este sedán es más largo que esta SUV":** se confirma. El Eado mide 4.770 mm y el Deepal S05, 4.620 mm. Pero el S05 tiene más entre ejes (2.880 contra 2.765 mm). Hay que decir "más largo", no "más espacio".
- **El 132 km NEDC es de laboratorio.** En otros mercados el mismo auto declara 120 km NEDC o 108 km WLTP. Para E10 y E11 (Cosquín, un día sin nafta) hay que mostrar lo medido por Valparaiso, como ya dicen los guiones.

### Gaps
- **Sin datos confirmados para Argentina:**
  - tiempo de carga AC de 0 a 100 %;
  - si trae cargador portátil para enchufe común;
  - carga DC;
  - V2L;
  - despeje;
  - tanque (Chile dice 51 L en la ficha y 48 L en el legal);
  - consumo homologado;
  - intervalos y precios de service.
- No pude abrir la prueba completa de Autoblog (403). No hay medición de autonomía eléctrica de prensa argentina.
- **Garantía de batería** (8 años / 150.000 km en el CLAUDE.md): no la reverifiqué en esta sesión. La web oficial muestra imágenes de garantía sin texto.
- No encontré recalls ni quejas en Argentina.

---

## 3. Deepal S05 PHEV: ¿ya se entrega o sigue en preventa? Precio y ficha

### Takeaway
- **La web oficial (26/11/2026) sigue mostrando "Precio de preventa USD 34.000".**
- En Mercado Libre ya hay unidades "0 km". Valparaiso publica US$33.900 y "Entrega inmediata a todo el país".
- **Ficha oficial:**
  - 86 CV a nafta + 218 CV eléctricos;
  - 18,4 kWh;
  - "100 km o superior (ciclo LEV2)";
  - AC 6,6 kW en "6 horas o menos";
  - pantalla de 15,4";
  - cámara 540° con chasis transparente;
  - **garantía de 7 años / 200.000 km** (la prensa dijo 150.000 km) y batería de 8 años / 150.000 km.
- **Financiación Santander:** 0 % TNA en 18 cuotas hasta $20.000.000, **con CFTEA mínimo de 43,72 %** (incluye el seguro).

### Cited Findings

| Dato | Valor | Fuente | Fecha | Tipo |
|---|---|---|---|---|
| Precio | "Precio de preventa · DEEPAL S05 · USD 34.000" | [deepal.com.ar/s05](https://deepal.com.ar/s05) | vista 26/11/2026 | oficial |
| Precio de lanzamiento | U$S 34.000, versión única | [16 Válvulas](https://www.16valvulas.com.ar/nuevo-deepal-s05-phev-lanzamiento-en-argentina-desde-us-34-000/) | 02/10/2026 | declarado (prensa) |
| Debut | Expo Auto Chino 2026, Grupo Antelo | [Autocosmos](https://noticias.autocosmos.com.ar/2026/10/02/deepal-s05-debuta-en-expo-auto-chino) | 02/10/2026 | prensa |
| Precio Valparaiso | US$33.900 (2027, 0 km), "Entrega inmediata a todo el país" + flete y formularios | [ML aviso](https://auto.mercadolibre.com.ar/MLA-4180273754-changan-deepal-2027-_JM) | 26/11/2026 | aviso |
| Otros vendedores en Córdoba | Grupo Tutu US$35.500; Le Parc US$36.900; particular US$34.900 | [ML Deepal Córdoba](https://autos.mercadolibre.com.ar/deepal/_PciaId_cordoba) | 26/11/2026 | aviso |
| Financiación tasa fija | "Hasta $20.000.000 en 18 cuotas a Tasa Fija 0% TNA a través de Santander". Línea de 12 a 60 meses, TNA 0 % a 30,50 %, **CFTEA mín. 43,72 % y máx. 89,64 %** (con seguro). Monto $4M a $71M | [deepal.com.ar/financiacion](https://deepal.com.ar/financiacion) | 26/11/2026 ("válido para las operaciones solicitadas en el día de hoy") | promo |
| Financiación UVA | Ajustable por CER, TNA 0 % a 9,50 %, de 12 a 48 meses, **CFTEA 45,44 % a 57,95 %**. Ejemplo: $10M = 4.518 UVAs al 25/11/2026, 48 meses: 1.ª cuota $267.856,37 + $200.000 de seguro | [deepal.com.ar/financiacion](https://deepal.com.ar/financiacion) | 25–26/11/2026 | promo |
| Motor a nafta | 1.5 L atmosférico (1.497 cm³), **63 kW / 86 CV, 122 Nm** | [Ficha oficial (PDF)](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Motor eléctrico | Síncrono de imanes permanentes, delantero, **160 kW / 218 CV, 320 Nm** | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Transmisión / tracción | Automática de una relación; delantera | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Velocidad máxima | 180 km/h | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Batería | LFP **18,4 kWh**, con precalentamiento de serie | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Autonomía eléctrica | "**100 o superior (ciclo LEV2)**" | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Autonomía total | "A confirmar" | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Carga | AC **6,6 kW**, "**6 horas o menos**", Tipo 2 (no menciona DC) | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Medidas | 4.620 × 1.900 × 1.600 mm; entre ejes **2.880 mm**; 245/45 R20 | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Auxilio | **Kit de reparación de pinchazos** (sin rueda de auxilio) | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Baúl | 462 L según el aviso de Valparaiso; sin fuente oficial argentina | [ML aviso](https://auto.mercadolibre.com.ar/MLA-4180273754-changan-deepal-2027-_JM) | 26/11/2026 | aviso (verificar) |
| Pantalla / procesador | Táctil 15,4" 2.5K; Qualcomm Snapdragon 8155; 8 parlantes; WiFi; radio DAB | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Voz | "Asistente de voz inteligente con **diálogo continuo y reconocimiento de doble zona**"; interfaz en español e inglés | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Cámaras | **540°** con vista 2D/3D y **"chasis transparente"**; DVR perimetral; cámara HD frontal | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Cámara de techo 4K | "Cámara 4K integrada en el techo... con estabilización" (está en la web, no en la ficha) | [deepal.com.ar/s05](https://deepal.com.ar/s05) | 26/11/2026 | oficial (verificar en la unidad) |
| Control remoto | "Entrada y salida del vehículo por control remoto (RSIO)" | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial (verificar en la unidad) |
| Airbags | 6 | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| ADAS | ACC con Stop & Go; IACC con centrado de carril (LCC), asistente de embotellamiento (TJA) y desplazamiento inteligente (LDC); FCW; AEB para vehículos, peatones y ciclistas; LAEB; LDW, LKA y ELK; HMA; BSD y LCA; RCW, RCTA y RCTB; DOW; alerta de exceso de velocidad. Hardware: 3 radares, 6 ultrasónicos y 5 cámaras | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Diseño | Puertas **sin marco**, manijas ocultas, llantas de 20" | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Interior | Tapizado **de tela**; butaca del conductor eléctrica (6 posiciones) y del acompañante (4); climatizador monozona; portón manual | [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Garantía | Gráfico de la ficha: **vehículo 7 años o 200.000 km**; **batería 8 años o 150.000 km** | [Ficha oficial, p. 2 y 5](https://deepal.com.ar/s05/DEEPAL-FT.pdf) | 30/09/2026 | oficial |
| Garantía (prensa) | Vehículo 7 años / **150.000 km**; batería 8 años / 150.000 km | [16 Válvulas](https://www.16valvulas.com.ar/nuevo-deepal-s05-phev-lanzamiento-en-argentina-desde-us-34-000/) | 02/10/2026 | declarado (prensa); **contradice la ficha** |
| Mediciones en Argentina | No encontré ninguna prueba argentina con datos medidos | — | — | — |
| Mediciones en España | 5,1 L/100 km y 11,3 kWh/100 km (computadora de a bordo) | resumen de búsqueda de [eldiario.es](https://www.eldiario.es/motor/novedades/volante-tecnologico-eficiente-changan-deepal-s05-phev_1_13389276.html) | 2026 | otro mercado |
| Estimación en España | 75–90 km eléctricos reales en uso mixto (orientativo, no medido) | resumen de búsqueda de [menorca.info](https://www.menorca.info/actualidad/motor-1/2026/10/16/2730077/prueba-del-changan-deepal-s05-phev-calidad-complejos.html) | 16/10/2026 | otro mercado |

### Inferences
- **"¿Ya se entrega?":** la marca todavía lo llama preventa, pero hay 0 km publicados con "entrega inmediata" por varios vendedores de Córdoba. Para decir "entrega inmediata" en un video, confirmar ese día que hay unidad patentable en el salón (regla de la sección 5 del CLAUDE.md).
- **La promo "0 % TNA" tiene un CFTEA mínimo de 43,72 %** (por el seguro). Sirve de ejemplo real para el video de créditos ("no mires solo la tasa"). En la línea UVA, el 0 % convive con ajuste por CER: nunca decir "sin interés".
- **El CLAUDE.md dice "218 CV, 4,62 m, tracción delantera, ~100 km":** se confirma. Hay que agregar que el motor a nafta tiene 86 CV y que el ciclo declarado es "LEV2", no NEDC ni WLTP.
- **Garantía:** usar la cifra de la ficha oficial (7 años / 200.000 km) y confirmarla con Deepal, porque la prensa dijo 150.000 km.

### Gaps
- Fecha real de inicio de entregas en Argentina: no publicada.
- Sin datos oficiales argentinos de:
  - baúl;
  - despeje;
  - consumo;
  - carga DC;
  - V2L;
  - si trae cargador portátil.
- El dato "Changan fabricó 243.894 autos en un año" del video original no lo pude verificar.
- La cifra global "300.000 S05 entregados" (05/11/2026) apareció solo en un resumen que cita a Wikipedia; no la verifiqué.

---

## 4. Changan CS55 Plus PHEV (SUV)

### Takeaway
- **Precio oficial hoy: USD 31.990** (bajó de USD 32.000 en el lanzamiento de noviembre de 2025). Valparaiso lo publica a **US$29.399** en Mercado Libre.
- **Es el modelo con más pruebas medidas en Argentina:**
  - Parabrisas: 21,7 km/l en ciudad sin recargar y 0–100 en 7,6 s;
  - Autotest: 4,5 L/100 km en ciudad y baúl de 475 L;
  - La Nación: 6,6 L/100 km mixto real.
- Declara 125 km eléctricos (CLTC) y 1.215 km totales (CLTC). Autotest estima "hasta 100 km" eléctricos reales.

### Cited Findings

| Dato | Valor | Fuente | Fecha | Tipo |
|---|---|---|---|---|
| Precio sugerido | **USD 31.990**; sin impuestos nacionales USD 26.438 | [changan.com.ar/modelos/cs55](https://changan.com.ar/modelos/cs55); [Valparaiso Changan](https://changan.valparaisomotors.com.ar/) | vista 26/11/2026 | oficial |
| Precio de lanzamiento | USD 32.000, versión única | [Parabrisas](https://parabrisas.perfil.com/noticias/test/como-es-el-suv-mediano-hibrido-encufable-mas-barato-de-la-argentina.phtml); [Autotest](https://autotest.com.ar/pruebas/changan-cs55-plus-suv-test-drive/) | 02/2026 y 06/2026 | prensa |
| Precio Valparaiso | US$29.399 (2027, 0 km); unidades 2026 con km de US$28.447 a US$30.500 | [ML Changan Córdoba](https://autos.mercadolibre.com.ar/changan/_PciaId_cordoba); [sitio](https://valparaisomotors.com.ar/listing/changan-cs55-plus-1-5-phev-dht-2026-3/) | 26/11/2026 | aviso |
| Motores | Eléctrico **212 hp**; a nafta **109 hp**; 1.5 L; caja DHT | [Ficha oficial (PDF)](https://changan.com.ar/FT%20-%20Changan%20-%20CS55%20PLUS%20PHEV.pdf) | 18/11/2025 | oficial |
| Torque | Nafta 143 Nm; eléctrico 330 Nm. Potencia combinada no oficial (Parabrisas calcula 268 CV) | [Parabrisas](https://parabrisas.perfil.com/noticias/test/como-es-el-suv-mediano-hibrido-encufable-mas-barato-de-la-argentina.phtml) | 26/02/2026 | declarado (prensa) |
| Modos | EV 100 %, HEV, **REEV** (el motor a nafta solo carga), IEM inteligente; Sport, Eco y Normal | [Ficha oficial](https://changan.com.ar/FT%20-%20Changan%20-%20CS55%20PLUS%20PHEV.pdf) | 18/11/2025 | oficial |
| Batería | 18,4 kWh LFP | [Parabrisas](https://parabrisas.perfil.com/noticias/test/como-es-el-suv-mediano-hibrido-encufable-mas-barato-de-la-argentina.phtml) | 26/02/2026 | declarado (prensa) |
| Autonomía eléctrica | 125 km (fabricante); Autotest: "hasta 100 kilómetros" en modo eléctrico | [Parabrisas](https://parabrisas.perfil.com/noticias/test/como-es-el-suv-mediano-hibrido-encufable-mas-barato-de-la-argentina.phtml); [Autotest](https://autotest.com.ar/pruebas/changan-cs55-plus-suv-test-drive/) | 02/2026 y 06/2026 | declarado / estimado por prensa |
| Autonomía total | **1.215 km CLTC** | [changan.com.ar/modelos/cs55](https://changan.com.ar/modelos/cs55) | 26/11/2026 | oficial |
| Autonomía total observada | "cerca de los 870 kilómetros" | [La Nación](https://www.lanacion.com.ar/autos/suv-hibrido-enchufable-vs-naftero-cuanto-se-ahorra-en-tres-anos-de-uso-en-la-argentina-nid18062026/) | 18/06/2026 | medido por prensa |
| Carga | 30–80 % en 50 min con AC doméstica, según la marca | resumen de búsqueda de [LM Neuquén](https://www.lmneuquen.com/autos/changan-cs55-plus-el-auto-hibrido-minimalista-futurista-y-volante-deportivo-cuanto-cuesta-argentina-n1248514) | ~11/2025 | declarado (sin abrir; verificar) |
| Consumo (Parabrisas) | Sin recarga: ciudad **21,7 km/l**; 90 km/h 15,6 km/l; 120 km/h 12 km/l | [Parabrisas](https://parabrisas.perfil.com/noticias/test/como-es-el-suv-mediano-hibrido-encufable-mas-barato-de-la-argentina.phtml) | 26/02/2026 | medido por prensa |
| Prestaciones (Parabrisas) | 0–100: **7,6 s** (Sport); 80–120: 5,7 s; máxima 186,3 km/h | [Parabrisas](https://parabrisas.perfil.com/noticias/test/como-es-el-suv-mediano-hibrido-encufable-mas-barato-de-la-argentina.phtml) | 26/02/2026 | medido por prensa |
| Consumo (Autotest) | Urbano **4,5 L/100 km**; 100 km/h 5,3; 130 km/h 8,5; promedio de la semana 5,7 (no aclara el estado de la batería) | [Autotest](https://autotest.com.ar/pruebas/changan-cs55-plus-suv-test-drive/) | 25/06/2026 | medido por prensa |
| 0–100 (Autotest) | 8,2 s en el texto; 8,1 s en la tabla | [Autotest](https://autotest.com.ar/pruebas/changan-cs55-plus-suv-test-drive/) | 25/06/2026 | medido por prensa |
| Consumo (La Nación) | **6,6 L/100 km** mixto real, sin técnicas de ahorro | [La Nación](https://www.lanacion.com.ar/autos/suv-hibrido-enchufable-vs-naftero-cuanto-se-ahorra-en-tres-anos-de-uso-en-la-argentina-nid18062026/) | 18/06/2026 | medido por prensa |
| Baúl | **475 L** | [Autotest](https://autotest.com.ar/pruebas/changan-cs55-plus-suv-test-drive/) | 25/06/2026 | declarado (prensa) |
| Medidas | 4.539 × 1.865 × 1.680 mm; entre ejes 2.656 mm | [Parabrisas](https://parabrisas.perfil.com/noticias/test/como-es-el-suv-mediano-hibrido-encufable-mas-barato-de-la-argentina.phtml) | 26/02/2026 | declarado (prensa) |
| Neumáticos | 225/55 R19 | [Ficha oficial](https://changan.com.ar/FT%20-%20Changan%20-%20CS55%20PLUS%20PHEV.pdf) | 18/11/2025 | oficial |
| Pantallas y voz | Tablero LCD 10"; central 12,3"; **interacción por voz inteligente en inglés y español**; carga inalámbrica; **reducción activa de ruido**; CarPlay y Android Auto | [Ficha oficial](https://changan.com.ar/FT%20-%20Changan%20-%20CS55%20PLUS%20PHEV.pdf) | 18/11/2025 | oficial |
| ADAS | ACC e IACC (nivel 2), LDW, FCW, punto ciego con asistente de cambio de carril y alerta de apertura de puertas, centrado de carril, TJA, AEB (autos y peatones), **estacionamiento automático**, grabación panorámica 360 | [Ficha oficial](https://changan.com.ar/FT%20-%20Changan%20-%20CS55%20PLUS%20PHEV.pdf) | 18/11/2025 | oficial |
| Airbags | La ficha lista conductor, pasajero y cortina (no da el número total) | [Ficha oficial](https://changan.com.ar/FT%20-%20Changan%20-%20CS55%20PLUS%20PHEV.pdf) | 18/11/2025 | oficial |
| Confort | Techo panorámico eléctrico (con cierre automático si llueve); portón eléctrico con sensor; butaca del conductor eléctrica con memoria | [Ficha oficial](https://changan.com.ar/FT%20-%20Changan%20-%20CS55%20PLUS%20PHEV.pdf) | 18/11/2025 | oficial |
| Garantía | 5 años / 150.000 km; componentes eléctricos 8 años / 150.000 km | [Autotest](https://autotest.com.ar/pruebas/changan-cs55-plus-suv-test-drive/) | 25/06/2026 | declarado (prensa) |
| Rueda de auxilio | **No tiene** (kit de reparación; Parabrisas menciona asistencia en ruta gratis) | [Parabrisas](https://parabrisas.perfil.com/noticias/test/como-es-el-suv-mediano-hibrido-encufable-mas-barato-de-la-argentina.phtml); [Autotest](https://autotest.com.ar/pruebas/changan-cs55-plus-suv-test-drive/) | 2026 | prensa |
| Costo en 3 años vs Corolla Cross | ~$6,5 millones menos (combustible + precio + patente en **CABA**, con nafta a $2.043 y dólar a $1.460) | [La Nación](https://www.lanacion.com.ar/autos/suv-hibrido-enchufable-vs-naftero-cuanto-se-ahorra-en-tres-anos-de-uso-en-la-argentina-nid18062026/) | 18/06/2026 | cálculo de prensa |

**Veredicto de la prensa**
- **Parabrisas:**
  - a favor: prestaciones, respuesta y equipamiento;
  - en contra: no tiene auxilio, no tiene levas y hay poca información técnica oficial;
  - lo describe como "el SUV mediano híbrido enchufable más barato" en febrero de 2026.
- **Autotest:**
  - a favor: relación precio/producto, equipamiento, comportamiento y consumos;
  - en contra: sin auxilio y valor de reventa.

### Inferences
- **Para la "cuenta de la nafta" conviene el CS55 Plus**, porque es el que más mediciones de prensa tiene.
- El ahorro de patente de La Nación vale para CABA, no para Córdoba: no usarlo sin verificar el régimen cordobés.
- **Es más corto que el Eado:** 4,54 m contra 4,77 m. Sirve para el juego de "¿cuál es más largo?" (E24).

### Gaps
- Sin tiempo de carga de 0 a 100 % confirmado ni dato de cargador incluido, V2L, carga DC ni despeje.
- No hay medición de autonomía eléctrica pura.
- La cantidad de airbags no figura en la ficha.

---

## 5. JMEV Easy 3 (eléctrico)

### Takeaway
- **Precio oficial hoy: USD 17.900** (sin impuestos nacionales: USD 13.966,94), con **"Wallbox gratis"** (la instalación la paga el comprador).
- Valparaiso lo publica a **US$17.899** o **$27.899.000**.
- **Parabrisas midió una autonomía real de ~285 km** (declara 330 km CLTC) y 11 km por kWh en ciudad.
- Garantía: 3 años / 100.000 km; batería, 8 años / 120.000 km.

### Cited Findings

| Dato | Valor | Fuente | Fecha | Tipo |
|---|---|---|---|---|
| Precio sugerido | **USD 17.900*** (también muestra USD 18.900); sin impuestos USD 13.966,94 | [jmevargentina.com.ar](https://jmevargentina.com.ar/) | vista 26/11/2026 | oficial |
| Wallbox | "Wallbox gratis!" y "Wallbox corre por cuenta del comprador. Chan One no se responsabiliza por la instalación" | [jmevargentina.com.ar](https://jmevargentina.com.ar/) | 26/11/2026 | oficial / promo |
| Historia del precio | Lanzamiento US$18.900; bajó a US$16.900 (lista del 31/07/2026); subió a US$17.900 en noviembre | [La Nación](https://www.lanacion.com.ar/autos/un-auto-bajo-us2000-y-se-convirtio-en-el-mas-barato-del-pais-cual-es-y-cuanto-cuesta-nid01082026/); [Autotest](https://autotest.com.ar/noticias/el-auto-mas-barato-tiene-nuevo-precio-hasta-330-km-de-autonomia-camara-360-y-pantalla-de-101-pulgadas/) | 02/08/2026 y 13/11/2026 | prensa |
| Precio Valparaiso | US$17.899 y $27.899.000 (2027, 0 km); unidad 2026 con 1.800 km a $23.543.100 | [ML JMEV Córdoba](https://autos.mercadolibre.com.ar/jmev/_PciaId_cordoba); [sitio](https://valparaisomotors.com.ar/listing/jmev-easy-easy-3-2026/) | 26/11/2026 | aviso |
| Financiación | Santander, tasa fija 0 %, hasta $15.000.000 en 18 meses | [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml); [La Nación](https://www.lanacion.com.ar/autos/un-auto-bajo-us2000-y-se-convirtio-en-el-mas-barato-del-pais-cual-es-y-cuanto-cuesta-nid01082026/) | 07/2026 y 08/2026 | promo (vigencia actual sin confirmar) |
| Motor | 50 kW (**68 CV**), 125 Nm; caja de una marcha, tracción delantera | [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml) | 09/07/2026 | declarado (prensa) |
| Prestaciones | 0–50 km/h en **4,5 s** | [Ficha (PDF alojado por 16 Válvulas)](https://www.16valvulas.com.ar/wp-content/uploads/2025/10/FT-Easy-3_compressed.pdf) | 10/2025 | oficial |
| Velocidad máxima | La ficha dice **110 km/h**; Parabrisas, "no supera los 125 km/h" | [Ficha](https://www.16valvulas.com.ar/wp-content/uploads/2025/10/FT-Easy-3_compressed.pdf); [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml) | 2025–2026 | contradicción |
| Batería | 30,24 kWh, refrigeración líquida | [Ficha](https://www.16valvulas.com.ar/wp-content/uploads/2025/10/FT-Easy-3_compressed.pdf); [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml) | 2025–2026 | oficial |
| Autonomía declarada | **330 km CLTC** (ciclo chino) | [jmevargentina.com.ar](https://jmevargentina.com.ar/); [Ficha](https://www.16valvulas.com.ar/wp-content/uploads/2025/10/FT-Easy-3_compressed.pdf) | 2025–2026 | oficial |
| Autonomía real | **~285 km**, promedio de uso urbano y extraurbano | [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml) | 09/07/2026 | medido por prensa |
| Consumo medido | **11 km por kWh** en ciudad; 7,9 km por kWh en avenidas y autopistas | [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml) | 09/07/2026 | medido por prensa |
| Carga medida | Enchufe domiciliario: del 51 % al 63 % en 1,5 h. Marca: del 20 % al 80 % en ~9 h. Cargador de 22 kW: carga completa en ~50 min | [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml) | 09/07/2026 | medido / declarado |
| Costo de carga | Carga completa ~**$5.800** con tarifa residencial, contra ~$80.000 un tanque de 40 L | [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml) | 09/07/2026 | cálculo de prensa (tarifas de julio de 2026) |
| Conectores / cargador | CCS2 (DC) + Tipo 2 (AC) detrás del logo de la parrilla. La ficha lista un "cargador de emergencia interno (cargador de batería alterna, de carga lenta)" | [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml); [Ficha](https://www.16valvulas.com.ar/wp-content/uploads/2025/10/FT-Easy-3_compressed.pdf) | 2025–2026 | oficial / prensa |
| Medidas | 3,72 m de largo; 1,64 de ancho; 1,53 de alto; entre ejes 2,39 m; 1.060 kg | [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml); [Ficha](https://www.16valvulas.com.ar/wp-content/uploads/2025/10/FT-Easy-3_compressed.pdf); [ficha Valparaiso](https://valparaisomotors.com.ar/listing/jmev-easy-easy-3-2026/) | 2025–2026 | oficial / prensa |
| Baúl | **250 L** | [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml) | 09/07/2026 | declarado (prensa) |
| Seguridad | 2 airbags frontales; ABS + EBD; control de estabilidad; asistente en pendiente; TPMS; ISOFIX; **cámara 360°**; sensores traseros | [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml) | 09/07/2026 | prensa |
| Pantalla / modos | 10,1"; modos Eco, Normal, Sport y One Pedal; control remoto por app | [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml); [Ficha](https://www.16valvulas.com.ar/wp-content/uploads/2025/10/FT-Easy-3_compressed.pdf) | 2025–2026 | prensa / oficial |
| Garantía | 3 años / 100.000 km; batería 8 años / 120.000 km | [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml); [La Nación](https://www.lanacion.com.ar/autos/un-auto-bajo-us2000-y-se-convirtio-en-el-mas-barato-del-pais-cual-es-y-cuanto-cuesta-nid01082026/) | 2026 | declarado (prensa) |

**Veredicto de Parabrisas** (09/07/2026) — [nota](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml)
- **A favor:**
  - precio;
  - agilidad en ciudad y buen radio de giro;
  - modo One Pedal;
  - seguridad completa para su segmento.
- **En contra:**
  - plásticos duros;
  - pantalla lenta y sin botones físicos;
  - butacas sin regulación de altura;
  - atrás viajan cómodos 2, no 3;
  - vibra en empedrado;
  - poca seguridad percibida en ruta;
  - carga lenta en enchufe común;
  - autonomía real "muy por debajo" de la declarada.
- Lo define como un auto de ciudad.

### Inferences
- **Para E02 ("¿cuántos km con lo que sale un café?")** el Easy 3 tiene un dato medido mejor que el WLTP del ORA 03: 11 km por kWh en ciudad, según Parabrisas. Igual hay que rotularlo "estimado" y mostrar la cuenta.
- **El gancho "el 0 km más barato del país"** salió en la prensa en agosto (La Nación). Es un superlativo que cambia con cada lista: verificarlo el día de la publicación o decir "uno de los 0 km más baratos".
- El wallbox gratis es un argumento fuerte para D05 ("¿tenés que instalar algo en tu casa?"): **viene el cargador, la instalación la pagás vos**.

### Gaps
- No pude abrir la lista de precios oficial con fecha. La web muestra USD 17.900 y USD 18.900 a la vez (probablemente precio anterior tachado).
- Potencia del wallbox incluido: no encontrada.
- Potencia máxima de carga AC y DC: no encontrada.
- V2L: no encontrado.
- Vigencia actual de la tasa 0 % de Santander: no confirmada.

---

## 6. Mitsubishi L200 (pick-up)

### Takeaway
- **En Argentina hay una sola versión, GLS 6AT 4WD Full:** lista de USD 54.000, **USD 51.500 con bonificación** (oficial, 26/11/2026). Valparaiso la publica a US$48.989.
- Carga **1.025 kg** (brochure; la web dice 1.030 kg).
- Tracción Super Select 4WD-II con **7 modos** y bloqueo trasero.
- **5 estrellas Latin NCAP (2024)** y **7 airbags**.
- Garantía corta: **3 años / 100.000 km**.
- **La capacidad de remolque no está publicada en Argentina.**

### Cited Findings

| Dato | Valor | Fuente | Fecha | Tipo |
|---|---|---|---|---|
| Precio | **USD 54.000** de lista; **USD 51.500 con bonificación**; sin impuestos nacionales USD 46.063 | [mitsubishi-motors.com.ar/vehicles/l200](https://www.mitsubishi-motors.com.ar/vehicles/l200) | vista 26/11/2026 | oficial / promo |
| Precio en mayo de 2025 | US$56.500 (~$66.670.000 al BNA) | [Parabrisas](https://parabrisas.perfil.com/noticias/test/probamos-la-nueva-mitsubishi-l200.phtml) | 09/05/2025 | prensa (antiguo) |
| Precio Valparaiso | US$48.989 (2027, 0 km) | [ML Mitsubishi 0 km Córdoba](https://autos.mercadolibre.com.ar/mitsubishi/0-km/_PciaId_cordoba) | 26/11/2026 | aviso |
| Versión | GLS, "la única que se comercializa en Argentina" | [Parabrisas](https://parabrisas.perfil.com/noticias/test/probamos-la-nueva-mitsubishi-l200.phtml) | 09/05/2025 | prensa |
| Motor | 2.4 L 4N16 MIVEC turbodiésel common rail; **184 CV a 3.500 rpm**; **430 Nm** a 2.250–2.500 rpm | [Brochure oficial (PDF)](https://www.mitsubishi-motors.com.ar/Brochure_L200_digital.pdf) | 06/2025 | oficial |
| Contradicción de potencia | La web dice "181 CV @ 3500 rpm" y "carga 1030 kg"; el brochure, 184 CV y 1.025 kg | [web L200](https://www.mitsubishi-motors.com.ar/vehicles/l200) | 26/11/2026 | oficial (contradicción) |
| Caja / 4x4 | Automática de 6 con modo Sport; **Super Select 4WD-II**, con reductora y **bloqueo de diferencial trasero** | [Brochure](https://www.mitsubishi-motors.com.ar/Brochure_L200_digital.pdf) | 06/2025 | oficial |
| Modos | **7**: Normal, Eco (2H), Tierra (4H), Nieve (4H), Barro (4HLc), Arena (4HLc) y Roca (4LLc) | [Brochure](https://www.mitsubishi-motors.com.ar/Brochure_L200_digital.pdf) | 06/2025 | oficial |
| Todoterreno | Ataque **30,4°**; ventral 23,4°; salida 22,8°; inclinación lateral **45°**; despeje **222 mm** | [Brochure](https://www.mitsubishi-motors.com.ar/Brochure_L200_digital.pdf) | 06/2025 | oficial |
| Carga | **1.025 kg**; peso bruto 3.000 kg; peso en orden de marcha 1.975 kg | [Brochure](https://www.mitsubishi-motors.com.ar/Brochure_L200_digital.pdf) | 06/2025 | oficial |
| Caja de carga | 1.555 × 1.545 × 525 mm (largo × ancho × alto); con cobertor | [Brochure](https://www.mitsubishi-motors.com.ar/Brochure_L200_digital.pdf) | 06/2025 | oficial |
| Medidas | 5.320 × 1.865 × 1.795 mm; entre ejes 3.130 mm; giro 6,2 m; tanque 75 L | [Brochure](https://www.mitsubishi-motors.com.ar/Brochure_L200_digital.pdf) | 06/2025 | oficial |
| Remolque | **No publicado** por Mitsubishi Argentina | — | — | dato faltante |
| Seguridad | **7 airbags** (incluye rodilla del conductor); **5 estrellas Latin NCAP**; FCM con peatones, LDW, LCA, RCTA, BSW, AHB, TSA (balanceo del tráiler), HDC, AYC; cámara 360° | [Brochure](https://www.mitsubishi-motors.com.ar/Brochure_L200_digital.pdf) | 06/2025 | oficial |
| Interior | Cuero; butaca eléctrica de 8 posiciones; climatizador bizona; pantalla de 9"; **CarPlay y Android Auto con cable**; cargador inalámbrico; salidas de aire atrás | [Brochure](https://www.mitsubishi-motors.com.ar/Brochure_L200_digital.pdf); [Autocosmos](https://noticias.autocosmos.com.ar/2025/11/13/test-mitsubishi-l200-la-mejor-anti-hilux) | 2025 | oficial / prensa |
| Garantía | 3 años o 100.000 km | [Brochure](https://www.mitsubishi-motors.com.ar/Brochure_L200_digital.pdf) | 06/2025 | oficial |
| Consumo (Parabrisas) | Promedio **11,2 km/l**; ciudad 9,2; 90 km/h **13,3**; 120 km/h 11,1 | [Parabrisas](https://parabrisas.perfil.com/noticias/test/probamos-la-nueva-mitsubishi-l200.phtml) | 09/05/2025 | medido por prensa (antiguo) |
| Prestaciones (Parabrisas) | 0–100 **10,9 s**; 80–120 8,6 s; máxima 177,8 km/h | [Parabrisas](https://parabrisas.perfil.com/noticias/test/probamos-la-nueva-mitsubishi-l200.phtml) | 09/05/2025 | medido por prensa |
| Consumo (Autocosmos) | Urbano 10,4 L/100 km; 120 km/h 8,1 L/100 km | [Autocosmos](https://noticias.autocosmos.com.ar/2025/11/13/test-mitsubishi-l200-la-mejor-anti-hilux) | 13/11/2025 | medido por prensa |
| Consumo (Autoweb) | 100 km/h 6,9; 130 km/h 9,5; urbano 11,1 L/100 km | resumen de búsqueda de [Autoweb](https://www.autoweb.com.ar/2025/07/11/prueba-mitsubishi-l200-gls-full/) | 11/07/2025 | medido por prensa (sin abrir) |
| Campaña de seguridad | Mitsubishi convoca a "propietarios de los vehículos Mitsubishi L200 que se indican" para cambiar el inflador del airbag del conductor (campaña iniciada por Alfacar, el distribuidor anterior; gratis, ~2 h; buscador por chasis) | [Acciones de servicio](https://www.mitsubishi-motors.com.ar/acciones-de-servicio) | vista 26/11/2026 | oficial |

**Veredicto de la prensa**
- **Parabrisas:**
  - a favor: "Calidad general", "Espacio interior" y "Aptitudes off-road";
  - en contra: "Garantía acotada", "Faltantes de seguridad" y "Sin levas";
  - su garantía es "una de las más cortas del segmento".
- **Autocosmos:**
  - "más apuntada al trabajo que al ocio";
  - en contra: dirección pesada a baja velocidad, vibraciones y Android Auto/CarPlay con cable.

### Inferences
- **E05 ("¿cuánto carga esta camioneta?")** se puede hacer con 1.025 kg (dato del brochure; avisar que la web dice 1.030 kg).
- **La campaña del airbag** parece de L200 anteriores (la convocó Alfacar). Sirve para un video de posventa ("chequeá tu chasis"), pero no hay que asociarla a la L200 nueva sin confirmar los chasis afectados.
- **Las mediciones de consumo son de 2025:** marcarlas como antiguas.

### Gaps
- Capacidad de remolque para Argentina.
- Profundidad de vadeo.
- Intervalo y precio del service.
- No hay otras versiones (4x2 o manual) en la web oficial.

---

## 7. Mitsubishi Outlander (y si hay PHEV o Montero Sport)

### Takeaway
- **Una sola versión, Outlander GLS S-AWC 2.5 nafta CVT de 7 plazas:** lista de USD 52.500, **USD 51.500 con bonificación** (oficial, 26/11/2026). Se lanzó a USD 61.000 en diciembre de 2024.
- Valparaiso la publica a US$46.996.
- **La web oficial solo tiene L200 y Outlander.** No se venden el Outlander PHEV ni el Montero Sport.

### Cited Findings

| Dato | Valor | Fuente | Fecha | Tipo |
|---|---|---|---|---|
| Gama oficial | Solo "L200" y "Outlander" en el menú de vehículos | [mitsubishi-motors.com.ar](https://www.mitsubishi-motors.com.ar/) | 26/11/2026 | oficial |
| Precio | U$D 52.500 de lista; **USD 51.500 con bonificación**; sin impuestos USD 42.562 | [web Outlander](https://www.mitsubishi-motors.com.ar/vehicles/outlander) | 26/11/2026 | oficial / promo |
| Precio de lanzamiento | USD 61.000, versión única GLS AT Full | [iProfesional](https://www.iprofesional.com/autos/418833-mitsubishi-lanza-nuevo-suv-7-plazas-argentina-cuanto-sale) | 11/12/2024 | prensa (antiguo) |
| Precio Valparaiso | US$46.996 (2027, 0 km) | [ML Mitsubishi 0 km Córdoba](https://autos.mercadolibre.com.ar/mitsubishi/0-km/_PciaId_cordoba) | 26/11/2026 | aviso |
| Motor | 2.5 L MIVEC nafta, inyección directa; **184 CV a 6.000 rpm**; 244 Nm a 3.600 (la web dice 245 Nm) | [Ficha oficial (PDF)](https://www.mitsubishi-motors.com.ar/ft_outlander.pdf); [web](https://www.mitsubishi-motors.com.ar/vehicles/outlander) | 12/2024 y 11/2026 | oficial |
| Caja / tracción | CVT ("8 velocidades"); **S-AWC** + Active Yaw Control; **6 modos**: Normal, Eco, Tierra, Asfalto, Barro y Nieve | [Ficha oficial](https://www.mitsubishi-motors.com.ar/ft_outlander.pdf) | 12/2024 | oficial |
| Plazas / baúl | **7 plazas**; baúl **331 L** | [Ficha oficial](https://www.mitsubishi-motors.com.ar/ft_outlander.pdf) | 12/2024 | oficial |
| Medidas | 4.710 × 1.897 mm; entre ejes 2.706; despeje **210 mm**; 1.690 kg; llantas de 20" | [Ficha oficial](https://www.mitsubishi-motors.com.ar/ft_outlander.pdf) | 12/2024 | oficial |
| Seguridad | 7 airbags (incluye rodilla); ADAS: mitigación de colisión, cambio de carril, punto ciego, tráfico cruzado trasero y atención del conductor | [Ficha oficial](https://www.mitsubishi-motors.com.ar/ft_outlander.pdf); [iProfesional](https://www.iprofesional.com/autos/418833-mitsubishi-lanza-nuevo-suv-7-plazas-argentina-cuanto-sale) | 12/2024 | oficial / prensa |
| Confort | Techo solar panorámico; cuero con butacas delanteras calefaccionadas; pantalla de 9" con CarPlay y Android Auto; asientos traseros 40:20:40 | [web](https://www.mitsubishi-motors.com.ar/vehicles/outlander); [Ficha](https://www.mitsubishi-motors.com.ar/ft_outlander.pdf) | 2024–2026 | oficial |
| Origen | Planta de Okazaki, **Japón** | [iProfesional](https://www.iprofesional.com/autos/418833-mitsubishi-lanza-nuevo-suv-7-plazas-argentina-cuanto-sale) | 11/12/2024 | prensa |
| Garantía | 3 años o 100.000 km | [Ficha oficial](https://www.mitsubishi-motors.com.ar/ft_outlander.pdf) | 12/2024 | oficial |

### Inferences
- **La baja de USD 61.000 (2024) a USD 51.500 con bonificación (2026)** es un dato concreto para un video de precio (V07 "Adiviná el precio"). Confirmar la bonificación el día que se publique.
- Si se habla de "híbrido" en Mitsubishi, aclarar que hoy en Argentina no hay Outlander PHEV.

### Gaps
- No encontré pruebas argentinas con consumo medido del Outlander. El consumo homologado tampoco está en la web ni en la ficha.
- No hay fecha de llegada del Outlander PHEV ni del Montero Sport.

---

## 8. Problemas conocidos, recalls y quejas (2025–2026)

### Takeaway
- **Única campaña oficial encontrada:** el inflador del airbag del conductor en L200 (convocatoria iniciada por el distribuidor anterior).
- **No encontré recalls de Changan, Deepal ni JMEV en Argentina.**
- **Contras que repite la prensa:**
  - falta de rueda de auxilio (Eado, CS55 y Deepal S05);
  - autonomía real menor a la declarada (JMEV);
  - garantía corta (Mitsubishi, 3 años).

### Cited Findings
- L200, campaña de inflador del airbag del conductor, gratuita y con buscador por chasis — [Mitsubishi, acciones de servicio](https://www.mitsubishi-motors.com.ar/acciones-de-servicio)
- **Sin rueda de auxilio:**
  - Eado Plus — [La Nación](https://www.lanacion.com.ar/autos/asi-anda-el-changan-eado-un-sedan-chino-que-promete-1000km-de-autonomia-nid19112026/);
  - CS55 Plus — [Parabrisas](https://parabrisas.perfil.com/noticias/test/como-es-el-suv-mediano-hibrido-encufable-mas-barato-de-la-argentina.phtml);
  - Deepal S05, que trae "kit de reparación de pinchazos" — [ficha Deepal](https://deepal.com.ar/s05/DEEPAL-FT.pdf).
- **JMEV Easy 3:** "autonomía real muy por debajo de la declarada" y "poca seguridad percibida en ruta" — [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml)
- **L200:** "garantía acotada", una de las más cortas del segmento — [Parabrisas](https://parabrisas.perfil.com/noticias/test/probamos-la-nueva-mitsubishi-l200.phtml)
- **CS55 Plus:** "valor de reventa" como punto en contra — [Autotest](https://autotest.com.ar/pruebas/changan-cs55-plus-suv-test-drive/)

### Inferences
- La falta de auxilio es la objeción concreta más repetida en los Changan y Deepal. Conviene que el vendedor tenga la respuesta lista: kit de reparación y asistencia en ruta (Parabrisas menciona asistencia gratis en el CS55).

### Gaps
- No revisé las alertas de Defensa del Consumidor ni de la ANSV marca por marca, ni foros de dueños. "No encontré" no quiere decir "no existen".

---

## 9. Datos listos para guion (5–8 por modelo, en una frase simple y con fuente)

### Takeaway
Frases que se pueden decir en cámara. Las marcadas **(gancho)** son las más sorprendentes. Cada número va en pantalla con su aclaración chica (ciclo, "declarado", "medido por…").

### Cited Findings

**Changan Eado Plus PHEV**
1. **(gancho)** "Lo cargás en tu casa y, según la marca, hace hasta 132 km sin usar nafta" (en pantalla: *ciclo NEDC, dato de laboratorio*) — [Ficha oficial Changan](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf)
2. **(gancho)** "Tiene dos motores: uno a nafta de 101 caballos y uno eléctrico de 212" — [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf)
3. **(gancho)** "Le hablás en español y te abre las ventanillas, el techo y te prende el aire" — [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf)
4. "Cuando anda a nafta, La Nación midió 5,7 litros cada 100 km en ciudad" — [La Nación, 19/11/2026](https://www.lanacion.com.ar/autos/asi-anda-el-changan-eado-un-sedan-chino-que-promete-1000km-de-autonomia-nid19112026/)
5. **(gancho)** "Mide 4,77 metros: es más largo que la Deepal S05, que es una SUV" (4,77 m contra 4,62 m) — [Ficha Eado](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf); [ficha Deepal](https://deepal.com.ar/s05/DEEPAL-FT.pdf)
6. "Tiene un baúl de 500 litros" — [Autotest, 29/09/2026](https://autotest.com.ar/noticias/cuesta-menos-de-30-000-dolares-y-tiene-212-cv-asi-es-el-nuevo-sedan-hibrido-rival-de-toyota-corolla/)
7. "La cámara 360 también graba como una dashcam" — [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf)
8. "Si te distraés, frena solo: trae frenado autónomo de emergencia y 6 airbags" — [Ficha oficial](https://changan.com.ar/FT-EADO-PLUS-PHEV.pdf)

**Deepal S05**
1. **(gancho)** "Su cámara te muestra lo que hay debajo del auto, como si el piso fuera transparente" (cámara 540° con "chasis transparente") — [Ficha oficial Deepal](https://deepal.com.ar/s05/DEEPAL-FT.pdf)
2. **(gancho)** "Tiene 7 años de garantía, y la batería 8" (en pantalla, los km de cada una; **confirmar** 200.000 contra 150.000 km del vehículo) — [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf)
3. "El motor eléctrico tiene 218 caballos; el de nafta, 86" — [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf)
4. "Según la marca, hace 100 km o más en eléctrico, y se carga en 6 horas o menos" (*ciclo LEV2, declarado; AC 6,6 kW*) — [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf)
5. "Tiene una pantalla de 15,4 pulgadas: más grande que muchas notebooks" (la comparación es nuestra) — [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf)
6. "Sus puertas no tienen marco y las manijas están escondidas" — [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf)
7. "Ojo: la financiación dice 0 % de tasa, pero el costo financiero total arranca en 43,72 % por el seguro" (para el video de créditos, con legal) — [Deepal financiación, 26/11/2026](https://deepal.com.ar/financiacion)
8. "Un asistente de voz con diálogo continuo te escucha a vos y al acompañante" (*reconocimiento de doble zona*; probarlo antes en la unidad) — [Ficha oficial](https://deepal.com.ar/s05/DEEPAL-FT.pdf)

**Changan CS55 Plus PHEV**
1. **(gancho)** "En ciudad, Parabrisas midió casi 22 km por litro sin cargarlo nunca" (21,7 km/l) — [Parabrisas, 26/02/2026](https://parabrisas.perfil.com/noticias/test/como-es-el-suv-mediano-hibrido-encufable-mas-barato-de-la-argentina.phtml)
2. **(gancho)** "Es una SUV familiar que llega a 100 en 7,6 segundos" (*medido por Parabrisas, modo Sport*) — [Parabrisas](https://parabrisas.perfil.com/noticias/test/como-es-el-suv-mediano-hibrido-encufable-mas-barato-de-la-argentina.phtml)
3. "Autotest midió 4,5 litros cada 100 km en ciudad" — [Autotest, 25/06/2026](https://autotest.com.ar/pruebas/changan-cs55-plus-suv-test-drive/)
4. "La marca declara 1.215 km con un tanque y la batería llenos; La Nación hizo unos 870 km reales" — [Changan](https://changan.com.ar/modelos/cs55); [La Nación, 18/06/2026](https://www.lanacion.com.ar/autos/suv-hibrido-enchufable-vs-naftero-cuanto-se-ahorra-en-tres-anos-de-uso-en-la-argentina-nid18062026/)
5. "Tiene un modo en el que el motor a nafta no mueve las ruedas: solo carga la batería" (modo REEV) — [Ficha oficial](https://changan.com.ar/FT%20-%20Changan%20-%20CS55%20PLUS%20PHEV.pdf)
6. "Estaciona solo y carga tu celular sin cable" — [Ficha oficial](https://changan.com.ar/FT%20-%20Changan%20-%20CS55%20PLUS%20PHEV.pdf)
7. "Tiene un baúl de 475 litros" — [Autotest](https://autotest.com.ar/pruebas/changan-cs55-plus-suv-test-drive/)

**JMEV Easy 3**
1. **(gancho)** "Con lo que sale llenar un tanque de 40 litros, cargás este auto más de 13 veces" (estimado: ~$80.000 contra ~$5.800 por carga, tarifas de julio de 2026; rehacer la cuenta con las tarifas de Córdoba de ese mes) — [Parabrisas, 09/07/2026](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml)
2. **(gancho)** "Viene con el cargador de pared de regalo; la instalación la pagás vos" — [JMEV Argentina](https://jmevargentina.com.ar/)
3. "La marca dice 330 km, pero en una prueba real hizo unos 285" — [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml)
4. "En ciudad hace 11 km con cada kWh" — [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml)
5. "Mide 3,72 metros: entra en cualquier cochera" — [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml)
6. "Sale de 0 a 50 en 4,5 segundos: en el semáforo arranca primero" — [Ficha JMEV](https://www.16valvulas.com.ar/wp-content/uploads/2025/10/FT-Easy-3_compressed.pdf)
7. "Trae cámara 360, algo raro en un auto de este precio" (*opinión; la cámara está confirmada*) — [Parabrisas](https://parabrisas.perfil.com/noticias/test/jmev-easy-3-auto-electrico-mas-barato-de-la-argentina.phtml)
8. "La batería tiene 8 años o 120.000 km de garantía" — [La Nación, 02/08/2026](https://www.lanacion.com.ar/autos/un-auto-bajo-us2000-y-se-convirtio-en-el-mas-barato-del-pais-cual-es-y-cuanto-cuesta-nid01082026/)

**Mitsubishi L200**
1. **(gancho)** "En la caja le cargás más de una tonelada: 1.025 kilos" — [Brochure oficial](https://www.mitsubishi-motors.com.ar/Brochure_L200_digital.pdf)
2. **(gancho)** "Puede andar inclinada 45 grados de costado" (*ángulo de inclinación lateral declarado; nunca demostrarlo en cámara*) — [Brochure](https://www.mitsubishi-motors.com.ar/Brochure_L200_digital.pdf)
3. "Tiene 7 modos de manejo, de Eco a Roca, y bloqueo del diferencial trasero" — [Brochure](https://www.mitsubishi-motors.com.ar/Brochure_L200_digital.pdf)
4. "5 estrellas en Latin NCAP y 7 airbags, uno para las rodillas del conductor" — [Brochure](https://www.mitsubishi-motors.com.ar/Brochure_L200_digital.pdf)
5. "Entre el piso y la panza hay 22 centímetros" (despeje de 222 mm) — [Brochure](https://www.mitsubishi-motors.com.ar/Brochure_L200_digital.pdf)
6. "A 90 km/h, Parabrisas midió 13,3 km por litro" (*prueba de mayo de 2025*) — [Parabrisas](https://parabrisas.perfil.com/noticias/test/probamos-la-nueva-mitsubishi-l200.phtml)
7. "Lista de USD 54.000; con la bonificación de la marca queda en USD 51.500" (*confirmar el día*) — [Mitsubishi](https://www.mitsubishi-motors.com.ar/vehicles/l200)

**Mitsubishi Outlander**
1. **(gancho)** "Siete asientos y tracción integral S-AWC con 6 modos de manejo" — [Ficha oficial](https://www.mitsubishi-motors.com.ar/ft_outlander.pdf)
2. **(gancho)** "Se fabrica en Japón" (planta de Okazaki) — [iProfesional](https://www.iprofesional.com/autos/418833-mitsubishi-lanza-nuevo-suv-7-plazas-argentina-cuanto-sale)
3. "Se lanzó a USD 61.000; hoy la marca la ofrece a USD 51.500 con bonificación" (*confirmar el día*) — [iProfesional, 12/2024](https://www.iprofesional.com/autos/418833-mitsubishi-lanza-nuevo-suv-7-plazas-argentina-cuanto-sale); [Mitsubishi, 26/11/2026](https://www.mitsubishi-motors.com.ar/vehicles/outlander)
4. "Tiene 6 modos de manejo, incluidos Barro y Nieve" — [Ficha oficial](https://www.mitsubishi-motors.com.ar/ft_outlander.pdf)
5. "Tiene 7 airbags, techo panorámico y butacas delanteras calefaccionadas" — [Ficha oficial](https://www.mitsubishi-motors.com.ar/ft_outlander.pdf)
6. "Tiene 21 centímetros de despeje" (210 mm) — [Ficha oficial](https://www.mitsubishi-motors.com.ar/ft_outlander.pdf)

### Inferences
- **Para no repetir el error de los avisos:** en los guiones del Eado no decir "215 cv" ni "cámara de retroceso". Decir "212 caballos eléctricos" y "cámara 360".
- Las frases con comparación propia ("más que muchas notebooks", "más de 13 veces") van rotuladas como "estimado" o "ejemplo", con la cuenta en la descripción (regla de la sección 4 del CLAUDE.md).

### Gaps
- **Datos sin respaldo argentino que no deben usarse hasta confirmarlos:**
  - Eado: 995 km totales, V2L, cargador incluido, tiempo de carga, despeje;
  - Deepal S05: baúl de 462 L, cámara de techo 4K en la unidad argentina, km de la garantía;
  - JMEV: potencia del wallbox;
  - L200: capacidad de remolque.
