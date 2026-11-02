"""Saca tramos de la voz (y sus palabras) y corre los tiempos de lo que sigue.

Uso: python3 tools/recorte.py <voz> <voz-salida.wav>
Edita timing.json en el lugar. Los cortes van en segundos de la voz original,
medidos en los silencios (ver la forma de onda).
"""
import json
import subprocess
import sys

CORTES = [
    (13.42, 15.48),  # "Es la Haval H6." (pedido del dueño: la foto y el nombre aparecen recien en "Pedinos")
]
SR = 48000


def main(src, dst):
    T = json.load(open("timing.json", encoding="utf-8"))
    toks = T["tokens"]
    for a, b in sorted(CORTES, reverse=True):
        d = b - a
        toks = [t for t in toks if not (t["start"] >= a - 0.05 and t["end"] <= b + 0.05)]
        for t in toks:
            if t["start"] >= b - 0.05:
                t["start"] = round(t["start"] - d, 3)
                t["end"] = round(t["end"] - d, 3)
        T["voiceEnd"] = round(T["voiceEnd"] - d, 3)
    # renumerar frases sin huecos
    seen = {}
    for t in toks:
        t["sentence"] = seen.setdefault(t["sentence"], len(seen))
    T["tokens"] = toks
    json.dump(T, open("timing.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    keep, prev = [], 0.0
    for a, b in sorted(CORTES):
        keep.append((prev, a))
        prev = b
    keep.append((prev, None))
    parts, labels = [], ""
    for i, (a, b) in enumerate(keep):
        trim = f"atrim=start={a}" + (f":end={b}" if b is not None else "")
        parts.append(f"[s{i}]{trim},asetpts=PTS-STARTPTS[p{i}]")
        labels += f"[p{i}]"
    split = f"[0:a]aresample={SR},aformat=channel_layouts=stereo,asplit={len(keep)}" + "".join(f"[s{i}]" for i in range(len(keep)))
    fc = split + ";" + ";".join(parts) + f";{labels}concat=n={len(keep)}:v=0:a=1[out]"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-filter_complex", fc, "-map", "[out]", "-ar", str(SR), dst], check=True)
    print(f"{len(CORTES)} corte(s) · {dst}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
