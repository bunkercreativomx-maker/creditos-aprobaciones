"""3 fotos documentales nuevas para la campaña $800 (FAL gpt-image-2, retrato 2:3)."""
import sys, os, urllib.request, concurrent.futures as cf
sys.path.insert(0, "/opt/data/hermes-agent")
from tools.image_generation_tool import resolve_managed_tool_gateway, _get_managed_fal_client
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fotos")
BASE = ("Documentary photograph, 35mm lens, natural daylight, real skin texture with natural wrinkles, unretouched, "
        "ordinary everyday clothing, authentic Ciudad Juarez, Chihuahua, Mexico setting. Mexican people. Warm, dignified, candid, "
        "both faces fully visible and in frame, subjects in the upper half of the frame. Absolutely NO text, NO letters, NO logos, "
        "NO watermarks, NO signage, NO readable screens. The lower 45% of the frame is calm, plain and uncluttered (table surface, floor or wall).")
SCENES = {
 "mismo-dia": "A Mexican retired couple in their late 60s at their home kitchen table in the morning; the woman holds a mobile phone (screen facing away from camera) and both look at it with genuine relieved happy smiles, the man with grey hair and a pressed short-sleeve button shirt has his hand on her shoulder; coffee cups, simple oilcloth tablecloth, window light.",
 "dependencias": "A proud Mexican retired man about 68 with grey mustache, wearing a clean white guayabera, standing on the front porch of his modest stucco home, arms relaxed, smiling confidently at the camera; potted plants, warm late-afternoon desert light.",
 "ine-nss": "A friendly Mexican female advisor in her 30s in a navy blazer sitting at a desk in a bright small office, attending a Mexican retired woman about 66 with short grey hair and glasses; the retired woman holds a plain blank ID-sized card and smiles, the advisor smiles back; open blank folder on the desk, plant, window light.",
}
gw = resolve_managed_tool_gateway("fal-queue"); client = _get_managed_fal_client(gw)
def gen(name):
    path = f"{OUT}/{name}.png"
    if os.path.exists(path): return name, "ya existe"
    r = client.submit("fal-ai/gpt-image-2", arguments={"prompt": SCENES[name] + " " + BASE, "quality": "medium",
        "image_size": {"width": 1024, "height": 1536}, "num_images": 1}).get()
    data = urllib.request.urlopen(urllib.request.Request(r["images"][0]["url"], headers={"User-Agent": "Mozilla/5.0"}), timeout=120).read()
    open(path, "wb").write(data); return name, f"{len(data)//1024} KB"
with cf.ThreadPoolExecutor(3) as ex:
    for n, s in ex.map(gen, SCENES): print(n, s)
