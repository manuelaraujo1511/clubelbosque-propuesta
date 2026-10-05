def venue(name, cap, cap_label, text, imgs, alt, max_cap=400, tags=()):
    pct = round(min(cap, max_cap) / max_cap * 100) if cap else 15
    thumbs = "".join(f'<button aria-label="Ver foto {i+1}"><img src="@U/{im}" alt="" loading="lazy"></button>' for i, im in enumerate(imgs[:4]))
    t = "".join(f'<span class="tag">{x}</span>' for x in tags)
    capblock = (f'<div class="capacity"><strong>{cap}</strong><span>{cap_label}</span></div><div class="capacity-bar" aria-hidden="true"><span style="width:{pct}%"></span></div>'
                if cap else f'<div class="capacity"><strong style="font-size:1.6rem">Ceremonias</strong></div>')
    return f'''
    <article class="venue reveal">
      <div class="venue-media"><img src="@U/{imgs[0]}" alt="{alt}" loading="lazy"><div class="venue-thumbs">{thumbs}</div></div>
      <div class="venue-body">
        <div style="display:flex;gap:.4rem;flex-wrap:wrap">{t}</div>
        <h3 style="font-size:2rem;margin-top:.5rem">{name}</h3>
        {capblock}
        <p style="color:var(--text-muted)">{text}</p>
        <div class="hero-actions" style="margin-top:auto"><a class="btn btn--dark" href="#cotizar">Cotizar este espacio</a></div>
      </div>
    </article>'''

def gallery(group, imgs, alt):
    return '<div class="masonry">' + "".join(
        f'<button data-lightbox="{group}" aria-label="Ampliar foto"><img src="@U/{im}" alt="{alt}" loading="lazy"></button>' for im in imgs) + "</div>"

VENUES = (
  venue("Casona", 400, "personas entre salas y patio principal",
        "Nuestra casona colonial, corazón histórico del club, recibe hasta 400 invitados distribuidos en sus salas y su patio principal empedrado.",
        ["2020/10/casona-5.jpg","2020/03/casona_1-1.jpeg","2020/03/f_administracion_2-1.jpg"], "Casona colonial", tags=("Bodas","Grados","Galas")) +
  venue("Capilla", 0, "",
        "Un espacio adornado con una gran maravilla de recursos naturales e históricos que harán de tu ceremonia una celebración inolvidable.",
        ["2020/03/capilla_3-scaled.jpg","2020/03/capilla_4-scaled.jpg","2020/03/f_capilla-2.jpg","2020/10/f_capilla-1.jpg"], "Capilla del club", tags=("Matrimonios","Primeras comuniones")) +
  venue("Salón Múltiple", 230, "personas en montaje tipo auditorio",
        "Salón de conferencias con ayudas audiovisuales que complementan el desarrollo de tu actividad. Ideal para convenciones y capacitaciones.",
        ["2020/04/f_salon_multiple_3-001.jpg","2020/04/salon_multiple_6-001.jpg","2020/04/salon_multiple_4-001.jpg","2020/04/salon_multiple_5-001.jpg"], "Salón Múltiple", tags=("Corporativo","Audiovisuales")) +
  venue("Salón Verde", 40, "personas en montaje tipo auditorio",
        "Un salón fresco y confortable, con amplio balcón que da un toque de frescura a tus reuniones. Perfecto para juntas y talleres.",
        ["2020/10/f_salon_verde_1-1.jpg","2020/10/f_salon_verde_2.jpg","2020/10/salon_verde_2.jpg","2020/10/salon_verde_4.jpg"], "Salón Verde", tags=("Reuniones","Balcón"))
)

EVENTOS = dict(
slug="eventos",
title="Salones y eventos · Bodas, corporativos y colegios | Club Campestre El Bosque",
desc="Capilla, Casona colonial para 400 personas, Salón Múltiple para 230 y Salón Verde para 40. Cotiza tu evento social, corporativo o salida pedagógica.",
og="2020/10/casona-5.jpg",
body="""
<section class="page-hero">
  <img src="@U/2020/10/casona-5.jpg" alt="">
  <div class="container">
    <nav class="breadcrumb" aria-label="Ruta"><a href="index.html">Inicio</a><span>/</span><span>Salones y eventos</span></nav>
    <h1>Celebra rodeado de historia y naturaleza</h1>
    <p class="lead">Espacios para eventos sociales, culturales, corporativos y todo tipo de celebraciones, de 40 a 400 personas.</p>
    <div class="hero-actions"><a class="btn btn--primary" href="#cotizar">Cotizar mi evento</a><a class="btn btn--ghost" href="#comparar">Comparar salones</a></div>
  </div>
</section>

<section class="section" aria-labelledby="salones-h">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow">Nuestros espacios</span><h2 id="salones-h">Elige el escenario de tu evento</h2></div></div>
    """ + VENUES + """
  </div>
</section>

<section class="section--tight" id="comparar" aria-labelledby="comp-h">
  <div class="container">
    <h2 id="comp-h" class="reveal" style="font-size:clamp(1.6rem,3vw,2.2rem)">Comparación rápida</h2>
    <div class="table-wrap reveal">
      <table class="compare">
        <caption class="sr-only" style="position:absolute;left:-9999px">Capacidad y uso recomendado de cada salón</caption>
        <thead><tr><th scope="col">Espacio</th><th scope="col">Capacidad</th><th scope="col">Ideal para</th><th scope="col">Destacado</th></tr></thead>
        <tbody>
          <tr><td>Casona</td><td>Hasta 400</td><td>Bodas, galas, grados</td><td>Patio colonial empedrado</td></tr>
          <tr><td>Salón Múltiple</td><td>230 (auditorio)</td><td>Convenciones, capacitaciones</td><td>Ayudas audiovisuales</td></tr>
          <tr><td>Salón Verde</td><td>40 (auditorio)</td><td>Juntas, talleres</td><td>Balcón amplio</td></tr>
          <tr><td>Capilla</td><td>Ceremonias</td><td>Matrimonios, sacramentos</td><td>Entorno natural e histórico</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section--alt" id="cotizar" aria-labelledby="cot-h">
  <div class="container split" style="align-items:start">
    <div class="reveal">
      <span class="eyebrow">Cotizador</span>
      <h2 id="cot-h">Cuéntanos tu evento en 1 minuto</h2>
      <p class="lead">Recibe una propuesta a la medida. Reservas en las líneas de atención de domingo a domingo.</p>
      <ul class="check-list">
        <li>Respuesta del equipo de eventos por WhatsApp o correo</li>
        <li>Montaje, alimentación y hospedaje en un solo lugar</li>
        <li>Visita guiada previa a los espacios</li>
      </ul>
    </div>
    <form class="form form-card reveal reveal-d1" data-demo="whatsapp" novalidate>
      <div class="field"><span style="font-weight:600;font-size:.88rem">Tipo de evento</span>
        <div class="segmented">
          <input type="radio" name="Tipo" id="ev1" value="Boda" checked><label for="ev1">Boda</label>
          <input type="radio" name="Tipo" id="ev2" value="15 años"><label for="ev2">15 años</label>
          <input type="radio" name="Tipo" id="ev3" value="Corporativo"><label for="ev3">Corporativo</label>
          <input type="radio" name="Tipo" id="ev4" value="Colegio"><label for="ev4">Colegio</label>
          <input type="radio" name="Tipo" id="ev5" value="Otro"><label for="ev5">Otro</label>
        </div>
      </div>
      <div class="form-row">
        <div class="field"><label for="c-fecha">Fecha tentativa</label><input id="c-fecha" name="Fecha" type="date" required></div>
        <div class="field"><label for="c-inv">Invitados</label><select id="c-inv" name="Invitados" required><option value="">Selecciona</option><option>Hasta 40</option><option>41 – 100</option><option>101 – 230</option><option>231 – 400</option><option>Más de 400</option></select></div>
      </div>
      <div class="form-row">
        <div class="field"><label for="c-nom">Nombre</label><input id="c-nom" name="Nombre" autocomplete="name" required></div>
        <div class="field"><label for="c-cel">Celular</label><input id="c-cel" name="Celular" type="tel" autocomplete="tel" inputmode="tel" required></div>
      </div>
      <div class="field"><label for="c-msg">¿Algo más que debamos saber?</label><textarea id="c-msg" name="Detalles" placeholder="Alimentación, hospedaje, decoración…"></textarea></div>
      <button class="btn btn--primary" type="submit">Enviar solicitud por WhatsApp</button>
      <p class="form-success" tabindex="-1" role="status">¡Gracias! Abrimos WhatsApp con tu solicitud para que la envíes al equipo de eventos.</p>
    </form>
  </div>
</section>

<section class="section" id="comunidad" aria-labelledby="com-h">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow">Galería</span><h2 id="com-h">Eventos que ya vivimos</h2><p class="lead">Compartiendo con la gran familia Club El Bosque.</p></div></div>

    <div id="social" class="reveal" style="scroll-margin-top:100px">
      <h3>Eventos sociales</h3><p style="color:var(--text-muted)">Nuestras instalaciones son el deleite para hacer tus sueños realidad: Día de la Madre, 15 años y más.</p>
      """ + gallery("social", ["2020/03/eventos-8.jpg","2020/03/dia_madre-1.jpg","2020/03/eventos-13.jpg","2020/03/dia_madre-16.jpg","2020/03/15_a%C3%B1os-37-780x675.jpeg","2020/03/dia_madre-4.jpg","2020/03/dia_madre-5.jpg","2020/03/dia_madre-7.jpg"], "Evento social en el club") + """
    </div>

    <div id="corporativo" class="reveal" style="margin-top:3rem;scroll-margin-top:100px">
      <h3>Eventos corporativos</h3><p style="color:var(--text-muted)">Grandes y amplios espacios ideales para eventos empresariales y de integración.</p>
      """ + gallery("corp", ["2020/03/eventos-2.jpeg","2020/03/eventos-17.jpg","2020/03/eventos-5.jpeg","2020/03/eventos-4.jpeg","2020/03/eventos-1.jpeg","2020/03/eventos-3.jpeg","2020/03/eventos-7.jpeg","2020/03/eventos-6.jpg"], "Evento corporativo") + """
    </div>

    <div id="deportivo" class="reveal" style="margin-top:3rem;scroll-margin-top:100px">
      <h3>Eventos deportivos</h3><p style="color:var(--text-muted)">Competencias que incentivan el sano desarrollo físico y emocional.</p>
      """ + gallery("dep", ["2020/03/futbol-1.jpg","2020/03/futbol-5.jpg","2020/03/futbol-6.jpg"], "Torneo deportivo") + """
    </div>

    <div id="colegios" class="reveal" style="margin-top:3rem;scroll-margin-top:100px">
      <h3>Salidas pedagógicas</h3><p style="color:var(--text-muted)">Espacios de formación que favorecen el desarrollo integral de la comunidad educativa.</p>
      """ + gallery("ped", ["2020/03/IMG_20190628_100415629_HDR.jpg","2020/03/IMG_20190501_120307259_HDR.jpg","2020/03/IMG_20190628_131745499.jpg","2020/03/IMG_20190501_123653517_HDR.jpg","2020/03/IMG_20190501_141737012_HDR.jpg"], "Salida pedagógica") + """
      <a class="btn btn--dark" href="#cotizar">Programar salida pedagógica</a>
    </div>

    <div id="familia" class="reveal" style="margin-top:3rem;scroll-margin-top:100px">
      <h3>Familia El Bosque</h3><p style="color:var(--text-muted)">Un evento diseñado para reunir a nuestras familias y asociados para compartir y conocernos dentro del club.</p>
      """ + gallery("fam", ["2020/03/famila_bosque-1.jpg"], "Encuentro Familia El Bosque") + """
    </div>
  </div>
</section>
"""
)
