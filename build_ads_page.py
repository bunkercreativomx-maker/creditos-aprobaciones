#!/usr/bin/env python
"""Genera ads/index.html: página de entrega (calentamiento + 6 anuncios + paso a paso + ZIP)."""
import json, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, "ads", "campana.json"), encoding="utf-8"))
E = html.escape

def copybox(label, text):
    return f'<div class="cp"><div class="lb">{E(label)}<button onclick="cp(this)">Copiar</button></div><pre>{E(text)}</pre></div>'

cards = []
c = D["calentamiento"]
cards.append(f'''<section class="card" id="calentamiento"><h2>Post de calentamiento</h2>
<p class="meta">Publicación orgánica fijada en la página. Se promociona con $200 MXN (ver paso 3).</p>
<div class="imgs"><figure><img src="calentamiento_1x1.png" loading="lazy"><figcaption>1:1 feed</figcaption></figure>
<figure><img src="calentamiento_9x16.png" loading="lazy"><figcaption>9:16 stories</figcaption></figure></div>
{copybox("Texto de la publicación", c["copy"])}{copybox("Primer comentario (desde la página)", c["primer_comentario"])}</section>''')
for i, a in enumerate(D["ads"], 1):
    url = D["destino"] + "?" + D["utm"] + a["id"].lower()
    cards.append(f'''<section class="card" id="{a["id"]}"><h2>{a["id"]} · {E(a["nombre"])}</h2>
<p class="meta">Ángulo: {E(a["angulo"])} · CTA: <b>{E(a["cta"])}</b></p>
<div class="imgs"><figure><img src="{a["id"]}_1x1.png" loading="lazy"><figcaption>1:1 feed</figcaption></figure>
<figure><img src="{a["id"]}_9x16.png" loading="lazy"><figcaption>9:16 stories/reels</figcaption></figure></div>
{copybox("Texto principal A", a["primario"][0])}{copybox("Texto principal B", a["primario"][1])}
{copybox("Titular A", a["titular"][0])}{copybox("Titular B", a["titular"][1])}
{copybox("Descripción", a["descripcion"])}{copybox("URL del sitio web (con UTM)", url)}</section>''')

files = ["calentamiento_1x1.png", "calentamiento_9x16.png"] + [f"{a['id']}_{t}.png" for a in D["ads"] for t in ("1x1", "9x16")]
PASOS = open(os.path.join(HERE, "ads", "PASO-A-PASO.md"), encoding="utf-8").read()

page = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Créditos a tu medida · Calentamiento + Anuncios Meta</title>
<script src="https://cdn.jsdelivr.net/npm/jszip@3.10.1/dist/jszip.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked@12/marked.min.js"></script>
<style>
body{{margin:0;font-family:Manrope,system-ui,sans-serif;background:#060d1c;color:#faf7f0}}
header{{padding:28px 20px;background:#0a1628;border-bottom:1px solid #c9a22755}}
h1{{font-family:Georgia,serif;margin:0 0 6px;font-size:26px}} h2{{font-family:Georgia,serif;color:#e3cd7f;margin:0 0 6px}}
.wrap{{max-width:980px;margin:0 auto;padding:20px}} .btn{{background:#c9a227;color:#060d1c;border:0;border-radius:999px;padding:12px 22px;font-weight:800;font-size:15px;cursor:pointer}}
.card{{background:#0d1b33;border:1px solid #ffffff14;border-radius:16px;padding:20px;margin:18px 0}}
.meta{{color:#b0b8c6;margin:0 0 12px}} .imgs{{display:flex;gap:14px;flex-wrap:wrap}} figure{{margin:0}}
.imgs img{{height:320px;border-radius:10px;display:block}} figcaption{{font-size:12px;color:#b0b8c6;margin-top:4px}}
.cp{{margin-top:12px}} .lb{{font-size:12px;color:#e3cd7f;font-weight:800;text-transform:uppercase;display:flex;justify-content:space-between;align-items:center}}
.lb button{{background:#25d366;color:#fff;border:0;border-radius:8px;padding:5px 12px;font-weight:700;cursor:pointer}}
pre{{white-space:pre-wrap;background:#060d1c;border:1px solid #ffffff14;border-radius:10px;padding:12px;font:15px/1.5 Manrope,system-ui,sans-serif;margin:6px 0 0}}
#pasos{{background:#faf7f0;color:#0a1628;border-radius:16px;padding:8px 24px 20px;margin:18px 0}} #pasos h2{{color:#0a1628}} #pasos code{{background:#0a162812;padding:1px 5px;border-radius:4px}}
#pasos table{{border-collapse:collapse;width:100%}} #pasos td,#pasos th{{border:1px solid #0a162822;padding:6px 8px;text-align:left;font-size:14px}}
nav a{{color:#e3cd7f;margin-right:12px;font-size:14px}}
</style></head><body>
<header><div class="wrap" style="padding:0"><h1>Créditos a tu medida · Calentamiento + 6 anuncios Meta</h1>
<p class="meta">Destino de todos los anuncios: <b>creditoatumedida.com</b> (sitio web, no Messenger). Imágenes 1:1 + 9:16, copys listos para pegar.</p>
<button class="btn" onclick="zip()">⬇ Descargar todo (ZIP)</button>
<nav style="margin-top:12px"><a href="#pasos">Paso a paso</a><a href="#calentamiento">Calentamiento</a>{"".join(f'<a href="#{a["id"]}">{a["id"]}</a>' for a in D["ads"])}</nav></div></header>
<div class="wrap"><div id="pasos"></div>{"".join(cards)}</div>
<script id="md" type="text/markdown">{E(PASOS)}</script>
<script>
document.getElementById('pasos').innerHTML = marked.parse(document.getElementById('md').textContent
  .replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&quot;/g,'"').replace(/&#x27;/g,"'").replace(/&amp;/g,'&'));
function cp(b){{navigator.clipboard.writeText(b.parentElement.nextElementSibling.textContent);b.textContent='¡Copiado!';setTimeout(()=>b.textContent='Copiar',1500)}}
const FILES={json.dumps(files)};
async function zip(){{const z=new JSZip();let n=1;
 for(const f of FILES){{const r=await fetch(f);z.file(String(n++).padStart(2,'0')+'_'+f,await r.blob())}}
 z.file('copys.json',JSON.stringify({json.dumps(D, ensure_ascii=False)},null,1));
 z.file('PASO-A-PASO.md',document.getElementById('md').textContent);
 const b=await z.generateAsync({{type:'blob'}});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='creditos-meta-ads-oct2026.zip';a.click()}}
</script></body></html>'''
open(os.path.join(HERE, "ads", "index.html"), "w", encoding="utf-8").write(page)
print("ok", len(files), "imágenes")
