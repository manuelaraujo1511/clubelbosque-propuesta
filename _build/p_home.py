HOME = dict(
slug="index",
title="Club Campestre El Bosque · Naturaleza, deporte y familia en Silvania",
desc="Club social, recreativo y deportivo en Silvania, Cundinamarca. Golf cross, 17 canchas de tenis, hípica, piscinas, salones para eventos y 52 fanegadas de naturaleza.",
body="""
<section class="hero" aria-label="Bienvenida">
  <div class="hero-media">
    <video autoplay muted loop playsinline preload="metadata" poster="@U/2020/03/f_entrada-compressor-1.jpg" aria-hidden="true">
      <source src="@U/2020/10/Club-Campestre-El-Bosque-medio.mp4" type="video/mp4">
    </video>
  </div>
  <div class="container hero-content">
    <span class="eyebrow" style="color:var(--gold-400)">Silvania · Cundinamarca</span>
    <h1>Donde la familia <em>se encuentra</em> con la naturaleza</h1>
    <p class="lead">52 fanegadas de bosque, ríos y lago alrededor de una casona colonial con más de cuatro siglos de historia. Deporte, descanso y celebraciones en un clima cautivante.</p>
    <div class="hero-actions">
      <a class="btn btn--primary" href="contacto.html#visita">Planear mi visita</a>
      <a class="btn btn--ghost" href="#explora">Explorar el club</a>
    </div>
    <div class="hero-meta" aria-label="El club en cifras">
      <div><strong>9</strong>hoyos de golf cross</div>
      <div><strong>17</strong>canchas de tenis</div>
      <div><strong>400</strong>invitados en la Casona</div>
      <div><strong>1608</strong>año de origen de la hacienda</div>
    </div>
  </div>
  <button class="icon-btn video-toggle" aria-label="Pausar video"></button>
</section>

<div class="quickbar">
  <div class="container">
    <div class="quickbar-inner reveal">
      <a class="quick-item" href="eventos.html#cotizar"><span class="quick-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18"/></svg></span><div><strong>Cotiza tu evento</strong><span>Bodas, 15 años, empresas</span></div></a>
      <a class="quick-item" href="deportes.html"><span class="quick-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M5.6 5.6c3.5 3.5 3.5 9.3 0 12.8M18.4 5.6c-3.5 3.5-3.5 9.3 0 12.8"/></svg></span><div><strong>Deportes</strong><span>Golf, tenis, hípica y más</span></div></a>
      <a class="quick-item" href="asociados.html#afiliacion"><span class="quick-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="8" r="4"/><path d="M2 21c0-4 3-6 7-6s7 2 7 6M19 8v6M16 11h6"/></svg></span><div><strong>Hazte asociado</strong><span>Beneficios y requisitos</span></div></a>
      <a class="quick-item" href="contacto.html#llegar"><span class="quick-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12Z"/><circle cx="12" cy="10" r="2.5"/></svg></span><div><strong>Cómo llegar</strong><span>KM 37 vía Silvania–Tibacuy</span></div></a>
    </div>
  </div>
</div>

<section class="section" id="para-ti" aria-labelledby="para-ti-h">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow">Un club para cada persona</span>
        <h2 id="para-ti-h">¿Cómo quieres vivir El Bosque?</h2>
        <p class="lead">Elige tu perfil y te mostramos lo que más te sirve, sin tener que buscarlo.</p>
      </div>
    </div>
    <div data-tabs>
      <div class="audience-tabs reveal" role="tablist" aria-label="Perfiles de visitante">
        <button role="tab" id="t-asoc" aria-controls="p-asoc" aria-selected="true">Soy asociado</button>
        <button role="tab" id="t-fam" aria-controls="p-fam" aria-selected="false" tabindex="-1">Quiero conocer el club</button>
        <button role="tab" id="t-emp" aria-controls="p-emp" aria-selected="false" tabindex="-1">Empresas</button>
        <button role="tab" id="t-col" aria-controls="p-col" aria-selected="false" tabindex="-1">Colegios</button>
        <button role="tab" id="t-cel" aria-controls="p-cel" aria-selected="false" tabindex="-1">Celebraciones</button>
      </div>

      <div class="audience-panel" role="tabpanel" id="p-asoc" aria-labelledby="t-asoc">
        <img src="@U/2021/04/ropita_tenis.jpeg" alt="Asociado jugando tenis en cancha de polvo de ladrillo" loading="lazy">
        <div>
          <h3>Tu club, desde el celular</h3>
          <p class="lead">Reserva canchas, consulta tu estado de cuenta y lleva tu carné digital para ingresar a los clubes en convenio.</p>
          <ul class="check-list">
            <li>Reserva de canchas de tenis y salones en segundos</li>
            <li>Carné digital con código QR</li>
            <li>Agenda de torneos y eventos del club</li>
            <li>Convenios con Serrezuela Country Club y Club Militar</li>
          </ul>
          <a class="btn btn--dark" href="asociados.html">Entrar al portal</a>
        </div>
      </div>

      <div class="audience-panel" role="tabpanel" id="p-fam" aria-labelledby="t-fam" hidden>
        <img src="@U/2020/03/lago.jpeg" alt="Lago del club rodeado de vegetación" loading="lazy">
        <div>
          <h3>Un día de campo para toda la familia</h3>
          <p class="lead">Piscinas, cabalgatas, senderos junto al río y gastronomía campestre, a pocos minutos de Bogotá.</p>
          <ul class="check-list">
            <li>Cabalgatas con caballos del club</li>
            <li>Senderos ecológicos, lago y avistamiento de aves</li>
            <li>Parrilla y cafeterías con vista campestre</li>
            <li>Cabañas y zona de camping</li>
          </ul>
          <a class="btn btn--dark" href="contacto.html#visita">Planear visita</a>
        </div>
      </div>

      <div class="audience-panel" role="tabpanel" id="p-emp" aria-labelledby="t-emp" hidden>
        <img src="@U/2020/03/eventos-17.jpg" alt="Evento corporativo en las instalaciones del club" loading="lazy">
        <div>
          <h3>Eventos corporativos con aire libre</h3>
          <p class="lead">Convenciones, integraciones y jornadas de bienestar con espacios para 40 a 400 personas.</p>
          <ul class="check-list">
            <li>Salón Múltiple para 230 personas con ayudas audiovisuales</li>
            <li>Canchas y campos para actividades de integración</li>
            <li>Alimentación y hospedaje en el mismo lugar</li>
          </ul>
          <a class="btn btn--dark" href="eventos.html#cotizar">Cotizar evento</a>
        </div>
      </div>

      <div class="audience-panel" role="tabpanel" id="p-col" aria-labelledby="t-col" hidden>
        <img src="@U/2020/03/IMG_20190628_131745499.jpg" alt="Estudiantes en salida pedagógica en el club" loading="lazy">
        <div>
          <h3>Salidas pedagógicas que se recuerdan</h3>
          <p class="lead">Espacios de formación que favorecen el desarrollo integral de la comunidad educativa: historia, naturaleza y deporte.</p>
          <ul class="check-list">
            <li>Recorrido por la Casona colonial de la Hacienda El Chocho</li>
            <li>Educación ambiental en senderos y lago</li>
            <li>Jornadas deportivas y recreativas</li>
          </ul>
          <a class="btn btn--dark" href="eventos.html#colegios">Programar salida</a>
        </div>
      </div>

      <div class="audience-panel" role="tabpanel" id="p-cel" aria-labelledby="t-cel" hidden>
        <img src="@U/2020/03/capilla_3-scaled.jpg" alt="Capilla del club decorada para ceremonia" loading="lazy">
        <div>
          <h3>Bodas, 15 años y celebraciones</h3>
          <p class="lead">Una capilla rodeada de naturaleza y una casona colonial para hacer de tu ceremonia un día inolvidable.</p>
          <ul class="check-list">
            <li>Capilla para ceremonias religiosas</li>
            <li>Casona con capacidad hasta 400 personas</li>
            <li>Escenarios naturales para fotografía</li>
          </ul>
          <a class="btn btn--dark" href="eventos.html">Ver salones</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt" id="explora" aria-labelledby="explora-h">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow">Experiencias</span>
        <h2 id="explora-h">Todo lo que puedes hacer en el club</h2>
      </div>
      <a class="link-arrow" href="deportes.html">Ver todos los deportes</a>
    </div>
    <div class="bento">
      <a class="bento-item b-span-3 b-row-2 b-feature reveal" href="deportes.html#golf">
        <img src="@U/2021/04/golf1-scaled.jpg" alt="Campo de golf cross del club" loading="lazy">
        <span class="pill">9 hoyos</span>
        <div class="bento-caption"><h3>Golf Cross</h3><p>Un reto entre ríos, lago y naturaleza, con un clima espectacular.</p></div>
      </a>
      <a class="bento-item b-span-3 reveal reveal-d1" href="deportes.html#tenis">
        <img src="@U/2020/03/f_tenis_9-001.jpg" alt="Canchas de tenis en polvo de ladrillo" loading="lazy">
        <span class="pill">17 canchas</span>
        <div class="bento-caption"><h3>Tenis</h3><p>Polvo de ladrillo, iluminación y estadio para 300 personas.</p></div>
      </a>
      <a class="bento-item b-span-2 reveal reveal-d1" href="deportes.html#hipica">
        <img src="@U/2021/04/equitacion.jpeg" alt="Jinete montando a caballo" loading="lazy">
        <div class="bento-caption"><h3>Hípica</h3><p>Cabalgatas y escuela</p></div>
      </a>
      <a class="bento-item b-span-1 reveal reveal-d2" href="deportes.html#natacion">
        <img src="@U/2021/04/pis.jpg" alt="Piscina del club" loading="lazy">
        <div class="bento-caption"><h3>Piscinas</h3></div>
      </a>
      <a class="bento-item b-span-2 reveal" href="eventos.html">
        <img src="@U/2020/10/casona-5.jpg" alt="Patio de la Casona colonial" loading="lazy">
        <span class="pill">Hasta 400 personas</span>
        <div class="bento-caption"><h3>Salones y eventos</h3><p>Capilla, Casona y salones</p></div>
      </a>
      <a class="bento-item b-span-2 reveal reveal-d1" href="gastronomia.html">
        <img src="@U/2020/04/restaurante-1.jpeg" alt="Restaurante del club" loading="lazy">
        <div class="bento-caption"><h3>Gastronomía</h3><p>Parrilla y cafeterías</p></div>
      </a>
      <a class="bento-item b-span-2 reveal reveal-d2" href="hospedaje.html">
        <img src="@U/2020/03/sendero.jpeg" alt="Sendero entre árboles" loading="lazy">
        <div class="bento-caption"><h3>Hospedaje y bienestar</h3><p>Cabañas, camping, sauna y turco</p></div>
      </a>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="historia-h">
  <div class="container split">
    <div class="split-media reveal">
      <img src="@U/2020/03/casona_1-1.jpeg" alt="Casona colonial de la antigua Hacienda El Chocho" loading="lazy">
      <div class="floating"><strong>1608</strong>Origen de las estancias que darían vida a la Hacienda El Chocho</div>
    </div>
    <div class="reveal reveal-d1">
      <span class="eyebrow">Nuestra historia</span>
      <h2 id="historia-h">Una casona colonial en el corazón del club</h2>
      <p class="lead">El epicentro social del club es la histórica Casa del Chocho, un palacete tropical de rasgos hispano-arábigos conservado en su integridad arquitectónica: patios empedrados, aljibes, corredores de columnas de madera y jardines bajo samanes y ceibas.</p>
      <p>Su parcelación dio origen a Silvania en 1935 y hoy, bordeado por el río Chocho, el club ocupa 52 fanegadas unidas por senderos y modernas instalaciones.</p>
      <a class="btn btn--dark" href="club.html#historia">Conoce la historia completa</a>
    </div>
  </div>
</section>

<section class="section section--dark" aria-labelledby="cifras-h">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow">El Bosque en cifras</span>
        <h2 id="cifras-h">Espacio de sobra para lo que te mueve</h2>
      </div>
    </div>
    <div class="stats">
      <div class="stat reveal"><strong data-count="52">52</strong><span>fanegadas de naturaleza junto al río Chocho</span></div>
      <div class="stat reveal reveal-d1"><strong data-count="17">17</strong><span>canchas de tenis, 5 con iluminación</span></div>
      <div class="stat reveal reveal-d2"><strong data-count="300">300</strong><span>espectadores en el estadio de tenis</span></div>
      <div class="stat reveal reveal-d3"><strong data-count="4">4</strong><span>restaurantes y cafeterías</span></div>
    </div>
  </div>
</section>

<section class="section" id="eventos" aria-labelledby="eventos-h">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow">Vida en comunidad</span>
        <h2 id="eventos-h">Momentos de la gran familia El Bosque</h2>
      </div>
      <a class="link-arrow" href="eventos.html#comunidad">Ver todos los eventos</a>
    </div>
    <div class="grid grid-3">
      <a class="card reveal" href="eventos.html#social"><div class="card-media"><img src="@U/2020/03/15_a%C3%B1os-37-780x675.jpeg" alt="Celebración de 15 años" loading="lazy"><span class="tag">Social</span></div><div class="card-body"><h3>Eventos sociales</h3><p>Día de la Madre, 15 años y celebraciones que hacen tus sueños realidad.</p><span class="link-arrow">Ver galería</span></div></a>
      <a class="card reveal reveal-d1" href="eventos.html#deportivo"><div class="card-media"><img src="@U/2020/03/futbol-1.jpg" alt="Torneo de fútbol en el club" loading="lazy"><span class="tag">Deportivo</span></div><div class="card-body"><h3>Torneos deportivos</h3><p>Competencias que incentivan el sano desarrollo físico y emocional.</p><span class="link-arrow">Ver galería</span></div></a>
      <a class="card reveal reveal-d2" href="eventos.html#familia"><div class="card-media"><img src="@U/2020/03/famila_bosque-1.jpg" alt="Encuentro Familia El Bosque" loading="lazy"><span class="tag">Familia</span></div><div class="card-body"><h3>Familia El Bosque</h3><p>Un encuentro para reunir a nuestras familias y asociados y conocernos.</p><span class="link-arrow">Ver galería</span></div></a>
    </div>
  </div>
</section>

<section class="section--tight" aria-label="Convenios">
  <div class="container">
    <div class="cta-band reveal">
      <img src="@U/2020/03/f_lago.jpg" alt="" loading="lazy">
      <span class="eyebrow" style="color:var(--gold-400)">Beneficio para asociados</span>
      <h2>Tu carné abre más puertas</h2>
      <p class="lead">Con el carné del club ingresa al Serrezuela Country Club y, sin costo, a las sedes del Club Militar en Bogotá, Melgar, Boyacá y Santa Marta.</p>
      <div class="hero-actions"><a class="btn btn--primary" href="convenios.html">Ver convenios</a><a class="btn btn--ghost" href="asociados.html#afiliacion">Quiero afiliarme</a></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="faq-h">
  <div class="container split" style="align-items:start">
    <div class="reveal">
      <span class="eyebrow">Preguntas frecuentes</span>
      <h2 id="faq-h">Resolvemos tus dudas antes de venir</h2>
      <p class="lead">¿No encuentras lo que buscas? Escríbenos por WhatsApp y te respondemos.</p>
      <a class="btn btn--dark" href="contacto.html">Contactar al club</a>
    </div>
    <div class="faq reveal reveal-d1">
      <details><summary>¿Dónde queda el club?</summary><p>En el kilómetro 37 de la vía Silvania – Tibacuy, Cundinamarca, bordeado por el río Chocho (Fusagasugá).</p></details>
      <details><summary>¿Puedo visitar el club sin ser asociado?</summary><p>Sí. Puedes venir como invitado de un asociado o para un evento, una salida pedagógica o actividades como las cabalgatas. Contáctanos para conocer las condiciones vigentes.</p></details>
      <details><summary>¿Cómo me afilio y cuánto cuesta?</summary><p>En la sección Asociados encontrarás los pasos de afiliación y un formulario para que el equipo comercial te comparta las tarifas actualizadas.</p></details>
      <details><summary>¿Qué capacidad tienen los salones?</summary><p>Casona hasta 400 personas, Salón Múltiple 230 (tipo auditorio), Salón Verde 40, además de la Capilla para ceremonias.</p></details>
      <details><summary>¿En qué horario atienden reservas?</summary><p>Las líneas de atención al cliente reciben reservas de domingo a domingo.</p></details>
    </div>
  </div>
</section>
"""
)
