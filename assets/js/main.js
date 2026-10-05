/* Club Campestre El Bosque — interacciones del sitio */
(function () {
  "use strict";

  // Ruta base de las imágenes del sitio original (el script descargar-medios las vuelve locales)
  var U = "https://clubelbosque.com.co/wp-content/uploads/";
  var WA = "573164341805";
  var WA_MSG = encodeURIComponent("Hola, quisiera información sobre el Club Campestre El Bosque");

  // Autor de la propuesta (quitar junto con el distintivo al pasar a producción)
  var AUTHOR = "Manuel Araujo";
  var AUTHOR_EMAIL = "manuel.araujo1511@gmail.com";
  var AUTHOR_WA = "+573137130787";
  var AUTHOR_WA_MSG = encodeURIComponent("Hola Manuel, vi la propuesta del nuevo sitio del Club Campestre El Bosque");

  var ICON = {
    chevron: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>',
    menu: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    close: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>',
    user: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg>',
    wa: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.5 3.5A11.8 11.8 0 0 0 1.9 17.7L.5 23.5l6-1.6A11.8 11.8 0 0 0 20.5 3.5ZM12 21.3c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.6.9.9-3.5-.2-.4A9.8 9.8 0 1 1 12 21.3Zm5.4-7.3c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1-.8 1-.9 1.2-.3.2-.6.1a8 8 0 0 1-4-3.5c-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6a1.1 1.1 0 0 0-.8.4 3.4 3.4 0 0 0-1 2.5 5.9 5.9 0 0 0 1.2 3.1 13.4 13.4 0 0 0 5.2 4.6c1.9.8 2.7.9 3.6.7a3.1 3.1 0 0 0 2-1.4 2.5 2.5 0 0 0 .2-1.4c-.1-.2-.3-.3-.6-.4Z"/></svg>',
    fb: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v9h4v-9h3l.5-4h-3.5V8.8c0-.5.3-.8.5-.8Z"/></svg>',
    phone: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg>',
    pin: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12Z"/><circle cx="12" cy="10" r="2.5"/></svg>',
    cal: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18"/></svg>',
    a11y: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="4.5" r="1.8"/><path d="M5 8.5l7 1.5 7-1.5M12 10v5m0 0-3 6m3-6 3 6"/></svg>',
    prev: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg>',
    next: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg>'
  };

  var NAV = [
    { label: "El Club", items: [
      { href: "club.html#historia", t: "Historia", d: "De la Hacienda El Chocho (1608) al club de hoy", img: "2020/03/casona_1-1.jpeg" },
      { href: "club.html#proposito", t: "Misión, visión y promesa", d: "Lo que nos mueve como comunidad", img: "2020/03/f_fuente-compressor.jpg" },
      { href: "club.html#gobierno", t: "Junta Directiva y de Vigilancia", d: "Quiénes dirigen el club", img: "2020/03/f_administracion_2-1.jpg" },
      { href: "sostenibilidad.html", t: "Sostenibilidad", d: "52 fanegadas de naturaleza, lago y senderos", img: "2020/03/lago_garza.jpg" }
    ]},
    { label: "Deportes", items: [
      { href: "deportes.html#golf", t: "Golf Cross", d: "Campo de 9 hoyos entre ríos y lago", img: "2021/04/golf1-scaled.jpg" },
      { href: "deportes.html#tenis", t: "Tenis", d: "17 canchas en polvo de ladrillo", img: "2020/03/tenis_1.jpeg" },
      { href: "deportes.html#natacion", t: "Natación", d: "Piscinas en clima cálido", img: "2021/04/pis.jpg" },
      { href: "deportes.html#hipica", t: "Hípica", d: "Cabalgatas y escuela de equitación", img: "2021/04/equitacion.jpeg" },
      { href: "deportes.html#futbol", t: "Fútbol", d: "Estadio iluminado + 2 campos de fútbol 8", img: "2020/03/futbol-5-1.jpg" },
      { href: "deportes.html#baloncesto", t: "Baloncesto y vóleibol", d: "Canchas múltiples", img: "2020/09/voleibol_1.jpg" }
    ]},
    { label: "Experiencias", items: [
      { href: "eventos.html", t: "Salones y eventos", d: "Capilla, Casona, Salón Múltiple y Verde", img: "2020/10/casona-5.jpg" },
      { href: "gastronomia.html", t: "Gastronomía", d: "Parrilla y tres cafeterías", img: "2020/04/restaurante-1.jpeg" },
      { href: "hospedaje.html", t: "Hospedaje y bienestar", d: "Cabañas, camping, sauna y turco", img: "2020/03/sendero.jpeg" },
      { href: "eventos.html#comunidad", t: "Eventos y comunidad", d: "Sociales, corporativos, deportivos y pedagógicos", img: "2020/03/eventos-2.jpeg" }
    ]}
  ];

  var page = document.body.getAttribute("data-page") || "";
  var lightHeader = document.body.hasAttribute("data-light-header");

  function megaHTML(group) {
    return group.items.map(function (i) {
      return '<a href="' + i.href + '"><img src="' + U + i.img + '" alt="" loading="lazy"><div><strong>' + i.t + "</strong><span>" + i.d + "</span></div></a>";
    }).join("");
  }

  var header = document.createElement("header");
  header.className = "site-header" + (lightHeader ? " is-light" : "");
  header.innerHTML =
    '<div class="container header-inner">' +
      '<a class="brand" href="index.html" aria-label="Club Campestre El Bosque, inicio"><img src="' + U + '2020/03/logo.png" alt="" width="50" height="50"><span class="brand-text">El Bosque<small>Club Campestre · Golf Cross</small></span></a>' +
      '<nav class="main-nav" aria-label="Principal"><ul>' +
        NAV.map(function (g, idx) {
          return '<li class="has-mega"><button class="nav-trigger" aria-haspopup="true" aria-expanded="false">' + g.label + ICON.chevron + '</button><div class="mega" role="menu">' + megaHTML(g) + "</div></li>";
        }).join("") +
        '<li><a href="convenios.html"' + (page === "convenios" ? ' aria-current="page"' : "") + '>Convenios</a></li>' +
        '<li><a href="contacto.html"' + (page === "contacto" ? ' aria-current="page"' : "") + '>Contacto</a></li>' +
      "</ul></nav>" +
      '<div class="header-actions">' +
        '<a class="btn btn--ghost btn--sm" href="asociados.html">' + ICON.user + "Asociados</a>" +
        '<a class="btn btn--primary btn--sm" href="contacto.html#visita">Planear visita</a>' +
        '<button class="icon-btn menu-toggle" aria-label="Abrir menú" aria-expanded="false" aria-controls="mobile-nav">' + ICON.menu + "</button>" +
      "</div>" +
    "</div>";
  document.body.prepend(header);

  var skip = document.createElement("a");
  skip.className = "skip-link"; skip.href = "#main"; skip.textContent = "Saltar al contenido";
  document.body.prepend(skip);

  // Menú móvil
  var mobile = document.createElement("div");
  mobile.className = "mobile-nav"; mobile.id = "mobile-nav"; mobile.setAttribute("aria-hidden", "true");
  mobile.innerHTML =
    '<div class="mobile-nav-top"><a class="brand" href="index.html"><img src="' + U + '2020/03/logo.png" alt="Club Campestre El Bosque" style="height:44px"></a><button class="icon-btn" style="color:#fff" aria-label="Cerrar menú" data-close-menu>' + ICON.close + "</button></div>" +
    "<nav aria-label='Móvil'>" +
      '<a href="index.html">Inicio</a>' +
      NAV.map(function (g) {
        return "<details><summary>" + g.label + "</summary><div>" + g.items.map(function (i) { return '<a href="' + i.href + '">' + i.t + "</a>"; }).join("") + "</div></details>";
      }).join("") +
      '<a href="convenios.html">Convenios</a><a href="contacto.html">Contacto</a>' +
    "</nav>" +
    '<div class="mobile-cta"><a class="btn btn--primary" href="contacto.html#visita">Planear visita</a><a class="btn btn--ghost" href="asociados.html">' + ICON.user + "Portal del asociado</a></div>";
  document.body.appendChild(mobile);

  var toggle = header.querySelector(".menu-toggle");
  function setMenu(open) {
    mobile.classList.toggle("is-open", open);
    mobile.setAttribute("aria-hidden", String(!open));
    toggle.setAttribute("aria-expanded", String(open));
    document.body.style.overflow = open ? "hidden" : "";
  }
  toggle.addEventListener("click", function () { setMenu(true); });
  mobile.querySelector("[data-close-menu]").addEventListener("click", function () { setMenu(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });

  header.querySelectorAll(".has-mega").forEach(function (li) {
    var b = li.querySelector(".nav-trigger");
    li.addEventListener("mouseenter", function () { b.setAttribute("aria-expanded", "true"); });
    li.addEventListener("mouseleave", function () { b.setAttribute("aria-expanded", "false"); });
    b.addEventListener("click", function () { b.setAttribute("aria-expanded", b.getAttribute("aria-expanded") === "true" ? "false" : "true"); });
  });

  // Header sólido al hacer scroll
  function onScroll() { header.classList.toggle("is-solid", window.scrollY > 40); }
  onScroll(); window.addEventListener("scroll", onScroll, { passive: true });

  // Footer
  var footer = document.createElement("footer");
  footer.className = "site-footer";
  footer.innerHTML =
    '<div class="container"><div class="footer-top">' +
      '<div class="footer-brand"><a class="brand" href="index.html"><img src="' + U + '2020/03/logo.png" alt="" style="height:56px"><span class="brand-text" style="color:#fff">Club Campestre<br>El Bosque</span></a>' +
        "<p>A pocos minutos de Bogotá, en un clima cautivante e inmerso en naturaleza. Un club social, recreativo y deportivo para toda la familia.</p>" +
        '<div class="socials"><a href="https://www.facebook.com/Club-Campestre-El-Bosque-522481094486643/" target="_blank" rel="noopener" aria-label="Facebook">' + ICON.fb + '</a><a href="https://wa.me/' + WA + "?text=" + WA_MSG + '" target="_blank" rel="noopener" aria-label="WhatsApp">' + ICON.wa + "</a></div></div>" +
      "<div><h4>Explora</h4><ul><li><a href='club.html'>El Club</a></li><li><a href='deportes.html'>Deportes</a></li><li><a href='eventos.html'>Salones y eventos</a></li><li><a href='gastronomia.html'>Gastronomía</a></li><li><a href='hospedaje.html'>Hospedaje y bienestar</a></li><li><a href='sostenibilidad.html'>Sostenibilidad</a></li></ul></div>" +
      "<div><h4>Para ti</h4><ul><li><a href='asociados.html'>Portal del asociado</a></li><li><a href='asociados.html#afiliacion'>Cómo afiliarse</a></li><li><a href='eventos.html#cotizar'>Empresas</a></li><li><a href='eventos.html#colegios'>Colegios</a></li><li><a href='convenios.html'>Convenios</a></li></ul></div>" +
      "<div><h4>Visítanos</h4><ul class='contact-list'>" +
        "<li>KM 37 Vía Silvania – Tibacuy<br>Cundinamarca, Colombia</li>" +
        "<li><a href='tel:+576018987081'>(601) 898 7081</a></li>" +
        "<li><a href='https://wa.me/" + WA + "'>+57 316 434 1805</a></li>" +
        "<li><a href='mailto:gerencia@clubelbosque.com.co'>gerencia@clubelbosque.com.co</a></li>" +
        "<li>Atención de domingo a domingo</li>" +
      "</ul></div>" +
    "</div>" +
    '<div class="footer-bottom"><span>© ' + new Date().getFullYear() + ' Club Campestre El Bosque · Entidad privada sin ánimo de lucro</span><span><a href="propuesta.html">Propuesta de rediseño</a> · <a href="contacto.html">Política de datos</a></span></div>' +
    '<p class="proposal-credit">Prototipo no oficial elaborado por <strong>' + AUTHOR + '</strong> como propuesta para el Club Campestre El Bosque · <a href="mailto:' + AUTHOR_EMAIL + '">' + AUTHOR_EMAIL + '</a></p></div>';
  document.body.appendChild(footer);

  // Flotantes: WhatsApp, accesibilidad, barra móvil
  var fab = document.createElement("a");
  fab.className = "fab-whatsapp"; fab.href = "https://wa.me/" + WA + "?text=" + WA_MSG; fab.target = "_blank"; fab.rel = "noopener";
  fab.setAttribute("aria-label", "Escríbenos por WhatsApp"); fab.innerHTML = ICON.wa;
  document.body.appendChild(fab);

  var a11y = document.createElement("div");
  a11y.className = "a11y-panel";
  a11y.innerHTML = '<button aria-label="Opciones de accesibilidad" aria-expanded="false">' + ICON.a11y + "</button>" +
    '<div class="a11y-menu" role="group" aria-label="Accesibilidad"><strong>Accesibilidad</strong>' +
    '<button data-a11y="fs-lg" aria-pressed="false">Texto grande (A+)</button>' +
    '<button data-a11y="fs-xl" aria-pressed="false">Texto muy grande (A++)</button>' +
    '<button data-a11y="hc" aria-pressed="false">Alto contraste</button>' +
    '<button data-a11y="reset">Restablecer</button></div>';
  document.body.appendChild(a11y);
  var a11yBtn = a11y.querySelector("button"), a11yMenu = a11y.querySelector(".a11y-menu");
  a11yBtn.addEventListener("click", function () {
    var o = !a11yMenu.classList.contains("is-open");
    a11yMenu.classList.toggle("is-open", o); a11yBtn.setAttribute("aria-expanded", String(o));
  });
  function store(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function read(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  var root = document.documentElement;
  function applyA11y(state) {
    root.classList.remove("fs-lg", "fs-xl", "hc");
    state.forEach(function (c) { root.classList.add(c); });
    a11yMenu.querySelectorAll("[data-a11y]").forEach(function (b) {
      b.setAttribute("aria-pressed", String(state.indexOf(b.dataset.a11y) > -1));
    });
  }
  var a11yState = (read("bosque-a11y") || "").split(",").filter(Boolean);
  applyA11y(a11yState);
  a11yMenu.addEventListener("click", function (e) {
    var b = e.target.closest("[data-a11y]"); if (!b) return;
    var k = b.dataset.a11y;
    if (k === "reset") a11yState = [];
    else if (a11yState.indexOf(k) > -1) a11yState = a11yState.filter(function (x) { return x !== k; });
    else {
      if (k.indexOf("fs-") === 0) a11yState = a11yState.filter(function (x) { return x.indexOf("fs-") !== 0; });
      a11yState.push(k);
    }
    applyA11y(a11yState); store("bosque-a11y", a11yState.join(","));
  });

  var bar = document.createElement("nav");
  bar.className = "mobile-bar"; bar.setAttribute("aria-label", "Acciones rápidas");
  bar.innerHTML = '<a href="tel:+576018987081">' + ICON.phone + 'Llamar</a><a href="contacto.html#visita">' + ICON.cal + 'Reservar</a><a href="https://maps.google.com/?q=Club+Campestre+El+Bosque+Silvania" target="_blank" rel="noopener">' + ICON.pin + "Cómo llegar</a>";
  document.body.appendChild(bar);

  // Distintivo de propuesta (quitar al pasar a producción)
  if (page !== "propuesta") {
    var badge = document.createElement("a");
    badge.className = "proposal-badge"; badge.href = "propuesta.html";
    badge.innerHTML = "<strong>Propuesta de rediseño</strong><span>por " + AUTHOR + " · Ver detalles →</span>";
    document.body.appendChild(badge);
  }
  var authorBox = document.querySelector("[data-author-contact]");
  if (authorBox) {
    authorBox.innerHTML =
      '<a class="btn btn--primary" href="https://wa.me/' + AUTHOR_WA + "?text=" + AUTHOR_WA_MSG + '" target="_blank" rel="noopener">' + ICON.wa + " Escribir por WhatsApp</a>" +
      '<a class="btn btn--ghost" href="mailto:' + AUTHOR_EMAIL + "?subject=" + encodeURIComponent("Propuesta sitio web Club El Bosque") + '">' + AUTHOR_EMAIL + "</a>";
  }

  // Fallback de imágenes
  document.querySelectorAll("img").forEach(function (img) {
    img.addEventListener("error", function () { img.classList.add("img-fallback"); img.removeAttribute("srcset"); img.style.minHeight = "120px"; }, { once: true });
  });

  // Animaciones al aparecer
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-visible"); io.unobserve(en.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    document.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("is-visible"); });
  }

  // Contadores
  document.querySelectorAll("[data-count]").forEach(function (el) {
    var target = parseFloat(el.dataset.count), suffix = el.dataset.suffix || "", done = false;
    var run = function () {
      if (done) return; done = true;
      var start = performance.now(), dur = 1400;
      (function tick(now) {
        var p = Math.min((now - start) / dur, 1), v = Math.round(target * (1 - Math.pow(1 - p, 3)));
        el.textContent = v.toLocaleString("es-CO") + suffix;
        if (p < 1) requestAnimationFrame(tick);
      })(start);
    };
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (en, obs) { if (en[0].isIntersecting) { run(); obs.disconnect(); } }).observe(el);
    } else run();
  });

  // Video del hero: pausa/reproducción
  var vid = document.querySelector(".hero video");
  var vt = document.querySelector(".video-toggle");
  if (vid && vt) {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) { vid.pause(); vid.removeAttribute("autoplay"); }
    var syncVt = function () {
      vt.setAttribute("aria-label", vid.paused ? "Reproducir video" : "Pausar video");
      vt.innerHTML = vid.paused
        ? '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
        : '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7 5h4v14H7zM13 5h4v14h-4z"/></svg>';
    };
    vt.addEventListener("click", function () { vid.paused ? vid.play() : vid.pause(); });
    vid.addEventListener("play", syncVt); vid.addEventListener("pause", syncVt); syncVt();
  }

  // Pestañas genéricas (audiencias, portal)
  document.querySelectorAll("[data-tabs]").forEach(function (wrap) {
    var tabs = wrap.querySelectorAll('[role="tab"]');
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        tabs.forEach(function (t) {
          var sel = t === tab;
          t.setAttribute("aria-selected", String(sel));
          t.tabIndex = sel ? 0 : -1;
          var p = document.getElementById(t.getAttribute("aria-controls"));
          if (p) p.hidden = !sel;
        });
      });
      tab.addEventListener("keydown", function (e) {
        var list = Array.prototype.slice.call(tabs), i = list.indexOf(tab);
        if (e.key === "ArrowRight" || e.key === "ArrowDown") { e.preventDefault(); list[(i + 1) % list.length].focus(); list[(i + 1) % list.length].click(); }
        if (e.key === "ArrowLeft" || e.key === "ArrowUp") { e.preventDefault(); list[(i - 1 + list.length) % list.length].focus(); list[(i - 1 + list.length) % list.length].click(); }
      });
    });
  });

  // Filtro de deportes
  var chips = document.querySelectorAll("[data-filter]");
  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      var f = chip.dataset.filter;
      chips.forEach(function (c) { c.setAttribute("aria-pressed", String(c === chip)); });
      document.querySelectorAll("[data-cat]").forEach(function (el) {
        el.hidden = !(f === "all" || el.dataset.cat.split(" ").indexOf(f) > -1);
      });
    });
  });

  // Miniaturas de salones
  document.querySelectorAll(".venue").forEach(function (v) {
    var main = v.querySelector(".venue-media > img");
    v.querySelectorAll(".venue-thumbs button").forEach(function (b) {
      b.addEventListener("click", function () { main.src = b.querySelector("img").src; });
    });
  });

  // Lightbox
  var groups = {};
  document.querySelectorAll("[data-lightbox]").forEach(function (el) {
    var g = el.dataset.lightbox; (groups[g] = groups[g] || []).push(el);
  });
  if (Object.keys(groups).length) {
    var lb = document.createElement("div");
    lb.className = "lightbox"; lb.setAttribute("role", "dialog"); lb.setAttribute("aria-modal", "true"); lb.setAttribute("aria-label", "Galería de imágenes");
    lb.innerHTML = '<img alt=""><button class="icon-btn lb-close" aria-label="Cerrar">' + ICON.close + '</button><button class="icon-btn lb-prev" aria-label="Anterior">' + ICON.prev + '</button><button class="icon-btn lb-next" aria-label="Siguiente">' + ICON.next + '</button><div class="lb-count" aria-live="polite"></div>';
    document.body.appendChild(lb);
    var lbImg = lb.querySelector("img"), cur = [], idx = 0, lastFocus = null;
    var show = function () {
      var el = cur[idx], im = el.querySelector("img");
      lbImg.src = el.dataset.full || (im && im.src); lbImg.alt = (im && im.alt) || "";
      lb.querySelector(".lb-count").textContent = (idx + 1) + " / " + cur.length;
    };
    var open = function (g, i) { cur = groups[g]; idx = i; show(); lb.classList.add("is-open"); lastFocus = document.activeElement; lb.querySelector(".lb-close").focus(); document.body.style.overflow = "hidden"; };
    var close = function () { lb.classList.remove("is-open"); document.body.style.overflow = ""; if (lastFocus) lastFocus.focus(); };
    Object.keys(groups).forEach(function (g) {
      groups[g].forEach(function (el, i) { el.addEventListener("click", function (e) { e.preventDefault(); open(g, i); }); });
    });
    lb.querySelector(".lb-close").addEventListener("click", close);
    lb.querySelector(".lb-prev").addEventListener("click", function () { idx = (idx - 1 + cur.length) % cur.length; show(); });
    lb.querySelector(".lb-next").addEventListener("click", function () { idx = (idx + 1) % cur.length; show(); });
    lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
    document.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("is-open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowRight") lb.querySelector(".lb-next").click();
      if (e.key === "ArrowLeft") lb.querySelector(".lb-prev").click();
    });
  }

  // Formularios (prototipo: valida y muestra confirmación; puede conectarse a WhatsApp/CRM)
  document.querySelectorAll("form[data-demo]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var ok = form.querySelector(".form-success");
      if (ok) { ok.classList.add("is-visible"); ok.focus(); }
      if (form.dataset.demo === "whatsapp") {
        var data = new FormData(form), lines = [];
        data.forEach(function (v, k) { if (v) lines.push(k + ": " + v); });
        window.open("https://wa.me/" + WA + "?text=" + encodeURIComponent("Solicitud desde la web\n" + lines.join("\n")), "_blank", "noopener");
      }
      form.reset();
    });
  });

  // Portal: selección de horarios
  document.querySelectorAll(".slots").forEach(function (s) {
    s.addEventListener("click", function (e) {
      var b = e.target.closest(".slot"); if (!b || b.disabled) return;
      s.querySelectorAll(".slot").forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
      var out = document.getElementById(s.dataset.output);
      if (out) out.textContent = "Horario seleccionado: " + b.textContent;
    });
  });

  // Año dinámico
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
