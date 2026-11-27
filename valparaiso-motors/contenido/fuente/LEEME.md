# Cómo se regenera el calendario

- `datos.py`: piezas, tareas, anuncios, evento, códigos, tablero y fuentes. El Día D de ejemplo es el sábado 19/12/2026.
- `guiones.py`: junta el banco de guiones (ver abajo).
- `datos_guiones.py`: los datos verificados de cada modelo (hoja Datos de los autos), las cuentas de Córdoba con sus supuestos (hoja Cuentas de Córdoba, con fórmulas) y los errores encontrados (hoja Errores a corregir). Las notas de la investigación, con todos los links, están en `research_notes/Guiones con datos reales/`.
- `armar.py`: arma `../Calendario de contenido Valparaiso Motors.xlsx` con openpyxl.

```sh
python3 armar.py
python3 <skill xlsx>/scripts/recalc.py "../Calendario de contenido Valparaiso Motors.xlsx" 90   # recalcula y verifica que no haya errores
```

La guía se edita en `../Guía paso a paso del calendario de contenido.md` y se convierte con
`pandoc "<guía>.md" -o "<guía>.docx" --reference-doc ref.docx` (después, LibreOffice a PDF).

## Banco de ideas y guiones

- Los guiones viven en `guiones_ent.py` (E, entretener), `guiones_edu.py` (D, educar) y `guiones_ven.py` (V, vender). Los carruseles (C) y las piezas de todos los días (O) salen de `guiones_base.py`; `guiones.py` los junta.
- `python3 banco.py` escribe `../Banco de ideas y guiones.md`; después `pandoc … --reference-doc ref_horizontal.docx` y LibreOffice a PDF.
- `MAPA_GUIONES` en `datos.py` dice qué guion usa cada pieza del calendario.
- Cada guion lleva `honesto` (la limitación que dice en voz alta) y `fuentes` (IDs de `datos_guiones.DATOS` y `CUENTAS`). Si cambia un dato, se cambia en `datos_guiones.py` y en el texto de los guiones que lo citan (buscar el ID).
