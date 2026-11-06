# Error en el análisis del swing 2 (no publicar el reel ni el informe)

El reel y el informe dicen que **la bajada está en plano** ("56–61°, dentro de la zona"). Es incorrecto: el swing es
**over the top**. Se midió solo el ángulo de la varilla y no dónde estaban las manos y la varilla respecto del plano de subida.

Evidencia medida en el video (desde atrás, escala ≈0,21 cm por pixel):
- A la misma altura, las manos en la bajada pasan **14 a 23 cm por encima/afuera** de su camino de subida
  (700 px: +14 cm · 800 px: +20 cm · 900 px: +23 cm · 1000 px: +19 cm). Criterio V1: en P5, ¿el palo está por encima o
  por debajo del plano de subida?
- Varilla en P5 (bajada, brazo paralelo, cuadro 60): **61°**. En P3 (subida, cuadro 13): **47°**. Se empina 14° en vez de aplanarse.
- Tope (P4, cuadro 40) **cruzado**: la varilla apunta a la derecha del objetivo.
- Patrón completo: sale por dentro y plano → se cruza en el tope → baja por encima (over the top). Según V1 produce
  pulls, slices y contacto débil; según TPI es una de las causas principales del slice.

Lo que sí sigue en pie: se para en la subida (rodilla de atrás 161° → 177°, tronco 46° → 34°), vuelve a bajar en la bajada
(cabeza ↓9 cm desde el tope, talón de atrás temprano) y la cola se mantiene sobre su línea hasta el impacto.

Verificación automática (06/11/2026, `tools/plano_check.py`, resultado en `plano_check.json`): veredicto **OVER THE TOP**.
Manos de bajada contra subida a la misma altura: mediana +18,7 cm (rango 15,6–19,2, alturas 840–1010 px); varilla P5 62,8° contra
P3 46,4° (+16,4°); cabeza del palo hasta 23 cm por fuera de las manos entre P4 y P5. La cámara estaba girada 8,5° (punto de fuga
330,790), así que el slot de TPI no se usó para decidir. Las diferencias con los números de arriba son por el tramo de alturas
(ahora entre P3/P5 y P1/P7) y por la definición del ángulo.
