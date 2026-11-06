# Precisión real de la estimación de pose sin marcadores en el swing de golf, y mejores modelos (cuerpo, palo, eventos)

> Notas de investigación (04/11/2026). Etiquetas de evidencia: **[REVISADO POR PARES]**, **[PREPRINT]** (sin revisión), **[FABRICANTE]** (marketing o informe propio de la empresa), **[AUTODECLARADO]** (README de GitHub o blog). Las licencias se leyeron en el archivo LICENSE de cada repositorio el 04/11/2026.
> Contexto del proyecto: `swing-analisis/tools/pose_extract.py` usa hoy **MediaPipe Pose Landmarker heavy**, y `club_detect.py` detecta el palo con visión clásica (OpenCV), sin modelo entrenado.

## 1. Validación de Sportsbox AI (3D con un solo video de celular) contra captura de movimiento

### Takeaway
La única validación de Sportsbox es un informe de la propia empresa, sin revisión por pares: ~2° de error angular y ~0,4 pulgadas (~1 cm) de error lineal contra el sistema electromagnético AMM3D, en solo 30 swings, solo en address, tope e impacto, y con pocos de sus más de 200 indicadores. No encontré ninguna validación independiente revisada por pares.

### Cited Findings
- **[FABRICANTE]** Referencia: AMM3D, sistema de captura con sensores electromagnéticos, que Sportsbox llama "uno de los estándares de oro" en biomecánica de golf. El estudio lo hizo el Dr. Phil Cheetham, jefe de Ciencias del Deporte de Sportsbox AI. — [Sportsbox AI Accuracy](https://help.sportsbox.ai/sportsbox-ai-accuracy)
- **[FABRICANTE]** Muestra: 30 golfistas, 1 swing cada uno, grabados a la vez con los dos sistemas. Mezcla de amateurs y profesionales, hierro 7 y driver, adentro y afuera. — [Sportsbox AI Accuracy](https://help.sportsbox.ai/sportsbox-ai-accuracy)
- **[FABRICANTE]** Parámetros:
  - angulares: giro del pecho, giro de la pelvis, inclinación lateral del pecho y de la pelvis, inclinación hacia adelante del pecho;
  - lineales: sway y lift del pecho y de la pelvis (solo en tope e impacto).
  — [Sportsbox AI Accuracy](https://help.sportsbox.ai/sportsbox-ai-accuracy)
- **[FABRICANTE]** Error absoluto medio, con todos los parámetros juntos:
  - angular: **2,2° en address, 2,5° en el tope y 2,0° en impacto** ("aproximadamente 2 grados");
  - lineal: **0,6 pulgadas en el tope y 0,2 pulgadas en impacto, 0,4 pulgadas combinado** (≈1,5 cm, 0,5 cm y 1 cm).
  - La tabla por parámetro (Tabla 2) está publicada solo como imagen. No hay correlaciones ni límites de acuerdo.
  — [Sportsbox AI Accuracy](https://help.sportsbox.ai/sportsbox-ai-accuracy)
- **[FABRICANTE]** Condiciones de la prueba:
  - cámaras y transmisor perpendiculares a la línea de objetivo, obturador rápido contra el desenfoque;
  - la precisión "depende de buenas prácticas": ubicación de la cámara, exposición, fps, fondo y luz;
  - no informan fps;
  - solo se validaron "unos pocos" de los más de 200 indicadores.
  — [Sportsbox AI Accuracy](https://help.sportsbox.ai/sportsbox-ai-accuracy)
- **[ANECDÓTICO]** Usuarios de un foro dicen que la luz influye en que la app funcione y que, para clases, no rindió más que un video de frente y uno desde atrás. — [MyGolfSpy forum](https://forum.mygolfspy.com/topic/53138-sportsbox-3d/)
- **[FABRICANTE, competidor]** Onform dice que validó su 3D con 190 swings contra OptiTrack (prueba interna) y con Polhemus, Qualisys y Gears (pruebas externas). En la página no da ningún número de error: remite a un "Model Card" en PDF.
  - Como ejemplo ilustrativo, cuenta que dos apps sin nombre midieron 101° y 114° de rotación del torso en el mismo swing (13° de diferencia). No es un resultado medido.
  — [Onform blog](https://onform.com/blog/3d-golf-swing-analysis-accuracy/)

### Inferences
- El "~2°" de Sportsbox está medido en las condiciones ideales del fabricante: posiciones estáticas clave, cámara perpendicular, obturador rápido y una referencia (AMM3D) que también tiene error propio. No sirve como margen general para cualquier video de un seguidor.
- La evidencia independiente de otros sistemas 3D sin marcadores, incluso con varias cámaras, está en 4–10° (secciones 2 y 5). Por eso ±2° para rotaciones medidas con una sola cámara es probablemente optimista fuera de esas condiciones.
- Para el producto: si citamos a Sportsbox, decir "según el fabricante (no revisado por pares)".

### Gaps
- No hay valores por parámetro en texto: la Tabla 2 es una imagen y no se pudo leer.
- No se encontró ningún estudio independiente de Sportsbox en PubMed ni en la búsqueda web general. No consulté Scholar con acceso pago.
- No se sabe con qué fps ni con qué modelo de iPhone se hizo la validación.

## 2. Validación de modelos 2D (MediaPipe/BlazePose, OpenPose, RTMPose, ViTPose, HRNet, AlphaPose) para ángulos en deporte y golf

### Takeaway
No hay validación revisada por pares de estos modelos para ángulos articulares en el swing de golf contra captura con marcadores. En movimientos lentos o en el plano de la cámara, los errores típicos son de 2–5°. En gestos deportivos rápidos, con oclusión o fuera del plano, suben a 10–40°, y aparecen cambios de lado izquierdo/derecho y saltos de puntos. El único trabajo de golf con video 2D validado contra Vicon midió el ángulo de la varilla (no articulaciones) con digitalización manual a 240 fps: no hubo diferencias significativas en las posiciones clave.

### Cited Findings
- **[REVISADO POR PARES] Golf, video 2D contra Vicon** (Hunter et al., Sci Rep 2022):
  - Montaje: 12 golfistas, hierro 7, una cámara de frente a 240 Hz con obturador de 1/2000 s, 4 m de distancia y 1 m de altura. Referencia: Vicon de 8 cámaras a 240 Hz.
  - Software: Kinovea, SiliconCoach Pro y SiliconCoach Live, con digitalización manual.
  - Tiempo del swing: 1,95–1,99 s con video contra 1,97 s con Vicon, sin diferencias (P = 0,763).
  - Ángulo de la varilla: sin diferencias significativas en address, tope, impacto y final. Medición típica (SM) de ≈3,2° en el tope y ≈0,6–1,4° en impacto, pero ≈19–20° en el final.
  - En address hubo un sesgo proporcional significativo (Vicon contra Kinovea).
  - Los autores recomiendan obturadores más rápidos para evitar la estela.
  — [Hunter et al. 2022, PMC9385988](https://pmc.ncbi.nlm.nih.gov/articles/PMC9385988/)
- **[REVISADO POR PARES] Golf con HRNet en una cámara, sin comparar con marcadores** (Frontiers 2023):
  - Montaje: HRNet-w48 (17 puntos) para el cuerpo y DeepLabCut (ResNet-50) para la cabeza del palo. Una cámara a 240 Hz, desde atrás a 3,5 m. 27 golfistas, 20 tiros cada uno.
  - Los autores dicen que la precisión "requerirá experimentos futuros" contra captura 3D y que el 2D es "inferior en precisión" a un análisis 3D.
  - En las pruebas preliminares, la estimación de la cabeza del palo cerca del impacto empeoraba.
  - El artículo tiene inconsistencias: intervalos de confianza que no coinciden con los r informados.
  — [Frontiers 2023, PMC10684732](https://pmc.ncbi.nlm.nih.gov/articles/PMC10684732/)
- **[REVISADO POR PARES] Deporte rápido (pase largo de fútbol) contra Xsens:**
  - Modelos: MediaPipe Pose heavy, DWPose-l y YOLOv11x-pose, con 2 iPhones a 60 Hz.
  - RMSE de **9,88° a 39,92°** según articulación y modelo. Rodilla derecha: MediaPipe 21,51°, DWPose 21,15°. Rodilla izquierda: MediaPipe 11,57°, DWPose 13,21°.
  - Conclusión de los autores: ninguno sirve para medir con alta precisión en el campo.
  - Causas citadas: oclusión del codo por el tronco, piernas superpuestas y "jitter" de los puntos en los movimientos explosivos. YOLO-Pose se desviaba más en muñecas y tobillos.
  — [PMC13306328](https://pmc.ncbi.nlm.nih.gov/articles/PMC13306328/)
- **[REVISADO POR PARES] Centros articulares 3D con 9 cámaras a 200 Hz contra Qualisys** (Needham et al. 2021):
  - OpenPose y AlphaPose: **14–48 mm** según articulación y tarea. DeepLabCut: hasta 58 mm en la rodilla al correr.
  - Cadera y rodilla tienen un sesgo sistemático de ~30–50 mm, probablemente por cómo se etiquetaron esas articulaciones en los datos de entrenamiento.
  - En todos los métodos aparecen falsos positivos, fallas de seguimiento y **cambios erróneos de miembro (izquierda/derecha)**.
  — [Needham et al. 2021, PMC8526586](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8526586/)
- **[REVISADO POR PARES] BlazePose al correr al aire libre** (cadera, rodilla y tobillo en eventos de la marcha): MAE 2,11°, RMSE 2,63°. Ojo: la referencia fue anotación manual en Kinovea, no captura con marcadores. — [Biomed Hum Kinet 2025](https://reference-global.com/article/10.2478/bhk-2025-0002)
- **[PREPRINT] MediaPipe heavy, rodilla con una cámara:** en estático, la precisión depende del ángulo (RMSE 15,49°). En las tareas dinámicas de flexión, la validez fue mejor. — [JMIR Preprints 102399](https://preprints.jmir.org/preprint/102399)
- **[REVISADO POR PARES] Béisbol, lanzamiento con una cámara (pitchAI) contra marcadores:** sesgo por ángulo de **−11,31° a +12,01°**, según el resumen. — [Sports Biomechanics 2022](https://www.tandfonline.com/doi/abs/10.1080/14763141.2022.2137425)
- **Brazo con 8 cámaras contra infrarrojo:** error medio menor a 10° en 34 ángulos, pero mayor a 10° en la abducción máxima del hombro. Visto solo como resumen en ResearchGate. — [ResearchGate 380981971](https://www.researchgate.net/publication/380981971_Validation_of_Upper_Extremity_Kinematics_using_Markerless_Motion_Capture)
- **Precisión 2D en benchmarks** (no son ángulos):
  - RTMPose-m: 75,8 AP en COCO.
  - GolfPose (ajustado con datos de golf): ViTPose-H 0,887 AP en golfista; HRNet-w48 0,884 AP.
  — [RTMPose README](https://github.com/open-mmlab/mmpose/tree/main/projects/rtmpose); [GolfPose GitHub](https://github.com/MingHanLee/GolfPose)

### Inferences
- Para un swing filmado con celular conviene separar dos casos:
  - **Ángulos en el plano de la imagen**, con la cámara perpendicular: inclinación del tronco desde atrás, ángulo de la varilla, flexión de rodilla desde atrás, inclinación lateral de frente. Con fps altos y obturador rápido, se puede sostener un error de **±3–5°** en P1, P4 y P7 (Hunter 2022 y los resultados de 2–3° en tareas lentas).
  - **Ángulos fuera del plano** (giro de pelvis y pecho, X-factor) con una sola cámara 2D: no se pueden medir de forma válida. Solo se pueden aproximar con modelos 3D, con márgenes de ±10° o más.
- En los cuadros de mayor velocidad (P5–P7) hay que esperar el peor error: desenfoque, brazos superpuestos al tronco desde atrás y cambios de lado entre manos y muñecas. Eso coincide con la caída de precisión cerca del impacto en Frontiers 2023 y con los cambios de miembro de Needham 2021.
- MediaPipe heavy (lo que usa el proyecto) no tiene ventaja demostrada sobre DWPose o RTMPose en deporte rápido: en el estudio de fútbol los tres rindieron parecido y mal.

### Gaps
- No hay estudio que compare RTMPose, ViTPose o HRNet contra marcadores **en el swing de golf**.
- No encontré números de desenfoque (por ejemplo, error según la velocidad de obturación) para el palo ni para las muñecas en golf.
- Los resultados de MediaPipe en halterofilia (hasta 13,6°) salieron solo en resúmenes de búsqueda y no pude atribuirlos a una fuente concreta: no se usan.

## 3. Datos y modelos específicos de golf (GolfPose, GolfDB/SwingNet, detección del palo) y sus licencias

### Takeaway
- **GolfPose** (ICPR 2024) tiene puntos del palo y licencia que **permite usar comercialmente los modelos entrenados**, pero el dataset se pide por email y no se puede redistribuir.
- **GolfDB/SwingNet** es la base para detectar los 8 eventos del swing. Su código es **CC BY-NC 4.0 (no comercial)**: para un producto pago hay que reimplementarlo y entrenarlo de nuevo, y la licencia de los videos de YouTube no está clara.
- Para el palo, lo único listo es **swingtrace** (YOLO11m, AGPL-3.0). Detecta la cabeza en 71,6 % de los cuadros y la cabeza o la varilla en 93,4 %.

### Cited Findings
- **GolfPose** (Lee et al., ICPR 2024):
  - Dataset GolfSwing 2D y 3D con poses del golfista y del palo. Ajusta HRNet, ViTPose, DEKR y MixSTE.
  — [ACM DL / Springer ICPR 2024](https://dl.acm.org/doi/abs/10.1007/978-3-031-78305-0_25); [GitHub](https://github.com/MingHanLee/GolfPose)
  - Configuración golfista + palo: 22 puntos (17 del cuerpo + 5 del palo). — [Notas de reproducibilidad RRPR 2024](https://rrpr2024.sciencesconf.org/data/RRPR_2024_paper_17.pdf)
  - AP 2D (todo del README oficial): golfista 0,884 (HRNet-w48), 0,887 (ViTPose-H), 0,869 (DEKR); palo 0,857, 0,870, 0,858; golfista + palo 0,915, 0,925, 0,942. Detector YOLOX-s de 1 clase: AP 0,984. — [GitHub GolfPose](https://github.com/MingHanLee/GolfPose)
  - MPJPE 3D (GolfPose-3D): **35,6 mm (17+0), 30,7 mm (17+1) y 39,2 mm (17+5)**. — [GitHub GolfPose](https://github.com/MingHanLee/GolfPose)
  - Un trabajo posterior dice que GolfPose bajó el error 3D del golfista de 109,4 mm a 35,6 mm, con anotaciones 3D derivadas de Vicon. — [arXiv 2606.22876](https://arxiv.org/html/2606.22876)
  - **Licencia:** EULA propia del dataset. Permite I+D interno, entrenar modelos y "integrar los modelos entrenados en productos o servicios comerciales". Prohíbe redistribuir o revender el dataset, reidentificar personas y sugerir aval de los autores. Exige citar. El acceso se pide por email (mhlee.cs09@nycu.edu.tw). — [GolfPose LICENSE](https://github.com/MingHanLee/GolfPose/blob/main/LICENSE)
  - El código usa MMDetection y MMPose (Apache-2.0); el 3D se basa en MixSTE. — [GitHub GolfPose](https://github.com/MingHanLee/GolfPose); [MMPose LICENSE](https://github.com/open-mmlab/mmpose/blob/main/LICENSE)
- **GolfDB / SwingNet** (McNally et al., CVPRW 2019):
  - **Datos:** 1400 videos (de 580 videos de YouTube), mitad en tiempo real a 30 fps y mitad en cámara lenta (≈195 mil cuadros cada grupo).
  - **Los 8 eventos:** Address, Toe-up, Mid-backswing, Top, Mid-downswing, Impact, Mid-follow-through y Finish.
  - **Métrica (PCE):** porcentaje de eventos correctos dentro de una tolerancia δ = max(redondeo(n/f), 1), con n = cuadros de address a impacto. En videos a 30 fps, δ ≈ 1 cuadro, porque de address a impacto pasa ≈1 s.
  - **Resultado:** **PCE 76,1 %** en promedio. Por evento: A 31,7, TU 84,2, MB 88,7, **T 83,9**, MD 98,1, **I 98,4**, MFT 97,6, F 26,5. Sin contar Address y Finish: **91,8 %**. En tiempo real 79,2 % y en cámara lenta 72,5 %; en cámara lenta el Top es más difícil.
  - **Modelo y velocidad:** MobileNetV2 + LSTM bidireccional, entrada de 160 px, 5,38 M parámetros, **10,6 ms por cuadro en un CPU Intel i7-8700K**.
  — [GolfDB arXiv 1903.06528](https://arxiv.org/abs/1903.06528)
  - **Licencia del código:** CC BY-NC 4.0 (no comercial). El repositorio no dice la licencia del dataset; los videos vienen de YouTube. El modelo publicado da PCE 0,715 sin aumentación de datos. — [GitHub golfdb](https://github.com/wmcnally/golfdb)
- **swingtrace / golf-club-tracking** (nishsm) **[AUTODECLARADO]**:
  - YOLO11m ajustado con el dataset "golf-club-tracking" de Roboflow (CC BY 4.0), con 3 clases: varilla, cabeza y manos.
  - En 7 videos de celular no vistos (3018 cuadros): **cabeza detectada en 71,6 % de los cuadros; cabeza o varilla en 93,4 %**. En un simulador hubo un hueco de 40 cuadros sin cabeza.
  - mAP@50 de validación 0,918. El autor lo toma como un techo, porque el 91 % de los cuadros de validación tiene un casi duplicado en el entrenamiento.
  - Cuando falta la cabeza, la deduce de la esquina de la caja de la varilla. Ese truco falla con la varilla casi vertical u horizontal.
  - **Licencia AGPL-3.0**, heredada de Ultralytics.
  — [GitHub swingtrace](https://github.com/nishsm/swingtrace); [Ultralytics LICENSE (AGPL-3.0)](https://github.com/ultralytics/ultralytics/blob/main/LICENSE)
- **Trabajo clásico:** seguimiento de la cabeza del palo en video de frente, detectando bordes rectos paralelos para encontrar las posiciones posibles de la varilla (Gehrig et al., BMVC 2003). — [Gehrig et al. 2003](https://www.commsp.ee.ic.ac.uk/~ng1/pdf/gehrig-et-al-bmvc03.pdf)
- **DeepLabCut** para la cabeza del palo: 27 videos, 30 cuadros anotados por video. Pierde precisión cerca del impacto. — [Frontiers 2023, PMC10684732](https://pmc.ncbi.nlm.nih.gov/articles/PMC10684732/)
- **Pose2Par** (MMPose + OpenSim para golf) **[AUTODECLARADO]**: según el resumen de búsqueda, su tabla propia califica como confiables la pelvis y el X-factor en el tope, y como no confiables la velocidad angular y la inclinación sagital. No está verificado. — [GitHub Pose2Par](https://github.com/cavanaulton/Pose2Par)

### Inferences
- **Para un producto pago, lo mejor en licencias es:**
  - pose del cuerpo con RTMPose (Apache-2.0);
  - opcionalmente, ajuste con GolfPose (la EULA permite comercializar modelos entrenados);
  - SwingNet **reentrenado desde cero con código propio**: la arquitectura está publicada y el código es NC. Antes hay que revisar si GolfDB, que son videos de YouTube, se puede usar comercialmente.
- swingtrace sirve para prototipar. Pero AGPL-3.0 obliga a publicar el código del servicio, o a comprarle a Ultralytics una licencia Enterprise. Alternativa con licencia permisiva: entrenar un detector o un modelo de puntos del palo con RTMDet o RTMPose (Apache-2.0) sobre el dataset de Roboflow (CC BY 4.0, exige atribución).
- Para el palo, la cabeza es lo que falla justo en P6–P8 (desenfoque). La **varilla** (dos puntos: manos y un punto intermedio) es más robusta para medir planos y ángulos de la varilla en P2, P3, P5 y P6.
- Tiempos de eventos: Impact y Mid-downswing salen confiables (≈98 %), Top razonable (≈84 %) y Address/Finish poco confiables (≈30 %). En el producto, el address conviene fijarlo con una regla (primer movimiento de las manos o de la cabeza del palo) y no con el modelo.

### Gaps
- No se leyó el texto completo del paper de GolfPose: no sé con qué fps ni en qué condiciones se grabó GolfSwing (interior o exterior, cámaras), ni la precisión del palo en mm.
- No hay un benchmark público, con licencia comercial, de puntos de la varilla en video de celular a 30, 60 o 240 fps.
- No se sabe la licencia de los videos de GolfDB.

## 4. Pasar a 3D con una sola cámara (MotionBERT, VideoPose3D, WHAM, 4DHumans/HMR2, SMPL): MPJPE y licencias

### Takeaway
Los mejores modelos 3D con una sola cámara tienen 36–58 mm de error medio por articulación en benchmarks (3DPW, Human3.6M), es decir, ~4–6 cm sin alinear. Están medidos con movimientos cotidianos y lentos, no con un swing. En golf, ajustar con datos de golf (GolfPose-3D) llega a 31–39 mm en su propio conjunto. Varias licencias bloquean el uso pago: todo lo basado en SMPL es no comercial salvo licencia de Meshcapade, y VideoPose3D es CC BY-NC.

### Cited Findings
- **MotionBERT:** MPJPE en Human3.6M de **39,2 mm** desde cero y **37,2 mm** ajustado, con 2D detectado. Error de malla en 3DPW: 88,1 mm (MPVE). **Licencia Apache-2.0.** — [MotionBERT README](https://github.com/Walter0807/MotionBERT); [LICENSE](https://github.com/Walter0807/MotionBERT/blob/main/LICENSE)
- **VideoPose3D:** **46,8 mm** de MPJPE (36,5 mm alineado) en Human3.6M, con detecciones CPN y 243 cuadros de contexto. Con 2D perfecto, 37,2 mm. **Licencia CC BY-NC 4.0 (no comercial).** — [VideoPose3D README](https://github.com/facebookresearch/VideoPose3D); [LICENSE](https://github.com/facebookresearch/VideoPose3D/blob/main/LICENSE)
- **WHAM (CVPR 2024):**
  - 3DPW: **35,9 mm alineado (PA-MPJPE), 57,8 mm sin alinear (MPJPE)**, 68,7 mm de error por vértice. En EMDB: 50,4, 79,7 y 94,4 mm.
  - La red corre a 200 fps sin contar el preprocesamiento (detección y puntos 2D); no se dice en qué hardware.
  - Código MIT, pero necesita descargar SMPL con registro.
  — [WHAM paper (arXiv 2312.07531)](https://arxiv.org/html/2312.07531v2); [WHAM GitHub](https://github.com/yohanshin/WHAM); [LICENSE MIT](https://github.com/yohanshin/WHAM/blob/main/LICENSE)
- **HMR2.0 (4DHumans)**, en la tabla de WHAM: 3DPW 44,4 mm alineado y 69,8 mm sin alinear. Código MIT, pero requiere el modelo neutro de SMPL. — [WHAM paper](https://arxiv.org/html/2312.07531v2); [4D-Humans GitHub](https://github.com/shubham-goel/4D-Humans)
- **Licencia de SMPL:** solo para investigación científica no comercial. La licencia comercial se tramita con Meshcapade (smpl@max-planck-innovation.de). — [SMPL Model License](https://smpl.is.tue.mpg.de/modellicense.html)
- **GolfPose-3D** (lifting tipo MixSTE ajustado con golf): 30,7–39,2 mm de MPJPE en su propio conjunto de prueba. — [GitHub GolfPose](https://github.com/MingHanLee/GolfPose)
- **MeTRAbs** (3D directo desde la imagen): código MIT. Hay una tesis del MIT que lo aplica al golf; no encontré sus números. — [MeTRAbs GitHub](https://github.com/isarandi/metrabs); [Tesis MIT](https://dspace.mit.edu/entities/publication/c9b09f89-dadb-4002-9229-89b5016925b2)
- **Sapiens (Meta):** CC BY-NC 4.0, no comercial. — [Sapiens LICENSE](https://github.com/facebookresearch/sapiens/blob/main/LICENSE)
- **[PREPRINT]** Lauer, con un sensor de muñeca: 4,0° de error en ángulos y 5,3 cm en posiciones. Pero su "verdad" salió de WHAM sobre video, no de marcadores, y las entradas eran sintéticas. Los autores del preprint siguiente advierten que eso infla la precisión. — [arXiv 2606.22876](https://arxiv.org/html/2606.22876)

### Inferences
- Un MPJPE de 36–58 mm en benchmarks generales significa que, en un swing (rápido, con brazos que cruzan el cuerpo y un palo que tapa), hay que esperar errores de posición de **≥5 cm** por articulación y **errores de rotación de dos dígitos** en pelvis y pecho, salvo ajuste con datos de golf. Es una extrapolación: no hay validación de estos modelos en golf contra marcadores.
- Opciones comerciales viables para 3D con una cámara:
  - MotionBERT (Apache-2.0);
  - GolfPose-3D, si se entrena uno propio con el dataset bajo su EULA.
  - Riesgo legal a revisar: MotionBERT y MixSTE se entrenaron con Human3.6M, cuya licencia suele ser académica (no se pudo verificar; ver Gaps).
- WHAM y HMR2 dan mejor movimiento global y malla, pero dependen de SMPL (no comercial). Para un producto pago necesitan licencia de Meshcapade.
- Esto confirma la decisión del dueño del 04/11/2026 ("sin modelo 3D"): un 3D con una sola cámara agregaría números con márgenes grandes y riesgos de licencia.

### Gaps
- No pude leer la licencia de Human3.6M: vision.imar.ro devolvió error, así que no está verificado si los pesos entrenados con ese dataset se pueden usar comercialmente.
- No hay MPJPE de MotionBERT, WHAM ni HMR2 medido en swings de golf.
- No hay datos de velocidad en CPU para WHAM, HMR2 ni MotionBERT; los 200 fps de WHAM no dicen hardware.

## 5. Varias cámaras (2 celulares): OpenCap, Pose2Sim, Theia3D, y si sirve triangular desde atrás + de frente

### Takeaway
Con 2 o más cámaras calibradas, la cinemática 3D validada llega a ~3–5° de error medio (OpenCap 4,5°, Pose2Sim 3,0–4,1°). Pero todas las validaciones son de marcha, sentadilla, carrera o ciclismo. Las rotaciones transversales (justamente pelvis y tórax en golf) son el punto débil, y hay errores puntuales de 10–21°. Triangular desde atrás y de frente (≈90°) es geométricamente favorable y Pose2Sim lo permite, pero exige calibrar con un tablero, sincronizar los dos celulares y que no se muevan.

### Cited Findings
- **OpenCap [REVISADO POR PARES, autores del sistema]:**
  - Montaje: 2 iPhone 12 Pro a ±45°, 1,5 m de altura y 3 m, video 720x1280 a 60 Hz con foco fijo.
  - Calibración con un tablero de ajedrez (alcanza con uno impreso en A4) y sincronización por correlación de velocidades de los puntos. HRNet como modelo de pose y una red LSTM que agrega 43 marcadores anatómicos.
  - **MAE de 4,5° (rango 1,7–10,3°)** en 18 grados de libertad. Traslaciones de la pelvis: **12,3 mm** de MAE. Error de marcadores mayor en tronco y pelvis (39 y 38 mm) que en las piernas (27 mm).
  - Agregar cámaras mejoró menos de 0,3°. Tareas: marcha, sentadilla, sentarse y pararse, salto en caída; no se trató el movimiento rápido.
  - Código Apache-2.0. El uso comercial se canaliza por Model Health, Inc.
  — [OpenCap, PLOS Comp Biol 2023](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011462); [opencap-core LICENSE](https://github.com/stanfordnmbl/opencap-core/blob/main/LICENSE)
- **OpenCap, estudios independientes:**
  - Contra Vicon en tareas funcionales: cadera frontal con RMSE < 6°, rodilla sagital 4–10°, cadera sagital en marcha > 10°. — [J Biomech 2025](https://www.sciencedirect.com/science/article/abs/pii/S0021929025001137)
  - Caminando alejándose de las cámaras: ~12° de RMSE en algunos ángulos. — [Sensors 2025, PMC12568194](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12568194/)
  - **[PREPRINT]** "OpenCap Monocular", con un celular a 45°: 4,8° de MAE en 18 ángulos, en actividades sin saltos. Visto solo en el resumen de búsqueda. — [arXiv 2607.17639](https://arxiv.org/html/2607.17639)
- **Pose2Sim [REVISADO POR PARES]** (Pagnon et al., Sensors 2022), un solo participante:
  - Error medio de **3,0° caminando, 4,1° corriendo y 4,0° en bicicleta**. Cadera al correr: desfase sistemático de 15°.
  - Con imagen degradada (desenfoque, menos cámaras, error de calibración), el MAE contra la condición de referencia fue de solo 0,35–1,6°.
  - Licencia BSD-3-Clause.
  — [Pose2Sim Part 2, PMC9002957](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9002957/); [LICENSE](https://github.com/perfanalytics/pose2sim/blob/main/LICENSE)
- **Theia3D (comercial, varias cámaras):**
  - Marcha contra marcadores: RMSD de hasta 8,5° sagital, 5,3° frontal y **10,2° transversal**. — [LJMU](https://researchonline.ljmu.ac.uk/id/eprint/27367/1/Comparison%20of%20Theia3D%20and%20the%20conventional%20gait%20model%20in%20typically%20developing%20children%20and%20adults%20in%20a%20clinical%20gait%20laboratory.pdf)
  - En otro estudio, los ángulos rotacionales difieren y las medidas "no son intercambiables" con las de marcadores. — [Sci Rep 2024](https://www.nature.com/articles/s41598-024-80499-8)
  - Rangos del hombro sobreestimados. — [J Biomech 2025](https://www.sciencedirect.com/science/article/pii/S0021929025004178)
  - Salto con contramovimiento: tobillo y rodilla con RMSD < 5°, cadera con RMSD promedio de 21° (autores no confirmados). — [core.ac.uk](https://core.ac.uk/download/478536344.pdf)
  - No encontré validación de Theia3D en golf.
- **Referencia de sensores inerciales (IMU) en golf [REVISADO POR PARES]**, contra 10 cámaras Motion Analysis, 36 golfistas y 103 swings:
  - Rotación de pelvis: ICC 0,99, sesgo 0,76°, límites de acuerdo **−9,6 a +11,1°**.
  - Rotación del torso: ICC 1,00, sesgo 1,05°, límites **−11,2 a +13,3°**.
  - X-factor: ICC 0,94, límites **−21,4 a +18,6°**.
  — [PMC10611231](https://pmc.ncbi.nlm.nih.gov/articles/PMC10611231/)
- **[PREPRINT] Reloj inteligente** (una IMU en la muñeca) contra Vicon de 9 cámaras: MAE de 8,53° en todo el cuerpo; pelvis 7,28°, torso 7,96°, brazos 11,14°. Límites de acuerdo de ±~26° en la rotación máxima del torso. — [arXiv 2606.22876](https://arxiv.org/html/2606.22876)

### Inferences
- **Desde atrás + de frente con 2 celulares sí se puede**, con condiciones:
  - El ángulo de ~90° entre cámaras es mejor para triangular que los ±45° de OpenCap.
  - Pose2Sim (BSD-3) acepta cámaras arbitrarias y se calibra con un tablero.
  - Hay que tener: trípodes que no se muevan, un tablero visible para las dos cámaras, sincronización (las velocidades de los puntos alcanzan, como en OpenCap) y los mismos fps en los dos celulares, con obturador rápido.
  - Riesgo práctico: los seguidores filman con un solo celular y en momentos distintos. Dos tomas de swings distintos **no se pueden triangular**: tiene que ser el mismo swing grabado a la vez.
- Aun con varias cámaras, para giro de pelvis y torso conviene declarar **±5–10°**. Ni las IMU dedicadas bajan de límites de acuerdo de ±10° contra marcadores, y las rotaciones transversales son lo peor de Theia3D y OpenCap.

### Gaps
- No hay ninguna validación revisada por pares de OpenCap, Pose2Sim ni Theia3D en el swing de golf.
- No se probó la sincronización por velocidades con desenfoque de 30 fps en P5–P7.

## 6. Precisión realista para declarar (cm, grados, ms) y ranking de herramientas

### Takeaway
Con un video de celular y una sola cámara, lo honesto es declarar:
- **±3–5° en ángulos del plano de la imagen** en posiciones quietas o lentas (P1, P2, P4, P10);
- **±1–3 cm en desplazamientos dentro del plano** (sway desde la vista de frente, cambio de altura de la cabeza), con una referencia de tamaño;
- **±1 cuadro en los eventos** (±33 ms a 30 fps, ±17 ms a 60 fps, ±4 ms a 240 fps);
- **no dar valores absolutos de rotación de pelvis o pecho** con una sola cámara: son estimaciones de ±10° o más.

### Cited Findings
- Precisión de la medición 2D del palo, validada en las posiciones clave (frente, 240 Hz, 1/2000 s): medición típica de ~0,6–3,2°; en el final de 19–20°. — [Hunter 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9385988/)
- Mejor caso declarado por un fabricante con una cámara: ~2° y ~0,4 pulgadas (~1 cm). — [Sportsbox](https://help.sportsbox.ai/sportsbox-ai-accuracy)
- Varias cámaras: 3–5° y 12 mm en la pelvis. — [OpenCap](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011462); [Pose2Sim](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9002957/)
- Centros articulares 3D con 9 cámaras: 14–58 mm. — [Needham 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8526586/)
- Deporte rápido con modelos 2D en celulares: 10–40° de RMSE. — [PMC13306328](https://pmc.ncbi.nlm.nih.gov/articles/PMC13306328/)
- Eventos:
  - SwingNet detecta el impacto con 98,4 % de acierto y el tope con 83,9 %, con tolerancia ≈1 cuadro a 30 fps (address a impacto ≈1 s ≈ 30 cuadros). Address 31,7 %, Finish 26,5 %. — [GolfDB](https://arxiv.org/abs/1903.06528)
  - Del tope al impacto pasan ≈0,23–0,29 s (citado de trabajos anteriores). — [arXiv 2606.22876](https://arxiv.org/html/2606.22876)
- Velocidad en CPU:
  - RTMPose-m (256x192), 11,06 ms por persona en un i7-11700 con ONNXRuntime (90+ FPS). Con el detector RTMDet-nano, 26,6 ms. RTMPose-s en un Snapdragon 865: 70+ FPS. — [RTMPose README](https://github.com/open-mmlab/mmpose/tree/main/projects/rtmpose)
  - SwingNet: 10,6 ms por cuadro en un i7-8700K. — [GolfDB](https://arxiv.org/abs/1903.06528)
  - rtmlib corre RTMPose y DWPose con ONNX, sin mmcv. Apache-2.0. — [rtmlib](https://github.com/Tau-J/rtmlib)
- Licencias verificadas en cada LICENSE:
  - **Apache-2.0** (comercial permitido): MediaPipe ([LICENSE](https://github.com/google-ai-edge/mediapipe/blob/master/LICENSE)), MMPose/RTMPose ([LICENSE](https://github.com/open-mmlab/mmpose/blob/main/LICENSE)), rtmlib, ViTPose ([LICENSE](https://github.com/ViTAE-Transformer/ViTPose/blob/main/LICENSE)), DWPose ([repo](https://github.com/IDEA-Research/DWPose)), MotionBERT, opencap-core.
  - **MIT** (comercial permitido): HRNet ([LICENSE](https://github.com/leoxiaobin/deep-high-resolution-net.pytorch/blob/master/LICENSE)), MeTRAbs, WHAM y 4D-Humans (pero estos dos dependen de SMPL, que es no comercial).
  - **BSD-3** (comercial permitido): Pose2Sim.
  - **Solo investigación no comercial:** OpenPose ([LICENSE](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/LICENSE)) y AlphaPose ([LICENSE](https://github.com/MVIG-SJTU/AlphaPose/blob/master/LICENSE)).
  - **CC BY-NC 4.0** (no comercial): VideoPose3D, Sapiens y GolfDB/SwingNet.
  - **AGPL-3.0** (obliga a publicar el código del servicio): Ultralytics YOLO y swingtrace.
  - **EULA que permite modelos comerciales:** dataset GolfPose.

### Inferences
**Márgenes de error para poner en el informe** (estimados a partir de la evidencia anterior, no validados en golf con nuestro pipeline):

| Medida | Condición | Margen honesto |
|---|---|---|
| Inclinación del tronco, flexión de rodilla, ángulo de la varilla | Vista desde atrás o de frente, cámara perpendicular y a la altura de las manos, ≥60 fps, obturador rápido, posiciones P1/P2/P4/P10 | ±3–5° |
| Lo mismo en P5–P8 (bajada e impacto) | 30–60 fps con desenfoque | ±5–10°, o "no evaluado" si el punto tiene baja confianza |
| Giro de pelvis y pecho, X-factor | Una cámara | Solo cualitativo o "estimado ±10°+"; no dar números absolutos |
| Giro de pelvis y pecho | Dos celulares sincronizados y calibrados | ±5–10° |
| Sway y lift de pelvis y cabeza | Vista de frente, escala conocida en el plano del jugador | ±1–3 cm (con 2D se mezclan la distancia a la cámara y la perspectiva) |
| Manos o varilla respecto del plano (por ejemplo, "manos 14–23 cm por encima") | Vista desde atrás | ±2–4 cm por la escala y la perspectiva; mejor dar rangos |
| Momento del impacto o del tope | Detección automática o manual | ±1 cuadro (30 fps: ±33 ms; 60 fps: ±17 ms; 240 fps: ±4 ms) |
| Tempo (subida y bajada) | Video a velocidad real | ±1 cuadro en cada borde; no medir con cámara lenta "horneada" |

- Cuentas: a 30 fps, la bajada (0,23–0,29 s) son solo ~7–9 cuadros. A 240 fps son ~55–70. Por eso los cuadros de P5–P7 a 30 fps tienen mucho desenfoque y salteos, y la cámara lenta del iPhone mejora la geometría pero no el tempo.

**Herramientas recomendadas, en orden (producto pago, CPU):**
1. **Cuerpo 2D: RTMPose-m o RTMPose-l con rtmlib (ONNX, Apache-2.0).** Corre en tiempo real en CPU y es el mejor equilibrio de licencia, velocidad y AP. Sumar el modelo de 26 puntos (Halpe26/Body8, incluye talones y puntas de los pies) para la postura. Opcional: ajustarlo con GolfPose (la EULA permite el modelo comercial) para agregar la varilla.
2. **Alternativa o control cruzado: MediaPipe Pose heavy (Apache-2.0).** Es lo que ya usa el proyecto. Correr dos modelos y marcar los cuadros donde no coinciden sirve para detectar cambios de lado.
3. **Más precisión offline:** ViTPose (Apache-2.0) o HRNet (MIT) en GPU, o ajustados con GolfPose. En GolfPose, ViTPose-H y HRNet-w48 rinden casi igual (0,887 contra 0,884 AP en golfista).
4. **Palo:**
   - detector o puntos propios (varilla, cabeza y manos) entrenados con RTMDet o RTMPose (Apache-2.0) sobre golf-club-tracking (CC BY 4.0, con atribución) o sobre GolfPose;
   - swingtrace solo para prototipar (AGPL);
   - mantener la visión clásica actual como respaldo (líneas paralelas, Gehrig 2003).
5. **Eventos:** SwingNet **reimplementado y reentrenado** (el código original es NC), o reglas simples sobre la cinemática (velocidad de manos o muñecas, dirección de la varilla). Usar el modelo para Impact y Top, y reglas para Address y Finish.
6. **3D:** no usar con una cámara para dar números al cliente. Si hay dos celulares sincronizados, Pose2Sim (BSD-3). Evitar WHAM, HMR2 y SMPL sin licencia de Meshcapade, VideoPose3D (NC), OpenPose y AlphaPose (NC).

### Gaps
- No existe una validación pública de este pipeline (RTMPose o MediaPipe sobre celular, en golf) contra marcadores. Los márgenes de la tabla son inferencias y habría que comprobarlos con un estudio propio (por ejemplo, contra un video calibrado o contra IMU).
- No se verificó la licencia de los pesos que distribuye MediaPipe (model card de BlazePose) por separado del código.
- No se verificó qué tan bien se puede medir la distancia en 2D de un video de celular sin calibrar (error de escala y perspectiva con lente gran angular).
