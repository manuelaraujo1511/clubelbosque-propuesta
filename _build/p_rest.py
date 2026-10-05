def hero(img, crumb, h1, lead, actions=""):
    return f'''
<section class="page-hero">
  <img src="@U/{img}" alt="">
  <div class="container">
    <nav class="breadcrumb" aria-label="Ruta"><a href="index.html">Inicio</a><span>/</span><span>{crumb}</span></nav>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>{actions}
  </div>
</section>'''

def card(img, tag, title, text, delay=""):
    return f'''<article class="card reveal {delay}"><div class="card-media"><img src="@U/{img}" alt="{title}" loading="lazy"><span class="tag">{tag}</span></div><div class="card-body"><h3>{title}</h3><p>{text}</p></div></article>'''

GASTRONOMIA = dict(
slug="gastronomia",
title="Gastronomía · Parrilla y cafeterías | Club Campestre El Bosque",
desc="Parrilla, Cafetería Uno, Cafetería Tres y Cafetería Hípica: lugares para compartir en familia en un entorno campestre.",
og="2020/04/restaurante-1.jpeg",
body=hero("2020/04/restaurante-1.jpeg","Gastronomía","Sabores para compartir en familia","Diferentes lugares para disfrutar alimentos con familia y amigos, con vista a la naturaleza.",
          '<div class="hero-actions" style="margin-top:1.5rem"><a class="btn btn--primary" href="contacto.html#visita">Reservar mesa</a></div>') + """
<section class="section">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow">Restaurantes</span><h2>Cuatro ambientes, un mismo paisaje</h2></div></div>
    <div class="grid grid-2">
      """ + card("2020/04/restaurante-1.jpeg","Tardes y noches","Parrilla","En las tardes y noches, el lugar perfecto para compartir en familia alrededor de la parrilla.") +
      card("2020/10/f_cafeteria_deportiva-1.jpg","Vista campestre","Cafetería Uno","Su estructura y entorno campestre te permiten disfrutar un momento tranquilo con una estupenda vista.","reveal-d1") +
      card("2020/10/f_cafeteria_3.jpg","Zona deportiva","Cafetería Tres","Un punto de encuentro para recargar energía entre partido y partido.") +
      card("2020/10/f_cafeteria_hipica-1.jpg","Ambiente equino","Cafetería Hípica","Un pequeño y acogedor lugar que ofrece una gran experiencia rodeado de un ambiente equino.","reveal-d1") + """
    </div>
    <div class="masonry reveal" style="margin-top:2.5rem">
      <button data-lightbox="gastro"><img src="@U/2020/10/f_cafeteria_3_2.jpg" alt="Cafetería Tres" loading="lazy"></button>
      <button data-lightbox="gastro"><img src="@U/2020/10/cafeteria_3_1.jpg" alt="Interior de cafetería" loading="lazy"></button>
      <button data-lightbox="gastro"><img src="@U/2020/10/f_cafeteria_hipica-2.jpg" alt="Cafetería Hípica" loading="lazy"></button>
    </div>
  </div>
</section>
<section class="section--tight"><div class="container"><div class="cta-band reveal">
  <img src="@U/2020/10/f_cafeteria_hipica-2.jpg" alt="" loading="lazy">
  <h2>¿Celebración especial?</h2><p class="lead">Reservas en las líneas de atención al cliente de domingo a domingo.</p>
  <div class="hero-actions"><a class="btn btn--primary" href="contacto.html#visita">Reservar</a><a class="btn btn--ghost" href="eventos.html#cotizar">Cotizar evento</a></div>
</div></div></section>
"""
)

HOSPEDAJE = dict(
slug="hospedaje",
title="Hospedaje y bienestar · Cabañas, camping, sauna y turco | Club Campestre El Bosque",
desc="Cabañas, zona de camping con los mejores paisajes, sauna y turco en el Club Campestre El Bosque, Silvania.",
og="2020/03/sendero.jpeg",
body=hero("2020/03/f_club-21.jpg","Hospedaje y bienestar","Quédate una noche más","Cabañas y camping con los mejores paisajes del club, y zona húmeda para relajarte después del deporte.",
          '<div class="hero-actions" style="margin-top:1.5rem"><a class="btn btn--primary" href="#reservar">Consultar disponibilidad</a></div>') + """
<section class="section">
  <div class="container">
    <div class="grid grid-3">
      """ + card("2020/03/f_club-12.jpg","Hospedaje","Cabañas","Descansa en medio de la naturaleza y amanece con el sonido del río.") +
      card("2020/03/sendero.jpeg","Al aire libre","Camping","Los mejores paisajes del club para acampar en familia o con amigos.","reveal-d1") +
      card("2020/03/f_lugares-9.jpg","Bienestar","Sauna y turco","Zona húmeda para relajarte y recuperarte después de una jornada deportiva.","reveal-d2") + """
    </div>
  </div>
</section>
<section class="section section--alt" id="reservar">
  <div class="container split" style="align-items:start">
    <div class="reveal"><span class="eyebrow">Disponibilidad</span><h2>Planea tu estadía</h2><p class="lead">Déjanos tus fechas y te confirmamos disponibilidad y tarifas vigentes.</p></div>
    <form class="form form-card reveal reveal-d1" data-demo="whatsapp" novalidate>
      <div class="field"><span style="font-weight:600;font-size:.88rem">Tipo de estadía</span><div class="segmented">
        <input type="radio" name="Estadía" id="h1" value="Cabaña" checked><label for="h1">Cabaña</label>
        <input type="radio" name="Estadía" id="h2" value="Camping"><label for="h2">Camping</label></div></div>
      <div class="form-row"><div class="field"><label for="h-in">Llegada</label><input id="h-in" name="Llegada" type="date" required></div><div class="field"><label for="h-out">Salida</label><input id="h-out" name="Salida" type="date" required></div></div>
      <div class="form-row"><div class="field"><label for="h-p">Personas</label><input id="h-p" name="Personas" type="number" min="1" value="2" required></div><div class="field"><label for="h-n">Nombre</label><input id="h-n" name="Nombre" autocomplete="name" required></div></div>
      <button class="btn btn--primary" type="submit">Consultar por WhatsApp</button>
      <p class="form-success" tabindex="-1" role="status">¡Listo! Abrimos WhatsApp con tu solicitud.</p>
    </form>
  </div>
</section>
"""
)

SOSTENIBILIDAD = dict(
slug="sostenibilidad",
title="Sostenibilidad · Naturaleza y turismo ecológico | Club Campestre El Bosque",
desc="52 fanegadas de bosque, lago, senderos y el río Chocho: el compromiso del club con la naturaleza y las comunidades vecinas.",
og="2020/03/lago_garza.jpg",
body=hero("2020/03/lago_garza.jpg","Sostenibilidad","Cuidamos el bosque que nos da nombre","En armonía con la comunidad y con la naturaleza: ese es nuestro compromiso.") + """
<section class="section">
  <div class="container split">
    <div class="reveal"><span class="eyebrow">Turismo ecológico y familiar</span><h2>Un modelo que beneficia a nuestro entorno</h2>
      <p class="lead">Nuestra visión es proyectarnos como modelo del turismo ecológico y familiar, cuya labor social, cultural y económica repercuta en beneficio de las comunidades que nos rodean.</p>
      <ul class="check-list"><li>Senderos entre samanes, ceibas y chicalaes</li><li>Lago con fauna nativa, como garzas</li><li>Ribera del río Chocho (Fusagasugá)</li><li>Patrimonio arquitectónico colonial conservado</li></ul>
    </div>
    <div class="split-media reveal reveal-d1"><img src="@U/2020/03/f_lago.jpg" alt="Lago del club" loading="lazy"><div class="floating"><strong>52</strong>fanegadas de naturaleza protegida</div></div>
  </div>
</section>
<section class="section section--alt">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow">Galería</span><h2>Paisajes del club</h2></div></div>
    <div class="masonry reveal">
      <button data-lightbox="eco"><img src="@U/2020/03/sendero.jpeg" alt="Sendero" loading="lazy"></button>
      <button data-lightbox="eco"><img src="@U/2020/03/lago_garza.jpg" alt="Garza en el lago" loading="lazy"></button>
      <button data-lightbox="eco"><img src="@U/2020/03/f_club-12.jpg" alt="Zonas verdes del club" loading="lazy"></button>
      <button data-lightbox="eco"><img src="@U/2020/03/f_lugares-9.jpg" alt="Rincón natural del club" loading="lazy"></button>
      <button data-lightbox="eco"><img src="@U/2020/03/f_lugares-8.jpg" alt="Paisaje del club" loading="lazy"></button>
      <button data-lightbox="eco"><img src="@U/2020/03/f_club-21.jpg" alt="Instalaciones entre árboles" loading="lazy"></button>
      <button data-lightbox="eco"><img src="@U/2020/03/f_fuente-compressor.jpg" alt="Fuente del club" loading="lazy"></button>
    </div>
  </div>
</section>
"""
)

CONVENIOS = dict(
slug="convenios",
title="Convenios para asociados | Club Campestre El Bosque",
desc="Con el carné del Club El Bosque ingresa al Serrezuela Country Club y gratis a las sedes del Club Militar.",
og="2020/12/serrezuela-1.jpeg",
body=hero("2020/03/f_lago.jpg","Convenios","Tu carné vale en más clubes","Beneficios exclusivos para asociados del Club Campestre El Bosque.") + """
<section class="section">
  <div class="container">
    <div class="grid grid-2">
      <article class="card reveal"><div class="card-media"><img src="@U/2020/12/serrezuela-1.jpeg" alt="Serrezuela Country Club" loading="lazy"><span class="tag">Convenio</span></div>
        <div class="card-body"><h3>Serrezuela Country Club</h3><p>Ingresa con el carné de nuestro club.</p>
        <a class="link-arrow" href="https://clubelbosque.com.co/wp-content/uploads/2020/12/COMUNICACIO%CC%81N-CONVENIO-CLUB-SERREZUELA.pdf" target="_blank" rel="noopener">Ver condiciones (PDF)</a></div></article>
      <article class="card reveal reveal-d1"><div class="card-media"><img src="@U/2020/12/militar-1.jpeg" alt="Club Militar" loading="lazy"><span class="tag">Gratis</span></div>
        <div class="card-body"><h3>Club Militar — todas las sedes</h3><p>Ingreso gratuito presentando tu carné:</p>
        <ul class="check-list" style="margin:.75rem 0 0"><li>Sede Bogotá (Puente Aranda)</li><li>Sede Melgar (Las Mercedes)</li><li>Sede Boyacá (Lago Sochagota)</li><li>Sede Santa Marta (San Fernando)</li></ul></div></article>
    </div>
  </div>
</section>
<section class="section--tight"><div class="container"><div class="cta-band reveal">
  <img src="@U/2020/03/f_entrada-compressor-1.jpg" alt="" loading="lazy">
  <h2>¿Aún no eres asociado?</h2><p class="lead">Conoce los requisitos y recibe la información de afiliación.</p>
  <div class="hero-actions"><a class="btn btn--primary" href="asociados.html#afiliacion">Quiero afiliarme</a></div>
</div></div></section>
"""
)

CONTACTO = dict(
slug="contacto",
title="Contacto y cómo llegar | Club Campestre El Bosque",
desc="KM 37 vía Silvania – Tibacuy, Cundinamarca. Teléfono (601) 898 7081, WhatsApp y gerencia@clubelbosque.com.co.",
body=hero("2020/03/f_entrada-compressor-1.jpg","Contacto","Estamos para ayudarte","Escríbenos y te contactaremos lo antes posible. Atención de domingo a domingo.") + """
<section class="section" id="visita">
  <div class="container split" style="align-items:start">
    <div class="reveal">
      <span class="eyebrow">Canales de atención</span>
      <h2>Habla con nosotros</h2>
      <ul class="contact-list" style="margin-top:1.5rem">
        <li><span class="quick-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg></span><div><small style="color:var(--text-muted)">Teléfono</small><br><a href="tel:+576018987081">(601) 898 7081</a></div></li>
        <li><span class="quick-icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Z"/></svg></span><div><small style="color:var(--text-muted)">WhatsApp</small><br><a href="https://wa.me/573164341805" target="_blank" rel="noopener">+57 316 434 1805</a> · <a href="https://wa.me/573164072744" target="_blank" rel="noopener">+57 316 407 2744</a></div></li>
        <li><span class="quick-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span><div><small style="color:var(--text-muted)">Correo</small><br><a href="mailto:gerencia@clubelbosque.com.co">gerencia@clubelbosque.com.co</a></div></li>
        <li><span class="quick-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12Z"/><circle cx="12" cy="10" r="2.5"/></svg></span><div><small style="color:var(--text-muted)">Dirección</small><br><strong>KM 37 Vía Silvania – Tibacuy</strong><br>Cundinamarca, Colombia</div></li>
      </ul>
    </div>
    <form class="form form-card reveal reveal-d1" data-demo="whatsapp" novalidate>
      <h3>Escríbenos</h3>
      <div class="field"><label for="f-asunto">¿Sobre qué quieres hablar?</label><select id="f-asunto" name="Asunto" required><option value="">Selecciona un tema</option><option>Planear una visita</option><option>Afiliación</option><option>Eventos y salones</option><option>Hospedaje</option><option>Clases y deportes</option><option>Otro</option></select></div>
      <div class="form-row"><div class="field"><label for="f-n">Nombre</label><input id="f-n" name="Nombre" autocomplete="name" required></div><div class="field"><label for="f-c">Celular</label><input id="f-c" name="Celular" type="tel" inputmode="tel" autocomplete="tel" required></div></div>
      <div class="field"><label for="f-e">Correo electrónico</label><input id="f-e" name="Correo" type="email" autocomplete="email" required></div>
      <div class="field"><label for="f-m">Mensaje</label><textarea id="f-m" name="Mensaje"></textarea></div>
      <label style="display:flex;gap:.6rem;font-size:.85rem;color:var(--text-muted)"><input type="checkbox" required style="width:20px;height:20px;flex:none"> Autorizo el tratamiento de mis datos personales conforme a la Ley 1581 de 2012.</label>
      <button class="btn btn--primary" type="submit">Enviar mensaje</button>
      <p class="form-success" tabindex="-1" role="status">¡Gracias! Te contactaremos lo antes posible.</p>
    </form>
  </div>
</section>
<section class="section--tight" id="llegar">
  <div class="container">
    <h2 class="reveal">Cómo llegar</h2>
    <p class="lead reveal">Desde la Autopista (vía Bogotá – Girardot), toma la carretera hacia Tibacuy en Silvania. El club está en el kilómetro 37.</p>
    <div class="reveal" style="margin-top:1.5rem"><iframe class="map-embed" title="Mapa de ubicación del club" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Club+Campestre+El+Bosque+Silvania+Cundinamarca&output=embed"></iframe></div>
    <div class="hero-actions" style="margin-top:1.25rem"><a class="btn btn--dark" href="https://maps.google.com/?q=Club+Campestre+El+Bosque+Silvania" target="_blank" rel="noopener">Abrir en Google Maps</a><a class="btn btn--ghost" href="https://waze.com/ul?q=Club%20Campestre%20El%20Bosque%20Silvania" target="_blank" rel="noopener">Abrir en Waze</a></div>
  </div>
</section>
"""
)
