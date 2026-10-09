# Carolina García B. — Sitio web estático

Sitio one-page de marca personal para **Carolina García Berguecio** (coach, speaker, referente en resiliencia e inclusión, Chile).

## Estructura

```
hermes-handoff/
├── index.html           # Página completa (HTML + CSS + JS inline)
├── assets/              # Imágenes optimizadas
│   ├── hero-bg.jpg      #   Fondo del hero
│   ├── carolina-1.jpeg  #   Foto conferencista
│   ├── carolina-2.jpg   #   Retrato blanco/negro
│   └── carolina-3.png   #   Foto editorial Factor de Éxito
└── README.md            # Este archivo
```

## Características técnicas

- **Static site** — HTML + CSS + JS; `scripts/build.py` prepara solo los archivos públicos para Pages
- **Responsive** — mobile-first, breakpoints en 900px y 560px
- **Tipografía** — Google Fonts (Poppins 300-800)
- **Imágenes** — servidas desde `/assets/` (rutas relativas)
- **Sin backend** — el formulario solo muestra alerta JS, no envía emails
- **WhatsApp flotante** con link directo (`wa.me/56992380039`)

## Deploy actual

El sitio público `carolinagarcia.cl` y `www.carolinagarcia.cl` se sirve desde **Cloudflare Pages**, proyecto `carolinagarcia-public` en la cuenta `7426511883333d726e94f6988eafb07e`. Ambos dominios apuntan por CNAME DNS-only a `carolinagarcia-public.pages.dev`; las rutas del Worker anterior no interceptan ese tráfico. Un cambio en GitHub no publica por sí mismo.

```bash
python scripts/build.py
CLOUDFLARE_ACCOUNT_ID=7426511883333d726e94f6988eafb07e \
  CLOUDFLARE_API_TOKEN="$(< /root/.hermes/secrets/cloudflare_lobo_token)" \
  npx wrangler pages deploy dist --project-name=carolinagarcia-public --branch=master
```

`dist/_worker.js` deniega rutas internas y sirve el resto mediante `env.ASSETS.fetch`; nunca subir todo el repositorio como activos. Verificar `/`, `/accessibility.js` y `/.git/config` en ambos dominios tras cada despliegue.

## Pendientes / TODOs para Carolina

- [ ] Reemplazar las fotos placeholder por fotos profesionales definitivas
- [ ] Conectar el formulario a un servicio real (Formspree, Netlify Forms, Resend, etc.)
- [x] Configurar dominio propio (`carolinagarcia.cl`)
- [ ] Agregar Google Analytics o Plausible
- [ ] Linkear redes sociales reales (LinkedIn, Instagram)
- [ ] Reemplazar logo "CB" por logo real de marca si existe

## Contacto de Carolina

- Email: contacto@carolina-garcia.com
- Email alternativo: carolina@comunidadinclusiva.cl
- Tel: +56 9 9238 0039
