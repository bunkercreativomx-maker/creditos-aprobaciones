"""Genera index.html: campaña Meta $800 MXN (copys con botón Copiar + paso a paso + ZIP)."""
import json, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://creditoatumedida.com/"
UTM = "utm_source=facebook&utm_medium=paid_social&utm_campaign=creditos_800_oct26&utm_content="

ADS = [
 {"n": "01", "id": "AD-01", "nombre": "Depósito el mismo día", "foto": "mismo-dia", "angulo": "Rapidez (la oferta más fuerte del sitio)",
  "primario": [
   "Solicite antes de las 3:00 pm y, si sus documentos están en orden, su crédito se deposita ese mismo día.\n\nCrédito vía nómina para pensionados y jubilados del IMSS, ISSSTE, CFE, Pemex y SNTE Sección 8. El pago se descuenta directo de la pensión.\n\n👉 Deje sus datos en creditoatumedida.com y un asesor le llama en horario de oficina.",
   "Antes de las 3 de la tarde, el depósito sale el mismo día; después, al día siguiente. Así de claro.\n\nPensionados y jubilados del IMSS, ISSSTE, CFE, Pemex y SNTE Sección 8, con atención en persona en Zona Pronaf. Más de 8 años otorgando créditos en Ciudad Juárez.\n\nInicie su solicitud en creditoatumedida.com"],
  "titular": ["Depósito el mismo día", "Solicite antes de las 3:00 pm"],
  "descripcion": "Sujeto a aprobación de crédito", "cta": "Solicitar ahora"},
 {"n": "02", "id": "AD-02", "nombre": "Para quién es", "foto": "dependencias", "angulo": "Filtra al público correcto (dependencias)",
  "primario": [
   "Crédito vía nómina para pensionados y jubilados del IMSS, ISSSTE, CFE, Pemex y SNTE Sección 8 en Ciudad Juárez.\n\n✅ El pago se descuenta directo de la pensión\n✅ No necesita historial crediticio perfecto\n✅ Un asesor le acompaña de principio a fin\n\nSolicite en creditoatumedida.com",
   "Pensionados y jubilados de IMSS, ISSSTE, CFE, Pemex y SNTE Sección 8: en Créditos a tu medida el trámite es claro y en persona, en Zona Pronaf.\n\nDeje sus datos en nuestra página y un asesor le contacta para explicarle todo, sin compromiso."],
  "titular": ["Crédito para pensionados y jubilados", "IMSS · ISSSTE · CFE · Pemex · SNTE 8"],
  "descripcion": "Financiera Fortaleza, SOFOM, E.N.R.", "cta": "Solicitar ahora"},
 {"n": "03", "id": "AD-03", "nombre": "INE + NSS", "foto": "ine-nss", "angulo": "Facilidad para empezar",
  "primario": [
   "Con su INE y su número de seguro social le cotizamos. Así de fácil empieza su crédito vía nómina.\n\nNo necesita historial crediticio perfecto: cada caso se revisa de forma individual.\n\nPara pensionados y jubilados del IMSS, ISSSTE, CFE, Pemex y SNTE Sección 8. Cotice sin compromiso en creditoatumedida.com",
   "Cotizar no cuesta nada. Deje su nombre y teléfono en creditoatumedida.com y un asesor le explica qué documentos necesita según su dependencia.\n\nAtención en persona: Benjamín Franklin 3220, Int 22-D, Zona Pronaf (por la entrada de Subway)."],
  "titular": ["Con su INE y NSS le cotizamos", "Cotice sin compromiso"],
  "descripcion": "Pensionados y jubilados · Cd. Juárez", "cta": "Obtener cotización"},
]
for a in ADS:
    a["url"] = SITE + "?" + UTM + a["id"].lower()
    a["f45"] = f"piezas/{a['n']}_{a['id']}_{a['foto']}_4x5.png"
    a["f916"] = f"piezas/{a['n']}_{a['id']}_{a['foto']}_9x16.png"

def esc(s): return html.escape(s)
def box(label, text):
    return f'<div class="box"><div class="lab">{esc(label)}<button class="cp">Copiar</button></div><pre>{esc(text)}</pre></div>'

cards = []
for a in ADS:
    c = [f'<section class="ad"><h3>{a["n"]} · {esc(a["nombre"])} <span>{esc(a["angulo"])}</span></h3>',
         f'<div class="imgs"><figure><img src="{a["f45"]}" loading="lazy"><figcaption>4:5 · Feed</figcaption></figure>'
         f'<figure><img src="{a["f916"]}" loading="lazy"><figcaption>9:16 · Stories y Reels</figcaption></figure></div><div class="copys">']
    c.append(box("Texto principal A", a["primario"][0]))
    c.append(box("Texto principal B (agregar como opción)", a["primario"][1]))
    c.append(box("Titular A", a["titular"][0]))
    c.append(box("Titular B", a["titular"][1]))
    c.append(box("Descripción", a["descripcion"]))
    c.append(box("URL del sitio web (con UTM)", a["url"]))
    c.append(f'<p class="cta">Botón (CTA): <b>{esc(a["cta"])}</b></p></div></section>')
    cards.append("".join(c))

files = [a["f45"] for a in ADS] + [a["f916"] for a in ADS]

PAGE = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>Campaña Meta $800 · Créditos a tu medida</title>
<style>
:root{{--navy:#060d1c;--n2:#0e1b33;--gold:#c9a227;--gl:#e3cd7f;--cream:#faf7f0;--mut:#aab3c5;--ok:#25d366}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--navy);color:var(--cream);font:16px/1.55 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}}
main{{max-width:1080px;margin:0 auto;padding:28px 18px 80px}}h1{{font-size:clamp(26px,5vw,40px);line-height:1.1;margin:0 0 6px}}
h2{{color:var(--gl);margin:44px 0 12px;font-size:24px;border-top:1px solid #1d2b47;padding-top:26px}}h3{{margin:0 0 14px;font-size:21px}}h3 span{{display:block;font-size:14px;color:var(--mut);font-weight:500}}
.sub{{color:var(--mut);margin:0 0 18px}}.pill{{display:inline-block;background:var(--gold);color:var(--navy);font-weight:800;border-radius:99px;padding:4px 12px;font-size:13px;margin:0 6px 6px 0}}
.zip{{display:inline-block;background:var(--ok);color:#06210f;font-weight:800;border:0;border-radius:12px;padding:15px 22px;font-size:17px;cursor:pointer}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px}}.k{{background:var(--n2);border-radius:14px;padding:14px 16px}}.k b{{display:block;color:var(--gl);font-size:13px;text-transform:uppercase;letter-spacing:.04em}}
.ad{{background:var(--n2);border-radius:18px;padding:20px;margin:18px 0}}.imgs{{display:flex;gap:12px;margin-bottom:14px;flex-wrap:wrap}}figure{{margin:0;flex:1;min-width:140px;max-width:300px}}figure img{{width:100%;border-radius:10px;display:block}}figcaption{{font-size:12px;color:var(--mut);margin-top:4px}}
.box{{background:#091428;border:1px solid #1d2b47;border-radius:12px;margin:10px 0}}.lab{{display:flex;justify-content:space-between;align-items:center;padding:8px 12px;font-size:13px;color:var(--gl);font-weight:700;border-bottom:1px solid #1d2b47}}
pre{{margin:0;padding:12px;white-space:pre-wrap;font:15px/1.5 system-ui,sans-serif}}.cp{{background:var(--gold);color:var(--navy);border:0;border-radius:8px;padding:6px 12px;font-weight:800;cursor:pointer}}.cp.ok{{background:var(--ok)}}
ol li,ul li{{margin:6px 0}}table{{width:100%;border-collapse:collapse;font-size:15px}}td,th{{border-bottom:1px solid #1d2b47;padding:9px 8px;text-align:left;vertical-align:top}}th{{color:var(--gl)}}
.warn{{background:#2a1f05;border:1px solid var(--gold);border-radius:12px;padding:14px 16px}}code{{background:#091428;padding:1px 6px;border-radius:6px}}a{{color:var(--gl)}}
</style></head><body><main>
<span class="pill">META ADS</span><span class="pill">$800 MXN</span><span class="pill">8 DÍAS</span>
<h1>Campaña de solicitudes · Créditos a tu medida</h1>
<p class="sub">1 campaña → 1 conjunto → 3 anuncios. Todo apunta a <b>creditoatumedida.com</b> y optimiza a <b>Lead</b> (formulario enviado = llega al CRM).</p>
<button class="zip" id="zip">⬇ Descargar las 6 imágenes (ZIP)</button>

<h2>Resumen</h2>
<div class="grid">
<div class="k"><b>Presupuesto</b>$800 MXN total (de por vida) ≈ $100/día</div>
<div class="k"><b>Fechas</b>Lun 19 oct 00:00 → Lun 26 oct 23:59</div>
<div class="k"><b>Objetivo</b>Clientes potenciales → Sitio web → evento Lead</div>
<div class="k"><b>Público</b>Cd. Juárez · 50 a 65+ · sin intereses · excluir EE.UU.</div>
<div class="k"><b>Anuncios</b>3 (no más: con $800 cada anuncio extra roba datos)</div>
<div class="k"><b>Estimado honesto</b>8–25 solicitudes si el costo por lead cae entre $30 y $100. Es prueba, no garantía.</div>
</div>

<h2>Por qué así (lo que hace que funcione con poco dinero)</h2>
<ul>
<li><b>Edad 50+ fija.</b> Verificado hoy en Meta: la categoría especial financiera (que bloquea edad y obliga 18-65+) es obligatoria solo si el anunciante es de EE.UU. o el anuncio llega a EE.UU./Canadá/partes de Europa. Juárez-solo no entra, así que podemos cerrar la edad. Con $800 no hay dinero para pagarle impresiones a gente de 25 años.</li>
<li><b>Excluir Estados Unidos.</b> El radio de Juárez cruza a El Paso. Si el anuncio llega a EE.UU., Meta exige la categoría especial y se pierde el filtro de edad.</li>
<li><b>Presupuesto de por vida con fechas.</b> Meta reparte el gasto en los días y horas con más probabilidad de lead; no se pasa de $800.</li>
<li><b>3 ángulos distintos</b> (rapidez, para quién es, facilidad) con 2 textos y 2 titulares cada uno: Meta prueba las combinaciones y empuja la ganadora.</li>
<li><b>Letra grande y trato de usted</b> en las piezas: el público es 55+ y lee en celular.</li>
</ul>

<h2>Las 3 piezas y sus copys</h2>
{''.join(cards)}

<h2>Paso a paso en Ads Manager (≈15 min)</h2>
<div class="warn"><b>Antes de empezar (2 min):</b> Events Manager → dataset <code>1401885575462193</code> → <b>Probar eventos</b> → abre creditoatumedida.com, manda el formulario con un teléfono de prueba y confirma que aparece <b>Lead</b>. Si no aparece, no lances: avísame. Luego borra ese lead de prueba del CRM.</div>
<h3 style="margin-top:22px">1 · Campaña</h3>
<ol>
<li>adsmanager.facebook.com → <b>+ Crear</b> → <b>Clientes potenciales</b> → Continuar.</li>
<li>Si pregunta configuración: elige <b>Campaña de clientes potenciales manual</b> (no la Advantage+ automática; esa no deja fijar edad).</li>
<li>Nombre: <code>CAM · Leads Web · $800 · Oct26</code></li>
<li><b>Categoría especial de anuncios: déjala SIN marcar</b> (ver “Por qué así”). Si tu portafolio de negocio está dado de alta en EE.UU., Meta la va a exigir: márcala “Productos y servicios financieros” y en el público solo pon Juárez (edad quedará 18-65+).</li>
<li><b>Presupuesto de la campaña Advantage+</b>: activado → <b>Presupuesto total</b> → <code>800</code> MXN.</li>
</ol>
<h3>2 · Conjunto de anuncios</h3>
<ol>
<li>Nombre: <code>Juárez 50+ · Lead web</code></li>
<li><b>Ubicación de la conversión: Sitio web</b> (no formulario instantáneo, no WhatsApp, no Messenger).</li>
<li>Objetivo de rendimiento: <b>Maximizar el número de conversiones</b>. Dataset: <code>1401885575462193</code> → evento <b>Cliente potencial (Lead)</b>.</li>
<li>Calendario: inicio <b>lun 19 oct 00:00</b>, fin <b>lun 26 oct 23:59</b>.</li>
<li>Público → <b>Usar opciones de público originales</b> (o “Cambiar a opciones originales”):
<ul><li>Ubicación: <b>Ciudad Juárez, Chihuahua</b> → personas que <b>viven</b> en esta ubicación.</li>
<li>En ubicaciones → <b>Excluir</b> → escribe <b>Estados Unidos</b>.</li>
<li>Edad <b>50 – 65+</b>. Sexo: todos. Idioma: Español.</li>
<li>Segmentación detallada: <b>vacía</b>. Nada de intereses, el filtro lo hacen la edad y las piezas.</li></ul></li>
<li>Ubicaciones → <b>Ubicaciones manuales</b>: deja solo <b>Facebook</b> (Feed, Stories, Reels) e <b>Instagram</b> (Feed, Stories, Reels). Quita Audience Network, Messenger y Threads; con poco dinero ahí se va en clics basura.</li>
</ol>
<h3>3 · Anuncios (repetir 3 veces)</h3>
<ol>
<li>Identidad: página <b>Credito a tu Medida</b> (+ Instagram si está conectado).</li>
<li>Formato <b>Imagen única</b> → sube la <b>4:5</b> → en “Personalizar por ubicación” pon la <b>9:16</b> para Stories y Reels.</li>
<li>Texto principal A, y “+ Agregar opción de texto” para el B. Titular A y B. Descripción.</li>
<li>Destino: <b>Sitio web</b> → pega la URL con UTM de ese anuncio. CTA el indicado.</li>
<li><b>Mejoras creativas Advantage+: apaga todo lo de texto generado por IA, expandir imagen, música y “agregar superposiciones”.</b> En crédito, un texto inventado por IA puede prometer algo que no ofrecemos y causar rechazo.</li>
<li>Seguimiento: confirma que el dataset esté marcado en “Eventos del sitio web”. <b>Publicar.</b></li>
</ol>

<h2>Reglas que ya cumplen estos anuncios (para que no los rechacen)</h2>
<ul>
<li>Crédito a largo plazo (más de 90 días) por descuento de pensión: permitido. Meta prohíbe préstamos de día de pago, adelantos de nómina y préstamos de ≤90 días. <a href="https://transparency.meta.com/policies/ad-standards/restricted-goods-services/financial-services/" target="_blank">Política de Meta</a></li>
<li>Ninguna tasa, monto, CAT ni plazo (si se menciona uno, hay que mostrar todos).</li>
<li>Nada de “¿estás endeudado?” ni “¿eres jubilado?”: Meta prohíbe afirmar o insinuar atributos personales (situación financiera, edad). Todo va en tercera persona/usted.</li>
<li>Razón social visible en cada pieza: Financiera Fortaleza, S.A. de C.V., SOFOM, E.N.R. Si Meta pide verificar el negocio o la autorización financiera, se hace con los papeles de la SOFOM.</li>
<li>El anuncio no pide datos personales dentro de Facebook; el formulario está en el sitio.</li>
</ul>

<h2>Cómo operarla los 8 días</h2>
<table><tr><th>Cuándo</th><th>Qué hacer</th></tr>
<tr><td>Días 1–3</td><td><b>No tocar nada.</b> Cada cambio reinicia el aprendizaje. Solo contestar cada lead del CRM en menos de 5 minutos en horario: eso decide si el lead se vuelve crédito.</td></tr>
<tr><td>Día 4 (jue 22)</td><td>Si un anuncio gastó ≥$150 con 0 leads y los otros sí traen, <b>pausa ese</b>. Si ninguno trae leads con $300 gastados, revisa Events Manager (¿llega Lead?) y avísame antes de seguir.</td></tr>
<tr><td>Días 5–8</td><td>No subir presupuesto a media prueba. Anotar en el CRM cuáles leads contestan y agendan.</td></tr>
<tr><td>Al cerrar</td><td>Mándame captura de Ads Manager (gasto, resultados, costo por resultado por anuncio) + cuántos leads agendaron. Con eso decidimos el siguiente mes: escalar el ganador o cambiar creativos.</td></tr>
</table>

<h2>Pendiente que afecta conversión</h2>
<p class="sub">El sitio todavía dice “20+ años” y menciona Gobierno/Educación, mientras los anuncios dicen “más de 8 años” y solo pensionados/jubilados. No lo cambié porque falta el permiso del cliente; si lo autoriza, lo alineo en 10 minutos.</p>
</main>
<script src="https://cdn.jsdelivr.net/npm/jszip@3.10.1/dist/jszip.min.js"></script>
<script>
document.querySelectorAll('.cp').forEach(b=>b.onclick=async()=>{{const t=b.closest('.box').querySelector('pre').innerText;
try{{await navigator.clipboard.writeText(t)}}catch(e){{const a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();document.execCommand('copy');a.remove()}}
b.textContent='¡Copiado!';b.classList.add('ok');setTimeout(()=>{{b.textContent='Copiar';b.classList.remove('ok')}},1500)}});
const FILES={json.dumps(files)};
document.getElementById('zip').onclick=async e=>{{const b=e.target;b.textContent='Preparando…';const z=new JSZip();
for(const f of FILES){{const r=await fetch(f);z.file(f.split('/').pop(),await r.blob())}}
const blob=await z.generateAsync({{type:'blob'}});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='creditos-meta-800-oct26.zip';a.click();b.textContent='⬇ Descargar las 6 imágenes (ZIP)'}};
</script></body></html>"""
open(os.path.join(HERE, "index.html"), "w").write(PAGE)
json.dump({"ads": ADS}, open(os.path.join(HERE, "campana.json"), "w"), ensure_ascii=False, indent=1)
print("ok", len(PAGE))
