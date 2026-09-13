#!/usr/bin/env python
"""Genera calendar.json y ads.json para el portal de aprobación de Créditos a tu medida.

Fuente del copy: /opt/data/creditos-facebook/copys-30-dias-creditos.md (un día por sección).
El portal NO incluye el warm up ni el cover, por indicación del cliente.
"""
import json, re, os

SRC = "/opt/data/creditos-facebook/copys-30-dias-creditos.md"
HERE = os.path.dirname(os.path.abspath(__file__))

VISUAL_BY_FORMAT = {
    "Reel": "posts/plantilla-reel.png",
    "Story + Grupos": "posts/plantilla-story.png",
    "Story": "posts/plantilla-story.png",
    "Carrusel": "posts/plantilla-carrusel.png",
    "Carrusel 4 tarjetas": "posts/plantilla-carrusel.png",
    "Foto": "posts/plantilla-post.png",
    "Imagen": "posts/plantilla-post.png",
    "Imagen + pregunta": "posts/plantilla-post.png",
    "Foto real": "posts/plantilla-post.png",
    "Imagen + carrusel": "posts/plantilla-post.png",
}

# Ejemplos ya producidos: se muestran como arte real de esos días
VISUAL_OVERRIDE = {}   # todas las piezas llevan gente: posts/dia-NN.png

EXTRA = {
    "Día 19": "Solo se publica con carta de autorización firmada del cliente. Si no está firmada a esa fecha, se sustituye por la foto de oficina del Día 13 o por un Reel de preguntas frecuentes.",
    "Día 26": "Solo con carta de autorización firmada de cada persona. Si no están, se graba al asesor explicando las cuatro dependencias.",
}

text = open(SRC, encoding="utf-8").read()
blocks = re.split(r"\n### ", text)
posts = []
for b in blocks[1:]:
    head, _, rest = b.partition("\n")
    m = re.match(r"Día (\d+) — (.+?) · (.+?) · (.+)$", head.strip())
    if not m:
        raise SystemExit("Encabezado no reconocido: " + head)
    day = int(m.group(1))
    date_label, fmt, pillar = m.group(2), m.group(3), m.group(4)
    # el copy es todo lo que va antes de las notas de producción / hashtags
    copy_lines, prod_lines = [], []
    for line in rest.splitlines():
        s = line.strip()
        if not s or s == "---":
            if copy_lines and not prod_lines:
                copy_lines.append("")
            continue
        if s.startswith("**⚠️") or s.startswith("**📹") or s.startswith("**🖼️") or s.startswith("**📷"):
            prod_lines.append(re.sub(r"\*\*", "", s).strip())
            continue
        if s.startswith("`#"):
            continue
        if s.startswith("**") and s.endswith("**"):
            continue
        if prod_lines:
            prod_lines.append(s)
        else:
            copy_lines.append(s)
    copy_text = "\n".join(l for l in copy_lines).strip()
    copy_text = re.sub(r"\n{3,}", "\n\n", copy_text)
    production = " ".join(prod_lines).strip()
    if date_label in EXTRA:
        production = (production + " " + EXTRA[date_label]).strip()

    posts.append({
        "id": day,
        "day": day,
        "date": date_label,
        "format": fmt,
        "pillar": pillar,
        "copy": copy_text,
        "production": production,
        "visuals": VISUAL_OVERRIDE.get(day) or [f"posts/dia-{day:02d}.png"],
        "visualNote": "Propuesta con foto documental de jubilados y pensionados; la foto definitiva de este día se produce o valida contigo",
    })

posts.sort(key=lambda p: p["day"])
assert len(posts) == 30, f"esperaba 30 días, hay {len(posts)}"

json.dump({"client": "Créditos a tu medida", "campaign": "14 sep – 13 oct 2026", "posts": posts},
          open(os.path.join(HERE, "calendar.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

ads = [
    {"id": "META-01", "name": "Testimonio en video", "objective": "Mensajes a WhatsApp",
     "audience": "Amplia, 55-80 años (jubilados y pensionados), Ciudad Juárez + 25 km",
     "creative": "Cliente real contando su proceso (con carta de autorización). Video vertical 9:16.",
     "primary": ["Doña Marta es pensionada del ISSSTE y llevaba meses queriendo arreglar su casa. Vino a la oficina, revisamos su caso y lo resolvimos. Si tú también lo has estado posponiendo, escríbenos y te decimos exactamente qué necesitas.",
                  "¿Llevas meses pensando en pedir tu crédito y no te animas? Nunca vas a estar seguro hasta preguntar. Un asesor te dice si tu caso califica, sin compromiso."],
     "headline": ["Pensionados y jubilados: crédito con descuento de tu pensión", "Pregúntanos sin compromiso"],
     "cta": "Enviar mensaje"},
    {"id": "META-02", "name": "Demo de proceso", "objective": "Mensajes a WhatsApp",
     "audience": "Amplia, 55-80 años (jubilados y pensionados), Ciudad Juárez + 25 km",
     "creative": "Asesor a cuadro explicando los 3 requisitos en 20 s. Vertical y cuadrada.",
     "primary": ["Son 3 requisitos y no dependen de tu historial crediticio. Te explicamos cuáles son según tu dependencia antes de que vayas a la oficina.",
                  "IMSS, ISSSTE, CFE, Pemex y magisterio: cada dependencia pide un comprobante distinto. Mándanos de qué dependencia recibes tu pensión y te decimos exactamente qué llevar."],
     "headline": ["3 requisitos, sin filas", "Te decimos qué llevar"],
     "cta": "Enviar mensaje"},
    {"id": "META-03", "name": "Carrusel por dependencia", "objective": "Mensajes a WhatsApp",
     "audience": "Amplia, 55-80 años (jubilados y pensionados), Ciudad Juárez + 25 km",
     "creative": "Carrusel de 4 tarjetas: cada dependencia con su comprobante de ingresos.",
     "primary": ["¿Sabes qué comprobante de ingresos te piden? Depende de tu dependencia: NSS del IMSS, número de ISSSTE, ficha de CFE o Pemex, RFC o CURP si eres maestro jubilado.",
                  "Preparamos la lista completa por dependencia para que no te hagan ir dos veces. Desliza y dime la tuya por WhatsApp."],
     "headline": ["Tu comprobante según tu dependencia", "Lista completa, sin vueltas"],
     "cta": "Enviar mensaje"},
    {"id": "META-04", "name": "Texto dominante (mismo día)", "objective": "Mensajes a WhatsApp",
     "audience": "Amplia, 55-80 años (jubilados y pensionados), Ciudad Juárez + 25 km",
     "creative": "Imagen limpia con tipografía grande: \"Crédito vía nómina · dinero el mismo día\".",
     "primary": ["Solicita antes de las 3:00 pm y tu crédito se aprueba y se deposita el mismo día. Más de 20 años prestando en Ciudad Juárez, con asesoría de principio a fin.",
                  "Antes de las 3 de la tarde entra el mismo día; después, cae al siguiente. Si quieres resolverlo hoy, escríbenos ahora."],
     "headline": ["Dinero el mismo día", "Solicita antes de las 3:00 pm"],
     "cta": "Enviar mensaje"},
    {"id": "META-05", "name": "Lifestyle (afinidad)", "objective": "Alcance / reconocimiento",
     "audience": "Amplia, 55-80 años (jubilados y pensionados), Ciudad Juárez + 25 km",
     "creative": "La señora mayor con el gatito (mismo estilo del warm up orgánico, sin promesa de producto).",
     "primary": ["Cuidar a los que quieres también es un plan financiero. Estamos en Zona Pronaf para ayudarte a ordenarlo.",
                  "Un gusto pequeño, una tranquilidad grande. Si quieres saber si te conviene un crédito vía nómina, aquí estamos."],
     "headline": ["Cerca de ti, en Zona Pronaf", "Planes claros, trato cercano"],
     "cta": "Más información"},
]

json.dump({"campaign": "Anuncios Facebook/Instagram · sep-oct 2026",
           "strategy": {
               "objective": "Conversaciones por WhatsApp (wa.me/526563748899), no clics ni formularios.",
               "structure": "1 campaña de Mensajes con Advantage+ activo y público amplio. 5 conceptos genuinamente distintos (no 5 versiones del mismo arte), cada uno con 2 variantes de texto principal y 2 titulares para que el sistema rote.",
               "budget": "Porcentajes del total aprobado del mes; no se autoriza incremento de gasto sin aprobación.",
               "activation": "Arranca el día 4-5 del calendario orgánico (página ya con historial), no el día 1.",
               "guardrails": [
                   "Prohibido el copy de atributo personal ('¿estás endeudado?', 'tu mal historial'): viola políticas de Meta y devalúa la marca.",
                   "Ninguna tasa, monto, CAT o plazo que no esté por escrito y aprobado: en este plan no se inventó ninguna cifra.",
                   "Razón social visible (Financiera Fortaleza, S.A. de C.V., SOFOM, E.N.R.) en los anuncios y en la página.",
                   "Responder todo mensaje de WhatsApp en horario; fuera de horario contesta el bot."
               ],
               "measure": ["Comentarios y compartidos por publicación (no likes)",
                           "Alcance de personas que no te siguen",
                           "Conversaciones de WhatsApp iniciadas",
                           "Citas agendadas en el CRM",
                           "Costo por conversación, semana a semana"]},
           "ads": ads},
          open(os.path.join(HERE, "ads.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print("calendar.json:", len(posts), "posts · ads.json:", len(ads), "anuncios")
print("ejemplo día 2 copy:", posts[1]["copy"][:90].replace("\n", " | "))
print("ejemplo día 10 visual:", posts[9]["visuals"])
