# Software vertical (micro-SaaS) para pymes de Argentina y LatAm: oportunidades para un emprendedor solo con Claude Code

> Investigación hecha el 20/11/2026. Todo lo que no tiene fuente va a "Inferences" o a "Gaps". Los precios en ARS cambian rápido con la inflación: tomarlos como foto de 2026. **No encontré una fuente para el tipo de cambio de noviembre de 2026.** Cuando convierto a USD uso un supuesto de **≈ ARS 1.450 por USD**, marcado como supuesto y a verificar.

## 1. ¿Qué rubros de pymes ya pagan software, qué usan y cuánto cuesta?

### Takeaway
Hay pago demostrado y proveedores locales con precio publicado en cinco rubros: turnos y consultorios (AgendaPro), facturación para monotributistas (muchos jugadores), consorcios (cobro por unidad funcional), gimnasios y clubes (cobro de cuotas) y administración de alquileres (varios productos locales con ajustes IPC/ICL). En talleres mecánicos y veterinarias la evidencia de pago recurrente es floja: hay pocos precios publicados y se venden licencias o planillas de pago único.

### Cited Findings
**Turnos / consultorios / estética (AgendaPro es el líder regional)**
- AgendaPro Argentina (precios en ARS por mes con IVA incluido, solo para cuentas nuevas): **Individual $9.900** (los 3 primeros meses a $990), **Básico $19.900** (2 profesionales; +$5.000 del 3.º al 5.º profesional), **Premium $39.900** (suma historia clínica, consentimientos y telemedicina), **Pro IA $129.900** (hasta 5 profesionales, CRM, agentes de IA). Pago anual con 15 % de descuento. Los clientes actuales pueden pasarse a estos planes desde el 1/1/2027. — [AgendaPro AR planes](https://agendapro.com/ar/planes)
- Extras de AgendaPro AR: **recordatorios por WhatsApp desde $7.900/mes con 50 mensajes incluidos**; "Recepcionista IA" a +$30.000/mes en Individual o +$10.000 por profesional; **integraciones por API: US$200/mes**; **la integración con Mercado Pago está en todos los planes**; **la "Facturación electrónica" figura como "Próximamente"**. — [AgendaPro AR planes](https://agendapro.com/ar/planes)
- Una guía de Pabau (octubre de 2026, competidor, sin fuente oficial) da precios en USD de AgendaPro: de USD 9 (Individual) a USD 199 (Pro). Capterra y GetApp muestran "desde USD 19". Las fuentes no coinciden. — [Pabau](https://pabau.com/es/blog/agendapro-precios/); [Capterra ES](https://www.capterra.es/software/218709/agendapro)
- AgendaPro dice tener más de 135.000 profesionales usuarios y se presenta como "software líder en Argentina para psicólogos" (dato del propio proveedor). — [AgendaPro psicólogos](https://agendapro.com/ar/psicologos/software-para-psicologos)
- Otros productos para psicólogos: Psicobit (App Store AR, gratis, para iPad, sin precio de planes pagos encontrado); PsicoGest (España, desde 9,99 €/mes, recordatorios por WhatsApp; su facturación sigue la norma española VeriFactu, no sirve para ARCA). — [Psicobit](https://apps.apple.com/ar/app/psicobit-soft-para-psic%C3%B3logos/id6670581019); [PsicoGest Capterra](https://www.capterra.es/software/1087146/PsicoGest)
- Software para clínicas y consultorios en Argentina, rango por categoría según un blog de una agencia de desarrollo (marzo de 2026, sin nombrar productos): **SaaS de ARS 15.000 a 80.000 por mes**; instalado en el local, USD 5.000–30.000 de una vez; a medida, USD 15.000–80.000. — [Develop Argentina, clínicas 2026](https://developargentina.com/blog/software-clinicas-consultorios-argentina-2026)
- YoFacturo ofrece para clínicas y kinesiología agenda, historia clínica y **facturación a obras sociales** en una sola plataforma, con un mes de prueba sin tarjeta. — [YoFacturo clínicas](https://yo-facturo.com/clinicas/)

**Facturación electrónica para monotributistas (rubro muy poblado)**
- YoFacturo: **plan Emprendedor/Punto de Venta AR$ 20.000/mes**, Básico 50.000, Completo 75.000 ("Más popular"), Premium 150.000 (incluye API). Factura sola cada cobro o transferencia de Mercado Pago. Dice tener 200+ empresas clientes y 150.000+ facturas emitidas. — [YoFacturo gimnasios/precios](https://yo-facturo.com/gimnasios/); [YoFacturo MP](https://yo-facturo.com/facturar-transferencias-mercado-pago/)
- Tributo Simple: facturación gratis, más un plan pago "Asistente Contable"; factura sola cada cobro de Mercado Pago. — [Tributo Simple MP](https://tributosimple.com/automatiza-la-facturacion-de-mercado-pago-con-tributo-simple/)
- Tiendanube Facturador Cloud: conecta Mercado Pago y factura links de pago, QR y transferencias (las detecta cada 15 minutos). — [Tiendanube app store](https://www.tiendanube.com/tienda-aplicaciones-nube/facturador-cloud)
- Tramitito (lanzado en junio de 2026, factura por chat o WhatsApp con la API oficial): monotributo **$4.900 y $7.900/mes**; responsable inscripto $8.900 y $13.900; **contadores $12.900 (hasta 15 clientes) y $19.900 (clientes ilimitados)**; gratis hasta 5 facturas por mes. — [Infonegocios, 4/8/2026](https://infonegocios.info/plus/tramitito-la-app-argentina-que-factura-en-arca-con-un-mensaje-de-chat-en-10-segundos-y-avisa-antes-de-que-te-pases-de-categoria)
- Facturitas: bot de WhatsApp que factura a partir de texto, audio, foto o Excel; importa ventas de Mercado Pago y Tiendanube; no pide clave fiscal. **5.000 usuarios activos**, 226.272 facturas en un mes. — [iProUP, 22/7/2026](https://www.iproup.com/startups/69692-app-monotributistas-iaemitir-facturas-whatsapp-mercado-pago-tienda-nube-facturitas)
- El Facturador oficial de ARCA es gratis (también desde la app ARCA móvil), pero no factura solo los cobros de Mercado Pago. — [ARCA Facturador](https://www.arca.gob.ar/facturador/caracteristicas-y-funciones/que-es.asp)

**Contadores (estudios contables)**
- Herramientas para estudios: SOS Contador (panel de topes y recategorización de monotributistas, avisos de deuda), Aconpy (bots que bajan y clasifican comprobantes de ARCA con solo el CUIT), Plan In, Tributa Ya. Ninguno publica precio en los resultados. — [Ignacio Online, SOS Contador](https://www.ignacioonline.com.ar/monotributo-en-sos-contador-control-recategorizacion-y-alertas-todo-en-una-sola-plataforma/); [Contadores en Red, Aconpy](https://contadoresenred.com/el-futuro-llego-a-los-estudios-contables-conoce-todos-los-bots-inteligentes-que-hoy-automatizan-aconpy/?noamp=mobile)
- Lannis: USD 25/mes por contribuyente; el plan para contadores todavía no tenía precio (estaba en prueba). La atribución a esta nota de El Cronista sale del resultado de búsqueda: verificar. — [El Cronista](https://www.cronista.com/economia-politica/como-la-inteligencia-artificial-ya-simplifica-la-liquidacion-de-impuestos-y-agiliza-tiempos/)

**Consorcios / expensas (cobro por unidad funcional, UF)**
- CONSO: **$2.950 + IVA por unidad funcional por mes**, todo incluido, 30 días de prueba sin tarjeta (Capterra, sin fecha visible). — [Capterra CONSO](https://www.capterra.es/software/1111352/CONSO)
- Una startup argentina de expensas cobraba $1.200 por UF por mes, a cargo del consorcio (nota sin fecha; probablemente un precio viejo). — [El Cronista Apertura](https://www.cronista.com/apertura/emprendedoress/una-startup-argentina-puso-las-expensas-bajo-control-y-conquisto-a-manu-ginobili)
- Simple Solutions: abonos **desde $800 hasta $1.500 por usuario**, más de 320.000 UF gestionadas, 25 empleados, en 5 países; arrancó con ahorros propios y un premio de USD 80.000 (mayo de 2025). — [iProfesional](https://www.iprofesional.com/negocios/427891-como-funciona-la-app-que-permite-pagar-expensas-y-controlar-accesos-desde-el-celular)
- Otros jugadores: Octopus (suscripción más un fee por UF; nota de 2023), Unitify, Consorcio Abierto (app), HomeApp en Córdoba (15+ edificios y 2.500 usuarios, canon fijo por edificio). En Mercado Libre se venden también "software de administración de consorcios". — [iProfesional Octopus](https://www.iprofesional.com/tecnologia/372227-consorcios-octopus-proptech-apuesta-por-la-modernizacion); [Unitify](https://unitify.com/argentina); [Consorcio Abierto](https://apps.apple.com/ar/app/consorcioabierto/id1361121401); [Infonegocios HomeApp](https://infonegocios.info/nota-principal/una-proptech-cordobesa-quiere-ordenar-los-consorcios-desde-adentro-ya-gestiona-mas-de-15-edificios-y-2-500-usuarios-activos); [ML](https://www.mercadolibre.com.ar/shorts/clips/G1c4bb/software-administracion-consorcios-expensas-recibos-edificio)

**Administración de alquileres (inmobiliarias y administradores)**
- Productos locales con ajustes IPC/ICL y liquidación a propietarios: **Gestion Domus** (de 10 a varios cientos de contratos; ICL/IPC, mora, liquidaciones y ARCA), **Rents** (para dueños particulares; ajusta por ICL, IPC o UVA con datos del BCRA y el INDEC y factura en ARCA), **YoFacturo alquileres** (planes por cantidad de inmuebles), **Adminprop**, **Inmobilio**, **Forux**, **Llavik**. Ninguno muestra precio en los resultados. — [Gestion Domus](https://www.capterra.co.uk/software/1236945/Gestion-Domus); [Rents](https://www.capterra.co.uk/software/1110826/Rents); [YoFacturo alquileres](https://yo-facturo.com/alquileres/); [YoFacturo blog (Adminprop, Inmobilio)](https://yo-facturo.com/blog/sistema-gestion-inmobiliaria-alquileres/); [Forux](https://www.capterra.com/p/10047889/Forux/); [Llavik](https://www.comparasoftware.com/llavik)
- Rango por categoría para software inmobiliario SaaS en Argentina: **"desde $20.000 hasta $100.000 por mes"**; a medida, USD 10.000–50.000 (blog de una agencia, marzo de 2026, sin nombrar productos). — [Develop Argentina, inmobiliarias 2026](https://developargentina.com/blog/sistema-gestion-inmobiliaria-argentina-2026)

**Gimnasios, estudios y clubes**
- YoFacturo para gimnasios: cuotas con cobro recurrente por Mercado Pago, factura con CAE por cada cobro enviada por WhatsApp o email, recordatorios de cuotas vencidas (planes de AR$ 20.000 a 150.000). — [YoFacturo gimnasios](https://yo-facturo.com/gimnasios/)
- GymAr: software argentino, precios en pesos, "integración real con MercadoPago", sin comisión sobre los cobros (texto de marketing, sin precio). — [Comparasoftware GymAr](https://www.comparasoftware.com/gymar)

**Talleres mecánicos y veterinarias (evidencia floja)**
- Talleres: Appli-Car (SaaS para Chile, Colombia y Argentina, sin precio), OK CAR (MXN 699), AutoRepair Cloud (USD 59,99); en Mercado Libre se venden "programas" para taller y **una planilla Excel de taller a ARS 20.000 de pago único**. — [Comparasoftware Appli-Car](https://www.comparasoftware.com/appli-car); [Capterra OK CAR](https://www.capterra.es/software/1110636/OK-CAR); [Capterra AutoRepair Cloud](https://www.capterra.es/software/147213/autorepair-cloud); [Servidos.ar](https://servidos.ar/clasificados/planilla-excel-de-mantenimiento-preventivo-taller-en-orden-87eb9b); [ML](https://www.mercadolibre.com.ar/shorts/clips/c4TxBT/programa-software-taller-mecanico)
- Veterinarias: VetPaw (argentino, "precio de lanzamiento $30.000/mes", sin moneda clara), Volki (recordatorios clínicos por WhatsApp; licencia o SaaS), MyVete (Argentina, precio a consultar), AgendaPro. — [Comparasoftware VetPaw](https://www.comparasoftware.com/vetpaw); [Capterra Volki](https://www.capterra.com/p/240877/Volki/); [Capterra MyVete](https://www.capterra.es/software/216975/myvete)

### Inferences
- **Precio ancla del mercado:** el plan de 1 profesional de AgendaPro sale ARS 9.900 (≈ USD 7 con el supuesto de ARS 1.450). La facturación para monotributistas cuesta de ARS 4.900 (Tramitito) a 20.000 (YoFacturo). Un micro-SaaS para profesionales sueltos compite contra precios de USD 5–15 por mes. Por eso conviene apuntar a negocios con varios usuarios o cobrar por unidad: por UF en consorcios, por contrato en alquileres, por socio o como porcentaje de lo cobrado en clubes.
- **Rubros con mejor ticket y pago demostrado:** consorcios (cobro por UF) y administración de alquileres (ARS 20.000–100.000 por mes). Ahí el negocio cliente mueve plata de terceros, así que el software es "infraestructura" y cuesta cambiarlo.
- **Facturación por WhatsApp para monotributistas:** queda **descartada como producto principal**. Ya están Facturitas, Tramitito, YoFacturo, Tributo Simple, Facturador Cloud y el Facturador gratis de ARCA. Sí sirve como **módulo** dentro de un producto vertical.

### Gaps
- Precios publicados de Gestion Domus, Adminprop, Inmobilio, Octopus, Turnito, Appli-Car, MyVete, SOS Contador y Aconpy: no aparecen en las búsquedas. Hay que pedirlos o hacer "mystery shopping".
- Precio de AgendaPro AR anterior a 2026: no se pudo comparar cuánto subió.
- Uso real de Tango, Xubio, Colppy y Alegra en estos rubros: no se investigó por falta de tiempo. Son ERPs y contables generales, no verticales.

## 2. Quejas de usuarios y huecos concretos (WhatsApp, ARCA, Mercado Pago, seña, expensas)

### Takeaway
Las quejas públicas en reseñas son pocas y moderadas: AgendaPro tiene 4,8/5. Los huecos concretos que se pueden documentar son tres. (a) **AgendaPro AR todavía no factura en ARCA** ("Próximamente") y una psicóloga se queja de tener que cobrar por fuera del sistema. (b) **WhatsApp se cobra caro como extra**: ARS 7.900 por 50 mensajes, unas 3–5 veces el costo de Meta. (c) En consorcios, alquileres y clubes se sigue trabajando con **Excel, mails, efectivo y transferencias manuales**.

### Cited Findings
- AgendaPro en Capterra España: **4,8/5 con 158 reseñas**. Una psicóloga dice que el cobro le resulta ineficaz porque **"tiene que hacerlo siempre por fuera del sistema"**. Según Secret, a los usuarios les cuesta el sistema de membresías y suscripciones y piden mejoras en pagos. — [Capterra ES](https://www.capterra.es/software/218709/agendapro); [Secret](https://www.joinsecret.com/es/agendapro/reviews)
- AgendaPro AR: "Facturación electrónica — **Próximamente**"; recordatorios de WhatsApp **desde $7.900/mes con 50 mensajes** (con un número propio son ilimitados en algunos planes). — [AgendaPro AR planes](https://agendapro.com/ar/planes)
- Clínicas: una guía de 2026 advierte que **los nomencladores desactualizados de las obras sociales generan rechazos de facturación**, y pide integración nativa con la API de WhatsApp Business "con automatización real, no solo envío manual". Sus estadísticas (de 15 a 25 % de ausentismo sin sistema, de 30 a 40 % menos con recordatorio) **no tienen fuente**. — [Develop Argentina, clínicas](https://developargentina.com/blog/software-clinicas-consultorios-argentina-2026)
- Consorcios: los administradores tradicionales trabajan con **planillas de Excel y cadenas de mails** (barrios con 600 lotes "todo lo hacían a mano") y desconfían de las herramientas nuevas. — [iProfesional, Simple Solutions](https://www.iprofesional.com/negocios/427891-como-funciona-la-app-que-permite-pagar-expensas-y-controlar-accesos-desde-el-celular)
- Consorcios en CABA, presión regulatoria nueva: **examen de idoneidad presencial obligatorio** para la matrícula del RPA (Disp. 358/2025); **declaración jurada anual** y actualización de matrícula (Disp. 882/2025); **muchas bajas de administradores** (Disp. 4550/2025); **canal para denunciar a administradores que no dieron de alta un consorcio** (Disp. 1129/2026). — [Liga del Consorcista 358/2025](https://ligadelconsorcista.org/caba-disposicion-358-2025-examenes-para-aspirantes-a-inscribirse-en-el-rpa-para-administrar-consorcios-); [Liga del Consorcista 882/2025](https://ligadelconsorcista.org/caba-disposicion-882-2025-administradores-instructivos-declaraciones-juradas-certificados-); [Liga del Consorcista, bajas](https://ligadelconsorcista.org/administradores-dados-de-baja-rpa); [Boletín Oficial CABA 1129/2026](https://boletinoficial.buenosaires.gob.ar/normativaba/norma/838956); [BAE Negocios](https://www.baenegocios.com/sociedad/Los-administradores-de-consorcios-deberan-pasar-un-examen-de-idoneidad-20250423-0044.html)
- Alquileres: el trabajo mensual pesado es **recalcular el alquiler por ICL o Casa Propia, avisar al inquilino, actualizar la facturación y liquidar al propietario** (alquiler cobrado menos comisión, expensas y arreglos). Algunas inmobiliarias usan un SaaS para CRM y publicación y **se hacen a medida el módulo de liquidación**. — [Develop Argentina, inmobiliarias](https://developargentina.com/blog/sistema-gestion-inmobiliaria-argentina-2026); [YoFacturo blog alquileres](https://yo-facturo.com/blog/sistema-gestion-inmobiliaria-alquileres/)
- Hay demanda masiva del cálculo de ajuste de alquileres: Mercado Libre tiene una página "calculadora de alquiler IPC/ICL" en su blog inmobiliario. — [ML blog](https://www.mercadolibre.com.ar/blog/re-calculadora-alquiler-ipc-icl)
- Clubes de barrio: la cuota social promedia unos **$23.000**, la morosidad crece y, según el sector, un club que solo acepta efectivo o transferencias manuales puede perder **del 30 al 50 % de los cobros** (estimación de un actor interesado, CuotaQ). Alrededor del 90 % de las organizaciones sin fines de lucro no tiene procesos digitalizados (estimación del sector). — [Mercado](https://mercado.com.ar/noticias/clubes-de-barrio-la-cuota-promedia-23-000-y-la-morosidad-crece-sin-cobros-digitales)
- **El 68,2 % de los clubes de barrio del AMBA opera fuera de las federaciones** y enfrenta morosidad. — [Mercado](https://mercado.com.ar/vida-y-estilo/clubes-de-barrio-del-amba-682-opera-fuera-de-federaciones-y-enfrenta-morosidad)
- Gimnasios: una guía argentina de 2025 marca como integraciones prioritarias **AFIP/ARCA para facturar solo y Mercado Pago para cobros recurrentes** (además de débito en cuenta, Modo y Ualá Bis). — [Develop Argentina, gimnasios](https://developargentina.com/blog/sistema-gestion-gimnasios-argentinos-2025)

### Inferences
- **Hueco más claro y verificable:** "cobro + factura ARCA automática + aviso por WhatsApp" dentro del flujo de trabajo de un rubro. Los generalistas (AgendaPro) todavía no facturan en Argentina, y los facturadores (Facturitas, Tramitito) no conocen el flujo del rubro (turnos, contratos, expensas, cuotas de socios).
- **Margen en WhatsApp:** 50 mensajes a ARS 7.900 son ≈ ARS 158 por mensaje (≈ USD 0,11 con el supuesto de cambio), contra ≈ USD 0,03 de Meta por mensaje de utilidad en Argentina (ver pregunta 3). Un producto que use la API directo puede incluir los recordatorios en el precio y competir por ahí.
- **Regulación como motor de compra:** el RPA de CABA exige DDJJ, examen y alta de cada consorcio. Un producto que deje el administrador "listo para la DDJJ y las auditorías" tiene un argumento de venta que no depende de la moda.

### Gaps
- No pude leer reseñas de Google Play ni de App Store (cantidad y texto) de AgendaPro, Turnito, Consorcio Abierto u Octopus. Las búsquedas no las devolvieron y Capterra bloqueó la descarga (403).
- No encontré hilos de Reddit (r/argentina, r/devsarg) ni de grupos de Facebook con quejas específicas por rubro.
- Turnos con seña o depósito: AgendaPro integra Mercado Pago, pero no confirmé si cobra señas obligatorias ni cómo maneja las devoluciones.

## 3. Costos y barreras de las integraciones clave en 2026 (WhatsApp, ARCA, Mercado Pago)

### Takeaway
**WhatsApp:** desde julio de 2025 se cobra por mensaje entregado, y **desde el 1/10/2026 Meta volvió a cobrar los mensajes de servicio y de utilidad dentro de la ventana de 24 h**, con 1.000 mensajes de servicio gratis por número y por mes. En Argentina, un recordatorio de utilidad cuesta ≈ USD 0,03 y uno de marketing ≈ USD 0,07. **ARCA:** los web services de factura electrónica son gratis, pero piden certificado digital y homologación; hay intermediarios pagos (Afip SDK, TusFacturas). **Mercado Pago:** cobra comisión por venta, sin abono.

### Cited Findings
**WhatsApp Business Platform**
- Desde el 1/7/2025 se cobra **por mensaje entregado**, según la categoría (marketing, utilidad, autenticación, servicio) y el país del destinatario. Los mensajes que manda el usuario no se cobran. — [Meta, Pricing](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing)
- Las plantillas de utilidad enviadas dentro de la ventana de atención fueron **gratis del 1/7/2025 al 30/9/2026**. **Desde el 1/10/2026 Meta volvió a cobrar los mensajes de servicio** (gratis desde noviembre de 2024) **y los de utilidad dentro de la ventana**; cada número tiene **1.000 mensajes de servicio gratis por mes** (no se acumulan). — [Meta, Pricing](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing)
- Las respuestas a un usuario que llegó desde un anuncio "Click to WhatsApp" son **gratis durante la "free entry point window"** (marketing, utilidad, autenticación y servicio). — [Meta, Pricing](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing)
- Desde el 1/7/2026 hay una quinta categoría, "Meta Business Agent", a USD 2 por millón de tokens (≈ 4–5 centavos por mensaje según Meta). — [Meta, Pricing](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing)
- Argentina es un mercado con tarifa propia; las tarifas de utilidad y autenticación **bajaron el 1/10/2025**. Los descuentos por volumen se aplican solo a utilidad y autenticación. — [Meta, Pricing](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing); [Kommo](https://www.kommo.com/support/messenger-apps/whatsapp-pricing)
- Tabla de SleekFlow para Argentina (vigente desde el 1/10/2026; no aclara si incluye margen): **marketing USD 0,07107; utilidad USD 0,02990; autenticación USD 0,02990; servicio USD 0,0260**. — [SleekFlow](https://help.sleekflow.io/en_US/pricing)
- Go4whatsup publica utilidad a USD 0,011 y marketing a USD 0,025 "para Argentina", pero la misma página dice que son **las tarifas de India**: no es confiable. La tarjeta de tarifas de Salesforce (mayo de 2026) muestra para Argentina 76,3 y 32,10, en una unidad que no aclara. — [Go4whatsup](https://www.go4whatsup.com/argentina/whatsapp-business-api-pricing/); [Salesforce rate card](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/WhatsApp-Business-Messaging-Rate-Card-MM-Lite-May-1-2026.pdf)

**ARCA (ex AFIP), factura electrónica**
- Los web services de ARCA usan **WSAA** (autenticación) y piden un **certificado digital** que se gestiona con clave fiscal. Para pruebas hay un entorno de **homologación** y la app WSASS para certificados de prueba. Algunos servicios necesitan autorizaciones o convenios especiales. — [ARCA certificados](https://www.afip.gob.ar/ws/programadores/certificados-digitales.asp); [ARCA WSAA](https://www.afip.gob.ar/ws/documentacion/wsaa.asp); [ARCA WSASS](https://arca.gob.ar/ws/WSASS/html/conceptos.html); [ARCA catálogo](https://www.afip.gob.ar/ws/documentacion/catalogo.asp)
- Afip SDK (intermediario) permite arrancar en modo desarrollo con un CUIT de prueba (20-40937847-2) sin certificado; en producción se agrega el certificado propio. Tiene guías para Python, Go, Ruby y n8n. **No encontré su precio.** — [Afip SDK docs](https://docs.afipsdk.com/integracion/python)
- TusFacturas ofrece una API de factura electrónica ARCA para integrar en sistemas propios (precio no encontrado). — [TusFacturas API](https://developers.tusfacturas.app/api-factura-electronica-afip-facturacion-ventas/referencia-api-afip-arca)
- Facturitas factura **sin pedir clave fiscal** ("no accede a las cuentas de ARCA"), y Tramitito "no guarda la clave fiscal". Tramitito también guarda la factura si ARCA está caído y la emite cuando vuelve. — [iProUP](https://www.iproup.com/startups/69692-app-monotributistas-iaemitir-facturas-whatsapp-mercado-pago-tienda-nube-facturitas); [Infonegocios](https://infonegocios.info/plus/tramitito-la-app-argentina-que-factura-en-arca-con-un-mensaje-de-chat-en-10-segundos-y-avisa-antes-de-que-te-pases-de-categoria)

**Mercado Pago**
- Comisiones en Argentina (iProfesional, julio de 2026): **dinero en cuenta y otras billeteras o bancos 0,8 % + IVA, al instante; tarjeta de crédito 1,79 % + IVA, a 35 días**. No dice a qué producto aplica (QR, link, Point). — [iProfesional](https://www.iprofesional.com/tecnologia/386153-mercado-pago-que-debes-saber-sobre-comisiones-plazos-y-montos)
- Mercado Pago tiene un producto de **Suscripciones** (cobros recurrentes por API) documentado para desarrolladores; no encontré su comisión. — [MP Developers, suscripciones](https://www.mercadopago.com.ar/developers/es/docs/subscriptions/resources/tutorial-videos)
- El link de pago no tiene costo mensual: se paga solo cuando hay venta. Las tasas de referencia publicadas son de México, no de Argentina. — [MP México link de pago](https://www.mercadopago.com.mx/herramientas-para-vender/link-de-pago)

### Inferences
- **Costo de WhatsApp por cliente:** un consultorio con 120 turnos por mes y un recordatorio de utilidad por turno gasta ≈ 120 × 0,03 = **USD 3,6 por mes**. Una administración con 300 UF y 2 avisos de expensas por mes, ≈ USD 18 por mes. Se puede incluir en el precio, pero ya no es "gratis": desde octubre de 2026 también se pagan las respuestas dentro de la ventana, salvo los primeros 1.000 mensajes de servicio.
- **Barrera de ARCA:** es de onboarding, no de costo. Cada cliente tiene que delegar el web service o subir un certificado, y eso hace perder gente. Los competidores la bajan con modelos que no piden clave fiscal. Copiar ese patrón (delegar el servicio a un representante) es clave. Es un supuesto técnico a verificar con la documentación de ARCA.
- **Anuncios Click to WhatsApp:** la conversación gratis con quien entra desde el anuncio se lleva bien con Higgsfield, que puede manejar Meta Ads. Es un canal de adquisición pago, no viral.

### Gaps
- No pude bajar la planilla oficial de tarifas de Meta (CSV o PDF) para confirmar las de Argentina. Las de SleekFlow (0,0299 utilidad / 0,0711 marketing) son de un tercero.
- Política de Meta sobre chatbots de IA "de propósito general" en la API de WhatsApp (cambios anunciados para 2026): no la verifiqué. Antes de construir un asistente con IA por WhatsApp hay que confirmar que un bot propio del negocio está permitido.
- Comisión de Mercado Pago Suscripciones y del "marketplace fee" (cobrar una comisión sobre los cobros de los clientes): no la encontré.
- Precio de Afip SDK y de TusFacturas API.

## 4. Cómo descubren y compran software estos negocios (canales) y datos de CAC y churn

### Takeaway
Los canales con evidencia son **las asociaciones y consejos profesionales** (el CPCE de CABA ofrece un beneficio de Aconpy a sus matriculados), **los marketplaces y app stores** (Tiendanube, el marketplace y el botón "Reservar con Google" de AgendaPro, y ventas de software en Mercado Libre), **la búsqueda en Google de herramientas como calculadoras** y **la prueba gratis sin tarjeta** (CONSO 30 días, YoFacturo 1 mes, Tramitito 14 días). El dato de churn para SaaS de LatAm es alto: **8,2 % mensual** (informe de 2023 citado por un tercero).

### Cited Findings
- El Consejo Profesional de Ciencias Económicas de CABA publica un **"Beneficio Aconpy"** para sus matriculados: las asociaciones profesionales funcionan como canal de distribución de herramientas para contadores. — [CPCE CABA, PDF](https://consejo.org.ar/storage/attachments/Beneficio%20Aconpy.pdf-JSui1ZaT6w.pdf)
- El CPCE también capacita en administración de consorcios (otro punto de contacto con administradores). — [CPCE](https://www.consejo.org.ar/noticias/2025/capacitate-en-administracion-de-consorcios-de-propiedad)
- AgendaPro incluye en todos los planes "nuevos clientes desde el Marketplace" y el botón "Reservar" en Google: el canal de adquisición está dentro del producto. — [AgendaPro AR planes](https://agendapro.com/ar/planes)
- La app store de Tiendanube distribuye facturadores (Facturador Cloud). — [Tiendanube](https://www.tiendanube.com/tienda-aplicaciones-nube/facturador-cloud)
- En Mercado Libre Argentina se publica software vertical (consorcios, talleres, gimnasios) como producto. — [ML consorcios](https://www.mercadolibre.com.ar/shorts/clips/G1c4bb/software-administracion-consorcios-expensas-recibos-edificio); [ML gimnasios](https://www.mercadolibre.com.ar/shorts/clips/CxpmxA/software-gestion-gimnasios-panel-web-app)
- Pruebas gratis comunes: CONSO 30 días sin tarjeta; YoFacturo 1 mes sin tarjeta; Tramitito 14 días sin permanencia, más un plan gratis de 5 facturas; AgendaPro con 3 meses a ARS 990. — [Capterra CONSO](https://www.capterra.es/software/1111352/CONSO); [YoFacturo](https://yo-facturo.com/gimnasios/); [Infonegocios Tramitito](https://infonegocios.info/plus/tramitito-la-app-argentina-que-factura-en-arca-con-un-mensaje-de-chat-en-10-segundos-y-avisa-antes-de-que-te-pases-de-categoria); [AgendaPro](https://agendapro.com/ar/planes)
- Facturitas vende con la "fricción cero" de WhatsApp (sin app y sin clave fiscal) y crece **sin inversión externa, reinvirtiendo lo que factura**. — [iProUP](https://www.iproup.com/startups/69692-app-monotributistas-iaemitir-facturas-whatsapp-mercado-pago-tienda-nube-facturitas)
- **Churn:** un artículo cita el State of SaaS LATAM Report 2023, con un **churn promedio de 8,2 % mensual** en SaaS de la región, contra 4,5 % en Estados Unidos. Un análisis de pymes argentinas cuenta que un SaaS de inventario pasó de 4 % a 9 % mensual en la crisis de 2020–2021. — [Ecosistema Startup](https://ecosistemastartup.com/?p=59797)
- **CAC y repago:** según Benchmarkit 2025 (citado por un blog), el repago promedio del CAC fue de 18 meses en 2024; para SaaS de pymes, de 8 a 12 meses se considera bueno. Otro blog da un CAC promedio de USD 1.200 en SaaS B2B (no es de LatAm ni de micro-pymes). — [Beancount blog 2026](https://beancount.io/es/blog/2026/05/10/saas-metrics-founders-must-track-2026-ltv-cac-nrr-churn-cac-payback-benchmarks-guide); [We Are Founders](https://www.wearefounders.uk/saas-churn-rates-and-customer-acquisition-costs-by-industry-2025-data/)
- Los administradores tradicionales de consorcios desconfían de las herramientas nuevas: venderles es lento. — [iProfesional](https://www.iprofesional.com/negocios/427891-como-funciona-la-app-que-permite-pagar-expensas-y-controlar-accesos-desde-el-celular)

### Inferences
- **Canal recomendado para alguien solo (sin depender de Instagram):**
  1. Venta directa a listas públicas: inmobiliarias publicadas en Zonaprop, Argenprop o ML Inmuebles; administradores del RPA y de los colegios provinciales; clubes del registro RENACED o del registro de clubes de barrio. Se arma con scraping y mensajes personalizados escritos con Claude.
  2. **SEO con una herramienta gratis** (calculadora de aumento de alquiler IPC/ICL, simulador de expensas, calculadora de recategorización) que lleve a la prueba del producto.
  3. Convenios con colegios y consejos (corredores inmobiliarios, administradores, contadores), como Aconpy con el CPCE.
  4. Anuncios Click to WhatsApp en la zona, con la conversación gratis y Higgsfield para hacer las piezas.
- **Efecto del churn de 8 % mensual:** para sostener 50 clientes hay que sumar unos 4 por mes solo para no caer. Rubros con "dinero de terceros" (expensas, alquileres, cuotas de socios) deberían tener menos churn que los profesionales sueltos, porque cambiar de sistema significa migrar cuentas corrientes. Es una inferencia sin dato que la respalde.

### Gaps
- No encontré datos propios de CAC, conversión de prueba a pago ni churn de SaaS argentinos verticales (AgendaPro, Octopus, etc.).
- No encontré datos de cuánto se busca en Google cada término ("software consorcios", "calcular aumento alquiler") en Argentina. Se podrían ver con Google Keyword Planner.

## 5. Evaluación de cada nicho candidato (cantidad de negocios, precio, suscriptores para USD 1.000 netos, tiempo, defensa y riesgos)

### Takeaway
Con la evidencia reunida, el orden recomendado es: **(1) administración de alquileres para inmobiliarias chicas y administradores**, **(2) consorcios para administradores chicos del interior (Córdoba)** y **(3) cobro de cuotas para clubes, academias y escuelas deportivas**. Quedan como opciones más débiles **(4) cobro + factura + recordatorio para consultorios independientes** y **(5) panel de monotributistas para contadores**. Se descartan talleres (pago recurrente dudoso, tamaño de mercado sin dato) y la facturación por WhatsApp suelta (saturada).

### Cited Findings
**Datos para estimar el tamaño de cada mercado**
- Psicólogos: según la OCDE (Panorama de la Salud LAC 2023), Argentina tiene **más de 286 psicólogos cada 100.000 habitantes**, la tasa más alta de la región (el promedio de la OCDE es ≈ 40). El relevamiento de Alonso (UBA) contó **98.311 psicólogos activos en 2015**. — [OCDE 2023](https://www.oecd.org/pt/publications/panorama-da-saude-america-latina-e-caribe-2023_047f9a8a-pt/full-report/component-52.html); [Alonso/Klinar 2015](https://bvs-psi.mdp.edu.ar/wp-content/uploads/2024/11/2015_PSI_ARG_PDF.pdf)
- Monotributistas: los medios hablan de "unos dos millones", pero hay cifras que no coinciden (otra nota dice más de 5 millones). — [El Cronista](https://www.cronista.com/informacion-gral/confirmado-arca-cambia-las-cuotas-del-monotributo-y-millones-ya-calculan-cuanto-tendran-que-pagar-con-el-aumento/)
- Clubes: **más de 3.100 clubes en el AMBA** (Observatorio del Deporte Metropolitano, UMET); el registro nacional pide un mínimo de 50 asociados y 3 años de antigüedad. — [Cadena 3, abril de 2026](https://www.cadena3.com/noticia/sociedad/mas-de-3000-clubes-de-barrio-en-caba-sobreviven-con-cuotas-y-sin-apoyo-oficial_546031); [Guía RNCBYP](https://argentina.gob.ar/sites/default/files/2024/08/guia_de_tramite_-_rncbyp.pdf)
- Talleres: las cifras no coinciden. FAATRA habla de **45.000 talleres independientes** (dicho por la federación, sin censo) y una nota de divulgación, de **3.300** "registrados" en 2024. — [Conclusión (FAATRA)](https://www.conclusion.com.ar/?p=1321169); [Comparaencasa](https://www.comparaencasa.com/17-datos-sobre-las-reparaciones-de-autos-mas-comunes-en-argentina/)
- El "GPS de Empresas" del Ministerio de Producción está **discontinuado** y solo cuenta empleadores registrados (deja afuera a los unipersonales): no sirve para contar talleres ni veterinarias. — [datos.gob.ar](https://www.datos.gob.ar/dataset?tags=Empresas)
- Consorcios: Simple Solutions sola gestiona **más de 320.000 UF**, lo que muestra la escala del mercado de UF. No encontré cuántos consorcios ni administradores hay en CABA o en Córdoba. — [iProfesional](https://www.iprofesional.com/negocios/427891-como-funciona-la-app-que-permite-pagar-expensas-y-controlar-accesos-desde-el-celular)

**Precios de referencia por nicho (los de arriba, resumidos)**
- Consorcios: ARS 2.950 + IVA por UF (CONSO); ARS 800–1.500 por usuario (Simple Solutions). — [Capterra CONSO](https://www.capterra.es/software/1111352/CONSO); [iProfesional](https://www.iprofesional.com/negocios/427891-como-funciona-la-app-que-permite-pagar-expensas-y-controlar-accesos-desde-el-celular)
- Inmobiliario o alquileres: ARS 20.000–100.000 por mes según la categoría. — [Develop Argentina](https://developargentina.com/blog/sistema-gestion-inmobiliaria-argentina-2026)
- Consultorios: ARS 9.900 (AgendaPro Individual) a 39.900 (Premium); categoría ARS 15.000–80.000. — [AgendaPro](https://agendapro.com/ar/planes); [Develop Argentina](https://developargentina.com/blog/software-clinicas-consultorios-argentina-2026)
- Contadores: Tramitito ARS 12.900–19.900 por estudio; Lannis USD 25 por contribuyente. — [Infonegocios](https://infonegocios.info/plus/tramitito-la-app-argentina-que-factura-en-arca-con-un-mensaje-de-chat-en-10-segundos-y-avisa-antes-de-que-te-pases-de-categoria); [El Cronista](https://www.cronista.com/economia-politica/como-la-inteligencia-artificial-ya-simplifica-la-liquidacion-de-impuestos-y-agiliza-tiempos/)
- Clubes: cuota social promedio ≈ ARS 23.000 por socio (sirve para calcular un modelo de porcentaje sobre lo cobrado). — [Mercado](https://mercado.com.ar/noticias/clubes-de-barrio-la-cuota-promedia-23-000-y-la-morosidad-crece-sin-cobros-digitales)

### Inferences
**Supuestos de costos para llegar a USD 1.000 netos por mes** (estimaciones propias, no datos):
- Infraestructura (hosting, base de datos, API de Claude para leer documentos): USD 50–150 por mes.
- WhatsApp: ≈ USD 0,03 por recordatorio de utilidad.
- Comisión de Mercado Pago sobre la suscripción: ≈ 1–2,5 % con IVA.
- Pauta paga: USD 100–300 por mes.
- Impuestos propios (monotributo o RI, ingresos brutos): sin calcular.
- **Total: hace falta facturar unos USD 1.400–1.700 por mes** para quedarse con USD 1.000 netos.

| Nicho | Precio propuesto (supuesto de cambio ARS 1.450/USD) | Clientes para ~USD 1.500 brutos | Tiempo estimado* | Defensa (moat) | Riesgos principales |
|---|---|---|---|---|---|
| **1. Alquileres** (inmobiliarias chicas con 30–300 contratos y administradores de alquileres) | ARS 1.000–1.500 por contrato por mes, con un mínimo de ARS 30.000. Una cartera de 60 contratos paga ≈ ARS 72.000 (≈ USD 50) | **≈ 30 inmobiliarias** | 9–15 meses | Contratos e historial de índices cargados; liquidaciones mensuales; cuentas corrientes de inquilinos y propietarios (difíciles de migrar). **Ventaja con IA:** Claude lee el PDF del contrato y carga solo índice, periodicidad y fechas, así la migración tarda minutos. | Muchos competidores locales (Gestion Domus, YoFacturo, Adminprop, Inmobilio, Rents); cambios de la ley de alquileres; inmobiliarias muy chicas que siguen con Excel |
| **2. Consorcios** (administradores chicos y medianos del interior, empezando por Córdoba) | ARS 1.000–2.000 por UF por mes (debajo de CONSO). Un administrador con 200 UF paga ≈ ARS 200.000–400.000 | **≈ 6–10 administradores** | 9–18 meses (venta lenta, desconfianza) | Cuentas corrientes de cada UF, historial de liquidaciones, relación con los vecinos (cambiar de sistema es muy caro). **Ventaja con IA:** leer facturas de proveedores y armar el borrador de la liquidación; bot de WhatsApp para vecinos ("¿cuánto debo?", "mandame el cupón"); papeles listos para la DDJJ del RPA | Mercado con muchos jugadores (Octopus, Simple Solutions con 25 empleados, CONSO, Unitify, Consorcio Abierto, HomeApp en Córdoba); dominio complejo (sueldos de encargados, fondos de reserva); errores de cálculo con dinero de terceros = riesgo legal y de reputación |
| **3. Clubes, academias y escuelas deportivas** (cobro de cuotas con débito automático y morosidad por WhatsApp) | 1–1,5 % de lo cobrado o ARS 200–400 por socio por mes. Un club de 300 socios × ARS 23.000 = ARS 6,9 M por mes cobrados; 1 % ≈ ARS 69.000 (≈ USD 48) | **≈ 30 clubes** | 6–12 meses | Datos de socios, carnet digital, historial de pagos; el cobro digital baja la morosidad (beneficio que se puede medir) | Poca disposición a pagar (asociaciones civiles con comisiones directivas que rotan); CuotaQ y otros competidores; dependencia de las comisiones y reglas de Mercado Pago |
| **4. Consultorios sueltos** (psicólogos, nutricionistas, kinesiólogos particulares): turno + seña + factura C automática + recordatorio | ARS 12.000–20.000 por mes (≈ USD 8–14) | **≈ 110–190 profesionales** | 12–24 meses | Baja: AgendaPro anunció la facturación ("Próximamente") y YoFacturo ya la tiene para clínicas | Ticket bajo; churn alto de los profesionales sueltos; AgendaPro saca la facturación y cierra el hueco |
| **5. Contadores** (panel de monotributistas: topes, recategorización, VEP y reportes por WhatsApp a cada cliente) | ARS 25.000–60.000 por estudio, o ARS 1.000 por cliente | **≈ 40–60 estudios** | 9–15 meses | Integración con ARCA y datos históricos de cada cliente | Competencia con anclas de precio bajas (Tramitito ARS 19.900 con clientes ilimitados) y con beneficios ya armados con los consejos profesionales (Aconpy) |
| Descartados | Talleres (pago recurrente dudoso: se venden planillas a ARS 20.000 de una vez; el tamaño del mercado va de 3.300 a 45.000), facturación suelta por WhatsApp (saturada), veterinarias (poca evidencia de precio) | — | — | — | — |

\* Los tiempos son estimaciones propias sin fuente, pensadas para una persona sola con venta directa y algo de pauta. Con churn de 8 % mensual, el número de clientes a sostener sube.

**Por qué el n.º 1 va primero**
- El ticket es medio y se cobra por contrato.
- Los datos (contratos, índices, cuentas corrientes) atan al cliente.
- Hay una tarea mensual que se repite sí o sí (el ajuste y la liquidación).
- Hay un imán de SEO natural: la calculadora de aumento de alquiler.
- La IA da una ventaja concreta en la migración y en los avisos.
- No necesita convencer a un consorcio entero ni a una comisión directiva.

**Cómo encaja con LatAm:** los alquileres y los consorcios dependen mucho de las reglas de cada país, así que conviene quedarse en Argentina al principio. Los clubes y las academias son más fáciles de llevar a Uruguay, Chile o México cambiando la pasarela de pago.

### Gaps
- No encontré cuántas inmobiliarias hay en Córdoba o en Argentina (colegios de corredores), ni cuántos consorcios y administradores hay en CABA o Córdoba. Hay que pedirlo a los colegios o hacer un pedido de acceso a la información al RPA.
- No encontré el total de kinesiólogos, nutricionistas ni veterinarias.
- No hay precios publicados de los competidores directos en alquileres (Gestion Domus, Adminprop): sin ellos, el precio propuesto es una hipótesis.
- Tipo de cambio de noviembre de 2026: no lo verifiqué.

## 6. Evidencia de fundadores solos o equipos chicos en LatAm con USD 1.000–10.000 MRR en software vertical (2024–2026)

### Takeaway
**No encontré ningún caso verificado de un fundador solo en LatAm con USD 1.000–10.000 de MRR en SaaS vertical** con números públicos. Sí hay casos argentinos de 2025–2026 con tracción documentada que validan el modelo. **Facturitas** es bootstrapped, tiene 5.000 usuarios activos y apunta a USD 500.000 de ARR para fines de 2026. **Tramitito** se lanzó en junio de 2026 y tiene 2.126 usuarios registrados. **HomeApp** (Córdoba) tiene más de 15 edificios y 2.500 usuarios. **Simple Solutions** arrancó con ahorros propios y un premio, y hoy tiene 25 empleados y 320.000 UF.

### Cited Findings
- Facturitas (CEO: Agustín Zeppa): **5.000 usuarios activos** (últimos 3 meses), 226.272 facturas por más de $14.166 millones en un mes. El monto facturado se duplicó desde enero. Crece **bootstrapped, reinvirtiendo ingresos**, con la meta de **USD 500.000 de ARR a fines de 2026**. — [iProUP, 22/7/2026](https://www.iproup.com/startups/69692-app-monotributistas-iaemitir-facturas-whatsapp-mercado-pago-tienda-nube-facturitas)
- Tramitito (fundador: Nicolás Cabanillas): lanzado en junio de 2026; **2.126 usuarios registrados y 12.960 facturas** a agosto de 2026; planes de ARS 4.900 a 19.900. No publica MRR. — [Infonegocios, 4/8/2026](https://infonegocios.info/plus/tramitito-la-app-argentina-que-factura-en-arca-con-un-mensaje-de-chat-en-10-segundos-y-avisa-antes-de-que-te-pases-de-categoria)
- HomeApp (proptech de Córdoba para consorcios): **más de 15 edificios y 2.500 usuarios activos**, canon fijo por edificio. — [Infonegocios](https://infonegocios.info/nota-principal/una-proptech-cordobesa-quiere-ordenar-los-consorcios-desde-adentro-ya-gestiona-mas-de-15-edificios-y-2-500-usuarios-activos)
- Simple Solutions: se financió con ahorros personales y un premio de USD 80.000 (Buenos Aires Emprende); hoy tiene 25 empleados, 320.000 UF y un cuarto de su facturación viene del exterior. — [iProfesional, 17/5/2025](https://www.iprofesional.com/negocios/427891-como-funciona-la-app-que-permite-pagar-expensas-y-controlar-accesos-desde-el-celular)
- Una guía de "indie hackers" en España, México y Argentina (2026) plantea USD 5.000 de MRR como meta que "cambia la vida" y señala que **cobrar a clientes del exterior desde Argentina trae complicaciones de impuestos y medios de pago**. Es opinión, no un dato. — [Pasquale Pillitteri](https://pasqualepillitteri.it/es/news/3087/stack-indie-hacker-espana-mexico-argentina-2026)
- En Indie Hackers aparecen perfiles de fundadores de Mendoza y Buenos Aires (por ejemplo EzWrite y Droon), sin datos de ingresos en lo que encontré. — [Indie Hackers, AlejandroEzWrite](https://www.indiehackers.com/AlejandroEzWrite); [Indie Hackers, franp](https://www.indiehackers.com/franp)

### Inferences
- **El patrón que funciona en Argentina en 2026:** WhatsApp como interfaz, Mercado Pago y ARCA integrados de fábrica, y un plan gratis o barato para entrar. Facturitas y Tramitito lo muestran en facturación. Pasar ese mismo patrón a un rubro con ticket más alto (alquileres, consorcios, clubes) es la tesis más defendible para una persona sola.
- **Vara de comparación:** que Tramitito llegue a 2.126 registrados en dos meses no dice cuántos pagan. Con conversiones típicas de freemium de un dígito (supuesto, sin fuente), serían menos de 200 pagos a ARS 4.900–7.900, es decir **menos de USD 1.000 de MRR**. Esto refuerza que, a ticket bajo, hace falta mucho volumen.

### Gaps
- No encontré entrevistas ni publicaciones (en X/Twitter o Indie Hackers) con MRR verificado de fundadores solos de LatAm en software vertical durante 2024–2026. Las búsquedas en X no están disponibles con estas herramientas.
- No hay MRR ni cantidad de clientes pagos de Tramitito, HomeApp ni CONSO.
