# Reel · Haval H6 en Brasil

Reel 1080x1920 (HyperFrames) sobre la nota de Motor1 Brasil: la Haval H6, un híbrido, pasa a ser la SUV mediana más vendida de Brasil en 2026 (datos parciales de octubre). No nombra a la rival; el nombre del auto aparece recién en la revelación (dibujo de líneas → foto real).

## Archivos
- `guion/guion-pantalla.txt`: texto correcto (subtítulos).
- `guion/guion-voz-elevenlabs.txt`: lo que se pega en ElevenLabs (números y siglas escritos como se dicen).
- `guion/descripcion-y-comentario.md`: descripción, comentario fijado y lista para verificar.
- `revision/hoja-de-cuadros.jpg`: cuadros de prueba (con voz temporal).
- `tools/index.template.html`: la composición. Todas las animaciones se anclan a palabras del guion, así que cambiar la voz no rompe nada.
- `CREDITOS.md`: fuentes de datos, foto, música, efectos y tipografías.

## Cambiar a la voz definitiva (ElevenLabs)
Desde esta carpeta:

```sh
mkdir -p audio/voz
cp <voz-elevenlabs>.mp3 audio/voz/original.mp3
# acelerar x1,20 sin cambiar el tono
ffmpeg -y -i audio/voz/original.mp3 -af "rubberband=tempo=1.2:pitchq=quality:formant=preserved" -ar 48000 audio/voz/voz.wav
npx --yes hyperframes@0.8.230 transcribe audio/voz/voz.wav --model small --language es   # escribe audio/voz/transcript.json
python3 tools/align.py audio/voz/transcript.json guion/guion-pantalla.txt timing.json
python3 tools/mix.py audio/voz/voz.wav        # voz > efectos > música, -14 LUFS / -1 dBTP
python3 tools/build.py                        # arma index.html
npx --yes hyperframes@0.8.230 check
npx --yes hyperframes@0.8.230 render -o render/haval-h6-brasil.mp4
ffmpeg -i render/haval-h6-brasil.mp4 -c:v libx264 -crf 26 -preset slow -c:a aac -b:a 192k -movflags +faststart render/haval-h6-brasil-liviano.mp4
```

Requisitos de Python: `numpy` (mix.py). La alineación usa solo la biblioteca estándar.
