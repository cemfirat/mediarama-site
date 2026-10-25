from pathlib import Path

readme = Path("README.md")

if not readme.is_file():
    raise SystemExit("README.md fehlt")

text = readme.read_text(encoding="utf-8")

if not text.strip():
    raise SystemExit("README.md ist leer")

if "Mediarama" not in text:
    raise SystemExit("Projektname fehlt")

if "https://mediarama.gallery" not in text:
    raise SystemExit("Projekt-Domain fehlt")

markers = ("<<<<<<< ", "=======", ">>>>>>> ")

if any(line.startswith(markers) for line in text.splitlines()):
    raise SystemExit("Merge-Konfliktmarker gefunden")

print("Mediarama site README validation successful")
