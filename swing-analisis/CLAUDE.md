# Análisis de swings de espectadores · Contexto para Claude

> Proyecto aparte de Valparaiso Motors: las reglas de marca de `/CLAUDE.md` (bordó, Anton, CTA del concesionario) **no** valen acá.
> Iniciado el 04/11/2026. Se asumió **golf** (confirmar con el dueño).

## Qué quiere el dueño
1. **Parámetros de filmación** para que los espectadores manden su swing bien grabado.
2. **Un reel** analizando el swing, con la **pantalla dividida**: video real con esqueleto de un lado y **personaje 3D** del otro.
3. **Un PDF completo**: qué hace bien, qué hace mal y qué hacer para cambiarlo.
4. Información **correcta, con fuente**, "no decir por decir".

## Reglas de precisión (no negociables)
- Cada diagnóstico se apoya en **un cuadro concreto** que se muestra (en el PDF y en el reel). Sin cuadro, no hay diagnóstico.
- Las medidas salen de una sola cámara de celular: son **aproximadas**. Mostrar "aprox." y dar rangos, nunca decimales de laboratorio.
  No encontramos un estudio que valide MediaPipe contra captura de movimiento en golf (búsqueda del 04/11/2026).
- El modelo 3D es **estimado** (la profundidad la adivina el modelo desde una sola cámara). Rotularlo "estimado".
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

## Proceso técnico (probado el 04/11/2026)
1. **Pose:** MediaPipe Pose Landmarker *heavy* (Google, gratis, corre en CPU). Hace falta `apt-get install libegl1 libgles2 libgl1`.
   - Modelo: `https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_heavy/float16/latest/pose_landmarker_heavy.task`
   - `python -I tools/pose_extract.py VIDEO MODELO pose.json`: en la prueba detectó el cuerpo en 264 de 264 cuadros (~20 s en CPU).
2. **Momentos y medidas:** `python -I tools/analyze.py pose.json VIDEO salida/`. Saca `metrics.json`, los cuadros clave con esqueleto y todos los cuadros dibujados. Está pensado para la toma desde atrás; falta la versión de frente.
3. **Pantalla dividida 3D:** `tools/split.html` (Three.js 0.170: maniquí armado con los puntos 3D, cámara que gira de "como el video" a "de frente") + `tools/shoot.js` (Playwright saca cada cuadro). Va en una carpeta `r3d/` con `npm install three@0.170.0`, servida con `python3 -m http.server`.
4. **Reel final:** HyperFrames (skills `hyperframes`, `threejs-*`, `embedded-captions`, `media-use`), con la voz que elija el dueño.
5. **PDF:** skill `pdf`, o HTML impreso con Playwright.

**Límites vistos en la prueba** (clip de muestra de GolfDB, licencia CC BY-NC: solo para pruebas internas, no publicar):
- el clip tenía zoom y paneo, así que la línea de referencia de la cadera no sirve: por eso la regla de "celular fijo";
- era cámara lenta, así que el ritmo medido (subida 3,5 s) no es real: por eso "archivo original".

**Pendiente:**
- versión de frente del análisis;
- personaje 3D más lindo (humanoide con huesos en vez del maniquí);
- centrar mejor la figura en la zona segura;
- diseño del reel (nombre de la cuenta, colores, voz);
- plantilla del PDF.

## Skills (búsqueda en skills.sh, 04/11/2026)
- **No existe una skill de análisis de swing de golf.** Los resultados con "swing" son de trading ("swing-review") y "golf-data" es de torneos.
- **Revisadas y descartadas para instalar:**
  - `vivixiao980/tennis-video-coach-report` (2 instalaciones): misma idea (esqueleto, cámara lenta, PDF) pero de tenis. Sirve de referencia de estructura.
  - `kinemotioninc/kinemotion` (`mediapipe-pose-detection` 82 y `video-analysis-workflow` 45, MIT): es de saltos, pero tomamos sus prácticas (suavizar los puntos, corregir izquierda/derecha cambiadas, chequear la calidad del video).
  - `jayv29/pose-analysis-skill` (1): esgrima y escalada; tomamos la idea de no puntuar si el video no sirve.
  - `move-ai-motion-capture` (108): servicio pago de captura profesional; no hace falta para esto.
- **Lo que usamos:** skills ya instaladas (hyperframes, threejs-*, embedded-captions, media-use, pdf, ffmpeg) + MediaPipe. Siguiente paso recomendado: convertir este proceso en una skill propia `analisis-swing`.
