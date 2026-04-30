"""Erzeugt karteikarten.html durch Einbettung der JSON-Daten in das HTML-Template.

Verwendung:
    python build_html.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(HERE, "karteikarten.json")
TEMPLATE_PATH = os.path.join(HERE, "template.html")
OUTPUT_PATH = os.path.join(HERE, "karteikarten.html")

with open(JSON_PATH, encoding="utf-8") as f:
    cards_json = f.read()

with open(TEMPLATE_PATH, encoding="utf-8") as f:
    template = f.read()

# Validierung
data = json.loads(cards_json)
print(f"Anzahl Karten: {len(data['cards'])}")

# Einbetten
html = template.replace("__CARDS_JSON__", cards_json)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print(f"karteikarten.html geschrieben ({len(html)} Bytes).")
