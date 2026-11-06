import pathlib
import time

VER = time.strftime("%Y%m%d%H%M")

OUT = pathlib.Path(__file__).resolve().parent.parent / "site"
TEL = "tel:+33757468512"
TEL_TXT = "07 57 46 85 12"
IG = "https://www.instagram.com/aqua.clean.59/"
FB = "https://www.facebook.com/search/top?q=Aqua%20Clean%2059"

I = {
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "msg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 5h16v11H8l-4 4z"/></svg>',
}
STAR = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3l-5.9 3.3 1.3-6.6L2.5 9.4l6.6-.8z"/></svg>'
STARS = '<span class="stars" aria-label="5 étoiles sur 5">' + STAR * 5 + "</span>"

NAV = [("index.html", "Accueil"), ("voitures.html", "Voitures"), ("textiles.html", "Canapés & matelas"),
       ("realisations.html", "Réalisations"), ("contact.html", "Devis & contact")]


CUR = ' aria-current="page"'

def page(file, title, desc, body, promo=True):
    links = "".join(
        f'<li><a href="{h}"{CUR if h == file else ""}>{t}</a></li>' for h, t in NAV)
    promo_html = (
        '<div class="promo-bar"><strong>Novembre :</strong> −10 % sur toutes les prestations, '
        '−15 % à Pecquencourt. <a href="voitures.html#offres">Voir les offres</a></div>'
    ) if promo else ""
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0b0d10">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/video/poster.jpg">
<link rel="icon" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,300..900&family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css?v={VER}">
</head>
<body>
{promo_html}
<header class="site-header">
  <nav class="nav wrap" aria-label="Navigation principale">
    <a class="brand" href="index.html" aria-label="Aqua Clean 59, accueil">
      <span class="brand-mark" aria-hidden="true"></span>
      <span><span class="brand-name">Aqua <span>Clean</span></span><span class="brand-sub">Nettoyage à domicile · 59</span></span>
    </a>
    <ul class="nav-links">{links}</ul>
    <a class="btn btn-primary nav-cta" href="{TEL}">{I['phone']}{TEL_TXT}</a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </nav>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true"></span><span class="brand-name">Aqua <span>Clean</span> 59</span></a>
        <p>Nettoyage de véhicules et de textiles à domicile. Camion autonome en eau et en électricité, basé à Pecquencourt.</p>
      </div>
      <div><h4>Prestations</h4><ul>
        <li><a href="voitures.html">Voitures &amp; utilitaires</a></li>
        <li><a href="textiles.html">Canapés &amp; matelas</a></li>
        <li><a href="voitures.html#options">Rénovation des phares</a></li>
        <li><a href="realisations.html">Avant / après</a></li>
      </ul></div>
      <div><h4>Contact</h4><ul>
        <li><a href="{TEL}">{TEL_TXT}</a></li>
        <li><a href="contact.html">Demander un devis</a></li>
        <li>7 j/7, sur rendez-vous</li>
      </ul></div>
      <div><h4>Suivre</h4><ul>
        <li><a href="{IG}" target="_blank" rel="noopener">Instagram · aqua.clean.59</a></li>
        <li><a href="{FB}" target="_blank" rel="noopener">Facebook · Aqua Clean 59</a></li>
      </ul></div>
    </div>
    <div class="footer-legal"><span>© <span data-year>2026</span> Aqua Clean 59 · Pecquencourt (59146)</span><span>Nord · Pas-de-Calais · Belgique</span></div>
  </div>
</footer>
<div class="callbar">
  <a class="btn btn-primary" href="{TEL}">{I['phone']}Appeler</a>
  <a class="btn btn-ghost" href="contact.html">{I['msg']}Devis</a>
</div>
<script src="assets/main.js?v={VER}" defer></script>
</body>
</html>
"""
    (OUT / file).write_text(html)


def ba(before, after, alt_b, alt_a, start=50):
    return f"""<div class="ba">
  <img class="ba-after" src="assets/img/{after}" alt="{alt_a}" loading="lazy">
  <img class="ba-before" src="assets/img/{before}" alt="{alt_b}" loading="lazy">
  <span class="ba-handle"></span>
  <span class="ba-tag l">Avant</span><span class="ba-tag r">Après</span>
  <input type="range" min="0" max="100" value="{start}" aria-label="Comparer avant et après">
</div>"""


def cta(title="Une voiture à remettre à neuf&nbsp;?"):
    return f"""<section class="section cta-band">
  <div class="wrap cta-inner reveal">
    <div>
      <span class="label">Réservation</span>
      <h2 class="display h2 mt-s">{title}</h2>
      <a class="phone-big" href="{TEL}">{TEL_TXT}</a>
    </div>
    <div class="hero-actions">
      <a class="btn btn-primary" href="contact.html">Demander un devis {I['arrow']}</a>
    </div>
  </div>
</section>"""


REVIEWS = [
    ("Maxime est rapide, disponible et très minutieux. Le résultat est vraiment impressionnant&nbsp;: l’intérieur comme l’extérieur sont parfaitement propres.", "Léa C.", "Google"),
    ("Un grand merci à Aqua Clean 59 et à Maxime pour un travail exceptionnel sur mes voitures, avec déplacement à domicile. Mes voitures semblent comme neuves.", "Michel S.", "Google"),
    ("De passage sur la région pour un chantier, j’ai fait appel à Aqua Clean pour nettoyer mon utilitaire en fin de chantier. Il me l’a rendu comme neuf&nbsp;!", "Jonathan R.", "Google"),
    ("Découvert par hasard, Maxime est venu pour le nettoyage de mes canapés. Je suis plus que satisfait de la prestation, vous pouvez y aller les yeux fermés.", "TheVerty9", "Google"),
    ("Rapport qualité-prix excellent par rapport à la concurrence du secteur. Travail propre et soigné sur l’intérieur et l’extérieur de mon véhicule.", "Adrien B.", "Google"),
    ("Je recommande les yeux fermés&nbsp;! Très ponctuel et surtout très professionnel. Ma voiture est comme neuve, travail impeccable.", "Soizic H.", "Google"),
]


def reviews(n=3):
    items = "".join(f"""<figure class="review">
  {STARS}
  <blockquote>« {q} »</blockquote>
  <figcaption><b>{a}</b><small>Avis {s}</small></figcaption>
</figure>""" for q, a, s in REVIEWS[:n])
    return f'<div class="reviews reveal">{items}</div>'


# ---------------------------------------------------------------- ACCUEIL
home = f"""
<section class="hero">
  <div class="hero-media">
    <video data-hero-video autoplay muted loop playsinline preload="metadata" poster="assets/video/poster.webp" aria-hidden="true">
      <source src="assets/video/hero.mp4" type="video/mp4">
    </video>
  </div>
  <div class="wrap">
    <span class="label">Pecquencourt · Nord · Pas-de-Calais · Belgique</span>
    <h1 class="display h1">Votre voiture comme neuve, <span class="thin">sans bouger de chez vous.</span></h1>
    <div class="hero-bottom">
      <p class="lead hide-m">Maxime vient avec son camion-atelier, à votre domicile ou sur votre lieu de travail. Eau, électricité, produits&nbsp;: tout est à bord. Vous n’avez qu’à donner les clés.</p>
      <p class="lead show-m">Lavage à domicile ou sur votre lieu de travail, autour de Pecquencourt.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="{TEL}">{I['phone']}{TEL_TXT}</a>
        <a class="btn btn-ghost" href="voitures.html"><span class="hide-m">Voir les tarifs</span><span class="show-m">Tarifs</span></a>
      </div>
    </div>
    <div class="facts">
      <div class="fact"><b>Dès 80 €</b><span>Intérieur complet, petite voiture</span></div>
      <div class="fact"><b>100 % autonome</b><span>Pas besoin de prise ni d’eau</span></div>
      <div class="fact"><b>Trajet offert</b><span>Jusqu’à 25 km de Pecquencourt</span></div>
      <div class="fact"><b>5★ clients</b><span>16 avis, 100 % recommandé</span></div>
    </div>
  </div>
</section>

<section class="section paper">
  <div class="wrap">
    <div class="section-head reveal">
      <div>
        <span class="label">Prestations</span>
        <h2 class="display h2">Trois métiers,<br>un seul camion.</h2>
      </div>
      <a class="arrow-link" href="voitures.html">Tous les tarifs {I['arrow']}</a>
    </div>
    <div class="services reveal">
      <a class="service" href="voitures.html">
        <div class="service-img"><img src="assets/img/injecteur.webp" alt="Injection-extraction sur la moquette avant d’une voiture" loading="lazy"></div>
        <div class="service-body">
          <span class="service-num">01</span>
          <h3 class="display h3">Voitures &amp; utilitaires</h3>
          <p>Aspiration en profondeur, shampoing des sièges et moquettes, plastiques, vitres, coffre. Carrosserie et jantes en option extérieur.</p>
          <div class="from"><small>À partir de</small><strong>80 €</strong></div>
        </div>
      </a>
      <a class="service" href="textiles.html">
        <div class="service-img"><img src="assets/img/banquette.webp" alt="Banquette arrière en tissu après shampoing" loading="lazy"></div>
        <div class="service-body">
          <span class="service-num">02</span>
          <h3 class="display h3">Canapés &amp; matelas</h3>
          <p>Nettoyage textile en profondeur à domicile&nbsp;: taches, odeurs, acariens. Matelas traités recto-verso, tapis et sièges sur demande.</p>
          <div class="from"><small>À partir de</small><strong>35 €</strong></div>
        </div>
      </a>
      <a class="service" href="voitures.html#options">
        <div class="service-img"><img src="assets/img/phare-apres.webp" alt="Phare avant rénové, transparent" loading="lazy"></div>
        <div class="service-body">
          <span class="service-num">03</span>
          <h3 class="display h3">Rénovation des phares</h3>
          <p>Les optiques jaunies ou ternes retrouvent leur transparence. Plus esthétique, et surtout un meilleur éclairage la nuit.</p>
          <div class="from"><small>Seule</small><strong>70 €</strong></div>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <span class="label">Avant / après</span>
      <h2 class="display h2 mt-s">Le résultat parle de lui-même.</h2>
      <p class="lead mt-s">Siège conducteur d’une berline, traité par injection-extraction. Faites glisser le curseur pour comparer. Aucune retouche, photos prises sur place.</p>
      <a class="arrow-link mt-m" href="realisations.html">Voir d’autres réalisations {I['arrow']}</a>
    </div>
    <div class="split-media reveal">
      {ba("siege-avant.webp", "siege-apres.webp", "Siège en tissu très sale avant nettoyage", "Le même siège propre après nettoyage", 55)}
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="wrap">
    <div class="section-head reveal">
      <div>
        <span class="label">Comment ça se passe</span>
        <h2 class="display h2">Simple. Vraiment.</h2>
      </div>
    </div>
    <div class="steps reveal">
      <div class="step"><h3 class="display h3">Vous appelez</h3><p>Par téléphone, SMS ou Messenger. On fixe le créneau et on valide le prix ensemble.</p></div>
      <div class="step"><h3 class="display h3">Maxime arrive</h3><p>Chez vous ou au travail, avec le camion équipé&nbsp;: eau, groupe électrogène, aspirateurs, produits.</p></div>
      <div class="step"><h3 class="display h3">Il nettoie</h3><p>Vous vaquez à vos occupations. Aucun branchement, aucune installation de votre côté.</p></div>
      <div class="step"><h3 class="display h3">Vous récupérez</h3><p>Une voiture qui sent le propre. Vous payez une fois satisfait du résultat.</p></div>
    </div>
  </div>
</section>

<section class="section paper">
  <div class="wrap">
    <div class="section-head reveal">
      <div>
        <span class="label">Avis clients</span>
        <div class="score mt-s"><strong>100&nbsp;%</strong><span>de recommandation sur Facebook (16 avis), 5★ sur Google.</span></div>
      </div>
      <a class="arrow-link" href="realisations.html#avis">Lire plus d’avis {I['arrow']}</a>
    </div>
    {reviews(3)}
  </div>
</section>

{cta()}
"""
page("index.html", "Aqua Clean 59 · Nettoyage auto et textile à domicile, Pecquencourt",
     "Nettoyage intérieur et extérieur de voitures, canapés et matelas à domicile autour de Pecquencourt (59). Camion 100 % autonome, déplacement gratuit jusqu’à 25 km. Dès 80 €.", home)

# ---------------------------------------------------------------- VOITURES
def row(name, sub, a, b, c):
    return f"<tr><th scope=\"row\">{name}<small>{sub}</small></th><td>{a}</td><td>{b}</td><td class=\"hl\">{c}</td></tr>"

cars = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Accueil</a> / Voitures</div>
    <h1 class="display h1">Tarifs<br><span class="thin">véhicules.</span></h1>
    <p class="lead">Des prix fixes, annoncés avant de commencer. Lavage à domicile ou sur votre lieu de travail, déplacement offert jusqu’à 25&nbsp;km.</p>
  </div>
</section>

<section class="section paper">
  <div class="wrap">
    <div class="section-head reveal">
      <div><span class="label">Grille tarifaire</span><h2 class="display h2">Choisissez votre gabarit.</h2></div>
      <div class="seg" role="tablist" data-tabs="veh">
        <button role="tab" aria-selected="true" aria-controls="p-voitures">Voitures</button>
        <button role="tab" aria-selected="false" aria-controls="p-utilitaires">Utilitaires</button>
      </div>
    </div>

    <div id="p-voitures" data-panel-group="veh" role="tabpanel" class="reveal">
      <div class="price-cards">
        <article class="pcard">
          <span class="tag">Petite</span><h3 class="display h3">Citadine</h3>
          <p>Citadine ou petit utilitaire, 2 places.</p>
          <div class="rows"><div class="row"><span>Intérieur</span><strong>80 €</strong></div><div class="row"><span>Intérieur + extérieur</span><strong>105 €</strong></div></div>
        </article>
        <article class="pcard featured">
          <span class="tag">Moyenne · la plus demandée</span><h3 class="display h3">Berline &amp; compacte</h3>
          <p>Berline, break compact, petit SUV.</p>
          <div class="rows"><div class="row"><span>Intérieur</span><strong>90 €</strong></div><div class="row"><span>Intérieur + extérieur</span><strong>115 €</strong></div></div>
        </article>
        <article class="pcard">
          <span class="tag">Grande</span><h3 class="display h3">SUV &amp; familiale</h3>
          <p>Grand SUV, 4×4, familiale 5 à 7 places.</p>
          <div class="rows"><div class="row"><span>Intérieur</span><strong>100 €</strong></div><div class="row"><span>Intérieur + extérieur</span><strong>125 €</strong></div></div>
        </article>
      </div>
    </div>

    <div id="p-utilitaires" data-panel-group="veh" role="tabpanel" hidden>
      <table class="price-table">
        <thead><tr><th>Volume</th><th>Intérieur</th><th>Int. + extérieur</th><th>&nbsp;</th></tr></thead>
        <tbody>
          <tr><th scope="row">Utilitaire 6 m³<small>Kangoo, Berlingo, Caddy…</small></th><td>80 €</td><td>120 €</td><td></td></tr>
          <tr><th scope="row">Utilitaire 11 m³<small>Trafic, Vivaro, Vito…</small></th><td>90 €</td><td>140 €</td><td></td></tr>
          <tr><th scope="row">Utilitaire 14 m³<small>Master, Boxer, Sprinter…</small></th><td>100 €</td><td>160 €</td><td></td></tr>
          <tr><th scope="row">Poids lourd, camping-car, agricole<small>Selon l’état et le volume</small></th><td colspan="2" style="font-size:22px">Sur devis</td><td></td></tr>
        </tbody>
      </table>
    </div>
    <p class="note">Prix TTC, véhicule en état d’usage normal. Les suppléments éventuels sont annoncés avant intervention.</p>
  </div>
</section>

<section class="section">
  <div class="wrap two-col">
    <div class="reveal">
      <span class="label">Formule intérieur</span>
      <h2 class="display h2 mt-s">Ce qui est inclus.</h2>
      <ul class="check-list mt-m">
        <li>Aspiration complète en profondeur</li>
        <li>Sols, moquettes et tapis nettoyés en profondeur</li>
        <li>Plastiques&nbsp;: tableau de bord, portières, console centrale, contours de portes</li>
        <li>Shampoing des sièges par injection-extraction</li>
        <li>Vitres intérieures</li>
        <li>Coffre et ouverture de coffre</li>
      </ul>
    </div>
    <div class="reveal">
      <span class="label">Option extérieur</span>
      <h2 class="display h2 mt-s">Et dehors.</h2>
      <ul class="check-list mt-m">
        <li>Lavage de la carrosserie</li>
        <li>Nettoyage des jantes</li>
        <li>Vitres extérieures</li>
      </ul>
      <img class="mt-m" src="assets/img/jante.webp" alt="Nettoyage d’une jante au dégraissant" loading="lazy" style="border-radius:4px;aspect-ratio:16/10;object-fit:cover;width:100%">
    </div>
  </div>
</section>

<section class="section ink-2" id="options">
  <div class="wrap">
    <div class="section-head reveal">
      <div><span class="label">Suppléments &amp; options</span><h2 class="display h2">À la carte.</h2></div>
    </div>
    <div class="extras reveal">
      <div>
        <div class="extra"><span>Rénovation optique des phares (avec un nettoyage)</span><b>+50 €</b></div>
        <div class="extra"><span>Rénovation optique des phares (seule)</span><b>70 €</b></div>
        <div class="extra"><span>Cire hydrophobe brillante + brillant pneus</span><b>25 €</b></div>
        <div class="extra"><span>Paire de tapis supplémentaire</span><b>+10 €</b></div>
        <div class="extra"><span>Nettoyage du plafonnier seul</span><b>Sur devis</b></div>
      </div>
      <div>
        <div class="extra"><span>Véhicule très sale</span><b>+25 €</b></div>
        <div class="extra"><span>Poils d’animaux</span><b>dès 10 €</b></div>
        <div class="extra"><span>Bonbons, chewing-gum</span><b>dès 10 €</b></div>
        <div class="extra"><span>Terre, verdure, moisissure</span><b>dès 10 €</b></div>
        <div class="extra"><span>Cas extrême</span><b>Sur devis</b></div>
      </div>
    </div>
    <div class="split mt-l">
      <div class="reveal">
        <span class="label">Rénovation optique</span>
        <h3 class="display h2 mt-s">Des phares qui éclairent à nouveau.</h3>
        <p class="lead mt-s">Les optiques en polycarbonate jaunissent avec les UV. Ponçage, polissage et protection&nbsp;: la lentille redevient transparente.</p>
      </div>
      <div class="split-media reveal">{ba("phare-avant.webp", "phare-apres.webp", "Phare terne avant rénovation", "Phare rénové et transparent")}</div>
    </div>
  </div>
</section>

<section class="section-tight" id="offres">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="label">Offres du moment · novembre</span><h2 class="display h2">Profitez-en.</h2></div></div>
    <div class="reveal" style="display:grid;gap:16px">
      <div class="offer"><span class="offer-badge">−10 %</span><div><h3 class="display h3">Sur toutes les prestations</h3><p>Voitures, canapés, matelas, tapis, sièges. Valable tout le mois de novembre.</p></div><a class="btn btn-ghost" href="contact.html">Réserver</a></div>
      <div class="offer"><span class="offer-badge">−15 %</span><div><h3 class="display h3">À Pecquencourt</h3><p>Pour les habitants de la commune, avec la cire hydrophobe brillante offerte.</p></div><a class="btn btn-ghost" href="contact.html">Réserver</a></div>
      <div class="offer"><span class="offer-badge">+50 €</span><div><h3 class="display h3">Offre combinée</h3><p>Ajoutez un canapé (4/5 places max) ou un matelas à votre nettoyage voiture pour seulement 50&nbsp;€ de plus.</p></div><a class="btn btn-ghost" href="contact.html">Réserver</a></div>
    </div>
  </div>
</section>

{cta()}
"""
page("voitures.html", "Tarifs nettoyage voiture à domicile · Aqua Clean 59",
     "Nettoyage intérieur dès 80 €, intérieur + extérieur dès 105 €. Utilitaires, rénovation des phares, options. Déplacement gratuit jusqu’à 25 km autour de Pecquencourt.", cars)

# ---------------------------------------------------------------- TEXTILES
tex = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Accueil</a> / Canapés &amp; matelas</div>
    <h1 class="display h1">Canapés<br><span class="thin">&amp; matelas.</span></h1>
    <p class="lead">Le même matériel d’injection-extraction que pour les sièges auto, directement dans votre salon. Taches, odeurs et acariens partent, le tissu sèche en quelques heures.</p>
  </div>
</section>

<section class="section paper">
  <div class="wrap">
    <div class="section-head reveal">
      <div><span class="label">Tarifs textiles</span><h2 class="display h2">Prix fixes, sans surprise.</h2></div>
      <div class="seg" role="tablist" data-tabs="tex">
        <button role="tab" aria-selected="true" aria-controls="p-canapes">Canapés</button>
        <button role="tab" aria-selected="false" aria-controls="p-matelas">Matelas</button>
      </div>
    </div>
    <div id="p-canapes" data-panel-group="tex" role="tabpanel">
      <table class="price-table">
        <thead><tr><th>Format</th><th>Prix</th><th></th><th></th></tr></thead>
        <tbody>
          <tr><th scope="row">Fauteuil<small>1 place</small></th><td class="hl">50 €</td><td></td><td></td></tr>
          <tr><th scope="row">Canapé 2/3 places<small>Droit, assises et dossiers</small></th><td class="hl">70 €</td><td></td><td></td></tr>
          <tr><th scope="row">Canapé 4/5 places<small>Angle ou méridienne</small></th><td class="hl">85 €</td><td></td><td></td></tr>
          <tr><th scope="row">Canapé 5/6 places<small>Grand angle, panoramique</small></th><td class="hl">100 €</td><td></td><td></td></tr>
        </tbody>
      </table>
    </div>
    <div id="p-matelas" data-panel-group="tex" role="tabpanel" hidden>
      <table class="price-table">
        <thead><tr><th>Format · recto / verso</th><th>Prix</th><th></th><th></th></tr></thead>
        <tbody>
          <tr><th scope="row">Matelas bébé<small>Lit à barreaux</small></th><td class="hl">35 €</td><td></td><td></td></tr>
          <tr><th scope="row">1 place<small>90 × 190 / 90 × 200</small></th><td class="hl">50 €</td><td></td><td></td></tr>
          <tr><th scope="row">2 places, standard<small>140 × 190</small></th><td class="hl">75 €</td><td></td><td></td></tr>
          <tr><th scope="row">2 places, grande taille<small>160 × 200 / 180 × 200</small></th><td class="hl">90 €</td><td></td><td></td></tr>
        </tbody>
      </table>
    </div>
    <p class="note">Tapis, chaises et sièges&nbsp;: sur devis. Supplément pour grosse salissure, vomi ou animaux, annoncé avant intervention.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <span class="label">La méthode</span>
      <h2 class="display h2 mt-s">En profondeur, pas en surface.</h2>
      <ul class="check-list mt-m">
        <li>Nettoyage en profondeur des fibres par injection-extraction</li>
        <li>Traitement ciblé des taches</li>
        <li>Désinfection et assainissement</li>
        <li>Aucun branchement chez vous&nbsp;: eau et électricité fournies par le camion</li>
      </ul>
      <p class="note">Astuce&nbsp;: ajoutez un canapé 4/5 places ou un matelas à un nettoyage voiture pour 50&nbsp;€ seulement.</p>
    </div>
    <div class="split-media reveal">
      {ba("arriere-avant.webp", "arriere-apres.webp", "Banquette arrière jonchée de déchets et de miettes", "Même banquette après nettoyage", 50)}
    </div>
  </div>
</section>

<section class="section paper">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="label">Ils ont testé</span><h2 class="display h2">Avis canapés.</h2></div></div>
    <div class="reviews reveal">
      <figure class="review">{STARS}<blockquote>« Découvert par hasard, Maxime est venu pour le nettoyage de mes canapés. Je suis plus que satisfait de la prestation, vous pouvez y aller les yeux fermés. »</blockquote><figcaption><b>TheVerty9</b><small>Avis Google</small></figcaption></figure>
      <figure class="review">{STARS}<blockquote>« Nettoyage de mon canapé, très professionnel, je suis ravie. Encore merci. »</blockquote><figcaption><b>Di So</b><small>Avis Google</small></figcaption></figure>
      <figure class="review">{STARS}<blockquote>« Très pro, ponctuel, travail impeccable. Je recommande. »</blockquote><figcaption><b>Joël L.</b><small>Avis Facebook</small></figcaption></figure>
    </div>
  </div>
</section>

{cta("Un canapé qui a besoin d’un coup de frais&nbsp;?")}
"""
page("textiles.html", "Nettoyage canapé et matelas à domicile · Aqua Clean 59",
     "Nettoyage de canapés dès 50 € et de matelas dès 35 € à domicile autour de Pecquencourt (59). Injection-extraction, désinfection, détachage.", tex)

# ---------------------------------------------------------------- RÉALISATIONS
real = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Accueil</a> / Réalisations</div>
    <h1 class="display h1">Avant.<br><span class="thin">Après.</span></h1>
    <p class="lead">De vraies interventions chez de vrais clients, photographiées sur place. Faites glisser chaque curseur.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="gallery">
      <figure class="reveal">{ba("siege-avant.webp", "siege-apres.webp", "Siège en tissu taché avant nettoyage", "Siège propre après nettoyage", 55)}<figcaption><span>Siège conducteur, berline</span><small>Intérieur</small></figcaption></figure>
      <figure class="reveal">{ba("arriere-avant.webp", "arriere-apres.webp", "Banquette arrière encombrée de déchets", "Banquette arrière propre", 50)}<figcaption><span>Banquette arrière, citadine</span><small>Véhicule très sale</small></figcaption></figure>
      <figure class="reveal">{ba("phare-avant.webp", "phare-apres.webp", "Phare terni", "Phare rénové", 50)}<figcaption><span>Optique avant, utilitaire</span><small>Rénovation</small></figcaption></figure>
    </div>
  </div>
</section>

<section class="section ink-2">
  <div class="wrap">
    <div class="section-head reveal">
      <div><span class="label">En intervention</span><h2 class="display h2">Le camion-atelier.</h2></div>
      <p class="lead" style="max-width:40ch">Tente, groupe électrogène, réserve d’eau, injecteur-extracteur&nbsp;: tout tient dans le Kangoo.</p>
    </div>
    <div class="video-frame reveal">
      <video controls muted playsinline preload="none" poster="assets/video/poster.webp">
        <source src="assets/video/hero.mp4" type="video/mp4">
      </video>
    </div>
    <div class="stills mt-s reveal">
      <img src="assets/img/atelier.webp" alt="Maxime aspire l’habitacle d’une Golf, portière ouverte" loading="lazy">
      <img src="assets/img/injecteur.webp" alt="Injecteur sur la moquette" loading="lazy">
      <img src="assets/img/habitacle.webp" alt="Habitacle propre après intervention" loading="lazy">
    </div>
  </div>
</section>

<section class="section paper" id="avis">
  <div class="wrap">
    <div class="section-head reveal">
      <div><span class="label">Avis clients</span><div class="score mt-s"><strong>5★</strong><span>sur Google, 100&nbsp;% de recommandation sur Facebook.</span></div></div>
      <a class="arrow-link" href="{FB}" target="_blank" rel="noopener">Tous les avis Facebook {I['arrow']}</a>
    </div>
    {reviews(6)}
  </div>
</section>

{cta()}
"""
page("realisations.html", "Réalisations avant / après · Aqua Clean 59",
     "Photos avant / après de nos nettoyages de voitures, sièges et phares, et avis clients. Aqua Clean 59, nettoyage à domicile.", real)

# ---------------------------------------------------------------- CONTACT
svc = ["Voiture — petite", "Voiture — moyenne", "Voiture — grande", "Utilitaire", "Canapé 2/3 places",
       "Canapé 4/5 places", "Matelas 2 places", "Rénovation des phares", "Autre"]
opts = "".join(f"<option>{s}</option>" for s in svc)
contact = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Accueil</a> / Devis &amp; contact</div>
    <h1 class="display h1">On vient<br><span class="thin">à vous.</span></h1>
    <p class="lead">Le plus rapide reste un appel. Sinon, remplissez le formulaire&nbsp;: il prépare un SMS que vous n’avez plus qu’à envoyer.</p>
  </div>
</section>

<section class="section">
  <div class="wrap contact-grid">
    <div class="reveal">
      <a class="channel" href="{TEL}"><span><small>Téléphone · 7 j/7</small><b>{TEL_TXT}</b></span>{I['arrow']}</a>
      <a class="channel" href="sms:+33757468512"><span><small>SMS</small><b>Écrire un message</b></span>{I['arrow']}</a>
      <a class="channel" href="{IG}" target="_blank" rel="noopener"><span><small>Instagram</small><b>@aqua.clean.59</b></span>{I['arrow']}</a>
      <a class="channel" href="{FB}" target="_blank" rel="noopener"><span><small>Facebook · Messenger</small><b>Aqua Clean 59</b></span>{I['arrow']}</a>

      <div class="mt-l">
        <span class="label">Zone d’intervention</span>
        <div class="zone mt-m">
          <div><b>59</b><span>Nord · Douaisis, Valenciennois, Lille</span></div>
          <div><b>62</b><span>Pas-de-Calais · Arras, Lens, Hénin</span></div>
          <div><b>BE</b><span>Belgique frontalière</span></div>
        </div>
        <p class="note">Basé à Pecquencourt (59146). Déplacement gratuit jusqu’à 25&nbsp;km, au-delà nous consulter.</p>
      </div>
    </div>

    <form class="form reveal" data-quote novalidate>
      <div>
        <h2 class="display h3">Demande de devis</h2>
        <p class="mt-s">Réponse rapide par SMS ou appel.</p>
      </div>
      <div class="field">
        <label for="service">Prestation</label>
        <select id="service" name="service" required>
          <option value="" disabled selected>Choisir…</option>{opts}
        </select>
      </div>
      <fieldset class="field" data-formula hidden>
        <legend>Formule</legend>
        <div class="chips">
          <label><input type="radio" name="formula" value="Intérieur" checked><span>Intérieur</span></label>
          <label><input type="radio" name="formula" value="Intérieur + extérieur"><span>Intérieur + extérieur</span></label>
        </div>
      </fieldset>
      <div class="field-row">
        <div class="field"><label for="city">Commune</label><input id="city" name="city" autocomplete="address-level2" placeholder="Pecquencourt" required></div>
        <div class="field"><label for="when">Disponibilité</label>
          <select id="when" name="when"><option value="">Indifférent</option><option>En semaine</option><option>Le week-end</option><option>Au plus vite</option></select>
        </div>
      </div>
      <div class="field"><label for="details">Précisions</label><textarea id="details" name="details" placeholder="Modèle, état, poils d’animaux, taches…"></textarea></div>
      <div class="field"><label for="name">Prénom</label><input id="name" name="name" autocomplete="given-name"></div>
      <div class="estimate"><small>Estimation, hors options</small><strong data-estimate>—</strong></div>
      <div class="form-actions">
        <button class="btn btn-dark" type="submit">{I['msg']}Envoyer par SMS</button>
        <button class="btn btn-outline-ink" type="button" data-copy>Copier le message</button>
      </div>
    </form>
  </div>
</section>

<section class="section ink-2">
  <div class="wrap two-col">
    <div class="reveal"><span class="label">Questions fréquentes</span><h2 class="display h2 mt-s">Bon à savoir.</h2></div>
    <div class="faq reveal">
      <details><summary>Dois-je fournir l’eau ou l’électricité&nbsp;?</summary><p>Non. Le camion est 100&nbsp;% autonome&nbsp;: réserve d’eau et groupe électrogène à bord. Il suffit d’un emplacement pour se garer à côté du véhicule.</p></details>
      <details><summary>Combien de temps dure un nettoyage&nbsp;?</summary><p>Comptez en général entre 2 et 4 heures selon le gabarit, la formule et l’état du véhicule.</p></details>
      <details><summary>Pouvez-vous venir sur mon lieu de travail&nbsp;?</summary><p>Oui, tant qu’on peut accéder au véhicule et stationner le camion à proximité (parking d’entreprise, cour, rue…).</p></details>
      <details><summary>Combien de temps pour que les sièges sèchent&nbsp;?</summary><p>Quelques heures selon la météo et la ventilation. Laissez les vitres entrouvertes si possible.</p></details>
      <details><summary>Les professionnels sont-ils acceptés&nbsp;?</summary><p>Oui&nbsp;: flottes, utilitaires, fins de chantier. Pour les poids lourds, camping-cars et engins agricoles, on établit un devis.</p></details>
    </div>
  </div>
</section>
"""
page("contact.html", "Devis et contact · Aqua Clean 59, nettoyage à domicile",
     "Appelez le 07 57 46 85 12 ou demandez un devis par SMS. Nettoyage auto et textile à domicile, Nord, Pas-de-Calais et Belgique.", contact)
print("ok")
