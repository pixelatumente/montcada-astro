import json
import re
import unicodedata
import sys

def slugify(text):
    text = text.lower().strip()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

with open('src/data/enriched-negocios.json') as f:
    data = json.load(f)

negocios = data['negocios']
categories = data['categories']

# Find highest id
max_id = max(int(n.get('id', 0)) for n in negocios)
print(f"Current max ID: {max_id}, total items: {len(negocios)}")

# New public services to add
new_services = [
    {
        "title": "Ayuntamiento de Montcada i Reixac",
        "slug": "ayuntamiento-de-montcada-i-reixac",
        "category": "Servicios públicos y trámites",
        "categories": ["Servicios públicos y trámites"],
        "permalink": "https://montcada.com.es/servicios-publicos-y-tramites/ayuntamiento-de-montcada-i-reixac/",
        "content": "El Ayuntamiento de Montcada i Reixac es la institución pública que gobierna el municipio del Vallès Occidental. En sus instalaciones se gestionan todos los trámites administrativos municipales: empadronamiento, licencias de obras, solicitudes de subvenciones, tributos municipales, registro de entrada de documentos y atención ciudadana. El edificio principal del ayuntamiento está en la Avinguda de la Unitat, donde se concentran la mayoría de servicios administrativos. También cuenta con la Casa de la Vila como edificio auxiliar para determinados servicios municipales. El horario de atención al público es de lunes a viernes de 9:00 a 14:00 horas. Para muchos trámites se puede solicitar cita previa a través de la sede electrónica www.montcada.cat o llamando al 935 726 474.",
        "phone": "935 726 474",
        "clean_content": "El Ayuntamiento de Montcada i Reixac es la institución pública que gobierna el municipio de Montcada i Reixac, en la comarca del Vallès Occidental, provincia de Barcelona. Ofrece servicios de administración general, atención ciudadana (OAC), gestión tributaria, empadronamiento, licencias y permisos, urbanismo y servicios sociales. El horario de atención al público es de lunes a viernes de 9:00 a 14:00 horas en la sede principal de la Avinguda de la Unitat.",
        "excerpt": "El Ayuntamiento de Montcada i Reixac gestiona todos los trámites municipales: empadronamiento, licencias, tributos y atención ciudadana.",
        "address": "Av. de la Unitat, 6, 08110 Montcada i Reixac, Barcelona",
        "enriched": {
            "google_address": "Av. de la Unitat, 6, 08110 Montcada i Reixac, Barcelona, España",
            "google_phone": "935 726 474",
            "google_website": "https://www.montcada.cat",
            "google_hours": ["lunes: 9:00-14:00", "martes: 9:00-14:00", "miércoles: 9:00-14:00", "jueves: 9:00-14:00", "viernes: 9:00-14:00", "sábado: Cerrado", "domingo: Cerrado"],
            "google_business_status": "OPERATIONAL",
            "google_rating": None,
            "google_reviews": None
        }
    },
    {
        "title": "CAP Montcada i Reixac",
        "slug": "cap-montcada-i-reixac",
        "category": "Servicios públicos y trámites",
        "categories": ["Servicios públicos y trámites"],
        "permalink": "https://montcada.com.es/servicios-publicos-y-tramites/cap-montcada-i-reixac/",
        "content": "El CAP Montcada i Reixac (Centro de Atención Primaria) es el centro de salud pública del municipio, gestionado por el Instituto Catalán de la Salud (ICS). Ofrece atención médica general, pediatría, enfermería, atención continuada de urgencias y servicios de prevención y promoción de la salud. Dispone de servicio de extracciones analíticas, vacunación, curas y seguimiento de enfermedades crónicas como diabetes o hipertensión. El centro está ubicado en la calle Jaume I, 1, en pleno centro de Montcada. Para ser atendido es necesario pedir cita previa a través del teléfono 902 111 444.",
        "phone": "935 750 544",
        "clean_content": "El CAP Montcada i Reixac es el centro de atención primaria de referencia del municipio, gestionado por el ICS. Ofrece medicina general, pediatría, enfermería, atención continuada y programas de salud preventiva. Dirección: calle Jaume I, 1. Teléfono cita previa: 902 111 444.",
        "excerpt": "Centro de Atención Primaria del ICS en Montcada con servicios de medicina general, pediatría y atención continuada.",
        "address": "Carrer Jaume I, 1, 08110 Montcada i Reixac, Barcelona",
        "enriched": {
            "google_address": "Carrer Jaume I, 1, 08110 Montcada i Reixac, Barcelona, España",
            "google_phone": "935 750 544",
            "google_website": "https://ics.gencat.cat",
            "google_hours": ["lunes: 8:00-20:00", "martes: 8:00-20:00", "miércoles: 8:00-20:00", "jueves: 8:00-20:00", "viernes: 8:00-20:00", "sábado: 8:00-15:00", "domingo: Cerrado"],
            "google_business_status": "OPERATIONAL",
            "google_rating": None,
            "google_reviews": None
        }
    },
    {
        "title": "CAP Les Indianes",
        "slug": "cap-les-indianes",
        "category": "Servicios públicos y trámites",
        "categories": ["Servicios públicos y trámites"],
        "permalink": "https://montcada.com.es/servicios-publicos-y-tramites/cap-les-indianes/",
        "content": "El CAP Les Indianes es el segundo centro de atención primaria de Montcada i Reixac, gestionado por el ICS. Ofrece medicina general, pediatría, enfermería y programas de salud comunitaria. En este centro se encuentra el Punto de Atención Continuada (PAC) de Montcada, que atiende urgencias fuera del horario ordinario de los centros de salud. Está ubicado en el Camí de la Font Freda, 9, en el barrio de Can Sant Joan. Cita previa: 902 111 444.",
        "phone": "935 752 601",
        "clean_content": "El CAP Les Indianes es el centro de atención primaria del barrio de Can Sant Joan, gestionado por el ICS. Alberga el Punto de Atención Continuada (PAC) para urgencias fuera del horario habitual. Dirección: Camí de la Font Freda, 9.",
        "excerpt": "Centro de Atención Primaria en Can Sant Joan con servicio de urgencias PAC fuera del horario ordinario.",
        "address": "Camí de la Font Freda, 9, 08110 Montcada i Reixac, Barcelona",
        "enriched": {
            "google_address": "Camí de la Font Freda, 9, 08110 Montcada i Reixac, Barcelona, España",
            "google_phone": "935 752 601",
            "google_website": "https://ics.gencat.cat",
            "google_hours": ["lunes: 8:00-20:00", "martes: 8:00-20:00", "miércoles: 8:00-20:00", "jueves: 8:00-20:00", "viernes: 8:00-20:00", "sábado: Cerrado", "domingo: Cerrado"],
            "google_business_status": "OPERATIONAL",
            "google_rating": None,
            "google_reviews": None
        }
    },
    {
        "title": "Biblioteca Can Sant Joan",
        "slug": "biblioteca-can-sant-joan",
        "category": "Servicios públicos y trámites",
        "categories": ["Servicios públicos y trámites"],
        "permalink": "https://montcada.com.es/servicios-publicos-y-tramites/biblioteca-can-sant-joan/",
        "content": "La Biblioteca de Can Sant Joan es una de las dos bibliotecas públicas municipales de Montcada i Reixac, dando servicio al barrio de Can Sant Joan desde los años 90. Gestionada en convenio con la Diputación de Barcelona, ofrece préstamo de libros, películas y música, acceso a internet, zona Wi-Fi, clubes de lectura y talleres infantiles. Dirección: calle Turó, 45.",
        "phone": "935 751 901",
        "clean_content": "Biblioteca pública municipal del barrio de Can Sant Joan con préstamo de documentos, internet y actividades culturales. Dirección: c. Turó, 45.",
        "excerpt": "Biblioteca pública del barrio de Can Sant Joan con préstamo de libros, Wi-Fi y actividades culturales.",
        "address": "c. Turó, 45, 08110 Montcada i Reixac, Barcelona",
        "enriched": {
            "google_address": "c. Turó, 45, 08110 Montcada i Reixac, Barcelona, España",
            "google_phone": "935 751 901",
            "google_website": "https://biblioteques.montcada.cat",
            "google_hours": ["lunes: 9:30-14:30", "martes: 9:30-14:30", "miércoles: 9:30-14:30", "jueves: 9:30-14:30", "viernes: 9:30-14:30", "sábado: Cerrado", "domingo: Cerrado"],
            "google_business_status": "OPERATIONAL",
            "google_rating": None,
            "google_reviews": None
        }
    },
    {
        "title": "Biblioteca Elisenda de Montcada",
        "slug": "biblioteca-elisenda-de-montcada",
        "category": "Servicios públicos y trámites",
        "categories": ["Servicios públicos y trámites"],
        "permalink": "https://montcada.com.es/servicios-publicos-y-tramites/biblioteca-elisenda-de-montcada/",
        "content": "La Biblioteca Elisenda de Montcada es la biblioteca central del municipio, un equipamiento cultural de más de 2.300 m² con auditorio, sala de exposiciones y 47.000 volúmenes. Gestionada con la Diputación de Barcelona, ofrece préstamo, sala de estudio, internet, Wi-Fi, clubes de lectura, presentaciones de libros y talleres. Dirección: calle Tarragona, 32.",
        "phone": "934 925 959",
        "clean_content": "Biblioteca central de Montcada con 47.000 volúmenes, auditorio y programación cultural. Dirección: c. Tarragona, 32.",
        "excerpt": "Biblioteca central con 47.000 volúmenes, auditorio, sala de exposiciones y amplia programación cultural.",
        "address": "c. Tarragona, 32, 08110 Montcada i Reixac, Barcelona",
        "enriched": {
            "google_address": "c. Tarragona, 32, 08110 Montcada i Reixac, Barcelona, España",
            "google_phone": "934 925 959",
            "google_website": "https://biblioteques.montcada.cat",
            "google_hours": ["lunes: 9:30-20:30", "martes: 9:30-20:30", "miércoles: 9:30-20:30", "jueves: 9:30-20:30", "viernes: 9:30-20:30", "sábado: 10:00-14:00", "domingo: Cerrado"],
            "google_business_status": "OPERATIONAL",
            "google_rating": None,
            "google_reviews": None
        }
    },
    {
        "title": "Correos Montcada i Reixac",
        "slug": "correos-montcada-i-reixac",
        "category": "Servicios públicos y trámites",
        "categories": ["Servicios públicos y trámites"],
        "permalink": "https://montcada.com.es/servicios-publicos-y-tramites/correos-montcada-i-reixac/",
        "content": "Oficina de Correos de Montcada i Reixac con todos los servicios postales: envío de cartas y paquetes nacionales e internacionales, correo certificado, burofax, giros postales, paquetería urgente, venta de sellos y embalajes, y notificaciones administrativas. Dirección: Carrer Montiu, 12.",
        "phone": "935 640 347",
        "clean_content": "Oficina de Correos con servicios postales completos en Montcada i Reixac. Dirección: Carrer Montiu, 12.",
        "excerpt": "Oficina de Correos con servicios postales: cartas, paquetes, certificados y giros.",
        "address": "Carrer Montiu, 12, 08110 Montcada i Reixac, Barcelona",
        "enriched": {
            "google_address": "Carrer Montiu, 12, 08110 Montcada i Reixac, Barcelona, España",
            "google_phone": "935 640 347",
            "google_website": "https://www.correos.es",
            "google_hours": ["lunes: 8:30-20:30", "martes: 8:30-20:30", "miércoles: 8:30-20:30", "jueves: 8:30-20:30", "viernes: 8:30-20:30", "sábado: 9:30-13:00", "domingo: Cerrado"],
            "google_business_status": "OPERATIONAL",
            "google_rating": None,
            "google_reviews": None
        }
    },
    {
        "title": "Casal de Gent Gran Casa de la Mina",
        "slug": "casal-de-gent-gran-casa-de-la-mina",
        "category": "Servicios públicos y trámites",
        "categories": ["Servicios públicos y trámites"],
        "permalink": "https://montcada.com.es/servicios-publicos-y-tramites/casal-de-gent-gran-casa-de-la-mina/",
        "content": "El Casal de Gent Gran Casa de la Mina es un equipamiento municipal para personas mayores en un edificio histórico junto al Parc de les Aigües. Ofrece talleres de gimnasia, baile, pintura, informática y memoria, además de excursiones y actividades festivas. Horario: lunes a viernes de 9:30 a 12:30 y de 16:00 a 20:00.",
        "phone": "935 644 418",
        "clean_content": "Centro municipal para personas mayores con talleres y actividades. Edificio histórico junto al Parc de les Aigües.",
        "excerpt": "Centro municipal para mayores con talleres, actividades culturales y excursiones.",
        "address": "Av. de la Unitat, s/n, 08110 Montcada i Reixac, Barcelona",
        "enriched": {
            "google_address": "Avinguda de la Unitat, s/n, 08110 Montcada i Reixac, Barcelona, España",
            "google_phone": "935 644 418",
            "google_website": "https://www.montcada.cat",
            "google_hours": ["lunes: 9:30-12:30, 16:00-20:00", "martes: 9:30-12:30, 16:00-20:00", "miércoles: 9:30-12:30, 16:00-20:00", "jueves: 9:30-12:30, 16:00-20:00", "viernes: 9:30-12:30, 16:00-20:00", "sábado: Cerrado", "domingo: Cerrado"],
            "google_business_status": "OPERATIONAL",
            "google_rating": None,
            "google_reviews": None
        }
    }
]

# Add new entries
for i, svc in enumerate(new_services):
    svc['id'] = str(max_id + 1 + i)
    negocios.append(svc)

# Update category count
servicios_slug = "servicios-publicos-y-tramites"
servicios_count = sum(1 for n in negocios if n.get('category') == 'Servicios públicos y trámites')
cat_found = False
for c in categories:
    if c['slug'] == servicios_slug:
        c['count'] = servicios_count
        cat_found = True
        break
if not cat_found:
    categories.append({"name": "Servicios públicos y trámites", "slug": servicios_slug, "count": servicios_count})

data['total'] = len(negocios)

with open('src/data/enriched-negocios.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Añadidos {len(new_services)} servicios públicos")
print(f"   Total 'Servicios públicos y trámites': {servicios_count}")
print(f"   Total en directorio: {data['total']}")
for s in new_services:
    print(f"   + {s['title']} | 📞 {s['phone']}")
