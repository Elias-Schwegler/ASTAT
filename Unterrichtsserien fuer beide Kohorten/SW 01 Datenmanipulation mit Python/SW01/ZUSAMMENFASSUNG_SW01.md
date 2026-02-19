# ASTAT – Angewandte Statistik für Datenwissenschaften
## SW 01 – Datenmanipulation mit Python

---

## 🎯 Lernziele

1. Sie wissen, was eine **statistische Einheit** ist und können ihre Merkmale bezüglich ihrer **Ausprägungen** unterscheiden.
2. Sie kennen die Python-Module **NumPy** und **Pandas**.
3. Sie können Daten **laden** und **einfache Operationen** ausführen.

---

## 📖 Wichtigste Begriffe

| Begriff | Definition |
|---------|-----------|
| **Statistische Einheit** (statistical unit) | Träger von Informationen und Eigenschaften, die für eine statistische Untersuchung von Interesse sind (z.B. eine Person, ein Unfall, ein Fahrzeug) |
| **Statistisches Merkmal** (statistical feature/variable) | Eine Eigenschaft einer statistischen Einheit, die von Interesse ist (z.B. Note, Gewicht, Unfallkosten) |
| **Ausprägung** (value / level) | Konkreter Wert, den ein Merkmal annehmen kann (z.B. Note = 5.5, Geschlecht = "w") |
| **Nominales Merkmal** (nominal feature) | Merkmal, dessen Ausprägungen nur auf Gleichheit ($=$) oder Ungleichheit ($\neq$) untersucht werden können |
| **Ordinales Merkmal** (ordinal feature) | Merkmal mit natürlicher Reihenfolge ($>$, $<$), aber ohne sinnvolle Rechenoperationen |
| **Metrisches Merkmal** (metric/quantitative feature) | Merkmal mit Zahlenwerten, mit denen gerechnet werden kann ($+$, $-$, $\cdot$, $/$) |
| **NumPy Array** | Mehrdimensionale Datenstruktur für numerische Berechnungen (elementweise Operationen) |
| **Pandas DataFrame** | Zweidimensionale, tabellarische Datenstruktur mit benannten Spalten und Index |
| **Slicing** | Teilbereich aus einem Array oder DataFrame ausschneiden mit `[start:stop]` |
| **Indexing** | Zugriff auf einzelne Elemente mit `[zeile, spalte]` (0-basiert) |
| **NaN / Not Available** | Fehlender Wert in einem Datensatz |
| **inplace** | Parameter, der bewirkt, dass eine Änderung dauerhaft im Objekt gespeichert wird |
| **axis** | Parameter zur Festlegung der Richtung: `axis=0` = entlang der Zeilen (spaltenweise), `axis=1` = entlang der Spalten (zeilenweise) |

---

## 📐 Konzepte & Definitionen

### 1. Statistische Einheit & Merkmal

**Formale Definition:**
Eine **statistische Einheit** ist der elementare Informationsträger in einer statistischen Untersuchung. Ein **statistisches Merkmal** ist eine messbare oder beobachtbare Eigenschaft dieser Einheit.

**Intuitive Erklärung:**
Stell dir eine Tabelle vor – jede **Zeile** ist eine statistische Einheit und jede **Spalte** ist ein Merkmal. Die Zellwerte sind die Ausprägungen.

**Beispiel:**

$$\begin{bmatrix}
\text{Anna}&1981&w&176\\
\text{Beat}&2005&m&181\\
\text{Cary}&2011& &169\\
\text{Dana}&1991&w&165\\
\text{Edin}&1964&m&194
\end{bmatrix}$$

- **Statistische Einheiten:** Anna, Beat, Cary, Dana, Edin
- **Merkmale:** Geburtsjahr, Geschlecht, Körpergrösse
- **Ausprägungen:** z.B. Geschlecht ∈ {w, m}, Körpergrösse ∈ ℝ

---

### 2. Merkmalstypen (Skalenniveaus)

**Formale Definition:**
Merkmale werden nach den zulässigen Vergleichsoperationen klassifiziert:

- **Nominal:** Nur $=$ und $\neq$ sinnvoll
- **Ordinal:** Zusätzlich $<$ und $>$ sinnvoll
- **Metrisch:** Zusätzlich $+$, $-$, $\cdot$, $/$ sinnvoll

**Intuitive Erklärung:**
- **Nominal** = Kategorie ohne Rangfolge (z.B. Farbe: rot ≠ blau, aber rot ist nicht "grösser" als blau)
- **Ordinal** = Kategorie mit Rangfolge (z.B. Schulnote: "sehr gut" > "gut", aber Abstände sind nicht definiert)
- **Metrisch** = Zahlen, mit denen man rechnen kann (z.B. Temperatur: 20°C − 15°C = 5°C)

**Beispiele mit Zahlen:**
| Merkmal | Typ | Begründung |
|---------|-----|-----------|
| Nationalität | Nominal | CH ≠ DE, aber keine Rangfolge |
| Hochschulprädikat | Ordinal | "ausgezeichnet" > "gut" > "genügend" |
| Temperatur in °C | Metrisch | 20°C − 15°C = 5°C ist sinnvoll |
| Anzahl Mausklicks | Metrisch | 10 + 5 = 15 Klicks |
| Geschlecht | Nominal | m ≠ w, keine Ordnung |

---

### 3. Python-Listen vs. NumPy Arrays

**Problem mit Listen:**
Python-Listen unterstützen **keine elementweisen** mathematischen Operationen:
- `[5.0, 5.0, 5.5] + [4.5, 4.0, 4.5]` → **Konkatenation:** `[5.0, 5.0, 5.5, 4.5, 4.0, 4.5]`
- `[5.0, 5.0, 5.5] * [4.5, 4.0, 4.5]` → **TypeError!**

**Lösung mit NumPy:**
NumPy Arrays erlauben **elementweise** Operationen:
- `np.array([5.0, 5.0, 5.5]) + np.array([4.5, 4.0, 4.5])` → `array([9.5, 9.0, 10.0])`
- Mittelwert: `(P_1 + P_2) / 2` → `array([4.75, 4.5, 5.0])`

---

### 4. NumPy: Mehrdimensionale Arrays

**Erstellung:**
```python
Noten = np.array([[5.0, 5.0, 5.5],
                   [4.5, 4.0, 4.5]])
```

**Attribut `shape`:**
- `Noten.shape` → `(2, 3)` — 2 Zeilen, 3 Spalten
- `Noten.shape[0]` → `2` (Anzahl Zeilen)
- `Noten.shape[1]` → `3` (Anzahl Spalten)

**Indexing (0-basiert!):**
- `Noten[0, 2]` → `5.5` (1. Zeile, 3. Spalte)

**Slicing:**
- `Noten[1, :]` → `array([4.5, 4.0, 4.5])` (ganze 2. Zeile)
- `Noten[:, 2]` → `array([5.5, 4.5])` (ganze 3. Spalte)
- `Noten[0:2, 1:3]` → `array([[5.0, 5.5], [4.0, 4.5]])` (Teilmatrix)

> ⚠️ **Prüfungshinweis:** Der Endindex bei Slicing ist **exklusiv** – `0:2` bedeutet Index 0 und 1, NICHT 0, 1, 2!

---

### 5. NumPy: `axis`-Parameter

**Grundregel:**
- `axis=0` → Operation **entlang der Zeilen** (= Ergebnis pro **Spalte**)
- `axis=1` → Operation **entlang der Spalten** (= Ergebnis pro **Zeile**)
- Kein `axis` → Operation über **alle** Elemente

**Zahlenbeispiel mit `Noten = [[5.0, 5.0, 5.5], [4.5, 4.0, 4.5]]`:**

| Methode | Ergebnis | Erklärung |
|---------|----------|-----------|
| `Noten.sum()` | `28.5` | Summe aller 6 Elemente |
| `Noten.sum(axis=0)` | `[9.5, 9.0, 10.0]` | Spaltensummen |
| `Noten.sum(axis=1)` | `[15.5, 13.0]` | Zeilensummen |
| `Noten.mean()` | `4.75` | Mittelwert aller Elemente |
| `Noten.mean(axis=0)` | `[4.75, 4.5, 5.0]` | Spaltenmittelwerte |
| `Noten.mean(axis=1)` | `[5.167, 4.333]` | Zeilenmittelwerte |
| `Noten.min()` | `4.0` | Globales Minimum |
| `Noten.max()` | `5.5` | Globales Maximum |

> ⚠️ **Eselsbrücke:** `axis=0` "klappt" die Zeilen zusammen → **eine Zahl pro Spalte**. `axis=1` "klappt" die Spalten zusammen → **eine Zahl pro Zeile**.

---

### 6. NumPy: `np.unique()`

Gibt alle **unterschiedlichen** Elemente zurück (sortiert, ohne Duplikate).

**Optionen:**
- `np.unique(array)` → Eindeutige Werte
- `np.unique(array, return_counts=True)` → Werte **und** Häufigkeiten
- `np.unique(array, axis=0)` → Eindeutige **Zeilen**
- `np.unique(array, axis=1)` → Eindeutige **Spalten**

**Zahlenbeispiel:**
```
Noten = [[5.0, 5.0, 5.5], [4.5, 4.0, 4.5]]
np.unique(Noten)           → array([4.0, 4.5, 5.0, 5.5])
np.unique(Noten, return_counts=True) 
    → (array([4.0, 4.5, 5.0, 5.5]), array([1, 2, 2, 1]))
```

---

### 7. Pandas: DataFrame erstellen

**Aus Listen/Arrays:**
```python
df = pd.DataFrame({
    "cities": ["Greater London", "Tokyo", "Paris", "New York"],
    "population": [8663300, 9272565, 2229621, 8491079],
    "area": [1572, 627, 105, 784]
})
```

**Aus CSV-Datei:**
```python
gla_cities = pd.read_csv("Daten/GLA_World_Cities_2016.csv")
```

---

### 8. Pandas: Auswahl & Navigation

| Methode | Beschreibung | Beispiel |
|---------|-------------|---------|
| `df.head(n)` | Erste n Zeilen | `df.head(3)` |
| `df.tail(n)` | Letzte n Zeilen | `df.tail(2)` |
| `df.shape` | (Zeilen, Spalten) | `(4, 3)` |
| `df.columns` | Spaltennamen | `Index(['cities', 'population', 'area'])` |
| `df[["col"]]` | Spalte(n) auswählen | `df[["population"]]` |
| `df[["col"]][a:b]` | Spalte mit Zeilenslicing | `df[["population"]][2:4]` |
| `df.iloc[zeilen, spalten]` | Auswahl per **Positionsindex** (integer) | `df.iloc[[1,3], [1,2]]` |
| `df.loc[label, spalte]` | Auswahl per **Label** (Index-/Spaltenname) | `df.loc["Tokyo", "population"]` |

> ⚠️ **Prüfungshinweis: `iloc` vs. `loc`**
> - `iloc` = **integer**-basiert (Position), Slicing exklusiv
> - `loc` = **label**-basiert (Name), Slicing **inklusiv**!

---

### 9. Pandas: Index setzen

```python
df.set_index("cities")           # Nur für Anzeige, NICHT dauerhaft!
df.set_index("cities", inplace=True)  # Dauerhaft!
```

Nach `set_index` kann mit `loc` per Label zugegriffen werden:
```python
df.loc["Tokyo"]                    # → Series
df.loc[["Tokyo", "Paris"]]         # → DataFrame
df.loc["Tokyo", "population"]      # → int64 (Einzelwert)
df.loc[["Tokyo"], ["population"]]  # → DataFrame
```

> ⚠️ **Prüfungsfalle:** `df.loc["Tokyo"]` gibt eine **Series** zurück, `df.loc[["Tokyo"]]` ein **DataFrame**!

---

### 10. Pandas: Datenbereinigung

**Fehlende Werte entfernen (`dropna`):**
```python
df.dropna(how="any")     # Zeilen mit MINDESTENS einem NaN entfernen
df.dropna(how="all")     # Nur komplett leere Zeilen entfernen
df.dropna(how="all", inplace=True)  # Dauerhaft entfernen
```

**Spalten umbenennen (`rename`):**
```python
df.rename(columns={"alter Name": "neuer Name"}, inplace=True)
```

**Datentyp umwandeln:**
```python
df["Population"] = df["Population"].str.replace(",", "").astype(float)
```
→ Entfernt Tausendertrennzeichen und wandelt String in float um.

---

### 11. Pandas: Neue Spalten berechnen

**Direkte Berechnung:**
```python
df["pop_density"] = df["population"] / df["area"]
```

**Einheiten umrechnen:**
```python
df["Population (M)"] = df["Population"] / 1_000_000
```

---

### 12. Pandas: `apply()` – Funktionen auf Spalten anwenden

```python
def city_size(x):
    if x < 1.5:
        return "Small"
    elif 1.5 <= x < 3:
        return "Medium"
    elif 3 <= x < 5:
        return "Large"
    else:
        return "Mega"

df["City Size"] = df["Population (M)"].apply(city_size)
```

> **Intuition:** `apply()` wendet eine Funktion **auf jeden einzelnen Wert** einer Spalte an.

---

### 13. Pandas: Filtern

**Syntax:** `df[Bedingung]`

```python
# Alle "kleinen" Städte:
df[df["City Size"] == "Small"]

# Städte mit mehr als 8 Mio. Einwohner:
df[["City", "Population (M)"]][df["Population (M)"] > 8]
```

---

### 14. Pandas: `groupby()` – Gruppierung

```python
grouped = df.groupby("City Size")
grouped.size()                          # Anzahl pro Gruppe
grouped["Population (M)"].mean()        # Mittelwert pro Gruppe
grouped["Population (M)"].min()         # Minimum pro Gruppe
```

---

## 🔢 Formeln & Rechenregeln

### Arithmetisches Mittel (Mittelwert)

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$

**Variablen:**
- $\bar{x}$ = Mittelwert
- $n$ = Anzahl Beobachtungen
- $x_i$ = einzelne Beobachtungswerte

**Zahlenbeispiel:**
$$\bar{x} = \frac{5.0 + 5.0 + 5.5 + 4.5 + 4.0 + 4.5}{6} = \frac{28.5}{6} = 4.75$$

**Python:** `Noten.mean()` → `4.75`

**Randfälle:**
- $n = 0$: Division durch 0! Python gibt `nan` bei leerem Array zurück.
- Einzelner Wert: $\bar{x} = x_1$

---

### Bevölkerungsdichte

$$\text{Dichte} = \frac{\text{Population}}{\text{Fläche}}$$

**Zahlenbeispiel (Greater London):**
$$\text{Dichte} = \frac{8\,663\,300}{1\,572} \approx 5\,511.0 \; \text{Personen/km}^2$$

---

### Einheitenumrechnung (Aufgabe 2)

$$\text{km/l} = \text{mpg} \times 0.425144$$
$$\text{kg} = \text{lbs (weight)} \times 0.453592$$

**Zahlenbeispiel (Fahrzeug 1: mpg=33, weight=2560):**
$$\text{km/l} = 33 \times 0.425144 = 14.03$$
$$\text{kg} = 2560 \times 0.453592 = 1161.2$$

---

## 📊 Vergleiche & Klassifizierungen

### Merkmalstypen im Überblick

| Eigenschaft | Nominal | Ordinal | Metrisch |
|-------------|---------|---------|----------|
| $=$ / $\neq$ prüfbar | ✅ | ✅ | ✅ |
| $<$ / $>$ sinnvoll | ❌ | ✅ | ✅ |
| $+$ / $-$ / $\cdot$ / $/$ | ❌ | ❌ | ✅ |
| Mittelwert sinnvoll | ❌ | ❌ | ✅ |
| Beispiel | Geschlecht, Beruf | Schulnoten-Prädikat | Temperatur, Gewicht |
| Python-Typ | `str`, `category` | `category` (ordered) | `int`, `float` |

### Listen vs. NumPy Arrays

| Operation | Python-Liste | NumPy Array |
|-----------|-------------|-------------|
| `a + b` | Konkatenation | Elementweise Addition |
| `a * b` | TypeError | Elementweises Produkt |
| `a * 2` | Liste verdoppeln | Jedes Element ×2 |
| Mehrdimensional | Verschachtelte Listen | ndarray mit `shape` |
| Statistische Funktionen | Nicht verfügbar | `.mean()`, `.sum()`, `.min()`, `.max()` |

### `iloc` vs. `loc`

| Merkmal | `iloc` | `loc` |
|---------|--------|-------|
| Zugriff über | **Position** (Integer-Index) | **Label** (Name) |
| Slicing-Endpunkt | **exklusiv** | **inklusiv** |
| Beispiel | `df.iloc[0:2]` → Zeile 0, 1 | `df.loc["A":"C"]` → A, B, C |
| Spalten | Per Positionsnummer | Per Spaltenname |

### `dropna()` Parameter `how`

| Wert | Verhalten |
|------|-----------|
| `"any"` | Löscht Zeilen/Spalten mit **mindestens einem** NaN |
| `"all"` | Löscht nur Zeilen/Spalten, die **komplett** aus NaN bestehen |

---

## 💻 Code-Beispiele (Python)

#### Konzept: Listen vs. NumPy Arrays
Zeigt den Unterschied zwischen Python-Listen (Konkatenation) und NumPy Arrays (elementweise Operationen).

```python
# Python-Listen: + bedeutet Konkatenation
Person_1 = [5.0, 5.0, 5.5]
Person_2 = [4.5, 4.0, 4.5]
print(Person_1 + Person_2)  # [5.0, 5.0, 5.5, 4.5, 4.0, 4.5]

# NumPy: + bedeutet elementweise Addition
import numpy as np
P_1 = np.array(Person_1)
P_2 = np.array(Person_2)
print((P_1 + P_2) / 2)  # Elementweiser Mittelwert
```

**Output/Interpretation:**
- Liste: `[5.0, 5.0, 5.5, 4.5, 4.0, 4.5]` – die Listen werden angehängt
- NumPy: `array([4.75, 4.5, 5.0])` – elementweiser Durchschnitt beider Personen

---

#### Konzept: 2D-Array erstellen und Shape abfragen
Zeigt wie aus verschachtelten Listen ein 2D-Array entsteht und dessen Dimensionen abgefragt werden.

```python
# 2D-Array aus zwei Personen-Arrays
Noten = np.array([P_1, P_2])
print(Noten)
# [[5.  5.  5.5]
#  [4.5 4.  4.5]]

# Dimensionen abfragen
print("Shape:", Noten.shape)          # (2, 3)
print("Zeilen:", Noten.shape[0])      # 2
print("Spalten:", Noten.shape[1])     # 3
```

**Output/Interpretation:** Das Array hat 2 Zeilen (Personen) und 3 Spalten (Prüfungen).

---

#### Konzept: Indexing und Slicing bei NumPy Arrays
Zugriff auf einzelne Elemente und Teilbereiche eines Arrays.

```python
# Einzelnes Element: Zeile 0, Spalte 2
print(Noten[0, 2])          # 5.5

# Ganze Zeile (2. Zeile = Index 1)
print(Noten[1, :])          # [4.5 4.  4.5]

# Ganze Spalte (3. Spalte = Index 2)
print(Noten[:, 2])          # [5.5 4.5]

# Teilmatrix: Zeile 0-1, Spalte 1-2
print(Noten[0:2, 1:3])      # [[5.  5.5] [4.  4.5]]
```

**Output/Interpretation:** 0-basierte Indexierung; Slicing `[start:stop]` ist am Ende exklusiv.

---

#### Konzept: Aggregationsmethoden mit axis-Parameter
Berechnung von Summe, Mittelwert, Min, Max über verschiedene Achsen.

```python
# Gesamt
print(Noten.sum())           # 28.5
print(Noten.mean())          # 4.75

# Pro Spalte (axis=0)
print(Noten.sum(axis=0))     # [9.5 9.  10. ]
print(Noten.mean(axis=0))    # [4.75 4.5  5.  ]

# Pro Zeile (axis=1)
print(Noten.sum(axis=1))     # [15.5 13. ]
print(Noten.mean(axis=1))    # [5.16666667 4.33333333]

# Min/Max auf Teilarrays
print(Noten[0, :].max())     # 5.5 (Maximum der 1. Person)
print(Noten[:, 2].min())     # 4.5 (Minimum der 3. Prüfung)
```

**Output/Interpretation:** `axis=0` aggregiert spaltenweise (über Zeilen), `axis=1` zeilenweise (über Spalten).

---

#### Konzept: `np.unique()` – Eindeutige Werte und Häufigkeiten
Ermittlung der vorhandenen Werte und deren Häufigkeiten in einem Array.

```python
# Eindeutige Werte
print(np.unique(Noten))      # [4.  4.5 5.  5.5]

# Werte mit Häufigkeiten
werte, haeufigkeiten = np.unique(Noten, return_counts=True)
print(werte)                 # [4.  4.5 5.  5.5]
print(haeufigkeiten)         # [1 2 2 1]

# Eindeutige Zeilen
marks = np.array([P_1, P_1, P_1, P_2, P_2, [4, 4.5, 4.5]])
zeilen, counts = np.unique(marks, return_counts=True, axis=0)
print(zeilen)                # 3 verschiedene Zeilen
print(counts)                # [1 3 2] - Häufigkeit jeder Zeile
```

**Output/Interpretation:** 4.0 kommt 1×, 4.5 kommt 2×, 5.0 kommt 2×, 5.5 kommt 1× vor.

---

#### Konzept: Pandas DataFrame erstellen
Erstellt einen DataFrame aus Listen/Arrays mit benannten Spalten.

```python
import pandas as pd

# DataFrame aus Listen
names = ["Greater London", "Tokyo", "Paris", "New York"]
population = [8663300, 9272565, 2229621, 8491079]
area = [1572, 627, 105, 784]

df = pd.DataFrame({"cities": names, "population": population, "area": area})
print(df)
```

**Output/Interpretation:**
```
           cities  population  area
0  Greater London     8663300  1572
1           Tokyo     9272565   627
2           Paris     2229621   105
3        New York     8491079   784
```
Standardmässig wird ein numerischer Index (0, 1, 2, ...) zugewiesen.

---

#### Konzept: DataFrame Navigation (head, tail, shape, columns)
Grundlegende Methoden zur Erkundung eines DataFrames.

```python
print(df.head(2))          # Erste 2 Zeilen
print(df.tail(2))          # Letzte 2 Zeilen
print(df.shape)            # (4, 3) – 4 Zeilen, 3 Spalten
print(df.columns)          # Index(['cities', 'population', 'area'])
```

**Output/Interpretation:** `.shape` gibt ein Tupel zurück; `.columns` ein Index-Objekt mit Spaltennamen.

---

#### Konzept: iloc und loc – Positionsbasierter vs. labelbasierter Zugriff

```python
# iloc: Zugriff per Position (Integer)
print(df.iloc[[1, 3], [1, 2]])    # Zeilen 1+3, Spalten 1+2

# Index setzen (dauerhaft)
df.set_index("cities", inplace=True)

# loc: Zugriff per Label
print(df.loc["Tokyo"])                        # Series
print(df.loc[["Tokyo", "Paris"]])             # DataFrame
print(df.loc[["Tokyo", "Paris"], ["population"]])  # Teilauswahl
print(df.loc["Tokyo", "population"])          # Einzelwert (int64)
```

**Output/Interpretation:** 
- `iloc` nutzt Ganzzahl-Indizes → `iloc[[1,3]]` = 2. und 4. Zeile
- `loc` nutzt Labels → `loc["Tokyo"]` = Zeile mit Label "Tokyo"

---

#### Konzept: CSV-Daten laden und bereinigen
Einlesen von CSV-Dateien, fehlende Werte entfernen, Spalten umbenennen, Datentypen konvertieren.

```python
# CSV laden
gla_cities = pd.read_csv("Daten/GLA_World_Cities_2016.csv")
print(gla_cities.shape)     # (18, 11)

# Leere Zeilen entfernen
gla_cities.dropna(how="all", inplace=True)

# Spalte umbenennen
gla_cities.rename(columns={"Inland area in km2": "Area km2"}, inplace=True)

# Tausendertrennzeichen entfernen und Typ konvertieren
gla_cities["Population"] = gla_cities["Population"].str.replace(",", "").astype(float)
gla_cities["Area km2"] = gla_cities["Area km2"].str.replace(",", "").astype(float)
```

**Output/Interpretation:** Die Daten enthalten Tausendertrennzeichen als Kommas, die als String gelesen werden. Erst nach `.str.replace(",", "").astype(float)` kann gerechnet werden.

---

#### Konzept: Neue Spalten berechnen und apply()
Berechnung abgeleiteter Spalten und Anwendung eigener Funktionen.

```python
# Direkte Berechnung
gla_cities["pop_density"] = gla_cities["Population"] / gla_cities["Area km2"]
gla_cities["Population (M)"] = gla_cities["Population"] / 1_000_000

# Eigene Klassifikationsfunktion
def city_size(x):
    if x < 1.5:
        return "Small"
    elif 1.5 <= x < 3:
        return "Medium"
    elif 3 <= x < 5:
        return "Large"
    else:
        return "Mega"

# Funktion auf Spalte anwenden
gla_cities["City Size"] = gla_cities["Population (M)"].apply(city_size)
```

**Output/Interpretation:** `apply()` wendet die Funktion `city_size` auf jeden einzelnen Wert der Spalte an und erstellt damit eine neue kategoriale Spalte.

---

#### Konzept: Filtern und Gruppieren
Zeilen nach Bedingungen filtern und mit groupby() aggregieren.

```python
# Filtern: Nur kleine Städte
small = gla_cities[gla_cities["City Size"] == "Small"]

# Filtern mit Spaltenwahl
big = gla_cities[["City", "Population (M)"]][gla_cities["Population (M)"] > 8]

# Gruppieren
grouped = gla_cities.groupby("City Size")
print(grouped.size())                         # Anzahl pro Gruppe
print(grouped["Population (M)"].mean())       # Mittelwert pro Gruppe
print(grouped["Population (M)"].min())        # Minimum pro Gruppe
```

**Output/Interpretation:** `groupby()` teilt den DataFrame in Gruppen auf. Danach können Aggregationsfunktionen pro Gruppe angewendet werden.

---

## 🔗 Konzept-Code-Zuordnung

| Konzept | Python-Funktion/Code | Library | Beschreibung |
|---------|---------------------|---------|-------------|
| Array erstellen | `np.array([...])` | NumPy | Liste → Array konvertieren |
| Dimensionen abfragen | `.shape` | NumPy | Tupel mit (Zeilen, Spalten) |
| Element zugreifen | `array[i, j]` | NumPy | 0-basierter Index |
| Zeile/Spalte auswählen | `array[i, :]` / `array[:, j]` | NumPy | Slicing mit `:` |
| Teilmatrix | `array[a:b, c:d]` | NumPy | Bereich ausschneiden |
| Maximum | `.max()` | NumPy | Grösster Wert |
| Minimum | `.min()` | NumPy | Kleinster Wert |
| Summe | `.sum()` / `.sum(axis=0/1)` | NumPy | Gesamtsumme oder pro Achse |
| Mittelwert | `.mean()` / `.mean(axis=0/1)` | NumPy | Arithm. Mittel |
| Eindeutige Werte | `np.unique(array)` | NumPy | Deduplizierte Werte |
| Häufigkeiten | `np.unique(array, return_counts=True)` | NumPy | Werte + Anzahlen |
| DataFrame erstellen | `pd.DataFrame({...})` | Pandas | Dict mit Spalten → Tabelle |
| CSV laden | `pd.read_csv("pfad")` | Pandas | Datei einlesen |
| Erste/Letzte Zeilen | `.head(n)` / `.tail(n)` | Pandas | Datenübersicht |
| Spaltennamen | `.columns` | Pandas | Index-Objekt |
| Positions-Zugriff | `.iloc[zeilen, spalten]` | Pandas | Integer-basiert |
| Label-Zugriff | `.loc[label, spalte]` | Pandas | Name-basiert |
| Index setzen | `.set_index("col", inplace=True)` | Pandas | Spalte als Index |
| Fehlende Werte | `.dropna(how="all/any", inplace=True)` | Pandas | NaN entfernen |
| Umbenennen | `.rename(columns={...}, inplace=True)` | Pandas | Spaltennamen ändern |
| Typ konvertieren | `.str.replace(",","").astype(float)` | Pandas | String → Zahl |
| Neue Spalte | `df["neu"] = df["a"] / df["b"]` | Pandas | Berechnung |
| Funktion anwenden | `.apply(funktion)` | Pandas | Pro Wert anwenden |
| Filtern | `df[df["col"] == wert]` | Pandas | Zeilen filtern |
| Gruppieren | `.groupby("col")` | Pandas | Gruppen bilden |
| Gruppengrösse | `grouped.size()` | Pandas | Anzahl pro Gruppe |
| Gruppen-Aggregation | `grouped["col"].mean()` | Pandas | Funktion pro Gruppe |

---

## ✏️ Übungsaufgaben-Zusammenfassung

### Aufgabe 1: Weather-Datensatz

| Nr. | Aufgabe | Konzept | Lösungsansatz |
|-----|---------|---------|---------------|
| 1.1 | Datensatz laden | `pd.read_csv()` | `data = pd.read_csv("Daten/weather.csv")` |
| 1.2 | Wert 2. Zeile, 3. Spalte | `iloc` | `data.iloc[1, 2]` → Wert: 1 (Chur im Feb) |
| 1.3 | 4. Zeile auswählen | `iloc` | `data.iloc[3]` |
| 1.4 | 1. und 4. Spalte | Spaltenauswahl | `data.iloc[:, [0, 3]]` oder `data[["Luzern", "Zurich"]]` |
| 1.5 | "Basel" → "Genf" umbenennen | `rename()` | `data.rename(columns={"Basel": "Genf"}, inplace=True)` |
| 1.6 | Mittlere Temp. aller Städte | `.mean(axis=0)` | `data.mean(axis=0)` (Spaltenmittelwerte) |
| 1.7 | Mittlere Temp. aller Monate | `.mean(axis=1)` | `data.mean(axis=1)` (Zeilenmittelwerte) |
| 1.8 | Spalte mit Monatsmittel | Neue Spalte | `data["mean_temp"] = data.mean(axis=1)` |

**Daten `weather.csv`:**
```
       Luzern  Basel  Chur  Zurich
Jan       2      5    -3      4
Feb       5      6     1      0
Mar      10     11    13      8
May      21     23    21     20
Jun      25     21    23     27
```

---

### Aufgabe 2: Fuel-Datensatz

| Nr. | Aufgabe | Konzept | Lösungsansatz |
|-----|---------|---------|---------------|
| 2.1 | Datensatz laden | `pd.read_csv()` | `fuel = pd.read_csv("Daten/d.fuel.dat")` |
| 2.2 | Merkmale beschreiben | Merkmalstypen | weight: metrisch, mpg: metrisch, type: nominal |
| 2.3 | 5. Zeile | `iloc` | `fuel.iloc[4]` → X=5, weight=2440, mpg=32, type=Small |
| 2.4 | Zeile 1–5 | Slicing | `fuel.iloc[0:5]` oder `fuel.head(5)` |
| 2.5 | Zeile 1–3 und 57–60 | `pd.concat` | `pd.concat([fuel.iloc[0:3], fuel.iloc[56:60]])` |
| 2.6 | Mittelwert mpg (alle) | `.mean()` | `fuel["mpg"].mean()` |
| 2.7 | Mittelwert mpg (7–22) | Slicing + mean | `fuel["mpg"].iloc[6:22].mean()` |
| 2.8 | Spalte km/l und kg | Umrechnung | `fuel["t.kml"] = fuel["mpg"] * 0.425144` |
| 2.9 | Mittelwerte km/l und kg | `.mean()` | `fuel["t.kml"].mean()`, `fuel["t.kg"].mean()` |
| 2.10 | Mittleres Gewicht Sporty | groupby/filter | `fuel[fuel["type"]=="Sporty"]["weight"].mean()` |

**Merkmale des Fuel-Datensatzes:**
| Merkmal | Typ | Erklärung |
|---------|-----|-----------|
| `X` | Metrisch (ID) | Laufnummer des Fahrzeugs |
| `weight` | Metrisch | Gewicht in Pfund (lbs) |
| `mpg` | Metrisch | Reichweite in Miles per Gallon |
| `type` | Nominal | Fahrzeugkategorie (Small, Sporty, Compact, Medium, Large, Van) |

---

## ⚠️ Prüfungsrelevante Hinweise

### Typische Aufgabentypen
1. **"Welcher Merkmalstyp liegt vor?"** → Nominal/Ordinal/Metrisch bestimmen
2. **"Was gibt dieser Code aus?"** → NumPy/Pandas-Operationen nachvollziehen
3. **"Wie greift man auf Element X zu?"** → Indexing/Slicing/iloc/loc
4. **"Was ist der Unterschied zwischen...?"** → Listen vs. Arrays, iloc vs. loc, inplace vs. nicht

### Häufige Fehlerquellen & Fallstricke

| Falle | Erklärung |
|-------|-----------|
| `axis=0` vs. `axis=1` | 0 = spaltenweise (über Zeilen), 1 = zeilenweise (über Spalten) – **verwechseln ist häufigster Fehler!** |
| Slicing-Endindex | Bei NumPy und `iloc` ist der Endindex **exklusiv**: `[0:2]` = Index 0, 1 |
| `set_index()` ohne `inplace=True` | Ändert den DataFrame **nicht** dauerhaft! |
| `dropna()` ohne `inplace=True` | Löscht **keine** Zeilen dauerhaft! |
| `loc` vs. `iloc` | `loc` ist label-basiert und **inklusiv**, `iloc` ist integer-basiert und **exklusiv** |
| Listen-Addition | `+` bei Listen = Konkatenation, nicht elementweise Addition! |
| String-Spalten rechnen | Erst `.str.replace(",","").astype(float)` nötig |
| `loc["Tokyo"]` vs. `loc[["Tokyo"]]` | Ersteres → Series, Letzteres → DataFrame |

### Merkregeln & Eselsbrücken

- **axis=0** → "**N**ull wie **N**ach unten" (über Zeilen, ergibt Spaltenwerte)
- **axis=1** → "**E**ins wie **E**ntlang" (über Spalten, ergibt Zeilenwerte)
- **iloc = integer location**, **loc = label location**
- **inplace = in place** → "An Ort und Stelle ändern" (dauerhaft)
- **Merkmalstypen:** N-O-M = **N**ominell – **O**rdentlich – **M**essbar (zunehmende Operationen)

### Formeln für das A4-Blatt
- Arithmetisches Mittel: $\bar{x} = \frac{1}{n}\sum x_i$
- Umrechnung mpg → km/l: $\times\; 0.425144$
- Umrechnung lbs → kg: $\times\; 0.453592$

### SC/MC-Hinweise
- **Distraktor:** "Listen in Python können elementweise addiert werden" → **FALSCH** (Konkatenation!)
- **Distraktor:** "`set_index()` ändert den DataFrame dauerhaft" → **FALSCH** (nur mit `inplace=True`)
- **Distraktor:** "`Noten[0:2]` gibt 3 Elemente zurück" → **FALSCH** (nur 2, Endindex exklusiv)
- **Distraktor:** "axis=0 berechnet Zeilenwerte" → **FALSCH** (Spaltenwerte!)

---

## 🔗 Verbindung zu vorherigen/folgenden Wochen

### Voraussetzungen (vorherige Wochen)
- Grundlegende Python-Kenntnisse (Variablen, Listen, Funktionen, Schleifen)
- Keine statistischen Vorkenntnisse nötig

### Aufbau für folgende Wochen
| Diese Woche (SW 01) | Wird gebraucht in |
|---------------------|-------------------|
| **Statistische Einheiten & Merkmale** | SW 02+ (Grundlage für alles) |
| **Merkmalstypen (Nominal/Ordinal/Metrisch)** | SW 02 (Lagemasse nur für metrische Merkmale), SW 04 (Verteilungen), SW 07–08 (Wahl des Testverfahrens) |
| **NumPy Arrays & Operationen** | Jede Woche (Berechnungen, Vektoren) |
| **Pandas DataFrames** | SW 02 (Datenbeschreibung), SW 03 (Visualisierung), alle weiteren Wochen |
| **`pd.read_csv()` & Datenbereinigung** | Jede Woche (Datensätze laden) |
| **`groupby()` & Filtern** | SW 02 (Vergleiche), SW 09–10 (Zusammenhangsanalyse) |
| **`apply()` & neue Spalten** | SW 02 (berechnete Kennzahlen), SW 11–12 (Regression) |

> **Vorausschau SW 02:** Die nächste Woche behandelt **Datenbeschreibung** (Lagemasse, Streuungsmasse, Quantile, Box-Plots). Die hier gelernten NumPy-Methoden (`.mean()`, `.min()`, `.max()`) werden erweitert um `.median()`, `.std()`, `.var()` und Quantil-Funktionen. Pandas-Grundlagen (DataFrame, Slicing, Filtern) werden vorausgesetzt.
