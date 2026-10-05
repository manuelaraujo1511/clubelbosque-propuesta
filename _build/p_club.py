def person(name, role):
    ini = "".join(w[0] for w in name.split()[:2]).upper()
    return f'<div class="person"><span class="avatar" aria-hidden="true">{ini}</span><div><strong>{name}</strong><span>{role}</span></div></div>'

directiva = [("César Muñoz Torres","Presidente"),("Julio Manrique Rodríguez","Vicepresidente"),("Graciela Suárez Cortés","Secretaria"),("Natalia Umaña Flechas","Vocal"),("Germán Muelle Jaime","Vocal"),("Fabián Escallón Mayorga","Vocal"),("Eusebio Vanegas Vergara","Vocal")]
vigilancia = [("Guillermo Trujillo Cedeño","Coordinador"),("Daniel Silva Castro","Secretario"),("Diana Trujillo Gómez","Vocal"),("Carlos Alfredo Neira","Vocal"),("Ancízar Bocanegra Andrade","Vocal")]

CLUB = dict(
slug="club",
title="El Club · Historia, propósito y gobierno | Club Campestre El Bosque",
desc="De las estancias de 1608 a la Hacienda El Chocho y el Club Campestre El Bosque: historia, misión, visión, promesa de valor y juntas.",
og="2020/03/casona_1-1.jpeg",
body="""
<section class="page-hero">
  <img src="@U/2020/03/casona_1-1.jpeg" alt="">
  <div class="container">
    <nav class="breadcrumb" aria-label="Ruta"><a href="index.html">Inicio</a><span>/</span><span>El Club</span></nav>
    <h1>Cuatro siglos de historia, una sola familia</h1>
    <p class="lead">A pocos minutos de Bogotá, en un clima cautivante e inmerso en su exuberante naturaleza, se encuentra un lugar para vivir experiencias inolvidables con un equipo humano dispuesto a hacer de cada visita algo especial.</p>
  </div>
</section>

<section class="section" id="historia" aria-labelledby="hist-h">
  <div class="container">
    <div class="center reveal" style="margin-bottom:3.5rem">
      <span class="eyebrow">Nuestra historia colonial</span>
      <h2 id="hist-h">De la Hacienda El Chocho al Club El Bosque</h2>
      <p class="lead">Una línea de tiempo para recorrer, en pocos minutos, la historia que se conserva en cada muro de la Casona.</p>
    </div>
    <div class="timeline">
      <div class="t-item reveal"><div class="t-year">1608</div><div class="t-body"><h3>Estancias de ganado</h3><p>Las estancias de Francisco Gómez de la Cruz se convertirían, tres siglos después, en la Hacienda El Chocho: 23.850 fanegadas entre Tibacuy, Fusagasugá y Soacha, con linderos “calculados y no medidos”.</p></div></div>
      <div class="t-item reveal"><div class="t-year">1806</div><div class="t-body"><h3>La hacienda se consolida</h3><p>Se intenta verificar sus linderos con los de Usatama por orden del Virrey Amar y Borbón, algo imposible porque los mojones habían desaparecido.</p></div></div>
      <div class="t-item reveal"><div class="t-year">1845</div><div class="t-body"><h3>Don Ángel María Caballero</h3><p>Nace en la provincia de Neiva quien sería propietario de la hacienda, descendiente de familia hidalga, alto funcionario del gobierno del Tolima y diputado a su Asamblea.</p></div></div>
      <div class="t-item reveal"><div class="t-year">1920–30</div><div class="t-body"><h3>El esplendor de la Casona</h3><p>La Casa Señorial era un palacete tropical de rasgos hispano-arábigos: gruesas paredes, patios empedrados con aljibes y albercas, samanes, ceibas y chicalaes, corredores de columnas de madera, capilla y oratorio. La hacienda tenía incluso su propia moneda, el “medio real”.</p></div></div>
      <div class="t-item reveal"><div class="t-year">1935</div><div class="t-body"><h3>Nace Silvania</h3><p>La parcelación de El Chocho en más de mil parcelas la convirtió en símbolo de la reforma agraria y en cuna del primer partido agrario. El 21 de febrero se funda Silvania, impulsada por el líder campesino Ismael Silva, último contabilista de la hacienda.</p></div></div>
      <div class="t-item reveal"><div class="t-year">Hoy</div><div class="t-body"><h3>Club Campestre El Bosque</h3><p>Bordeado por el río Chocho y la carretera a Tibacuy, en 52 fanegadas, el club tiene como epicentro social la Casa del Chocho, conservada en su integridad arquitectónica y rodeada de modernas instalaciones.</p></div></div>
    </div>
  </div>
</section>

<section class="section section--alt" id="proposito" aria-labelledby="prop-h">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow">Propósito</span><h2 id="prop-h">Lo que nos mueve</h2></div></div>
    <div class="grid grid-3">
      <article class="value-card reveal"><span class="num">01 · MISIÓN</span><h3>Integración familiar</h3><p>Proporcionar, con el concurso de un excelente equipo humano, el mejor ambiente para fortalecer la integración familiar y satisfacer necesidades de orden recreacional, cultural y deportivo del asociado y sus allegados, con profundo respeto por los valores éticos y cívicos, en armonía con la comunidad y la naturaleza.</p></article>
      <article class="value-card reveal reveal-d1"><span class="num">02 · VISIÓN</span><h3>Referente nacional</h3><p>Ser el primer Club Social, Recreativo y Deportivo de Colombia que, por sus recursos naturales, históricos y arquitectónicos y la calidad de sus servicios, se proyecte internacionalmente como modelo del turismo ecológico y familiar, en beneficio de las comunidades de su entorno.</p></article>
      <article class="value-card reveal reveal-d2"><span class="num">03 · PROMESA DE VALOR</span><h3>El mejor ambiente</h3><p>El mejor ambiente para compartir en familia: naturaleza, deporte y cultura, atendidos por un equipo humano comprometido con la ética, el civismo y el cuidado del entorno.</p></article>
    </div>
  </div>
</section>

<section class="section" id="gobierno" aria-labelledby="gob-h">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow">Gobierno corporativo</span><h2 id="gob-h">Quiénes dirigen el club</h2><p class="lead">Entidad privada sin ánimo de lucro. Periodo publicado en el sitio actual: 2021 – 2023.</p></div></div>
    <h3 class="reveal">Junta Directiva</h3>
    <div class="people reveal" style="margin-bottom:3rem">""" + "".join(person(n, r) for n, r in directiva) + """</div>
    <h3 class="reveal">Junta de Vigilancia</h3>
    <div class="people reveal">""" + "".join(person(n, r) for n, r in vigilancia) + """</div>
  </div>
</section>

<section class="section--tight"><div class="container">
  <div class="cta-band reveal">
    <img src="@U/2020/03/f_administracion_2-1.jpg" alt="" loading="lazy">
    <h2>Ven a conocer la Casona</h2>
    <p class="lead">Recorre los patios empedrados y corredores donde comenzó la historia de Silvania.</p>
    <div class="hero-actions"><a class="btn btn--primary" href="contacto.html#visita">Agendar recorrido</a></div>
  </div>
</div></section>
"""
)
