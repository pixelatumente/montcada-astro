# 🗺️ Guía de Mantenimiento — Montcada Online

> Directorio local de negocios de Montcada i Reixac y municipios cercanos.
> Stack: Astro + Cloudflare Pages + Google Places (datos enriquecidos)

---

## 📁 Estructura del proyecto

```
montcada-astro/
├── src/
│   ├── components/       # Componentes reutilizables
│   │   ├── SearchBar.astro     # Buscador fuzzy (cliente)
│   │   ├── Schema.astro        # Datos estructurados SEO
│   │   ├── AdUnit.astro        # Anuncios AdSense
│   │   ├── Welcome.astro       # Hero de bienvenida
│   │   └── ...
│   ├── layouts/
│   │   ├── BaseLayout.astro    # Layout principal (header, footer, SEO)
│   │   └── Layout.astro        # Layout secundario
│   ├── data/
│   │   └── enriched-negocios.json   # ⭐ TODOS LOS DATOS del directorio
│   ├── pages/
│   │   ├── index.astro                         # Portada
│   │   ├── [categoria].astro                   # Páginas de categoría
│   │   ├── [categoria]/[slug].astro            # Fichas de negocio
│   │   ├── publica-tu-negocio.astro            # Formulario de alta
│   │   ├── tiempo-montcada-i-reixac.astro      # El tiempo
│   │   ├── aviso-legal.astro / politica-*.astro# Páginas legales
│   │   └── peluquerias/peluqueria-gaby.astro   # Landing destacada
│   └── data/
│       └── enriched-negocios.json               # Fuente de datos única
├── public/
│   ├── search-data.json       # Índice para el buscador (se genera automáticamente)
│   ├── montcada-hero.jpg      # Imagen del hero
│   └── logo.jpg               # Logo
├── dist/                      # Build generado (no tocar)
├── astro.config.mjs           # Configuración de Astro
├── wrangler.toml              # Configuración Cloudflare Pages
├── GUIA-MANTENIMIENTO.md      # Este archivo
└── package.json
```

---

## 🧱 Cómo se estructuran los datos

Todo el contenido vive en **`src/data/enriched-negocios.json`**. No hay base de datos. Cada negocio tiene esta estructura:

```json
{
  "title": "Restaurante Fandi",
  "slug": "restaurante-fandi",
  "category": "Restaurantes",
  "category_slug": "restaurantes",
  "phone": "937 91 63 99",
  "address": "Carrer Major, 45, Montcada i Reixac",
  "municipio": "Montcada i Reixac",
  "enriched": {
    "google_place_id": "ChIJ...",
    "google_rating": 4.3,
    "google_reviews": 87,
    "google_maps_url": "https://maps.google.com/?cid=...",
    "google_business_status": "OPERATIONAL",
    "google_hours": ["lunes: 9:00–21:00", ...],
    "google_website": "https://..."
  }
}
```

Además hay un objeto `categories` al inicio del JSON que lista las categorías disponibles:

```json
{
  "categories": [
    { "name": "Restaurantes", "slug": "restaurantes", "count": 157, "icon": "🍽️" },
    ...
  ],
  "total": 384,
  "negocios": [...]
}
```

---

## ➕ Añadir un nuevo negocio

### 1. Añadir a enriched-negocios.json

Abre `src/data/enriched-negocios.json`, ve al array `"negocios"` y añade un nuevo objeto al final:

```json
{
  "title": "Nombre del Negocio",
  "slug": "nombre-del-negocio",
  "category": "Restaurantes",
  "category_slug": "restaurantes",
  "phone": "93X XX XX XX",
  "address": "Calle Ejemplo, 12, Montcada i Reixac",
  "municipio": "Montcada i Reixac",
  "enriched": {}
}
```

**Campos obligatorios:** `title`, `slug`, `category`, `category_slug`.
**Campos opcionales:** `phone`, `address`, `municipio`, `enriched`.

> 💡 **Para obtener datos enriquecidos de Google Places**, puedes pedirle al asistente que los busque automáticamente usando Google Places API.

### 2. Actualizar el contador de categoría

Si es una categoría existente, suma 1 al `count` en el array `categories`. Si es una categoría nueva, añádela al array.

### 3. Actualizar el total

Suma 1 al `total` del directorio.

### 4. Regenerar search-data.json

```bash
cd montcada-astro
node scripts/generate-search-json.js
```

(Si el script no existe, el asistente puede generarlo —lee el JSON y escribe `public/search-data.json` con `{t, c, s}` para cada negocio.)

### 5. Construir y desplegar

```bash
npx astro build          # Genera dist/
git add -A
git commit -m "Añadir Nuevo Restaurante"
git push origin main     # Cloudflare lo despliega automáticamente
```

---

## ✏️ Modificar un negocio existente

1. Busca el negocio en `src/data/enriched-negocios.json` por su `slug`
2. Modifica los campos que necesites
3. Reconstruye y despliega (pasos 4-5 de arriba)

> ⚠️ Si cambias el `slug`, se creará una URL nueva y la vieja dejará de funcionar. Mejor no tocar el slug.

---

## 🗑️ Eliminar un negocio

1. Borra el objeto del array `"negocios"`
2. Resta 1 al `count` de su categoría
3. Resta 1 al `total`
4. Reconstruye y despliega

> Si eliminas el último negocio de una categoría, también puedes borrar la categoría del array `categories`.

---

## 🆕 Añadir una categoría nueva

1. Añade la categoría al array `categories` de `enriched-negocios.json`:
   ```json
   { "name": "Fontaneros", "slug": "fontaneros", "count": 1, "icon": "🔧" }
   ```
2. En `src/pages/index.astro`, añade la categoría al objeto `categoryIcons` para que se muestre con su icono y color:
   ```js
   "Fontaneros": { icon: "🔧", bg: "#E8F5F0" },
   ```
3. Añade negocios con `category: "Fontaneros"`, `category_slug: "fontaneros"`
4. La URL será `/fontaneros/nombre-del-negocio/`
5. Despliega

> Las páginas de categoría y las fichas de negocio se generan automáticamente con el template dinámico `[categoria].astro` y `[categoria]/[slug].astro`. No necesitas crear archivos nuevos.

---

## 🧪 Probar cambios en local

```bash
cd montcada-astro
npx astro dev
```

Abre `http://localhost:4321` para ver los cambios en tiempo real.

---

## 🚀 Despliegue

El proyecto está conectado a **Cloudflare Pages** vía GitHub. Con hacer `git push origin main` se despliega automáticamente a **montcada.com.es**.

Si quieres desplegar manualmente:
```bash
npx astro build
npx wrangler pages deploy dist --project-name=montcada-astro --branch=production
```

---

## 🔍 Cómo funciona el buscador

El buscador (`SearchBar.astro`) carga un archivo JSON ligero (`/search-data.json`) en el cliente y hace búsqueda fuzzy local. No necesita servidor ni llamadas API.

Cada resultado en el JSON es:
```json
{ "t": "Nombre del Negocio", "c": "Categoría", "s": "/categoria/slug/", "d": "descripción", "r": 4.5 }
```

Para regenerar este archivo tras cambios, usa el script de generación o pídele al asistente.

---

## 💡 Notas importantes

- **Los datos de Google Places** (horarios, valoraciones) se obtienen con la API de Google. Si caducan, puedes pedirle al asistente que los refresque.
- **Las páginas legales** (aviso legal, privacidad, cookies) están en `src/pages/` como archivos `.astro` independientes.
- **AdSense** está configurado con Auto Ads + unidades manuales. Si cambias de cuenta, actualiza el `client` en `BaseLayout.astro`.
- **La landing de Peluquería Gaby** es un caso especial con diseño propio (`peluquerias/peluqueria-gaby.astro`). Si quieres hacer lo mismo para otro negocio, puedes pedírselo al asistente.

---

## ❓ Preguntas frecuentes

| Problema | Solución |
|----------|----------|
| Los cambios no se ven en la web | Espera 1-2 minutos a que Cloudflare termine el despliegue. Refresca la página con F5. |
| Error al hacer build | Revisa que `enriched-negocios.json` tenga JSON válido (usa https://jsonlint.com) |
| El buscador no encuentra un negocio | Regenera `public/search-data.json` |
| Quiero cambiar el color del sitio | Los colores están en `:root` de `BaseLayout.astro`. Cambia `--primary`, `--secondary`, etc. |
| Quiero añadir una página nueva | Crea un `.astro` en `src/pages/`. La URL será `/nombre-del-archivo/`. |

---

> **Última actualización:** Junio 2026
> **Asistente:** Puedes pedir ayuda al asistente de Hermes para modificar el directorio —conoce el proyecto y puede hacer cambios directos.
