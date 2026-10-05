# Club Campestre El Bosque — Propuesta de nuevo sitio web

## Cómo verlo
Abre `index.html` con doble clic (Chrome, Edge, Safari o Firefox). Necesitas internet:
las fotos y el video se cargan directo desde clubelbosque.com.co.

Para la presentación, empieza por `propuesta.html` (auditoría del sitio actual + antes/después + hoja de ruta)
y luego navega el sitio nuevo desde el botón "Ver el nuevo sitio".

## Usar las fotos sin conexión (opcional)
    python3 descargar_medios.py
Descarga todas las fotos, el video y el PDF a `assets/media/` y ajusta las rutas para que el sitio funcione sin internet.

## Páginas
- index.html — Inicio: video, acciones rápidas, vistas por perfil (asociado, visitante, empresa, colegio, celebraciones)
- club.html — Historia en línea de tiempo, misión/visión/promesa, juntas
- deportes.html — Golf, tenis, natación, hípica, fútbol, baloncesto (filtro + galerías)
- eventos.html — Salones con capacidad, comparación, cotizador por WhatsApp, galerías de eventos
- gastronomia.html, hospedaje.html, sostenibilidad.html, convenios.html, contacto.html
- asociados.html — Portal del asociado (DEMO con datos de ejemplo) + afiliación
- propuesta.html — Documento de venta

## Pendiente de validar con el club
Textos de natación, hospedaje y sauna/turco (el sitio actual no tiene contenido), juntas vigentes,
tarifas de afiliación y número de WhatsApp principal.

## Técnica
HTML + CSS + JavaScript sin dependencias. Encabezado, pie y menús están en `assets/js/main.js`.
Las páginas se generan desde `_build/` (`python3 _build/build.py`), opcional.
