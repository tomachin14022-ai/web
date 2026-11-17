---
name: lo-barato-3d
description: Hacer un video vertical "Lo barato sale caro" (comparación de costo por uso entre dos productos) en el estilo 3D de personaje con Remotion, con la voz del dueño grabada en ElevenLabs. Usar cuando pida un video nuevo de la serie, otro par de productos, cambiar algo de los videos de impresora, cafetera o aire, o "el estilo 3D de las referencias".
---

# Lo barato sale caro · estilo 3D (Remotion)

Proyecto: `lo-barato-sale-caro/remotion/`. Un solo componente (`src/VideoComparacion.tsx`) arma todos los videos a partir de los datos de `src/datos/videos.ts`. Los videos son para Instagram, con links de afiliado de Mercado Libre en la bio. Las reglas de Valparaiso Motors del CLAUDE.md **no** valen acá.

## El estilo (sale de las referencias del dueño)

Videos explicativos 3D con un personaje de juguete: cabeza redonda, cara mínima y emociones solo con las cejas. Textos grandes como de miniatura.

- **Personaje** (`src/3d/Personaje.tsx`): original, armado con formas simples.
  - Cabeza blanca redonda, ojos negros con brillo y cejas que marcan la emoción (−1 enojado, 0 normal, 1 sorprendido).
  - Remera amarilla y pantalón azul oscuro.
  - Mira y señala: los valores positivos van hacia la derecha de la pantalla, donde está la opción cara. Salta en los golpes.
  - Nunca copiar personajes de otros canales.
- **Escenario** (`src/3d/Escenario.tsx`): estudio con pared y piso de un color por video, niebla, contraluz de color y papelitos flotando.
  - Hay sombras, cámara en mano suave y viñeta.
- **Productos** (`src/3d/Productos.tsx`): de juguete, armados con formas simples y **sin marcas ni logos**.
  - La barata va a la izquierda, en un podio con aro rojo; la cara a la derecha, en un podio con aro amarillo.
- **Torres de billetes** (`src/3d/Torre.tsx`): muestran el costo acumulado mes a mes.
  - Encima, un cartel con el total que va contando.
  - Un contador "MES n" y el destello "SE DA VUELTA" en el mes del cruce.
- **Textos:**
  - Anton en blanco con **una** palabra clave en amarillo #ffcc00, con sombra dura. El rojo #ff3b30 es solo para el costo caro.
  - Los carteles son tarjetas con sombra dura.
  - Subtítulos de **una palabra por vez**, en minúscula, Inter 900 blanco con borde negro, a la altura y 1150.
- **Zona segura** (común a Reels, TikTok y Shorts): el texto importante va en x 120–888 e y 288–1248.

## Estructura del video (sincronizada a la voz)

1. **Gancho:** título visible desde el cuadro 0, con el personaje desconfiado mirando la barata.
2. **"¿Cuál comprás?":** carteles con el precio de cada uno.
3. **Primer plano de la barata:** costo por uso en rojo.
4. **Primer plano de la cara:** costo por uso en amarillo y la etiqueta "x VECES MENOS".
5. **Las torres:** los productos salen, crecen las torres y el contador llega al mes del cruce. Destello "SE DA VUELTA".
6. **"Desde ahí gana la cara":** el personaje la señala y la cámara se abre mientras las torres siguen creciendo.
7. **"En N años ahorrás":** número amarillo que cuenta hasta el ahorro, y el personaje festeja.
8. **"Link en la bio":** el personaje saluda.

## Hacer un video nuevo

1. **Números:** calcular costo por uso, totales, mes de cruce y ahorro (como en `lo-barato-sale-caro/videos/generar.py`). Anotar la fuente de cada dato en la descripción.
2. **Guion:** escribirlo con la misma estructura y la misma forma de decir las cosas que `lo-barato-sale-caro/videos/guiones-voz.md`.
   - Al dueño se le pasa **solo el texto**, sin números de línea ni indicaciones.
   - Cierra con "Link en la bio." y nada más.
3. **Voz:** la graba el dueño en ElevenLabs (voz "Tomas – Argentina / Uruguaya") y la guardás en `public/voz/<id>.mp3`. **No** usar voces sintéticas propias: el dueño las rechazó.
4. **Tiempos por palabra:**
   ```sh
   node ~/.claude/skills/hyperframes/scripts/plugin-cli.mjs transcribe voz.mp3 -m small -l es --json   # en una carpeta aparte
   python3 palabras.py <carpeta>/transcript.json <id>   # → src/datos/palabras-<id>.json
   ```
   `palabras.py` separa las palabras pegadas, corrige el voseo ("compras" → "comprás") y pone `$` en los precios. Si hay precios nuevos, agregarlos en `PRECIOS`.
5. **Datos:** agregar el video en `src/datos/videos.ts`.
   - Cada momento de `t` sale de la palabra en que empieza esa parte del guion.
   - `fin` = fin del audio + ~0,6 s.
   - Agregar su `<Composition>` en `src/Root.tsx` con `durationInFrames = fin × 30`.
6. **Producto nuevo:** modelarlo en `Productos.tsx` con formas simples (RoundedBox, cilindros, cápsulas) y darle su `ESCALA` y `ALTO_PRODUCTO` en `VideoComparacion.tsx`.
7. **Revisar cuadros antes del render final:**
   ```sh
   export REMOTION_CHROME=/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell
   npx remotion render <Id> out/cuadros --sequence --frames=3,60,95,200,300,340,420,465,500,590,650 --image-format=png --scale=0.5
   ```
   Armar una hoja con ffmpeg (`tile=6x2`). Verificar que nada se pise (título, carteles y subtítulo) y que todo quede dentro de la zona segura. Mostrársela al dueño y hacerle una sola pregunta.
8. **Render y volumen:**
   ```sh
   npx remotion render <Id> out/<Id>-crudo.mp4 --concurrency=3
   ffmpeg -i out/<Id>-crudo.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:a aac -b:a 192k -movflags +faststart out/<Id>.mp4
   ```

## Reglas técnicas

- **Animación:** solo con `useCurrentFrame()` e `interpolate()`. Nada de `useFrame()`, `Math.random()` ni transiciones CSS.
- **Cámara:** sale de `Camara` (props por cuadro). Los carteles HTML se anclan al 3D con `proyectar()`, usando la misma toma.
- **Render en este servidor:**
  - WebGL va por software (`swangle`, en `remotion.config.ts`).
  - Las fuentes son **locales** (`public/fuentes`, OFL), porque Chrome no acepta el certificado del proxy para Google Fonts.
- **Destellos con `interpolate`:** poner tres puntos (`[t-0.01, t, t+d] → [0, x, 0]`). Con `clamp` y dos puntos, el valor inicial queda prendido desde el cuadro 0.
