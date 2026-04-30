# ASTAT Karteikarten

Lern-Karteikarten für das Modul **Angewandte Statistik für Datenwissenschaften** (HSLU Semester 2). 99 Karten über alle 11 Wochen, mit Filter, Fortschrittsspeicher und Tastaturbedienung.

---

## Schnellstart

**Doppelklick auf [`karteikarten.html`](karteikarten.html)** – fertig. Funktioniert offline ohne Setup.

---

## Bedienung

### Tastatur
| Taste | Aktion |
|---|---|
| `Space` / `Enter` | Antwort zeigen |
| `J` | ✓ kann ich (nach Antwort) |
| `F` | ✗ muss üben (nach Antwort) |
| `→` | nächste Karte |
| `←` | vorige Karte |
| `S` | Karten mischen |

### Filter
- **Wochen** – SW01 bis SW11 ein-/ausschalten
- **Kategorien** – Begriff, Formel, Konzept, Code, Falle
- **Schwierigkeit** – leicht, mittel, schwer
- **Status** – noch nicht / muss üben / kann ich
- **"Nur muss üben"** – Schnellfilter für Wiederholung

### Fortschritt
Wird in `localStorage` gespeichert (browserspezifisch). Übersteht Tab-Schliessen, Reloads, Updates der HTML-Datei.

---

## Dateien

| Datei | Zweck |
|---|---|
| `karteikarten.json` | Quelldaten – 99 Karten in strukturiertem JSON |
| `template.html` | HTML/CSS/JS-Template mit `__CARDS_JSON__`-Platzhalter |
| `build_html.py` | Generiert `karteikarten.html` aus Template + JSON |
| `karteikarten.html` | **Diese Datei öffnen** – standalone, alles inline |

---

## Karten erweitern oder ändern

1. **Neue Karte:** in `karteikarten.json` ein neues Objekt im `cards`-Array hinzufügen:

```json
{
  "id": "sw11-13",
  "week": "SW11",
  "topic": "Regression",
  "category": "Konzept",
  "difficulty": "medium",
  "front": "Frage in HTML mit $\\LaTeX$ erlaubt",
  "back": "Antwort in HTML – &lt;b&gt;, &lt;code&gt;, &lt;br&gt; etc."
}
```

2. **Neu generieren:**
```bash
python build_html.py
```

3. Die `karteikarten.html` neu öffnen (oder Reload).

### Verfügbare Kategorien
- `Begriff` – Definitionen, Grundkonzepte
- `Formel` – Mathematische Formeln
- `Code` – Python-Befehle und ihre Bedeutung
- `Konzept` – Tieferes Verständnis und Zusammenhänge
- `Falle` – Häufige Fehler und Misverständnisse

### Schwierigkeitsgrade
- `easy` – Vokabular, einfache Rechnung
- `medium` – Anwendung, Verständnis
- `hard` – Tiefere Konzepte, häufige Fallen

### LaTeX
Inline-Mathematik in `$...$`, Block-Mathematik in `$$...$$`. Wird via MathJax gerendert. **In JSON müssen Backslashes verdoppelt werden:** `$\\frac{a}{b}$`.

---

## Statistik der Karten

| Woche | Anzahl |
|---|---|
| SW01 Datenmanipulation | 5 |
| SW02 Datenbeschreibung | 11 |
| SW03 Visualisierung | 6 |
| SW04 Wahrscheinlichkeit | 12 |
| SW05 Stichproben | 7 |
| SW06 Schätzverfahren & Bootstrap | 11 |
| SW07 Hypothesentests | 11 |
| SW08 ANOVA & Chi-Quadrat | 6 |
| SW09 Zusammenhang nominal | 6 |
| SW10 Korrelation & Kausalität | 10 |
| SW11 Regression | 14 |
| **Total** | **99** |

| Kategorie | Anzahl |
|---|---|
| Begriff | 21 |
| Formel | 11 |
| Code | 12 |
| Konzept | 35 |
| Falle | 20 |

| Schwierigkeit | Anzahl |
|---|---|
| leicht | 20 |
| mittel | 53 |
| schwer | 26 |
