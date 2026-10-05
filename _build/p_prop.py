def a(sev, title, problem, fix):
    label = {"high": "Crítico", "med": "Importante", "low": "Mejora"}[sev]
    return f'<article class="audit-card reveal"><span class="sev sev-{sev}">{label}</span><h3>{title}</h3><p>{problem}</p><p class="fix">→ {fix}</p></article>'

FINDINGS = "".join([
  a("high", "Página de Natación sin contenido propio", "El menú Deportes › Natación muestra un listado de entradas del blog (convenios, eventos) en lugar de información de piscinas.", "Página dedicada con fotos, horarios y reglas de uso."),
  a("high", "Hospedaje y Sauna y Turco están vacías", "Ambas páginas cargan sin texto ni imágenes. Un visitante interesado en quedarse no encuentra nada y abandona.", "Fichas de cabañas, camping y zona húmeda con formulario de disponibilidad."),
  a("high", "Aspirantes a socio sin respuesta", "En la entrada de Convenios hay comentarios públicos de 2021 preguntando costos de afiliación que nunca se respondieron.", "Sección de Afiliación con proceso en 3 pasos y formulario que llega al equipo comercial."),
  a("high", "Sin una acción principal clara", "La portada no invita a reservar, cotizar ni afiliarse (solo enlaces “Ver más”) y el formulario de contacto es genérico.", "Barra de acciones rápidas, cotizador de eventos y CTAs por perfil de usuario."),
  a("med", "Teléfono con indicativo desactualizado", "Se publica “(031) 8987081”. Desde 2021 los fijos en Colombia se marcan con el indicativo 601.", "Actualizado a (601) 898 7081 con enlace para llamar desde el celular."),
  a("med", "WhatsApp abre WhatsApp Web", "Los enlaces apuntan a web.whatsapp.com, que en celulares no abre la app directamente.", "Enlaces wa.me con mensaje prellenado y botón flotante."),
  a("med", "Contenido desactualizado", "Las juntas publicadas son del periodo 2021–2023 y las entradas de eventos más recientes son de 2020.", "Gestor de contenidos simple para que el club publique noticias y eventos."),
  a("med", "Errores de redacción", "Textos como “Eventos? el club…”, “Camping? El Club…”, “sano aparecimiento” y fotos de 15 años con el pie “nuestras Madres”.", "Revisión editorial completa de todos los textos."),
  a("med", "Misión y Promesa de valor idénticas", "La página Promesa de valor repite palabra por palabra el texto de la Misión.", "Propósito presentado en una sola vista con tres mensajes diferenciados."),
  a("med", "Imágenes pesadas y slider", "Fotos de hasta 2560 px sin optimizar y un slider de 6 imágenes, que hacen lenta la carga en datos móviles.", "Imágenes WebP/AVIF responsivas, carga diferida y video de portada con póster."),
  a("low", "Direcciones poco amigables", "Convenios vive en /1757-2/ y los eventos repiten widgets de blog (“Comentarios recientes”).", "URLs legibles, metadatos para Google y redes sociales."),
  a("low", "Sin accesibilidad ni segmentación", "No hay opciones de tamaño de texto o contraste, ni rutas pensadas para socios, empresas o colegios.", "Panel de accesibilidad y portada con vistas por tipo de usuario."),
])

PROPUESTA = dict(
slug="propuesta",
title="Propuesta de rediseño web · Club Campestre El Bosque",
desc="Auditoría del sitio actual y propuesta de un nuevo sitio web moderno, accesible y orientado a resultados para el Club Campestre El Bosque.",
body=f"""
<section class="page-hero">
  <img src="@U/2020/03/f_golf-12-006.jpg" alt="">
  <div class="container">
    <span class="eyebrow" style="color:var(--gold-400)">Propuesta de Manuel Araujo · <span data-year></span></span>
    <h1>Un sitio a la altura del club</h1>
    <p class="lead">Revisamos todas las páginas de clubelbosque.com.co. Este documento resume lo que encontramos y cómo el nuevo sitio lo resuelve.</p>
    <div class="hero-actions" style="margin-top:1.5rem"><a class="btn btn--primary" href="index.html">Ver el nuevo sitio</a><a class="btn btn--ghost" href="#hallazgos">Ver hallazgos</a></div>
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="stats">
      <div class="stat reveal"><strong data-count="30">30</strong><span>páginas y entradas revisadas</span></div>
      <div class="stat reveal reveal-d1"><strong data-count="3">3</strong><span>páginas del menú vacías o rotas</span></div>
      <div class="stat reveal reveal-d2"><strong data-count="2">2</strong><span>prospectos de socio sin respuesta</span></div>
      <div class="stat reveal reveal-d3"><strong>2020</strong><span>año de la última entrada de eventos</span></div>
    </div>
  </div>
</section>

<section class="section" id="hallazgos">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow">Auditoría</span><h2>Lo que encontramos</h2><p class="lead">Hallazgos ordenados por impacto en la experiencia del usuario y en la captación de socios y eventos.</p></div></div>
    <div class="audit-grid">{FINDINGS}</div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow">Antes y después</span><h2>Qué cambia para cada usuario</h2></div></div>
    <div class="ba reveal">
      <div class="before"><h3>Sitio actual</h3><ul>
        <li>Menú con 25 enlaces y páginas vacías</li><li>Información dispersa en entradas de blog</li><li>Sin reservas ni cotización</li><li>Diseño de 2020 poco adaptado a celular</li><li>Sin vista para el asociado</li></ul></div>
      <div class="after"><h3>Nuevo sitio</h3><ul>
        <li>3 grupos de menú visual con fotos (mega menú)</li><li>Vistas por perfil: asociado, visitante, empresa, colegio, celebraciones</li><li>Cotizador de eventos y solicitud de hospedaje que llegan por WhatsApp</li><li>Diseño móvil primero con barra de acciones (llamar, reservar, cómo llegar)</li><li>Portal del asociado: carné digital, reservas y estado de cuenta</li></ul></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow">Principios de UX aplicados</span><h2>Diseñado para todos</h2></div></div>
    <div class="grid grid-3">
      <div class="value-card reveal"><span class="num">MÓVIL PRIMERO</span><h3>Pensado para el celular</h3><p>Barra inferior con acciones clave, botones de 48 px y formularios con teclado adecuado para cada dato.</p></div>
      <div class="value-card reveal reveal-d1"><span class="num">ACCESIBILIDAD</span><h3>Pautas WCAG 2.2</h3><p>Contraste AA, navegación con teclado, textos alternativos, controles de tamaño de texto y alto contraste, respeto a “reducir movimiento”.</p></div>
      <div class="value-card reveal reveal-d2"><span class="num">CONVERSIÓN</span><h3>Cada página lleva a una acción</h3><p>Reservar, cotizar, afiliarse o llegar al club: siempre a un clic, con WhatsApp como canal principal.</p></div>
      <div class="value-card reveal"><span class="num">ARQUITECTURA</span><h3>Menos clics</h3><p>De 25 enlaces sueltos a 5 secciones claras, con migas de pan y enlaces directos a cada deporte.</p></div>
      <div class="value-card reveal reveal-d1"><span class="num">RENDIMIENTO</span><h3>Carga rápida</h3><p>Carga diferida de imágenes, video con póster y sin librerías pesadas: HTML, CSS y JavaScript ligeros.</p></div>
      <div class="value-card reveal reveal-d2"><span class="num">IDENTIDAD</span><h3>Fiel al club</h3><p>Paleta inspirada en el escudo (verde bosque y dorado) y el polvo de ladrillo del tenis; tipografía con carácter colonial.</p></div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow">Hoja de ruta</span><h2>Cómo lo llevamos a producción</h2></div></div>
    <div class="roadmap">
      <div class="step reveal"><h3>Descubrimiento</h3><p>Validación de contenidos con gerencia, tarifas, fotos nuevas y textos de hospedaje y natación.</p></div>
      <div class="step reveal reveal-d1"><h3>Diseño final</h3><p>Ajustes sobre este prototipo y aprobación de cada vista.</p></div>
      <div class="step reveal reveal-d2"><h3>Desarrollo</h3><p>Gestor de contenidos, integración de reservas, pagos y portal del asociado.</p></div>
      <div class="step reveal reveal-d3"><h3>Lanzamiento</h3><p>Migración, SEO, analítica y capacitación del equipo del club.</p></div>
    </div>
  </div>
</section>

<section class="section" id="autor">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow">Quién presenta esta propuesta</span><h2>Manuel Araujo</h2>
      <p class="lead">Este prototipo fue diseñado y desarrollado por Manuel Araujo como propuesta independiente para el Club Campestre El Bosque. No es el sitio oficial del club: los textos e imágenes provienen de clubelbosque.com.co y se usan solo para ilustrar la propuesta.</p></div></div>
    <div class="hero-actions reveal" data-author-contact></div>
  </div>
</section>
"""
)
