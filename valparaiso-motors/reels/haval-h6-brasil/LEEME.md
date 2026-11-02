# Reel · Haval H6 en Brasil

Reel 1080x1920 a 60 fps (HyperFrames), 21,5 s. Gancho: "¿Comprarías un auto chino? En Brasil, mucha gente ya contestó."
Cuenta que la Haval H6 pasó a ser la SUV mediana más vendida de Brasil en 2026 (datos parciales de octubre), abre el debate con "¿Pasará lo mismo en Argentina?" y cierra con "Pedinos precio y financiación de la H6 PRO HEV en Valparaiso Motors".
No nombra a la rival. El auto aparece como dibujo de líneas andando (ruedas que giran sincronizadas con el piso) y sigue en dibujo durante la pregunta; la foto real de la H6 PRO HEV y el nombre aparecen recién en "Pedinos precio y financiación". La pregunta no suena a cierre: queda abierta con "¿Y CUÁL ES?" y "COMENTÁ" va como sticker al final, sin voz.

## Archivos
- `guion/guion-pantalla.txt`: texto correcto (subtítulos).
- `guion/guion-voz-elevenlabs.txt`: lo que se grabó en ElevenLabs (02/11, 18:15).
- `guion/descripcion-y-comentario.md`: descripción, comentario fijado y lista para verificar.
- `audio/voz/elevenlabs-tomas.mp3`: voz del dueño (sin cortes).
- `tools/index.template.html`: la composición. Las animaciones se anclan a palabras del guion.
- `tools/ajustes-tiempos.json`: tiempos medidos a mano sobre la forma de onda (empalme "año. / ¿Pasará", la pregunta y el cierre).
- `tools/recorte.py`: para sacar tramos de la voz si hiciera falta (con esta voz no hay cortes).
- `CREDITOS.md`: fuentes de datos, imagen, voz, música, efectos y tipografías.
- `render/` (no se sube al repositorio): `haval-h6-brasil-final.mp4` (máxima calidad) y `haval-h6-brasil-liviano.mp4` (para subir).

## Volver a armarlo
Desde esta carpeta:

```sh
npx --yes hyperframes@0.8.230 transcribe audio/voz/elevenlabs-tomas.mp3 --model small --language es   # audio/voz/transcript.json
python3 tools/align.py audio/voz/transcript.json guion/guion-pantalla.txt timing.json
python3 tools/recorte.py audio/voz/elevenlabs-tomas.mp3 audio/voz/voz-recortada.wav   # sin cortes: copia la voz
python3 tools/velocidad.py audio/voz/voz-recortada.wav audio/voz/voz-tramos.wav     # x1,05 desde "¿Pasará"
python3 tools/mix.py audio/voz/voz-tramos.wav     # voz > efectos > música, -14 LUFS / -1 dBTP
python3 tools/build.py                            # arma index.html
npx --yes hyperframes@0.8.230 check
npx --yes hyperframes@0.8.230 render -o render/haval-h6-brasil-final.mp4 --fps 60 --quality delivery
ffmpeg -i render/haval-h6-brasil-final.mp4 -c:v libx264 -crf 26 -preset slow -c:a aac -b:a 192k -movflags +faststart render/haval-h6-brasil-liviano.mp4
```

`tools/pausas.py` sirve para meter silencios en la voz si hace falta (en este video no se usó).
Requisitos de Python: `numpy` (mix.py). La alineación usa solo la biblioteca estándar.
