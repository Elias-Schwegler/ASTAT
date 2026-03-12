# ASTAT – Angewandte Statistik für Datenwissenschaften

## SW 04 – Modelle für zufällige Ereignisse mit Python

---

## 🎯 Lernziele

1. Sie verstehen das Konzept von **Zufallsvariablen** (diskret und stetig) und deren **Wahrscheinlichkeitsverteilungen**.
2. Sie können das Python-Modul `scipy.stats` verwenden, um mit Wahrscheinlichkeitsverteilungen zu arbeiten.
3. Sie können **Erwartungswert** und **Standardabweichung** für verschiedene Verteilungen berechnen.
4. Sie können die **kumulative Verteilungsfunktion (CDF)** nutzen, um Wahrscheinlichkeiten für Intervalle zu berechnen.
5. Sie kennen die wichtigsten **diskreten Verteilungen** (Uniform, Bernoulli, Binomial, Geometrisch, Poisson, Hypergeometrisch) und die stetige Uniform- und Normalverteilung.

---

## 📖 Wichtigste Begriffe

| Begriff                                                      | Definition                                                                                                                                         |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zufallsexperiment** (random experiment)              | Ein Vorgang mit ungewissem Ausgang (z.B. Würfelwurf, Münzwurf).                                                                                  |
| **Ergebnisraum** $\Omega$ (sample space)             | Die Menge aller möglichen Ergebnisse eines Zufallsexperiments.                                                                                    |
| **Zufallsvariable** $X$ (random variable)            | Eine Funktion, die jedem Ergebnis eines Zufallsexperiments eine reelle Zahl zuordnet.                                                              |
| **Diskrete Zufallsvariable** (discrete r.v.)           | Nimmt endlich viele oder abzählbar unendlich viele Werte an (z.B. Augenzahl beim Würfeln, Anzahl Anrufe).                                        |
| **Stetige Zufallsvariable** (continuous r.v.)          | Nimmt alle Werte aus einem Intervall an (z.B. Körpergrösse, Zeit).                                                                               |
| **Wahrscheinlichkeitsfunktion** (PMF)                  | Gibt für eine*diskrete* Zufallsvariable $X$ die Wahrscheinlichkeit für jeden Wert $x$ an: $P(X=x)$. (Probability Mass Function)          |
| **Dichtefunktion** (PDF)                               | Beschreibt die Verteilung einer*stetigen* Zufallsvariablen. Wahrscheinlichkeit für einen exakten Wert ist 0. (Probability Density Function)     |
| **Kumulative Verteilungsfunktion** (CDF)               | Gibt die Wahrscheinlichkeit an, dass$X$ einen Wert kleiner oder gleich $x$ annimmt: $F(x) = P(X \leq x)$. (Cumulative Distribution Function) |
| **Erwartungswert** $\mu$ oder $E(X)$ (mean)        | Der durchschnittlich zu erwartende Wert einer Zufallsvariablen bei unendlich vielen Durchführungen.                                               |
| **Varianz** $\sigma^2$ oder $Var(X)$ (variance)    | Ein Mass für die Streuung der Werte von$X$ um den Erwartungswert herum.                                                                         |
| **Standardabweichung** $\sigma$ (standard deviation) | Die Wurzel aus der Varianz. Besitzt dieselbe Einheit wie die Zufallsvariable.                                                                      |
| **$p$-Quantil** $x_p$ (p-quantile/PPF)             | Der Wert, für den gilt: Die Wahrscheinlichkeit, dass$X$ kleiner oder gleich $x_p$ ist, beträgt $p$. (Percent Point Function)               |
| **Bernoulli-Experiment** (Bernoulli trial)             | Ein Zufallsexperiment mit genau zwei möglichen Ausgängen (z.B. Erfolg/Misserfolg).                                                               |

---

## 📐 Konzepte & Definitionen

### 1. Zufallsvariablen und Verteilungen

Um Zufallsereignisse mathematisch greifbar zu machen, ordnet man den Ereignissen (z. B. "Kopf" oder "Zahl") Zahlen zu ("Kopf" = 1, "Zahl" = 0). Die Zufallsvariable $X$ repräsentiert dieses unbestimmte Ergebnis. Die Wahrscheinlichkeitsverteilung beschreibt, wie wahrscheinlich die verschiedenen möglichen Werte von $X$ sind.

### 2. Diskrete Verteilungen im Überblick

| Verteilung                 | Notation                           | Typisches Beispiel                        | Parameter                                                              | Wesen                                                                                                          |
| -------------------------- | ------------------------------------------------ | ----------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Diskrete Uniform** | $X \sim dUni(low, high)$                       | Faires Würfeln ($low=1, high=6$)       | $low$, $high$ (inklusive Range in der Theorie, Exklusiv bei SciPy) | Alle Werte im Bereich sind exakt gleich wahrscheinlich.                                                        |
| **Bernoulli**        | $X \sim Bernoulli(p)$                          | Gezinkter Münzwurf (Kopf ist Erfolg)     | $p$ (Erfolgswk.)                                                     | Ein einzelnes Experiment mit Erfolg (1) oder Misserfolg (0).                                                   |
| **Binomial**         | $X \sim Binom(n, p)$                           | Anzahl Erfolge bei 10 Würfen             | $n$ (Versuche), $p$ (Erfolgswk.)                                   | Anzahl Erfolge bei$n$ unabhängigen Bernoulli-Experimenten.                                                  |
| **Geometrisch**      | $X \sim Geom(p)$                               | Anzahl Fehlversuche bis zum ersten Erfolg | $p$ (Erfolgswk.)                                                     | "Wie oft muss ich probieren, bis es klappt?" (inkl. dem Erfolgsversuch).                                       |
| **Poisson**          | $X \sim Poisson(\mu)$                          | Anrufe pro Stunde                         | $\mu$ (Erwartungswert)                                               | Wahrscheinlichkeit der Anzahl von Ereignissen in einem festen Zeit-/Raumintervall.                             |
| **Hypergeometrisch** | $X \sim Hyper(M, n, N)$                        | Rote Kugeln ziehen ohne Zurücklegen      | $M$ (Total), $n$ (Erfolge im Total), $N$ (Ziehungen)             | Wie Binomial, aber Ziehen**ohne** Zurücklegen (Wahrscheinlichkeit ändert sich, abhängige Ereignisse). |

### 3. Stetige Verteilungen im Überblick

Für stetige Verteilungen ist die Wahrscheinlichkeit für einen *exakten* Wert immer 0 ($P(X = c) = 0$). Wahrscheinlichkeiten existieren nur für Intervalle: $P(a \leq X \leq b) = \int_{a}^{b} f(x) dx$.

| Verteilung                 | Notation                             | Typisches Beispiel           | Parameter                                    | Wesen                                                           |
| -------------------------- | --------------------------------------------------- | ---------------------------- | -------------------------------------------- | --------------------------------------------------------------- |
| **Stetige Uniform**  | $X \sim sUni(loc, scale)$                         | Zufallszahl zwischen 0 und 1 | $loc$ (Start), $scale$ (Breite)          | Konstante Dichte im Intervall$[loc, loc+scale]$.              |
| **Exponential**      | $X \sim Exp(loc, scale)$                          | Lebensdauer einer Glühbirne | $loc$ (Minimum), $scale$ = $1/\lambda$ | Modelliert die Zeit zwischen unabhängigen Poisson-Ereignissen. |
| **Normalverteilung** | $X \sim Norm(loc, scale)$                         | Körpergrösse von Menschen  | $loc = \mu$, $scale = \sigma$            | Die wichtigste Verteilung. Symmetrische Glockenkurve.           |

---

## 🔢 Formeln & Rechenregeln

### Wahrscheinlichkeiten berechnen

Die kumulative Wahrscheinlichkeitsverteilung (CDF) ist der wichtigste Schlüssel für Intervall-Wahrscheinlichkeiten:

**Diskrete Variablen:**

- $P(X \leq k) = F(k)$ (Funktion `cdf(k)`)
- $P(X < k) = P(X \leq k-1) = F(k-1)$ (Funktion `cdf(k-1)`)
- $P(X \geq k) = 1 - P(X \leq k-1) = 1 - F(k-1)$ (oder `sf(k-1)`)
- $P(X = k) = P_{PMF}(k)$ (Funktion `pmf(k)`)
- $P(k_1 \leq X \leq k_2) = P(X \leq k_2) - P(X \leq k_1-1) = F(k_2) - F(k_1-1)$

> ⚠️ Bei diskreten Verteilungen ist es **extrem wichtig**, ob ein $\leq$ oder $<$ steht! Da Einzelwahrscheinlichkeiten echt grösser als $0$ sein können, macht z.B. $P(X \leq 5)$ vs. $P(X < 5)$ einen grossen Unterschied.

**Stetige Variablen:**

- $P(X \leq x) = P(X < x) = F(x)$ (Funktion `cdf(x)`)
- $P(X = x) = 0$ (immer!)
- $P(a \leq X \leq b) = P(a < X < b) = F(b) - F(a)$ (oder `cdf(b) - cdf(a)`)

> 💡 Bei stetigen Verteilungen sind $\leq$ und $<$ äquivalent. Die Intervall-Rechnung ist einfacher: "Obere Grenze CDF minus untere Grenze CDF".

---

## 📊 Vergleiche & Klassifizierungen

### Binomial- vs. Hypergeometrische Verteilung

Beide modellieren die Anzahl von "Erfolgen" bei mehreren Ziehungen/Versuchen.

- **Binomial:** Ziehen **mit** Zurücklegen. Die Versuche sind unabhängig, die Wahrscheinlichkeit $p$ bleibt konstant (z.B. mehrfacher Münzwurf).
- **Hypergeometrisch:** Ziehen **ohne** Zurücklegen. Die Versuche hängen voneinander ab, die Wahrscheinlichkeit ändert sich nach jedem Zug (z.B. Lotto, Urnenmodell).

### Die 4 zentralen Funktionen in SciPy (`scipy.stats`)

Alle Verteilungen in `scipy.stats` (wie `binom`, `norm`, `poisson` etc.) bieten dasselbe Interface:

| Funktion          | SciPy Methode                       | Input                   | Output                           | Was macht sie?                                                                         |
| ----------------- | ----------------------------------- | ----------------------- | -------------------------------- | -------------------------------------------------------------------------------------- |
| **PDF/PMF** | `.pdf(x)` / `.pmf(k)`           | Wert ($x, k$)         | Wahrscheinlichkeit (oder Dichte) | Berechnet$P(X = k)$ für diskrete $X$ (bzw. die Dichte für stetige $X$).        |
| **CDF**     | `.cdf(x)`                         | Wert ($x$)            | Wahrscheinlichkeit$p$          | Kumulative Wahrscheinlichkeit:$P(X \leq x)$.                                         |
| **PPF**     | `.ppf(p)`                         | Wahrscheinlichkeit$p$ | Quantilwert ($x$)              | Umkehrfunktion zur CDF. "Bis zu welchem$x$-Wert habe ich $p$% der Daten erreicht?" |
| **RVS**     | `.rvs(size=n)`                    | Anzahl$n$             | Array von Werten                 | Generiert Zufallszahlen, die dieser Verteilung folgen (Simulation).                    |
| **Weitere** | `.mean()`, `.var()`, `.std()` | -                       | Wert                             | Berechnet analytisch Erwartungswert, Varianz oder Standardabweichung.                  |

---

## 💻 Code-Beispiele (Python)

#### Konzept: Diskrete Uniformverteilung (Würfelwurf)

Ein sechsseitiger Würfel soll modelliert werden.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import randint

# Definieren der Variable: X ~ dUni(1, 6)
# ACHTUNG: scipy.stats.randint verlangt (low, high), wobei 'high' EXKLUSIVE ist!
X = randint(low=1, high=7)

# Wahrscheinlichkeit für Augenzahl 4: P(X=4)
print(X.pmf(4))  # 0.1666... (1/6)

# Wahrscheinlichkeit für höchstens 3: P(X <= 3)
print(X.cdf(3))  # 0.5 (3/6)

# Erwartungswert und Standardabweichung
print("Mu:", X.mean(), "Sigma:", X.std()) # 3.5 und ~1.707

# 10 zufällige Würfe generieren
print(X.rvs(size=10))
```

> ⚠️ **Falle:** In `scipy.stats.randint` ist das Parameter `high` offen (exklusiv), wie bei Listen-Slicing. Für einen 6-seitigen Würfel wählt man `low=1, high=7`.

---

#### Konzept: Binomialverteilung

Eine gezinkte Münze (KopfWahrscheinlichkeit 70%) wird 20-mal geworfen. $X$ = Anzahl geworfener "Köpfe".

```python
from scipy.stats import binom

# X ~ Binom(n=20, p=0.7)
X = binom(n=20, p=0.7)

# Genau 15 Köpfe: P(X = 15)
print(X.pmf(15)) # 0.1788...

# Höchstens 12 Köpfe: P(X <= 12)
print(X.cdf(12))

# Zwischen 10 und 15 Köpfen inkl.: P(10 <= X <= 15)
print(X.cdf(15) - X.cdf(9))

# 80%-Quantil: Welchen Wert unterschreitet man in 80% der Fälle?
print(X.ppf(0.8))
```

---

#### Konzept: Stetige Normalverteilung

Körpergrösse mit Mittelwert 170cm und Standardabweichung 10cm.

```python
from scipy.stats import norm

# X ~ Norm(loc=170, scale=10)
X = norm(loc=170, scale=10)

# Wahrscheinlichkeit kleiner als 185cm zu sein: P(X <= 185)
print(X.cdf(185))

# Wahrscheinlichkeit genau 185cm zu sein: P(X = 185) -> ist bei stetigen Variablen IMMER 0! 
# (X.pdf(185) gäbe hier die Wahrscheinlichkeitsdichte, NICHT die Wahrscheinlichkeit!)

# Wahrscheinlichkeit zwischen 160cm und 180cm: P(160 <= X <= 180)
print(X.cdf(180) - X.cdf(160))

# Welche Grösse trennt die grössten 5% ab? (Gesucht: 95%-Quantil)
print(X.ppf(0.95))
```

---

## 🔗 Konzept-Code-Zuordnung

| Verteilung       | SciPy Import                          | Instanziierung (Parameter)  | SciPy Argumente                                                  |
| ---------------- | ------------------------------------- | --------------------------- | ---------------------------------------------------------------- |
| Diskret Uniform  | `from scipy.stats import randint`   | `X = randint(low, high)`  | `low`, `high` (exklusiv)                                     |
| Bernoulli        | `from scipy.stats import bernoulli` | `X = bernoulli(p)`        | `p` (Wahrscheinlichkeit)                                       |
| Binomial         | `from scipy.stats import binom`     | `X = binom(n, p)`         | `n` (Anzahl), `p` (Wahrscheinlichkeit)                       |
| Geometrisch      | `from scipy.stats import geom`      | `X = geom(p)`             | `p` (Wahrscheinlichkeit)                                       |
| Poisson          | `from scipy.stats import poisson`   | `X = poisson(mu)`         | `mu` (Erwartungswert $\mu$)                                  |
| Hypergeometrisch | `from scipy.stats import hypergeom` | `X = hypergeom(M, n, N)`  | `M`(Pop-Grösse), `n`(Erfolge in Pop), `N`(Ziehung-Anzahl) |
| Stetig Uniform   | `from scipy.stats import uniform`   | `X = uniform(loc, scale)` | `loc`(Start), `scale`(Intervall-Breite)                      |
| Exponential      | `from scipy.stats import expon`     | `X = expon(loc, scale)`   | `loc`, `scale` (oft $= 1/\lambda$)                         |
| Normal           | `from scipy.stats import norm`      | `X = norm(loc, scale)`    | `loc`(Erwartungswert $\mu$), `scale`(Std-Abw $\sigma$)   |

---

## ✏️ Zusammenfassung der Aufgaben-Typen

Die Übungsaufgaben der Woche 04 basieren auf einem einheitlichen Muster für verschiedene Verteilungen (dUni, Bernoulli, Binomial, Geom, Poisson, Hypergeom, Uniform, Expon, Normal):

1. **Zufallsvariable definieren:** Mit entsprechendem SciPy-Befehl und korrekten Parametern (z.B. `X = binom(n=10, p=0.4)`).
2. **Visualisierung PDF/PMF und CDF:**
   - Ein Array von x-Werten (diskret mit `arange`, stetig mit `linspace`) erstellen.
   - PMF/PDF via `X.pmf(x)` bzw. `X.pdf(x)` zeichnen.
   - CDF via `X.cdf(x)` zeichnen.
   - Zufällige Samples via `X.rvs(size=...)` ziehen und ein Histogramm (`plt.hist` / `sns.histplot`) im Vergleich zur theoretischen Verteilung (`pmf/pdf`) plotten.
3. **Erwartungswert und Varianz/Std-Abw. berechnen:** Mit `X.mean()`, `X.var()` und `X.std()`.
4. **Wahrscheinlichkeiten ermitteln:**
   - Intervalle mit der CDF berechnen: $P(X \leq c)$ wird zu `X.cdf(c)`. Das Intervall $P(a < X < b)$ wird zu `X.cdf(b-1) - X.cdf(a)` bei diskreten Werten, bzw. `X.cdf(b) - X.cdf(a)` bei stetigen Werten.
5. **Quantile:**
   - Ein bestimmtes Quantil (z.B. 70%-Quantil) mit `X.ppf(0.7)` ermitteln.

---

## ⚠️ Prüfungsrelevante Hinweise

### Häufige Fehlerquellen & Fallstricke

| Falle                                           | Erklärung & Korrektur                                                                                                                                                                  |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $\leq$ vs. $<$ bei diskreten Verteilungen   | $P(X \leq k)$ ist nicht das Gleiche wie $P(X < k)$.  $P(X < k)$ bedeutet $P(X \leq k-1)$. Bei stetigen Verteilungen gibt es diesen Unterschied nicht.                           |
| Intervallgrenzen                                | $P(a \leq X \leq b)$ für **diskrete** Variablen wird gerechnet als `cdf(b) - cdf(a-1)`. Nicht `cdf(b) - cdf(a)`!                                                           |
| Einzelwahrscheinlichkeit stetig                 | $P(X = c)$ ist bei **stetigen** Verteilungen immer 0! `X.pdf(c)` gibt nur die Dichte an.                                                                                      |
| `scipy.stats.randint` Intervall               | Das obere Limit `high` ist **exklusiv**! Für einen Würfelwurf von 1 bis 6 ist `low=1, high=7`.                                                                              |
| Binomial vs. Hypergeometrisch                   | "Ohne Zurücklegen" = Hypergeometrisch. "Mit Zurücklegen" (oder unendlich grosse Population) = Binomial.                                                                               |
| Hypergeometrische Parameter `(M, n, N)`       | `M`: Gesamtanzahl Dinge in der Urne. `n`: Anzahl "Erfolgsdinger" in der Urne. `N`: Anzahl wie oft wir ziehen. (Oft inkonsistent in Büchern benannt, auf die SciPy Doku achten!). |
| Stetige Uniform Parametrierung `(loc, scale)` | Nicht verwechseln mit "Min" und "Max".`loc` ist das Minimum, aber `scale` ist die Intervall-**Breite** (Max - Min).                                                           |

### SC/MC-Hinweise: Typische Distraktoren

- ❌ "Die Wahrscheinlichkeit, dass ein stetig normalverteilter Mensch genau 185cm misst, ist 0.05" -> **FALSCH**: Sie ist 0. (Wahrscheinlichkeit eines Punktes bei stetigen Verteilungen ist immer 0).
- ❌ "Für $P(X \geq 5)$ bei einer Binomialverteilung rechnet man $1 - P(X \leq 5)$." -> **FALSCH**: Es heisst $1 - P(X \leq 4)$.
- ❌ "Die Dichtefunktion (PDF) liefert im Gegensatz zur CDF immer Werte zwischen 0 und 1." -> **FALSCH**: Die Wahrscheinlichkeits*dichte* kann (im Gegensatz zur Wahrscheinlichkeit) durchaus grösser als 1 sein. Nur das Integral (=Fläche unter der Kurve) muss exakt 1 ergeben. Die CDF hingegen liegt immer in $[0,1]$.
- ❌ "Verwenden Sie `X.pdf(4)` um bei der Poisson-Verteilung die Wahrscheinlichkeit für 4 Events zu berechnen." -> **FALSCH**: Poisson ist diskret, es heisst `X.pmf(4)`.

### Formeln für das A4-Blatt (unbedingt draufschreiben!)

| Formel / Befehl                                              | Grund                                         |
| ------------------------------------------------------------ | --------------------------------------------- |
| Intervall diskret:$P(a \leq X \leq b) = F(b) - F(a-1)$     | Verhindert den typischen "Off-by-one" Fehler. |
| Gegenwahrscheinlichkeit diskret:$P(X \geq k) = 1 - F(k-1)$ | "Mindestens k" -> 1 minus "höchstens k-1".   |
| `randint(low, high)`: $high$ ist exklusiv                | Sehr schnell vergessen in der Prüfung.       |
| $E(X) = \mu$, $Var(X) = \sigma^2$                        | SciPy:`.mean()`, `.var()`, `.std()`.    |

---

## 🔗 Verbindung zu vorherigen/folgenden Wochen

### Rückbezug zu SW 02 & SW 03

- **Erwartungswert und Varianz:** Was empirisch das Arithmetische Mittel ($\bar{x}$) und die Standardabweichung ($s$) gemäss SW 02 waren, sind in der theoretischen Modell-Sicht der Erwartungswert ($\mu$) und die theoretische Standardabweichung ($\sigma$).
- **Histogramme (SW 03):** Das Plotten von Zufalls-Samples (`X.rvs()`) als Histogramme (wie in SW 03 gelernt) wurde hier genutzt, um empirische Stichproben mit theoretischen PDF/PMF-Kurven abzugleichen. Verwendet wurde das Argument `stat="density"`, damit sich die Flächen zu 1 summieren.
