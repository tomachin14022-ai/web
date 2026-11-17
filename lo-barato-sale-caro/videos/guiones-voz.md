# Guiones de voz · Lo barato sale caro

Texto para grabar o pegar en ElevenLabs. Cada video dura 24,5 s y cada frase tiene que caer sobre su escena. Si la grabás vos, mandame el audio de cada video (o cada frase por separado) y lo acomodo.

## 1. Impresora

La impresora barata te sale casi el doble.
¿Cuál comprás? Mirá cuánto cuesta usarla.
Con cartuchos: doscientos catorce por hoja.
Con tanque de tinta: menos de cinco. Cuarenta y cuatro veces menos.
Si imprimís cien hojas por mes…
en el mes doce se da vuelta. Desde ahí, gana la cara.
En tres años, ahorrás más de quinientos mil.
Los links de las dos están en la bio.

## 2. Cafetera

La cafetera barata te sale más del doble.
¿Cuál comprás? Mirá cuánto cuesta cada café.
Con cápsulas: dos mil cuatrocientos por café.
Con café en grano: setecientos tres pesos. Tres veces menos.
Si tomás dos cafés por día…
en el mes siete se da vuelta. Desde ahí, gana la cara.
En tres años, ahorrás casi tres millones.
Los links de las dos están en la bio.

## 3. Aire acondicionado

El aire barato te sale más caro.
¿Cuál comprás? Mirá cuánta luz gasta cada uno.
El común: ciento setenta y tres por hora.
El inverter, unos ciento veintiuno. Treinta por ciento menos.
Ocho horas por día, cinco meses al año…
en el mes veintidós se da vuelta. Desde ahí, gana el caro.
En cinco años, ahorrás casi doscientos mil.
Los links de los dos están en la bio.

---

## En qué segundo entra cada frase (igual en los tres videos)

| Frase | Entra en | Tiene hasta |
|---|---|---|
| 1 (gancho) | 0,0 s | 2,6 s |
| 2 (¿Cuál comprás?) | 2,7 s | 6,1 s |
| 3 (la barata) | 6,2 s | 8,6 s |
| 4 (la cara) | 8,75 s | 13,1 s |
| 5 (el uso) | 13,25 s | 15,7 s |
| 6 (se da vuelta) | 15,85 s | 19,7 s |
| 7 (el ahorro) | 19,8 s | 22,3 s |
| 8 (los links) | 22,4 s | 24,3 s |

Para regenerar la voz automática: `python3 voz.py datos/02-cafetera.json 02-cafetera` (voz es-AR-TomasNeural; con `--voz es-AR-ElenaNeural` usa la voz femenina) y después `python3 generar.py` + render.
