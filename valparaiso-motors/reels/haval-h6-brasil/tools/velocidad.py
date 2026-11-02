"""Acelera la voz desde una palabra hasta el final (sin cambiar el tono) y corre los tiempos.

Uso: python3 tools/velocidad.py <voz> <voz-salida.wav>
Edita timing.json en el lugar. Se configura abajo: desde la palabra (n-esima aparicion),
con el factor de velocidad. El corte se hace en el silencio justo antes de esa palabra.
"""
import json
import re
import subprocess
import sys
import unicodedata

DESDE = ("¿Pasará", 1)   # "¿Pasará lo mismo en Argentina?" hasta el final
FACTOR = 1.05
SR = 48000


def norm(s):
    s = "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]", "", s)


def main(src, dst):
    T = json.load(open("timing.json", encoding="utf-8"))
    toks = T["tokens"]
    word, k = DESDE
    c, idx = 0, None
    for i, t in enumerate(toks):
        if norm(t["text"]) == norm(word):
            c += 1
            if c == k:
                idx = i
                break
    prev_end = toks[idx - 1]["end"] if idx else 0.0
    cut = round(max(prev_end, toks[idx]["start"] - 0.08), 3)  # en el silencio previo
    for t in toks[idx:]:
        t["start"] = round(cut + (t["start"] - cut) / FACTOR, 3)
        t["end"] = round(cut + (t["end"] - cut) / FACTOR, 3)
    T["voiceEnd"] = round(cut + (T["voiceEnd"] - cut) / FACTOR, 3)
    json.dump(T, open("timing.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    fc = (f"[0:a]aresample={SR},aformat=channel_layouts=stereo,asplit=2[a][b];"
          f"[a]atrim=0:{cut},asetpts=PTS-STARTPTS[p1];"
          f"[b]atrim=start={cut},asetpts=PTS-STARTPTS,rubberband=tempo={FACTOR}:pitchq=quality:formant=preserved[p2];"
          f"[p1][p2]concat=n=2:v=0:a=1[out]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-filter_complex", fc, "-map", "[out]", "-ar", str(SR), dst], check=True)
    print(f"voz x{FACTOR} desde {cut:.2f} s ({word}) · {dst}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
