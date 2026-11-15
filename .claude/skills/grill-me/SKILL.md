---
name: grill-me
description: Pone a prueba un plan o un diseño con hasta 5 preguntas, de a una, cada una con la opción recomendada primero, hasta que no quede ninguna decisión importante abierta. Usala cuando el usuario diga "grill me", "poneme a prueba", "haceme preguntas", "estresá este plan" o pida revisar un plan antes de producirlo (un reel, una campaña, una promo, un flujo de mensajes).
---

# Poner a prueba un plan (máximo 5 preguntas)

Entrevistá al usuario sobre su plan hasta que las decisiones que importan queden resueltas. El dueño quiere el trabajo terminado, no muchas preguntas: cada pregunta tiene que ganarse su lugar.

## Antes de preguntar

1. Leé lo que ya existe: `CLAUDE.md`, los archivos del proyecto y lo que se dijo en la conversación. No preguntes nada que ya esté resuelto ahí (marca, colores, formato, zonas seguras, reglas legales, tono).
2. Armá la lista de decisiones abiertas y ordenala por impacto: primero las que más cambian el resultado o las que más cuesta cambiar después (por ejemplo, una que obliga a volver a renderizar).
3. Si una decisión depende de otra, preguntá primero la de arriba.

## Cómo preguntar

- **Máximo 5 preguntas** en total.
- **Una por vez**, con la herramienta **AskUserQuestion**. Nunca escribas las preguntas como texto suelto.
- Entre 2 y 4 opciones concretas por pregunta, pensadas para este plan. Nada de "Sí / No" salvo que la decisión sea de verdad de dos caminos.
- **La primera opción es la que recomendás**, con "(Recomendado)" al final del nombre y el porqué en la descripción, en una frase.
- Cada pregunta se entiende sola: el usuario puede ver solo el cuadro de la pregunta, sin lo que escribiste antes.
- Español rioplatense, claro y profesional.

## Después de cada respuesta

- Confirmá la decisión en una frase y pasá a la siguiente pregunta.
- Si la respuesta resuelve otras decisiones de la lista, sacalas.
- Si el usuario dice "con eso alcanza", "decidí vos" o algo parecido, cortá y pasá al resumen.

## Al terminar

Cuando se acaban las 5 preguntas o no quedan decisiones abiertas:

1. **Resumen corto** con:
   - lo que se decidió;
   - lo que decidiste vos sin preguntar, con el porqué en una línea ("si no te gusta, avisame");
   - los datos que hay que verificar antes de publicar.
2. Si el pedido era producir algo (un guion, un reel, un carrusel), seguí con el trabajo usando esas decisiones. No pidas permiso otra vez.

---

Basada en [grill-me](https://github.com/RobMitt/grill-me-skill) de RobMitt, adaptada para Valparaiso Motors: en español, con la opción recomendada primero y un máximo de 5 preguntas.
