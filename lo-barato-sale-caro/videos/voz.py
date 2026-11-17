#!/usr/bin/env python3
"""Genera la voz en off de un video "Lo barato sale caro" con una voz argentina (es-AR).

Uso:  python3 voz.py datos/02-cafetera.json 02-cafetera [--voz es-AR-TomasNeural]

Lee "voz" del JSON: una lista de [segundo, "texto"]. Cada frase se genera aparte,
se le recorta el silencio del principio y se ubica en su segundo, para que caiga
sobre la escena que le corresponde. Si una frase no entra antes de la siguiente,
se regenera todo un poco más rápido
(misma velocidad en todo el video, hasta +30 %). Escribe <salida>/assets/voz.mp3 (−14 LUFS)
y <salida>/assets/voz.json con los tiempos reales de cada frase.

Necesita edge-tts (pip install edge-tts) y ffmpeg.
"""
import asyncio
import json
import os
import ssl
import subprocess
import sys
import tempfile
from pathlib import Path

import edge_tts
import edge_tts.communicate

# Detrás de un proxy con su propio certificado (SSL_CERT_FILE), edge-tts tiene que usarlo
if os.environ.get("SSL_CERT_FILE"):
    edge_tts.communicate._SSL_CTX = ssl.create_default_context(cafile=os.environ["SSL_CERT_FILE"])

DURACION = 24.5          # largo del video
MARGEN = 0.08            # aire mínimo entre una frase y la siguiente
VELOCIDADES = [15, 20, 25, 30]  # % más rápido que la voz normal


def duracion(archivo):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(archivo)], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def generar_frase(texto, voz, velocidad, destino):
    crudo = destino.with_suffix(".crudo.mp3")
    asyncio.run(edge_tts.Communicate(texto, voz, rate=f"+{velocidad}%").save(str(crudo)))
    # Recorta el silencio del principio y del final
    filtro = ("silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.02,"
              "areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.06,areverse")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(crudo), "-af", filtro,
                    "-ar", "48000", "-ac", "1", str(destino)], check=True)
    crudo.unlink()
    return duracion(destino)


def main():
    datos = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    salida = Path(sys.argv[2])
    voz = sys.argv[sys.argv.index("--voz") + 1] if "--voz" in sys.argv else "es-AR-TomasNeural"
    frases = datos["voz"]
    (salida / "assets").mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix="voz-"))

    # Una sola velocidad para todo el video (ritmo parejo): la más lenta en la que entran todas las frases
    for vel in VELOCIDADES:
        tiempos, sobra = [], []
        for i, (inicio, texto) in enumerate(frases):
            limite = frases[i + 1][0] - MARGEN if i + 1 < len(frases) else DURACION - 0.15
            archivo = tmp / f"frase{i:02d}.wav"
            dur = generar_frase(texto, voz, vel, archivo)
            if inicio + dur > limite:
                sobra.append(f"«{texto}» se pisa {inicio + dur - limite:.2f} s")
            tiempos.append({"inicio": inicio, "fin": round(inicio + dur, 3), "velocidad": vel,
                            "texto": texto, "archivo": archivo})
        if not sobra:
            break
        print(f"+{vel}%: " + "; ".join(sobra))
    if sobra:
        raise SystemExit("Hay frases que no entran ni a la velocidad máxima: acortalas.")
    for t in tiempos:
        print(f"{t['inicio']:6.2f}–{t['fin']:6.2f}  +{vel}%  {t['texto']}")

    # Mezcla: cada frase en su segundo, una sola pista de 24,5 s, normalizada a −14 LUFS
    entradas, filtros = [], []
    for i, t in enumerate(tiempos):
        entradas += ["-i", str(t["archivo"])]
        ms = round(t["inicio"] * 1000)
        filtros.append(f"[{i}:a]adelay={ms}|{ms}[f{i}]")
    mezcla = "".join(f"[f{i}]" for i in range(len(tiempos)))
    filtros.append(f"{mezcla}amix=inputs={len(tiempos)}:normalize=0,apad=whole_dur={DURACION},"
                   f"atrim=0:{DURACION},loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[out]")
    destino = salida / "assets" / "voz.mp3"
    subprocess.run(["ffmpeg", "-y", "-v", "error", *entradas, "-filter_complex", ";".join(filtros),
                    "-map", "[out]", "-ac", "2", "-c:a", "libmp3lame", "-b:a", "192k", str(destino)], check=True)
    for t in tiempos:
        t["archivo"].unlink()
        del t["archivo"]
    (salida / "assets" / "voz.json").write_text(
        json.dumps({"voz": voz, "frases": tiempos}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"→ {destino} ({duracion(destino):.2f} s, voz {voz})")


if __name__ == "__main__":
    main()
