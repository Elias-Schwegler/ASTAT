# 🤖 ASTAT – Wochen-Zusammenfassung – Prompt-Template

> **Zweck:** Diesen Prompt bei jeder neuen Semesterwoche verwenden, damit der Agent automatisch eine optimale Prüfungszusammenfassung für **Angewandte Statistik für Datenwissenschaften (ASTAT, HSLU)** erstellt.

> [!IMPORTANT]
> **Prüfungsformat:** 90 Minuten, closed book, 1× A4 (beidseitig) als Hilfsmittel erlaubt.
> **Fragetypen:** Single-Choice, Multiple-Choice, numerische Antwort, Lückentext, Zuordnung.

---

## Prompt (Copy-Paste für jede neue Woche)

```
Erstelle eine umfassende Prüfungszusammenfassung für die aktuelle Semesterwoche (SW XX)
des Moduls "Angewandte Statistik für Datenwissenschaften" (ASTAT, HSLU).

Das Ausgabeformat ist ein Markdown-File namens ZUSAMMENFASSUNG_SWXX.md im entsprechenden SW-Ordner.

### Quelldateien im Wochenordner:

Die Hauptquelle ist das Jupyter Notebook. Gehe wie folgt vor:

1. Navigiere zu: Unterrichtsserien fuer beide Kohorten/SW XX <Thema>/SWXX/
2. Lese das Notebook **SWXX.ipynb** vollständig (Markdown- UND Code-Zellen)
3. Lese optionale Daten-Dateien im Ordner **Daten/** (CSV, DAT etc.) für Kontextverständnis
4. Prüfe den Ordner **Bilder/** auf referenzierte Abbildungen
5. Falls zusätzliche PDFs vorhanden (z.B. Übungsblätter, Lösungen), diese ebenfalls einbeziehen

> WICHTIG: Das Notebook ist die primäre Quelle. Es enthält sowohl die Theorie (Markdown-Zellen)
> als auch die zugehörigen Code-Beispiele (Code-Zellen). Beides muss integriert werden.

### Struktur & Inhalt (in dieser Reihenfolge):

1. **Header**: Modulname (ASTAT), Wochennummer (SW XX), Thema
2. **🎯 Lernziele**: Aus dem Notebook abgeleitete Lernziele der Woche
3. **📖 Wichtigste Begriffe**: Tabelle mit Begriff + Definition aller neuen statistischen Konzepte
   - Jeder Begriff mit einer kurzen, verständlichen Erklärung
   - Bei englischen Fachbegriffen: deutsche Übersetzung angeben
4. **📐 Konzepte & Definitionen**: Alle zentralen statistischen Konzepte der Woche:
   - Formale Definition (wo angemessen mit mathematischer Notation)
   - Intuitive Erklärung in eigenen Worten
   - Konkrete Beispiele mit Zahlen
   - Visualisierungsbeschreibung (wenn im Notebook Plots gezeigt werden)
5. **🔢 Formeln & Rechenregeln**: Kompakte Übersicht aller relevanten Formeln:
   - Jede Formel mit Erklärung aller Variablen
   - Durchgerechnetes Zahlenbeispiel zu jeder Formel
   - Randfall-Hinweise (z.B. Division durch 0, n=0, leere Datensätze)
6. **📊 Vergleiche & Klassifizierungen**: Tabellen die Verfahren oder Konzepte gegenüberstellen
   - z.B. Merkmalstypen, Skalenniveaus, Testverfahren, Verteilungen, etc.
7. **💻 Code-Beispiele (Python)**: Zuordnung von Konzepten zu Code-Snippets:
   - Jedes Code-Beispiel hat einen Titel, der das zugehörige Konzept benennt
   - VOR dem Code: kurze Erklärung was der Code tut und welches statistische Konzept er umsetzt
   - NACH dem Code: erwarteter Output und Interpretation des Ergebnisses
   - Kommentare auf Deutsch im Code
   - Verwendete Libraries erklären (NumPy, Pandas, Matplotlib, SciPy, etc.)
   - Format:
     ```
     #### Konzept: <Name des statistischen Konzepts>
     <Erklärung was berechnet wird und warum>
     ```python
     # Code aus dem Notebook
     ```
     **Output/Interpretation:** <Was das Ergebnis bedeutet>
     ```
8. **🔗 Konzept-Code-Zuordnung**: Übersichtstabelle die jedes Konzept der Woche
   mit dem zugehörigen Python-Code/Funktion verknüpft:
   | Konzept | Python-Funktion/Code | Library | Beschreibung |
   |---------|---------------------|---------|-------------|
   | ... | ... | ... | ... |
9. **✏️ Übungsaufgaben-Zusammenfassung** (falls vorhanden): Tabelle aller Aufgaben mit:
   - Aufgabennummer
   - Thema / Konzept
   - Lösungsansatz (Kurzform)
   - Relevanter Code-Snippet
10. **⚠️ Prüfungsrelevante Hinweise**:
    - Typische Aufgabentypen und wie man sie erkennt
    - Häufige Fehlerquellen und Fallstricke
    - Merkregeln und Eselsbrücken
    - Formeln die man auswendig wissen muss vs. die man auf dem A4-Blatt haben sollte
    - Hinweise für SC/MC-Fragen: Typische Distraktoren und Fallen
    - Hinweise für numerische Antworten: Rundungsregeln, Einheiten
11. **🔗 Verbindung zu vorherigen/folgenden Wochen**: Rückbezug und Vorausschau:
    - Wie baut der Stoff auf?
    - Welche Konzepte werden später wieder gebraucht?

### Wichtige Regeln:
- **Sprache:** Deutsch (statistische/mathematische Fachbegriffe dürfen Englisch bleiben)
- **Jupyter Notebooks:** Markdown-Zellen UND Code-Zellen vollständig auswerten
  - Notebooks sind JSON-Dateien: cell_type "markdown" = Theorie, cell_type "code" = Code
  - Code-Zellen immer MIT ihrem Kontext (vorherige Markdown-Zelle) einordnen
- **Code:** Ausschliesslich Python (NumPy, Pandas, Matplotlib, SciPy wo relevant)
- **Mathematische Notation:** LaTeX-Syntax in Markdown ($..$ inline, $$...$$ Blöcke)
- **Formeln** immer mit konkretem Zahlenbeispiel ergänzen
- **Emojis** als Section-Icons verwenden für schnelles Scannen
- **Tabellen** bevorzugen für Vergleiche und Übersichten
- **Konzept→Code Mapping** ist zentral: Jedes theoretische Konzept soll mit seinem
  zugehörigen Code-Snippet verbunden werden
- Das File soll so vollständig sein, dass man damit alleine die Prüfung bestehen kann
- ZUSAMMENFASSUNG aus vorherigen Wochen lesen für Querverweise
- **Prüfungsformat beachten:** Da die Prüfung SC/MC/numerisch/Lückentext ist,
  besonders auf exakte Definitionen, korrekte Formeln und typische Zahlenwerte achten
```

---

## Themenübersicht pro Woche

| Woche | Thema | Schlüsselkonzepte (erwartet) |
|-------|-------|------------------------------|
| SW 01 | Datenmanipulation mit Python | NumPy Arrays, Indexing, statistische Grundbegriffe, Merkmalstypen |
| SW 02 | Datenbeschreibung | Lagemasse, Streuungsmasse, Quantile, Box-Plots |
| SW 03 | Datenvisualisierung | Matplotlib, Histogramme, Scatter-Plots, Balkendiagramme |
| SW 04 | Modelle für zufällige Ereignisse | Wahrscheinlichkeit, Verteilungen, Zufallsvariablen |
| SW 05 | Stichproben | Stichprobentheorie, Stichprobenverteilung, Zentraler Grenzwertsatz |
| SW 06 | Schätzverfahren | Punktschätzung, Konfidenzintervalle, Maximum-Likelihood |
| SW 07 | Testverfahren | Hypothesentests, p-Wert, Signifikanzniveau, Fehler 1./2. Art |
| SW 08 | Testverfahren | Weitere Tests, t-Test, Chi-Quadrat-Test |
| SW 09 | Zusammenhangsanalyse | Korrelation, Kovarianz, Zusammenhangsmasse |
| SW 10 | Zusammenhangsanalyse | Weitere Verfahren, Rangkorrelation, Kontingenzanalyse |
| SW 11 | Regressionsanalyse | Lineare Regression, Kleinste Quadrate, Bestimmtheitsmass |
| SW 12 | Regressionsanalyse | Multiple Regression, Modelldiagnostik |
| SW 13 | Zeitreihenanalyse | Trend, Saisonalität, Glättungsverfahren |

> **Hinweis:** Die Schlüsselkonzepte sind geschätzt und werden beim Erstellen
> der jeweiligen Zusammenfassung aus dem tatsächlichen Notebook-Inhalt abgeleitet.

---

## Ordnerstruktur-Erwartung

```
ASTAT/
├── Unterrichtsserien fuer beide Kohorten/
│   ├── SW 01 Datenmanipulation mit Python/
│   │   └── SW01/
│   │       ├── SW01.ipynb                    ← Hauptquelle (Notebook)
│   │       ├── Daten/                        (CSV, DAT Dateien)
│   │       ├── Bilder/                       (Referenzierte Abbildungen)
│   │       └── ZUSAMMENFASSUNG_SW01.md       ← Output
│   ├── SW 02 Datenbeschreibung/
│   │   └── SW02/
│   │       ├── SW02.ipynb
│   │       ├── Daten/
│   │       ├── Bilder/
│   │       └── ZUSAMMENFASSUNG_SW02.md       ← Output
│   ├── ...
│   └── SW 13 Zeitreihenanalyse/
│       └── SW13/
│           ├── SW13.ipynb
│           └── ZUSAMMENFASSUNG_SW13.md       ← Output
├── ADMIN/
│   └── SW00_admin.pdf                        (Modulübersicht)
├── ZIPS/
└── Prompt.md  ← Diese Datei
```

---

## Hinweise für den Agent

### Notebook-Verarbeitung (.ipynb)
- Jupyter Notebooks sind **JSON-Dateien** mit `cell_type: "markdown"` und `cell_type: "code"`
- **Markdown-Zellen** enthalten die Theorie, Definitionen und Erklärungen
- **Code-Zellen** enthalten die Python-Implementierungen der Konzepte
- Code-Zellen immer im **Kontext** der umgebenden Markdown-Zellen interpretieren
- `outputs`-Feld der Code-Zellen prüfen für tatsächliche Ergebnisse
- Bilder aus dem `Bilder/`-Ordner können im Notebook referenziert sein

### Zusammenfassungs-Erstellung
- Zuerst den **SW-Ordner** der aktuellen Woche in `Unterrichtsserien fuer beide Kohorten/` finden
- Das **Notebook vollständig** lesen (alle Zellen, nicht nur Code)
- **Konzept→Code Zuordnung** ist das Kernstück: Jede Theorie mit dem passenden Code verbinden
- ZUSAMMENFASSUNG aus vorherigen Wochen lesen für **Querverweise**
- **Formeln** immer mit durchgerechnetem Zahlenbeispiel belegen
- **Prüfungsrelevanz priorisieren:** Was könnte als SC/MC/Lückentext gefragt werden?
- Bei Datenmanipulations-Wochen: die konkreten Funktionsaufrufe und Parameter besonders betonen
- Bei Theorie-lastigen Wochen: Definitionen exakt und prüfungstauglich formulieren
