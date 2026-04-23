"""Grafiken für ZUSAMMENFASSUNG_SW09.md erzeugen."""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.colors import LinearSegmentedColormap

HSLU = (160/255, 0/255, 86/255)
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


# ---------------------------------------------------------------------------
# 1. Kontingenztafel-Konzept (Heatmap mit Zeilen-/Spaltensummen)
# ---------------------------------------------------------------------------
def fig_kontingenztafel():
    data = np.array([[6, 4], [2, 3], [2, 2], [0, 1]])
    zeilensummen = data.sum(axis=1)
    spaltensummen = data.sum(axis=0)
    total = data.sum()

    fig, ax = plt.subplots(figsize=(7.5, 5.5))
    ax.axis("off")

    cell_w, cell_h = 1.4, 0.8
    x0, y0 = 1.5, 0.5

    ax.text(x0 + cell_w, y0 + 4.6 * cell_h, "Mann", ha="center", fontsize=12, fontweight="bold")
    ax.text(x0 + 2 * cell_w, y0 + 4.6 * cell_h, "Frau", ha="center", fontsize=12, fontweight="bold")
    ax.text(x0 + 3 * cell_w + 0.1, y0 + 4.6 * cell_h, "$n(A)$",
            ha="center", fontsize=12, fontweight="bold", color=HSLU)

    zeilen = ["braun", "grün", "blau", "grau"]
    for i, z in enumerate(zeilen):
        ax.text(x0 - 0.1, y0 + (3.5 - i) * cell_h + cell_h / 2, z,
                ha="right", va="center", fontsize=12, fontweight="bold")

    for i in range(4):
        for j in range(2):
            x = x0 + (j + 0.5) * cell_w
            y = y0 + (3.5 - i) * cell_h
            ax.add_patch(plt.Rectangle((x, y), cell_w, cell_h,
                                       fill=True, facecolor="#fff0f6",
                                       edgecolor="black", linewidth=1))
            ax.text(x + cell_w / 2, y + cell_h / 2, str(data[i, j]),
                    ha="center", va="center", fontsize=13)

    for i in range(4):
        x = x0 + 2.5 * cell_w
        y = y0 + (3.5 - i) * cell_h
        ax.add_patch(plt.Rectangle((x, y), cell_w, cell_h,
                                   fill=True, facecolor=HSLU, alpha=0.25,
                                   edgecolor=HSLU, linewidth=1.5))
        ax.text(x + cell_w / 2, y + cell_h / 2, str(zeilensummen[i]),
                ha="center", va="center", fontsize=13, fontweight="bold", color=HSLU)

    for j in range(2):
        x = x0 + (j + 0.5) * cell_w
        y = y0 - cell_h
        ax.add_patch(plt.Rectangle((x, y), cell_w, cell_h,
                                   fill=True, facecolor=HSLU, alpha=0.25,
                                   edgecolor=HSLU, linewidth=1.5))
        ax.text(x + cell_w / 2, y + cell_h / 2, str(spaltensummen[j]),
                ha="center", va="center", fontsize=13, fontweight="bold", color=HSLU)

    x = x0 + 2.5 * cell_w
    y = y0 - cell_h
    ax.add_patch(plt.Rectangle((x, y), cell_w, cell_h,
                               fill=True, facecolor=HSLU, alpha=0.5,
                               edgecolor=HSLU, linewidth=1.5))
    ax.text(x + cell_w / 2, y + cell_h / 2, f"n = {total}",
            ha="center", va="center", fontsize=13, fontweight="bold", color="white")

    ax.text(x0 - 0.7, y0 - cell_h / 2, "$n(B)$ →",
            ha="right", va="center", fontsize=12, fontweight="bold", color=HSLU)

    ax.annotate("Zeilensumme\n$n(a_i)$",
                xy=(x0 + 3 * cell_w, y0 + 3 * cell_h),
                xytext=(x0 + 4.2 * cell_w, y0 + 3.8 * cell_h),
                fontsize=10, color=HSLU,
                arrowprops=dict(arrowstyle="->", color=HSLU))
    ax.annotate("Spaltensumme\n$n(b_j)$",
                xy=(x0 + cell_w, y0 - cell_h / 2),
                xytext=(x0 - 1.2, y0 - 1.3 * cell_h),
                fontsize=10, color=HSLU,
                arrowprops=dict(arrowstyle="->", color=HSLU))

    ax.set_xlim(-0.5, 7.5)
    ax.set_ylim(-1.5, 5.5)
    ax.set_title("Kontingenztafel: Augenfarbe × Geschlecht (n = 20)",
                 fontsize=14, color=HSLU, pad=15)
    save(fig, "kontingenztafel_konzept.png")


# ---------------------------------------------------------------------------
# 2. Unabhängig vs. abhängig – gestapelte Stabdiagramme
# ---------------------------------------------------------------------------
def fig_unabhaengig_vs_abhaengig():
    data_un = np.array([[16, 4, 20, 8, 2],
                        [24, 6, 30, 12, 3]])
    data_ab = np.array([[18, 5, 30, 9, 4],
                        [22, 5, 20, 11, 1]])

    def verteilung_A(d):
        return d / d.sum(axis=0)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5.3))
    fig.subplots_adjust(wspace=0.35)

    for ax, d, title, C_korr in [
        (axes[0], data_un, "UNABHÄNGIG  ($C_{korr} = 0$)", 0.0),
        (axes[1], data_ab, "ABHÄNGIG  ($C_{korr} > 0$)", None),
    ]:
        va = verteilung_A(d)
        df = pd.DataFrame(va, columns=["$b_1$", "$b_2$", "$b_3$", "$b_4$", "$b_5$"],
                          index=["$a_1$", "$a_2$"])
        df.T.plot.bar(stacked=True, ax=ax, width=0.6, edgecolor="black",
                      color=[HSLU, "#f5c6d9"])
        ax.set_title(title, color=HSLU)
        ax.set_xlabel("Wert von $B$")
        ax.set_ylabel("relative Häufigkeit von $A$")
        ax.set_xticklabels(df.columns, rotation=0)
        ax.legend(title="$A$", loc="upper right", framealpha=0.95,
                  fontsize=9, title_fontsize=10)
        ax.set_ylim(0, 1.18)
        ax.grid(axis="y", alpha=0.3)

    fig.suptitle("Verteilung des Merkmals $A$ innerhalb der Werte von $B$",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.text(0.5, -0.06,
             "Links: Alle Stäbe gleich segmentiert → Randverteilung stimmt überall überein → $A$ und $B$ unabhängig.  "
             "Rechts: Segmente variieren → Merkmale hängen zusammen.",
             ha="center", fontsize=10, style="italic")
    save(fig, "unabhaengig_vs_abhaengig.png")


# ---------------------------------------------------------------------------
# 3. C_korr-Skala mit Interpretation
# ---------------------------------------------------------------------------
def fig_c_korr_skala():
    fig, ax = plt.subplots(figsize=(11, 3.2))

    cmap = LinearSegmentedColormap.from_list("hslu", ["#e8e8e8", HSLU])
    n = 200
    for i in range(n):
        ax.add_patch(plt.Rectangle((i / n, 0.4), 1 / n, 0.35,
                                   facecolor=cmap(i / n), edgecolor="none"))

    for pos in np.linspace(0, 1, 11):
        ax.plot([pos, pos], [0.38, 0.42], color="black", lw=1)
        ax.text(pos, 0.33, f"{pos:.1f}", ha="center", va="top", fontsize=10)

    labels = [
        (0.00, "unabhängig",       "bottom"),
        (0.25, "schwach",           "bottom"),
        (0.50, "mittel",            "bottom"),
        (0.75, "stark",             "bottom"),
        (1.00, "maximal\nabhängig", "bottom"),
    ]
    for x, text, va in labels:
        ax.plot([x, x], [0.75, 0.85], color=HSLU, lw=1.5)
        ax.text(x, 0.88, text, ha="center", va=va, fontsize=11,
                fontweight="bold", color=HSLU)

    ax.annotate("Beispiel: Geschlecht × Sport\n$C_{korr} \\approx 0.33$",
                xy=(0.33, 0.4), xytext=(0.33, 0.05),
                ha="center", fontsize=10,
                arrowprops=dict(arrowstyle="->", color="black"))

    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(0, 1.1)
    ax.axis("off")
    ax.set_title("Interpretationsskala des korrigierten Kontingenzkoeffizienten $C_{korr}$",
                 fontsize=13, color=HSLU, pad=10)
    save(fig, "c_korr_skala.png")


# ---------------------------------------------------------------------------
# 4. Broadcasting-Prinzip
# ---------------------------------------------------------------------------
def fig_broadcasting():
    fig, ax = plt.subplots(figsize=(11, 4.5))
    ax.axis("off")

    h_A = np.array([0.4, 0.6])
    h_B = np.array([0.32, 0.08, 0.40, 0.16, 0.04])
    produkt = np.outer(h_A, h_B)

    def draw_box(x, y, w, h, text, color="#fff0f6", text_color="black", fontsize=11):
        ax.add_patch(plt.Rectangle((x, y), w, h, facecolor=color,
                                   edgecolor="black", linewidth=1))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=fontsize, color=text_color)

    # h_A column
    ax.text(0.5, 3.6, "$h(A)$ als Spalte\n`.reshape(2, 1)`", ha="center",
            fontsize=11, fontweight="bold", color=HSLU)
    for i, v in enumerate(h_A):
        draw_box(0.2, 2.5 - i * 0.7, 0.6, 0.6, f"{v}", color="#f5c6d9")

    # times
    ax.text(1.3, 2.0, "×", ha="center", va="center", fontsize=28, fontweight="bold")

    # h_B row
    ax.text(3.7, 3.6, "$h(B)$ als Zeile\n`.reshape(1, 5)`", ha="center",
            fontsize=11, fontweight="bold", color=HSLU)
    for j, v in enumerate(h_B):
        draw_box(1.8 + j * 0.8, 2.3, 0.7, 0.6, f"{v}", color="#f5c6d9")

    # equals
    ax.text(6.2, 2.0, "=", ha="center", va="center", fontsize=28, fontweight="bold")

    # result matrix
    ax.text(8.5, 3.6, "Produkt $h(a_i)\\cdot h(b_j)$\n(Broadcasting)",
            ha="center", fontsize=11, fontweight="bold", color=HSLU)
    for i in range(2):
        for j in range(5):
            draw_box(6.6 + j * 0.8, 2.5 - i * 0.7, 0.7, 0.6,
                     f"{produkt[i, j]:.3f}", color="#fff0f6", fontsize=9)

    ax.text(5.5, 0.3,
            "Python kopiert die Spalte nach rechts und die Zeile nach unten, "
            "dann multipliziert es stellenweise.",
            ha="center", fontsize=10, style="italic")

    ax.set_xlim(-0.3, 11)
    ax.set_ylim(-0.3, 4.5)
    ax.set_title("Broadcasting: Spalte × Zeile = Matrix der Produkte",
                 fontsize=13, color=HSLU, pad=10)
    save(fig, "broadcasting.png")


# ---------------------------------------------------------------------------
# 5. Pearson-Residuen Heatmap (beobachtet vs. erwartet)
# ---------------------------------------------------------------------------
def fig_pearson_residuen():
    obs = np.array([[33, 17], [21, 29]])
    n = obs.sum()
    h = obs / n
    h_A = h.sum(axis=1, keepdims=True)
    h_B = h.sum(axis=0, keepdims=True)
    erw = h_A * h_B
    residuen = (h - erw) ** 2 / erw
    chi2 = residuen.sum()
    C_max = min(obs.shape) - 1
    C_korr = np.sqrt(1 + 1 / C_max) * np.sqrt(chi2 / (1 + chi2))

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
    fig.subplots_adjust(wspace=0.55)

    labels_x = ["ja", "nein"]
    labels_y = ["Mann", "Frau"]

    for ax, mat, title, fmt in [
        (axes[0], h, "Beobachtet $h(a_i, b_j)$", "{:.3f}"),
        (axes[1], erw, "Erwartet $h(a_i)\\cdot h(b_j)$", "{:.3f}"),
        (axes[2], residuen, "Quadr. Pearson-Residuen $R^2$", "{:.4f}"),
    ]:
        im = ax.imshow(mat, cmap="RdPu", vmin=0, vmax=mat.max() * 1.1)
        for i in range(mat.shape[0]):
            for j in range(mat.shape[1]):
                val = mat[i, j]
                color = "white" if val > mat.max() * 0.55 else "black"
                ax.text(j, i, fmt.format(val), ha="center", va="center",
                        fontsize=13, color=color, fontweight="bold")
        ax.set_xticks(range(len(labels_x)))
        ax.set_xticklabels(labels_x)
        ax.set_yticks(range(len(labels_y)))
        ax.set_yticklabels(labels_y)
        ax.set_xlabel("Sport treiben?")
        ax.set_title(title, color=HSLU)
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

    fig.suptitle(
        f"Geschlecht × Sport:  $\\chi^2$ = {chi2:.4f},  $C_{{korr}}$ = {C_korr:.3f}  (schwacher Zusammenhang)",
        fontsize=13, fontweight="bold", color=HSLU, y=1.02)
    save(fig, "pearson_residuen_sw09.png")


# ---------------------------------------------------------------------------
# 6. C_korr Extremfälle: 0, mitte, 1
# ---------------------------------------------------------------------------
def fig_extremfaelle():
    tafeln = [
        (np.array([[16, 4, 20, 8, 2], [24, 6, 30, 12, 3]]),
         "Unabhängig",  "$C_{korr} = 0.000$"),
        (np.array([[33, 17], [21, 29]]),
         "Schwacher Zusammenhang", "$C_{korr} \\approx 0.331$"),
        (np.array([[40, 0, 0], [0, 40, 20]]),
         "Maximal abhängig", "$C_{korr} = 1.000$"),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    for ax, (d, titel, ck_text) in zip(axes, tafeln):
        va = d / d.sum(axis=0)
        n_cols = d.shape[1]
        col_names = [f"$b_{{{j+1}}}$" for j in range(n_cols)]
        idx = [f"$a_{{{i+1}}}$" for i in range(d.shape[0])]
        df = pd.DataFrame(va, columns=col_names, index=idx)
        df.T.plot.bar(stacked=True, ax=ax, width=0.65, edgecolor="black",
                      color=[HSLU, "#f5c6d9", "#fac0d5"][:d.shape[0]])
        ax.set_title(f"{titel}\n{ck_text}", color=HSLU)
        ax.set_xlabel("Wert von $B$")
        ax.set_ylabel("relative Häufigkeit von $A$")
        ax.set_ylim(0, 1.02)
        ax.grid(axis="y", alpha=0.3)
        ax.set_xticklabels(col_names, rotation=0)
        ax.legend(title="$A$", loc="upper right", fontsize=9)

    fig.suptitle("Stabdiagramme für die drei Extremfälle von $C_{korr}$",
                 fontsize=14, fontweight="bold", color=HSLU, y=1.03)
    fig.text(0.5, -0.04,
             "Gleich segmentierte Stäbe (links) ↔ Unabhängigkeit.  "
             "Starke Segmentunterschiede (rechts) ↔ maximale Abhängigkeit.",
             ha="center", fontsize=10, style="italic")
    save(fig, "extremfaelle_c_korr.png")


# ---------------------------------------------------------------------------
# 7. Skalenniveaus → passende Zusammenhangsmasse
# ---------------------------------------------------------------------------
def fig_skalenniveaus():
    fig, ax = plt.subplots(figsize=(11, 4.5))
    ax.axis("off")

    niveaus = [
        ("NOMINAL",  "Augenfarbe, Geschlecht,\nRauchverhalten",
         "Kontingenztafel\n$C_{korr}$", "#f5c6d9"),
        ("ORDINAL",  "Schulnoten,\nZufriedenheitsstufen",
         "+ gerichteter Zshg.\nRangkorrelation", "#f2a6c4"),
        ("METRISCH", "Körpergrösse, Gewicht,\nEinkommen",
         "+ lineare Korrelation\nPearson-Koeffizient", HSLU),
    ]

    for i, (name, bsp, mass, color) in enumerate(niveaus):
        x = 0.5 + i * 3.5
        ax.add_patch(FancyBboxPatch((x, 2.4), 3, 1.8,
                                    boxstyle="round,pad=0.05",
                                    facecolor=color, alpha=0.9,
                                    edgecolor="black", linewidth=1.2))
        ax.text(x + 1.5, 3.8, name, ha="center", fontsize=13,
                fontweight="bold", color="white" if i == 2 else "black")
        ax.text(x + 1.5, 3.0, bsp, ha="center", fontsize=10,
                color="white" if i == 2 else "black")

        ax.annotate("", xy=(x + 1.5, 1.8), xytext=(x + 1.5, 2.4),
                    arrowprops=dict(arrowstyle="->", color="black", lw=1.5))

        ax.add_patch(FancyBboxPatch((x, 0.2), 3, 1.5,
                                    boxstyle="round,pad=0.05",
                                    facecolor="white",
                                    edgecolor=HSLU, linewidth=1.5))
        ax.text(x + 1.5, 0.95, mass, ha="center", va="center",
                fontsize=11, fontweight="bold", color=HSLU)

    ax.set_xlim(0, 12)
    ax.set_ylim(-0.2, 4.5)
    ax.text(6, 4.4, "SW 09 behandelt die linke Säule: nominale Merkmale",
            ha="center", fontsize=11, style="italic", color=HSLU)
    ax.set_title("Skalenniveau bestimmt das passende Zusammenhangsmass",
                 fontsize=14, color=HSLU, pad=10)
    save(fig, "skalenniveaus.png")


if __name__ == "__main__":
    print("Erzeuge Grafiken für SW09 ...")
    fig_kontingenztafel()
    fig_unabhaengig_vs_abhaengig()
    fig_c_korr_skala()
    fig_broadcasting()
    fig_pearson_residuen()
    fig_extremfaelle()
    fig_skalenniveaus()
    print(f"Fertig. Output-Ordner: {OUT}")
