import os
import zipfile

# Pre generovanie prázdnych obrázkov
from PIL import Image

# --- Základný priečinok ---
base_dir = "Zahradkari-Rosuchov"
os.makedirs(base_dir, exist_ok=True)

# --- index.html ---
index_html = """<!DOCTYPE html>
<html lang="sk">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Záhradkári Rosuchov</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header>
<h1>Záhradkári Rosuchov</h1>
<nav>
<a href="#onas">O nás</a>
<a href="#aktualne">Aktuálne</a>
<a href="#archiv">Archív</a>
<a href="#spravy">Správy</a>
<a href="#kontakt">Kontakt</a>
</nav>
</header>

<section id="onas" class="content">
<h2>O nás</h2>
<p>Sme komunita záhradkárov z Rosuchova, ktorá pestuje rastliny a zdieľa skúsenosti medzi členmi.</p>
</section>

<section id="aktualne" class="content">
<h2>Aktuálne obrázky</h2>
<div class="gallery">
<img src="aktualne/januar2025/fotka1.jpg" alt="Január 2025">
<img src="aktualne/februar2025/fotka1.jpg" alt="Február 2025">
<img src="aktualne/marec2025/fotka1.jpg" alt="Marec 2025">
</div>
</section>

<section id="archiv" class="content">
<h2>Archív podľa mesiacov</h2>
<ul class="archive-list">
<li><a href="aktualne/januar2025/">Január 2025</a></li>
<li><a href="aktualne/februar2025/">Február 2025</a></li>
<li><a href="aktualne/marec2025/">Marec 2025</a></li>
</ul>
</section>

<section id="spravy" class="content">
<h2>Správy pre záhradkárov</h2>
<article class="sprava">
<h3>Jesenné práce v záhrade</h3>
<p>Pred príchodom mrazov zazimujte náradie a ošetrte ovocné stromy.</p>
</article>
</section>

<section id="kontakt" class="content">
<h2>Kontakt</h2>
<p>Email: <a href="mailto:zahradkari.rosuchov@gmail.com">zahradkari.rosuchov@gmail.com</a></p>
<p>Adresa: Rosuchov 123, Slovensko</p>
<p>Telefón: +421 900 123 456</p>
</section>

<footer>
<p>© 2025 Záhradkári Rosuchov</p>
</footer>
</body>
</html>
"""

# --- style.css ---
style_css = """body { font-family: Arial, sans-serif; margin:0; padding:0; background:#f6fff3; color:#2e402d; }
header { background:#4c9a2a; color:white; text-align:center; padding:20px 0; }
nav a { color:white; margin:0 15px; text-decoration:none; font-weight:bold; }
nav a:hover { text-decoration:underline; }
.content { padding:40px; max-width:900px; margin:auto; }
h2 { border-bottom:2px solid #4c9a2a; padding-bottom:10px; }
.gallery { display:flex; flex-wrap:wrap; gap:10px; justify-content:center; }
.gallery img { width:30%; border-radius:8px; box-shadow:0 2px 6px rgba(0,0,0,0.2); }
.archive-list { list-style:none; padding:0; }
.archive-list a { color:#2e402d; text-decoration:none; font-weight:bold; }
.archive-list a:hover { color:#4c9a2a; }
.sprava { margin-bottom:30px; background:#e9f5e4; padding:20px; border-radius:8px; }
footer { background:#4c9a2a; color:white; text-align:center; padding:15px; margin-top:40px; }
"""

# --- README.md ---
readme = """# Záhradkári Rosuchov

Jednoduchá webová stránka pre záhradkárov v Rosuchove.

## Struktúra priečinkov
Zahradkari-Rosuchov/
├── index.html
├── style.css
├── aktualne/
│   ├── januar2025/
│   │   └── index.html
│   ├── februar2025/
│   │   └── index.html
│   └── marec2025/
│       └── index.html
└── README.md
"""

# --- Uloženie hlavných súborov ---
os.makedirs(base_dir, exist_ok=True)
with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)
with open(os.path.join(base_dir, "style.css"), "w", encoding="utf-8") as f:
    f.write(style_css)
with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme)

# --- Šablóna mesiacov ---
months = ["januar2025", "februar2025", "marec2025"]
month_template = """<!DOCTYPE html>
<html lang="sk">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Záhradkári Rosuchov – {month}</title>
<link rel="stylesheet" href="../../style.css">
</head>
<body>
<header>
<h1>Záhradkári Rosuchov</h1>
<nav>
<a href="../../index.html">Domov</a>
<a href="../">Späť na aktuálne</a>
</nav>
</header>
<section class="content">
<h2>{month}</h2>
<p>Tu môžete pridať fotografie a text o aktivitách v mesiaci {month}.</p>
<div class="gallery">
<img src="fotka1.jpg" alt="Fotka 1">
<img src="fotka2.jpg" alt="Fotka 2">
<img src="fotka3.jpg" alt="Fotka 3">
</div>
</section>
<footer>
<p>© 2025 Záhradkári Rosuchov</p>
</footer>
</body>
</html>
"""

# --- Vytvorenie mesiacov a prázdnych obrázkov ---
for m in months:
    mdir = os.path.join(base_dir, "aktualne", m)
    os.makedirs(mdir, exist_ok=True)
    
    # Vytvor index.html
    with open(os.path.join(mdir, "index.html"), "w", encoding="utf-8") as f:
        f.write(month_template.format(month=m.capitalize()))
    
    # Vytvor prázdne obrázky (100x100 zelené)
    for i in range(1, 4):
        img_path = os.path.join(mdir, f"fotka{i}.jpg")
        img = Image.new("RGB", (100, 100), color=(144, 238, 144))  # svetlozelená
        img.save(img_path)

# --- Vytvorenie ZIP ---
zip_filename = "Zahradkari-Rosuchov.zip"
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            filepath = os.path.join(root, file)
            zipf.write(filepath, os.path.relpath(filepath, base_dir))

print(f"✅ Projekt zabalený ako {zip_filename}")
