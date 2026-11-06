---
name: analisis-swing
description: Análisis técnico y crítico de swings de golf de seguidores (video desde atrás y de frente) para el producto pago del dueño. Usar cuando llega un video de swing para analizar, cuando hay que pedirle a un seguidor que filme su swing, o cuando hay que armar el reel o el informe PDF de un análisis. Incluye el protocolo de filmación y calibración (con el mensaje listo para mandar), los márgenes honestos de medición, el protocolo de over the top con su herramienta (tools/plano_check.py), el checklist P1-P10, la tabla de decisión de las 16 características de TPI, las leyes de vuelo, la postura crítica sin sesgo positivo y el formato del reel (análisis puro que termina con un drill).
---

# Análisis de swing (producto pago)

Lo van a evaluar **profesores de golf**. Un error técnico (decir "en plano" a un swing over the top) es inaceptable.
Base de todo: `swing-analisis/investigacion/informe.md` (investigación del 05–06/11/2026, con fuentes). Contexto y herramientas:
`swing-analisis/CLAUDE.md`. Tablas completas en `referencias/` (abajo dice cuándo leer cada una).

## 1. Postura crítica (no negociable)

- **Evaluar sin sesgo positivo.** El diagnóstico sale de los datos, no del tono. Nada de "sándwich" de elogios:
  primero lo que más afecta el contacto y la dirección; lo bueno solo si es técnicamente relevante y está medido.
- **Asimetría:** para decir que algo está **bien** hacen falta todas las pruebas de esa zona dentro del margen. Si falta una,
  es "no evaluable", nunca "correcto". Nunca se da por bueno un fundamento por falta de evidencia en contra.
- **Lo que diga el dueño o el jugador es una hipótesis**, no un dato: aislar la afirmación, medirla, concluir, y cambiar de
  opinión solo con evidencia nueva, no por insistencia.
- **Cada afirmación lleva medida + cuadro + criterio con su tipo de fuente.** Si falta alguno, no se dice.
- **Solo tres tipos de afirmación:** *medido* (dibujado sobre el cuadro, con número y margen: cualquiera lo puede verificar mirando),
  *inferido* (del vuelo o del contacto, dicho como "por el vuelo que contás…") y *no evaluable*. **Si no se puede dibujar sobre el
  video, no se afirma como medido.** El dibujo es a la vez el visual del reel y la prueba.
- **Puerta antes de publicar (primeros 5 videos, 06/11/2026):** el dueño anota su diagnóstico a ciegas → se le muestra la hoja de
  cuadros con las líneas y el diagnóstico escrito → se discuten los desacuerdos con el cuadro y la medida → recién ahí voz y render.
  Lo que no se resuelve no se publica o se dice "no concluyente".
- **Una sola prioridad.** Ocho fallas del mismo peso se leen como análisis amateur. Prioridad = la causa, no el efecto.
- **Revisión final de "profesor desconfiado"** (sección 10) antes de entregar.

## 2. Qué se puede medir y con qué margen

Un celular mide posiciones **dentro del plano de la imagen** comparadas con el **address del mismo jugador**. No hay normas de tour en
cm validadas, y las que hay se contradicen entre fabricantes: la referencia defendible es el propio address y los propios videos.

| Se mide (aprox.) | Margen honesto [INF] |
|---|---|
| Ángulos en el plano de la imagen (tronco, rodilla, varilla) en P1, P3, P4, P5, P7, P10 | ±3–5° (±5–10° entre P5 y P8 a 30–60 fps) |
| Desplazamientos con escala en el plano del cuerpo (sway, cabeza, nalga, pelvis) | ±1–3 cm |
| Manos o varilla respecto del plano (desde atrás, cámara verificada) | ±2–4 cm |
| Momentos P1–P10 y ritmo (ritmo solo con video a velocidad real) | ±1 cuadro |

**No se informa con números:** giro de pelvis y tórax, X-factor, velocidades de la secuencia cinemática, muñecas (solo
"se ve cupped/bowed"), cara, path en grados, loft dinámico, velocidad. Se dice "no se mide con este video" o se **infiere del vuelo**.
- **P2 y P6 desde atrás:** la varilla apunta casi a la cámara (en las pruebas se vio a 17–48 % de su largo). Su ángulo en la imagen no vale.
- Redondear y dar margen: "≈37° (±5°)". Nunca decimales de laboratorio.
- **Consistencia entre los 3 swings** de cada toma: es algo que el ojo no mide y se relaciona con el score
  (inclinación del tronco, r = 0,801 [PR]). Informar cuánto varía cada medida entre swings.
- **Tipo de fuente en el PDF** para cada número de referencia: "estudio publicado (n = …)" [PR] · "estudio preliminar" [CONF] ·
  "dato del fabricante, sin validación independiente" [FAB] · "según TPI (dato propio)" [TPI] · "criterio de enseñanza" [INS] ·
  "estimación propia" [CP/INF]. Lo [NV] no se usa. No comparar contra referencias de otro sistema (el X-factor del mismo swing
  da −72° o −124° según el método [PR]).

## 3. Antes de analizar: video y datos

Leer **`referencias/filmacion.md`**: protocolo completo, error por ubicación de la cámara, control al recibir y el **mensaje listo
para mandarle al seguidor**. Lo esencial:
- **Desde atrás:** cámara en la **prolongación de la línea de las manos** del address (entre la varilla de las puntas y la de la
  pelota, más cerca de la de las puntas), **lente a la altura de las manos** (si se filma desde la línea de las puntas, subirla a
  ~1,05–1,10 m), 3–3,7 m, 1x, nivelada, paralela a la línea de tiro. Nunca detrás de la pelota. Es la única posición cómoda dentro del
  plano de la varilla: más alta aplana el swing (esconde un over the top), más baja lo empina (inventa uno), 4–16 cm a 3 m [CP].
- **De frente:** perpendicular a la línea de tiro, centrada en el medio de la postura (varilla perpendicular de guía), a la altura de las
  manos o la cadera, 3–3,7 m. **Escala con la varilla de las puntas**, nunca con la línea de la pelota (subestima ~20 %) ni con el palo.
- **Dos varillas en el piso** paralelas a la línea de tiro, medidas: dan punto de fuga (control de cámara), escala y homografía del piso.
- **Cámara lenta 240 fps, archivo original "100 % – 240 FPS"** (AirDrop, cable, Drive). Control con `ffprobe`; si es lenta horneada,
  no se mide el ritmo.
- **Cuestionario obligatorio** (salida, curva, altura, contacto con foto de la marca, divot, falla para uno o los dos lados, dolor,
  permiso). **Sin vuelo y contacto no se diagnostica el path.**
- Si hay **dolor o lesión**: derivar a un profesional de la salud; no dar ejercicios para eso.

**Mínimo para analizar** (el dueño no puede exigir todo el protocolo, 06/11/2026). Por ahora solo desde atrás:
- Un video **desde atrás**, celular fijo (trípode, o apoyado en la bolsa o una silla), en la línea de las manos y a la altura de las
  manos, 1x, cámara lenta, **archivo original**.
- **Dos palos en el piso** en lugar de varillas (no hace falta medirlos). Dan la línea de tiro y el punto de fuga.
- **Tres datos:** palo, dónde salió la pelota y cómo curvó.
- Sin varillas medidas: la escala sale del largo del palo del address (desde atrás está casi en el plano de la imagen; preguntar el palo).
  Si la cámara no pasa el control, el slot de TPI no vale y el over the top se decide con la prueba relativa.
- Lo que falte se dice en el análisis como "no evaluable con este video", nunca se supone.

## 4. Orden del diagnóstico (como trabaja un profesor)

1. **Qué hace la pelota** (lo informa el jugador).
2. **Qué tuvo que pasar en el impacto** (leyes de vuelo, sección 6).
3. **Qué cuadro del video lo explica** (checklist P1–P10: `referencias/checklist_p1_p10.md`).
4. **Qué limitación física podría estar detrás**, como hipótesis: "suele tener una causa física (por ejemplo …); un screen de TPI
   lo confirmaría". El video no diagnostica la limitación física.
5. **Una sola prioridad**, con su cadena de causa y efecto, su drill, la progresión y un **objetivo medible para el próximo video**.
   Revisar el setup (grip, pelota, postura, alineación) antes que el swing.

Nombrar las fallas con las 16 características de TPI y decidir cada una con **`referencias/fallas.md`** (criterio de video, vuelo,
causa física y drill). Marcar las 16 con **sí / no / no evaluable** y su evidencia.

**Patrones de tour que NO son fallas** (se describen; son falla solo si el impacto lo paga): codo volador · palo cruzado o laid off
en el tope · muñeca líder extendida en el tope · pelvis que sube y rodilla líder que se estira hacia el impacto · pelvis más abierta
que el tórax en el impacto · traslado hacia el objetivo (pelvis 6–14 cm adelante en el impacto con hierros [FAB]) · cabeza que se
mueve unos cm · levantarse después del impacto.

Reglas rápidas de fase y dirección (TPI):
- **Early extension** = la pelvis **avanza hacia la pelota** respecto de su línea del address (vertical tangente a la nalga en P1,
  desde atrás). Que suba no cuenta. Se informa graduada ("en P7 la nalga queda X cm por delante de su línea, ±1–3 cm").
- **Pérdida de postura:** solo entre P4 y P7. **Sway:** subida, alejándose del objetivo (cadera de atrás por fuera del pie de atrás y
  pelvis atrás en P4). **Slide:** bajada, cadera líder pasa su vertical **y** poca rotación. **Hanging back:** pelvis en el impacto en su
  posición del address o detrás (con hierros). **Forward lunge:** el tren superior se mueve más que la pelvis hacia el objetivo.

## 5. Over the top (protocolo obligatorio, nunca a ojo)

Correr **`python -I swing-analisis/tools/plano_check.py SWING3D.json POSICIONES.json --vp X,Y`** y copiar su veredicto.
| Paso | Qué se hace | Qué se concluye |
|---|---|---|
| 0. Cámara | Punto de fuga de las varillas cerca del centro; giro θ = atan(d/f) | Con más de 5° (o sin varillas), el slot no vale: solo la prueba relativa |
| 1. Slot de TPI | Línea A = varilla en P1; línea B = varilla en P3 (antebrazo líder apenas pasado la horizontal) | Cabeza por encima de B en P5–P6: over the top. Por debajo de A: debajo del plano |
| 2. Bajada contra subida (V1) | Manos de bajada contra manos de subida **a la misma altura** (mediana); varilla en P5 contra P3 | Más de ~4 cm por encima/afuera o P5 más de ~5° más empinada: over the top |
| 3. Pistas | Cabeza del palo por fuera de las manos al empezar la bajada; varilla sobre el antebrazo de atrás en P6 | Refuerzan, no deciden |
| 4. Vuelo y contacto | Pull, pull-slice o slice; divot a la izquierda; descartar talón con driver | Confirma el path de afuera hacia adentro |

**Regla asimétrica:** "over the top" si la prueba 1 o la 2 supera el margen **y** coincide una pista o el vuelo. "En plano" solo
con las dos pruebas dentro del margen y la cámara verificada; con la cámara sin verificar se dice "sin señales de over the top en la
prueba relativa". Si no, "no evaluable".
- **El tope cruzado no es falla:** la falla la define la bajada (Mickelson y Daly cruzan).
- **No todo slice es over the top:** depende de la cara respecto del path; con driver, un golpe de **talón** sale a la izquierda y
  curva a la derecha por gear effect. Antes de decir over the top por un slice con driver, pedir la marca del impacto.
- Gulgin 2014 [PR] no encontró asociación del screen de TPI con over the top: la causa física se plantea como hipótesis.

## 6. Leyes de vuelo (para inferir cara y path)

- **La cara manda la salida; la diferencia cara–path manda la curva.** La cara explica **61–76 %** de la salida según el único estudio
  publicado (PING 2018 [PR]: driver 76 %, hierro 7 69 %, wedge 61 %) y hasta ~85 % según la cifra de enseñanza de TrackMan [FAB].
  Decirlo así: "la cara controla la mayor parte de la salida, entre dos tercios y más de tres cuartos según el palo". Nunca "75 %" exacto.
- Con poco spin loft (driver) la misma diferencia cara–path curva más. 1° de diferencia a 274 m ≈ 11 m de curva [FAB].
- **El ataque mueve el path:** pegar hacia abajo lo corre a la derecha, hacia arriba a la izquierda (≈1:1 con driver, la mitad con
  hierros [INS]). "Con el driver hago slice y con los hierros no" puede ser el ataque, no otro swing.
- **Golpes descentrados** (driver): punta → sale a la derecha y curva a la izquierda; talón → sale a la izquierda y curva a la derecha.
- Inferencia del vuelo = **tendencia**, no grados. Tabla "vuelo → qué buscar en el video" en `referencias/fallas.md`.
- "Pegale hacia abajo" no es universal: el driver de tour va de −0,9° (PGA) a +2,8° (LPGA) de ataque [FAB].

## 7. Drills

- Progresión común: movilidad o ensayo sin palo ni pelota → cámara lenta con pausas en el tope y en P6 → medio swing de cintura a
  cintura → swing completo → pelota → velocidad. Se avanza solo si la señal del drill sigue bien.
- **Drills con pasos verificados:** early extension (glúteos contra pared o silla; silla adelante de Chris Como), over the top (manos al
  bolsillo de atrás / botella de agua, HackMotion), casting ("pegá fuerte, frená rápido" → "cuerpo primero" con silla), flat shoulder
  plane (palo cruzado sobre los hombros, Titleist). Detalle en `referencias/fallas.md`.
- Los drills y ejercicios de TPI (Step Change, Get Closer, Brettzel…) **se citan por el nombre, no se describen de memoria**. Lo que no
  tiene pasos verificados (pump drill, pies juntos, etc.) no se atribuye a nadie.
- Si la limitación física es probable, el plan se adapta a ella en vez de forzar un modelo.

## 8. Lenguaje

- Término castellano donde existe (plano, impacto, postura, cara, trayectoria) y el de TPI entre paréntesis la primera vez.
- **Over the top no se traduce como "por arriba"** (en la jerga local puede entenderse como pegarle arriba a la pelota): "over the top
  (bajada por afuera, de afuera hacia adentro)".
- Definir los P-números en el informe (se usan los de HackMotion: P2/P6/P8 varilla paralela, P3/P5/P9 brazo paralelo, P4 tope,
  P7 impacto, P10 final). V1 llama P6 al impacto.
- "Según TPI" para sus porcentajes (67 % de 90.000 con early extension es dato propio de TPI, sin método publicado).

## 9. Estructura del análisis (pedido del dueño, 06/11/2026) y formato del reel y del PDF

Rol: biomecánico de golf y coach de alto rendimiento. Lenguaje técnico, conciso, sin divagar. **Antes de cada fase, decir
expresamente si la información alcanza**; lo que no alcanza se marca "no evaluable con este video" y no se supone.
Ese rol es para el tono del análisis: en el reel y el PDF **nunca** se dice que lo hizo un coach del PGA Tour ni un biomecánico.

**1. Diagnóstico de posición y biomecánica** (desde atrás; entre corchetes, cómo se obtiene)
- *Postura y setup:* inclinación del tronco, flexión de rodillas, distancia a la pelota, brazos, S/C posture [medido, ±3–5°];
  alineación de pies con los palos del piso [medido]; cara del palo en el address [descripción, poco precisa desde atrás];
  distribución de peso [no se mide: no hay plataforma; solo pistas visuales].
- *Backswing y carga:* plano de la varilla en P2 (cabeza vs manos), P3 (línea B) y P4 (cruzado / laid off) [medido; P2 en escorzo];
  plano de hombros (receta TPI) y codo de atrás [medido / descripción]; giro de hombros vs caderas [**no en grados**: descripción];
  hinge de muñecas [descripción: "se ve cupped/bowed"].
- *Transición y downswing:* plano de bajada y over the top [`plano_check.py`]; lag (ángulo brazo líder–varilla en P5) [medido, ±5–10°];
  pelvis hacia la pelota (early extension), bajada y subida de la pelvis, talón de atrás, rodillas [medido, ±1–3 cm];
  secuencia cinemática y fuerzas contra el suelo [**no se miden** en 2D; a 240 fps solo el orden de algunos eventos visibles y pistas
  como la caída de la pelvis o la extensión de la rodilla líder].
- *Impacto y release:* postura en P7 contra P1 [medido]; ángulo de ataque, face-to-path, loft dinámico [**inferidos** del vuelo, el
  divot y la marca de contacto: tendencia, no grados]; punto de contacto [solo con foto de la marca]; shaft lean [**de frente**: no
  evaluable desde atrás].

**2. Error principal (causa raíz).** Una sola falla, con la cadena completa: cuadro y medida → qué pasa en el impacto (path, cara, ataque,
low point) → el vuelo que informó el jugador. Las secundarias, después y más cortas. Si la causa puede ser física, decirlo como hipótesis.

**3. Métricas** (solo con datos de TrackMan / GCQuad; si no hay, decir "sin datos de launch monitor" y dar la tendencia inferida del vuelo):
path vs cara y face-to-path (signo y tamaño de la curva) · ángulo de ataque y low point · loft dinámico y spin loft (tour: ~14,7° driver,
~24,3° hierro 6 [FAB]) · spin axis (±2 ≈ recto [FAB]). Comparar contra el propio jugador y el palo, no contra un promedio de otro sistema.

**4. Plan de corrección**
- *Sensación clave:* una sola, dicha como intención física concreta.
- *Drill:* 1 o 2, paso a paso, solo con pasos verificados (sección 7), con su progresión.
- *Chequeo sin ayuda externa:* la señal física del drill (la pared, la silla, la botella, el contacto) y el **mismo encuadre de video**
  con un objetivo medible para el próximo (ej.: "la nalga no se despega más de 3 cm de su línea en P7").

**Reel:** sin gancho ni re-gancho, análisis puro, siguiendo las 4 secciones: datos (palo, vista, vuelo informado) → swing completo a
velocidad real → recorrido P1–P10 con la medida de cada posición → error principal con su cadena → secundarias → **termina con el drill**
(pasos claros). Después, solo el cierre que pidió el dueño: el análisis va con un reporte + "Seguime para más análisis".
Voz: la misma (Kokoro `em_alex`, ×1,12). Subtítulos con alineación forzada.

**PDF:** las 4 secciones, sin la sección de método (solo una línea de "medidas aproximadas, ±margen"). Además: portada con la prioridad ·
definiciones P1–P10 · lista TPI con sí / no / no evaluable · consistencia entre swings · lo que no se mide con este video · registro de
práctica · referencias con su tipo de fuente.

**Validación sin profesor:** el dueño hace de evaluador a ciegas. Antes de ver el análisis, anota su falla principal y su prioridad.
Se comparan y se registran en `swing-analisis/validacion.md`; cada desacuerdo se discute con evidencia y, si corresponde, se vuelve regla.

## 10. Revisión final de "profesor desconfiado"

Antes de entregar, recorrer **`referencias/errores_amateur.md` fila por fila** y además:
- ¿Cada "bien" pasó todas sus pruebas? ¿El over the top salió de `plano_check.py`?
- ¿Algún patrón de tour marcado como falla? ¿Algún número que una cámara no mide?
- ¿Hay una sola prioridad y ataca la causa? ¿El drill tiene pasos verificados?
- "¿Qué me diría un profesor que mira esto cuadro a cuadro?": buscar el error en el propio análisis, no confirmarlo.

## 11. Lección aprendida (swing 2, 04/11/2026)

Se dijo "la bajada está en plano" midiendo solo el ángulo de la varilla. Era **over the top**: manos de bajada 16–19 cm por encima de su
camino de subida a la misma altura (mediana 18,7 cm, 4–5 veces el margen), varilla en P5 ≈16° más empinada que en P3, cabeza del palo
23 cm por fuera de las manos al empezar la bajada y tope cruzado. La cámara estaba girada 8,5°, así que el slot de TPI no valía, pero la
prueba relativa sí. Faltaba una regla, no precisión. `tools/plano_check.py` lo detecta solo (`run_demo/swing2/plano_check.json`).
