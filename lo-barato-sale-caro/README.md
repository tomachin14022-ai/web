# Lo Barato Sale Caro (prueba de 1–2 semanas)

- `web/index.html`: página de comparaciones (publicada como artifact de Claude).
- `videos/datos/*.json`: datos de cada comparación (precios, rendimientos, textos).
- `videos/generar.py`: genera el video de una comparación desde su JSON:
  `python3 generar.py datos/01-impresora.json 01-impresora` y después `render` con HyperFrames.

Pendiente: links de afiliado y precios reales de Mercado Libre (impresora, aire, cafetera).
