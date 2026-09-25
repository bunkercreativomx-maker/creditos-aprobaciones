"""Genera 7 fotos documentales NUEVAS (1 calentamiento + 6 anuncios) vía FAL gateway Nous, gpt-image-2 medium."""
import sys, os, json, urllib.request, concurrent.futures as cf
sys.path.insert(0, "/opt/data/hermes-agent")
from tools.image_generation_tool import resolve_managed_tool_gateway, _get_managed_fal_client

OUT = "/opt/data/creditos-aprobaciones/assets"
BASE = ("Documentary photograph, shot on a 35mm lens, natural daylight, real skin texture with natural wrinkles and pores, "
        "unretouched, ordinary everyday clothing, authentic Ciudad Juárez, Chihuahua, Mexico setting (desert light, stucco walls, "
        "tile floors). Mexican people. Warm, dignified, candid, not posed like stock. Absolutely NO text, NO letters, NO logos, "
        "NO watermarks, NO signage, NO brand names anywhere in the image. Leave the lower third of the frame calm and uncluttered.")
SCENES = {
    "calentamiento-album": "A Mexican retired couple in their early 70s sitting close together on the porch of their home, laughing while looking at an old family photo album on their laps; faded family photos visible but no faces readable; potted geraniums, late-afternoon golden light.",
    "ad-pareja-dependencias": "A Mexican couple in their late 60s standing arm in arm in front of their modest home's front door with a bougainvillea, both smiling calmly at the camera, man with grey mustache and plaid shirt, woman with short grey hair and cardigan.",
    "ad-ine-nss": "A Mexican retired man, about 68, sitting at his kitchen table holding a plain blank plastic ID-sized card and a folded sheet of paper (both blank, nothing printed), looking up with a relieved small smile; coffee mug, oilcloth tablecloth with a simple pattern.",
    "ad-mismo-dia": "A Mexican retired woman, about 65, standing in her sunny living room, looking at her mobile phone screen (screen not visible) with a genuine happy surprised smile, hand on her chest; framed family photos out of focus behind her.",
    "ad-asesor-persona": "A friendly Mexican female financial advisor in her 30s wearing a navy blazer, sitting across a desk from a Mexican retired man, about 70, in a simple bright office, explaining calmly with an open blank folder between them; the man nods, relaxed; plant and window light.",
    "ad-descuento-pension": "A Mexican retired school teacher, woman about 66 with glasses on a chain, sitting on a bench in a neighborhood park in the morning, smiling serenely, a canvas tote bag beside her; trees and soft light.",
    "ad-confianza-8-anos": "A Mexican retired man, about 72, wearing a straw hat and a clean guayabera, shaking hands warmly with a younger Mexican male advisor (30s, white shirt) at the door of a small office, both smiling; midday light.",
}
gw = resolve_managed_tool_gateway("fal-queue")
client = _get_managed_fal_client(gw)

def gen(name):
    path = f"{OUT}/{name}.png"
    if os.path.exists(path):
        return name, "ya existe"
    r = client.submit("fal-ai/gpt-image-2", arguments={
        "prompt": SCENES[name] + " " + BASE, "quality": "medium", "image_size": "square_hd", "num_images": 1}).get()
    url = r["images"][0]["url"]
    data = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=120).read()
    open(path, "wb").write(data)
    return name, f"{len(data)//1024} KB"

with cf.ThreadPoolExecutor(4) as ex:
    for n, s in ex.map(gen, SCENES):
        print(n, s)
