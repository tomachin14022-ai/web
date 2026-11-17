# Revisión: anuncio de producto de ejemplo (10 s, 1080x1920)

## Qué es
Demo del producto "foto de celular → anuncio": la foto real del producto en el cuadro 0, escaneo, recorte del producto, cambio de fondo, título, 3 beneficios, precio y botón.

## Decisiones
- El producto no se genera con IA: es el recorte de la foto real (fondo quitado con `hyperframes remove-background` y máscara limpiada a mano para sacar la sombra con arena).
- Textos dentro de la zona segura común de TikTok, Reels y Shorts (x 120–888 arriba; x 120–780 debajo de y 840; y 288–1248). Por eso la parte de abajo queda alineada a la izquierda.
- Textos, precio, botón y tienda son variables (para generar otro anuncio cambiando datos y foto).

## Qué se midió
- `hyperframes check`: sin errores ni advertencias.
- Cuadros del render revisados en 0; 1,4; 3,3; 6 y 8,6 s.

## Lo que no se revisó o falta
- Sin sonido (no se pidió). Un anuncio real llevaría música y efectos.
- Los beneficios ("livianas", "ventiladas", "se lavan con agua") y el precio son de ejemplo.

## Toma más débil
El final (7,5–10 s) deja vacía la mitad de abajo por la zona segura; con más tiempo sumaría una textura o un detalle del producto ahí.
