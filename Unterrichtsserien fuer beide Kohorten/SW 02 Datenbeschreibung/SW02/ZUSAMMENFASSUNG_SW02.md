# ASTAT – Angewandte Statistik für Datenwissenschaften
## SW 02 – Datenbeschreibung mit Python

GRÖSSER GLEICH BEI WEILSCHLEIFE MACHT BEI KLEINEN DATEN MÄNGEN EINEN GROSSEN UNTERSCHIED, BEI FINAL RICHTIG


---

## 🎯 Lernziele

1. Sie können **absolute und relative Häufigkeiten** und **Summenhäufigkeiten** berechnen und verstehen ihre Bedeutung.
2. Sie kennen **Lagemasse und Streumasse** für **nominale**, **ordinale** und **metrische** Merkmale und können sie berechnen.

---

## 📖 Wichtigste Begriffe

| Begriff | Definition |
|---------|-----------|
| **Absolute Häufigkeit** $n(w)$ (absolute frequency) | Anzahl, wie oft ein Wert $w$ in den Daten vorkommt |
| **Relative Häufigkeit** $h(w)$ (relative frequency) | Anteil, mit dem ein Wert $w$ vorkommt: $h(w) = \frac{n(w)}{n}$ |
| **Absolute Summenhäufigkeit** $N(w)$ (cumulative absolute frequency) | Anzahl, wie oft Werte $\leq w$ vorkommen |
| **Relative Summenhäufigkeit** $H(w)$ (cumulative relative frequency) | Anteil der Werte $\leq w$: $H(w) = \frac{N(w)}{n}$ |
| **Empirische Häufigkeitsverteilung** (empirical frequency distribution) | Auflistung aller Werte $w_1, \ldots, w_m$ mit ihren Häufigkeiten |
| **Lagemass** (measure of central tendency) | Beschreibt mit einem typischen Wert, **wo** die Ausprägungen liegen |
| **Streumass** (measure of dispersion) | Beschreibt mit einem typischen Wert, **wie unterschiedlich** die Ausprägungen sind |
| **Modus** $\bar{x}_D$ (mode) | Der am häufigsten vorkommende Wert (für alle Merkmalstypen) |
| **Dispersionsindex** $P$ (dispersion index) | Streumass für nominale Merkmale; $P = 0$ = keine Streuung, $P = 1$ = maximale Gleichverteilung |
| **$p$-Quantil** $x_p$ (p-quantile) | Wert, der die Daten so teilt, dass $p$% der Werte $\leq x_p$ sind |
| **Median** $x_{50}$ (median) | Das 50%-Quantil; teilt die Daten in zwei gleich grosse Hälften |
| **Unteres Quartil** $x_{25}$ (lower quartile) | 25%-Quantil; ca. ein Viertel der Daten ist kleiner |
| **Oberes Quartil** $x_{75}$ (upper quartile) | 75%-Quantil; ca. drei Viertel der Daten ist kleiner |
| **Diversität** $D$ (diversity) | Streumass für ordinale Merkmale; $D = 0$ = keine Streuung, $D = 1$ = maximale Streuung |
| **Arithmetisches Mittel** $\bar{x}$ (arithmetic mean) | Summe aller Werte geteilt durch Anzahl; nur für metrische Daten sinnvoll |
| **Robust** (robust) | Eigenschaft eines Masses, auf extreme Werte wenig zu reagieren (z.B. Median) |
| **Quartilsabstand** $Q$ (interquartile range, IQR) | $Q = x_{75} - x_{25}$; Bereich, in dem die mittleren 50% der Daten liegen |
| **Mittlere Abweichung** $MD$ (mean deviation) | Durchschnittliche Abweichung der Werte vom Mittelwert (mit Absolutbetrag) |
| **Mittlere quadratische Abweichung** $MQD$ (mean squared deviation) | Durchschnittliche quadrierte Abweichung vom Mittelwert |
| **Standardabweichung** $s$ (standard deviation) | $s = \sqrt{MQD}$; häufigstes Streumass für metrische Daten |

---

## 📐 Konzepte & Definitionen

### 1. Häufigkeitsanalyse

**Formale Definition:**
Die grundlegendste Aufbereitung statistischer Daten ist die Darstellung, wie häufig die Werte $w$ eines Merkmals vorkommen.

| Häufigkeitsart | Symbol | Formel | Gilt für |
|----------------|--------|--------|----------|
| Absolute Häufigkeit | $n(w)$ | Anzahl des Wertes $w$ | Nominal, Ordinal, Metrisch |
| Relative Häufigkeit | $h(w)$ | $\frac{n(w)}{n}$ | Nominal, Ordinal, Metrisch |
| Absolute Summenhäufigkeit | $N(w)$ | Anzahl der Werte $\leq w$ | Ordinal, Metrisch |
| Relative Summenhäufigkeit | $H(w)$ | $\frac{N(w)}{n}$ | Ordinal, Metrisch |

**Intuitive Erklärung:**
- $n(w)$: „Wie oft kommt $w$ vor?"
- $h(w)$: „Welcher Anteil ist $w$?" (Summe aller $h(w) = 1$)
- $N(w)$: „Wie viele Werte sind höchstens $w$?"
- $H(w)$: „Welcher Anteil ist höchstens $w$?" ($H$ wächst bis 1.0)

> ⚠️ **Merke:** Summenhäufigkeiten sind nur für ordinale und metrische Merkmale sinnvoll, weil eine Reihenfolge nötig ist!

> ⚠️ **Informationsverlust:** Aus der empirischen Häufigkeitsverteilung kann man **nicht** mehr herauslesen, welchen Wert eine einzelne statistische Einheit hat – nur noch, wie oft die Werte vorkommen.

**Konkretes Beispiel:** 10 Studierende mit Merkmal **Geschlecht** (nominal):

| Wert $w$ | $n(w)$ | $h(w)$ |
|----------|--------|--------|
| m | 4 | 0.4 |
| w | 6 | 0.6 |
| **Summe** | **10** | **1.0** |

**Konkretes Beispiel:** Merkmal **Prädikat** (ordinal, natürliche Reihenfolge):

| Wert $w$ | $n(w)$ | $h(w)$ | $N(w)$ | $H(w)$ |
|----------|--------|--------|--------|--------|
| genügend | 1 | 0.1 | 1 | 0.1 |
| gut | 3 | 0.3 | 4 | 0.4 |
| sehr gut | 4 | 0.4 | 8 | 0.8 |
| ausgezeichnet | 2 | 0.2 | 10 | 1.0 |

---

### 2. Lagemass und Streumass – Überblick

**Formale Definition:**
- **Lagemass:** Beschreibt mit einem typischen Wert, **wo** die Ausprägungen eines Merkmals liegen.
- **Streumass:** Beschreibt mit einem typischen Wert, **wie unterschiedlich** die Ausprägungen eines Merkmals sind.

Welches Mass man wählt, hängt vom **Merkmalstyp** (Skalenniveau) ab:

| Merkmalstyp | Lagemass | Streumass |
|-------------|----------|-----------|
| **Nominal** | Modus $\bar{x}_D$ | Dispersionsindex $P$ |
| **Ordinal** | Modus, **Median** $x_{50}$, Quantile | Diversität $D$ |
| **Metrisch** | Modus, Median, **Arithmetisches Mittel** $\bar{x}$ | $Q$, $MD$, $MQD$, **Standardabweichung** $s$ |

> ⚠️ **Prüfungshinweis:** Merkmalstyp bestimmt die zulässigen Masse! Arithmetisches Mittel ist **nur für metrische** Daten sinnvoll. Median ist **nicht für nominale** Daten sinnvoll (keine Ordnung).

---

### 3. Nominale Merkmale: Modus & Dispersionsindex

#### Modus $\bar{x}_D$

**Definition:** Der am **häufigsten** vorkommende Wert eines Merkmals.

- Gibt es **genau einen** häufigsten Wert → unimodal
- Gibt es **mehrere** gleich häufige Werte → multimodal (alle werden angegeben)

**Beispiel (Geschlecht):** $\bar{x}_D = \text{"w"}$ (6 × "w" vs. 4 × "m")

#### Dispersionsindex $P$

**Formel:**

$$P = \frac{m}{m-1} \Big( h(w_1) \cdot (1 - h(w_1)) + h(w_2) \cdot (1 - h(w_2)) + \ldots + h(w_m) \cdot (1 - h(w_m)) \Big)$$

**Variablen:**
- $m$ = Anzahl verschiedener Werte des Merkmals
- $h(w_i)$ = relative Häufigkeit des Wertes $w_i$

**Interpretation:**
| Wert | Bedeutung |
|------|-----------|
| $P = 0$ | Keine Streuung: **ein** Wert hat relative Häufigkeit 1.0 |
| $P < 0.8$ | Geringe Dispersion |
| $P > 0.9$ | Starke Dispersion |
| $P = 1$ | Maximale Gleichverteilung: alle Werte gleich häufig |

**Zahlenbeispiel (Geschlecht):** $m = 2$, $h(\text{m}) = 0.4$, $h(\text{w}) = 0.6$

$$P = \frac{2}{2-1} \Big( 0.4 \cdot (1 - 0.4) + 0.6 \cdot (1 - 0.6) \Big) = 2 \cdot (0.24 + 0.24) = 2 \cdot 0.48 = 0.96$$

→ $P = 0.96 > 0.9$ → **starke Dispersion** (fast gleich verteilt)

**Extremfälle nachvollziehen:**
- Alle gleich häufig ($h = \frac{1}{m}$ für alle): $P = \frac{m}{m-1} \cdot m \cdot \frac{1}{m} \cdot \frac{m-1}{m} = 1$
- Ein Wert dominiert ($h = 1$ für einen, $h = 0$ für Rest): $P = 0$

---

### 4. Ordinale Merkmale: Median, Quantile & Diversität

#### $p$-Quantil $x_p$

**Definition:** Das $p$-Quantil $x_p$ ist der Wert, der die geordneten Daten so teilt:
- **Unterer Teil:** $p$% der Daten sind $\leq x_p$
- **Oberer Teil:** $(1-p)$% der Daten sind $\geq x_p$

**Bestimmungsregel:** Wähle den Wert $w$, für den **zum ersten Mal** $H(w) \geq p$ gilt.

**Spezialfälle:**

| Quantil | Name | Bedeutung |
|---------|------|-----------|
| $x_{25}$ | Unteres Quartil | Ca. 25% der Daten sind kleiner |
| $x_{50}$ | **Median** | Ca. 50% der Daten sind kleiner (= «Mitte») |
| $x_{75}$ | Oberes Quartil | Ca. 75% der Daten sind kleiner |

**Zahlenbeispiel (Prädikat):**

| Wert $w$ | $H(w)$ | Prüfung |
|----------|--------|---------|
| genügend | 0.1 | $0.1 < 0.5$ → weiter |
| gut | 0.4 | $0.4 < 0.5$ → weiter |
| sehr gut | 0.8 | $0.8 \geq 0.5$ ✅ → **Median** |
| ausgezeichnet | 1.0 | |

→ $x_{50} = \text{"sehr gut"}$

> ⚠️ **Prüfungstipp:** Immer den **ersten** Wert nehmen, bei dem $H(w) \geq p$ zum ersten Mal gilt!

#### Diversität $D$

**Formel:**

$$D = \frac{4}{m-1} \Big( H(w_1) \cdot (1 - H(w_1)) + H(w_2) \cdot (1 - H(w_2)) + \ldots + H(w_m) \cdot (1 - H(w_m)) \Big)$$

**Variablen:**
- $m$ = Anzahl verschiedener Werte
- $H(w_i)$ = relative **Summenhäufigkeit** des Wertes $w_i$ (⚠️ nicht $h(w_i)$!)

**Interpretation:**
| Wert | Bedeutung |
|------|-----------|
| $D = 0$ | Keine Streuung: alle Daten beim gleichen Wert |
| $D < 0.6$ | Geringe Diversität |
| $D > 0.8$ | Starke Diversität |
| $D = 1$ | Maximale Streuung: 50% beim kleinsten, 50% beim grössten Wert |

**Zahlenbeispiel (Prädikat):**

$$D = \frac{4}{4-1} \Big( 0.1 \cdot 0.9 + 0.4 \cdot 0.6 + 0.8 \cdot 0.2 + 1.0 \cdot 0.0 \Big)$$
$$= \frac{4}{3} \cdot (0.09 + 0.24 + 0.16 + 0) = \frac{4}{3} \cdot 0.49 = 0.65\overline{3}$$

→ $D = 0.65\overline{3}$: mittlere Diversität (zwischen 0.6 und 0.8)

> ⚠️ **Wichtiger Unterschied:** Dispersionsindex $P$ verwendet **relative Häufigkeiten** $h(w)$, Diversität $D$ verwendet **relative Summenhäufigkeiten** $H(w)$!

---

### 5. Metrische Merkmale: Mittelwert, Quartilsabstand, Standardabweichung

#### Arithmetisches Mittel $\bar{x}$

**Formel (mit Rohdaten):**

$$\bar{x} = \frac{1}{n}(x_1 + x_2 + \ldots + x_n)$$

**Formel (mit Häufigkeiten):**

$$\bar{x} = h(w_1) \cdot w_1 + h(w_2) \cdot w_2 + \ldots + h(w_m) \cdot w_m$$

**Variablen:**
- $n$ = Anzahl Beobachtungen
- $x_i$ = einzelne Datenwerte
- $w_i$ = verschiedene Werte, $h(w_i)$ = deren relative Häufigkeiten

**Zahlenbeispiel (Alter):** Daten: 27, 34, 29, 24, 25, 27, 27, 69, 26, 31

$$\bar{x} = \frac{1}{10}(27 + 34 + 29 + 24 + 25 + 27 + 27 + 69 + 26 + 31) = \frac{319}{10} = 31.9$$

Alternativ mit Häufigkeiten:

$$\bar{x} = 0.1 \cdot 24 + 0.1 \cdot 25 + 0.1 \cdot 26 + 0.3 \cdot 27 + 0.1 \cdot 29 + 0.1 \cdot 31 + 0.1 \cdot 34 + 0.1 \cdot 69 = 31.9$$

> ⚠️ **Robustheit:** Das arithmetische Mittel wird von **extremen Werten** (hier: Hans mit 69) **stark beeinflusst**. Der Median ist **robuster**, weil extreme Werte die Reihenfolge in der Mitte nicht verändern.

#### Quartilsabstand $Q$ (Interquartile Range, IQR)

**Formel:**

$$Q = x_{75} - x_{25}$$

**Interpretation:** In diesem Bereich liegen ca. **50% der mittleren Daten**. Kleines $Q$ → Daten eng beieinander; grosses $Q$ → Daten streuen stark. Der Quartilsabstand ist **robust** (extreme Werte beeinflussen ihn kaum).

#### Mittlere Abweichung $MD$

**Formel (mit Rohdaten):**

$$MD = \frac{1}{n} \Big( |x_1 - \bar{x}| + |x_2 - \bar{x}| + \ldots + |x_n - \bar{x}| \Big)$$

**Formel (mit Häufigkeiten):**

$$MD = h(w_1) \cdot |w_1 - \bar{x}| + h(w_2) \cdot |w_2 - \bar{x}| + \ldots + h(w_m) \cdot |w_m - \bar{x}|$$

**Zahlenbeispiel (Alter):** mit $\bar{x} = 31.9$

$$MD = \frac{1}{10}(|27-31.9| + |34-31.9| + |29-31.9| + |24-31.9| + |25-31.9| + |27-31.9| + |27-31.9| + |69-31.9| + |26-31.9| + |31-31.9|)$$
$$= \frac{1}{10}(4.9 + 2.1 + 2.9 + 7.9 + 6.9 + 4.9 + 4.9 + 37.1 + 5.9 + 0.9) = \frac{78.4}{10} = 7.84$$

#### Mittlere quadratische Abweichung $MQD$

**Formel:**

$$MQD = \frac{1}{n} \Big( (x_1 - \bar{x})^2 + (x_2 - \bar{x})^2 + \ldots + (x_n - \bar{x})^2 \Big)$$

**Zahlenbeispiel (Alter):** mit $\bar{x} = 31.9$

$$MQD = \frac{1}{10}((27-31.9)^2 + (34-31.9)^2 + \ldots + (31-31.9)^2) = 160.69$$

> ⚠️ **Nachteil:** $MQD$ hat **quadratische Einheiten** (z.B. Jahre²). Darum braucht man die Standardabweichung.

#### Standardabweichung $s$

**Formel:**

$$s = \sqrt{MQD} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$

**Zahlenbeispiel:** $s = \sqrt{160.69} \approx 12.676$

> ⚠️ **Prüfungskritisch – `ddof`-Parameter:**
> - `ddof=0` → Division durch $n$ → **für gegebene Daten** (deskriptive Statistik)
> - `ddof=1` → Division durch $n-1$ → **für Stichproben** (inferenzielle Statistik, kommt später!)
> - In dieser Woche immer `ddof=0` verwenden!

---

## 🔢 Formeln & Rechenregeln

### Übersicht aller Formeln

| Formel | Ausdruck | Merkmalstyp | Variablen |
|--------|----------|-------------|-----------|
| Relative Häufigkeit | $h(w) = \frac{n(w)}{n}$ | Alle | $n(w)$ = abs. Häufigkeit, $n$ = Gesamtanzahl |
| Relative Summenhäufigkeit | $H(w) = \frac{N(w)}{n}$ | Ordinal, Metrisch | $N(w)$ = abs. Summenhäufigkeit |
| Dispersionsindex | $P = \frac{m}{m-1} \sum_{i=1}^{m} h(w_i)(1-h(w_i))$ | Nominal | $m$ = Anz. versch. Werte |
| Diversität | $D = \frac{4}{m-1} \sum_{i=1}^{m} H(w_i)(1-H(w_i))$ | Ordinal | $m$ = Anz. versch. Werte |
| Arithm. Mittel | $\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$ | Metrisch | $x_i$ = Datenwerte |
| Mittlere Abweichung | $MD = \frac{1}{n}\sum_{i=1}^{n} \|x_i - \bar{x}\|$ | Metrisch | $\bar{x}$ = arithm. Mittel |
| Mittl. quadr. Abweichung | $MQD = \frac{1}{n}\sum_{i=1}^{n}(x_i-\bar{x})^2$ | Metrisch | |
| Standardabweichung | $s = \sqrt{MQD}$ | Metrisch | |
| Quartilsabstand | $Q = x_{75} - x_{25}$ | Metrisch | $x_p$ = $p$-Quantil |

### Durchgerechnetes Beispiel: Geschlecht (nominal)

**Daten:** m, m, m, m, w, w, w, w, w, w → $n = 10$, $m = 2$

1. $h(\text{m}) = \frac{4}{10} = 0.4$, $h(\text{w}) = \frac{6}{10} = 0.6$
2. **Modus:** $\bar{x}_D = \text{"w"}$
3. **Dispersionsindex:** $P = \frac{2}{1}(0.4 \cdot 0.6 + 0.6 \cdot 0.4) = 2 \cdot 0.48 = 0.96$

### Durchgerechnetes Beispiel: Prädikat (ordinal)

**Daten (sortiert):** genügend, gut, gut, gut, sehr gut, sehr gut, sehr gut, sehr gut, ausgezeichnet, ausgezeichnet

1. $h$-Werte: 0.1, 0.3, 0.4, 0.2
2. $H$-Werte: 0.1, 0.4, 0.8, 1.0
3. **Median:** $x_{50} = \text{"sehr gut"}$ (erster Wert mit $H \geq 0.5$)
4. **Diversität:** $D = \frac{4}{3}(0.1 \cdot 0.9 + 0.4 \cdot 0.6 + 0.8 \cdot 0.2 + 1.0 \cdot 0.0) = \frac{4}{3} \cdot 0.49 = 0.65\overline{3}$

### Durchgerechnetes Beispiel: Alter (metrisch)

**Daten:** 27, 34, 29, 24, 25, 27, 27, 69, 26, 31 → $n = 10$

1. **Arithm. Mittel:** $\bar{x} = \frac{319}{10} = 31.9$
2. **Median:** Sortiert: 24, 25, 26, 27, 27, 27, 29, 31, 34, 69 → $x_{50} = \frac{27+27}{2} = 27$ (bei gerader Anzahl: Mittel der beiden mittleren Werte)
3. **$MD$:** $= 7.84$ (siehe Berechnung oben)
4. **$MQD$:** $= 160.69$
5. **$s$:** $= \sqrt{160.69} \approx 12.676$

### Randfälle & Hinweise

| Randfall | Verhalten |
|----------|-----------|
| $n = 0$ (leerer Datensatz) | Division durch 0; Python gibt `nan` |
| $m = 1$ (nur ein Wert) | $P$ und $D$ → Division durch 0 ($m-1 = 0$); Streuung = 0 per Definition |
| Alle Werte gleich | $MD = 0$, $MQD = 0$, $s = 0$, $P = 0$, $D = 0$ |
| Ein extremer Ausreisser | $\bar{x}$ stark beeinflusst; Median kaum beeinflusst |

---

## 📊 Vergleiche & Klassifizierungen

### Lagemasse im Vergleich

| Eigenschaft | Modus $\bar{x}_D$ | Median $x_{50}$ | Arithm. Mittel $\bar{x}$ |
|-------------|-------|--------|-----------|
| Gilt für nominal | ✅ | ❌ | ❌ |
| Gilt für ordinal | ✅ | ✅ | ❌ |
| Gilt für metrisch | ✅ | ✅ | ✅ |
| Robust gegen Ausreisser | – | ✅ | ❌ |
| Eindeutig | Nicht immer (multimodal) | Ja | Ja |
| Python-Methode | `.mode()` | `.median()` | `.mean()` |

### Streumasse im Vergleich

| Eigenschaft | Dispersionsindex $P$ | Diversität $D$ | $Q$ | $MD$ | $s$ |
|-------------|-----|-----|-----|------|-----|
| Merkmalstyp | Nominal | Ordinal | Metrisch | Metrisch | Metrisch |
| Verwendet | $h(w_i)$ | $H(w_i)$ | Quantile | $\|x_i - \bar{x}\|$ | $(x_i-\bar{x})^2$ |
| Wertebereich | $[0, 1]$ | $[0, 1]$ | $\geq 0$ | $\geq 0$ | $\geq 0$ |
| Robust | – | – | ✅ | Teilweise | ❌ |
| Einheit | Dimensionslos | Dimensionslos | Originaleinheit | Originaleinheit | Originaleinheit |
| Schwelle gering | $< 0.8$ | $< 0.6$ | – | – | – |
| Schwelle stark | $> 0.9$ | $> 0.8$ | – | – | – |

### Häufigkeitstypen nach Merkmalstyp

| | Nominal | Ordinal | Metrisch |
|---|---------|---------|----------|
| $n(w)$ – Absolute Häufigkeit | ✅ | ✅ | ✅ |
| $h(w)$ – Relative Häufigkeit | ✅ | ✅ | ✅ |
| $N(w)$ – Abs. Summenhäufigkeit | ❌ | ✅ | ✅ |
| $H(w)$ – Rel. Summenhäufigkeit | ❌ | ✅ | ✅ |

### $P$ vs. $D$ – Verwechslungsgefahr!

| Merkmal | Dispersionsindex $P$ | Diversität $D$ |
|---------|-----|-----|
| **Für** | Nominale Merkmale | Ordinale Merkmale |
| **Vorfaktor** | $\frac{m}{m-1}$ | $\frac{4}{m-1}$ |
| **Verwendet** | Relative Häufigkeiten $h(w_i)$ | Relative **Summen**häufigkeiten $H(w_i)$ |
| **Gering** | $P < 0.8$ | $D < 0.6$ |
| **Stark** | $P > 0.9$ | $D > 0.8$ |

---

## 💻 Code-Beispiele (Python)

#### Konzept: DataFrame erstellen und Daten strukturieren
Erstellt ein DataFrame mit verschiedenen Merkmalstypen (nominal, ordinal, metrisch) als Ausgangspunkt für alle weiteren Analysen.

```python
import numpy as np
import pandas as pd

# Beispieldaten: 10 Studierende
namen = ["Anna","Beat","Cary","Dana","Elif","Faro","Gabi","Hans","Ivea","Jose"]
geschlecht = ["w","m","m","w","w","m","w","m","w","w"]
prädikat = ["ausgezeichnet","gut","sehr gut","sehr gut","gut","ausgezeichnet","sehr gut","genügend","sehr gut","gut"]
alter = [27,34,29,24,25,27,27,69,26,31]

df = pd.DataFrame({"Name": namen,
                    "Geschlecht": geschlecht,
                    "Prädikat": prädikat,
                    "Alter": alter})
```

**Output/Interpretation:** Ein DataFrame mit 10 Zeilen und 4 Spalten. Geschlecht = nominal, Prädikat = ordinal, Alter = metrisch.

---

#### Konzept: Absolute und relative Häufigkeiten berechnen
Verwendet `np.unique()` mit `return_counts=True` um die empirische Häufigkeitsverteilung zu bestimmen.

```python
# Absolute Häufigkeiten für nominales Merkmal "Geschlecht"
werte, absH = np.unique(df["Geschlecht"], return_counts=True)

# Ausgabe
print("Verteilung der absoluten Häufigkeiten:")
for i in range(len(werte)):
    print("  n(" + werte[i] + ") =", absH[i])
print("Verteilung der relativen Häufigkeiten:")
for i in range(len(werte)):
    print("  h(" + werte[i] + ") =", absH[i]/df.shape[0])
```

**Output/Interpretation:**
```
Verteilung der absoluten Häufigkeiten:
  n(m) = 4
  n(w) = 6
Verteilung der relativen Häufigkeiten:
  h(m) = 0.4
  h(w) = 0.6
```
`np.unique()` gibt die Werte alphabetisch sortiert zurück und `df.shape[0]` liefert die Gesamtanzahl $n$.

---

#### Konzept: Ordinale Merkmale – Natürliche Reihenfolge herstellen
Bei ordinalen Merkmalen stimmt die alphabetische Sortierung oft nicht mit der natürlichen Ordnung überein. Man muss die Indizes manuell umsortieren.

```python
werte, absH = np.unique(df["Prädikat"], return_counts=True)
# Alphabetisch: ['ausgezeichnet', 'genügend', 'gut', 'sehr gut']
# Natürliche Ordnung: genügend < gut < sehr gut < ausgezeichnet
# Indizes: genügend=1, gut=2, sehr gut=3, ausgezeichnet=0

print("Verteilung der absoluten Häufigkeiten:")
for i in [1,2,3,0]:  # Indizes in natürlicher Reihenfolge
    print("  n(" + werte[i] + ") =", absH[i])
```

**Output/Interpretation:**
```
  n(genügend) = 1
  n(gut) = 3
  n(sehr gut) = 4
  n(ausgezeichnet) = 2
```

> ⚠️ `np.unique()` sortiert **immer alphabetisch**, nicht nach natürlicher Ordnung!

---

#### Konzept: Summenhäufigkeiten berechnen (ordinal)
Kumuliert die Häufigkeiten Schritt für Schritt auf, um $N(w)$ und $H(w)$ zu erhalten.

```python
print("Verteilung der absoluten Summenhäufigkeiten:")
absSH = 0
for i in [1,2,3,0]:
    absSH += absH[i]
    print("  N(" + werte[i] + ") =", absSH)

print("Verteilung der relativen Summenhäufigkeiten:")
absSH = 0
for i in [1,2,3,0]:
    absSH += absH[i]
    print("  H(" + werte[i] + ") =", absSH/df.shape[0])
```

**Output/Interpretation:**
```
  N(genügend) = 1,  H(genügend) = 0.1
  N(gut) = 4,       H(gut) = 0.4
  N(sehr gut) = 8,  H(sehr gut) = 0.8
  N(ausgezeichnet) = 10, H(ausgezeichnet) = 1.0
```

---

#### Konzept: Summenhäufigkeit als Funktion (metrische Daten)
Für metrische Merkmale mit vielen verschiedenen Werten ist eine Funktion praktikabler als eine vollständige Auflistung.

```python
def Summenhäufigkeit(w, n, x):
    '''w: Eindeutige Werte als numpy array
       n: Absolute Häufigkeiten als numpy array
       x: Abfragewert (z.B. ein Alter)'''
    N = 0
    i = 0
    while i < len(w) and w[i] <= x:
        N += n[i]
        i += 1
    return (N, N/sum(n))  # (N(x), H(x))

werte, absH = np.unique(df["Alter"], return_counts=True)
print(Summenhäufigkeit(werte, absH, 25))
```

**Output/Interpretation:** `(2, 0.2)` → 2 Personen sind höchstens 25 Jahre alt, das entspricht 20% der Daten.

---

#### Konzept: Modus berechnen mit `.mode()`
Die Pandas-Methode `.mode()` liefert den häufigsten Wert direkt.

```python
# Modus für nominales Merkmal
modus_g = df["Geschlecht"].mode()[0]
print("Modus Geschlecht: x_D =", modus_g)  # "w"

# Modus für ordinales Merkmal
modus_p = df["Prädikat"].mode()[0]
print("Modus Prädikat: x_D =", modus_p)     # "sehr gut"
```

**Output/Interpretation:**
- Geschlecht: $\bar{x}_D = \text{"w"}$ (6 von 10)
- Prädikat: $\bar{x}_D = \text{"sehr gut"}$ (4 von 10)
- `.mode()` gibt ein Series-Objekt zurück; `[0]` extrahiert den ersten (häufigsten) Wert.

---

#### Konzept: Dispersionsindex $P$ berechnen (nominal)
Berechnet den Dispersionsindex mit Broadcasting für effiziente Vektoroperationen.

```python
werte, absH = np.unique(df["Geschlecht"], return_counts=True)

m = len(werte)                        # Anzahl verschiedene Werte
relH = absH / df.shape[0]            # Relative Häufigkeiten

# Dispersionsindex berechnen
P = m/(m-1) * sum(relH * (1 - relH))  # Broadcasting!

print("P =", P)  # P = 0.96
```

**Output/Interpretation:** $P = 0.96 > 0.9$ → starke Dispersion. Die Geschlechterverteilung ist nahezu gleichmässig. `relH * (1 - relH)` ist elementweises NumPy-Broadcasting.

---

#### Konzept: Median für ordinale Daten berechnen
Den Median findet man, indem man den ersten Wert sucht, bei dem $H(w) \geq 0.5$.

```python
werte, absH = np.unique(df["Prädikat"], return_counts=True)
m = len(werte)

# In natürliche Reihenfolge umsortieren
werte = np.array([werte[1], werte[2], werte[3], werte[0]])
relH = np.array([absH[1], absH[2], absH[3], absH[0]]) / df.shape[0]

# Relative Summenhäufigkeiten
relSH = np.array([relH[0], sum(relH[:2]), sum(relH[:3]), sum(relH)])

# Median suchen: erster Wert mit H(w) >= 0.5
i = 0
while i < m:
    if relSH[i] > 0.5:
        break
    i += 1
median = werte[i]
print("Median =", median)  # "sehr gut"
```

**Output/Interpretation:** Median = "sehr gut", weil $H(\text{sehr gut}) = 0.8$ der erste Wert mit $H \geq 0.5$ ist.

---

#### Konzept: Diversität $D$ berechnen (ordinal)
Verwendet die relativen Summenhäufigkeiten (nicht die relativen Häufigkeiten!).

```python
D = 4/(m-1) * sum(relSH * (1-relSH))  # Broadcasting!
print("D =", D)  # D = 0.6533...
```

**Output/Interpretation:** $D \approx 0.653$ – mittlere Diversität. Die Prädikate sind weder extrem konzentriert noch extrem gestreut.

---

#### Konzept: Metrische Lagemasse – Median und Mittelwert
Für metrische Daten stehen `.median()` und `.mean()` als Pandas-Methoden zur Verfügung.

```python
# Median
q50 = df["Alter"].median()
print("Median =", q50)               # 27.0

# Arithmetisches Mittel
x_bar = df["Alter"].mean()
print("Arithmetisches Mittel =", x_bar)  # 31.9
```

**Output/Interpretation:** $x_{50} = 27.0$ vs. $\bar{x} = 31.9$ – der Ausreisser Hans (69) zieht den Mittelwert nach oben, beeinflusst den Median aber kaum. Das zeigt die **Robustheit** des Medians.

---

#### Konzept: Quantile und Quartilsabstand $Q$
Die Methode `.quantile(p/100)` berechnet beliebige $p$-Quantile.

```python
Q = df["Alter"].quantile(0.75) - df["Alter"].quantile(0.25)
print("Q =", Q)
```

**Output/Interpretation:** Der Quartilsabstand gibt an, wie breit der Bereich der mittleren 50% der Daten ist.

---

#### Konzept: Mittlere Abweichung $MD$
Berechnet die durchschnittliche Abweichung vom Mittelwert mit `np.abs()` für den Absolutbetrag.

```python
MD = sum(np.abs(df["Alter"] - x_bar)) / df.shape[0]
print("MD =", MD)  # 7.84
```

**Output/Interpretation:** Im Durchschnitt weichen die Alter um 7.84 Jahre vom Mittelwert ab.

---

#### Konzept: Standardabweichung $s$ mit `ddof=0`
Die Methode `.std()` berechnet die Standardabweichung. Der Parameter `ddof` ist entscheidend.

```python
s = df["Alter"].std(ddof=0)    # ddof=0: Division durch n (deskriptiv)
print("s =", s)                # ≈ 12.676

# NICHT verwechseln:
s_stichprobe = df["Alter"].std(ddof=1)  # Division durch n-1 (erst später relevant!)
```

**Output/Interpretation:** $s \approx 12.676$ Jahre. Die grosse Standardabweichung wird durch den Ausreisser Hans (69) verursacht. **Für gegebene Daten immer `ddof=0`!**

---

#### Konzept: CSV-Daten laden und analysieren (Aufgabe 1 – Personalerhebung)
Zeigt den typischen Workflow: Daten laden → Merkmale identifizieren → passende Masse berechnen.

```python
# Daten laden (Semikolon als Trennzeichen)
personal = pd.read_csv("Daten/2021_Personalerhebung.csv", sep=";")

# Merkmale und ihre Typen:
# PersNummer → nominal (ID)
# Abteilung → nominal
# Ausbildung → ordinal (Mittlere Reife < Abitur < Bachelor < Master < Promotion)
# Eintrittsjahr → metrisch (oder ordinal)
# Bruttogehalt → metrisch
```

**Output/Interpretation:** Die Datei enthält 25 Mitarbeitende mit verschiedenen Merkmalstypen. Für jedes Merkmal müssen die passenden Lage- und Streumasse gewählt werden.

---

## 🔗 Konzept-Code-Zuordnung

| Konzept | Python-Funktion/Code | Library | Beschreibung |
|---------|---------------------|---------|-------------|
| Absolute Häufigkeit | `np.unique(data, return_counts=True)` | NumPy | Werte und Anzahlen |
| Relative Häufigkeit | `absH / df.shape[0]` | NumPy | Anteil berechnen |
| Summenhäufigkeit | `np.cumsum()` oder manuell | NumPy | Kumulierte Häufigkeiten |
| Modus | `df["col"].mode()[0]` | Pandas | Häufigster Wert |
| Dispersionsindex $P$ | `m/(m-1) * sum(relH * (1-relH))` | NumPy | Streuung nominaler Daten |
| Diversität $D$ | `4/(m-1) * sum(relSH * (1-relSH))` | NumPy | Streuung ordinaler Daten |
| Median | `df["col"].median()` | Pandas | 50%-Quantil |
| Arithm. Mittel | `df["col"].mean()` | Pandas | Durchschnitt |
| $p$-Quantil | `df["col"].quantile(p/100)` | Pandas | Beliebiges Quantil |
| Quartilsabstand $Q$ | `.quantile(0.75) - .quantile(0.25)` | Pandas | IQR |
| Mittlere Abweichung $MD$ | `sum(np.abs(data - x_bar)) / n` | NumPy | Abs. Abweichungen |
| Standardabweichung $s$ | `df["col"].std(ddof=0)` | Pandas | $\sqrt{MQD}$ mit Division durch $n$ |
| Absolutbetrag | `np.abs(x)` | NumPy | $\|x\|$ |
| Broadcasting | `array * (1 - array)` | NumPy | Elementweise Operationen |
| CSV laden | `pd.read_csv("pfad", sep=";")` | Pandas | Daten einlesen |

---

## ✏️ Übungsaufgaben-Zusammenfassung

### Aufgabe 1: Personalerhebung (2021_Personalerhebung.csv)

| Nr. | Aufgabe | Konzept | Lösungsansatz |
|-----|---------|---------|---------------|
| 1 | Daten laden | `pd.read_csv()` | `pd.read_csv("Daten/2021_Personalerhebung.csv", sep=";")` |
| 2 | Merkmale zuordnen | Merkmalstypen | Abteilung=nominal, Ausbildung=ordinal, Bruttogehalt=metrisch |
| 3 | Lagemasse bestimmen | Modus, Median, Mittelwert | Nominal→Modus, Ordinal→Median, Metrisch→Mittelwert |
| 4 | Streumasse bestimmen | $P$, $D$, $s$ | Nominal→$P$, Ordinal→$D$, Metrisch→$s$ |
| 5 | Häufigkeiten Abteilung | `np.unique()` | Absolute und relative Häufigkeiten |
| 6 | Summenhäufigkeiten Ausbildung | Kumulieren | Natürliche Reihenfolge beachten! |

### Aufgabe 2: Gesundheitskosten (Gesundheitskosten.csv)

| Nr. | Aufgabe | Konzept | Lösungsansatz |
|-----|---------|---------|---------------|
| 1 | Daten laden | `pd.read_csv()` | `pd.read_csv("Daten/Gesundheitskosten.csv")` |
| 2 | Lagemasse bestimmen | Mittelwert, Median | Alle Kostenarten sind metrisch |
| 3 | Streumasse bestimmen | $Q$, $s$ | Quartilsabstand und Standardabweichung |

### Aufgabe 3: Mathematik-Prüfung (2022_Mathematik 1 WiSo Urliste.xls)

| Nr. | Aufgabe | Konzept | Lösungsansatz |
|-----|---------|---------|---------------|
| 1 | Excel laden | `pd.read_excel()` | `pd.read_excel("Daten/2022_Mathematik 1 WiSo Urliste.xls")` |
| 2 | Versionen A/B beachten | Datenbereinigung | Spaltenreihenfolge ist bei Version A und B **vertauscht**! |
| 3 | Lagemasse pro Aufgabe | Mittelwert, Median | Punkte = metrisch → `.mean()`, `.median()` |
| 4 | Streumasse pro Aufgabe | $Q$, $s$ | `.std(ddof=0)`, Quartilsabstand |

---

## ⚠️ Prüfungsrelevante Hinweise

### Typische Aufgabentypen und wie man sie erkennt

| Aufgabentyp | Erkennungsmerkmal | Vorgehen |
|-------------|-------------------|----------|
| „Welches Lagemass?" | Merkmalstyp erkennen | Nominal→Modus, Ordinal→Median, Metrisch→Mittelwert |
| „Berechnen Sie $P$" | Nominales Merkmal + Streuung | Relative Häufigkeiten → Formel mit $\frac{m}{m-1}$ |
| „Berechnen Sie $D$" | Ordinales Merkmal + Streuung | Relative **Summen**häufigkeiten → Formel mit $\frac{4}{m-1}$ |
| „Berechnen Sie $\bar{x}$ und $s$" | Metrisches Merkmal | Mittelwert → dann Abweichungen quadrieren |
| „Bestimmen Sie den Median" | Quantil gefragt | Werte sortieren → $H(w) \geq 0.5$ finden |
| „Was gibt dieser Code aus?" | Python-Snippet gegeben | `ddof`-Parameter beachten! `np.unique()` sortiert alphabetisch! |

### Häufige Fehlerquellen & Fallstricke

| Falle | Erklärung |
|-------|-----------|
| $P$ und $D$ verwechseln | $P$ nutzt $h(w)$, $D$ nutzt $H(w)$! Vorfaktoren unterschiedlich! |
| Alphabetische vs. natürliche Ordnung | `np.unique()` sortiert **alphabetisch** – bei ordinalen Daten muss man umsortieren! |
| `ddof=0` vs. `ddof=1` | Für **gegebene Daten** immer `ddof=0`; `ddof=1` erst bei Stichprobenstatistik (später) |
| Median bei gerader Anzahl | Bei metrischen Daten: **Mittelwert** der beiden mittleren Werte |
| Summenhäufigkeit für Nominale | **Nicht möglich!** Keine Ordnung → keine Kumulierung |
| Mittelwert für Ordinale | **Nicht sinnvoll!** "gut" + "sehr gut" = ? |
| Robustheit vergessen | Median = robust, Mittelwert = nicht robust |
| $H(w_m)$ bei Diversität | Letzter Wert hat immer $H(w_m) = 1.0$ → Beitrag $= 1 \cdot 0 = 0$ |

### Merkregeln & Eselsbrücken

| Regel | Eselsbrücke |
|-------|-------------|
| Welches Mass für welchen Typ? | **N**ominal → einfa**ch**ste Masse (Modus, $P$); **O**rdinal → **O**rdnung nutzen (Median, $D$); **M**etrisch → **M**aximale Möglichkeiten ($\bar{x}$, $s$, alles) |
| $P$ vs. $D$ unterscheiden | **P** = einzelne  **P**rozente ($h$); **D** = auf**D**addierte Prozente ($H$) |
| Dispersionsindex-Schwellen | $P$: 0.**8** gering, 0.**9** stark |
| Diversitäts-Schwellen | $D$: 0.**6** gering, 0.**8** stark |
| Robustheit | **Me**dian → **me**hr Robustheit; **Mi**ttelwert → **mi**nder robust |

### Formeln für das A4-Blatt (unbedingt draufschreiben!)

| Formel | Grund |
|--------|-------|
| $P = \frac{m}{m-1} \sum h(w_i)(1-h(w_i))$ | Vorfaktor und Summanden leicht verwechselbar |
| $D = \frac{4}{m-1} \sum H(w_i)(1-H(w_i))$ | Ähnlich wie $P$, aber mit $H$ statt $h$ und Faktor 4 statt $m$ |
| $MQD = \frac{1}{n}\sum(x_i - \bar{x})^2$ | Grundlage für $s$ |
| $s = \sqrt{MQD}$ | Einfach, aber manchmal vergessen |
| $Q = x_{75} - x_{25}$ | Definition Quartilsabstand |
| Schwellen: $P$: 0.8/0.9; $D$: 0.6/0.8 | Grenzwerte für Interpretation |

### Formeln die man auswendig wissen muss

| Formel | Warum auswendig? |
|--------|-----------------|
| $h(w) = \frac{n(w)}{n}$ | Zu grundlegend für das A4-Blatt |
| $\bar{x} = \frac{1}{n}\sum x_i$ | Grundformel, muss sitzen |
| $x_{50}$ = erster Wert mit $H \geq 0.5$ | Definitionsregel |

### SC/MC-Hinweise: Typische Distraktoren

- ❌ „Der Dispersionsindex verwendet Summenhäufigkeiten" → **FALSCH** (verwendet $h(w)$, nicht $H(w)$!)
- ❌ „Die Diversität verwendet relative Häufigkeiten" → **FALSCH** (verwendet $H(w)$!)
- ❌ „Das arithmetische Mittel ist robust" → **FALSCH** (reagiert stark auf Ausreisser)
- ❌ „Der Median ist für nominale Daten geeignet" → **FALSCH** (keine Ordnung!)
- ❌ „`std(ddof=1)` berechnet die Standardabweichung der Daten" → **FALSCH** (`ddof=0` für gegebene Daten!)
- ❌ „Bei $P = 1$ kommt nur ein Wert vor" → **FALSCH** ($P = 1$ bedeutet maximale Gleichverteilung!)
- ❌ „Summenhäufigkeiten sind für nominale Merkmale definiert" → **FALSCH**

### Numerische Antworten: Rundungsregeln

- Standardmässig auf **2 Dezimalstellen** runden, sofern nicht anders angegeben
- Bei Brüchen: exakt angeben wenn möglich (z.B. $0.65\overline{3}$ statt 0.65)
- $P$ und $D$ sind dimensionslos (keine Einheit)
- Standardabweichung hat die **gleiche Einheit** wie die Daten

---

## 🔗 Verbindung zu vorherigen/folgenden Wochen

### Rückbezug zu SW 01 (Datenmanipulation mit Python)

| SW 01 Konzept | Wird in SW 02 verwendet als |
|---------------|----------------------------|
| **Merkmalstypen** (Nominal/Ordinal/Metrisch) | Entscheidend für die **Wahl** von Lage- und Streumassen |
| **`np.unique(return_counts=True)`** | Grundlage für **Häufigkeitsberechnung** |
| **`pd.DataFrame`** | Datencontainer für alle Berechnungen |
| **`pd.read_csv()`** | Laden der Übungsdaten |
| **Broadcasting** | Effiziente Berechnung von $P$ und $D$ (`relH * (1-relH)`) |
| **`df.shape[0]`** | Gesamtanzahl $n$ für relative Häufigkeiten |
| **`.mean()`, `.min()`, `.max()`** | Erweitert um `.median()`, `.std()`, `.quantile()`, `.mode()` |

### Vorausschau auf kommende Wochen

| SW 02 Konzept | Wird gebraucht in |
|---------------|-------------------|
| **Häufigkeitsverteilung** | SW 03 (Visualisierung: Histogramme, Balkendiagramme) |
| **Mittelwert & Standardabweichung** | SW 04 (Normalverteilung), SW 05 (Stichprobenverteilung), SW 07–08 (Tests) |
| **Median & Quartile** | SW 03 (Box-Plots), alle weiteren Wochen |
| **Quantile** | SW 06 (Konfidenzintervalle), SW 07 (p-Wert, kritische Werte) |
| **`ddof=0` vs. `ddof=1`** | SW 05–06 (Stichproben: dann wird `ddof=1` relevant!) |
| **Robustheit** | SW 05 (Stichprobentheorie), SW 11–12 (Regression: Ausreissererkennung) |
| **Merkmalstyp → Mass-Zuordnung** | SW 07–08 (Wahl des richtigen Testverfahrens), SW 09–10 (Zusammenhangsmasse) |

> **Vorausschau SW 03:** Die nächste Woche behandelt **Datenvisualisierung** mit Matplotlib. Die in SW 02 berechneten Kennzahlen (Häufigkeiten, Lagemasse, Streumasse) werden dann **grafisch dargestellt** – als Histogramme, Balkendiagramme, Box-Plots und Scatter-Plots.
