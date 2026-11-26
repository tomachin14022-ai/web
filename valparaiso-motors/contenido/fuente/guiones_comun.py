"""Constantes y ayuda para escribir los guiones del banco."""
import guiones_base as _base

CTA = "Pedinos precio y financiación de cualquiera de nuestros autos."
LEGAL = _base.LEGAL
FIJADO = "Si querés precio y cuota, comentá {k} y te escribimos por mensaje 📩 (si no nos seguís, te llega a Solicitudes)."
MSG = "Hola, vengo del video {k}. Quiero precio y financiación."
FIN_ENT = "PEDINOS PRECIO Y FINANCIACIÓN"

TODOS, KM, FAM, USADO, CAMPO, ELEC, SEG = (_base.TODOS, _base.KM, _base.FAM, _base.USADO, _base.CAMPO, _base.ELEC, _base.SEG)


def v(id_, pieza, objetivo, publico, estructura, idea, formato, aparece, gancho, gancho_b, escenas, tomas, descripcion,
      hashtags, codigo, ojo="", fijado=None, mensaje=None, dificultad="Media", por_que=""):
    return dict(id=id_, pieza=pieza, objetivo=objetivo, publico=publico, estructura=estructura, idea=idea, formato=formato,
                aparece=aparece, gancho=gancho, gancho_b=gancho_b, escenas=escenas, tomas=tomas, descripcion=descripcion,
                hashtags=hashtags, codigo=codigo, ojo=ojo, dificultad=dificultad, por_que=por_que,
                fijado=FIJADO.format(k=codigo) if fijado is None and codigo else (fijado or ""),
                mensaje=MSG.format(k=codigo) if mensaje is None and codigo else (mensaje or ""))
