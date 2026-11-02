"""Mezcla de audio: voz > efectos > musica, con ducking y -14 LUFS / -1 dBTP.

Uso: python3 tools/mix.py <voz.wav|mp3>   (desde la carpeta del proyecto)
Lee timing.json para los tiempos de las palabras y de los efectos.
Escribe audio/mix.wav (lo que usa index.html).
"""
import json
import re
import subprocess
import sys
import unicodedata

import numpy as np

SR = 48000
SFX_DIR = "audio/sfx"
MUSIC = "audio/music/mixkit-running-out-of-time-77.mp3"
BPM_FIRST_BEAT, BPM = 1.855, 130.1  # de `hyperframes beats`
COLA = 1.3


def load(path, start=0.0, dur=None):
    cmd = ["ffmpeg", "-v", "error", "-ss", f"{start:.3f}", "-i", path]
    if dur:
        cmd += ["-t", f"{dur:.3f}"]
    cmd += ["-f", "f32le", "-ac", "2", "-ar", str(SR), "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).copy()


def db(x):
    return 10 ** (x / 20)


def peak_norm(x, peak_db=-1.0):
    p = np.max(np.abs(x)) or 1.0
    return x * (db(peak_db) / p)


def rms(x):
    return float(np.sqrt(np.mean(x ** 2)) + 1e-12)


def norm(s):
    s = "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]", "", s)


def main(voice_path):
    T = json.load(open("timing.json", encoding="utf-8"))
    toks = T["tokens"]
    dur = toks[-1]["end"] + COLA
    n = int(dur * SR)

    def W(word, k=1, end=False):
        c = 0
        for t in toks:
            if norm(t["text"]) == norm(word):
                c += 1
                if c == k:
                    return t["end"] if end else t["start"]
        raise KeyError(word)

    def S(i):  # inicio de la frase i del guion
        return next(t["start"] for t in toks if t["sentence"] == i)

    # --- Voz ---
    voice = load(voice_path)[:n]
    voice = np.pad(voice, ((0, n - len(voice)), (0, 0)))
    speech_mask = np.zeros(n, dtype=bool)
    for t in toks:
        a, b = int(max(0, t["start"] - 0.05) * SR), int(min(dur, t["end"] + 0.12) * SR)
        speech_mask[a:b] = True
    v_rms = rms(voice[speech_mask]) if speech_mask.any() else rms(voice)
    voice *= db(-18) / v_rms  # voz a -18 dBFS RMS mientras habla

    # --- Musica: un pulso cae justo en la revelacion ("Haval") ---
    period = 60.0 / BPM
    t_rev = W("Haval")
    offset = (BPM_FIRST_BEAT - t_rev) % period
    music = load(MUSIC, start=offset, dur=dur + 0.5)[:n]
    music = np.pad(music, ((0, n - len(music)), (0, 0)))
    music *= db(-18) / rms(music)  # mismo RMS que la voz antes del ducking
    # habla -> -16 dB respecto de la voz; entre frases -> -8 dB; nunca silencio
    sm = speech_mask.astype(np.float32)
    # suavizar (ataque ~60 ms, relajacion ~300 ms) con dos medias moviles
    def smooth(x, w):
        k = np.ones(int(w * SR), dtype=np.float32) / int(w * SR)
        return np.convolve(x, k, mode="same")
    env_speech = np.clip(smooth(np.maximum(sm, smooth(sm, 0.06) > 0.01), 0.3), 0, 1)
    gain_db = -8.0 - 8.0 * env_speech
    # fade de entrada muy corto y salida suave al final
    fade = np.ones(n, dtype=np.float32)
    fi = int(0.03 * SR)
    fade[:fi] = np.linspace(0, 1, fi)
    fo = int(0.7 * SR)
    fade[-fo:] = np.linspace(1, 0.25, fo)
    music *= (db(gain_db) * fade)[:, None]

    # --- Efectos reales (biblioteca media-use, Pixabay), cada uno nivelado al mismo pico ---
    def sfx(name, t, gain, seg=None):
        x = load(f"{SFX_DIR}/{name}.mp3")
        if seg:
            x = x[int(seg[0] * SR): int(seg[1] * SR)]
        x = peak_norm(x) * db(gain)
        a = int(t * SR)
        if a < 0:
            x, a = x[-a:], 0
        b = min(n, a + len(x))
        out[a:b] += x[: b - a]

    out = np.zeros((n, 2), dtype=np.float32)
    fr = 1 / 30  # "whoosh 2 cuadros antes"
    plan = [
        ("pop", W("Brasil", 1), -15),                       # sello BRASIL 2026
        ("whoosh", S(1) - 0.2 - 2 * fr, -13),               # el auto sale disparado / entran las tarjetas
        ("click", W("2026", 1), -17),
        ("whoosh", W("perdió") - 2 * fr, -14),              # las tarjetas se dan vuelta
        ("impact-bass-1", W("perdió") + 0.45, -15),
        ("pop", W("cuál", 1), -16),
        ("whoosh", S(2) - 0.08 - 2 * fr, -14),              # zoom al auto
        ("pop", W("híbrido", 1), -16),
        ("pop", W("china"), -17),
        ("whoosh", S(3) - 0.1 - 2 * fr, -15),
        ("ping", W("patentamientos", end=True) - 0.15, -19),
        ("pop", W("486"), -15),
        ("whoosh", S(4) - 0.12 - 2 * fr, -14),
        ("click", W("octubre"), -16),
        ("ping", W("2.000"), -18),
        ("whoosh", S(5) - 0.14 - 2 * fr, -15),
        ("pop", W("versiones"), -18),
        ("pop", W("desde"), -18),
        ("whoosh", S(6) - 2 * fr, -14),                     # el auto vuelve
        ("ping", W("vendida", 2), -16),
        ("riser", W("Haval") - 3.2, -16, (10.03 - 3.2, 10.03)),
        ("impact-bass-1", W("Haval") - 0.04, -9),
        ("pop", S(8), -15),                                 # boton
        ("pop", W("PRO"), -15),
    ]
    for item in plan:
        sfx(*item)

    mix = voice + out + music
    tmp = "audio/mix-pre.wav"
    write_wav(tmp, mix)
    # -14 LUFS integrado, pico -1 dBTP (dos pasadas de loudnorm)
    meas = subprocess.run(["ffmpeg", "-hide_banner", "-i", tmp, "-af", "loudnorm=I=-14:TP=-1.0:LRA=11:print_format=json", "-f", "null", "-"],
                          capture_output=True, text=True).stderr
    m = json.loads(meas[meas.rindex("{"): meas.rindex("}") + 1])
    af = (f"loudnorm=I=-14:TP=-1.0:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af", af, "-ar", str(SR), "audio/mix.wav"], check=True)
    subprocess.run(["rm", "-f", tmp])
    print(f"audio/mix.wav listo · {dur:.2f} s · musica desde {offset:.3f} s · {len(plan)} efectos")


def write_wav(path, x):
    x = np.clip(x, -1, 1)
    pcm = (x * 32767).astype("<i2").tobytes()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "s16le", "-ac", "2", "-ar", str(SR), "-i", "-", path], input=pcm, check=True)


if __name__ == "__main__":
    main(sys.argv[1])
