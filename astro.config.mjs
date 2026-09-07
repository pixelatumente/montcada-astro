// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://montcada.com.es',
  integrations: [
    sitemap({
      filter: (page) => {
        // Exclude legal pages from sitemap
        const excluded = ['/aviso-legal/', '/politica-privacidad/', '/politica-cookies/', '/publica-tu-negocio/', '/admin/'];
        return !excluded.includes(new URL(page).pathname);
      }
    })
  ],
});
