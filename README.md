# MSE public website

The site is generated from `build_pages.py`. Korean and English content is maintained in the `T` dictionary. Edit both languages, run `python build_pages.py`, review the generated `ko/` and `en/` pages, then commit and push. GitHub Pages publishes from `main`.

- Feature and guide screenshots are placeholders. Add approved images to `assets/` and replace the relevant placeholder markup in the generator. The player search image on the introduction is an older example.
- Replace the disabled download text and QR placeholder in the generator when the Google Play URL is available; generate a QR code for that actual URL.
- Add dated release entries to the updates template in the generator after a release; do not publish unreleased changes as released.
- Keep `privacy/ko.html` and `privacy/en.html` available at their existing URLs.
- This repository is public. Do not add app source code, save files, private screenshots or credentials.

Homepage feature copy, captions and screenshot mappings are maintained in features.json (15 Korean entries, 14 English entries). Screenshot originals are in assets/screens. Run python build_pages.py after editing content.

Screenshot emphasis uses annotations.json (2280x1080 pixel coordinates). build_pages.py generates inline SVG pencil circles; the image viewer preserves these overlays.
