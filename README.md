# Aqua Clean 59 — site vitrine

Site statique (HTML/CSS/JS) pour Aqua Clean 59, nettoyage auto et textile à domicile (Pecquencourt).

- `site/` : le site publié (déployé automatiquement sur GitHub Pages à chaque push sur `main`)
- `tools/build.py` : génère les 5 pages HTML (header, footer, bandeau promo communs)

```bash
python3 tools/build.py                                  # régénérer les pages
python3 -m http.server 4173 --directory site            # aperçu local
```
