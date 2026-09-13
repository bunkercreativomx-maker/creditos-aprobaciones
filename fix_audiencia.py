#!/usr/bin/env python
"""Ajuste de audiencia: el cliente SOLO atiende jubilados y pensionados (no activos).

Aplica las correcciones al archivo de copys y a los datos del portal, y verifica que no
quede ninguna frase que invite a trabajadores activos.
"""
import re, sys, os

MD = "/opt/data/creditos-facebook/copys-30-dias-creditos.md"

# (patrón, reemplazo) — del más específico al más general
REEMPLAZOS = [
    (r"Si trabajas en el IMSS, en el ISSSTE, en CFE, en Pemex o eres maestro… este crédito se descuenta directo de tu nómina\.",
     "Si eres pensionado o jubilado del IMSS, del ISSSTE, de CFE, de Pemex o del magisterio… este crédito se descuenta directo de tu pensión."),
    (r"¿Trabajas en el gobierno o en educación\? Escríbeme \*\*DEPENDE\*\*",
     "¿Eres pensionado o jubilado? Escríbeme **DEPENDE**"),
    (r"¿De qué dependencia recibes tu nómina\?",
     "¿De qué dependencia recibes tu pensión?"),
    (r"IMSS, ISSSTE, CFE, Pemex, educación, gobierno del estado… cada dependencia pide un comprobante distinto",
     "IMSS, ISSSTE, CFE, Pemex y magisterio… cada dependencia pide un comprobante distinto"),
    (r"Dime en los comentarios de qué dependencia eres y te digo qué documento te piden\.",
     "Dime en los comentarios de qué dependencia recibes tu pensión y te digo qué documento te piden."),
    (r"No tienes que ir al banco ni pagar en efectivo: el descuento va en tu quincena",
     "No tienes que ir al banco ni pagar en efectivo: el descuento va directo en tu pensión"),
    (r"No tienes que ir al banco ni pagar en efectivo: el descuento va en tu quincena, en pagos que ya tienes contemplados\.",
     "No tienes que ir al banco ni pagar en efectivo: el descuento va directo en tu pensión, con un monto fijo que ya tienes contemplado."),
    (r"Dime tu dependencia en los comentarios y te confirmo tu comprobante exacto antes de que vengas\.",
     "Dime de qué dependencia recibes tu pensión en los comentarios y te confirmo tu comprobante exacto antes de que vengas."),
    (r"Comparte esto en tu grupo de trabajo 👇\n+(— — —)?\n*Si en tu grupo de WhatsApp hay maestros, personal del IMSS o jubilados de CFE, este Reel les va a servir más que a nadie: explica qué documentos se piden por dependencia\.",
     "Comparte esto en tu grupo de jubilados y pensionados 👇\n\n— — —\n\nSi en tu grupo de WhatsApp hay pensionados del IMSS, jubilados del ISSSTE, maestros jubilados o pensionados de CFE, este Reel les va a servir más que a nadie: explica qué documentos se piden por dependencia."),
    (r"Mándalo a tu grupo \(el del trabajo, no el de la familia 😄\) y dime en comentarios en cuál lo compartiste\.",
     "Mándalo a tu grupo y dime en comentarios en cuál lo compartiste."),
    (r"Nos escribes por WhatsApp, te pregunto por tu dependencia y te digo qué documentos necesitas\.",
     "Nos escribes por WhatsApp, te pregunto de qué dependencia recibes tu pensión y te digo qué documentos necesitas."),
    (r"¿En qué paso te gustaría saber más\?", "¿En qué paso te gustaría saber más?"),
    (r"¿A qué hora podrías venir tú\?", "¿A qué hora podrías venir tú?"),
    (r"Si alguien de tu familia ya es cliente nuestro, etiquétalo\. Y si quieres saber si tu dependencia está con nosotros, comenta aquí\.",
     "Si alguien de tu familia ya es cliente nuestro, etiquétalo. Y si quieres saber si tu dependencia está con nosotros, comenta aquí."),
    (r"Un buró manchado no te descalifica\. 👀",
     "Un buró manchado no te descalifica. 👀"),
    (r"No pedimos historial crediticio perfecto\. Revisamos tu caso de forma individual: dependencia, antigüedad y capacidad de descuento\.",
     "No pedimos historial crediticio perfecto. Revisamos tu caso de forma individual: dependencia, antigüedad en tu pensión y capacidad de descuento."),
    (r"Cuéntame en comentarios si ya te habían dicho que no en otro lado\.",
     "Cuéntame en comentarios si ya te habían dicho que no en otro lado."),
    (r"Comenta de qué dependencia eres y te digo cuándo podrías tener tu dinero\.",
     "Comenta de qué dependencia recibes tu pensión y te digo cuándo podrías tener tu dinero."),
    (r"Doña Marta es pensionada del ISSSTE\.", "Doña Marta es pensionada del ISSSTE."),
    (r"Hasta \$500,000", "Hasta $500,000"),
    (r"IMSS, ISSSTE, CFE, maestros: todos con el mismo proceso\.",
     "Pensionados del IMSS, jubilados del ISSSTE, de CFE y maestros jubilados: todos con el mismo proceso."),
    (r"Comparte este video con tu compañero de trabajo\. Seguro hay alguien ahí que lleva meses queriendo preguntar y no se anima\.",
     "Comparte este video con tu grupo de jubilados. Seguro hay alguien ahí que lleva meses queriendo preguntar y no se anima."),
    (r"trae esto a tu cita", "trae esto a tu cita"),
    (r"Si quieres saber si tu dependencia maneja este esquema, escríbeme tu dependencia en los comentarios y te contesto\.",
     "Si quieres saber si tu dependencia maneja este esquema, escríbeme de qué dependencia recibes tu pensión en los comentarios y te contesto."),
    (r"creditoatumedida", "creditoatumedida"),
]


def aplicar(texto):
    cambios = 0
    for pat, rep in REEMPLAZOS:
        nuevo, n = re.subn(pat, rep, texto)
        if n:
            cambios += n
            texto = nuevo
    return texto, cambios


def main():
    texto = open(MD, encoding="utf-8").read()
    nuevo, n = aplicar(texto)
    # marca de auditoría
    nuevo = nuevo.replace("**Reglas aplicadas en todos:** trato de usted",
                          "**Público:** SOLO jubilados y pensionados (el cliente no atiende trabajadores activos).\n**Reglas aplicadas en todos:** trato de usted")
    open(MD, "w", encoding="utf-8").write(nuevo)
    print("reemplazos aplicados:", n)

    # auditoría: no debe quedar lenguaje de trabajador activo
    sospechosas = []
    for i, linea in enumerate(nuevo.splitlines(), 1):
        low = linea.lower()
        for frase in ["si trabajas", "compañero de trabajo", "grupo de trabajo", "recibes tu nómina",
                      "trabajadores activos", "activo en la nómina", "estás activo"]:
            if frase in low:
                sospechosas.append((i, frase, linea.strip()[:110]))
    if sospechosas:
        print("\nREVISAR — frases que aún suenan a trabajador activo:")
        for s in sospechosas:
            print(f"  línea {s[0]} [{s[1]}]: {s[2]}")
    else:
        print("auditoría: sin lenguaje de trabajador activo ✅")
    return 0


if __name__ == "__main__":
    sys.exit(main())
