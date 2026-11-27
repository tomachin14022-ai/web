# Cómo se regenera el calendario

## El calendario final (lo que se usa)

`../Calendario Valparaiso Motors.xlsx`: **una sola hoja**, una fila por día del 27/11/2026 al 28/02/2027, con todo lo de ese día:
qué se publica con su guion completo, qué se pega, qué se confirma antes, qué se graba, qué se edita, las tareas y lo de todos los días.
`../Calendario Valparaiso Motors (para leer).pdf` es lo mismo, día por día, para leer en el celular o imprimir.

- `calendario_plan.py`: qué pasa cada día (publicaciones, grabaciones, tareas de la inauguración y de anuncios, contexto de Córdoba).
  La inauguración está el sábado 19/12 (noche VIP el 18/12): si cambia, se cambian `DIA_D`, `VIP` y las fechas de las tareas que dicen "Inauguración".
- `calendario.py`: arma la planilla y el Markdown de la versión para leer. Toma los guiones del banco (`guiones_ent.py`, `guiones_edu.py`,
  `guiones_ven.py`, más los carruseles y las respuestas que están en `calendario_plan.py`) y los datos y cuentas de `datos_guiones.py`.

```sh
python3 calendario.py /tmp/cal                      # escribe la planilla y /tmp/cal/Calendario Valparaiso Motors.md
pandoc "/tmp/cal/Calendario Valparaiso Motors.md" -o "/tmp/cal/Calendario Valparaiso Motors (para leer).docx" --reference-doc ref_horizontal.docx
soffice --headless --convert-to pdf --outdir /tmp/cal "/tmp/cal/Calendario Valparaiso Motors (para leer).docx"
cp "/tmp/cal/Calendario Valparaiso Motors (para leer).pdf" ..
```

Si cambia el precio de la nafta o de la luz: se cambian `SUPUESTOS` en `datos_guiones.py` y se vuelve a correr (las cuentas de "Antes de publicar" se recalculan).
Las notas de la investigación, con todos los links, están en `research_notes/Guiones con datos reales/` y `research_notes/Calendario de contenido Valparaiso Motors/`.

## Versiones anteriores (archivo)

`../versiones anteriores/` guarda la planilla de 18 hojas, el banco de 95 guiones y la guía paso a paso. Se regeneran con `armar.py` y `banco.py`
(`datos.py`, `guiones.py`, `guiones_base.py`). El banco completo sigue siendo la fuente de los guiones que usa el calendario.
