# Análisis de swings de espectadores · Contexto para Claude

> Proyecto aparte de Valparaiso Motors: las reglas de marca de `/CLAUDE.md` (bordó, Anton, CTA del concesionario) **no** valen acá.
> Iniciado el 04/11/2026. Se asumió **golf** (confirmar con el dueño).

## Qué quiere el dueño
1. **Parámetros de filmación** para que los espectadores manden su swing bien grabado.
2. **Un reel** analizando el swing "como un instructor profesional": qué hace bien, qué hace mal y cómo mejorarlo.
3. **Un PDF completo**: qué hace bien, qué hace mal y qué hacer para cambiarlo.
4. Información **correcta, con fuente**, "no decir por decir".
5. **Decisión del 04/11/2026: sin modelo 3D.** Se probó un maniquí 3D y el dueño pidió sacarlo y enfocarse en la calidad del análisis y en mejorar el swing.
6. **Es un producto pago.** Tiene que parecer un análisis "de otro nivel", no uno genérico de IA: máxima calidad, profesionalismo y visuales.

## Pedidos del dueño (04/11/2026, después del swing 2) — los más recientes mandan
- **Usar la skill `analisis-swing`** (`.claude/skills/analisis-swing/SKILL.md`): protocolo de filmación, checklist técnico,
  postura crítica y formato. El análisis lo van a evaluar **profesores de golf**: no puede haber errores técnicos.
- **Mucho más técnico y preciso.** Pedir siempre el video **desde atrás y de frente** con el protocolo de la skill antes de analizar.
- **Criticar al jugador sin sesgo positivo.** No suavizar ni empezar por lo bueno para quedar bien.
- **Reel:** análisis puro, **sin gancho ni re-gancho**, y **termina con un drill** (después, solo el cierre breve de reporte + "Seguime").
- **Error del swing 2:** el reel y el informe dijeron "la bajada está en plano" y era **over the top** (manos 14–23 cm por encima de
  su camino de subida, varilla en P5 14° más empinada que en P3, tope cruzado). No publicar esos archivos.

## Pedidos del dueño (04/11/2026, después del primer reel) — valen para todos los análisis
- **Voz:** dejarla como está (Kokoro `em_alex`, `--lang es`, acelerada ×1,12). No cambiarla sin que lo pida.
- **Cierre del reel:** antes del final decir que el análisis va acompañado de un reporte (ej.: "Este análisis va acompañado
  de un reporte completo, con todos los números y el plan de práctica") y terminar con **"Seguime para más análisis"**.
- **Subtítulos sincronizados con la voz:** los tiempos de Whisper llegan ~0,2 s antes. Usar alineación forzada
  (`tools/align_captions.py`, modelo MMS_FA de torchaudio, en un venv con `torch==2.9.1 torchaudio==2.9.1` CPU).
- **Analizar varias cosas, no solo lo peor:** lo que hace bien (con datos) + 2 o 3 puntos a mejorar en orden de prioridad,
  con la secuencia de causa y efecto, y el plan. Preciso, y largo si hace falta (el reel del swing 2 dura 98 s).
- **PDF sin la sección "cómo se hizo el análisis".** Solo una línea de "medidas aproximadas" y las referencias al final.
- **Cámara lenta del iPhone:** los videos vienen con la cámara lenta "horneada" (normal → lento → normal). Detectarla por el
  movimiento por cuadro y no medir el ritmo. Igual suma cuadros alrededor del impacto.

## Estándar del producto pago
- **Estructura de profesional:** las 10 posiciones P1–P10, evaluación fundamento por fundamento (bien / mejorar / prioridad / no evaluado),
  **una sola prioridad** con su **secuencia de causa y efecto** sacada de los datos (ej.: "entre P4 y P5 la cadera avanza 3,3 cm; entre P5 y P7 pierde 7°").
- **Específico de ese swing:** cada frase con su número y su cuadro. Nada que sirva para cualquier golfista.
- **Plan que cambia el juego:** sensaciones, ejercicios con progresión de 3 semanas (sin pelota → medio swing → completo), objetivos medibles
  para el próximo video (marcados como objetivos de práctica, no como normas) y control antes/después.
- **Visuales:** video mejorado (superresolución si es chico), contorno del address sobre el impacto, P1 vs P7 lado a lado, zoom a la zona clave,
  datos en vivo, barra P1–P10, silla del ejercicio dibujada sobre el video. Subtítulos palabra por palabra.
- **Verificar cada dato mirando el video** antes de decirlo. Ejemplo de la prueba: el modelo decía que despegaban los dos talones y en el video
  solo despegaba el de atrás; y las manos más altas en el impacto son normales, así que no se mostraron como falla.

## Reglas de precisión (no negociables)
- Cada diagnóstico se apoya en **un cuadro concreto** que se muestra (en el PDF y en el reel). Sin cuadro, no hay diagnóstico.
- Las medidas salen de una sola cámara de celular: son **aproximadas**. Mostrar "aprox." y dar rangos, nunca decimales de laboratorio.
  No encontramos un estudio que valide MediaPipe contra captura de movimiento en golf (búsqueda del 04/11/2026).
- La pose **no ve el palo ni la cara del palo**. Lo que hace la pelota se le pregunta al espectador (dónde sale y cómo curva) y se explica con las leyes de vuelo (abajo).
- Nombrar las fallas con las **definiciones de TPI** (abajo). No inventar nombres ni porcentajes.
- Máximo **2–3 cambios prioritarios** por swing, del más importante al menos. Cada uno con un ejercicio.
- Si el espectador menciona **dolor o lesión**: recomendar ver a un profesional de salud; no dar ejercicios para eso.
- Si el video no sirve (cámara movida, cuerpo cortado, borroso), **no se analiza**: se pide otro con lo que falló.
- **Permiso por escrito** del espectador para publicar su swing. Si es menor, del padre, madre o tutor.

## Guía de filmación (para los espectadores)
Fuente principal: The Sand Trap, "Recording Your Golf Swing" (thesandtrap.com/b/playing_tips/filming_your_swing, act. 08/2024).
Complemento: V1 Golf (6–10 ft de frente, 8–12 ft desde atrás). Lo de "fijo, sin zoom" y "archivo original" sale de nuestra prueba.

**Dos tomas** (de frente y desde atrás), 2 o 3 swings en cada una:
- **De frente:** celular a la **altura de las manos** (cadera, apenas debajo del ombligo), mirando perpendicular a la línea de tiro y **centrado en el medio de los pies**, a **2 a 3,5 m de la pelota**. Truco: una varilla en el piso, perpendicular a la línea de tiro, en el medio de la postura; el celular sobre esa línea.
- **Desde atrás (down the line):** a la **altura de las manos**, apuntando **paralelo a la línea de tiro**, a la altura de los **dedos del pie de atrás**, a **2,5 a 3,5 m de la pelota**. Truco: varilla delante de los pies, paralela a la línea; el celular justo por dentro de la línea de la varilla. No filmar desde atrás de la pelota.
- **En las dos:**
  - celular **fijo** (trípode o soporte), **sin zoom y sin seguir al jugador**;
  - cuerpo entero, palo y pelota en cuadro todo el swing, con espacio arriba de la cabeza (para el palo en el tope) y debajo de la pelota;
  - **vertical**, lente normal **1x** (no el gran angular 0,5x, que deforma);
  - **60 fps como mínimo**; 120 o 240 fps mejor;
  - **de día**, con buena luz y sin contraluz, para que el palo no salga borroso;
  - ropa ajustada que contraste con el fondo;
  - empezar a grabar 2–3 s antes y cortar 2 s después del final;
  - mandar el **archivo original** (Drive, mail o WhatsApp "como documento"), **sin cámara lenta editada ni filtros**.
- **Datos que tiene que mandar:** diestro o zurdo, palo, adónde apuntaba, **dónde salió la pelota y cómo curvó**, qué quiere mejorar, nivel o hándicap, si tiene dolor o lesión, y el permiso para publicar.

## Base de conocimiento (con fuente)
- **Características de swing de TPI** (mytpi.com/improve-my-game/swing-characteristics, leído el 04/11/2026). Son 16:
  S-Posture, C-Posture, Loss of Posture, Flat Shoulder Plane, Flying Elbow, Early Extension, Over the Top, Sway, Slide, Late Buckle, Reverse Spine Angle, Forward Lunge, Hanging Back, Casting, Scooping, Chicken Winging.
  - Early Extension (TPI): "cualquier movimiento de la pelvis hacia la pelota en la subida o la bajada". Según TPI, 67 % de 90.000 golfistas evaluados la tienen (dato propio de TPI).
  - Sway: movimiento lateral excesivo del tren inferior **alejándose** del objetivo en la subida. Slide: lo mismo **hacia** el objetivo en la bajada.
- **Vuelo de la pelota** (Titleist Learning Lab, "Physics of ball striking"): la **cara** define la mayor parte de la dirección de salida (≈75 % en hierros medios, ≈85 % en driver) y la diferencia **cara–trayectoria** define la curva. "La cara la manda, el path la curva." Son valores aproximados y cambian con golpes fuera del centro.
- **Qué se puede medir con la pose (aprox.)**: inclinación del tronco, movimiento de cabeza, cadera hacia la pelota (early extension), sway y slide, flexión de rodillas, brazo adelantado en el tope, momentos del swing (address, tope, impacto, final) y ritmo subida/bajada (solo con video a velocidad real).
- **Qué NO**: cara del palo, path en grados, velocidad del palo o de la pelota, distancia, spin.

## Proceso técnico v2 (probado el 04/11/2026, toma desde atrás)
Entorno: venv con `mediapipe opencv-python-headless numpy scipy`; `apt-get install libegl1 libgles2 libgl1`;
carpeta `r3d/` con `npm install three@0.170.0`, servida con `python3 -m http.server 8765` desde la carpeta de trabajo.
1. **Pose + silueta:** `python -I tools/pose_extract.py VIDEO pose_landmarker_heavy.task pose.npz`
   (modelo: `https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_heavy/float16/latest/pose_landmarker_heavy.task`).
2. **Compensar la cámara** con el fondo: `tools/stabilize.py VIDEO pose.npz CUADRO_ADDRESS stab.npz`. Las líneas quedan pegadas al piso.
3. **Palo y pelota:** `tools/club_detect.py` (automático + correcciones a mano en JSON). La punta del palo se marca a ojo en ~20 cuadros clave
   (hojas con grilla: ver `run_demo/`) con su profundidad con signo (+ hacia la cámara). El impacto se confirma mirando cuándo desaparece la pelota.
4. **Datos 2D suavizados:** `tools/build3d.py` → `swing3d.json` (puntos del cuerpo estabilizados `p2`, palo `h2`/`g2`, momentos). El nombre quedó
   de la prueba 3D; el 3D ya no se usa, pero este archivo sí.
5. **Medidas:** `tools/metrics.py` (línea de cola con la silueta, columna, plano) y `tools/frame_metrics.py` (datos por cuadro y P1–P10 en
   `run_demo/posiciones.json`; P3/P5/P9 = muñeca a la altura del hombro, P2/P6/P8 = palo paralelo, P7 = la pelota desaparece).
6. **Superresolución** (solo si el video es chico): `tools/upscale.py` con `realesr-general-x4v3.pth` (Real-ESRGAN, ~4 s por cuadro en CPU, necesita torch).
7. **Panel del video:** `tools/render_v3.py` (760x1030, dibuja a 2x). Capas: esqueleto, contorno del address, hueco de la cadera, línea de cola,
   columna, plano, recorrido del palo, cabeza, ángulo de rodilla, talón, objetivo, silla. Modos: vista con zoom y comparación P1 | P7.
   La edición va en `run_demo/timeline_v3.py`, con tiempos sacados de las palabras de la voz.
8. **Voz:** guion en `run_demo/guion.json` (texto para la voz y texto para subtítulos por separado; texto limpio en `guion_voz.txt`).
   Prueba: Kokoro local (`hyperframes tts`, voz `em_alex`, `--lang es`, con `HYPERFRAMES_PYTHON` apuntando a un venv con `kokoro-onnx soundfile`),
   acelerada ×1,12 con rubberband. **Para el producto pago: la voz de ElevenLabs del dueño** (Kokoro suena neutro/español, no rioplatense).
   Tiempos por palabra: `hyperframes transcribe voz.wav -m small -l es`. Subtítulos: `tools/captions.py` (1–4 palabras, ≤20 letras).
9. **Composición:** `tools/reel_v3.html` (títulos, barra P1–P10, datos en vivo, subtítulos, tarjetas) + `tools/shoot_reel.js` (1080x1920, 30 fps).
   Audio: `tools/mix.py` (voz > efectos > música con ducking; cues en `run_demo/cues.json`) y loudnorm a −14 LUFS / −1 dBTP.
   Sonidos: Kenney (CC0) desde `series-ai/jam-ready-assets` (archivos LFS por `media.githubusercontent.com`).
**Videos HD (como el swing 2):** `tools/render_v4.py` con `cfg.json` (`up_scale: 1`, `src_w/src_h`, `unit` ≈ altura del cuerpo en px / 320,
`vp` = punto de fuga de la línea de tiro, `labels` configurables) y `tools/reel_s2.html`. Grillas para marcar el palo: `tools/grid_hd.py`.
Ejemplo completo en `run_demo/swing2/` (guion, posiciones, marcas del palo, edición, sonidos, informe).
10. **PDF:** `run_demo/informe_v3.html` (6 páginas: portada con prioridad y KPIs, P1–P10, evaluación, diagnóstico con secuencia, la clave y la silla,
    plan de 3 semanas con registro, método y fuentes) impreso con `tools/print_pdf.js`.

**Límites vistos en la prueba** (clip de muestra de GolfDB, licencia CC BY-NC: solo para pruebas internas, no publicar):
- el clip tenía paneo leve (~11 px): se compensó con el fondo;
- era cámara lenta: el ritmo medido no es real. Por eso pedir el archivo original;
- la varilla se pierde cuando pasa delante del cuerpo o sale borrosa: hay que marcarla a mano en los cuadros clave.

**Pendiente:**
- probar con un video real HD de un espectador (dos tomas) y sumar la versión de frente (sway, slide, posición de pelota, palo en el impacto);
- pedirle al espectador el vuelo de la pelota para conectar el diagnóstico con su error;
- convertir este proceso en una skill propia `analisis-swing`;
- nombre de la cuenta, logo, colores y voz definitivos (ElevenLabs del dueño) para el producto.

## Skills (búsqueda en skills.sh, 04/11/2026)
- **No existe una skill de análisis de swing de golf.** Los resultados con "swing" son de trading ("swing-review") y "golf-data" es de torneos.
- **Revisadas y descartadas para instalar:**
  - `vivixiao980/tennis-video-coach-report` (2 instalaciones): misma idea (esqueleto, cámara lenta, PDF) pero de tenis. Sirve de referencia de estructura.
  - `kinemotioninc/kinemotion` (`mediapipe-pose-detection` 82 y `video-analysis-workflow` 45, MIT): es de saltos, pero tomamos sus prácticas (suavizar los puntos, corregir izquierda/derecha cambiadas, chequear la calidad del video).
  - `jayv29/pose-analysis-skill` (1): esgrima y escalada; tomamos la idea de no puntuar si el video no sirve.
  - `move-ai-motion-capture` (108): servicio pago de captura profesional; no hace falta para esto.
- **Lo que usamos:** skills ya instaladas (hyperframes, threejs-*, embedded-captions, media-use, pdf, ffmpeg) + MediaPipe. Siguiente paso recomendado: convertir este proceso en una skill propia `analisis-swing`.
