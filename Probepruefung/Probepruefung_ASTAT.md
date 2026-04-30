# ASTAT – Probeprüfung

**Modul:** Angewandte Statistik für Datenwissenschaften
**Dauer:** 120 Minuten
**Hilfsmittel:** Eine handgeschriebene A4-Seite (Vor- und Rückseite), Taschenrechner
**Maximale Punktzahl:** 100 Punkte
**Stoff:** SW 01 – SW 11 (alle Themen des Moduls)

---

## Hinweise

- Bei **Single Choice (SC)** ist genau eine Antwort richtig.
- Bei **Multiple Choice (MC)** sind null bis vier Antworten richtig. Pro Teilantwort gibt es 1 Punkt – falsche Kreuze führen zu Punktabzug bis Minimum 0 für die Aufgabe.
- Bei **Erklärungs-Aufgaben** wird sowohl die fachliche Korrektheit als auch eine **eigenständige, klare Formulierung** bewertet. Stichworte allein genügen nicht.
- Code-Aufgaben prüfen das **Lesen und Verstehen**, nicht das Schreiben. Schreiben Sie keine eigenen Code-Lösungen, sondern beschreiben Sie, was der Code tut.
- Notieren Sie Zwischenrechnungen sichtbar – Teilpunkte werden vergeben.

---

## Zeitempfehlung

| Teil | Inhalt | Punkte | Empf. Zeit |
|:---:|:---|:---:|:---:|
| A | Zuordnungen | 12 | 15 min |
| B | Single Choice | 14 | 15 min |
| C | Multiple Choice | 16 | 20 min |
| D | Code-Lesen | 25 | 35 min |
| E | Kurzerklärungen | 23 | 25 min |
| F | Anwendungsaufgabe | 10 | 10 min |
| | **Total** | **100** | **120 min** |

---

# Teil A – Zuordnungen (12 Punkte)

## A1. Begriffe ↔ Definitionen (6 Punkte)

Ordnen Sie jedem Begriff die passende Definition zu (jede Definition wird genau einmal verwendet).

| Begriff | Buchstabe |
|---|---|
| 1. **Bootstrap** | ___ |
| 2. **Konfidenzintervall (Mittelwert)** | ___ |
| 3. **Vorhersageintervall** | ___ |
| 4. **Permutationstest** | ___ |
| 5. **Confounder** | ___ |
| 6. **Pearson-Residuum** ($\chi^2$-Kontext) | ___ |

| Buchstabe | Definition |
|:---:|---|
| **A** | Resampling **mit Zurücklegen** aus der Stichprobe zur Schätzung von Standardfehlern und Intervallen |
| **B** | Bereich, der bei wiederholten Stichproben mit angegebener Wahrscheinlichkeit den **wahren Parameter** enthält |
| **C** | Bereich, in dem mit angegebener Wahrscheinlichkeit eine **einzelne neue Beobachtung** liegen wird |
| **D** | Resampling-Test, bei dem die Daten **ohne Zurücklegen** umgemischt werden, um eine $H_0$-Verteilung zu erzeugen |
| **E** | Dritte Variable, die einen scheinbaren Zusammenhang zwischen zwei Merkmalen erzeugt |
| **F** | Normalisierter Beitrag einer Zelle: $(n_b - n_e)^2 / n_e$ |

---

## A2. Python-Befehle ↔ Bedeutung (6 Punkte)

Ordnen Sie jedem Befehl seine Beschreibung zu.

| Befehl | Buchstabe |
|---|---|
| 1. `df.sample(n, replace=True)` | ___ |
| 2. `binom.ppf(0.95, n=20, p=0.3)` | ___ |
| 3. `np.random.permutation(y)` | ___ |
| 4. `series.rank()` | ___ |
| 5. `scipy.optimize.minimize(f, x0=...)` | ___ |
| 6. `df.std(ddof=1)` | ___ |

| Buchstabe | Beschreibung |
|:---:|---|
| **A** | Vergibt jedem Wert seine Position in der sortierten Liste (mit Bindungen → Mittel der Plätze) |
| **B** | Liefert das **kleinste $k$**, für das $P(X \leqslant k) \geqslant 0.95$ bei $\text{Bin}(20; 0.3)$ – inverse CDF |
| **C** | Zieht $n$ Zeilen **mit Zurücklegen** – Bootstrap-Resample |
| **D** | Mischt die Werte zufällig **ohne Zurücklegen** um – Permutationstest |
| **E** | Numerische Minimierung einer Funktion – findet z.B. OLS-Parameter |
| **F** | Stichproben-Standardabweichung mit Korrektur $1/(n-1)$ |

---

# Teil B – Single Choice (14 Punkte, je 2 Punkte)

Markieren Sie **genau eine** Antwort.

### B1. (SW02 / SW06) Welche Aussage über `ddof` ist korrekt?
- [ ] **a)** `ddof=0` ist immer richtig, weil es die "echte" Standardabweichung ist.
- [ ] **b)** `ddof=1` korrigiert die Unterschätzung der Varianz und liefert die **erwartungstreue** Stichproben-Standardabweichung.
- [ ] **c)** Bei `df.corr()` muss man `ddof=1` setzen, sonst stimmt die Korrelation nicht.
- [ ] **d)** `ddof=1` ist nur sinnvoll bei $n < 30$.

---

### B2. (SW04) Bei $X \sim \text{Bin}(n=10, p=0.4)$ wollen Sie $P(3 \leqslant X \leqslant 6)$ berechnen. Welcher Ausdruck ist **korrekt**?
- [ ] **a)** `binom.cdf(6, 10, 0.4) - binom.cdf(3, 10, 0.4)`
- [ ] **b)** `binom.cdf(6, 10, 0.4) - binom.cdf(2, 10, 0.4)`
- [ ] **c)** `binom.pmf(6, 10, 0.4) - binom.pmf(3, 10, 0.4)`
- [ ] **d)** `binom.cdf(7, 10, 0.4) - binom.cdf(3, 10, 0.4)`

---

### B3. (SW05 / SW06) Sie verdoppeln die Stichprobengrösse $n$. Wie verhält sich der **Standardfehler des Mittelwerts** $\sigma_{\bar x} = \sigma / \sqrt n$?
- [ ] **a)** Halbiert sich.
- [ ] **b)** Bleibt gleich, weil $\sigma$ unverändert.
- [ ] **c)** Wird um den Faktor $1/\sqrt 2 \approx 0.707$ kleiner.
- [ ] **d)** Verdoppelt sich.

---

### B4. (SW07) Welche Definition des **p-Werts** ist korrekt?
- [ ] **a)** Die Wahrscheinlichkeit, dass $H_0$ wahr ist.
- [ ] **b)** Die Wahrscheinlichkeit, ein Resultat **mindestens so extrem** wie das beobachtete zu erhalten, **falls $H_0$ wahr wäre**.
- [ ] **c)** Die Wahrscheinlichkeit, $H_1$ irrtümlich abzulehnen.
- [ ] **d)** $1 - \alpha$, wenn $H_0$ verworfen wird.

---

### B5. (SW10) Welche Aussage gilt, wenn der **Pearson-Korrelationskoeffizient** $r = 0$ ist?
- [ ] **a)** Die zwei Merkmale sind unabhängig.
- [ ] **b)** Die zwei Merkmale haben **keinen Zusammenhang** überhaupt.
- [ ] **c)** Es gibt **keinen linearen** Zusammenhang – ein nicht-linearer Zusammenhang bleibt möglich.
- [ ] **d)** Die Kovarianz ist genau dann ebenfalls 0, wenn die Mittelwerte gleich sind.

---

### B6. (SW11) Warum wird in $\mathsf{RSE} = \sqrt{\mathsf{RSS}/(n - 2)}$ durch $n - \textcolor{red}{2}$ und nicht durch $n$ geteilt?
- [ ] **a)** Damit das Resultat positiv ist.
- [ ] **b)** Weil zwei Datenpunkte für die Schätzung nicht verwendet werden.
- [ ] **c)** Weil **zwei Parameter** ($\hat a, \hat b$) aus den Daten geschätzt werden – jede Schätzung verbraucht einen Freiheitsgrad.
- [ ] **d)** Aus historischen Konventionsgründen ohne mathematische Begründung.

---

### B7. (SW09) In einer 3×4-Kontingenztafel ergibt der $\chi^2$-Wert 0. Was bedeutet das?
- [ ] **a)** Es gibt **gar keinen** Zusammenhang zwischen den Merkmalen.
- [ ] **b)** Beobachtete und erwartete Häufigkeiten sind in **allen Zellen identisch** – die Merkmale sind in dieser Stichprobe **exakt unabhängig**.
- [ ] **c)** Der Test ist nicht aussagekräftig.
- [ ] **d)** $C_{\text{korr}} = 1$ – maximaler Zusammenhang.

---

# Teil C – Multiple Choice (16 Punkte, je 4 Punkte)

Mehrere Antworten können richtig sein. Markieren Sie alle zutreffenden.

### C1. (SW03 / SW02) Welche Aussagen über **Histogramme und Boxplots** sind korrekt?
- [ ] **a)** Ein Histogramm mit `density=True` zeigt **Flächendichte** – die Summe der Balkenhöhen mal Balkenbreite ergibt 1.
- [ ] **b)** Ein Boxplot zeigt **Median, Quartile (Q1, Q3)** und Ausreisser, aber nicht den Mittelwert.
- [ ] **c)** Bei rechtschiefen Daten liegt der **Median rechts vom Mittelwert**.
- [ ] **d)** Der Quartilsabstand (IQR) $= Q_3 - Q_1$ ist **robust gegen Ausreisser**.

---

### C2. (SW07 / SW08) Welche Aussagen über **Resampling-Tests** sind korrekt?
- [ ] **a)** Ein **Permutationstest** zerstört absichtlich den Zusammenhang zwischen zwei Merkmalen, indem die Werte einer Spalte umgemischt werden.
- [ ] **b)** Beim **Bootstrap** wird ohne Zurücklegen aus der Stichprobe gezogen.
- [ ] **c)** Ein **nicht-signifikanter** p-Wert beweist, dass $H_0$ wahr ist.
- [ ] **d)** Mit einem **kleineren Signifikanzniveau** $\alpha$ steigt die Gefahr eines **Typ-II-Fehlers** (echten Effekt nicht erkennen).

---

### C3. (SW09 / SW10) Welche Aussagen zum Thema **Zusammenhang** sind korrekt?
- [ ] **a)** Der korrigierte Kontingenzkoeffizient $C_{\text{korr}}$ liegt zwischen $0$ und $1$ und gilt für **nominale** Merkmale.
- [ ] **b)** **Spearman** ist robuster gegen Ausreisser als Pearson, weil er auf Rangzahlen statt Werten arbeitet.
- [ ] **c)** Der Betrag $|r|$ gibt die **Steigung** der Regressionsgeraden an.
- [ ] **d)** Eine **Scheinkorrelation** kann durch einen Confounder, eine umgekehrte Wirkungsrichtung oder durch reinen Zufall (kleine Stichprobe) entstehen.

---

### C4. (SW06 / SW11) Welche Aussagen zu **Konfidenz- und Vorhersageintervall** sind korrekt?
- [ ] **a)** Ein 95%-**Vorhersageintervall** ist immer **breiter** als ein 95%-**Konfidenzintervall** für den Mittelwert am gleichen $x$.
- [ ] **b)** Liegt das 95%-Konfidenzintervall für $\hat a$ **vollständig oberhalb von 0**, ist der Prädiktor auf dem 5%-Niveau **signifikant**.
- [ ] **c)** Das **99%-Konfidenzintervall** ist breiter als das 95%-Konfidenzintervall.
- [ ] **d)** Das Vorhersageintervall berücksichtigt **zusätzlich** zur Schätzunsicherheit die zufällige Streuung neuer Beobachtungen.

---

# Teil D – Code-Lesen (25 Punkte)

Beschreiben Sie, was der jeweilige Code-Block tut. **Schreiben Sie keinen eigenen Code**, sondern erklären Sie das Verhalten.

### D1. (6 Punkte) – Pandas/NumPy (SW01 / SW02)

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Stadt":  ["LU", "LU", "ZH", "ZH", "BE", "BE", "BE"],
    "Miete":  [1850, 2100, 2900, 3050, 1700, 1800, 1950],
    "Zimmer": [3, 4, 3, 4, 2, 3, 4],
})

result = (df.groupby("Stadt")["Miete"]
            .agg(["mean", "std"])
            .rename(columns={"mean": "Mittelwert", "std": "Streuung"}))

print(result.loc["BE", "Streuung"])
```

Beantworten Sie:

**a) (2 P)** Welcher numerische Wert wird ausgegeben? (Berechnung sichtbar.)

**b) (2 P)** Welche `ddof`-Konvention verwendet `pandas.DataFrame.std()` standardmässig? Was würde sich ändern, wenn man `ddof=0` setzt?

**c) (2 P)** Was passiert, wenn man die Zeile `.rename(...)` weglässt? Würde der `print()` weiterhin funktionieren? Begründen Sie.

---

### D2. (7 Punkte) – scipy.stats Binomialverteilung (SW04)

```python
from scipy.stats import binom

n, p = 12, 0.25

A = binom.pmf(3, n, p)
B = binom.cdf(3, n, p) - binom.cdf(0, n, p)
C = 1 - binom.cdf(4, n, p)
D = binom.ppf(0.5, n, p)
```

Beantworten Sie für **jede** der vier Variablen `A`, `B`, `C`, `D` (je 1.5 P, plus 1 P für eine Falle):

**a)–d) (6 P)** Welches Ereignis bzw. welche Grösse berechnet jeder Ausdruck **inhaltlich** (in der Sprache der Wahrscheinlichkeit, nicht in Code)?

**e) (1 P)** In `B` steht $-\,\texttt{binom.cdf(0, n, p)}$ statt nichts. Warum ist dieser Subtrahend hier **nicht** $0$, obwohl $X \geqslant 0$ immer gilt?

---

### D3. (6 Punkte) – Permutationstest (SW07)

```python
import numpy as np

n_perm = 10_000
diff_obs = group_A.mean() - group_B.mean()    # = 4.7

pool = np.concatenate([group_A, group_B])
n_a = len(group_A)

diff_perm = np.empty(n_perm)
for i in range(n_perm):
    pool_shuffled = np.random.permutation(pool)
    a_new = pool_shuffled[:n_a]
    b_new = pool_shuffled[n_a:]
    diff_perm[i] = a_new.mean() - b_new.mean()

p_value = np.mean(np.abs(diff_perm) >= np.abs(diff_obs))
```

**a) (2 P)** Welche **Nullhypothese** $H_0$ wird hier getestet? Welche Alternativhypothese $H_1$?

**b) (2 P)** Wofür wird `pool_shuffled` benötigt? Warum funktioniert dies, um die Verteilung **unter $H_0$** zu erzeugen?

**c) (1 P)** Ist der Test **einseitig** oder **zweiseitig**? Woran erkennt man das?

**d) (1 P)** Bei `p_value = 0.0123` – was bedeutet dieser Wert konkret im Kontext der Aufgabe?

---

### D4. (6 Punkte) – Lineare Regression mit `minimize` (SW11)

```python
from scipy.optimize import minimize
import numpy as np

X = df["Quadratmeter"].values
Y = df["Miete"].values

def model(x, a, b):
    return a * x + b

def RSS(p):
    return np.sum((Y - model(X, p[0], p[1]))**2)

fit = minimize(RSS, x0=np.array([10.0, 500.0]))

a_hat, b_hat = fit.x
print(fit.fun)
print(np.sqrt(fit.fun / (len(X) - 2)))
print(model(X, a_hat, b_hat).var() / Y.var())
```

**a) (2 P)** Was bedeuten `fit.x` und `fit.fun`? Geben Sie für **beides** eine kurze, präzise Erklärung in Worten.

**b) (2 P)** Welche **drei statistischen Grössen** werden durch die drei `print()`-Zeilen ausgegeben? Benennen Sie sie und schreiben Sie die zugehörige Formel daneben.

**c) (2 P)** Der Optimierer wird mit `x0 = [10.0, 500.0]` gestartet. Was wäre ein **schlechter** Startwert und welches Problem könnte daraus entstehen? Gilt das gleiche Argument auch bei einem nicht-linearen Modell?

---

# Teil E – Kurzerklärungen (23 Punkte)

Schreiben Sie **eigenständige, vollständige Sätze**. Stichpunktlisten allein reichen nicht. Empfohlene Länge: 4–8 Zeilen pro Antwort.

> **Hinweis:** Diese Aufgaben eignen sich zum Selbsttest – Sie können Ihre Antworten zur Prüfung an Claude geben (Hinweis am Ende des Dokuments).

### E1. (4 P) (SW05 / SW06) **Stichprobenverteilung vs. Datenverteilung**
Erklären Sie den Unterschied zwischen der **Datenverteilung** (Verteilung der Einzelwerte in einer Stichprobe) und der **Stichprobenverteilung** des Mittelwerts. Warum ist diese Unterscheidung praktisch wichtig?

---

### E2. (5 P) (SW06) **Zentraler Grenzwertsatz**
Formulieren Sie den **Zentralen Grenzwertsatz** in eigenen Worten. Welche Voraussetzungen müssen erfüllt sein? Warum macht er die Normalverteilung so zentral für die Statistik – auch wenn die Originaldaten **nicht** normalverteilt sind?

---

### E3. (4 P) (SW10) **Korrelation ≠ Kausalität**
Erklären Sie, warum aus einer hohen Korrelation $|r|$ **keine** Kausalbeziehung folgt. Geben Sie ein **konkretes Beispiel** mit einem Confounder, das **nicht** das Eis-/Sonnenbrand-Beispiel aus der Vorlesung ist.

---

### E4. (4 P) (SW06) **95%-Konfidenzintervall – wirklich**
Welches der folgenden zwei Statements ist die **korrekte** Interpretation eines 95%-Konfidenzintervalls $[\hat\mu_{lo}, \hat\mu_{up}]$? Erklären Sie den Unterschied:

- (i) "Mit 95% Wahrscheinlichkeit liegt $\mu$ in $[\hat\mu_{lo}, \hat\mu_{up}]$."
- (ii) "Wenn wir das Experiment sehr oft wiederholen, würden 95% der so berechneten Intervalle das wahre $\mu$ enthalten."

Welche Formulierung ist statistisch korrekt – und warum ist die andere problematisch?

---

### E5. (3 P) (SW10) **Pearson vs. Spearman**
Beschreiben Sie zwei **konkrete Datensituationen**, in denen Spearman dem Pearson-Koeffizienten **vorzuziehen** ist. Begründen Sie kurz.

---

### E6. (3 P) (SW11) **Bestimmtheitsmass $R^2$**
Erklären Sie das Bestimmtheitsmass $R^2$ als Verhältnis zweier Streuungen. Welche Beziehung besteht in der **linearen Einfachregression** zwischen $R^2$ und dem Pearson-$r$? Was sagt $R^2 = 0$ bzw. $R^2 = 1$ über das Modell aus?

---

# Teil F – Anwendungsaufgabe (10 Punkte)

Eine Immobilienplattform hat einen Datensatz mit den folgenden Merkmalen für 5 000 Mietwohnungen in der Schweiz erhoben:

| Merkmal | Skalenniveau | Beispielwerte |
|---|---|---|
| `stadt` | nominal | Luzern, Zürich, Bern, … |
| `energieklasse` | ordinal | A, B, C, D, E, F, G |
| `quadratmeter` | metrisch | 25, 50, 110, … |
| `miete` | metrisch | 1 200 CHF, 2 800 CHF, … |
| `baujahr` | metrisch | 1965, 2010, … |

Beantworten Sie kurz und mit kurzer Begründung (je 1–2 Sätze):

**F1. (2 P)** Sie wollen den Zusammenhang zwischen `stadt` und `energieklasse` quantifizieren. **Welches Mass** verwenden Sie? **Welche Visualisierung** ist passend?

**F2. (2 P)** Sie wollen wissen, ob `quadratmeter` und `miete` linear zusammenhängen. **Welcher Koeffizient**? Was bedeutet ein Wert von $r = 0.78$?

**F3. (2 P)** Sie wollen prüfen, ob die **mittlere Miete** in Luzern und Zürich **statistisch signifikant** unterschiedlich ist. **Welches Verfahren** schlagen Sie vor – und warum gerade dieses?

**F4. (2 P)** Sie möchten für eine **neue 80 m²-Wohnung** in Bern eine Miet-**Vorhersage mit Unsicherheitsbereich** liefern. **Welches Intervall** ist geeignet – und warum nicht das Konfidenzintervall des Mittelwerts?

**F5. (2 P)** Ein Manager behauptet: "Energieklasse A führt **kausal** zu höherer Miete." Sie sehen eine Korrelation zwischen `energieklasse` und `miete` (mit Spearman: $r_{Sp} \approx -0.4$, da bessere Klasse = höhere Miete). **Welche zwei Confounder** könnten diese Korrelation auch ohne Kausalität erklären?

---

# Hinweise zum Selbsttest

Sie können diese Probeprüfung wie folgt nutzen:

1. **Selbst durchgehen** und Ihre Antworten neben jeder Aufgabe notieren.
2. **Zeit messen** – sind Sie unter 120 min geblieben?
3. Für **Teile A–D und F**: Lösung in [Probepruefung_ASTAT_LOESUNGEN.md](Probepruefung_ASTAT_LOESUNGEN.md) selbst vergleichen.
4. Für **Teil E (Erklärungen)**: Senden Sie Ihre Antworten an Claude mit dem Prompt
   > "Bitte korrigiere meine Antworten zu Teil E der Probeprüfung. Hier sind sie: …"
   und ich gebe Ihnen punkteweise Rückmeldung.

**Viel Erfolg!**
