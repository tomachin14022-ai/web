"""Inserta silencios en la voz (y corre los tiempos de las palabras que siguen).

Uso: python3 tools/pausas.py <voz> <voz-salida.wav>
Edita timing.json en el lugar. Las pausas se definen abajo: despues de la palabra
(n-esima aparicion) se agregan esos segundos de silencio.
"""
import json
import re
import subprocess
import sys
import unicodedata

PAUSAS = [
    # ("H6", 1, 0.7),  # ejemplo: 0,7 s de silencio despues de "La Haval H6" (la voz de ElevenLabs ya trae la pausa)
]
SR = 48000


def norm(s):
    s = "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]", "", s)


def main(src, dst):
    T = json.load(open("timing.json", encoding="utf-8"))
    toks = T["tokens"]
    cuts = []
    for word, k, secs in PAUSAS:
        c = 0
        for i, t in enumerate(toks):
            if norm(t["text"]) == norm(word):
                c += 1
                if c == k:
                    cuts.append((t["end"], secs, i))
                    break
    cuts.sort()
    # corrimiento de tiempos
    for at, secs, i in reversed(cuts):
        for t in toks[i + 1:]:
            t["start"] = round(t["start"] + secs, 3)
            t["end"] = round(t["end"] + secs, 3)
        T["voiceEnd"] = round(T["voiceEnd"] + secs, 3)
    json.dump(T, open("timing.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # audio: cortar y pegar silencios con ffmpeg (concat de segmentos)
    parts, prev = [], 0.0
    for at, secs, _ in cuts:
        cut = at + 0.05
        parts.append(f"[0:a]atrim={prev}:{cut},asetpts=PTS-STARTPTS[a{len(parts)}]")
        parts.append(f"aevalsrc=0:d={secs}:s={SR}:c=stereo[s{len(parts)}]")
        prev = cut
    parts.append(f"[0:a]atrim=start={prev},asetpts=PTS-STARTPTS[a{len(parts)}]")
    labels = "".join(f"[{p.split('[')[-1]}" for p in parts)
    fc = ";".join(parts) + f";{labels}concat=n={len(parts)}:v=0:a=1[out]"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-filter_complex", fc, "-map", "[out]",
                    "-ar", str(SR), "-ac", "2", dst], check=True)
    print(f"{len(cuts)} pausa(s) agregada(s) · {dst}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
