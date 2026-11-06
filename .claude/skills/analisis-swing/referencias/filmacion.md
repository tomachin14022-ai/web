# Protocolo de filmación y calibración

> Fuente: `swing-analisis/investigacion/informe.md` (investigación del 05–06/11/2026). Etiquetas: [PR] estudio revisado por pares · [CONF] congreso o preprint · [FAB] fabricante · [TPI] dato propio de TPI · [INS] criterio de enseñanza · [CP]/[INF] cálculo o inferencia propia · [NV] no verificado (no usar como dato).

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


## Error por ubicación de la cámara de atrás (cálculo propio [CP], cámara a 3 m)

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

Una cámara **por encima** del plano aplana el swing (esconde un over the top); una **por debajo** lo empina (inventa un over the top). A 3,7 m el error baja ~25 %.

## Control al recibir el video

```sh
ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height,avg_frame_rate,r_frame_rate,nb_frames:format=duration \
  -of default=nw=1 VIDEO
```
- Cámara lenta original: ~238–240 fps (o ~120) y duración real. Si dice 30 fps o el swing dura ~8 veces más, es cámara lenta
  "horneada": **no medir ritmo** y pedir el original con "100 % – 240 FPS".
- La frecuencia es variable: usar el tiempo de cada cuadro (`ffprobe -show_frames -show_entries frame=pts_time`), no fps × cuadro.
- Punto de fuga de las dos varillas: marcar dos puntos en cada varilla, cortar las rectas y pasar el punto a
  `tools/plano_check.py --vp X,Y`. Con más de 5° de giro (θ = atan(d/f), f ≈ 1.400 px en 1080x1920) el slot de TPI no vale.
- Si el video no sirve (cámara movida o girada, cuerpo o palo cortado, borroso, 0,5x), **no se analiza**: se pide otro
  diciendo exactamente qué falló.

## Mensaje listo para mandarle al seguidor

> **Cómo filmar tu swing para el análisis**
>
> Vas a necesitar: un trípode o algo firme para el celular, dos palos o varillas de alineación y una cinta métrica.
>
> **1. Varillas en el piso.** Poné una varilla justo delante de las puntas de tus pies y otra sobre la línea pelota–objetivo,
> paralelas entre sí. Medí el largo de cada una y la distancia entre ellas, y anotalo. Para la toma de frente, sumá una tercera
> varilla perpendicular, en el medio de tus pies.
>
> **2. Celular.** Vertical, **lente 1x** (nunca 0,5x), **cámara lenta a 240 fps** (120 si hay poca luz), nivelado y fijo. De día,
> sin contraluz, con ropa que contraste con el fondo. Que entren tu cuerpo entero, la pelota y el palo arriba de tu cabeza.
>
> **3. Desde atrás.** Celular **detrás tuyo, en la prolongación de la línea de tus manos** (entre la varilla de los pies y la de la
> pelota, más cerca de la de los pies), **a la altura de tus manos** en el address, a **3 a 3,7 m**, apuntando paralelo a la línea de
> tiro. Nunca detrás de la pelota.
>
> **4. De frente.** Celular sobre la línea de la varilla perpendicular, mirando de frente a la línea de tiro, a la **altura de tus
> manos o tu cadera**, a **3 a 3,7 m** de la pelota.
>
> **5. Tomas.** 3 swings en cada vista sin mover el trípode. Si tenés dos celulares, mejor: el mismo swing desde las dos vistas a la vez.
>
> **6. Envío.** Mandá el **archivo original**, sin recortar ni editar: en iPhone, abrilo en Fotos → Editar y poné la velocidad en
> "100 %"; mandalo por AirDrop, cable o Google Drive como archivo. Por WhatsApp, solo "como documento".
>
> **7. Contame de cada swing:** diestro o zurdo · palo · adónde apuntabas · **dónde salió la pelota** (izquierda, derecho, derecha) ·
> **cómo curvó y cuánto** · si salió más alta o más baja de lo normal · **contacto** (centro, punta o talón; pesado o finito; si
> podés, foto de la marca en la cara con spray o cinta de impacto, y del divot) · si fallás para un lado o para los dos · distancia ·
> condiciones (viento, pendiente, alfombra) · datos de launch monitor si tenés · **si tenés dolor o alguna lesión** · y si me das
> permiso para publicar tu swing (si sos menor, el permiso es de tu madre, padre o tutor).

## Historia de Instagram (versión corta, solo desde atrás, 06/11/2026)

1. **ANALIZO TU SWING 🏌️** · Elijo 5 swings y los analizo gratis en un reel: ángulos medidos sobre tu video, la causa principal de
   tu error y un drill para corregirla. Te explico cómo mandármelo 👉
2. **CÓMO FILMARLO 📱** · Celular fijo (trípode o apoyado en la bolsa), vertical y sin zoom (1x) · Detrás tuyo, mirando hacia el
   objetivo · En la línea de tus manos (entre tus pies y la pelota) y a la altura de tus manos · A unos 3 metros (4 pasos largos) ·
   En CÁMARA LENTA · Que se vean tu cuerpo entero, el palo arriba y la pelota.
3. **ANTES DE PEGAR ⛳** · Poné 2 palos en el piso, paralelos a la línea de tiro: uno justo delante de la punta de tus pies y otro del
   otro lado de la pelota, a un palmo. Con eso mido con precisión.
4. **CÓMO MANDARLO 📩** · Subí el video sin editar ni recortar a Google Drive y mandame el link por DM (por Instagram pierde
   calidad). Contame qué palo usaste, para dónde salió la pelota (izquierda, derecho o derecha), cómo curvó y si sos zurdo.
   Al mandarlo aceptás que publique tu swing; si sos menor, con permiso de tu mamá, papá o tutor.
