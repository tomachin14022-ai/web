# Diagnosticar el swing con cuadro, número y margen

Un análisis de swing hecho con dos videos de celular, uno desde atrás (down the line, DTL) y otro de frente (face-on), puede ser más preciso y más defendible que la mirada de un instructor experto. Para eso tiene que medir solo lo que el video 2D permite medir y declarar cuánto se puede equivocar. Lo medible son las posiciones dentro del plano de la imagen comparadas con el address del propio golfista, los ángulos de la varilla, los desplazamientos en centímetros con una escala ubicada en el plano del cuerpo y los tiempos de cada posición, con márgenes honestos de **±3–5° en ángulos del plano de la imagen, ±1–3 cm en desplazamientos y ±1 cuadro en eventos**. Lo que el video no mide (giro de pelvis y tórax, X-factor, velocidades de la secuencia cinemática, ángulos de muñeca, cara, path y velocidad del palo) no se informa con números: se infiere del vuelo de la pelota con las leyes modernas. Según esas leyes, la cara explica **entre el 61 % y el 85 % de la dirección de salida** y la diferencia cara–path explica la curva. Las fallas se nombran con las 16 características de TPI, pero solo dos tienen receta de video publicada por TPI (over the top y flat shoulder plane). El resto se juzga contra el address del mismo jugador, porque no existe ningún umbral en centímetros validado. El análisis anterior llamó "en plano" a una bajada con las manos **14–23 cm por encima de su camino de subida**, y el problema no fue de precisión: esa diferencia es entre 3,5 y 11 veces el margen de medición. Faltaron un criterio relativo (bajada contra subida) y una regla que exija pruebas para decir "en plano". Casi todos los valores de tour que circulan son de fabricantes (Sportsbox, GEARS, GOLFTEC, HackMotion, TrackMan) o de TPI, sin revisión por pares, y ningún modelo de pose está validado contra captura con marcadores en el swing de golf. Por eso cada número del informe tiene que llevar su tipo de fuente. Los profesores, además, razonan hacia atrás (vuelo, impacto, causa en el movimiento, limitación física) y eligen una sola prioridad con un drill y su progresión. Un informe con ocho fallas del mismo peso se lee como amateur.

## Siete etiquetas de evidencia, y casi ningún número de tour revisado por pares

La primera conclusión de la investigación es incómoda: la biomecánica de tour revisada por pares es escasa, de muestras chicas y casi siempre de laboratorio 3D. Los dos estudios más usados miden a **10 profesionales con hierro 5** (Meister et al. 2011: 8 cámaras ópticas a 240 Hz) ([Meister 2011](https://people.stfx.ca/smackenz/Courses/DirectedStudy/Articles/Meister%20-%20Rotational%20Biomechanics%20of%20the%20Elite%20Golf%20Swing.pdf)) y a **100 golfistas recreativos con driver** (Myers et al. 2008: 200 Hz) ([Myers 2008](https://chs.uky.edu/sites/default/files/2023-12/Myers_2008_Role%20of%20upper%20torso%20and%20pelvis%20during%20golf%20swing.pdf)). La mayoría de los valores "de tour" que citan los medios viene de fabricantes:
- Sportsbox AI: 3D sin marcadores a partir de un video de celular;
- GEARS: captura óptica, con datos publicados en un foro por un dueño del sistema;
- GOLFTEC SwingTRU;
- HackMotion: sensor de muñeca;
- TrackMan: radar.

TPI publica definiciones y algunos números propios sin método. Sus probabilidades del tipo "si fallás este test tenés X % de chances de tener tal característica" circulan por gimnasios certificados, no por artículos.

El mismo nombre tampoco garantiza la misma medida. En un golfista de hándicap 7, el X-factor en el tope con driver dio **−71,9° con una secuencia de ángulos de Cardan y −123,5° con otra**, sobre el mismo swing ([Joyce et al. 2010](https://people.stfx.ca/smackenz/Courses/DirectedStudy/Articles/Joyce%202010%20Methodological%20considerations%20for%20the%203D%20measurement%20of%20the%20X-factor.pdf)). Las proyecciones al plano horizontal de Meister y Myers dan X-factors de 45–60°, y los rangos de Sportsbox, de 58–69°. La regla que sale es simple: no comparar un número del cliente con una referencia de otro sistema y no mezclar fuentes en un mismo juicio. Para que un profesor pueda auditar el informe, cada afirmación de este documento lleva una de estas etiquetas, y el producto debería hacer lo mismo con su propia redacción.

| Etiqueta | Qué significa | Ejemplos | Cómo decirlo en el producto |
|---|---|---|---|
| **[PR]** | Artículo revisado por pares | Meister 2011, Myers 2008, PING 2018, Hunter 2022, Gulgin 2014 | "Estudio publicado (n = …)" |
| **[CONF]** | Actas de congreso o preprint | Byrne y Kenny 2008, Sweeney 2012, Grober 2006, GolfDB, GolfPose | "Estudio preliminar" |
| **[FAB]** | Datos o guías de un fabricante o proveedor | TrackMan, Sportsbox, GEARS, GOLFTEC, HackMotion, V1 | "Dato del fabricante, sin validación independiente" |
| **[TPI]** | Definiciones y datos propios de TPI | Las 16 características; 67 % con early extension | "Según TPI (dato propio, sin método publicado)" |
| **[INS]** | Criterio de instructores o de medios especializados | GOLF.com Top 100, The Sand Trap, Golf Digest | "Criterio de enseñanza" |
| **[CP] / [INF]** | Cálculo geométrico propio o inferencia de este informe | Error por ubicación de cámara; márgenes de error | "Estimación propia" |
| **[NV]** | No verificado: solo fragmento de buscador, página bloqueada o foro sin datos | Porcentajes de blogs; el nombre "tush line" | No usar como dato |

## Las referencias de tour sirven contra el address propio, no como norma absoluta

### El giro separa a los mejores, pero una sola cámara no lo ve

Los mejores jugadores no giran más la pelvis: separan más el tórax de la pelvis. En Myers, el giro del tórax y el de la pelvis en el tope **no difirieron** entre los grupos de menor y mayor velocidad de pelota (p = 0,264 y 0,660). La separación sí: **44° contra 59°** (p < 0,0001) [PR] ([Myers 2008](https://chs.uky.edu/sites/default/files/2023-12/Myers_2008_Role%20of%20upper%20torso%20and%20pelvis%20during%20golf%20swing.pdf)). Meister encontró lo mismo dentro de cada sujeto [PR]:
- el X-factor máximo se correlacionó con la velocidad del palo (mediana ρ = 0,900) y el giro de la pelvis apenas (ρ = 0,572);
- los amateurs llegaron al impacto con **menos X-factor (23–25°) que los profesionales (33 ± 6°)**, señal de que el tórax alcanza a la pelvis antes de tiempo ([Meister 2011](https://people.stfx.ca/smackenz/Courses/DirectedStudy/Articles/Meister%20-%20Rotational%20Biomechanics%20of%20the%20Elite%20Golf%20Swing.pdf)).

El "X-factor stretch" (la separación que sigue creciendo al empezar la bajada) fue de 19 % en los jugadores hábiles contra 13 % en los menos hábiles, en un capítulo de 2001 del que solo se leyó el resumen [CONF] ([Cheetham et al. 2001](https://works.bepress.com/philip_martin/5/)). En la tabla de Myers, en cambio, ese aumento es de apenas 1,4–2,7° (cálculo propio). Las definiciones no coinciden, así que "stretch %" no se cita sin decir de quién es.

| Parámetro | Meister 2011 [PR]: 10 profesionales, hierro 5, plano horizontal | Myers 2008 [PR]: grupo rápido, n = 14, hcp 1,8, driver | Sportsbox "Tour Range" [FAB, alojado en un sitio no oficial]: hombres hierro 6 / hombres driver / LPGA driver |
|---|---|---|---|
| Giro del tórax en el tope | 99 ± 6° (máximo) | 104 ± 10° | 90–100 / 94–106 / 96–110° |
| Giro de la pelvis en el tope | 46 ± 6° | 45 ± 10° | 33–43 / 39–47 / 41–50° |
| X-factor máximo | 56 ± 4° | 59 ± 8° en el tope; 62 ± 8° en la bajada | 59–69 / 59–68 / 58–67° |
| Pelvis abierta en el impacto | — | 38 ± 7° | ≈40° (Golf Digest) |
| Tórax abierto en el impacto | — | 25 ± 9° | ≈30° (Golf Digest) |

Fuentes de Sportsbox: [informe hierro 6](https://moccasin-micheline-88.tiiny.site/D1-Male-Player-Swing-Score-Report.pdf), [informe driver](https://moccasin-micheline-88.tiiny.site/Bryson-Driver-Swing-Score-Report-1.pdf), [informe LPGA](https://moccasin-micheline-88.tiiny.site/LPGA-Tour-Player-Swing-Score-Report.pdf) y [Australian Golf Digest](https://www.australiangolfdigest.com.au/useful-golf-swingfacts-sportsbox-ai-graph).

Lo que sí es un patrón firme es que la pelvis llega al impacto más abierta que el tórax. Según Sportsbox, eso se ve en **el 100 % de los jugadores de tour con hierros** [FAB] ([GOLF.com](https://golf.com/instruction/three-musts-solid-ball-striking-sportbox-ai-playsmart/)), y es coherente con Myers. Para el producto, de todos modos, estos números son contexto y no medidas: el giro ocurre en el plano transversal, que una cámara ve solo como escorzo. Ni siquiera los sensores inerciales dedicados lo resuelven con precisión: comparados con 10 cámaras ópticas en 36 golfistas, tuvieron límites de acuerdo de **−9,6 a +11,1° en la pelvis y de −21,4 a +18,6° en el X-factor** [PR] ([PMC10611231](https://pmc.ncbi.nlm.nih.gov/articles/PMC10611231/)). Un celular no puede prometer más que eso.

### La pelvis de tour termina 6 a 14 cm más cerca del objetivo en el impacto

De frente, el dato más útil es el desplazamiento lateral de la pelvis respecto del address. Las fuentes coinciden en la dirección, pero no en el tamaño, y una de ellas se contradice con otra en la subida. La tabla junta lo disponible, con su tipo de fuente. Las pulgadas están pasadas a centímetros.

| Medida (vista de frente) | Valor de referencia | Fuente y tipo |
|---|---|---|
| Pelvis en el impacto respecto del address (+ hacia el objetivo) | Hierros 11,9 cm (rango intercuartil 8,1–14,0; total 4,1–22,9). Driver 8,9 cm (6,1–10,4; total −1,3 a 27,4) | GEARS, 61 swings de jugadores de tour, en un foro [FAB/foro] ([The Sand Trap](https://thesandtrap.com/forums/topic/111900-gears-pro-data-axis-tilt-vs-pelvis-sway-shift/)) |
| Pelvis en el impacto | "~10 cm (4 in)" en un traslado normal | [TPI] ([Hanging Back](https://www.mytpi.com/improve-my-game/swing-characteristics/hanging-back)) |
| Pelvis en el impacto | Profesionales +4,1 cm; jugadores de más de 100 golpes −1,0 cm | GOLFTEC SwingTRU [FAB] ([Golf Digest ME](https://golfdigestme.com/swing-numbers-new-study-unlocks-6-swing-secrets/)) |
| Tórax o costillas en el impacto | Hierros 5,8 cm (3,8–7,9); driver 1,0 cm (−2,3 a 2,3) | GEARS [FAB/foro] (mismo enlace) |
| Tren superior en la bajada | 5–7,6 cm, siempre menos que la pelvis | [TPI] ([Forward Lunge](https://www.mytpi.com/improve-my-game/swing-characteristics/forward-lunge)) |
| Pelvis en el tope | Clearwater (GOLFTEC): 0,8 cm alejada del objetivo con el brazo paralelo y luego 1,3 cm hacia el objetivo, o sea, apenas adelante del address. SwingTRU: 9,9 cm hacia el objetivo. Golf Digest (Sportsbox): menos de ~5 cm alejada | [FAB], **en conflicto** ([GOLF.com](https://golf.com/instruction/nick-clearwater-calrifies-hip-sway-misunderstanding/); [GOLFTEC](https://scramble.golftec.com/blog/2016/09/hip-movement-good-golf-swing/)) |
| Altura de la pelvis en la bajada | Baja 2,5–8,4 cm al empezar y sube 3,6–10,9 cm hacia el impacto | Sportsbox "Tour Range" [FAB, sitio no oficial] ([informe hierro 6](https://moccasin-micheline-88.tiiny.site/D1-Male-Player-Swing-Score-Report.pdf)) |
| Inclinación del eje pelvis–hombros en el impacto (90° = vertical) | Hierros 103,9° (101,2–106,5); driver 108,0° (104,0–111,1) | GEARS [FAB/foro] |
| Cabeza, vista de frente, driver | Hándicap bajo (4,5): 5,5 ± 3,0 cm en el tope y 3,1 ± 0,9 cm en el impacto. Hándicap medio (17,8): 12,4 ± 1,7 cm y 5,2 ± 0,6 cm. En el impacto, los dos grupos quedaron de lados opuestos del address (no se pudo verificar el sentido exacto) | Byrne y Kenny 2008, n = 8 [CONF] ([ISBS](https://ojs.ub.uni-konstanz.de/cpa/article/view/1991/1859)) |

Hay tres conclusiones defendibles. La primera es que la pelvis por delante del tórax en el impacto es la norma. Con hierros, una pelvis que llega al impacto en su posición del address o detrás queda fuera de toda la muestra de GEARS (el mínimo fue 4,1 cm); con driver queda en el extremo. Eso define el hanging back con datos, aunque con fuentes de fabricante [INF]. La segunda es que el patrón vertical de "bajar y después subir" la pelvis es de tour: subir la pelvis hacia el impacto no es una falla por sí mismo. La tercera es que **no existe ningún valor publicado de cuánto avanza la pelvis hacia la pelota** (thrust, la early extension en cm), ni de Sportsbox, ni de GEARS, ni de la literatura. La early extension se juzga contra la línea del address del propio golfista. Con la cabeza pasa algo parecido: los golfistas hábiles la mueven unos centímetros; la idea de una cabeza inmóvil no tiene respaldo. Sportsbox informa que el tórax de tour se desplaza ~5 cm alejándose del objetivo en la salida con driver y vuelve cerca de cero [FAB] ([Australian Golf Digest](https://www.australiangolfdigest.com.au/useful-golf-swingfacts-sportsbox-ai-graph)).

### Postura, rodillas, muñecas, varilla y ritmo: pocas normas y muy dependientes de la definición

**Inclinación del tronco.** Sportsbox informa una inclinación del tórax hacia adelante de ~30° en el address y de nuevo en el impacto, y una inclinación lateral de ~15° alejándose del objetivo en el address y de más de 30° en el impacto [FAB] ([Australian Golf Digest](https://www.australiangolfdigest.com.au/useful-golf-swingfacts-sportsbox-ai-graph)). Un estudio 2D desde atrás, con otra definición, midió 45–60° [PR] ([Yamamoto et al. 2023](https://frontiersin.org/articles/10.3389/fspor.2023.1272038/full)). La diferencia muestra que el valor absoluto depende del método. Lo comparable es el **cambio** respecto del address del mismo jugador. El mismo estudio aporta un dato valioso para el producto: la variación de la inclinación entre tiros se correlacionó con el score promedio (**r = 0,801**). Medir la consistencia entre los tres swings de cada toma es algo que el ojo no puede hacer.

**Rodillas.** La única norma confiable es la flexión de la rodilla líder en el tope: **35 ± 5° en hombres y 17 ± 6° en mujeres** con experiencia (Egret et al., citado en una revisión sistemática que agrega que la flexión en el impacto "sigue sin estar clara") [PR] ([Baker et al. 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5684267/)).

**Muñeca líder.** Una muñeca líder extendida ("cupped") en el tope no es una falla. Los 10 jugadores hábiles de un estudio con 12 cámaras la tenían extendida (**27 ± 8°**) y después la flexionaban 46° en la bajada [CONF] ([Sweeney et al. 2012](https://ojs.ub.uni-konstanz.de/cpa/article/view/5195/4770)). HackMotion da 0–30° de extensión en el tope y ±10° en el impacto como rango de tour [FAB] ([HackMotion](https://hackmotion.com/learn-from-pga-tour-player-wrist-data)). Desde un video 2D esto solo se describe como "se ve cupped o bowed".

**Inclinación de la varilla en el impacto (shaft lean).** No apareció ningún promedio de tour primario. Titleist dice que los mejores la inclinan 10–15° hacia el objetivo con wedges [INS] ([Titleist](https://www.titleist.com/teamtitleist/b/tourblog/posts/titleist-tips-lean-the-shaft-for-more-consistent-distance-wedges)), y con driver casi no hay inclinación [FAB] ([HackMotion](https://hackmotion.com/shaft-lean-at-impact/)). Conviene informarla como presente, ausente o hacia atrás, no en grados.

**Ritmo.** El famoso **3:1** viene del libro *Tour Tempo* de John Novosel: 24 cuadros de subida y 8 de bajada a 30 fps, con un rango de 21/7 a 30/10. Grober y Cholewicki lo confirmaron con acelerómetros en el palo: los profesionales están entre 2,5 y 3,5, con una subida de 0,7–0,8 s. Pero los amateurs también promedian ≈3,0, con más dispersión [CONF] ([Grober y Cholewicki 2006](https://arxiv.org/abs/physics/0611291)). El ratio no distingue niveles. Lo que sí los distingue es la consistencia entre swings y el tiempo total.

**Secuencia cinemática.** Va de la pelvis al tórax, al brazo y al palo, y las velocidades máximas de tour en hombres son de ~370–540 °/s en la pelvis y ~1.960–2.360 °/s en la varilla según Sportsbox [FAB] ([informe driver](https://moccasin-micheline-88.tiiny.site/Bryson-Driver-Swing-Score-Report-1.pdf); [Cheetham](https://philcheethamthe3dguy.blogspot.com/2009/11/kinematic-sequence-signature-of.html)). No se mide en 2D. Como mucho, a 240 fps se puede describir el orden en que aparecen algunos eventos visibles.

### Lo que se mide con un celular y lo que necesita 3D o radar

No se encontró ningún estudio que valide ángulos articulares de golf medidos en 2D (MediaPipe o similar) contra captura 3D. Un estudio fuera del golf, con movimientos de saltos y cambios de dirección, encontró que el 2D y el 3D coinciden en promedio dentro de 5° en el plano frontal, pero con límites de acuerdo de hasta −12,8 a 21,3° en la pelvis [PR] ([IJSPT 2022](https://doaj.org/article/f12ab9f81be643da965e432c6585f3d2)). La clasificación siguiente es una inferencia [INF] que combina esa evidencia con la geometría de la cámara.

| Parámetro | Desde atrás | De frente | Veredicto para 2D |
|---|---|---|---|
| Momentos P1–P10 y ritmo | sí | sí | Confiable con archivo a velocidad real y ≥60 fps |
| Desplazamiento lateral de pelvis y tórax respecto del address | — | sí | Aproximado: ±1–3 cm con escala en el plano del cuerpo |
| Cabeza: lateral / vertical / profundidad | profundidad y vertical | lateral y vertical | Aproximado |
| Inclinación lateral de la columna | — | sí | Aproximado; la definición difiere de GEARS y Sportsbox |
| Inclinación de la varilla en el impacto | — | sí | Solo con el cuadro de impacto real y la cámara perpendicular |
| Inclinación del tronco y su cambio | sí | — | Aproximado; se juzga el cambio, no el valor absoluto |
| Pelvis hacia la pelota (early extension) | sí | — | Aproximado; no existe norma de tour en cm |
| Caída y subida de la pelvis | sí | sí | Aproximado |
| Flexión de rodillas | parcial | parcial | Grosero: error por el ángulo fuera del plano de la imagen |
| Plano de manos y varilla; over the top | sí | — | Aproximado: ±2–4 cm |
| Giro de pelvis y tórax; X-factor | no | no | Necesita 3D |
| Velocidades de la secuencia cinemática | no | no | Necesita 3D o sensores |
| Flexión o extensión de muñeca | no | no | Necesita sensor; en video, solo descripción |
| Cara, path en grados, loft dinámico, velocidad | no | no | Necesita launch monitor |

## Over the top exige dos pruebas coincidentes y una cámara verificada

Según TPI, over the top es "quizás la falla más común entre los hándicaps altos". Es también la que más rigor necesita, porque es la que se erró en el análisis anterior. TPI la atribuye a un "uso excesivo del tren superior en la bajada": el palo sale por fuera del plano y la cabeza llega a la pelota de afuera hacia adentro, y eso **produce un pull si la cara está square y un slice si está abierta** [TPI] ([TPI, Over the Top](https://www.mytpi.com/improve-my-game/swing-characteristics/over-the-top)). Es una de las dos características con receta de video publicada:
1. En la vista desde atrás, se dibuja una línea por la varilla del address, prolongada por encima del hombro (línea A).
2. Se dibuja otra a lo largo del palo cuando el antebrazo líder pasa apenas la horizontal en la subida, cerca de P3 (línea B).
3. El espacio entre las dos es el "slot". Si en la bajada el palo pasa "por fuera o por encima del slot", hay over the top.

V1 suma un criterio relativo [FAB]: la cabeza del palo aparece por fuera de las manos al empezar la bajada, y en P5 se pregunta si el palo está "por encima o por debajo del plano de la subida" ([V1](https://swing-analysis.v1sports.com/swing-analysis/over-the-top-analysis)). Ojo: la guía de V1 llama P6 al impacto, una numeración distinta de la estándar. Los instructores agregan pistas no validadas [INS]. Si la varilla baja "a través del antebrazo de atrás", los tiros salen derechos ([RotarySwing](https://rotaryswing.com/golf-instruction/swingfundamentals/golf-shaft-forearm-plane)). Para Brian Mogg, una bajada empinada es aquella en que "la varilla está demasiado vertical y el plano queda por encima de un camino natural de vuelta al impacto" ([GOLF.com, Top 100](https://golf.com/instruction/too-steep-meaning-top-100-roundtable/)).

En esa misma mesa redonda, Dom DiJulia define "empinado" como una cabeza del palo que viaja más hacia abajo de lo previsto. Eso no equivale a pegarle hacia abajo, que es normal: el ángulo de ataque promedio del PGA Tour con hierro 7 es **−3,9°** en la tabla de TrackMan de 2023 [FAB] ([TrackMan](https://www.trackman.com/blog/introducing-updated-tour-averages)). Ninguna fuente publica un umbral validado en grados o centímetros para over the top.

El caso del swing 2 muestra por qué hace falta una regla de decisión explícita. Según los datos internos del proyecto (`swing-analisis/CLAUDE.md`):
- las manos bajaron **14–23 cm por encima de su camino de subida**;
- la varilla en P5 estaba **14° más empinada que en P3**;
- el tope estaba cruzado.

Contra un margen de ±2–4 cm para las manos respecto del plano y de ±3–5° para los ángulos de la varilla, esa diferencia no es ruido. Cumple el criterio de V1 (bajada por encima del plano de subida) y, casi con seguridad, el slot de TPI.

Un cálculo geométrico propio muestra cómo puede quedar oculta si se compara contra la línea del address en vez de contra la subida. Con la cámara a 3 m, ponerla a la altura del pecho o en la línea de la pelota corre hacia abajo (hace ver más planas) las posiciones que están en plano **entre 7 y 16 cm** [CP]. Es el mismo orden que el over the top medido. Como la subida y la bajada pasan por profundidades parecidas, compararlas entre sí cancela casi todo ese sesgo [CP/INF].

El tope cruzado, en cambio, no es una falla en sí. Mickelson y Daly cruzan el palo en el tope, y los instructores lo aceptan "mientras el jugador pueda aplanarlo en la bajada" [INS] ([Australian Golf Digest](https://www.australiangolfdigest.com.au/allow-the-club-to-cross-the-line-to-hit-more-booming-draws/); [Golf Today](https://golftoday.co.uk/leslie-king-tuition-series-an-end-to-trial-error-golf-lesson-8/)). La falla la define la bajada.

| Paso | Qué se hace | Qué se concluye |
|---|---|---|
| 0. Control de cámara | Cámara desde atrás en la línea de las manos, a la altura de las manos y nivelada. Las dos varillas del piso tienen que converger cerca del centro de la imagen; el giro de la cámara se calcula como θ = atan(d/f) | Si el control falla, las pruebas contra líneas absolutas pierden validez: se usa solo la prueba relativa y se informa |
| 1. Slot de TPI | Líneas A y B; se revisan la varilla y la cabeza del palo en P5 y P6 | Entre A y B: en el slot. Por encima o por fuera de B: over the top. Por debajo de A: debajo del plano ("atascado") |
| 2. Bajada contra subida (V1) | Distancia perpendicular entre el camino de las manos en la bajada y en la subida, a la misma altura (P5 contra P3, P6 contra P2). Ángulo de la varilla en P5 contra P3 | Si la bajada queda por encima de la subida por más que el margen (más de ~4 cm o ~5°): over the top |
| 3. Pistas secundarias | Cabeza del palo por fuera de las manos al empezar la bajada; varilla por encima del antebrazo de atrás en P6 | Refuerzan, no deciden |
| 4. Vuelo y contacto | Pull, pull-slice o slice; divot hacia la izquierda; descartar un golpe de talón con driver | Confirma el path de afuera hacia adentro. Un slice solo no alcanza |

La regla que propone este informe es asimétrica [INF]:
- se dice "over the top" cuando la prueba 1 o la 2 supera el margen y además coincide al menos una pista o el vuelo;
- se dice "en plano" solo cuando las dos pruebas quedan dentro del margen;
- si la cámara no pasa el control y la diferencia es chica, se informa "no evaluable".

La asimetría es deliberada: nunca se da por correcto un fundamento por falta de evidencia en contra.

Las consecuencias se explican con las leyes modernas. El over the top da un path negativo y, con hierros, un ataque más empinado. La cara decide si sale un pull (cara igual al path) o un slice (cara abierta respecto del path), así que no todo slice es over the top [TPI]. Con driver, además, un golpe de talón cierra la cara por gear effect: la pelota sale a la izquierda y curva a la derecha, imitando un pull-slice aunque el path sea bueno [FAB] ([GOLFTEC](https://scramble.golftec.com/blog/2018/05/bulge-and-roll-and-gear-effect/)). Antes de llamar over the top a un slice con driver hay que pedir la marca del impacto.

**Causas físicas.** Según TPI, iniciar la bajada con el traslado del tren inferior requiere buena movilidad de cadera, core y glúteos fuertes y capacidad de separar el tren inferior del superior [TPI]. HackMotion atribuye la raíz a la muñeca líder demasiado extendida en el tope [FAB] ([HackMotion](https://hackmotion.com/over-the-top-golf-swing/)). Esa explicación choca con el dato de Sweeney de que todos los jugadores hábiles tienen la muñeca extendida en el tope. El único estudio revisado por pares que cruzó el screen de TPI con 14 fallas **no encontró ninguna asociación significativa con over the top** [PR] ([Gulgin et al. 2014](https://pubmed.ncbi.nlm.nih.gov/24476744/)).

## Las otras características se juzgan contra el address del propio golfista

### Early extension: distinguir la pelvis que avanza de la que sube

TPI define la early extension con tres redacciones distintas según la página:
- "cualquier movimiento hacia adelante (empuje) del tren inferior hacia la pelota durante la bajada" ([TPI, Early Extension](https://www.mytpi.com/improve-my-game/swing-characteristics/early-extension));
- "cualquier movimiento de la pelvis hacia la pelota en la subida o la bajada" ([TPI, artículo](https://www.mytpi.com/articles/swing/early-extension-swing-characteristic));
- "cualquier movimiento hacia la pelota durante el swing" ([TPI, índice](https://www.mytpi.com/improve-my-game/swing-characteristics)).

En el artículo, TPI afirma dos cosas:
- **el 67 % de más de 90.000 golfistas evaluados** tiene early extension;
- **el 99 % de más de 100 jugadores de PGA Tour, European Tour y LPGA evaluados no la tiene**.

Las dos son datos propios de TPI, leídos en la página, sin método publicado ni revisión por pares. El mismo artículo la llama "característica" y no "falla", porque algunos golfistas se mueven así por ser "la forma más efectiva de swingar con sus herramientas físicas".

El debate público parece contradecir el 99 %. Algunos profesores citan a Jack Nicklaus como ejemplo de extensión, y Peter Kostis escribió "So much for early extension being terrible for your swing!" [INS] ([GOLF.com](https://golf.com/instruction/is-early-extension-good-or-bad-heres-what-you-need-to-know/)). La contradicción se resuelve separando dos direcciones. La pelvis que **baja y después sube** antes del impacto es un patrón de tour: Sportsbox la usa como indicador de potencia ([GOLF.com, Sportsbox](https://golf.com/instruction/driving/pelvic-lift-generate-power-sportsbox-ai/)), y TPI, según un gimnasio certificado, dice que los mejores retrovierten la pelvis "hasta 20°" en la bajada [TPI, de segunda mano] ([Pinnacle](https://pinnaclefitness.squarespace.com/blog/the-power-of-golf-tpi-screen-pelvic-tilt)). La pelvis que **avanza hacia la pelota** es early extension. Lo más probable es que el 99 % de TPI y la "extensión" de Nicklaus hablen de cosas distintas [INF].

**Criterio en video.** Se juzga desde atrás. Se traza una vertical tangente a la nalga de atrás en P1, la "tush line" (el nombre es de uso común y no tiene fuente primaria [NV]). Después se mide cuánto se despega la nalga hacia la pelota en P4, P5, P6 y P7, y cuánto se achica la distancia entre la cadera y la pelota. V1 dice que se ve mejor de frente [FAB] ([V1](https://swing-analysis.v1sports.com/swing-analysis/early-extension-analysis)), pero el avance hacia la pelota cae en el plano de la imagen desde atrás, no de frente. Como no hay norma en cm, se informa de forma graduada ("en P7 la nalga queda X cm por delante de su línea, ±1–3 cm") y no como aprobado o desaprobado.

**Vuelo y causas físicas.** TPI la vincula con el palo "atascado" detrás del cuerpo, el block a la derecha y el hook a la izquierda, golpes pesados y finitos en el juego corto y el shank [TPI]. Es la única característica con evidencia física revisada por pares. Gulgin et al. encontraron que no tocarse la punta de los pies se asocia con early extension (p = 0,015) y que fallar el puente del lado derecho se asocia con early extension (p = 0,050) y con pérdida de postura (p = 0,028). Los que no completaban la sentadilla profunda con los brazos arriba o el equilibrio en la pierna izquierda tenían **2 a 3 veces** más probabilidad de early extension, pérdida de postura o slide [PR] ([Gulgin et al. 2014](https://pubmed.ncbi.nlm.nih.gov/24476744/)).

### Sway, slide, hanging back y forward lunge: dirección, fase y cuánto es normal

TPI separa estas cuatro características por fase y dirección [TPI]:
- **Sway:** movimiento lateral excesivo del tren inferior que se aleja del objetivo en la subida y lleva el peso al borde externo del pie de atrás ([TPI, Sway](https://www.mytpi.com/improve-my-game/swing-characteristics/sway)).
- **Slide:** lo mismo, pero hacia el objetivo en la bajada ([TPI, Slide](https://www.mytpi.com/improve-my-game/swing-characteristics/slide)).
- **Hanging back:** falta de traslado hacia el objetivo, con el jugador todavía sobre el pie de atrás en el impacto.
- **Forward lunge:** el tren superior se mueve hacia el objetivo más que el inferior. Lo normal, según TPI, son unos 10 cm de pelvis y 5–7,6 cm de tren superior.

V1 propone un criterio de frente para el sway: la cadera de atrás pasa por fuera del pie de atrás entre P2 y P4 [FAB] ([V1](https://swing-analysis.v1sports.com/swing-analysis/hip-sway-analysis)).

Los datos de tour sobre la subida se contradicen entre sí [FAB]. Clearwater (GOLFTEC) dice que los jugadores de tour terminan el tope apenas más cerca del objetivo que en el address. SwingTRU, también de GOLFTEC, informa 9,9 cm hacia el objetivo en el tope. Por eso el sway se marca con el criterio más conservador [INF]: el centro de la pelvis claramente alejado del objetivo en P4 y la cadera por fuera de la vertical del pie de atrás.

El slide necesita dos condiciones, porque trasladarse 6–14 cm hacia el objetivo es normal en el tour. Hay que ver la cadera líder claramente más allá de su vertical **y además** poca rotación. Como referencia [FAB], SwingTRU midió la cadera abierta 36° en el impacto en profesionales contra 19,5° en jugadores de más de 100 golpes ([Golf Digest ME](https://golfdigestme.com/swing-numbers-new-study-unlocks-6-swing-secrets/)).

### Las demás características y los patrones de tour que no son fallas

Varias características dependen de una regla de fase:
- **Pérdida de postura:** cualquier "alteración significativa de los ángulos del address", según TPI. Se marca solo entre P4 y P7, porque TPI aclara en la página de Late Buckle que levantarse hacia el final después del impacto es normal ([TPI, Late Buckle](https://www.mytpi.com/improve-my-game/swing-characteristics/late-buckle)).
- **Late buckle:** la caída y flexión brusca de las rodillas después del impacto. Para TPI, la causa es "casi siempre" física.
- **Reverse spine angle:** el tronco inclinado hacia el objetivo en el tope. TPI la considera una de las principales causas de dolor lumbar ([TPI](https://www.mytpi.com/improve-my-game/swing-characteristics/reverse-spine-angle)).
- **Flat shoulder plane:** tiene receta de video. Desde atrás se traza en P1 una línea del cóccix a la nuca y una paralela justo por encima del hombro de atrás. Si en P4 el hombro líder queda por encima de esa paralela, el plano de hombros es plano ([TPI, Flat Shoulder Plane](https://www.mytpi.com/improve-my-game/swing-characteristics/flat-shoulder-plane)).

SwingTRU aporta el contexto [FAB]: en el tope, los profesionales inclinan los hombros 36° contra 29,6° de los hándicaps altos. Los hombros "nivelados" son el patrón amateur.

Del otro lado están los patrones que un profesor reconoce como normales y que un análisis amateur marca como errores:
- el **codo volador**, que según TPI "no es necesariamente una falla y muchos grandes jugadores lo tienen" ([TPI, Flying Elbow](https://www.mytpi.com/improve-my-game/swing-characteristics/flying-elbow));
- el palo **cruzado o laid off** en el tope;
- la muñeca líder extendida en el tope;
- la pelvis que sube y la rodilla líder que se estira hacia el impacto;
- la pelvis más abierta que el tórax en el impacto;
- el traslado lateral hacia el objetivo;
- la cabeza que se mueve unos centímetros.

Todos se describen y se convierten en falla solo si el impacto lo paga: path, cara, centro del golpe o low point.

### El screen físico: TPI afirma mucho, la evidencia revisada confirma poco

TPI vincula cada característica con limitaciones físicas y tests de su screen. Las probabilidades que circulan vienen de un gimnasio certificado y son afirmaciones de TPI de segunda mano [TPI] ([Pinnacle](https://pinnaclefitness.squarespace.com/blog/the-power-of-golf-tpi-screen)). Algunos ejemplos:
- un S-posture daría "80 % de chances" de early extension;
- fallar el pelvic tilt, 70 % de early extension;
- fallar la rotación pélvica, 55 % de over the top.

La evidencia revisada por pares es más modesta:
- Gulgin et al. encontraron solo tres asociaciones significativas entre el screen y 14 fallas definidas por TPI.
- Una crítica posterior les objetó medir fallas y no rendimiento ([Speariett y Armstrong 2020](https://insight.cumbria.ac.uk/id/eprint/5880)).
- Sell et al. mostraron, en 257 golfistas, que los de hándicap menor que 0 tienen más fuerza, flexibilidad y equilibrio que los de hándicap 10–20, sin vincularlo a fallas concretas [PR] ([Sell et al. 2007](https://chs.uky.edu/sites/default/files/2023-12/Sell_2007JSCR_Strength%20flexibility%20and%20balance%20characteristics.pdf)).

La redacción defendible es "esta característica suele tener una causa física (por ejemplo, la rotación de la cadera líder); un screen de TPI lo confirmaría". El análisis por video no diagnostica la limitación física.

## La cara manda la salida y la diferencia cara–path manda la curva

Durante años, el examen de la PGA of America exigía afirmar que la pelota sale en la dirección del path. El estudio de PING sobre el tema lo llama un malentendido [PR] ([Wood, Henrikson y Broadie 2018](https://mdpi-res.com/proceedings/proceedings-02-00249/article_deploy/proceedings-02-00249.pdf)). Ese trabajo midió 157 golfistas con captura óptica a 720 fps y un GC2, contando solo golpes a menos de 6,35 mm del centro de la cara. La salida horizontal se fue hacia la cara en estas proporciones:
- **76 % ± 8 % con driver**;
- **69 % ± 3 % con hierro 7**;
- **61 % ± 7 % con wedge**;
- 63 % con un robot.

La proporción baja a medida que sube el spin loft.

La cifra más difundida, "75 % en hierros medios y 85 % en driver", es una cifra de enseñanza de TrackMan University. Titleist la atribuye a Niklas Bergdahl, pero solo se pudo leer en fragmentos de búsqueda [FAB/NV] ([Titleist Learning Lab](https://www.titleist.com/learning-lab/performance/physics-of-ball-striking-in-golf)). La frase defendible es "la cara controla la mayor parte de la salida, entre dos tercios y más de tres cuartos según el palo y el contacto". Un "75 %" exacto suena a falsa precisión. La guía actual del proyecto usa ≈75 %/≈85 % y debería actualizarse.

Las definiciones de TrackMan son el vocabulario que comparten los profesores [FAB] ([TrackMan, parámetros](https://www.trackman.com/blog/golf/40-trackman-parameters)):
- **Path:** el movimiento de adentro hacia afuera o de afuera hacia adentro del centro geométrico de la cabeza en la máxima compresión.
- **Ángulo de la cara:** hacia dónde apunta la cara en el punto de contacto.
- **Cara respecto del path (face to path):** la cara menos el path. Si la diferencia es positiva, la pelota curva a la derecha en un diestro, "cualquiera sea la mano" ([TrackMan](https://trackman.com/blog/golf/face-to-path)).
- **Spin loft:** el ángulo 3D entre la dirección de la cabeza y la orientación de la cara; restar el ángulo de ataque al loft dinámico da una buena aproximación. En el tour vale **14,7° con driver y 24,3° con hierro 6** ([TrackMan](https://www.trackman.com/blog/spin-loft)).
- **Eje de giro (spin axis):** un valor entre −2 y +2 "puede considerarse un tiro recto" ([TrackMan](https://www.trackman.com/blog/golf/spin-axis)).

El D-plane une todo: la pelota sale entre la cara y la dirección de la cabeza, y el eje de giro es perpendicular a ese plano [INS] ([The DIY Golfer](https://thediygolfer.com/d-plane-golf)). Con poco spin loft, la misma diferencia cara–path inclina más el eje. Por eso el driver curva más. Los ejemplos de TrackMan lo cuantifican [FAB]:
- con el driver de tour (251 m de carry), −2° de cara respecto del path son ~17 m de curva a la izquierda y +5° son ~40 m a la derecha;
- con el hierro 6 de tour, +2° son ~7 m.

John Parkinson resume que **1° de diferencia a 274 m produce ~11 m de curva** (mismo enlace).

El ángulo de ataque también mueve el path, y eso explica patrones que confunden. Como el palo gira sobre un plano inclinado, pegar hacia abajo corre el path hacia la derecha y pegar hacia arriba lo corre hacia la izquierda. Según una regla práctica, el efecto es 1:1 con driver y de la mitad con hierros [INS] ([Andrew Rice](https://terri-rice-0z1d.squarespace.com/andrew-rice-golf/tag/hitting+down); [Hattrick Golf](https://hattrickgolfinstruction.blogspot.com/2013/04/work-in-progress-understanding-ball.html)). Una aproximación geométrica propia es path ≈ dirección del swing − ataque / tan(plano). Con un hierro (plano de ~60°), −4° de ataque corren el path +2,3°. Con driver (~45°), +3° lo corren −3° [CP]. Así, "con el driver hago slice y con los hierros no" puede venir del ángulo de ataque y no de un swing distinto.

Los golpes fuera del centro rompen todo lo anterior. Con driver, un golpe de punta abre la cara, la pelota sale a la derecha y curva hacia el draw. Uno de talón la cierra, sale a la izquierda y curva hacia el fade [FAB] ([GOLFTEC](https://scramble.golftec.com/blog/2018/05/bulge-and-roll-and-gear-effect/)). Cuando el signo de la cara respecto del path contradice la curva, TrackMan lo usa como señal de golpe descentrado ([TrackMan](https://www.trackman.com/blog/golf/spin-axis)).

| TrackMan 2023 [FAB] | Velocidad del palo | Ataque | Velocidad de la pelota | Smash | Lanzamiento | Spin | Carry |
|---|---|---|---|---|---|---|---|
| PGA, driver | 115 mph (185 km/h) | −0,9° | 171 mph (275 km/h) | 1,49 | 10,4° | 2.545 rpm | 258 m |
| PGA, hierro 7 | 92 mph (148 km/h) | −3,9° | 123 mph (198 km/h) | 1,34 | 16,1° | 7.124 rpm | 161 m |
| PGA, PW | 84 mph (135 km/h) | −4,7° | 104 mph (167 km/h) | 1,24 | 23,7° | 9.316 rpm | 130 m |
| LPGA, driver | 96 mph (154 km/h) | +2,8° | 143 mph (230 km/h) | 1,49 | 12,6° | 2.506 rpm | 204 m |
| LPGA, hierro 7 | 78 mph (126 km/h) | −2,5° | 106 mph (171 km/h) | 1,38 | 18,5° | 6.630 rpm | 131 m |
| LPGA, PW | 72 mph (116 km/h) | −3,2° | 88 mph (142 km/h) | 1,25 | 25,2° | 8.465 rpm | 101 m |

Fuente: [TrackMan, 2 de mayo de 2024](https://www.trackman.com/blog/introducing-updated-tour-averages). La tabla no publica path, cara, cara respecto del path ni loft dinámico. TrackMan asume cara respecto del path = 0 para todos los palos. El ataque del driver en el tour es casi neutro en el PGA y positivo en la LPGA, así que "pegale hacia abajo" no es un consejo universal.

Lo que un video de celular no puede hacer es medir la cara. A 240 fps, la cabeza de un hierro 7 de tour avanza ~17 cm entre cuadros, y a 60 fps, ~69 cm [CP]. Uno o dos grados de cara son entre 4 y 19 yardas de curva. La cara y el path se reconstruyen del vuelo informado por el jugador, invirtiendo las leyes [INF]: la curva da el signo y el tamaño aproximado de la cara respecto del path, y la salida da la cara. Por ejemplo, un hierro 6 de tour que sale 2° a la izquierda y curva ~18 m a la derecha implica una cara respecto del path de ≈ +5°, una cara de ≈ −0,5° y un path de ≈ −5,5°, de afuera hacia adentro. Es la firma clásica del over the top. El eslabón débil es la estimación del jugador, así que el resultado es una tendencia y no grados. El divot tampoco resuelve el path: solo muestra la dirección general del swing en el punto bajo [INS] ([GolfWRX](https://golfwrx.com/112812/understanding-swing-direction-vs-swing-path/)).

| Vuelo informado (diestro, golpe centrado) | Cara respecto del objetivo | Path | Cara respecto del path | Qué buscar en el video |
|---|---|---|---|---|
| Pull recto | Cerrada | De afuera hacia adentro, ≈ igual a la cara | ≈ 0 | Over the top; alineación a la izquierda |
| Pull-slice | A la izquierda, menos que el path | Muy de afuera hacia adentro | Positiva | Over the top con la cara abierta; con driver, descartar talón |
| Slice que sale al objetivo | ≈ square | De afuera hacia adentro | Muy positiva | Over the top; la cara abierta no se ve en el video |
| Push recto o block | Abierta, ≈ igual al path | De adentro hacia afuera | ≈ 0 | Early extension, pérdida de postura (TPI) |
| Push-hook | A la derecha, menos que el path | Muy de adentro hacia afuera | Negativa | Early extension "atascado" |
| Hook o pull-hook | Cerrada | Neutro o de adentro hacia afuera | Muy negativa | Early extension o pérdida de postura con flip |
| Falla para los dos lados | Variable | Por lo general de adentro hacia afuera | Cambia de signo | Early extension, pérdida de postura (TPI) |
| Pesado o finito | — | — | — | Punto bajo atrás: hanging back, casting, sway sin recuperar ([TrackMan](https://www.trackman.com/blog/golf/top-8-ways-to-practice-indoors-with-trackman)) |
| Alto, corto, con mucho spin | — | — | — | Casting, scooping, chicken winging, que suman loft [TPI] |
| Shank | — | — | — | Early extension, según el artículo de TPI |

## La cámara en la línea de las manos es la única que ve el plano de canto

La mayoría de las fuentes de enseñanza pone la cámara de atrás **en la línea de las manos, a la altura de las manos, nivelada y paralela a la línea del objetivo** [FAB/INS] ([V1](https://swing-analysis.v1sports.com/swing-analysis/down-the-line-view); [Titleist](https://www.titleist.com/teamtitleist/team-titleist/f/golf-tips/54984/online-golf-instruction-how-to-film-your-swing)). The Sand Trap prefiere la línea de las puntas de los pies y descarta filmar detrás de la pelota, que "distorsiona casi todas las fases del swing" [INS] ([The Sand Trap](https://thesandtrap.com/b/playing_tips/filming_your_swing)). Nadie publicó una medición del error, así que este informe lo calculó con un modelo de cámara estenopeica [CP]. Supuestos: hierro medio, manos a 0,75 m de altura, varilla a 58,3° y cámara a 3 m.

La explicación es geométrica. Un plano se ve como una línea solo si la cámara está dentro de él. El plano de la varilla del address contiene la línea de las manos a la altura de las manos, la línea del objetivo a nivel del piso y la línea de las puntas a ~1,05–1,10 m. Fuera de esos lugares, las posiciones que están en plano aparecen corridas.

| Ubicación de la cámara (a 3 m) | Palo 60 cm detrás y 60 cm arriba (zona P2/P6) | Palo 90 cm detrás y 1,2 m arriba | Cómo se ve |
|---|---|---|---|
| Línea de las manos, a la altura de las manos | 0 cm | 0 cm | Referencia |
| Línea del objetivo, a nivel del piso | −0,4 cm | −0,7 cm | Casi igual |
| Línea de las puntas, a 1,07 m | 0 cm | 0 cm | Igual (dentro del plano) |
| Línea de las puntas, a la altura de las manos | **+4,3 cm** | **+7,3 cm** | Más empinado: parece over the top |
| Mitad entre pelota y puntas, a la altura de las manos | −2,7 cm | −4,6 cm | Algo más plano |
| Línea de la pelota, a la altura de las manos | **−9,6 cm** | **−16,4 cm** | Mucho más plano: esconde un over the top |
| Línea de las manos, a la altura del pecho (1,25 m) | −6,6 cm | −11,2 cm | Más plano |
| Línea de las manos, baja (0,45 m) | +3,9 cm | +6,7 cm | Más empinado |

La regla es clara: **una cámara por encima del plano aplana el swing y una por debajo lo empina**. Coincide con lo que observan instructores en foros [NV] y con la advertencia de GOLF.com de que un ángulo torcido hace ver el takeaway "muy adentro" y cambia incluso cómo se percibe el ritmo [INS] ([GOLF.com](https://golf.com/instruction/bad-camera-angle-messing-with-your-golf-swing/?amp=1)). Alejarse reduce el error: a 3,7 m baja ~25 %, y a 6 m queda en ~45 % del valor a 3 m [CP]. La guía actual del proyecto pide la cámara de atrás "a la altura de los dedos del pie de atrás", a la altura de las manos. Esa posición empina el plano 4–7 cm y empuja hacia falsos over the top. Conviene pasarla a la línea de las manos o subir la cámara a ~1,05–1,10 m. La varilla del address, en cambio, se mide bien desde casi cualquier posición paralela: con 5° de giro de cámara su ángulo no cambia, y con 10° de giro y 10° de inclinación cambia 1,2° [CP].

De frente, la cámara va perpendicular a la línea del objetivo, centrada en el medio de la postura (con una varilla perpendicular como guía), a la altura de las manos o la cadera y a 1,8–3,7 m [INS/FAB] ([The Sand Trap](https://thesandtrap.com/b/playing_tips/filming_your_swing); [V1](https://swing-analysis.v1sports.com/swing-analysis/face-on-view)). El error más común es de escala. La pelvis está más lejos de la cámara que la pelota, así que, si la escala se toma en la línea de la pelota, **un sway real de 10 cm se mide como ~8 cm a 3 m**: se subestima ~20–25 % [CP]. El palo del address tampoco sirve como escala de frente, porque está ~32° fuera del plano de la imagen y se ve ~15 % más corto. Desde atrás, en cambio, está casi en el plano y es buena escala [CP]. Este principio está publicado: el escalado simple exige que el objeto de referencia esté en el mismo plano que lo medido, y su error crece con la inclinación de la cámara [PR] ([Brewin y Kerwin 2003](https://www.semanticscholar.org/paper/Accuracy-of-scaling-and-DLT-reconstruction-for-Brewin-Kerwin/6442d8afe29b2187fa1fa33de610639dad4b3f8a)).

Fuera del plano de la imagen, los ángulos se deforman. Un ángulo real de 90° se leyó como 110–112° con 45° fuera del plano y como ~180° con 90°. La corrección θ = arccos(largo aparente / largo real) lo dejó en ±2–3°, pero no se recomienda aplicarla por debajo de 20° [PR] ([Stevens et al. 2006](https://people.ohio.edu/stevensn/documents/Stevens%20et%20al%202006%20Technical%20note.pdf)).

Para medir en centímetros con una sola cámara hay herramientas estándar de visión por computadora:
- **Punto de fuga.** Dos varillas paralelas a la línea del objetivo dan el punto de fuga. Si la cámara de atrás apunta bien, ese punto cae en el centro de la imagen, y el desvío se calcula como θ ≈ atan(d/f).
- **Homografía del piso.** Un rectángulo de varillas medidas da la homografía del piso. Con ella se pasan a centímetros la pelota, los pies, el ancho de postura y la alineación [CP] ([Hartley y Zisserman](https://www.robots.ox.ac.uk/~vgg/hzbook/)).
- **Métrica de una sola vista.** Sirve incluso para alturas: en el trabajo de Criminisi et al. midió una persona de 180 cm como 178,8 cm [PR] ([Criminisi et al.](https://www.microsoft.com/en-us/research/publication/single-view-metrology-4/)).

En buenas condiciones (video vertical de 1080×1920 y ~1,4 mm por píxel), el presupuesto de error es de ±1 cm en cadera, cabeza y manos marcadas a mano, y de ±1° en segmentos del plano frontal [CP].

Los cuadros por segundo y el obturador deciden qué se puede leer del palo. The Sand Trap pide 200–300 fps y un obturador de al menos 1/1000 s [INS]. A 240 fps, la cabeza de un palo a 31–51 m/s avanza **13–21 cm entre cuadros**. Su estela dentro de un cuadro es de 13–21 cm a 1/240 s y de 3–5 cm a 1/1000 s [CP]. El "Slo-mo" del iPhone guarda el video a alta frecuencia con una curva de velocidad encima, y según cómo se exporte queda a 240, 120 o 30 fps [INS] ([Stolovitz](https://ben.stolovitz.com/posts/export-slo-mo-videos-from-your-iPhone/); [Apple](https://support.apple.com/guide/iphone/record-videos-iph61f49e4bb/ios)). Hay que pedir el original con la velocidad al 100 %, verificar los fps reales y usar el tiempo de cada cuadro, porque la frecuencia es variable.

Con dos celulares se puede sincronizar por el cuadro del impacto con ±1 cuadro de error. Sincronizar por sonido no alcanza: el audio y el video se codifican por separado [CONF] ([RocSync](https://arxiv.org/pdf/2511.14948)), y el sonido llega 2,9 ms más tarde por cada metro de diferencia de distancia [CP]. Para triangular en 3D hace falta el mismo swing filmado a la vez desde las dos vistas.

## Ningún modelo de pose está validado en golf contra marcadores

La validación de Sportsbox AI es un informe de la propia empresa, sin revisión por pares [FAB] ([Sportsbox](https://help.sportsbox.ai/sportsbox-ai-accuracy)). Comparó el sistema contra sensores electromagnéticos AMM3D:
- muestra: 30 golfistas, un swing cada uno;
- solo en el address, el tope y el impacto, y con pocos de sus más de 200 indicadores;
- resultado: **~2° de error angular y ~1 cm de error lineal**, con cámaras perpendiculares y obturador rápido.

No se encontró ninguna validación independiente. El único trabajo de golf que validó video 2D contra Vicon midió el ángulo de la varilla, no articulaciones, y lo hizo con digitalización manual: una cámara de frente a 240 Hz, con obturador de 1/2000 s, a 4 m. No hubo diferencias significativas en las posiciones clave. El error típico fue de **≈3,2° en el tope y 0,6–1,4° en el impacto, pero 19–20° en el final**, y el tiempo del swing coincidió (P = 0,763) [PR] ([Hunter et al. 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9385988/)).

Con modelos automáticos en gestos rápidos, el panorama empeora:
- En un pase largo de fútbol filmado con dos iPhone a 60 Hz, MediaPipe heavy, DWPose y YOLO-Pose dieron **RMSE de 9,9 a 39,9°** según la articulación, por oclusión y saltos de los puntos [PR] ([PMC13306328](https://pmc.ncbi.nlm.nih.gov/articles/PMC13306328/)).
- Incluso con 9 cámaras, OpenPose y AlphaPose erraron los centros articulares por 14–48 mm, con un sesgo de 30–50 mm en cadera y rodilla y **cambios de miembro izquierdo/derecho** [PR] ([Needham et al. 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8526586/)).
- El 3D desde una sola cámara tiene 36–58 mm de error por articulación en benchmarks de movimientos cotidianos (WHAM: 57,8 mm sin alinear en 3DPW) [CONF] ([WHAM](https://arxiv.org/html/2312.07531v2)).
- Con dos o más cámaras calibradas se llega a 3–5° (OpenCap 4,5°; Pose2Sim 3,0–4,1°), pero solo validado en marcha, sentadilla, carrera y bicicleta [PR] ([OpenCap](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011462); [Pose2Sim](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9002957/)).

La tabla siguiente traduce esa evidencia en márgenes para el informe del cliente. Son inferencias [INF] que todavía no se validaron con el pipeline propio contra una referencia.

| Medida | Condición | Margen honesto |
|---|---|---|
| Inclinación del tronco, flexión de rodilla, ángulo de la varilla | Cámara perpendicular a la altura de las manos, ≥60 fps, obturador rápido, en P1, P2, P4 y P10 | ±3–5° |
| Lo mismo entre P5 y P8 | 30–60 fps con estela | ±5–10°, o "no evaluado" si el punto tiene baja confianza |
| Giro de pelvis y tórax, X-factor | Una cámara | No se informa en números |
| Giro de pelvis y tórax | Dos celulares sincronizados y calibrados | ±5–10° |
| Sway y subida de pelvis y cabeza | De frente, escala en el plano del jugador | ±1–3 cm |
| Manos o varilla respecto del plano | Desde atrás, cámara verificada | ±2–4 cm; dar rangos |
| Momento del impacto o del tope | Detección automática o manual | ±1 cuadro (±33 ms a 30 fps, ±17 ms a 60, ±4 ms a 240) |
| Ritmo de subida y bajada | Solo con video a velocidad real | ±1 cuadro en cada borde |

En los eventos, el modelo SwingNet de GolfDB acierta el impacto el **98,4 %** de las veces y el tope el 83,9 %, con una tolerancia de ~1 cuadro a 30 fps. El address (31,7 %) y el final (26,5 %) conviene fijarlos con reglas [CONF] ([McNally et al. 2019](https://arxiv.org/abs/1903.06528)). Para un producto pago, las licencias pesan tanto como la precisión.

| Función | Recomendación | Licencia | Evidencia |
|---|---|---|---|
| Cuerpo 2D | RTMPose-m o RTMPose-l con rtmlib (ONNX, en CPU) | Apache-2.0 | 75,8 AP en COCO; ~11 ms por persona en CPU [FAB] ([RTMPose](https://github.com/open-mmlab/mmpose/tree/main/projects/rtmpose)) |
| Control cruzado | MediaPipe Pose heavy, que ya usa el proyecto | Apache-2.0 en el código; los pesos no se verificaron | Sin ventaja demostrada en deporte rápido [PR]. Comparar dos modelos detecta cambios de lado |
| Ajuste a golf | GolfPose (cuerpo + 5 puntos del palo) | La EULA permite comercializar modelos entrenados, no redistribuir el dataset | AP de golfista 0,887; golfista + palo hasta 0,942 [CONF] ([GolfPose](https://github.com/MingHanLee/GolfPose)) |
| Palo | Detector o puntos propios (RTMDet/RTMPose) entrenados con golf-club-tracking de Roboflow | Apache-2.0 + CC BY 4.0, con atribución | swingtrace (AGPL) solo para prototipar: cabeza del palo en 71,6 % de los cuadros, cabeza o varilla en 93,4 % [autodeclarado] ([swingtrace](https://github.com/nishsm/swingtrace)). La varilla es más robusta que la cabeza cerca del impacto |
| Eventos | SwingNet reimplementado y reentrenado, más reglas para el address y el final | El código original es CC BY-NC | Ver arriba ([golfdb](https://github.com/wmcnally/golfdb)) |
| 3D con dos celulares | Pose2Sim | BSD-3 | Ver arriba |
| Evitar | OpenPose y AlphaPose (no comerciales); VideoPose3D y Sapiens (CC BY-NC); WHAM y HMR2 sin licencia de SMPL ([SMPL](https://smpl.is.tue.mpg.de/modellicense.html)); YOLO de Ultralytics (AGPL) | — | — |

## Los profesores trabajan hacia atrás y cambian una sola cosa

El orden de diagnóstico que se enseña a los profesores es "vuelo de la pelota → factores de impacto → principios del swing". Empezar por el swing puede empeorar el vuelo (resumen de búsqueda, página no abierta) [NV] ([Golf Insider](https://golf-insider.beehiiv.com/p/how-pga-coaches-are-taught-to-teach)). Ryan Smith, instructor principal de la Marc Lapointe Golf Academy, lo formula en la publicación de la PGA de las Carolinas [INS] ([Carolinas PGA](https://carolinas.pga.com/news/a-practical-application-of-swing-mechanics-for-teaching-and-coaching/)). Cada clase tiene **un objetivo principal**: cambiar el vuelo a través de una de seis leyes, que son el centro del golpe, el ángulo de la cara, el path, la velocidad, el ángulo de ataque y el loft dinámico. Un método que no cambia al menos una de ellas en la clase puede estar cambiando solo la estética del swing. TrackMan insiste en que el path y el ángulo de ataque son resultados, no las entradas que el jugador controla, así que la clase tiene que atacar la causa [FAB] ([TrackMan](https://www.trackman.com/blog/trackman-talks-the-true-impact-factors)). Stickney muestra un caso en que el path demasiado de adentro hacia afuera era el efecto y un pivote defectuoso, la causa [INS] ([GolfWRX](https://golfwrx.com/237099/stickney-fix-the-real-cause-of-the-problem-with-a-launch-monitor/)). TPI suma el eslabón físico: para el over the top recomienda empezar por la movilidad de cadera y columna y recién después pasar a los drills de traslado de peso [TPI] ([TPI](https://cdn.site.mytpi.com/improve-my-game/swing-characteristics/over-the-top)).

Llevado al informe, la secuencia es:
1. Qué hace la pelota.
2. Qué tuvo que pasar en el impacto.
3. Qué cuadro del video lo explica.
4. Qué limitación física podría estar detrás, como hipótesis para un screen.
5. Una sola prioridad, con su drill, su progresión y un objetivo medible para el próximo video.

Revisar el setup (grip, posición de la pelota, postura, alineación) antes que el swing es práctica común. Smith lo trata como una palanca más, pero no se encontró como principio citado.

Los drills mejor documentados tienen pasos claros y una señal física que avisa el error:
- **Early extension:** los glúteos contra una pared o una silla, que "usan los Top 100 de GOLF.com" ([GOLF.com](https://golf.com/instruction/use-easy-drill-prevent-early-extension-in-your-swing/)), y la silla adelante de Chris Como, con progresión ([GOLF.com](https://golf.com/instruction/chair-drill-cure-early-extension-chris-como)).
- **Over the top:** llevar las manos hacia el bolsillo de atrás o "volcar" una botella de agua detrás del cuerpo en la transición ([HackMotion](https://hackmotion.com/drills-to-stop-coming-over-the-top/)).
- **Casting:** "pegá fuerte, frená rápido" y el "cuerpo primero" con una silla de obstáculo ([HackMotion](https://hackmotion.com/drills-to-stop-casting/)).

La progresión es la misma en todas las fuentes: ensayo sin pelota y lento, pausas en los puntos de control (tope y P6), medio swing de cintura a cintura, swing completo, pelota y, al final, velocidad. Se avanza solo cuando la señal (el contacto, el objeto que se cae, el vuelo) sigue bien.

TPI nombra drills y ejercicios para cada característica, como Step Change, Get Closer, Picket Fence o Brettzel, pero los muestra solo en video. Sus pasos no deben describirse de memoria. Tampoco se verificaron en esta investigación drills populares como el pump drill, los pies juntos, el step-through o el headcover por fuera de la pelota: no se atribuyen sin fuente.

Dos límites de la práctica profesional cierran el método. TPI y los entrenadores vinculados reconocen que algunas limitaciones físicas no se corrigen del todo, y entonces el plan se adapta a ellas en lugar de forzar el modelo [INS] ([The Dan Plan](https://thedanplan.com/a-month-of-working-with-bruce-furman-and-some-titleist-tpi-thoughts/)). Además, si hay dolor, se deriva a un profesional de la salud y no se dan ejercicios para eso.

En el idioma, no apareció ningún glosario autorizado argentino ni español. Lo seguro es usar el término castellano donde existe (plano, impacto, postura, cara, trayectoria) y el préstamo inglés donde ya se usa, con el término de TPI entre paréntesis la primera vez [INS] ([Wlingua](https://learn.spanish.wlingua.com/golf-vocabulary-in-spanish/)). Traducir over the top como "por arriba" es riesgoso: en la jerga local podría entenderse como pegarle arriba a la pelota [NV].

## Herramientas listas para aplicar

### (a) Protocolo de filmación y calibración

| Paso | Desde atrás (DTL) | De frente (face-on) | Por qué |
|---|---|---|---|
| Preparación | Poné dos varillas (o dos palos) en el piso, paralelas a la línea del objetivo: una justo delante de las puntas de los pies y otra sobre la línea pelota–objetivo. Medí con cinta el largo de cada una y la separación, y anotalo | Agregá una tercera varilla perpendicular a la línea del objetivo, en el medio de la postura | Dan el control de alineación (punto de fuga), la escala de frente y la homografía del piso [CP]. La perpendicular ubica la cámara de frente [INS] ([The Sand Trap](https://thesandtrap.com/b/playing_tips/filming_your_swing)) |
| Ubicación | En la prolongación de la línea de las manos del address, entre la varilla de las puntas y la de la pelota, más cerca de la de las puntas. Nunca detrás de la pelota | Sobre la línea de la varilla perpendicular, mirando en ángulo recto a la línea del objetivo y centrada en el medio de la postura | V1 y Titleist alinean con las manos; The Sand Trap prefiere las puntas. Es la única posición cómoda dentro del plano de la varilla [CP] |
| Altura | Lente a la altura de las manos en el address. Si se filma desde la línea de las puntas, subirlo a ~1,05–1,10 m | Altura de las manos o la cadera, con el golfista un poco por debajo del centro del cuadro | Más alta aplana el plano, más baja lo empina (4–16 cm a 3 m) [CP] |
| Distancia y lente | 3–3,7 m de las manos con 1x; más lejos con 2x si hay luz. Nunca 0,5x | 3–3,7 m de la pelota, con 1x | Más lejos hay menos paralaje (−25 % a 3,7 m) [CP]. Sportsbox pide ≤3,7 m con 1x ([Sportsbox](https://help.sportsbox.ai/how-do-i-set-up-my-camera-to-record-a-session)) |
| Nivel y encuadre | Celular nivelado (app o nivel de burbuja), sin inclinar ni girar. Vertical. Cuerpo entero, palo en el tope y final dentro del cuadro | Igual | Inclinar el celular 10° suma ~1,3° a la columna y tuerce las verticales ~1,3° [CP] |
| Cuadros y luz | Cámara lenta a 240 fps (120 si falta luz), de día o con mucha luz | Igual | 200–300 fps y obturador de ≥1/1000 s [INS]. A 240 fps el palo avanza 13–21 cm por cuadro [CP] |
| Tomas | 3 swings sin mover el trípode; hierro 7 y driver por separado | Igual | Un ángulo constante y la consistencia entre swings son datos en sí mismos ([The Sand Trap, foro](https://thesandtrap.com/forums/topic/104476-camera-angles-matter/)) |
| Dos celulares (opcional) | El mismo swing, filmado a la vez desde las dos vistas | Igual | Sincronizar por el cuadro de impacto (±1 cuadro, ±4 ms a 240 fps); el sonido desfasa 2,9 ms por metro [CP] |
| Envío | Original con la velocidad en "100 % – 240 FPS" (Fotos → Editar), por AirDrop, USB o Drive como archivo original | Igual | Exportar desde Fotos de la Mac deja 30 fps; AirDrop o "Editar con QuickTime" conservan 240 [INS] ([Stolovitz](https://ben.stolovitz.com/posts/export-slo-mo-videos-from-your-iPhone/)). No se encontró una fuente sobre cuánto recomprime WhatsApp |
| Control al recibir | Con ffprobe: ~238–240 fps y duración real. Usar el tiempo de cada cuadro. Si el archivo dice 30 fps o dura 8 veces más, pedir el original | Igual | La frecuencia es variable ([Stolovitz](https://ben.stolovitz.com/posts/export-slo-mo-videos-from-your-iPhone/)) |
| Calibración | Punto de fuga de las dos varillas cerca del centro; desvío θ = atan(d/f) (con f ≈ 1.400 px, 5° corren el punto ~120 px). Escala con el palo del address o con una varilla vertical en la línea de las manos | Escala con la varilla de las puntas, nunca con el palo del address. Homografía del piso con los extremos de las varillas | [CP]; referencia en el mismo plano [PR] ([Brewin y Kerwin](https://www.semanticscholar.org/paper/Accuracy-of-scaling-and-DLT-reconstruction-for-Brewin-Kerwin/6442d8afe29b2187fa1fa33de610639dad4b3f8a)) |
| Datos a pedir | Diestro o zurdo; palo; a dónde apuntaba; dónde salió la pelota y cuánto curvó; si fue más alta o más baja de lo normal; contacto (foto de la marca con spray o cinta de impacto, y del divot); si falla para un lado o para los dos; distancia; condiciones (viento, pendiente, alfombra); datos de launch monitor si tiene; dolor o lesión; permiso para publicar | | Las leyes de vuelo necesitan la salida, la curva y el centro del golpe ([PING](https://mdpi-res.com/proceedings/proceedings-02-00249/article_deploy/proceedings-02-00249.pdf); [TrackMan](https://trackman.com/blog/golf/face-to-path)) |

### (b) Checklist de medición P1–P10

**Definiciones usadas.** Son las de HackMotion, que coinciden con la mayoría de las fuentes [FAB] ([HackMotion](https://hackmotion.com/golf-swing-positions/)):
- P1: address;
- P2: varilla paralela al piso en la subida;
- P3: brazo líder paralelo en la subida;
- P4: tope;
- P5: brazo líder paralelo en la bajada;
- P6: varilla paralela en la bajada;
- P7: impacto;
- P8: varilla paralela después del impacto;
- P9: brazo líder paralelo en el follow-through;
- P10: final.

V1 llama P6 al impacto, y un autor de Keiser University llama P6 al brazo líder paralelo ([Keiser](https://collegeofgolf.keiseruniversity.edu/p6-the-gateway-to-your-best-ball-striking)). El informe tiene que traer esta lista. Los márgenes de la tabla son inferencias [INF] que todavía no se validaron con el pipeline propio.

| Posición | Vista | Medida | Criterio y referencia | Margen honesto |
|---|---|---|---|---|
| P1 | Atrás | Ángulo de la varilla (línea A) | Línea base del plano; sin norma absoluta | ±1–3° (se conserva con 5° de giro de cámara [CP]; [Hunter 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9385988/)) |
| P1 | Atrás | Inclinación del tronco y flexión de rodillas | Línea base para P4–P7. Los ~30° de Sportsbox no son comparables con un ángulo 2D | ±3–5° con el celular nivelado |
| P1 | Atrás | Línea vertical tangente a la nalga de atrás y distancia manos–cuerpo | Referencia para la early extension | ±1–3 cm, con el palo del address como escala |
| P1 | Atrás | Curvatura lumbar y torácica | S-posture (arco lumbar excesivo) y C-posture (espalda redondeada) según TPI | Cualitativo |
| P1 | Frente | Posición de la pelota, ancho de postura, alineación | Con homografía del piso. Referencia: ancho/altura del cuerpo de 30 % con driver y 26–27 % con hierros en 5 profesionales mujeres [CONF] ([Nozawa 2012](https://ojs.ub.uni-konstanz.de/cpa/article/view/5236)) | ±1–2 cm [CP]. Sin homografía, la pelota del driver se ve ~5 cm corrida |
| P1 | Frente | Inclinación lateral del tronco | Línea base; Sportsbox: ~15° alejándose del objetivo [FAB] | ±3–5° |
| P2 | Atrás | Cabeza del palo respecto de las manos | Apenas por fuera de las manos, con la varilla paralela a la línea del objetivo. "Enrollado adentro": la cabeza detrás de las manos y la punta mirando hacia atrás [INS] ([Golf Chicago](https://www.golfchicagomagazine.com/publications/gc_jul_25/GC%202025-4%20instruction.pdf)) | Cualitativo; ángulo ±3–5° |
| P2–P4 | Frente | Pelvis lateral (sway) | Que no termine alejada del objetivo en P4; cadera de atrás por fuera del pie de atrás = sway [FAB/TPI] | ±1–3 cm con escala en la línea de las puntas; sin ella se subestima ~20 % [CP] |
| P3 | Atrás | Línea B del slot | Varilla con el antebrazo líder apenas pasado la horizontal [TPI] | ±3–5° |
| P4 | Atrás | Plano de hombros | Hombro líder por encima de la paralela a la línea cóccix–nuca = flat shoulder plane [TPI] | ±3–5° |
| P4 | Atrás | Dirección de la varilla y codo de atrás | Cruzado, laid off y codo volador se describen; no son fallas por sí solos [TPI/INS] | Cualitativo |
| P4 | Atrás | Cambio de inclinación del tronco y de flexión de la rodilla de atrás respecto de P1 | Pérdida de postura si cambia "significativamente" (TPI no da umbral) | ±3–5° |
| P4 | Atrás | Nalga respecto de su línea del address | Si avanza hacia la pelota en la subida, entra en la definición del artículo de TPI | ±1–3 cm |
| P4 | Frente | Cabeza lateral | Hándicap bajo: 5,5 cm; hándicap medio: 12,4 cm (n = 8) [CONF] | ±1–3 cm |
| P4 | Frente | Tronco inclinado hacia el objetivo | Reverse spine angle [TPI] | ±3–5° |
| P4 | Frente | Inclinación de hombros | Profesionales 36° contra 29,6° en hándicaps altos [FAB] | ±3–5° |
| P4 | — | Giro de pelvis y tórax, X-factor, muñeca | Tour: 90–106°, 33–50° y 55–69°. No se miden con una cámara | No se informa número |
| P1→P4 | Video a velocidad real | Tiempo de subida | 0,7–0,8 s en profesionales con hierro 5 [CONF] | ±1 cuadro |
| P5 | Atrás | Prueba del slot y bajada contra subida (over the top) | Ver el protocolo de over the top: manos y varilla en P5 contra P3 | Manos ±2–4 cm; varilla ±3–5° a 240 fps, ±5–10° a 60 fps |
| P5 | Frente | Cabeza o esternón contra pelvis | Si el tren superior se mueve más que la pelvis entre P4 y P6: forward lunge [TPI] | ±1–3 cm |
| P5 | Frente | Caída de la pelvis | 2,5–8,4 cm es normal [FAB] | ±1–3 cm |
| P6 | Atrás | Varilla respecto del antebrazo de atrás; cabeza del palo respecto de las manos | Varilla por encima del antebrazo = empinada [INS]; cabeza por fuera de las manos = over the top [FAB] | Cualitativo; ±5–10° |
| P6 | Atrás | Nalga respecto de su línea; distancia cadera–pelota contra P1 | Early extension si avanza hacia la pelota; se gradúa en cm | ±1–3 cm |
| P6 | Atrás o frente | Ángulo entre el brazo líder y la varilla | Si se pierde temprano: casting [TPI]. Sin norma numérica | Cualitativo |
| P7 | Atrás | Nalga respecto de su línea; inclinación del tronco contra P1 | En el tour, el tronco vuelve a ~su inclinación del address [FAB]. Subir la pelvis no es falla | ±1–3 cm; ±5–10° |
| P7 | Frente | Pelvis lateral respecto del address | Hierros 8,1–14,0 cm y driver 6,1–10,4 cm (rango intercuartil de GEARS); ~10 cm según TPI. ≤0 con hierros = hanging back | ±1–3 cm |
| P7 | Frente | Tórax lateral y brecha pelvis–tórax | Hierros 3,8–7,9 cm; driver −2,3 a 2,3 cm; la pelvis por delante del tórax [FAB] | ±1–3 cm |
| P7 | Frente | Inclinación del eje pelvis–hombros | Hierros 101–107°, driver 104–111° (90° = vertical) [FAB] | ±3–5°, solo con el cuadro de impacto real |
| P7 | Frente | Inclinación de la varilla | Hierros: hacia el objetivo [TPI/INS]; driver: neutra. Se informa presente, ausente o hacia atrás | ±3–5° a 240 fps con cámara perpendicular; si no, "no evaluado" |
| P7 | Frente | Cabeza respecto del address | Sin norma (n = 8) | ±1–3 cm |
| P7 | Frente | Rodilla líder | En el tour se estira y la pelvis sube 3,6–10,9 cm [FAB]: no es falla | ±5–10° |
| P4→P7 | Video a velocidad real | Tiempo de bajada y ratio | ~0,23–0,29 s del tope al impacto ([arXiv](https://arxiv.org/html/2606.22876)); ratio de 2,5–3,5 en profesionales, pero no distingue niveles [CONF] | ±1 cuadro por borde |
| P7 | Cualquiera | Cuadro de impacto | Último cuadro antes de que se mueva la pelota | El palo cerca del impacto, ±8–10 cm a 240 fps [CP] |
| P7–P8 | Frente | Scooping | Cabeza del palo que pasa a las manos, con la varilla inclinada hacia atrás [TPI] | Cualitativo |
| P8 | Frente (y atrás) | Codo líder | Flexionado, apuntando abajo o abriéndose = chicken winging [TPI/FAB] | Cualitativo; ±5–10° |
| P7–P8 | Ambas | Rodillas después del impacto | Caída o flexión brusca = late buckle; levantarse es normal [TPI] | Cualitativo |
| P9–P10 | Ambas | Final y equilibrio | Pararse derecho es normal. La varilla en el final es poco confiable (error típico de 19–20° [PR]) | Cualitativo |

### (c) Tabla de decisión por falla

Progresión común a todos los drills [FAB/INS/TPI]: movilidad o ensayo sin palo ni pelota → cámara lenta con pausas en el tope y en P6 → medio swing de cintura a cintura → swing completo → pelota → velocidad. Se avanza solo si la señal del drill sigue bien. TPI nombra sus drills sin pasos escritos: se citan por el nombre, no se describen.

| Falla (TPI) | Criterio en video | Consecuencia en el vuelo o el contacto | Causa física · técnica | Drill y progresión |
|---|---|---|---|---|
| **Over the top** | Atrás, P3→P5/P6: palo por encima o por fuera del slot (líneas A y B), o manos en la bajada por encima de su camino de subida por más que el margen. Al menos una pista o el vuelo tienen que coincidir | Path de afuera hacia adentro: pull con la cara igual al path; pull-slice o slice con la cara abierta; con hierros, ataque más empinado [TPI] | Física: movilidad de cadera, core y glúteos, separación entre el tren inferior y el superior [TPI]. Técnica: el tren superior inicia la bajada. Gulgin no halló asociación con el screen [PR] | Manos al bolsillo de atrás o botella de agua: 10–15 repeticiones sin pelota y después tiros con la misma sensación [FAB] ([HackMotion](https://hackmotion.com/drills-to-stop-coming-over-the-top/)). TPI: Step Change, Side Arm Throw, Barriers; ejercicios Brettzel, Stork Turns Supported, Starfish Pattern 1 |
| **Early extension** | Atrás, P1 contra P4–P7: la nalga se despega de su línea del address hacia la pelota y se achica la distancia cadera–pelota. Que la pelvis suba y vaya hacia atrás no cuenta | Block a la derecha y hook a la izquierda (falla para los dos lados), palo atascado; golpes pesados y finitos en el juego corto; shank [TPI] | Sentadilla profunda o flexión de cadera limitada, rotación sobre la cadera líder, separación, glúteos y abdominales [TPI]. No tocarse la punta de los pies (p = 0,015) y el puente derecho (p = 0,050) [PR] | Glúteos contra pared o silla en swings lentos: si se abre un hueco, hay early extension [INS]. Silla adelante (Como): rodillas a 10–13 cm del asiento → en la bajada se acercan → en el impacto se alejan → final con las piernas casi juntas [INS] ([GOLF.com](https://golf.com/instruction/chair-drill-cure-early-extension-chris-como)). TPI: Get Closer, Picket Fence; ejercicios Search and Destroy with Calf Stretch, Disassociation Planks, Half-Kneeling Bounce Pass |
| **Pérdida de postura** (loss of posture) | Atrás, P1 contra P4–P7: cambio de inclinación del tronco o de flexión de rodillas antes del impacto | Block y hook [TPI] | Las mismas que la early extension, más caderas y hombros (tests 90/90, Lat y Lower Quarter Rotation) [TPI]. Puente derecho (p = 0,028) [PR] | TPI: Sweep the Dust, Loss of Posture Drill; ejercicios Two Arm Cross Body Lat Stretch, Windmills, Lunge Stance One Arm Incline Row |
| **Plano de hombros plano** (flat shoulder plane) | Atrás, P4: hombro líder por encima de la paralela a la línea cóccix–nuca | Compensaciones en la bajada, pérdida de potencia, golpe inconsistente [TPI] | Rotación torácica, dorsales, pelvic tilt, core, caderas [TPI] | Autocontrol de Titleist: palo cruzado sobre los hombros; si en el tope apunta al horizonte, el plano es demasiado plano ([Titleist](https://titleist.ca/videos/instruction/flat-shoulder-plane)) |
| **Codo volador** (flying elbow) | Atrás, P4: el codo de atrás apunta detrás del jugador | No es necesariamente una falla; solo si después aparece over the top [TPI] | Rotación externa del hombro de atrás, columna torácica, estabilidad escapular [TPI] | Headcover bajo la axila de atrás (si se levantan los brazos, se cae) [INS, resumen de búsqueda] |
| **Sway** | Frente, P1 contra P2–P4: la cadera de atrás pasa la vertical del borde externo del pie de atrás y el centro de la pelvis queda alejado del objetivo en P4 | TPI no indica vuelo. Inferencia: punto bajo atrás (pesado o finito) si no se recupera [INF] | Rotación interna de la cadera de atrás, separación, glúteo medio [TPI] | Varilla clavada por fuera del pie de atrás: la cadera no debe tocarla [INS, resumen de búsqueda]. TPI: Hip Drops, Helicopter Turns, Horizontal Chops, Change of Direction |
| **Slide** | Frente, P4 contra P6–P7: la cadera líder pasa claramente su vertical, con poca rotación. El traslado solo no alcanza | TPI: pérdida de potencia. Push o punto bajo adelante: inferencia sin fuente | Rotación interna de la cadera líder, separación, glúteo medio de la pierna líder [TPI] | No se verificó un drill con pasos |
| **Late buckle** | Ambas vistas, P7–P8: caída y flexión brusca de rodillas después del impacto | TPI no indica vuelo | "Casi siempre" física: cadera líder, core, zona lumbar, tobillos [TPI] | Derivar a una evaluación física; no hay drill técnico |
| **Ángulo de columna invertido** (reverse spine angle) | Frente, P4: tronco inclinado hacia el objetivo (desde atrás: echado hacia atrás) | Una de las principales causas de dolor lumbar [TPI] | Separación, rotación interna de la cadera de atrás (el sway fuerza la inclinación), core, S-posture [TPI] | Derivar a una evaluación física; si hay sway, trabajar primero el sway |
| **Forward lunge** | Frente, P4→P6: la cabeza o el esternón se mueven hacia el objetivo más que la pelvis | Ataque muy empinado; tiros altos con mucho spin [TPI] | Movilidad de cadera y tobillo, glúteos y core, potencia del tren inferior [TPI] | No se verificó un drill con pasos |
| **Hanging back** | Frente, P1 contra P7: la pelvis no queda por delante del address (≤0 cm) y el peso sigue atrás | Golpes pesados que empiezan detrás de la pelota; pelota compensada atrás; pérdida de velocidad [TPI] | No poder apoyarse en la pierna líder (cadera, tobillo, core), reverse pivot, poca potencia [TPI] | TPI: Step Change; ejercicio Change of Direction. Arrancar la bajada con el traslado y el empuje de cadera [FAB] |
| **Casting** | P5–P6: pérdida temprana del ángulo entre brazo y varilla. En P7, sin inclinación de la varilla hacia el objetivo con hierros | Pérdida de potencia, spin excesivo, más loft [TPI]. Punto bajo atrás [INF] | Poco aporte del tren inferior; falta de extensión de la muñeca de atrás [TPI] | "Pegá fuerte, frená rápido" → "cuerpo primero" con silla y palo al revés (pausa en L, después con pelota) → de cintura a cintura → swing completo controlando la inclinación de la varilla [FAB] ([HackMotion](https://hackmotion.com/drills-to-stop-casting/)) |
| **Scooping** | Frente, P7: la cabeza del palo pasa a las manos con la varilla inclinada hacia atrás | Más loft; tiros altos y cortos [TPI/INF] | Potencia del tren inferior; flexión de la muñeca líder y extensión de la de atrás [TPI] | Motorcycle (flexionar la muñeca líder) [FAB, resumen de búsqueda]; los mismos drills del casting |
| **Chicken winging** | Frente, P7–P8: el codo líder se flexiona y apunta abajo o se abre | Pérdida de potencia, más loft y spin [TPI] | Potencia del tren inferior; bajada empinada u over the top; rotación externa del hombro líder [TPI] | Toalla bajo las dos axilas en medios swings: si se cae, los brazos se separaron del torso [INS, resumen de búsqueda] |
| **S-posture** | Atrás, P1: arco lumbar excesivo | Pérdida de postura y reverse spine angle; predictor de dolor lumbar [TPI] ([Titleist](https://www.titleist.com/instruction/three-postures-in-golf)) | Síndrome cruzado inferior, abdominales débiles, demasiada flexión de rodillas [TPI] | No se verificó un drill; corregir el setup y evaluar con el screen |
| **C-posture** | Atrás, P1: hombros caídos y columna torácica redondeada | Según TPI de segunda mano, se asocia a early extension y a plano de hombros plano | Extensión torácica limitada, síndrome cruzado superior, palos cortos, grip muy en los dedos [TPI] | No se verificó un drill; revisar el largo de los palos y el grip |

### (d) Errores conceptuales que delatan un análisis amateur

| Error | Por qué lo detecta un profesional | Qué hacer |
|---|---|---|
| "La pelota sale hacia donde va el path" | Es la ley vieja; la cara explica el 61–76 % de la salida según el único estudio publicado [PR], y hasta 85 % según la cifra de enseñanza de TrackMan [FAB] ([PING](https://mdpi-res.com/proceedings/proceedings-02-00249/article_deploy/proceedings-02-00249.pdf); [The Sand Trap](https://thesandtrap.com/b/playing_tips/ball_flight_laws)) | "La cara manda la salida; la diferencia cara–path, la curva" |
| Dar "75 %" como dato exacto | Es una cifra de enseñanza; el único estudio con condiciones publicadas da 61–76 % | "Entre dos tercios y más de tres cuartos" |
| Llamar over the top a todo slice | El slice depende de la cara respecto del path; con driver, un golpe de talón lo imita [TPI/FAB] | Exigir el criterio de video, el vuelo y la marca del impacto |
| Decir "en plano" sin probarlo | Fue el error del swing 2 | Las dos pruebas dentro del margen; si no, "no evaluable" |
| Juzgar el plano sin controlar la cámara | La altura y la ubicación corren el plano 4–16 cm [CP/INS] | Punto de fuga y comparación bajada contra subida |
| Llamar early extension a la pelvis que sube o a la rodilla líder que se estira | Es un patrón de tour [FAB] | Early extension = pelvis hacia la pelota respecto de su línea del address |
| Marcar como falla la cadera abierta en el impacto | En el tour, la pelvis está más abierta que el tórax [PR/FAB] | Describirlo como correcto |
| Marcar como falla el codo volador, el palo cruzado, el laid off o la muñeca extendida en el tope | TPI y los datos de jugadores hábiles lo desmienten | Describirlo; es falla solo si la bajada lo paga |
| "Pierde la postura" al levantarse después del impacto | TPI lo considera normal | Pérdida de postura solo entre P4 y P7 |
| Confundir sway, slide, late buckle y hanging back, o casting, scooping y flip | TPI los separa por fase y dirección | Usar la tabla (c) |
| P-números sin definir | V1 y Keiser usan otra numeración | Incluir la lista de definiciones |
| Informar giro, X-factor, °/s, muñeca, cara o path en grados con un celular | No se miden en 2D; incluso los sensores inerciales tienen ±10–20° [PR] | "No se mide con este video", o inferirlo del vuelo |
| Comparar con referencias de otro sistema | El X-factor va de −72° a −124° según el método [PR] | Comparar contra el address propio |
| Decimales de laboratorio sin margen | Falsa precisión | "≈37° (±5°)" |
| Presentar los porcentajes de TPI como estudios | Son datos propios o de segunda mano | "Según TPI" |
| Medir el ritmo con la cámara lenta "horneada" o usar el 3:1 como marca de nivel | Los amateurs también promedian ~3:1 [CONF] | Ritmo solo con video a velocidad real; medir la consistencia |
| "Pegale hacia abajo" para todo | El driver de tour va de −0,9° a +2,8° [FAB] | Recomendaciones según el palo |
| "La cabeza tiene que quedar quieta" | Los jugadores hábiles la mueven ~5 cm [CONF] | Medirla contra el address y relacionarla con el contacto |
| Hombros "nivelados" como objetivo | Los profesionales los inclinan más [FAB] | Usar el criterio de flat shoulder plane de TPI |
| Ocho fallas sin prioridad, o atacar el efecto | Los profesores tienen un objetivo por clase y atacan la causa [INS/FAB] | Una prioridad, con su cadena de causa y efecto |
| Ignorar la causa física o el dolor | TPI vincula casi todas las características con limitaciones físicas | Sugerir un screen; si hay dolor, derivar a un profesional de la salud |
| Traducir over the top como "por arriba" | En la jerga local podría entenderse como pegarle arriba a la pelota [NV] | "Over the top (bajada por afuera, de afuera hacia adentro)" |

## Conclusión

La ventaja posible de este producto sobre un instructor no está en ver mejor, sino en medir de forma reproducible dentro del mismo jugador. Casi no existen normas de tour en centímetros validadas, y las que hay se contradicen entre fabricantes. Por eso la referencia más defendible es el address del propio golfista y sus propios videos antes y después del cambio. Además, la consistencia entre los tres swings de cada toma es una dimensión que el ojo no puede cuantificar y que se relaciona con el score (r = 0,801 en la inclinación del tronco). Si el informe muestra cuánto varía cada medida entre swings, ya hace algo que un profesor sin herramientas no hace.

El riesgo principal es conceptual, no de medición. Un over the top de 14–23 cm queda muy por encima de cualquier margen; se dijo "en plano" porque faltaba una regla. Las reglas asimétricas ("en plano" exige pruebas, la duda es "no evaluable") cierran esa brecha, junto con el control de cámara por punto de fuga y el vuelo de la pelota como segunda fuente. Para que los márgenes publicados pasen de "estimados" a "medidos", el próximo paso es validar el pipeline propio contra una referencia: dos celulares calibrados con Pose2Sim, un sensor inercial o digitalización manual a 240 fps. Mientras tanto, conviene corregir tres puntos de la guía actual: la cámara de atrás va a la línea de las manos y no a la de las puntas a la altura de las manos; el "75 %/85 %" se reemplaza por un rango; y el cuestionario de vuelo y contacto se vuelve obligatorio antes de diagnosticar.
