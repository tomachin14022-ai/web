# Cámara y calibración: cómo filmar el swing con el celular para medir planos, ángulos y distancias reales

> Notas de investigación (04/11/2026). Se separa siempre **recomendación de instructores/apps** (opinión de práctica) de **datos de error medidos** (estudios) y de **cálculos propios** (modelo de cámara estenopeica hecho para estas notas; marcados "CÁLCULO PROPIO", con los supuestos a la vista). Los cálculos propios no son datos publicados: sirven para dimensionar el error, no para citarlos como estudio.
>
> Supuestos del modelo geométrico propio (script en `/tmp/claude-0/-home-user-web/8c9ff960-462f-556a-8a54-ec679615e80e/scratchpad/calc/geom.py`): hierro medio; manos en el address a 0,75 m de altura y 20 cm por delante de la línea de las puntas de los pies; pelota a 65 cm de esa línea; varilla en el address a 58,3° del piso; cámara estenopeica sin distorsión. Ejes: x hacia el objetivo, y de los pies hacia la pelota, z arriba.

---

## 1. Down-the-line (desde atrás): ¿en la línea de las manos, de las puntas de los pies, del objetivo o de la pelota?

### Takeaway
La mayoría de las fuentes de enseñanza pone la cámara **en la línea de las manos, a la altura de las manos, nivelada y apuntando paralela a la línea del objetivo** (V1, Titleist, GolfWRX, Leadbetter); The Sand Trap prefiere la **línea de las puntas de los pies** y todos rechazan **detrás de la pelota** para juzgar el swing completo (sí sirve solo para ver el path en el impacto). La geometría explica el porqué: la línea de las manos a la altura de las manos es el único punto "cómodo" que queda **dentro del plano de la varilla del address**, así que ese plano se ve de canto (como una línea) y "en plano / arriba / abajo" se puede juzgar; fuera de ese plano, posiciones que están en plano aparecen desplazadas 4–16 cm (CÁLCULO PROPIO a 3 m).

### Cited Findings
**Recomendaciones (práctica, no medición):**
- The Sand Trap (Erik J. Barzeski, "Recording Your Golf Swing", 11/04/2021, act. 24/08/2024): DTL a la "altura de las manos" (cerca de la cadera o un poco debajo del ombligo); **posición preferida: paralela a la línea del objetivo, sobre el dedo gordo del pie de atrás (línea de las puntas)**; "aceptable pero no ideal": a mitad de camino entre la pelota y las puntas; **no recomendada: directamente detrás de la pelota**, que "will distort almost every phase of the golf swing"; sobre la línea del objetivo "puts the golfer completely to the side of the video" y da un mal ángulo por paralaje. Truco: una varilla de alineación justo delante de las puntas, paralela a la línea del objetivo, y la cámara "just inside that line". Distancia **8 a 12 pies (2,4–3,7 m) de la pelota**; más cerca, el arco del palo pasa cerca del lente y distorsiona. Postura un poco abierta o cerrada no importa. — [The Sand Trap](https://thesandtrap.com/b/playing_tips/filming_your_swing)
- The Sand Trap, foro (iacas = Erik Barzeski, 03/06/2020, "Camera Angles Matter"): cambios chicos del ángulo hacen que el mismo swing se vea muy distinto: cambian la posición de la cabeza del palo en A6, la profundidad del brazo izquierdo, la acción de las rodillas y la alineación de cadera, rodillas y hombros. "Be picky about your angles, or you can waste a lot of time trying to fix something that isn't even an issue." Para el path **en la pelota** (como TrackMan) la cámara va "behind the ball directly"; para todo lo demás, "stick with one camera angle for consistency, and know how certain things look from that angle"; un usuario propone "detrás de las manos en el address" como el mejor compromiso y iacas coincide en que un ángulo constante es mejor que mover la cámara. — [The Sand Trap foro](https://thesandtrap.com/forums/topic/104476-camera-angles-matter/)
- V1 Sports (guía oficial): DTL "8–12 feet behind you, pointing down the target line" y "**Align the camera with your hands at address**". — [V1 DTL](https://swing-analysis.v1sports.com/swing-analysis/down-the-line-view); [V1 Recording](https://swing-analysis.v1sports.com/swing-analysis/swing-recording)
- Titleist (Team Titleist): en las dos vistas, "always position the camera lens at the same height as the golfer's hands at address", y lo bastante lejos para que entre todo el arco. — [Titleist](https://www.titleist.com/teamtitleist/team-titleist/f/golf-tips/54984/online-golf-instruction-how-to-film-your-swing)
- GolfWRX (solo fragmentos del buscador; el sitio bloqueó la descarga): trípode con la altura "EXACTLY hand height and level", alineado "directly in line with the hand line", usando la varilla como guía; otra nota distingue **línea de las manos → altura de las manos, línea del objetivo → a nivel del piso, línea del cuerpo → apenas arriba de la cadera**. — [GolfWRX 160889](https://golfwrx.com/160889/use-the-proper-proper-camera-alignment-when-filming-your-swing/); [GolfWRX 164981](https://golfwrx.com/164981/what-golfers-should-see-in-swing-videos-with-proper-camera-alignment/)
- David Leadbetter (fragmento del buscador; la página dio error 503): cámara "directly on the hand line (between foot-line and ball-line)". — [Leadbetter](https://davidleadbetter.com/filming-instructions/)
- GOLF.com (Zephyr Melton, 27/05/2020, sobre un video de Athletic Motion Golf): "If the camera is not positioned directly down the swing plane line, you will not get an accurate representation"; en la vista torcida el takeaway parece ir muy adentro y "even the timing of the swing looks different". Sin números. — [GOLF.com](https://golf.com/instruction/bad-camera-angle-messing-with-your-golf-swing/?amp=1)
- Foro LynnBlake (fragmentos del buscador; el hilo dio 403): con la cámara en la línea del objetivo el plano se ve **más plano**; hacia la línea de los pies, **más empinado**; un usuario vio el mismo takeaway "muy empinado" con la cámara en el piso y "plano" con la cámara alta. — [LynnBlake](https://lynnblakegolf.com/forum/showthread.php?p=77685); [LynnBlake 2](https://www.lynnblakegolf.com/forum/showthread.php?p=949)
- The Sand Trap, comentario de lector (jr1under, 07/01/2022): el problema de no estar perpendicular/paralelo es paralaje; una app de nivel ayuda pero no lo resuelve del todo. — [The Sand Trap](https://thesandtrap.com/b/playing_tips/filming_your_swing)
- **Desacuerdo explícito:** The Sand Trap prefiere la línea de las puntas; V1, Titleist, GolfWRX y Leadbetter, la línea de las manos. Nadie publica una medición controlada del error. — fuentes de arriba.

### Inferences
- **Por qué la línea de las manos a la altura de las manos (geometría, CÁLCULO PROPIO):** el "plano de la varilla" es el plano que contiene la varilla del address y la dirección de la línea del objetivo. Un plano se proyecta como una **línea** solo si el centro de la cámara está **dentro** de ese plano. Ese plano pasa por la pelota (al piso) y por las manos, y se extiende hacia atrás paralelo a la línea del objetivo; por eso contiene: (a) la línea de las manos a la altura de las manos, (b) la línea del objetivo a la altura del piso y (c) la línea de las puntas a la altura donde el plano la cruza (~1,05–1,10 m en el modelo). Esto coincide exactamente con las tres alturas que da GolfWRX. Con la cámara en cualquiera de esos lugares, una posición que está en plano cae sobre la línea dibujada; fuera de ellos, no.
- **Cuánto se corre lo que está en plano según la cámara (CÁLCULO PROPIO, cámara a 3,0 m; desvío perpendicular a la línea pelota–manos del address, en cm a la profundidad de las manos; + = aparece arriba/"over", − = abajo/"under"). Columnas: palo 60 cm detrás y 60 cm "plano arriba" (zona P2/P6) | 90 cm detrás y 1,2 m arriba | follow-through 50 cm adelante:**
  - Línea de las manos, altura de las manos: 0 | 0 | 0
  - Línea del objetivo, a nivel del piso: −0,4 | −0,7 | +0,2
  - Línea de las puntas a 1,07 m (sobre el plano): 0 | 0 | 0
  - Línea de las puntas a la altura de las manos (0,75 m): **+4,3 | +7,3** | −2,4 → se ve más empinado / "over"
  - Mitad pelota–puntas, altura de las manos: −2,7 | −4,6 | +1,5
  - Línea de la pelota a la altura de las manos: **−9,6 | −16,4** | +5,5 → se ve más plano / "under"
  - Línea de las manos a la altura del pecho (1,25 m): **−6,6 | −11,2** | +3,7 → más plano
  - Línea de las manos, baja (0,45 m): +3,9 | +6,7 | −2,2 → más empinado
  - Regla que sale: **cámara por encima del plano → el swing parece más plano; por debajo → más empinado.** Coincide con lo que observan en LynnBlake (piso = empinado, alto = plano; objetivo = plano, pies = empinado).
  - A 3,7 m los desvíos bajan ~25 % y a 6,0 m a ~45 % de los de 3 m (p. ej., línea de la pelota: −16,4 → −12,3 → −6,8 cm): **más lejos (con zoom) = menos error de paralaje.**
- **Comparación con el error del swing 2 del proyecto:** el over the top medido fue "manos 14–23 cm por encima de su camino de subida". Un mal lugar de cámara produce desvíos absolutos del mismo orden (hasta ~16 cm). Pero subida y bajada pasan por profundidades parecidas, así que **comparar bajada contra subida (relativo) es mucho más robusto que comparar contra la línea del address (absoluto)**. Diagnosticar "over the top" debe apoyarse en la comparación relativa y en que la cámara esté verificada en la línea de las manos.
- **La varilla del address se mide bien desde casi cualquier lugar paralelo:** está en el plano frontal a la cámara (x≈0), así que su ángulo se conserva. CÁLCULO PROPIO: con la cámara desviada 5° (yaw) y sin inclinar, el ángulo de la varilla sigue en 58,3°; con 10° de yaw y 10° de inclinación, 57,1° (error ~1°). Lo que falla con la cámara mal puesta es todo lo que sale de ese plano (el palo detrás del cuerpo en la subida y la bajada).
- **Recomendación que surge:** línea de las manos, altura de las manos, celular nivelado (sin inclinar ni girar), apuntando paralelo a la línea del objetivo, a 3–3,7 m de las manos con 1x (o más lejos con 2x). Si el jugador "quiere" la línea de las puntas (The Sand Trap), subir la cámara hasta donde el plano cruza esa línea, o aceptar que se ve ~4–7 cm más empinado.

### Gaps
- No encontré ningún estudio que mida en grados/cm el error de "plano" por la posición DTL; los números de arriba son de un modelo propio.
- No pude leer completas las notas de GolfWRX, Leadbetter ni LynnBlake (403/503); lo citado sale de fragmentos del buscador.
- No encontré lo escrito por Mike Bennett/Andy Plummer sobre ubicación de cámara.

---

## 2. Altura de la cámara, distancia, distancia focal (0,5x / 1x / 2x) y distorsión; números de paralaje

### Takeaway
Altura: manos/cadera (The Sand Trap, Titleist, V1), "cintura, no más de 3,5 pies" (Sportsbox) o pecho (~130 cm, GolfFix). Para **líneas de plano** la altura importa (la cámara tiene que estar en el plano); para **ángulos de postura en el plano sagital** (inclinación de la columna en el address) importa más que el celular esté **nivelado** que la altura. Distancia: 2,4–3,7 m es el rango estándar; el ultra gran angular 0,5x obliga a acercarse (~2,1 m según Sportsbox), lo que **aumenta el error de perspectiva** y suma distorsión de lente: evitarlo para medir.

### Cited Findings
**Recomendaciones:**
- The Sand Trap: frente y DTL a "roughly hand height" (cerca de la cadera o un poco más abajo que el ombligo), el golfista un poco debajo del centro del cuadro. Frente: 6–12 pies (1,8–3,7 m) de la pelota; DTL: 8–12 pies (2,4–3,7 m); muy lejos el golfista no llena el cuadro y la perspectiva cambia; muy cerca el palo pasa cerca del lente. No da recomendaciones de lente o zoom. — [The Sand Trap](https://thesandtrap.com/b/playing_tips/filming_your_swing)
- V1: frente a la altura de la cadera, 6–10 pies; DTL 8–12 pies. — [V1](https://swing-analysis.v1sports.com/swing-analysis/swing-recording)
- Sportsbox AI (centro de ayuda): trípode a la cintura, "no higher than three-and-a-half feet (waist high)" (~1,07 m); "No more than 12 feet away from the golfer's toe line with standard zoom, 7ft with 0.5x zoom" (3,7 m con 1x; 2,1 m con 0,5x). — [Sportsbox](https://help.sportsbox.ai/how-do-i-set-up-my-camera-to-record-a-session)
- GolfFix (fragmento del buscador): altura del pecho en el address, ~130 cm; de frente a ~8–13 pies. — [GolfFix](https://notice.golffix.io/en/guide/recording)
- Uneekor Swing Optix (cámaras fijas de simulador): DTL ~6 pies detrás, a la altura de la cintura (~45 pulgadas), con **teleobjetivo**; la de frente usa ojo de pez. — [Uneekor](https://support.uneekor.com/knowledge/what-are-the-recommended-placement-and-orientation-for-swing-optix-cameras)
- iPhone: el ajuste **Ajustes > Cámara > Corrección de lente** "corrige la distorsión del lente en las cámaras frontal y ultra gran angular"; viene activado por defecto; hay reportes de usuarios de que apagarlo no cambia el ultra gran angular. Fuentes secundarias/foros, no encontré la página oficial de Apple. — [Gadget Hacks](https://ios.gadgethacks.com/how-to/disable-lens-correction-for-ultra-wide-camera-iphone-12-12-mini-12-pro-12-pro-max-0346741); [MacRumors](https://forums.macrumors.com/threads/13-pro-deactivating-lens-correction-has-no-effect.2323086); [Tom's Guide](https://tomsguide.com/how-to/how-to-enable-lens-correction-on-iphone)

**Datos de error medidos:**
- Stevens et al. 2006 (Am J Phys Anthropol, nota técnica): ángulos de codo y rodilla con **menos de 20° fuera del plano** de la cámara lateral "generally exhibit very little measurable difference from their 3D counterparts"; por encima de 20° se ven "significativamente más extendidos". Medido con un objeto de calibración (ángulo real 90°, cámara a 4 m): **a 45° fuera del plano se leyó 110,0° y 111,8°; a 90° fuera, 180,5° y 178,8°** (error de hasta ~100 %). Con la corrección trigonométrica (ángulo fuera del plano = arccos(largo aparente / largo real)) quedó en 88,1°, 88,5°, 87,6° y 92,7° (**error < 2–3°**). No recomiendan corregir debajo de 20° (amplifica el error de medición). Piden cámara fija "a distancia suficiente para reducir el paralaje". — [Stevens et al. 2006 (PDF)](https://people.ohio.edu/stevensn/documents/Stevens%20et%20al%202006%20Technical%20note.pdf)
- Informe DTIC (retropié): ángulos estáticos 2D vs 3D con error medio parecido (0,74° vs 0,81°) dentro de poco movimiento fuera del plano; movimientos transversales de más de ~20° requieren 3D. (Del fragmento del buscador.) — [DTIC](https://apps.dtic.mil/sti/pdfs/ADA267805.pdf)
- Brewin y Kerwin 2003 (J Appl Biomech 19:79–88): comparan "escalado" (objeto de medida conocida filmado en el plano del movimiento) contra 2D-DLT con distintas inclinaciones de cámara en 6 m de campo; el error del escalado **crece con la inclinación**; el 2D-DLT funciona con cualquier ángulo de cámara respecto del plano. No conseguí los números. — [Semantic Scholar](https://www.semanticscholar.org/paper/Accuracy-of-scaling-and-DLT-reconstruction-for-Brewin-Kerwin/6442d8afe29b2187fa1fa33de610639dad4b3f8a); [Tesis Marshall que lo resume](https://mds.marshall.edu/cgi/viewcontent.cgi?article=2884&context=etd)

### Inferences
- **Altura y líneas de plano:** ver la tabla de la pregunta 1. A 3 m, subir la cámara de la altura de las manos al pecho (+50 cm) corre ~7–11 cm hacia "abajo/plano" posiciones que están en plano.
- **Altura y ángulos de postura (CÁLCULO PROPIO):** la columna en el address está en el plano sagital del jugador, que en DTL queda de frente a la cámara: su ángulo se conserva a cualquier altura **si el celular está nivelado**. Si se inclina el celular hacia abajo para encuadrar: 5° → +0,6°, 10° → +1,3°, 15° → +2,3° en la inclinación de la columna (59,0° real). Conclusión: **nivelar es más importante que la altura exacta** para la postura; para el plano, la altura sí manda.
- **Distancia y error de profundidad (CÁLCULO PROPIO):** un error de escala por profundidad es ΔZ/Z. 1 cm de diferencia de profundidad da 0,48 % a 2,1 m, 0,33 % a 3 m, 0,27 % a 3,7 m y 0,20 % a 5 m; 10 cm de diferencia dan 4,8 %, 3,3 %, 2,7 % y 2,0 %. **Alejarse y usar 1x o 2x reduce todos los errores de perspectiva**; el 0,5x obliga a ~2,1 m y casi duplica el error respecto de 3,7 m, además de la distorsión de barril que el teléfono corrige por software (sin garantía de que la corrección sea métrica).
- **Lente para medir:** usar **1x (principal)** a 3–3,7 m, o **2x/teleobjetivo** desde más lejos si el espacio y la luz lo permiten (menos paralaje; pero en interiores el tele recibe menos luz → obturador más lento). Nunca 0,5x para medir. Si se quiere medir con rigor, calibrar la cámara una vez con un tablero de ajedrez (OpenCV `calibrateCamera` estima focal y coeficientes de distorsión) — ver pregunta 5.
- Encuadre: el golfista + el arco del palo deben entrar con margen (Sportsbox lo exige); en vertical 1080x1920 el golfista ocupa más píxeles que en horizontal.

### Gaps
- No encontré mediciones publicadas de la distorsión residual del 0,5x de iPhone después de la corrección de software, ni la documentación oficial de Apple sobre "Corrección de lente".
- No conseguí los números de Brewin y Kerwin (2003) ni de Sih et al. (2001).

---

## 3. De frente (face-on): centrada en el esternón, la pelota o el medio de la postura; efecto en sway, slide, inclinación de la varilla, posición de la pelota y cabeza

### Takeaway
The Sand Trap y V1 coinciden: **cámara perpendicular a la línea del objetivo, centrada en el medio de la postura** (varilla perpendicular entre los pies como guía), a la altura de las manos/cadera, a 1,8–3,7 m. Para **medir** en cm hay que recordar que el cuerpo está **más lejos** que la pelota: si se escala con algo en la línea de la pelota, los movimientos de cadera y cabeza se subestiman ~18–25 % a 3–3,7 m (CÁLCULO PROPIO); y la posición de la pelota respecto del talón tiene paralaje cuando la pelota está lejos del centro.

### Cited Findings
- The Sand Trap: "use an alignment stick perpendicular to your target line in the exact middle of your stance. Set the camera right on that line, and the stick can double as a ball position aid"; altura "hand height"; apuntada en ángulo recto a la línea del objetivo; 6–12 pies de la pelota. — [The Sand Trap](https://thesandtrap.com/b/playing_tips/filming_your_swing)
- V1: frente "parallel to the ball-target line, 6–10 feet in front of you", a la altura de la cadera; revela sway de cadera, extensión temprana, pivot invertido y transferencia de peso, "faults that are nearly invisible from down the line". — [V1 Face-on](https://swing-analysis.v1sports.com/swing-analysis/face-on-view)
- Sportsbox: para importar videos recomienda "an existing slow motion, face-on video". — [Sportsbox](https://help.sportsbox.ai/how-do-i-set-up-my-camera-to-record-a-session)
- Revisión (Salford) sobre 2D: el video 2D no puede medir movimiento en planos que no son perpendiculares a la cámara sin error de perspectiva; una nota comercial de Noraxon muestra una abducción de rodilla de −22° en 2D contra −2,3° en 3D (fuente comercial). — [Salford](https://salford-repository.worktribe.com/OutputFile/1492813); [Noraxon](https://www.noraxon.com/article/understanding-the-limitations-of-2d-video-analysis-vs-3d-imu-based-motion-capture/)

### Inferences
- **Centrado:** centrar en el **medio de la postura** (en el address el esternón está casi ahí). Centrarla en la pelota corre el eje óptico y aumenta el paralaje del lado de atrás (donde ocurre el sway).
- **Escala por profundidad (CÁLCULO PROPIO; cámara a D de la línea de la pelota; pies a +0,65 m; pelvis ~10 cm detrás de las puntas):** si la escala sale de una varilla en la línea de la pelota, la pelvis está ×1,36 más lejos a D=2,1 m (+36 %), ×1,25 a 3,0 m (+25 %), ×1,20 a 3,7 m (+20 %); las manos ×1,15 a 3 m. Es decir, **un sway real de 10 cm se mediría como ~8 cm** a 3 m si no se corrige. Regla: **escalar con un objeto en el plano de lo que se mide** (p. ej., una varilla vertical o horizontal apoyada contra la línea de las puntas/cadera) o corregir multiplicando por Z_objeto/Z_referencia.
- **El palo en el address NO sirve como escala de frente (CÁLCULO PROPIO):** de frente la varilla va de las manos a la pelota acercándose ~45 cm a la cámara: está ~32° fuera del plano de la imagen y se ve ~15 % más corta (cos 32° ≈ 0,85), además de cruzar profundidades. Desde atrás (DTL), en cambio, la varilla del address está casi en el plano de la imagen (la inclinación hacia el objetivo de ~10 cm la saca solo ~7°, cos ≈ 0,99): **en DTL la longitud del palo es buena escala para el plano manos–pelota.**
- **Posición de la pelota (CÁLCULO PROPIO):** la pelota está ~0,65 m más cerca de la cámara que el talón. Si la pelota está a X del eje óptico, aparece corrida X·0,65/D hacia afuera: con el driver a 25 cm del centro y D = 3 m, **~5 cm más adelante** de lo real respecto del talón; con un hierro a 10 cm, ~2 cm. Para posición de pelota, usar la varilla perpendicular que pasa por la pelota, o la homografía del piso (pregunta 5).
- **Movimiento en profundidad que se ve como lateral (CÁLCULO PROPIO):** un punto a 30 cm del eje que se acerca 10 cm a la cámara (p. ej., extensión temprana) aparece corrido 1,25 cm de costado a 2,5 m y 0,88 cm a 3,5 m; a 50 cm del eje, 2,1 y 1,5 cm. Es chico, pero suma ruido a "slide" y "cabeza quieta".
- **Inclinar el celular hacia abajo tuerce las verticales (CÁLCULO PROPIO):** una vertical a 40 cm del centro se ve inclinada 0,7° con 5° de inclinación del celular, 1,3° con 10° y 2,0° con 15°. Importa para inclinación de la varilla (shaft lean), inclinación de la columna y "pierna de adelante vertical". **Celular nivelado** (sin inclinación ni giro) es obligatorio para estas lecturas.
- Sway/slide/cabeza se leen bien de frente si: cámara perpendicular, centrada, nivelada, a ≥3 m, y escala tomada en el plano del cuerpo. Inclinación de columna y shaft lean: ángulos en el plano frontal → se conservan si el celular está nivelado y perpendicular.

### Gaps
- No encontré mediciones publicadas del error de sway/slide en video 2D de golf comparado con 3D.

---

## 4. Cuadros por segundo y obturador; cámara lenta del iPhone, frecuencia variable, re-mapeo de tiempo y cómo conseguir el archivo original

### Takeaway
The Sand Trap pide **~200–300 fps (mínimo 720p) y obturador de ~1/1000 s**; V1 y Sportsbox piden cámara lenta (240 fps en iPhone). A 240 fps la cabeza del palo de un amateur (~40 m/s) avanza ~17 cm entre cuadros (CÁLCULO PROPIO), así que el impacto exacto casi nunca queda en un cuadro. El "Slo-mo" del iPhone guarda un video de alta frecuencia con una **curva de velocidad** encima; según cómo se exporte, queda en 240, 120 o **30 fps**: hay que pedir el **original** (AirDrop/USB, velocidad al 100 %).

### Cited Findings
- The Sand Trap: ~200–300 fps con al menos 720p (4K casi nunca hace falta); con menos se pierden movimientos sutiles y el impacto puede errarse "by several inches"; 120 o 60 fps sirven para principiantes con errores grandes, ritmo o tiros cortos. Obturador mínimo ~1/1000 s (fácil afuera, incluso nublado; adentro cuesta llegar a 1/500); a 1/500 la cabeza del palo "barely visible", a 1/2000 se ve claro el filo. — [The Sand Trap](https://thesandtrap.com/b/playing_tips/filming_your_swing)
- V1: "Use slow motion (240fps on iPhone)". — [V1](https://swing-analysis.v1sports.com/swing-analysis/swing-recording); [V1 slow motion](https://swing-analysis.v1sports.com/swing-analysis/slow-motion-swing-analysis)
- Sportsbox: "The video must be in SLOW MOTION, NOT regular speed"; recortar para que sea "ONLY the swing"; ni muy oscuro ni muy claro ("Extreme Lighting Mode" adentro). — [Sportsbox Do This, Not That](https://help.sportsbox.ai/sportsbox-3dgolf-app-do-this-not-that)
- Apple (manual del iPhone): el modo Slo-mo "records your video as normal and then plays it back in slow motion"; se edita qué parte se reproduce lenta; frecuencia y resolución en Ajustes > Cámara > Grabar cámara lenta; en iPhone 16 Pro, 17 Pro, 18 Pro y iPhone Duo se puede grabar cámara lenta desde el modo Video eligiendo 120 fps; "Videos you record at faster frame rates can be played back at slower speeds in the Photos app". — [Apple Support](https://support.apple.com/guide/iphone/record-videos-iph61f49e4bb/ios)
- Ben Stolovitz (20/05/2026): el iPhone aplica por defecto una curva ("easing") que reproduce lento el medio y a velocidad normal el principio y el final; si se saca, queda "an ordinary 240FPS video file". **Arrastrar desde Fotos de macOS → 120 fps; Archivo > Exportar → 30 fps; AirDrop del iPhone a la Mac o "Editar con QuickTime" → 240 fps.** Método: en Fotos del iPhone, Editar → velocímetro → "100 % – 240 FPS"; pasar por AirDrop; verificar en QuickTime (Inspector) "Encoded FPS" ~238–239, la variación se debe a **frecuencia variable**. — [Stolovitz](https://ben.stolovitz.com/posts/export-slo-mo-videos-from-your-iPhone/)
- Klipa: el archivo es una secuencia de 120/240 fps más una instrucción dentro del MOV que dice dónde frenar la reproducción. — [Klipa](https://klipa.ai/en/blog/iphone-slow-motion-video-normal-speed-export_1379)
- Copiar por USB la carpeta DCIM conservó los originales a 240 fps (usuario de Synology). — [Synology](https://community.synology.com/enu/forum/1/post/122740)
- **Fuentes en conflicto:** un hilo de Apple dice que AirDrop conserva la cámara lenta; otro usuario dice que AirDrop mandó solo la versión editada; un post de Adobe afirma que el iPhone guarda 30 fps (contradice a los demás). — [Apple Community](https://discussions.apple.com/thread/6569030?page=3); [Adobe](https://community.adobe.com/t5/premiere-pro-discussions/exporting-240fps-iphone-footage-in-the-same-format-as-original/m-p/8789398)
- Immich (issue): los videos en cámara lenta de 240 fps de iOS se "exportan" en vez de respaldarse como original. — [GitHub immich #17576](https://github.com/immich-app/immich/issues/17576)

### Inferences
- **Recorrido y desenfoque de la cabeza del palo (CÁLCULO PROPIO):** a 70 / 90 / 113 mph (31 / 40 / 51 m/s), entre cuadros avanza: 30 fps 104 / 134 / 168 cm; 60 fps 52 / 67 / 84 cm; 120 fps 26 / 34 / 42 cm; **240 fps 13 / 17 / 21 cm**. Desenfoque dentro de un cuadro: 1/240 s 13–21 cm; 1/500 s 6–10 cm; **1/1000 s 3–5 cm**; 1/2000 s 1,6–2,5 cm. Coincide con lo que describe The Sand Trap.
- **Consecuencias para medir:** a 240 fps el "cuadro de impacto" es el último antes de que la pelota se mueva o el primero después; las posiciones del palo cerca del impacto tienen ±8–10 cm de incertidumbre temporal. Las manos (mucho más lentas) y el cuerpo sí quedan bien. A 60 fps no hay que leer nada del palo cerca del impacto.
- **Frecuencia variable:** no asumir fps constante; tomar los tiempos de cada cuadro del archivo (pts con ffprobe) y verificar fps real (≈238–240). Si un archivo dice 30 fps o dura 8× más, es una exportación con re-mapeo de tiempo: pedir el original.
- **Pedido práctico al seguidor:** grabar en Cámara lenta 240 fps (o 120 si hay poca luz), mucha luz (afuera o al lado de la puerta del galpón), y mandar el original por AirDrop/USB/Drive "archivo original" con la velocidad en 100 %; no por WhatsApp ni exportado desde Fotos de la Mac.

### Gaps
- No encontré documentación oficial de Apple sobre el formato interno (metadatos de re-mapeo) ni sobre qué hace "Incluir todos los datos de la foto" con la cámara lenta.
- No encontré una fuente confiable sobre cuánto recomprime WhatsApp/Instagram un video en cámara lenta (frecuencia final); no lo afirmo.
- No encontré cómo fijar manualmente el obturador en la app Cámara del iPhone (las apps de terceros sí lo permiten); sin fuente.

---

## 5. Fotogrametría de una sola vista: escala con un objeto de medida conocida, error por profundidad, punto de fuga con dos varillas paralelas, homografía del piso y precisión esperable

### Takeaway
Con una sola cámara se puede medir en cm **solo dentro de un plano conocido** (el piso, o el plano frontal a la cámara a una profundidad conocida). El escalado simple exige que el objeto de referencia esté **en el mismo plano** que lo medido (Brewin y Kerwin); fuera de ese plano el error es ΔZ/Z (≈3 % por cada 10 cm a 3 m). Dos varillas paralelas dan el **punto de fuga** de la línea del objetivo (sirve para verificar que la cámara apunta paralela) y un rectángulo de varillas en el piso da la **homografía** del piso (posición de pelota, pies, ancho de postura, alineación). La métrica de una sola vista (Criminisi et al.) permite incluso alturas con un punto de fuga vertical, con error del orden de 1 % en buenas condiciones.

### Cited Findings
- Brewin y Kerwin 2003: el escalado consiste en filmar "a calibration object of known horizontal and vertical dimensions ... within the calibration plane"; el error del escalado crece con la inclinación de la cámara; el 2D-DLT (homografía) funciona con cualquier ángulo de cámara respecto del plano. — [Semantic Scholar](https://www.semanticscholar.org/paper/Accuracy-of-scaling-and-DLT-reconstruction-for-Brewin-Kerwin/6442d8afe29b2187fa1fa33de610639dad4b3f8a); [Tesis Marshall](https://mds.marshall.edu/cgi/viewcontent.cgi?article=2884&context=etd)
- Criminisi, Reid y Zisserman ("Single View Metrology", ICCV 1999; IJCV 40:123–148, 2000): con la **línea de fuga de un plano de referencia** y un **punto de fuga** de una dirección no paralela se recuperan medidas afines 3D (distancias entre planos paralelos, razones de áreas y longitudes, posición de la cámara) **sin calibración interna ni pose**; el marco permite propagar el error a primer orden; ejemplo: altura de una persona calculada 178,8 cm contra 180 cm reales (≈0,7 %). — [Microsoft Research](https://www.microsoft.com/en-us/research/publication/single-view-metrology-4/); [PDF typeset](https://typeset.io/pdf/single-view-metrology-4b47v84cbh.pdf); [ICCV 1999](https://mlanthology.org/iccv/1999/criminisi1999iccv-single)
- Stevens et al. 2006: corrección de un segmento fuera del plano con θ = arccos(largo aparente / largo real); dejó el ángulo en ±2–3° aun a 45–90° fuera del plano; requiere conocer los largos reales y calibrar con medidas en el espacio de estudio. — [Stevens et al. 2006](https://people.ohio.edu/stevensn/documents/Stevens%20et%20al%202006%20Technical%20note.pdf)
- Sih, Williams y Hubbard 2001 (J Biomech): si se conoce la distancia fuera del plano, una corrección analítica mejora sustancialmente la precisión 2D. — [Registro](https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi.dedup.....94faa59052705b9c724b07173cbb09eb)
- Hartley y Zisserman, *Multiple View Geometry in Computer Vision* (2.ª ed.): referencia estándar de homografías, puntos y líneas de fuga, calibración y triangulación. — [Libro (Oxford VGG)](https://www.robots.ox.ac.uk/~vgg/hzbook/)
- OpenCV: tutoriales de homografía (`findHomography`, `getPerspectiveTransform`) y de calibración de cámara con tablero (`calibrateCamera`, coeficientes de distorsión). (Las URL dieron 403 desde este entorno; no verifiqué el texto.) — [OpenCV homografía](https://docs.opencv.org/4.x/d9/dab/tutorial_homography.html); [OpenCV calibración](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)

### Inferences
**Método (fórmulas estándar; números = CÁLCULO PROPIO):**
1. **Escala en un plano frontal:** s = L_px / L_real (px por cm) medida con un objeto en el plano de interés a profundidad Z₀. Un punto a profundidad Z tiene escala s·Z₀/Z. Error relativo si se ignora: ΔZ/Z (3,3 % por cada 10 cm a 3 m; 4,8 % a 2,1 m). En DTL, una varilla apoyada en el piso paralela a la línea del objetivo apunta a la cámara y no sirve de escala; usar **el palo en el address** (casi frontal en DTL) o **una varilla vertical clavada en la línea de las manos**. De frente, **una varilla horizontal paralela a la línea del objetivo apoyada en la línea de las puntas** (misma profundidad que pies/cadera, ±10 cm).
2. **Segmentos fuera del plano:** si se conoce el largo real L (palo, antebrazo), el ángulo fuera del plano es θ = arccos(L_aparente/L) (Stevens); no aplicar debajo de ~20°.
3. **Punto de fuga de la línea del objetivo (verificación de la cámara):** dos varillas paralelas a la línea del objetivo (una en la línea de las puntas y otra en la de la pelota). En coordenadas homogéneas: l₁ = p₁×p₂, l₂ = p₃×p₄, v = l₁×l₂. En DTL, si la cámara apunta exactamente paralela a la línea del objetivo, **v cae en el punto principal (centro de la imagen)**. El desvío angular es θ ≈ atan(|v − c| / f), con f en píxeles. Si v queda a la izquierda/derecha, la cámara apunta hacia ese lado; si queda arriba/abajo del centro, está inclinada (pitch). Con f ≈ 1.400 px, un error de 5° corre v ~120 px.
4. **Focal en píxeles:** de la calibración con tablero (OpenCV), o de dos puntos de fuga de direcciones ortogonales en el piso (varillas paralelas + varillas perpendiculares): f² = −(v₁ − c)·(v₂ − c) (resultado estándar de H&Z; c = centro). Aproximación sin calibrar: f_px ≈ ancho_px × (focal equivalente 35 mm / 36 mm) en horizontal, menos fiable porque el video recorta el sensor.
5. **Homografía del piso:** 4 puntos del piso con coordenadas reales conocidas (las puntas de dos varillas paralelas de largo conocido separadas una distancia medida forman un rectángulo) → H (3×3) con `getPerspectiveTransform`/`findHomography`. Después, cualquier punto **del piso** (pelota, punta y talón de cada pie, marca del divot) pasa a cm: [X, Y, 1]ᵀ ∝ H⁻¹[u, v, 1]ᵀ. Sirve para posición de pelota, ancho de postura, alineación de pies vs línea del objetivo y distancia a la pelota, con independencia del lugar de la cámara. **No sirve para puntos fuera del piso** (manos, cadera, cabeza): para esos, usar un plano paralelo a una altura conocida o la métrica de Criminisi con el punto de fuga vertical (una varilla o el palo sostenido vertical da la dirección vertical).
6. **Precisión esperable en buenas condiciones (CÁLCULO PROPIO, presupuesto de error):** video vertical 1080x1920 con golfista + arco (~2,6 m) en 1.920 px → ~1,4 mm/px. Marcar puntos a mano con ±3 px → ±4 mm. Profundidad del objeto incierta ±10 cm a 3 m → ±3,3 % de escala (un sway de 10 cm → ±0,3 cm). Desenfoque de movimiento y ropa suelta suman más que eso: **±1 cm para cadera/cabeza/manos y ±1° para ángulos de segmentos en el plano frontal** es un objetivo realista; segmentos fuera del plano (>20°) pueden errar decenas de grados sin corrección (Stevens). El palo cerca del impacto, ±8–10 cm por el intervalo entre cuadros (pregunta 4). Con detección automática de pose (sin marcadores), sumar su error propio (pregunta 7).
- **Cómo se usa con dos varillas en la práctica:** colocar una varilla en la línea de las puntas y otra en la línea de la pelota/objetivo, paralelas, y medir con cinta la separación y el largo. Sirven a la vez para: alinear la cámara DTL (punto de fuga en el centro), escala de frente (la de las puntas) y homografía del piso. Una tercera varilla perpendicular en el medio de la postura (The Sand Trap) ubica la cámara de frente y da la segunda dirección de fuga.

### Gaps
- No conseguí los valores de error de Brewin y Kerwin (2003) ni el error típico de la homografía de piso en video de celular; el presupuesto de arriba es propio.
- No encontré el largo estándar de las varillas de alineación con fuente; medirlas con cinta en cada caso.

---

## 6. Dos cámaras sincronizadas: cómo sincronizar (palmada, sonido del impacto) y qué se gana en 3D

### Takeaway
La sincronización por audio está publicada en biomecánica, pero **sincronizar el audio no garantiza que el video quede sincronizado** (se codifican por separado) y el sonido llega con retraso según la distancia. En golf hay un evento visual natural muy preciso: **el impacto (primer cuadro con la pelota en movimiento)** en las dos vistas, que da sincronía a ±1 cuadro (±4 ms a 240 fps). Con dos vistas casi ortogonales (DTL + frente) calibradas se puede triangular en 3D; sin calibrar, al menos cada vista corrige la profundidad que le falta a la otra.

### Cited Findings
- Biomecánica: método de sincronización de cámaras usando la banda de audio (J Biomech 39(4):776–780, 2006) y método de sincronización con datos de video digitalizados (Yeadon y King 1999), citados en la literatura de sincronización. — [Sensors 21(1):68](https://www.mdpi.com/1424-8220/21/1/68); [PMC7795013](https://pmc.ncbi.nlm.nih.gov/articles/PMC7795013)
- Audio y video se codifican por separado: aun con los audios perfectamente alineados, los videos pueden quedar desfasados; además, las cámaras tienen que estar cerca para captar el mismo sonido. Un método con flash logra precisión del orden de un cuadro (~40 ms); métodos de obturador rodante, sub-cuadro; un método con péndulo, 3,5 ms de diferencia absoluta media. — [RocSync, arXiv 2511.14948](https://arxiv.org/pdf/2511.14948)
- Sincronizar celulares correlacionando las señales de giroscopio (estudio de marcha 2025) y códigos de tiempo embebidos en audio y video (Syncalize). — [Syncalize AIT](https://publications.ait.ac.at/de/publications/syncalize-precise-automatic-timecodes-for-video-and-audio-devices/)
- Triangulación desde dos vistas calibradas: referencia estándar. — [Hartley y Zisserman](https://www.robots.ox.ac.uk/~vgg/hzbook/)
- Captura sin marcadores con varias cámaras (OpenPose): precisión de ≤30 mm para movimiento humano si se corrigen los errores de seguimiento. — [Nakano et al. 2020, PMC7739760](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7739760/)

### Inferences
- **Retraso del sonido (CÁLCULO PROPIO):** a 343 m/s, cada metro de diferencia de distancia al sonido son 2,9 ms ≈ 0,7 cuadros a 240 fps. Si un celular está a 3 m del impacto y el otro a 5 m, el audio desfasa ~6 ms (~1,4 cuadros) aunque los relojes fueran perfectos. Una palmada en el punto medio entre las cámaras lo reduce.
- **Método recomendado:** sincronizar por **evento visual**: el cuadro del impacto (pelota que empieza a moverse) en las dos vistas; como control, un segundo evento (la cabeza del palo pasando por la posición paralela al piso en la bajada). Audio solo como aproximación inicial (cross-correlation del "clic" del impacto) y después refinar con el cuadro visual.
- **Qué se gana:** (a) cada vista da la profundidad que falta en la otra: el DTL mide cuánto se acerca la cadera a la pelota (extensión temprana) y de frente se corrige la escala de esa cadera; el frente mide el desplazamiento lateral que el DTL ve como profundidad; (b) con calibración (puntos comunes en las dos vistas: varillas del piso + una vertical) se triangulan manos, cabeza del palo y cadera en 3D (ángulo real del plano de la subida y de la bajada, no proyectado). Vistas a ~90° son la mejor geometría para triangular (resultado estándar).
- Si las dos cámaras graban en frecuencias distintas o variables, sincronizar por tiempos de cuadro (pts), no por número de cuadro.

### Gaps
- No encontré el desfase típico audio-video de un iPhone en cámara lenta, ni cómo queda el audio dentro del tramo en cámara lenta del archivo.
- No encontré un estudio de precisión 3D con dos celulares filmando golf.

---

## 7. Qué piden Sportsbox AI y otras apps 3D sin marcadores para ser precisas

### Takeaway
Sportsbox AI pide **una sola cámara**, de frente o DTL, a **≤3,7 m (12 pies) de la línea de las puntas con 1x o ~2,1 m con 0,5x**, trípode **a la cintura (≤1,07 m)**, cuerpo y palo completos todo el swing, **cámara lenta** y video recortado al swing. No encontré una validación independiente publicada de Sportsbox contra captura con marcadores; los estudios de otros sistemas sin marcadores dan errores de ~3° y ~3 cm.

### Cited Findings
- Sportsbox AI: vertical u horizontal; ≤12 pies de la línea de las puntas con zoom estándar, 7 pies con 0,5x; trípode a la cintura, no más de 3,5 pies; "Make sure the entire body is in the frame throughout the full swing"; para importar, "an existing slow motion, face-on video". — [Sportsbox setup](https://help.sportsbox.ai/how-do-i-set-up-my-camera-to-record-a-session)
- Sportsbox AI: frente o DTL; "SLOW MOTION, NOT regular speed"; recortar al swing; cuerpo y palo enteros todo el swing; ni muy oscuro ni muy claro; "Extreme Lighting Mode". — [Sportsbox Do This, Not That](https://help.sportsbox.ai/sportsbox-3dgolf-app-do-this-not-that)
- Reseña alemana (no validación): Sportsbox reconoce más de 30 puntos clave y presenta "seis ángulos de vista"; afirma datos comparables a estudio, sin medición publicada. — [KI-Syndikat](https://www.ki-syndikat.de/tools/sportsbox-ai/)
- Uneekor Swing Optix: DTL ~6 pies detrás y ~45 pulgadas de alto, teleobjetivo; de frente con ojo de pez delante del jugador. — [Uneekor](https://support.uneekor.com/knowledge/what-are-the-recommended-placement-and-orientation-for-swing-optix-cameras)
- GolfFix: altura del pecho (~130 cm), de frente a ~8–13 pies (fragmento del buscador). — [GolfFix](https://notice.golffix.io/en/guide/recording)
- Precisión de sistemas sin marcadores (no golf, no Sportsbox): OpenPose con varias cámaras ≤30 mm; un estudio de saltos 2025: RMSE 3,29 ± 2,36° contra marcadores y concordancia de Lin 0,51 ± 0,19, peor en flexión de cadera (dato del fragmento del buscador). — [Nakano et al. 2020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7739760/); [PMC12833419](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12833419/)

### Inferences
- Lo que piden estas apps (cámara baja, cuerpo completo, cámara lenta, luz) coincide con lo que también pide la medición manual; el límite de 3,7 m de Sportsbox probablemente sale de cuántos píxeles necesita su modelo para el cuerpo (inferencia, no confirmada).
- Para el producto pago, los números de una app sin marcadores deben presentarse como "estimación de una vista", no como medición de laboratorio, salvo que exista validación publicada.

### Gaps
- No encontré ningún estudio independiente que valide Sportsbox AI (ni otra app de golf de una sola cámara) contra captura 3D con marcadores, ni su error en grados.
- No encontré la guía de cámara de Hudl Technique/Coach's Eye.

---

## 8. Protocolo resultante (síntesis de las respuestas anteriores)

### Takeaway
Dos videos (DTL y frente), cada uno con trípode, celular nivelado, lente 1x, cámara lenta 240 fps con mucha luz, y **dos varillas paralelas en el piso** (línea de las puntas y línea de la pelota) más una perpendicular en el medio de la postura, medidas con cinta. DTL en la línea de las manos a la altura de las manos, a 3–3,7 m; frente perpendicular, centrado en el medio de la postura, a la altura de las manos/cadera, a 3–3,7 m de la pelota. Enviar los originales.

### Cited Findings
- Altura de las manos, varilla junto a las puntas, cámara paralela/perpendicular, 2,4–3,7 m, 200–300 fps, 1/1000 s. — [The Sand Trap](https://thesandtrap.com/b/playing_tips/filming_your_swing)
- Alinear con las manos, 8–12 pies, 240 fps, trípode. — [V1](https://swing-analysis.v1sports.com/swing-analysis/swing-recording)
- Cuerpo y palo completos, cámara lenta, ≤3,7 m con 1x. — [Sportsbox](https://help.sportsbox.ai/how-do-i-set-up-my-camera-to-record-a-session)
- Original a 240 fps: velocidad 100 % y AirDrop/USB; no "Exportar" desde Fotos. — [Stolovitz](https://ben.stolovitz.com/posts/export-slo-mo-videos-from-your-iPhone/)

### Inferences
**Protocolo propuesto (para pedirle al seguidor):**
1. **Preparación:** dos varillas (o dos palos) en el piso, paralelas a la línea del objetivo: una justo delante de las puntas de los pies, otra en la línea de la pelota hacia el objetivo. Medir con cinta su largo y la distancia entre ellas y anotarlo. Opcional: una tercera perpendicular en el medio de la postura.
2. **DTL:** trípode detrás, **en la prolongación de la línea de las manos** (entre la varilla de las puntas y la de la pelota, más cerca de la de las puntas), con el lente **a la altura de las manos en el address**, celular **nivelado** (nivel de burbuja o app), apuntando **paralelo** a las varillas (las dos deben converger hacia el centro de la pantalla). Distancia 3–3,7 m de las manos. Lente 1x. Que entren todo el cuerpo, el palo arriba y el follow-through.
3. **Frente:** trípode enfrente, **perpendicular** a la línea del objetivo, en la línea de la varilla del medio de la postura, lente a la altura de las manos/cadera, **nivelado**, 3–3,7 m de la pelota, 1x, golfista un poco por debajo del centro.
4. **Video:** Cámara lenta 240 fps (120 si falta luz), afuera o con mucha luz; 3 swings por vista sin mover el trípode; un palo indicado (hierro 7 y driver por separado).
5. **Envío:** archivo original (AirDrop/USB/Drive como "original"), velocidad 100 %; no por WhatsApp ni exportado. Verificar al recibir: fps ≈ 240 (ffprobe), duración real (no 8× más larga).
6. **Al analizar:** (a) comprobar el punto de fuga de las varillas en DTL (si no está cerca del centro, avisar que las líneas de plano tienen error y cuantificar el giro θ = atan(d/f)); (b) en DTL, juzgar over/under comparando **bajada contra subida** y no solo contra la línea del address; (c) en frente, escalar con la varilla de las puntas (no con el palo del address) y usar homografía del piso para pelota y pies; (d) informar las medidas como "aproximadas" con su margen (±1 cm cuerpo/manos, ±1° ángulos frontales, ±8–10 cm palo cerca del impacto a 240 fps).

### Gaps
- El protocolo combina recomendaciones de práctica con un modelo geométrico propio; no hay un estudio que valide este protocolo específico contra 3D.
