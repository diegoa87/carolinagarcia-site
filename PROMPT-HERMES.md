# 🚀 PROMPT PARA AGENTE HERMES — Subir web de Carolina

Copia y pega este prompt tal cual al agente Hermes:

---

**Tarea:** Desplegar el sitio web estático de Carolina García Berguecio a producción.

**Path del proyecto:** `/workspace/hermes-handoff/`

**Estructura:**
- `index.html` — página completa con HTML + CSS + JS embebido
- `assets/` — 4 imágenes (hero-bg.jpg, carolina-1.jpeg, carolina-2.jpg, carolina-3.png)
- `README.md` — documentación del proyecto

**Deploy target:** Static site (HTML/CSS/JS, sin build). Cualquier host de static sites funciona:
- **Opción 1 (recomendada):** Cloudflare Pages o Netlify — drag & drop del directorio
- **Opción 2:** Vercel — `vercel deploy --prod` desde el directorio
- **Opción 3:** GitHub Pages — push a repo, habilitar Pages desde `main`
- **Opción 4:** S3 + CloudFront o cualquier static host

**Pasos a ejecutar:**

1. **Verificar contenido del directorio:**
   ```bash
   ls -la /workspace/hermes-handoff/
   ls -la /workspace/hermes-handoff/assets/
   ```
   Debe haber 1 HTML, 1 README y 4 imágenes.

2. **Verificar que el sitio abre localmente (sanity check):**
   ```bash
   cd /workspace/hermes-handoff
   python3 -m http.server 8080 &
   sleep 2
   curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost:8080/
   pkill -f "http.server 8080"
   ```
   Debe devolver `HTTP 200`.

3. **Subir a producción** usando la herramienta preferida del agente (Netlify drop, Vercel CLI, Cloudflare Pages, etc.). Si hay credenciales configuradas, úsalas. Si no, pedir al usuario que las provea.

4. **Verificar el deploy:**
   - Hacer GET a la URL final
   - Tomar screenshot con playwright/chromium para confirmar visual
   - Reportar la URL pública al usuario

5. **Reportar al usuario con:**
   - URL final del sitio en producción
   - Screenshot del hero funcionando
   - Cualquier warning o pendiente (ej: dominio custom, SSL, etc.)

**Notas importantes:**

- El sitio ya está desplegado en `https://aw3dwp8z07qh.space.minimax.io` — el nuevo deploy puede reemplazarlo o coexistir (según prefiera el usuario).
- Es un sitio 100% estático. NO requiere Node, build step, ni dependencias.
- NO modificar el HTML/CSS — solo desplegar tal cual.
- El sitio tiene un formulario que actualmente solo muestra una alerta JS. No se puede probar envío real sin backend (es intencional, está documentado en el README).
- Las imágenes están optimizadas y pesan en total ~1.5MB.

**Output esperado:**

Al terminar, devolver:
1. URL pública final
2. Screenshot del hero en producción
3. Confirmación de que las 4 imágenes cargan correctamente
4. Estado del SSL (debe ser HTTPS válido)
5. Cualquier issue encontrado

---

**TL;DR para Hermes:** Es un sitio estático simple. Súbelo a Netlify/Cloudflare/Vercel, dame la URL, confirma que carga.
