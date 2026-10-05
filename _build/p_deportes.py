def gal(group, imgs, alt):
    out = ""
    for i, im in enumerate(imgs[:3]):
        out += f'<button data-lightbox="{group}" aria-label="Ampliar foto {i+1} de {alt}"><img src="@U/{im}" alt="{alt}" loading="lazy"></button>'
    # imágenes extra solo para el lightbox
    for im in imgs[3:]:
        out += f'<button data-lightbox="{group}" hidden><img src="@U/{im}" alt="{alt}" loading="lazy"></button>'
    return out

def sport(id_, cat, title, eyebrow, text, facts, imgs, alt, cta=("Reservar cancha", "asociados.html#reservas")):
    f = "".join(f'<div class="fact"><strong>{a}</strong><span>{b}</span></div>' for a, b in facts)
    return f'''
    <article class="sport-block" id="{id_}" data-cat="{cat}">
      <div class="sport-gallery reveal">{gal(id_, imgs, alt)}</div>
      <div class="reveal reveal-d1">
        <span class="eyebrow">{eyebrow}</span>
        <h2>{title}</h2>
        <p class="lead">{text}</p>
        <div class="facts">{f}</div>
        <div class="hero-actions"><a class="btn btn--dark" href="{cta[1]}">{cta[0]}</a><a class="link-arrow" href="contacto.html">Preguntar por clases</a></div>
      </div>
    </article>'''

SPORTS = [
  sport("golf","aire","Golf Cross","Campo de 9 hoyos",
        "Un hermoso campo de golf cross donde el reto de jugar inmerso en la naturaleza, con un clima espectacular, junto a ríos y lago, hace de cada recorrido una experiencia inigualable.",
        [("9","hoyos"),("Ríos","y lago en juego"),("Todo","el año")],
        ["2021/04/golf1-scaled.jpg","2020/03/f_golf-12-006.jpg","2020/03/f_golf-10-001.jpg","2020/03/WhatsApp-Image-2020-03-13-at-11.50.14-PM-2.jpg"],"Campo de golf cross", ("Reservar salida","asociados.html#reservas")),
  sport("tenis","raqueta","Tenis","Polvo de ladrillo",
        "17 canchas reglamentarias en polvo de ladrillo para jugar en un clima inmejorable, 5 de ellas con espléndida iluminación, y un estadio donde se disputan torneos nacionales e internacionales. Profesores especializados para niños y adultos.",
        [("17","canchas"),("5","iluminadas"),("300","espectadores")],
        ["2021/04/ropita_tenis.jpeg","2020/03/f_tenis_9-001.jpg","2020/03/f_tenis_6-001.jpg","2020/03/tenis_1.jpeg","2020/03/tenis_4.jpg"],"Canchas de tenis"),
  sport("natacion","agua","Natación y piscinas","Clima cálido",
        "Piscinas para disfrutar el clima templado de Silvania en familia: espacios para nadar, recrearse y descansar al aire libre.",
        [("Familia","zonas para todas las edades"),("Sol","clima templado")],
        ["2021/04/pis.jpg","2020/03/lago.jpeg","2020/03/f_lago.jpg"],"Piscina del club", ("Consultar horarios","contacto.html")),
  sport("hipica","aire","Hípica","Cabalgatas y escuela",
        "Cabalgatas para conocer las instalaciones en uno de nuestros nobles ejemplares. Asociados y visitantes practican este deporte con sus propios caballos o con los que alquila el club, y una escuela dirigida por un instructor experto complementa la formación.",
        [("Escuela","con instructor"),("Alquiler","de caballos"),("Pesebreras","para propietarios")],
        ["2021/04/equitacion.jpeg","2020/03/f_hipica-1-001.jpg","2020/03/hipica_3.jpg","2020/03/f_hipica-10-001.jpg","2020/03/f_hipica-9-001.jpg"],"Hípica en el club", ("Reservar cabalgata","contacto.html#visita")),
  sport("futbol","balon","Fútbol","Estadio reglamentario",
        "Un estadio de fútbol reglamentario con iluminación donde cada semana se reúnen asociados e invitados, además de dos campos de fútbol 8.",
        [("1","estadio iluminado"),("2","campos de fútbol 8")],
        ["2020/03/futbol-5-1.jpg","2020/03/f_futbol-2-001.jpg","2020/03/futbol-1-001.jpg","2020/03/futbol-2-001.jpg"],"Campo de fútbol"),
  sport("baloncesto","balon","Baloncesto y vóleibol","Canchas múltiples",
        "Canchas múltiples para baloncesto y vóleibol donde los practicantes se reúnen el fin de semana en una sana integración.",
        [("Multi","canchas"),("Fines","de semana activos")],
        ["2020/09/f_voleibol_1-1.jpg","2020/09/voleibol_1.jpg","2020/09/voleibol_2.jpg","2020/09/voleibol_3.jpg"],"Cancha de vóleibol"),
]

DEPORTES = dict(
slug="deportes",
title="Deportes · Golf, tenis, hípica, natación y más | Club Campestre El Bosque",
desc="Golf cross de 9 hoyos, 17 canchas de tenis en polvo de ladrillo, hípica, piscinas, fútbol, baloncesto y vóleibol en Silvania.",
og="2021/04/golf1-scaled.jpg",
body="""
<section class="page-hero">
  <img src="@U/2020/03/f_tenis_9-001.jpg" alt="">
  <div class="container">
    <nav class="breadcrumb" aria-label="Ruta"><a href="index.html">Inicio</a><span>/</span><span>Deportes</span></nav>
    <h1>Deporte al aire libre, todo el año</h1>
    <p class="lead">Amplios espacios para practicar deporte con tu familia en un clima privilegiado.</p>
  </div>
</section>

<section class="section--tight">
  <div class="container">
    <div class="filters reveal" role="group" aria-label="Filtrar deportes">
      <button class="chip" data-filter="all" aria-pressed="true">Todos</button>
      <button class="chip" data-filter="raqueta">Raqueta</button>
      <button class="chip" data-filter="balon">Con balón</button>
      <button class="chip" data-filter="aire">Naturaleza</button>
      <button class="chip" data-filter="agua">Agua</button>
    </div>
    <nav class="filters reveal" aria-label="Ir a un deporte" style="margin-top:-1rem">
      <a class="link-arrow" href="#golf">Golf</a><a class="link-arrow" href="#tenis">Tenis</a><a class="link-arrow" href="#natacion">Natación</a><a class="link-arrow" href="#hipica">Hípica</a><a class="link-arrow" href="#futbol">Fútbol</a><a class="link-arrow" href="#baloncesto">Baloncesto</a>
    </nav>
    """ + "".join(SPORTS) + """
  </div>
</section>

<section class="section--tight"><div class="container">
  <div class="cta-band reveal">
    <img src="@U/2020/03/f_golf-12-006.jpg" alt="" loading="lazy">
    <h2>Torneos y escuelas deportivas</h2>
    <p class="lead">Inscríbete a las clases de tenis, la escuela de equitación o los torneos internos del club.</p>
    <div class="hero-actions"><a class="btn btn--primary" href="contacto.html">Solicitar información</a><a class="btn btn--ghost" href="asociados.html#reservas">Reservar como asociado</a></div>
  </div>
</div></section>
"""
)
