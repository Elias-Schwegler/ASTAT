# ASTAT – Probeprüfung: Lösungen

> Diese Lösungen sind als **Selbstkontrolle** gedacht. Bei Teil E (Erklärungen) sind die angegebenen Texte **Musterlösungen** – Ihre Antwort darf in der Formulierung abweichen, muss aber dieselben fachlichen Punkte abdecken.

---

# Teil A – Zuordnungen (12 Punkte)

## A1. Begriffe ↔ Definitionen (6 Punkte)

| Begriff | Buchstabe |
|---|:---:|
| 1. Bootstrap | **A** |
| 2. Konfidenzintervall (Mittelwert) | **B** |
| 3. Vorhersageintervall | **C** |
| 4. Permutationstest | **D** |
| 5. Confounder | **E** |
| 6. Pearson-Residuum | **F** |

**Eselsbrücke:** Bootstrap = mit Zurücklegen, Permutation = ohne Zurücklegen.

## A2. Python-Befehle ↔ Bedeutung (6 Punkte)

| Befehl | Buchstabe |
|---|:---:|
| 1. `df.sample(n, replace=True)` | **C** |
| 2. `binom.ppf(0.95, n=20, p=0.3)` | **B** |
| 3. `np.random.permutation(y)` | **D** |
| 4. `series.rank()` | **A** |
| 5. `scipy.optimize.minimize(f, x0=...)` | **E** |
| 6. `df.std(ddof=1)` | **F** |

**Falle:** `binom.ppf` ist die **inverse CDF** (Quantilfunktion). Sie liefert das kleinste $k$ mit $P(X \leqslant k) \geqslant q$.

---

# Teil B – Single Choice (14 Punkte)

| Frage | Antwort | Kurzbegründung |
|:---:|:---:|---|
| B1 | **b)** | $\frac{1}{n-1}$ ist erwartungstreu für die Stichprobenvarianz; `ddof=0` unterschätzt systematisch. **(c) ist falsch:** bei `df.corr()` kürzen sich die Faktoren weg. |
| B2 | **b)** | Diskrete Verteilung: $P(3 \leqslant X \leqslant 6) = F(6) - F(2)$. (a) lässt 3 weg. |
| B3 | **c)** | $\sigma/\sqrt{2n} = (1/\sqrt 2) \cdot \sigma/\sqrt{n}$. **Nicht** halbieren – das wäre nur bei Faktor 4. |
| B4 | **b)** | Bedingte Wahrscheinlichkeit unter $H_0$. **(a) ist die häufigste Falsche-Definition!** |
| B5 | **c)** | $r$ misst nur **lineare** Abhängigkeit (z.B. Parabel hat $r \approx 0$, ist aber abhängig). |
| B6 | **c)** | Zwei Parameter $\Rightarrow$ 2 Freiheitsgrade verloren. Bei multipler Regression mit $p$ Parametern: $n - p$. |
| B7 | **b)** | $\chi^2 = 0$ bedeutet **exakte** Übereinstimmung mit der Unabhängigkeitsannahme **in dieser Stichprobe** – nicht zwingend in der Grundgesamtheit. |

---

# Teil C – Multiple Choice (16 Punkte)

### C1. **a, b, d** richtig

- **a) ✓** `density=True`: Fläche unter dem Histogramm = 1.
- **b) ✓** Boxplot zeigt Median und Quartile, **nicht** den Mittelwert (manche Bibliotheken haben Optionen dafür, aber Standard nicht).
- **c) ✗** Bei rechtschiefer Verteilung: **Median links, Mittelwert rechts** (der Mittelwert wird durch den langen rechten Tail gezogen).
- **d) ✓** IQR ignoriert die obersten und untersten 25 % – damit immun gegen Ausreisser.

### C2. **a, d** richtig

- **a) ✓** Genau die Idee des Permutationstests.
- **b) ✗** Bootstrap ist **mit Zurücklegen**.
- **c) ✗** Klassische Falle: nicht-signifikant heisst **kein Beweis gegen** $H_0$, aber auch **kein Beweis für** $H_0$ ("absence of evidence is not evidence of absence").
- **d) ✓** Trade-off zwischen Typ-I- ($\alpha$) und Typ-II-Fehler ($\beta$).

### C3. **a, b, d** richtig

- **a) ✓** $C_{\text{korr}} \in [0, 1]$ für nominale Daten.
- **b) ✓** Rangzahlen sind robust gegen Ausreisser.
- **c) ✗** $|r|$ misst **die Güte** der Geraden-Anpassung, **nicht die Steigung**. Die Steigung ist $\hat a = r \cdot \sigma_y / \sigma_x$.
- **d) ✓** Drei klassische Quellen: Confounder, umgekehrte Wirkungsrichtung, Zufall/Selection-Bias.

### C4. **a, b, c, d** alle richtig

- **a) ✓** Vorhersageintervall enthält zusätzlich Streuung neuer Beobachtungen.
- **b) ✓** Liegt 0 ausserhalb des CI, ist der Effekt signifikant – äquivalent zum p-Wert-Test.
- **c) ✓** Höheres Konfidenzniveau → breiteres Intervall.
- **d) ✓** Definition des Vorhersageintervalls.

---

# Teil D – Code-Lesen (25 Punkte)

## D1. Pandas/NumPy (6 P)

**a) (2 P) Numerischer Wert für `result.loc["BE", "Streuung"]`:**

Bern: Mieten = [1700, 1800, 1950], $n = 3$.
$\bar x = (1700 + 1800 + 1950)/3 = 1816.\overline{6}$.
Abweichungen: $-116.\overline{6},\; -16.\overline{6},\; +133.\overline{3}$.
Quadrate: $13\,611.11,\; 277.78,\; 17\,777.78$. Summe: $31\,666.67$.
Mit `ddof=1` (Default in pandas): $s^2 = 31\,666.67 / 2 \approx 15\,833.33 \Rightarrow s \approx \boxed{125.83}$.

**b) (2 P)** `pandas.DataFrame.std()` verwendet **standardmässig `ddof=1`** – die erwartungstreue Stichproben-Standardabweichung. Mit `ddof=0` würde durch $n$ statt $n - 1$ geteilt → der Wert würde leicht **kleiner** ($\sqrt{31666.67/3} \approx 102.74$).

**c) (2 P)** Ohne `.rename(...)` heisst die Spalte **`std`** statt `Streuung`. `print(result.loc["BE", "Streuung"])` würde dann **mit `KeyError: 'Streuung'`** fehlschlagen, weil die Spalte unter dem alten Namen existiert. Korrekt wäre `result.loc["BE", "std"]`.

---

## D2. scipy.stats Binomialverteilung (7 P)

Mit $X \sim \text{Bin}(n = 12, p = 0.25)$:

| Var | Inhalt (in Worten) |
|:---:|---|
| **A** | $P(X = 3)$ – Wahrscheinlichkeit für **genau 3 Erfolge** |
| **B** | $P(X \leqslant 3) - P(X \leqslant 0) = P(1 \leqslant X \leqslant 3)$ – Erfolge im Intervall **1 bis 3** |
| **C** | $1 - P(X \leqslant 4) = P(X \geqslant 5)$ – mindestens **5 Erfolge** |
| **D** | $0.5$-Quantil = **Median**: kleinstes $k$ mit $P(X \leqslant k) \geqslant 0.5$ (hier $k = 3$, da $E[X] = 3$ und Verteilung leicht rechtschief) |

**e) (1 P)** $\texttt{binom.cdf(0, n, p)} = P(X \leqslant 0) = P(X = 0) = (1 - p)^n = 0.75^{12} \approx 0.0317$ – **nicht null**, weil $X = 0$ mit positiver Wahrscheinlichkeit auftreten kann. Vergessen würde $X = 0$ fälschlicherweise zum Intervall hinzugezählt.

---

## D3. Permutationstest (6 P)

**a) (2 P)**
- $H_0$: Die beiden Gruppen `group_A` und `group_B` haben **dieselbe Verteilung** – die Gruppenzugehörigkeit hat **keinen Effekt** auf das Merkmal. Insbesondere: $\mathbb{E}[A] = \mathbb{E}[B]$.
- $H_1$: Die Gruppen unterscheiden sich, $\mathbb{E}[A] \neq \mathbb{E}[B]$.

**b) (2 P)** `pool_shuffled` ist eine **zufällige Permutation aller Werte ohne Zurücklegen**. Anschliessend werden die ersten $n_a$ Werte als "neue Gruppe A" und der Rest als "neue Gruppe B" deklariert. Dies simuliert die Welt unter $H_0$, **in der die Gruppenzugehörigkeit egal ist**: jede beliebige Aufteilung wäre gleich plausibel. Die so entstehende Verteilung der Mittelwertsdifferenzen ist genau die **Permutationsverteilung der Teststatistik unter $H_0$**.

**c) (1 P)** **Zweiseitig.** Erkennbar an `np.abs(diff_perm) >= np.abs(diff_obs)` – beide Richtungen werden als "extrem" gezählt.

**d) (1 P)** $p = 0.0123 = 1.23\,\%$: **Falls $H_0$ wahr wäre**, würden in nur etwa 1.23 % der Permutationen eine Mittelwertsdifferenz von absolut 4.7 oder mehr auftreten. Da $p < 0.05$, **verwerfen** wir $H_0$ auf dem 5 %-Niveau – die beobachtete Differenz ist signifikant.

---

## D4. Lineare Regression mit `minimize` (6 P)

**a) (2 P)**
- `fit.x` = NumPy-Array $[\hat a, \hat b]$ mit den **optimalen Parametern** (Argumenten), die das Minimum erzeugen.
- `fit.fun` = der **Funktionswert am Minimum**, hier also der minimale Wert von $\mathsf{RSS}$.

**b) (2 P)**

| Zeile | Grösse | Formel |
|---|---|---|
| `print(fit.fun)` | **RSS** (Residuenquadratsumme) | $\mathsf{RSS} = \sum (y_i - \hat y_i)^2$ |
| `print(np.sqrt(fit.fun / (len(X) - 2)))` | **RSE** (Residual Standard Error) | $\mathsf{RSE} = \sqrt{\mathsf{RSS}/(n - 2)}$ |
| `print(model(X, a_hat, b_hat).var() / Y.var())` | **$R^2$** (Bestimmtheitsmass) | $R^2 = \frac{\mathrm{Var}(\hat y)}{\mathrm{Var}(y)}$ |

**c) (2 P)** Beim **linearen Modell** ist $\mathsf{RSS}$ eine **konvexe** quadratische Funktion in $(a, b)$ – es gibt nur **ein globales Minimum**, der Optimierer findet es praktisch unabhängig vom Startwert. Ein **schlechter** Startwert (z.B. weit vom Optimum) könnte höchstens mehr Iterationen benötigen.

Bei einem **nichtlinearen Modell** (z.B. $a \cdot e^{bx} + c$) gilt das **nicht mehr**: $\mathsf{RSS}$ kann **mehrere lokale Minima** haben. Ein schlechter Startwert kann den Optimierer in ein **lokales** statt globales Minimum führen → falsche Parameter, schlechtes Modell. Daher: bei nichtlinearen Modellen vernünftige Startwerte aus Vorabschätzungen oder mehrere Startwerte ausprobieren.

---

# Teil E – Kurzerklärungen (Musterlösungen, 23 Punkte)

## E1. Stichprobenverteilung vs. Datenverteilung (4 P)

Die **Datenverteilung** beschreibt, wie die einzelnen Beobachtungen $x_1, \ldots, x_n$ in einer Stichprobe verteilt sind – sie kann beliebig schief, mehrgipflig oder mit Ausreissern behaftet sein. Die **Stichprobenverteilung** des Mittelwerts hingegen ist die Verteilung **der Statistik** $\bar X$ über alle möglichen Stichproben gleicher Grösse aus derselben Grundgesamtheit. Diese Stichprobenverteilung wird mit grösserem $n$ **schmaler** (Standardfehler $\sigma/\sqrt n$) und tendiert **gegen eine Normalverteilung** (Zentraler Grenzwertsatz), unabhängig davon, wie die Datenverteilung selbst aussieht. Praktisch wichtig: Konfidenzintervalle und Hypothesentests basieren auf der **Stichprobenverteilung**, nicht auf der Datenverteilung. Schon bei stark schiefen Originaldaten liefern Mittelwerts-Schätzer mit moderatem $n$ verlässliche Inferenz.

## E2. Zentraler Grenzwertsatz (5 P)

Der **Zentrale Grenzwertsatz (CLT)** besagt: Für unabhängige, identisch verteilte Zufallsvariablen $X_1, \ldots, X_n$ mit endlichem Erwartungswert $\mu$ und endlicher Varianz $\sigma^2$ konvergiert die Verteilung des standardisierten Stichprobenmittelwerts $\sqrt n \cdot (\bar X_n - \mu)/\sigma$ mit $n \to \infty$ gegen die **Standardnormalverteilung** $\mathcal N(0, 1)$ – **unabhängig von der ursprünglichen Verteilung**. Voraussetzungen sind im Wesentlichen Unabhängigkeit, identische Verteilung und endliche Varianz. Praktisch nützlich ist der Satz, weil er es erlaubt, Mittelwerts-Statistiken **wie normalverteilt zu behandeln**, sobald $n$ moderat gross ist (Faustregel: $n \geqslant 30$). Daraus folgen $z$- und $t$-basierte Konfidenzintervalle und Tests, ohne die Originaldaten als normalverteilt voraussetzen zu müssen. Er ist die **theoretische Brücke** zwischen Realdaten (oft nicht normalverteilt) und der Inferenz mit der Normalverteilung.

## E3. Korrelation ≠ Kausalität (4 P)

Korrelation misst nur die **statistische Tendenz**, dass zwei Merkmale gemeinsam variieren. Eine kausale Beziehung erfordert hingegen, dass eine Veränderung in $X$ tatsächlich eine Veränderung in $Y$ **bewirkt** – das lässt sich nur durch Experimente oder fundiertes Fachwissen klären, nicht aus Beobachtungsdaten allein. Drei Quellen für hohe Korrelation **ohne** Kausalität: Confounder, umgekehrte Wirkungsrichtung, Zufall.

**Beispiel mit Confounder:** In einer Stadt korrelieren `Anzahl Kirchen` und `Anzahl Verbrechen` stark positiv (mit dem Argument: "Kirchen verursachen Verbrechen?"). Der Confounder ist die **Stadtgrösse**: grössere Städte haben mehr Einwohner – damit sowohl mehr Kirchen als auch (in absoluten Zahlen) mehr Verbrechen. Die Korrelation verschwindet, sobald man auf die Bevölkerungszahl normiert.

## E4. 95%-Konfidenzintervall – wirklich (4 P)

**Korrekt ist (ii):** "Wenn wir das Experiment sehr oft wiederholen, würden 95 % der so berechneten Intervalle das wahre $\mu$ enthalten."

Statement (i) ist im **klassischen (frequentistischen) Sinn falsch**, weil $\mu$ kein Zufallsobjekt ist – es ist ein **fester (aber unbekannter) Wert**. Das berechnete Intervall ist hingegen zufällig, weil es von der Stichprobe abhängt. Ein konkretes Intervall enthält $\mu$ **entweder** (Wahrscheinlichkeit 1) **oder eben nicht** (Wahrscheinlichkeit 0) – die "95 %" beschreibt die **langfristige Trefferquote der Methode**, nicht die Wahrscheinlichkeit für ein einzelnes Intervall.

(Im bayesianischen Rahmen mit Posterior-Verteilung wäre Aussage (i) zulässig, dort heisst das Konstrukt aber "Credible Interval", nicht "Confidence Interval".)

## E5. Pearson vs. Spearman (3 P)

**Situation 1 – Ausreisser:** Wenn der Datensatz einzelne extreme Werte enthält, die die Pearson-Schätzung dominieren, liefert Spearman robustere Ergebnisse. Beispiel: Einkommen × Zufriedenheit, wo ein einzelner Milliardär den Pearson-$r$ stark verzerrt, während Ränge unverändert bleiben.

**Situation 2 – Monoton, aber nicht linear:** Wenn der wahre Zusammenhang **monoton, aber gekrümmt** ist (z.B. exponentiell oder logarithmisch), unterschätzt Pearson die tatsächliche Stärke des Zusammenhangs. Spearman erkennt monotone Beziehungen unabhängig von der Form. Beispiel: Lerndauer × Prüfungsleistung mit Sättigungsverhalten.

(Bonusbeispiel: Wenn mindestens eines der Merkmale **nur ordinal** ist, ist Pearson formal gar nicht anwendbar – nur Spearman.)

## E6. Bestimmtheitsmass $R^2$ (3 P)

$R^2$ ist das Verhältnis der **vom Modell erklärten Streuung** ($\mathrm{Var}(\hat y)$) zur **Gesamtstreuung der Zielgrösse** ($\mathrm{Var}(y)$):

$$R^2 = \frac{\mathrm{Var}(\hat y)}{\mathrm{Var}(y)}, \qquad 0 \leqslant R^2 \leqslant 1.$$

In der **linearen Einfachregression** gilt $R^2 = r^2$, wobei $r$ der Pearson-Korrelationskoeffizient zwischen $X$ und $Y$ ist – $R^2$ und $r$ enthalten dieselbe Information, nur dass $R^2$ keine Richtungsinformation hat (immer positiv).

- $R^2 = 1$: Modell erklärt die **gesamte** Streuung – alle Punkte liegen exakt auf der Regressionsgeraden.
- $R^2 = 0$: Modell erklärt **nichts** – Vorhersagen sind nicht besser als der reine Mittelwert $\bar y$.

Wichtige Einschränkung: $R^2$ misst nur die **In-Sample-Anpassung** und sagt nichts über Kausalität, Generalisierung oder Modellgültigkeit aus.

---

# Teil F – Anwendungsaufgabe (10 Punkte)

## F1. (2 P) Stadt × Energieklasse

**Mass:** Korrigierter Kontingenzkoeffizient $C_{\text{korr}}$ (beide nominal/ordinal mit wenigen Kategorien → Kontingenztafel-Ansatz).
**Visualisierung:** **Gestapeltes Stabdiagramm** (relative Häufigkeiten der Energieklassen pro Stadt) – zeigt direkt, ob die Verteilung der Energieklassen sich über die Städte unterscheidet.

## F2. (2 P) Quadratmeter × Miete

**Koeffizient:** **Pearson** $r$ – beide Merkmale metrisch und linearer Zusammenhang plausibel.
**Interpretation $r = 0.78$:** Starker positiver linearer Zusammenhang; rund $r^2 \approx 61\,\%$ der Streuung der Miete lassen sich durch die Quadratmeter linear erklären. Höhere $m^2$ → tendenziell höhere Miete, aber **keine** kausale Aussage.

## F3. (2 P) Mittlere Miete LU vs. ZH signifikant unterschiedlich?

**Verfahren:** **Permutationstest auf die Differenz der Mittelwerte** (oder klassischer t-Test, falls Normalannahme akzeptabel).
**Begründung:** Permutationstest ist verteilungsfrei – wir benötigen keine Normalverteilungs-Annahme, was bei Mietpreisen mit langem rechten Tail wichtig ist. $H_0$: $\mathbb E[\text{Miete}_{LU}] = \mathbb E[\text{Miete}_{ZH}]$. Die Stadtzugehörigkeit wird viele Male permutiert und der p-Wert aus der Verteilung der Mittelwertsdifferenzen abgeleitet.

## F4. (2 P) Vorhersage für 80 m²-Wohnung in Bern

**Intervall:** **Vorhersageintervall** (Prediction Interval).
**Begründung:** Wir wollen den Bereich, in dem **eine konkrete neue Wohnung** mit 95 % Wahrscheinlichkeit liegen wird – nicht den Bereich des wahren Mittelwerts der Mietpreise aller 80 m²-Wohnungen. Das Konfidenzintervall des Mittelwerts ist viel zu schmal, weil es die zufällige Streuung **einzelner** Wohnungen um die Regressionsgerade nicht enthält. Berechnung über Bootstrap: Resample → Modell → Punktvorhersage **+ zufällig gewähltes Residuum** → Quantile.

## F5. (2 P) Confounder für Energieklasse → Miete

Zwei plausible Confounder:

1. **Baujahr:** Neuere Gebäude haben sowohl bessere Energieklassen als auch (oft) höhere Mieten wegen modernerer Ausstattung, Lage in neuen Quartieren usw.
2. **Lage / Stadt:** Innenstadtbereiche oder gefragte Quartiere haben sowohl strenger durchgesetzte Energievorgaben (Sanierungsdruck, Neubauten) als auch höhere Mieten – die Stadt verursacht beides gleichzeitig.

(Weitere Möglichkeiten: Quadratmeter, Eigentümertyp – institutionelle Vermieter sanieren systematischer und verlangen marktübliche bzw. höhere Mieten.)

Die kausale Aussage "Energieklasse → höhere Miete" lässt sich aus Beobachtungsdaten allein **nicht belegen**; es bräuchte eine kontrollierte Studie oder zumindest eine Adjustierung für die Confounder mittels multipler Regression.

---

# Punkteverteilung (zur Selbstkontrolle)

| Teil | Aufgabe | Punkte | Ihre Punkte |
|:---:|:---:|:---:|:---:|
| A | A1 | 6 | ___ |
| A | A2 | 6 | ___ |
| B | B1–B7 | 14 | ___ |
| C | C1–C4 | 16 | ___ |
| D | D1 | 6 | ___ |
| D | D2 | 7 | ___ |
| D | D3 | 6 | ___ |
| D | D4 | 6 | ___ |
| E | E1–E6 | 23 | ___ |
| F | F1–F5 | 10 | ___ |
| | **Total** | **100** | ___ |

**Notenrichtwerte (HSLU-üblich):**

| Punkte | Note |
|:---:|:---:|
| 90–100 | 6 |
| 80–89 | 5.5 |
| 70–79 | 5 |
| 60–69 | 4.5 |
| 50–59 | 4 (Bestanden) |
| < 50 | < 4 |

---

**Tipp für die echte Prüfung:** Was Sie auf Ihrem A4-Spick **wirklich** brauchen, ist nicht eine Formelliste zum Abschreiben, sondern:

1. **Entscheidungsbäume** ("nominal → $C_{\text{korr}}$, ordinal → Spearman, metrisch → Pearson").
2. **Trap-Liste** ("$r = 0$ heisst nicht unabhängig", "p-Wert ist nicht $P(H_0)$").
3. **Code-Skelette** für Bootstrap und Permutation – die Logik ist wichtiger als die Syntax.
4. **Formel-Beziehungen** ($R^2 = r^2$, $\hat a = r \cdot \sigma_y / \sigma_x$, $n - 2$ wegen 2 Parametern).
