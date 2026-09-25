# Paso a paso · Pixel + Calentamiento + 6 anuncios (sitio web)

> Todo apunta a **creditoatumedida.com** (sitio web, no Messenger). Lineamientos vigentes de Meta a sep 2026: categoría especial de anuncios financieros, flujo unificado Advantage+, Pixel + Conversions API con deduplicación.

## Estado del Pixel (verificado)
- **Pixel `1401885575462193` activo** en creditoatumedida.com (probado con navegador real):
  - `PageView` en cada visita ✅ (el CRM no carga el Pixel ✅)
  - `Contact` al tocar WhatsApp o teléfono ✅
  - `Lead` al enviar el formulario con éxito (ya conectado).
- **Conversions API** del servidor: el código está listo, pero se enciende hasta que pongas el token (Paso 1.5 + 2).

## Paso 1 · Crear el Pixel (dataset) · 5 min
1. Entra a **business.facebook.com** → **Administrador de eventos** (Events Manager).
2. **Conectar orígenes de datos** → **Web** → nombre `Creditos a tu medida - Web` → **Crear**.
3. Cuando pregunte cómo instalar, elige **"Configurar manualmente"**. No uses la integración de socios.
4. ✅ Ya hecho: el ID es `1401885575462193`.
5. En ese mismo dataset → **Configuración** → **API de conversiones** → **Generar token de acceso**. Cópialo.

## Paso 2 · Activarlo en Vercel · 3 min
Vercel → proyecto **creditos-a-tu-medida** → Settings → **Environment Variables** (Production):

| Variable | Valor |
|---|---|
| `META_CAPI_TOKEN` | el token del paso 1.5 (márcalo *Sensitive*) |
| `NEXT_PUBLIC_FB_DOMAIN_VERIFICATION` | el código del paso 2b (opcional pero recomendado) |

Después: **Deployments → Redeploy** del último. Las variables solo aplican tras redeploy.

**2b. Verificar el dominio:** Configuración del negocio → **Seguridad de la marca → Dominios** → Agregar `creditoatumedida.com` → método **Metaetiqueta** → copia solo el valor de `content="…"` y ponlo en la variable de arriba → redeploy → **Verificar**.

**2c. Probar:** Events Manager → tu dataset → **Probar eventos** → abre creditoatumedida.com. Debe aparecer `PageView`. Envía el formulario con un teléfono de prueba y debe aparecer `Lead` dos veces (Navegador + Servidor, marcado **"deduplicado"**). Luego borra ese lead de prueba del CRM.

## Paso 3 · Calentamiento de la página · $200 MXN
**Objetivo:** que la página tenga actividad real antes de anunciar el crédito y que el Pixel empiece a recibir datos.
1. Publica el **post de calentamiento** (imagen 1:1 + texto) desde la página y **fíjalo** arriba.
2. En los primeros 10 min, deja el **primer comentario** desde la página.
3. Ads Manager → **+ Crear** → objetivo **Interacción** → tipo de conversión **En tu publicación** → objetivo de rendimiento **Maximizar interacción con la publicación**.
4. **Categoría especial de anuncios: "Productos y servicios financieros".** Es obligatoria aunque el post no sea una oferta: el anunciante es de crédito y sin ella Meta rechaza o restringe la cuenta.
5. Presupuesto **total** (de por vida) **$200 MXN**, del lunes al domingo (**7 días** ≈ $28/día).
6. Ubicación: **Ciudad Juárez + radio mínimo que permita** (≈25 km). Edad y sexo quedan bloqueados por la categoría especial; déjalos así.
7. Público **Advantage+** activado. Ubicaciones **Advantage+**.
8. Anuncio → **Usar publicación existente** → el post de calentamiento.
9. **No lo toques en 7 días.** Invita a los que reaccionen a seguir la página (botón "Invitar" en la lista de reacciones).

> En paralelo siguen saliendo los 30 posts orgánicos que ya dejamos programados en Zernio.

## Paso 4 · Campaña mensual de 6 anuncios (sitio web)
Arranca **cuando el Pixel ya registró eventos** (≥3-4 días de calentamiento).

**Estructura (flujo unificado 2026):** 1 campaña → 1 conjunto → 6 anuncios. No crees 6 campañas: se divide el aprendizaje y ninguna sale de la fase de aprendizaje.

### 4.1 Campaña
- **+ Crear → Clientes potenciales** (Leads).
- **Categoría especial: Productos y servicios financieros** · país **México**.
- Presupuesto de campaña **Advantage+** activado.
- Nombre: `CAM · Leads Web · Oct26`.

### 4.2 Conjunto de anuncios
- **Ubicación de la conversión: Sitio web** (NO Formulario instantáneo, NO Messenger, NO WhatsApp).
- Dataset/Pixel: `Creditos a tu medida - Web` → evento **Cliente potencial (Lead)**.
- Objetivo de rendimiento: **Maximizar número de conversiones**.
- Presupuesto **diario** recomendado: **$150-$250 MXN/día** (≈$4,500-$7,500/mes). Con menos, Meta no junta las ~50 conversiones/semana que necesita para aprender. Si el presupuesto es menor, arranca con **3 anuncios** en vez de 6.
- Ubicación: **Ciudad Juárez, Chih. + 25 km**. Edad/sexo bloqueados (18-65+, todos) por la categoría especial.
- Público **Advantage+**. **No agregues intereses de "jubilados"**: en esta categoría están restringidos. El filtro de público lo hacen el copy y la imagen ("pensionados y jubilados del IMSS, ISSSTE…").
- Ubicaciones **Advantage+**.
- Calendario: fecha de inicio, sin fecha de fin (pausas manuales).

### 4.3 Anuncios (repetir 6 veces: AD-01 … AD-06)
- Identidad: página **Credito a tu Medida** (+ Instagram si está conectado).
- Formato: **Imagen única** → sube la **1:1** y en "Personalizar por ubicación" pon la **9:16** para Stories y Reels.
- Texto principal: pega **A** y agrega **B** como opción adicional ("+ Agregar opción de texto").
- Titular: **A** y **B**. Descripción la indicada.
- Destino: **Sitio web** → pega la **URL con UTM** de cada anuncio.
- CTA: el indicado en cada anuncio.
- **Mejoras creativas Advantage+:** activa solo *ajustes de brillo/contraste* y *plantilla visual*. **Desactiva** "texto generado por IA", "expandir imagen" y "música". En crédito, un texto inventado por IA puede prometer algo que no ofrecemos y causar rechazo.
- **Seguimiento:** confirma que el dataset esté marcado en "Eventos del sitio web".

### 4.4 Antes de publicar (evita rechazos)
- [ ] Categoría especial financiera marcada.
- [ ] Ningún anuncio menciona tasa, monto, CAT ni plazo (no hay cifras aprobadas y Meta exige mostrarlas completas si se mencionan).
- [ ] Nada de "¿Estás endeudado?" ni "tu mal buró". Meta prohíbe aludir a la situación financiera personal. Los copys ya están redactados en tercera persona/usted.
- [ ] Razón social visible: *Financiera Fortaleza, S.A. de C.V., SOFOM, E.N.R.* (ya va en las imágenes).
- [ ] Si Meta pide **verificación de anunciante financiero** o **verificación del negocio**, completa la del portafolio (RFC/Acta) a nombre de quien tenga el registro SOFOM/Condusef.
- [ ] El sitio carga rápido en celular y el formulario funciona (el Pixel mide ahí).

## Paso 5 · Operación del mes
| Semana | Qué hacer |
|---|---|
| 1 (aprendizaje) | **No tocar nada 7 días.** Solo contestar leads del CRM en menos de 5 min en horario. |
| 2 | Apagar los 2 anuncios con **costo por lead** más alto (si ya gastaron ≥2× el costo promedio). Deja 4. |
| 3 | Si el costo por lead es bueno y los leads califican, **sube el presupuesto 20% máx.** cada 3-4 días (más de 20% reinicia el aprendizaje). |
| 4 | Revisar en el CRM qué UTM (`utm_content=ad-0X`) trae **citas y créditos cerrados**, no solo leads. Renovar creativos del perdedor para el siguiente mes. |

**Métricas que importan:** costo por lead (Ads Manager) · % de leads que contestan · citas agendadas · créditos cerrados (CRM). El CTR solo sirve de diagnóstico.

## Paso 6 · Retargeting (opcional, desde la semana 2)
Con el Pixel ya activo: público personalizado de **visitantes del sitio 30 días que NO enviaron Lead** + **quienes interactuaron con la página 60 días**. Un conjunto aparte con **$50 MXN/día** usando AD-04 y AD-06 (confianza). Siempre con la categoría especial financiera.
