"""Banco de ideas y guiones de Valparaiso Motors (sin fechas).

Todo escrito para que lo entienda alguien de 15 años: una idea por pieza, frases cortas, cada frase con su imagen,
una promesa en los primeros segundos que se paga al final y estructuras distintas para no aburrir.
IDs: E = Entretener · D = Educar · V = Vender · C = Carrusel · O = Operativo (historias, Estados, vivos, mensajes, Google, YouTube).
"""
import copy

import guiones_base as _base
from guiones_edu import EDUCAR
from guiones_ent import ENTRETENER
from guiones_ven import VENDER

_POR_ID = {g["id"]: g for g in _base.GUIONES}
_REID = [
    ("C01", "G35", "Carrusel con texto por placa"), ("C02", "G36", "Carrusel de preguntas y respuestas"),
    ("C03", "G37", "Carrusel comparativo"), ("C04", "G38", "Carrusel explicativo"),
    ("C05", "G39", "Carrusel con un papel marcado"), ("C06", "G40", "Carrusel de fotos con una idea por placa"),
    ("C07", "G13", "Carrusel de precios, un modelo por placa"), ("C08", "G33", "Plantilla de carrusel"),
    ("O01", "G06", "Historias diarias"), ("O02", "G07", "Historias y vivo"), ("O03", "G20", "Vivo"),
    ("O04", "G21", "Video largo con capítulos"), ("O05", "G26", "Publicación de Google"), ("O06", "G27", "Estados de WhatsApp"),
    ("O07", "G28", "Historias de la semana"), ("O08", "G29", "Mensajes de WhatsApp"),
]
OTROS = []
for nuevo, viejo, estructura in _REID:
    g = copy.deepcopy(_POR_ID[viejo])
    g["id"] = nuevo
    g["estructura"] = estructura
    g.setdefault("dificultad", "Fácil" if nuevo.startswith("O") else "Media")
    g.setdefault("por_que", "")
    OTROS.append(g)

GUIONES = ENTRETENER + EDUCAR + VENDER + OTROS
EQUIVALENCIAS = {viejo: nuevo for nuevo, viejo, _ in _REID}
