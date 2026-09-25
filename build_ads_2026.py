"""Piezas de calentamiento + 6 anuncios (Meta, destino creditoatumedida.com).
Reusa el sistema de marca de build_piezas_30.py. Salida: ads/*.png (1:1 feed + 9:16 stories/reels).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_piezas_30 as B

OUT = os.path.join(B.HERE, "ads")
os.makedirs(OUT, exist_ok=True)

PIEZAS = [
    # (archivo, foto, chip, titular, apoyo, cta)
    ("calentamiento", "calentamiento-album", "CRÉDITOS A TU MEDIDA", "Ya estamos en Facebook", "Pensionados y jubilados de Ciudad Juárez · Zona Pronaf", None),
    ("AD-01", "ad-pareja-dependencias", "PENSIONADOS Y JUBILADOS", "Crédito para pensionados y jubilados", "IMSS · ISSSTE · CFE · Pemex · SNTE Sección 8", "Solicita en creditoatumedida.com"),
    ("AD-02", "ad-ine-nss", "COTIZA EN MINUTOS", "Con tu INE y tu número de seguro social te cotizamos", "Sin historial crediticio perfecto", "Cotiza en creditoatumedida.com"),
    ("AD-03", "ad-mismo-dia", "DEPÓSITO EL MISMO DÍA", "Solicita antes de las 3 pm y te depositamos hoy", "Si tus documentos están en orden", "Solicita en creditoatumedida.com"),
    ("AD-04", "ad-asesor-persona", "ATENCIÓN EN PERSONA", "Un asesor te explica todo antes de firmar", "Benjamín Franklin 3220 · Zona Pronaf · por la entrada de Subway", "Agenda en creditoatumedida.com"),
    ("AD-05", "ad-descuento-pension", "CRÉDITO VÍA NÓMINA", "Se descuenta directo de tu pensión", "Pagos fijos, sin ir al banco", "Conoce más en creditoatumedida.com"),
    ("AD-06", "ad-confianza-8-anos", "MÁS DE 8 AÑOS", "Más de 8 años otorgando créditos en Juárez", "De la mano de Financiera Fortaleza", "Solicita en creditoatumedida.com"),
]

if __name__ == "__main__":
    for name, foto, chip, head, sub, cta in PIEZAS:
        for tag, (W, H, pr) in {"1x1": (1080, 1080, 0.50), "9x16": (1080, 1920, 0.56)}.items():
            path = os.path.join(OUT, f"{name}_{tag}.png")
            over, n = B.pieza(path, W, H, foto, chip, head, sub, pr, cta), 0
            while over > 0 and n < 4:
                pr -= 0.04; n += 1
                over = B.pieza(path, W, H, foto, chip, head, sub, pr, cta)
            print(path, "ajustes", n, "sobra", -over)
