"""Grafiken für ZUSAMMENFASSUNG_SW10.md erzeugen."""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import FancyBboxPatch
from matplotlib.colors import LinearSegmentedColormap

HSLU = (160 / 255, 0 / 255, 86 / 255)
OUT = os.path.join(os.path.dirname(__file__), "Bilder")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "axes.titleweight": "bold",
})


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=130, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  saved {name}")


rng = np.random.default_rng(42)


# ---------------------------------------------------------------------------
# 1. Drei Korrelationsmuster: positiv, negativ, unkorreliert
# ---------------------------------------------------------------------------
def fig_korrelationsmuster():
    n = 200
    A = rng.uniform(0, 15, n)
    B_p = 0.2 * A + 3 + rng.normal(0, 0.8, n)
    B_n = -1.5 * A + 14 + rng.normal(0, 0.5, n)
    B_u = rng.uniform(0, 15, n)

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    for ax, A_, B_, titel, subtitle in [
        (axes[0], A, B_p, "Positive Korrelation",
         "$a_i \\uparrow \\Rightarrow b_i \\uparrow$"),
        (axes[1], A, B_n, "Negative Korrelation",
         "$a_i \\uparrow \\Rightarrow b_i \\downarrow$"),
        (axes[2], A, B_u, "Unkorreliert",
         "keine lineare Tendenz"),
    ]:
        r = np.corrcoef(A_, B_)[0, 1]
        ax.scatter(A_, B_, alpha=0.55, color=HSLU, s=20, edgecolor="white", linewidth=0.5)
        ax.set_title(f"{titel}\n{subtitle}   |   $r = {r:+.2f}$", color=HSLU)
        ax.set_xlabel("Merkmal $A$")
        ax.set_ylabel("Merkmal $B$")
        ax.grid(alpha=0.3)

    fig.suptitle("Drei prototypische Korrelationsmuster",
                 fontsize=14, fontweight="bold", y=1.02)
    save(fig, "korrelationsmuster.png")


# ---------------------------------------------------------------------------
# 2. Kovarianz-Quadranten – Interpretation des Produkts
# ---------------------------------------------------------------------------
def fig_kovarianz_quadranten():
    n = 80
    A = rng.normal(5, 2, n)
    B = 0.8 * A + rng.normal(0, 1.2, n)
    a_bar, b_bar = A.mean(), B.mean()

    fig, ax = plt.subplots(figsize=(8, 7))

    xmin, xmax = A.min() - 0.5, A.max() + 0.5
    ymin, ymax = B.min() - 0.5, B.max() + 0.5

    ax.add_patch(plt.Rectangle((a_bar, b_bar), xmax - a_bar, ymax - b_bar,
                               alpha=0.15, color="green", zorder=0))
    ax.add_patch(plt.Rectangle((xmin, b_bar), a_bar - xmin, ymax - b_bar,
                               alpha=0.15, color="red", zorder=0))
    ax.add_patch(plt.Rectangle((xmin, ymin), a_bar - xmin, b_bar - ymin,
                               alpha=0.15, color="green", zorder=0))
    ax.add_patch(plt.Rectangle((a_bar, ymin), xmax - a_bar, b_bar - ymin,
                               alpha=0.15, color="red", zorder=0))

    ax.axvline(a_bar, color="black", lw=1.5, linestyle="--")
    ax.axhline(b_bar, color="black", lw=1.5, linestyle="--")

    ax.scatter(A, B, color=HSLU, s=30, alpha=0.75, edgecolor="white", linewidth=0.5, zorder=3)
    ax.plot(a_bar, b_bar, "k*", markersize=18, zorder=4)
    ax.annotate("$(\\bar{a},\\bar{b})$", (a_bar, b_bar),
                xytext=(a_bar + 0.4, b_bar + 0.4), fontsize=13, fontweight="bold")

    # Quadrant labels
    ax.text(a_bar + (xmax - a_bar) * 0.5, b_bar + (ymax - b_bar) * 0.9,
            "Q1:  $(a_i - \\bar{a}) > 0$\n     $(b_i - \\bar{b}) > 0$\n→ Produkt $> 0$",
            ha="center", va="top", fontsize=10, color="darkgreen", fontweight="bold")
    ax.text(xmin + (a_bar - xmin) * 0.5, b_bar + (ymax - b_bar) * 0.9,
            "Q2:  $(a_i - \\bar{a}) < 0$\n     $(b_i - \\bar{b}) > 0$\n→ Produkt $< 0$",
            ha="center", va="top", fontsize=10, color="darkred", fontweight="bold")
    ax.text(xmin + (a_bar - xmin) * 0.5, ymin + (b_bar - ymin) * 0.15,
            "Q3:  $(a_i - \\bar{a}) < 0$\n     $(b_i - \\bar{b}) < 0$\n→ Produkt $> 0$",
            ha="center", va="bottom", fontsize=10, color="darkgreen", fontweight="bold")
    ax.text(a_bar + (xmax - a_bar) * 0.5, ymin + (b_bar - ymin) * 0.15,
            "Q4:  $(a_i - \\bar{a}) > 0$\n     $(b_i - \\bar{b}) < 0$\n→ Produkt $< 0$",
            ha="center", va="bottom", fontsize=10, color="darkred", fontweight="bold")

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_xlabel("Merkmal $A$")
    ax.set_ylabel("Merkmal $B$")
    ax.set_title(f"Kovarianz-Quadranten um $(\\bar{{a}}, \\bar{{b}})$  |  $\\sigma_{{ab}} = {np.cov(A, B, ddof=1)[0,1]:.2f} > 0$",
                 color=HSLU)
    save(fig, "kovarianz_quadranten.png")


# ---------------------------------------------------------------------------
# 3. r-Skala von -1 bis +1
# ---------------------------------------------------------------------------
def fig_r_skala():
    fig, ax = plt.subplots(figsize=(12, 3.3))

    cmap = LinearSegmentedColormap.from_list("r_scale",
                                             ["#b30032", "#e8e8e8", HSLU])
    n = 400
    for i in range(n):
        ax.add_patch(plt.Rectangle((i / n, 0.4), 1 / n, 0.35,
                                   facecolor=cmap(i / n), edgecolor="none"))

    ticks = np.linspace(0, 1, 11)
    labels = [f"{x:+.1f}" for x in np.linspace(-1, 1, 11)]
    labels[5] = "0"
    for t, l in zip(ticks, labels):
        ax.plot([t, t], [0.38, 0.42], color="black", lw=1)
        ax.text(t, 0.33, l, ha="center", va="top", fontsize=10)

    anchors = [
        (0.00, "perfekt\nnegativ", "-1"),
        (0.20, "stark\nnegativ",   "-0.6"),
        (0.35, "moderat\nnegativ", "-0.3"),
        (0.50, "unkorreliert",     "0"),
        (0.65, "moderat\npositiv", "+0.3"),
        (0.80, "stark\npositiv",   "+0.6"),
        (1.00, "perfekt\npositiv", "+1"),
    ]
    for x, text, _ in anchors:
        ax.plot([x, x], [0.75, 0.85], color=HSLU, lw=1.5)
        ax.text(x, 0.88, text, ha="center", va="bottom", fontsize=10,
                fontweight="bold", color=HSLU)

    ax.set_xlim(-0.03, 1.03)
    ax.set_ylim(0, 1.15)
    ax.axis("off")
    ax.set_title("Interpretationsskala des Korrelationskoeffizienten $r$",
                 fontsize=13, color=HSLU, pad=10)
    save(fig, "r_skala.png")


# ---------------------------------------------------------------------------
# 4. Nicht-linearer Zusammenhang mit r=0
# ---------------------------------------------------------------------------
def fig_r_null_aber_zusammenhang():
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    # quadratisch
    x1 = rng.uniform(-5, 5, 150)
    y1 = x1 ** 2 + rng.normal(0, 1.5, 150)
    r1 = np.corrcoef(x1, y1)[0, 1]
    axes[0].scatter(x1, y1, alpha=0.6, color=HSLU, s=25)
    axes[0].set_title(f"Quadratisch\n$r = {r1:+.2f}$ – aber klar abhängig!", color=HSLU)

    # kreis
    t = rng.uniform(0, 2 * np.pi, 200)
    x2 = np.cos(t) + rng.normal(0, 0.05, 200)
    y2 = np.sin(t) + rng.normal(0, 0.05, 200)
    r2 = np.corrcoef(x2, y2)[0, 1]
    axes[1].scatter(x2, y2, alpha=0.6, color=HSLU, s=25)
    axes[1].set_aspect("equal")
    axes[1].set_title(f"Kreisförmig\n$r = {r2:+.2f}$ – strukturiert!", color=HSLU)

    # sinus
    x3 = rng.uniform(0, 4 * np.pi, 200)
    y3 = np.sin(x3) + rng.normal(0, 0.2, 200)
    r3 = np.corrcoef(x3, y3)[0, 1]
    axes[2].scatter(x3, y3, alpha=0.6, color=HSLU, s=25)
    axes[2].set_title(f"Sinusförmig\n$r = {r3:+.2f}$ – perfekt periodisch", color=HSLU)

    for ax in axes:
        ax.set_xlabel("$A$")
        ax.set_ylabel("$B$")
        ax.grid(alpha=0.3)

    fig.suptitle("Achtung: $r \\approx 0$ heisst nicht unabhängig – nur kein linearer Zusammenhang!",
                 fontsize=13, fontweight="bold", color=HSLU, y=1.02)
    save(fig, "r_null_aber_zusammenhang.png")


# ---------------------------------------------------------------------------
# 5. Grosse Datensätze: Scatter vs. Hexbin vs. KDE
# ---------------------------------------------------------------------------
def fig_grosse_datensaetze():
    n = 15000
    x = rng.normal(2000, 800, n)
    y = 200 * x + 50000 + rng.normal(0, 200000, n)
    x = np.clip(x, 100, 3500)
    y = np.clip(y, 0, 750000)

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.8))

    # Scatter
    axes[0].scatter(x, y, alpha=0.15, color=HSLU, s=5)
    axes[0].set_title(f"Streudiagramm ($n = {n}$)\n→ Punkte überlagern sich", color=HSLU)

    # Hexbin
    hb = axes[1].hexbin(x, y, gridsize=30, cmap="Purples", mincnt=1)
    axes[1].set_title("Hexbin\n→ Dichte in Sechsecken", color=HSLU)
    plt.colorbar(hb, ax=axes[1], label="Anzahl Punkte")

    # KDE
    sns.kdeplot(x=x, y=y, ax=axes[2], cmap="Purples", levels=8, fill=True, thresh=0.02)
    axes[2].set_title("KDE-Dichte-Höhenlinien\n→ glatte Dichtefunktion", color=HSLU)

    for ax in axes:
        ax.set_xlabel("Wohnfläche [sqft]")
        ax.set_ylabel("Steuerwert [$]")
        ax.set_xlim(100, 3500)
        ax.set_ylim(0, 750000)

    fig.suptitle("Drei Darstellungen desselben grossen Datensatzes",
                 fontsize=14, fontweight="bold", y=1.02)
    save(fig, "grosse_datensaetze.png")


# ---------------------------------------------------------------------------
# 6. Rangzahlen – Bindungen
# ---------------------------------------------------------------------------
def fig_rangzahlen():
    werte = ["genügend", "gut", "gut", "gut", "gut", "gut", "gut",
             "sehr gut", "sehr gut", "ausgezeichnet"]
    positionen = list(range(1, 11))
    rangzahlen = [1, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 8.5, 8.5, 10]

    fig, ax = plt.subplots(figsize=(14, 3.8))
    ax.axis("off")

    cell_w = 1.2
    x0 = 0.5

    # Label column
    ax.text(x0 - 0.2, 2.3, "Wert", ha="right", va="center",
            fontsize=11, fontweight="bold", color=HSLU)
    ax.text(x0 - 0.2, 1.4, "Rohposition", ha="right", va="center",
            fontsize=11, fontweight="bold", color=HSLU)
    ax.text(x0 - 0.2, 0.5, "Rangzahl $R$", ha="right", va="center",
            fontsize=11, fontweight="bold", color=HSLU)

    colors = []
    current_val = None
    c = 0
    for w in werte:
        if w != current_val:
            c += 1
            current_val = w
        colors.append(["#fff0f6", "#f5c6d9", "#fac0d5", "#e0008a"][(c - 1) % 4])

    for i, (w, p, r, col) in enumerate(zip(werte, positionen, rangzahlen, colors)):
        x = x0 + i * cell_w

        ax.add_patch(plt.Rectangle((x, 2.0), cell_w, 0.6,
                                   facecolor=col, edgecolor="black", lw=1))
        ax.text(x + cell_w / 2, 2.3, w, ha="center", va="center", fontsize=8.5)

        ax.add_patch(plt.Rectangle((x, 1.1), cell_w, 0.6,
                                   facecolor="white", edgecolor="black", lw=1))
        ax.text(x + cell_w / 2, 1.4, str(p), ha="center", va="center", fontsize=11)

        rang_color = HSLU if r != int(r) or r in (1, 10) else "black"
        fweight = "bold" if r != int(r) else "normal"
        ax.add_patch(plt.Rectangle((x, 0.2), cell_w, 0.6,
                                   facecolor="white", edgecolor=HSLU, lw=1.5))
        ax.text(x + cell_w / 2, 0.5, str(r), ha="center", va="center",
                fontsize=12, color=rang_color, fontweight=fweight)

    ax.text(x0 + 5 * cell_w + cell_w / 2 - 4.5 * cell_w / 2, -0.2,
            "← Bindung: 6× 'gut', alle bekommen Rang (2+3+4+5+6+7) / 6 = 4.5 →",
            ha="center", fontsize=10, style="italic", color=HSLU)

    ax.set_xlim(-2.7, x0 + 10 * cell_w + 0.5)
    ax.set_ylim(-0.6, 3.0)
    ax.set_title("Rangzahlen für Spearman: Umgang mit Bindungen",
                 fontsize=13, color=HSLU, pad=10)
    save(fig, "rangzahlen_bindungen.png")


# ---------------------------------------------------------------------------
# 7. Pearson vs. Spearman – wo sie sich unterscheiden
# ---------------------------------------------------------------------------
def fig_pearson_vs_spearman():
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    # linear – beide gleich
    n = 100
    x1 = rng.uniform(0, 10, n)
    y1 = 1.5 * x1 + rng.normal(0, 1.5, n)
    r_p = np.corrcoef(x1, y1)[0, 1]
    r_s = pd.Series(x1).corr(pd.Series(y1), method="spearman")
    axes[0].scatter(x1, y1, color=HSLU, alpha=0.6, s=25)
    axes[0].set_title(f"Linear\nPearson {r_p:+.2f}  |  Spearman {r_s:+.2f}", color=HSLU)

    # exponentiell / monoton nicht-linear – Spearman höher
    x2 = rng.uniform(0, 5, n)
    y2 = np.exp(x2) + rng.normal(0, 3, n)
    r_p = np.corrcoef(x2, y2)[0, 1]
    r_s = pd.Series(x2).corr(pd.Series(y2), method="spearman")
    axes[1].scatter(x2, y2, color=HSLU, alpha=0.6, s=25)
    axes[1].set_title(f"Monoton (exponentiell)\nPearson {r_p:+.2f}  |  Spearman {r_s:+.2f}", color=HSLU)

    # linear mit Ausreissern – Pearson stark verzerrt
    x3 = rng.uniform(0, 10, n)
    y3 = 1.0 * x3 + rng.normal(0, 0.5, n)
    y3[:3] = [30, 35, 25]
    r_p = np.corrcoef(x3, y3)[0, 1]
    r_s = pd.Series(x3).corr(pd.Series(y3), method="spearman")
    axes[2].scatter(x3, y3, color=HSLU, alpha=0.6, s=25)
    axes[2].set_title(f"Linear + Ausreisser\nPearson {r_p:+.2f}  |  Spearman {r_s:+.2f}", color=HSLU)

    for ax in axes:
        ax.set_xlabel("$A$")
        ax.set_ylabel("$B$")
        ax.grid(alpha=0.3)

    fig.suptitle("Pearson vs. Spearman: drei typische Szenarien",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.text(0.5, -0.05,
             "Links: beide identisch. Mitte: Spearman erkennt die monotone Struktur besser. "
             "Rechts: Ausreisser drücken Pearson, Spearman bleibt stabil.",
             ha="center", fontsize=10, style="italic")
    save(fig, "pearson_vs_spearman.png")


# ---------------------------------------------------------------------------
# 8. Kausalität vs. Korrelation – Wein & Mortalität
# ---------------------------------------------------------------------------
def fig_kausalitaet_wein():
    wein = [2.8, 3.2, 3.2, 3.4, 4.3, 4.9, 5.1, 5.2, 5.9, 5.9,
            6.6, 8.3, 12.6, 15.1, 25.1, 33.1, 75.9, 75.9]
    mort = [6.2, 9.0, 7.1, 6.8, 10.2, 7.8, 9.3, 5.9, 8.9, 5.5,
            7.1, 9.1, 5.1, 4.7, 4.7, 3.1, 3.2, 2.1]
    laender = ["NO", "SCO", "GB", "IRL", "FIN", "CAN", "USA", "NL",
               "NZ", "DK", "SE", "AUS", "BE", "DE", "AT", "CH", "IT", "FR"]

    r = np.corrcoef(wein, mort)[0, 1]
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.scatter(wein, mort, color=HSLU, s=70, alpha=0.8, edgecolor="white", linewidth=1)
    for x, y, l in zip(wein, mort, laender):
        ax.annotate(l, (x, y), xytext=(5, 5), textcoords="offset points",
                    fontsize=9, color="black")

    # trend line
    coef = np.polyfit(wein, mort, 1)
    xs = np.linspace(0, 80, 100)
    ax.plot(xs, np.polyval(coef, xs), color=HSLU, linestyle="--", lw=1.5,
            label=f"Regressionsgerade (r = {r:.2f})")

    ax.set_xlabel("Weinkonsum [Liter/Person·Jahr]")
    ax.set_ylabel("Mortalität [Todesfälle/1000 Personen]")
    ax.set_title(f"Wein & Herzmortalität: $r = {r:.2f}$ – aber Kausalität?",
                 color=HSLU)
    ax.legend(loc="upper right")
    ax.grid(alpha=0.3)
    ax.text(40, 8, "⚠  Frankreich & Italien haben hohen Weinkonsum\n"
                    "    UND Mittelmeerkost, Lebensstil, etc.\n"
                    "    → Confounder möglich!",
            fontsize=10, color=HSLU, style="italic",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff0f6",
                      edgecolor=HSLU, alpha=0.9))
    save(fig, "kausalitaet_wein.png")


# ---------------------------------------------------------------------------
# 9. Confounder-Diagramm
# ---------------------------------------------------------------------------
def fig_confounder():
    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.axis("off")

    # Boxes
    def box(x, y, w, h, text, color=HSLU, tc="white"):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                                    facecolor=color, edgecolor="black", lw=1.2))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=11, fontweight="bold", color=tc)

    box(0.5, 2.5, 2.5, 1.2, "Eisverkauf\n(Merkmal A)", color="#f5c6d9", tc="black")
    box(7.0, 2.5, 2.5, 1.2, "Sonnenbrand\n(Merkmal B)", color="#f5c6d9", tc="black")
    box(3.75, 0.3, 2.5, 1.2, "Sommer / Hitze\n(Confounder C)", color=HSLU)

    # Arrows (spurious correlation)
    ax.annotate("", xy=(6.95, 3.1), xytext=(3.05, 3.1),
                arrowprops=dict(arrowstyle="<->", color="red", lw=2, linestyle="--"))
    ax.text(5, 3.4, "beobachtete Korrelation  $r > 0$\n(Scheinkorrelation)",
            ha="center", fontsize=10, color="red", style="italic")

    # Arrows from confounder
    ax.annotate("", xy=(1.75, 2.45), xytext=(4.5, 1.45),
                arrowprops=dict(arrowstyle="->", color=HSLU, lw=2))
    ax.annotate("", xy=(8.25, 2.45), xytext=(5.5, 1.45),
                arrowprops=dict(arrowstyle="->", color=HSLU, lw=2))
    ax.text(2.5, 1.85, "verursacht", fontsize=9, color=HSLU, rotation=37, style="italic")
    ax.text(7.0, 1.85, "verursacht", fontsize=9, color=HSLU, rotation=-37, style="italic")

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.2)
    ax.set_title("Confounder erzeugen Scheinkorrelationen",
                 fontsize=13, color=HSLU, pad=10)
    save(fig, "confounder.png")


if __name__ == "__main__":
    print("Erzeuge Grafiken für SW10 ...")
    fig_korrelationsmuster()
    fig_kovarianz_quadranten()
    fig_r_skala()
    fig_r_null_aber_zusammenhang()
    fig_grosse_datensaetze()
    fig_rangzahlen()
    fig_pearson_vs_spearman()
    fig_kausalitaet_wein()
    fig_confounder()
    print(f"Fertig. Output-Ordner: {OUT}")
