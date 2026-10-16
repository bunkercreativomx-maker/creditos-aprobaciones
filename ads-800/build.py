"""Campaña Meta $800 MXN · 3 anuncios · 4:5 (feed) + 9:16 (stories/reels).
Tipografía pesada y grande (público 55+), trato de usted, sin tasas/montos/plazos.
"""
import os, sys
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, "/opt/data/creditos-aprobaciones")
import build_piezas_30 as B

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "piezas")
os.makedirs(OUT, exist_ok=True)
NAVY, GOLD, GOLD_L, CREAM = B.NAVY, B.GOLD, B.GOLD_L, B.CREAM
F = B.font

ADS = [
    dict(id="01", foto="mismo-dia", chip="DEPÓSITO EL MISMO DÍA",
         head="Solicite antes de las 3\u00a0pm y reciba su crédito\u00a0hoy",
         sub="Si sus documentos están en orden", pills=None,
         cta="Solicite en creditoatumedida.com"),
    dict(id="02", foto="dependencias", chip="CRÉDITO VÍA NÓMINA",
         head="Crédito para pensionados y jubilados",
         sub="El pago se descuenta directo de la pensión",
         pills=["IMSS", "ISSSTE", "CFE", "PEMEX", "SNTE 8"],
         cta="Solicite en creditoatumedida.com"),
    dict(id="03", foto="ine-nss", chip="COTICE SIN COMPROMISO",
         head="Con su INE y su número de seguro social le cotizamos",
         sub="No necesita historial crediticio perfecto", pills=None,
         cta="Cotice en creditoatumedida.com"),
]


def cover(path, W, H, focus=0.0):
    im = Image.open(path).convert("RGB")
    r = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    l = (im.width - W) // 2
    t = int((im.height - H) * focus)
    return im.crop((l, t, l + W, t + H)).convert("RGBA")


def gradient(W, H, start, full):
    """Transparente arriba de `start`, navy sólido desde `full`."""
    g = Image.new("L", (1, H), 0)
    for y in range(H):
        if y <= start:
            v = 0
        elif y >= full:
            v = 255
        else:
            v = int(255 * ((y - start) / (full - start)) ** 1.3)
        g.putpixel((0, y), v)
    mask = g.resize((W, H))
    layer = Image.new("RGBA", (W, H), NAVY + (255,))
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    out.paste(layer, (0, 0), mask)
    return out


def wrap(d, text, f, maxw):
    lines, cur = [], ""
    for w in text.split(" "):
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    return lines + ([cur] if cur else [])


def fit(d, text, name, size, wght, maxw, maxlines):
    while True:
        f = F(name, size, [wght])
        lines = wrap(d, text, f, maxw)
        if len(lines) <= maxlines or size < 30:
            return f, lines
        size -= 3


def pieza(ad, W, H, story):
    img = cover(os.path.join(HERE, "fotos", ad["foto"] + ".png"), W, H, focus=0.0)
    # bloque de texto empieza donde termina la gente
    if story:
        g0, g1, top, bottom_limit = int(H * .40), int(H * .56), int(H * .53), int(H * .80)
    else:
        g0, g1, top, bottom_limit = int(H * .40), int(H * .57), int(H * .53), int(H * .86)
    img.alpha_composite(gradient(W, H, g0, g1))
    d = ImageDraw.Draw(img)
    m = int(W * 0.07)
    maxw = W - 2 * m
    y = top - (45 if ad["pills"] and not story else 0)

    # chip
    fc = F("Manrope.ttf", 30, [800])
    cw, ch = d.textlength(ad["chip"], font=fc) + 48, 30 + 28
    d.rounded_rectangle((m, y, m + cw, y + ch), radius=ch // 2, fill=GOLD)
    d.text((m + cw / 2, y + ch / 2), ad["chip"], font=fc, fill=NAVY, anchor="mm")
    y += ch + 22

    # titular (pesado, grande)
    fh, lines = fit(d, ad["head"], "Manrope.ttf", 76 if story else 70, 800, maxw, 3)
    for ln in lines:
        d.text((m, y), ln, font=fh, fill=(255, 255, 255))
        y += int(fh.size * 1.12)
    y += 10

    # pills de dependencias
    if ad["pills"]:
        fp = F("Manrope.ttf", 32, [800])
        x = m
        for p in ad["pills"]:
            pw, phh = d.textlength(p, font=fp) + 36, 32 + 22
            d.rounded_rectangle((x, y, x + pw, y + phh), radius=12, outline=GOLD_L, width=3)
            d.text((x + pw / 2, y + phh / 2), p, font=fp, fill=GOLD_L, anchor="mm")
            x += pw + 14
        y += 32 + 22 + 20

    # apoyo
    fs, sl = fit(d, ad["sub"], "Manrope.ttf", 38, 600, maxw, 2)
    for ln in sl:
        d.text((m, y), ln, font=fs, fill=(232, 228, 216))
        y += int(fs.size * 1.3)
    y += 22

    # CTA
    fcta = F("Manrope.ttf", 36, [800])
    bw, bh = d.textlength(ad["cta"], font=fcta) + 70, 36 + 38
    d.rounded_rectangle((m, y, m + bw, y + bh), radius=bh // 2, fill=(37, 211, 102))
    d.text((m + bw / 2, y + bh / 2), ad["cta"], font=fcta, fill=NAVY, anchor="mm")
    y += bh
    overflow = y - bottom_limit

    # pie: legal + logo + whatsapp
    fl = F("Manrope.ttf", 22, [500])
    legal = "Sujeto a aprobación de crédito · Financiera Fortaleza, S.A. de C.V., SOFOM, E.N.R."
    while d.textlength(legal, font=fl) > maxw and fl.size > 14:
        fl = F("Manrope.ttf", fl.size - 1, [500])
    lz = 58
    base_y = int(H * (0.80 if story else 0.875))
    if story:
        base_y = max(base_y, y + 30)
    d.text((m, base_y), legal, font=fl, fill=(176, 184, 198))
    ly = base_y + fl.size + 22
    img.alpha_composite(Image.open(B.LOGO).convert("RGBA").resize((lz, lz), Image.LANCZOS), (m, ly))
    d = ImageDraw.Draw(img)
    fb = F("Manrope.ttf", 30, [700])
    d.text((m + lz + 16, ly + lz / 2), "Créditos a tu medida", font=fb, fill=CREAM, anchor="lm")
    d.text((W - m, ly + lz / 2), "WhatsApp 656 374 8899", font=F("Manrope.ttf", 28, [700]), fill=GOLD_L, anchor="rm")
    if not story:
        overflow = max(overflow, y + 24 - base_y)
    return img.convert("RGB"), overflow


if __name__ == "__main__":
    for i, ad in enumerate(ADS, 1):
        for tag, (W, H, story) in {"4x5": (1080, 1350, False), "9x16": (1080, 1920, True)}.items():
            im, over = pieza(ad, W, H, story)
            p = os.path.join(OUT, f"{i:02d}_AD-{ad['id']}_{ad['foto']}_{tag}.png")
            im.save(p, optimize=True)
            print(os.path.basename(p), "OVERFLOW" if over > 0 else "ok", over)
