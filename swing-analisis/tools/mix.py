"""Mezcla: voz > efectos > musica. Musica ~8 dB debajo de la voz entre frases y 8 dB mas
cuando habla (nunca en silencio). Cada efecto se nivela al mismo pico antes de su volumen.

Uso: python -I mix.py VOZ.wav MUSICA.wav CUES.json CARPETA_SFX DURACION SALIDA.wav
CUES.json: [[segundo, "archivo.wav", ganancia_dB], ...]
Despues normalizar a -14 LUFS / -1 dBTP con ffmpeg loudnorm (sobre el MP4 final).
"""
import json
import sys

import numpy as np
import soundfile as sf

voz_p, mus_p, cues_p, sfx_dir, dur, out = sys.argv[1:7]
SR = 48000; N = int(float(dur) * SR)
db = lambda x: 10 ** (x / 20)

v, sr = sf.read(voz_p); assert sr == SR, sr
v = v if v.ndim == 1 else v.mean(1)
mix = np.zeros(N); mix[: min(N, len(v))] += v[:N]

# actividad de la voz (ventanas de 20 ms) -> envolvente con ataque y relajacion
win = SR // 50
e = np.array([np.sqrt(np.mean(v[i:i + win] ** 2)) for i in range(0, len(v), win)])
speaking = (e > 0.02).astype(float)
env = np.zeros_like(speaking); a_up, a_dn = 1 - np.exp(-1 / 4), 1 - np.exp(-1 / 18)
for i in range(1, len(env)):
    env[i] = env[i - 1] + (a_up if speaking[i] > env[i - 1] else a_dn) * (speaking[i] - env[i - 1])
env = np.interp(np.arange(N), np.arange(len(env)) * win, env)
v_rms = np.sqrt(np.mean(v[np.repeat(speaking, win)[: len(v)] > 0] ** 2))

m, sr = sf.read(mus_p); m = m if m.ndim == 1 else m.mean(1)
m = np.tile(m, int(np.ceil(N / len(m))) + 1)[:N]
m = m / (np.sqrt(np.mean(m ** 2)) + 1e-9) * v_rms  # musica al mismo RMS que la voz...
gain = db(-8) * (1 - env) + db(-16) * env  # ...y despues 8 dB abajo, 16 dB abajo cuando habla
fade = np.ones(N); fl = int(1.2 * SR); fade[-fl:] = np.linspace(1, 0, fl); fade[: SR // 5] = np.linspace(0, 1, SR // 5)
mix += m * gain * fade

for t, fn, g in json.load(open(cues_p)):
    s, sr = sf.read(f"{sfx_dir}/{fn}"); s = s if s.ndim == 1 else s.mean(1)
    s = s / (np.abs(s).max() + 1e-9) * db(-3)  # mismo pico para todos
    i = int(t * SR); j = min(N, i + len(s))
    mix[i:j] += s[: j - i] * db(g)
peak = np.abs(mix).max()
if peak > 0.98:
    mix = mix / peak * 0.98
sf.write(out, mix, SR)
print("listo", out, "pico", round(float(peak), 3))
