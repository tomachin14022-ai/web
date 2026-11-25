# Cómo se regenera el calendario

- `datos.py`: piezas, tareas, anuncios, evento, códigos, tablero y fuentes. El Día D de ejemplo es el sábado 19/12/2026.
- `guiones.py`: los 41 guiones (resumen y escenas), escritos para que los entienda alguien de 15 años.
- `armar.py`: arma `../Calendario de contenido Valparaiso Motors.xlsx` con openpyxl.

```sh
python3 armar.py
python3 <skill xlsx>/scripts/recalc.py "../Calendario de contenido Valparaiso Motors.xlsx" 90   # recalcula y verifica que no haya errores
```

La guía se edita en `../Guía paso a paso del calendario de contenido.md` y se convierte con
`pandoc "<guía>.md" -o "<guía>.docx" --reference-doc ref.docx` (después, LibreOffice a PDF).
