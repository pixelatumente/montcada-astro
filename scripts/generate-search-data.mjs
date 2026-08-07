/**
 * Generate search-data.json from enriched-negocios.json
 * Run before each build: node scripts/generate-search-data.mjs
 */
import { readFileSync, writeFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const projectRoot = join(__dirname, '..');

const data = JSON.parse(readFileSync(join(projectRoot, 'src/data/enriched-negocios.json'), 'utf-8'));

const searchData = data.negocios.map(n => {
  const e = n.enriched || {};
  const catSlug = n.category.toLowerCase()
    .normalize("NFD").replace(/[\u0300-\u036f]/g, "")
    .replace(/[\s|]+/g, "-").replace(/[^a-z0-9-]/g, "");

  return {
    t: n.title,
    c: n.category,
    d: (n.excerpt || n.clean_content || '').slice(0, 200),
    s: `/${catSlug}/${n.slug}/`,
    r: e.google_rating || 0
  };
});

// Also add categories as searchable items
data.categories.filter(c => c.slug !== "mir").forEach(c => {
  searchData.push({
    t: c.name,
    c: "Categoría",
    d: `${c.count} negocios en Montcada i Reixac`,
    s: `/${c.slug}/`,
    r: 0
  });
});

writeFileSync(join(projectRoot, 'public/search-data.json'), JSON.stringify(searchData), 'utf-8');
console.log(`✅ search-data.json generated with ${searchData.length} entries`);
