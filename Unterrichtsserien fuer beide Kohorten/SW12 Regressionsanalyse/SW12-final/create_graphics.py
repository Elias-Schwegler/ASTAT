"""Grafiken für ZUSAMMENFASSUNG_SW12.md erzeugen."""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from scipy.optimize import minimize

HSLU = (160 / 255, 0 / 255, 86 / 255)
HSLU_LIGHT = (160 / 255, 0 / 255, 86 / 255, 0.3)
BLUE = (0 / 255, 90 / 255, 156 / 255)
ORANGE = (230 / 255, 130 / 255, 0 / 255)
GREEN = (40 / 255, 140 / 255, 50 / 255)

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
# 1. Multiple Regression mit 2 Prädiktoren als 3D-Ebene
# ---------------------------------------------------------------------------
def fig_multiple_regression_3d():
    n = 150
    X1 = rng.uniform(0, 200, n)        # TV
    X2 = rng.uniform(0, 50, n)         # Radio
    Y = 0.045 * X1 + 0.19 * X2 + 3.0 + rng.normal(0, 1.5, n)

    # Fit
    X_design = np.column_stack([X1, X2, np.ones(n)])
    coef, *_ = np.linalg.lstsq(X_design, Y, rcond=None)
    a1, a2, b = coef

    fig = plt.figure(figsize=(15, 5.5))

    # 3D-Punktwolke + Ebene
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    ax.scatter(X1, X2, Y, color=HSLU, alpha=0.6, s=22, edgecolor="white")
    x1g, x2g = np.meshgrid(np.linspace(0, 200, 20), np.linspace(0, 50, 20))
    yg = a1 * x1g + a2 * x2g + b
    ax.plot_surface(x1g, x2g, yg, color=BLUE, alpha=0.25, edgecolor=BLUE,
                    linewidth=0.3)
    ax.set_xlabel("TV", labelpad=2)
    ax.set_ylabel("Radio", labelpad=2)
    ax.set_zlabel("Verkauf")
    ax.set_title("Multiple lineare Regression\n(Modell ist eine Ebene)",
                 color=HSLU)
    ax.view_init(elev=22, azim=-60)

    # Residuen-Ansicht: predict vs. actual
    ax2 = fig.add_subplot(1, 2, 2)
    y_hat = a1 * X1 + a2 * X2 + b
    ax2.scatter(y_hat, Y, color=HSLU, alpha=0.65, s=28,
                edgecolor="white", linewidth=0.5)
    lims = [min(Y.min(), y_hat.min()) - 1, max(Y.max(), y_hat.max()) + 1]
    ax2.plot(lims, lims, "--", color="gray", lw=1.5, label="ideal $y=\\hat y$")
    ax2.set_xlabel("Vorhersage $\\hat y = \\hat a_1\\,X_1 + \\hat a_2\\,X_2 + \\hat b$")
    ax2.set_ylabel("Beobachtung $y$")
    ax2.set_title("Vorhersage vs. Beobachtung", color=HSLU)
    ax2.grid(alpha=0.3)
    ax2.legend(loc="upper left")
    ax2.text(0.05, 0.92,
             f"$\\hat a_1 = {a1:.3f}$\n$\\hat a_2 = {a2:.3f}$\n$\\hat b = {b:.2f}$",
             transform=ax2.transAxes, va="top", fontsize=10,
             bbox=dict(boxstyle="round", fc="white", ec=HSLU, alpha=0.85))

    plt.tight_layout()
    save(fig, "multiple_regression_3d.png")


# ---------------------------------------------------------------------------
# 2. In-Sample vs. Out-of-Sample – Überanpassung
# ---------------------------------------------------------------------------
def fig_in_vs_out_sample():
    n = 25
    X = rng.uniform(0, 10, n)
    X.sort()
    Y = 1.2 * X + 1 + rng.normal(0, 1.5, n)

    grades = np.arange(1, 13)
    rss_train, rss_test = [], []
    # 70/30 Split deterministisch
    idx = np.arange(n)
    rng.shuffle(idx)
    train, test = idx[:18], idx[18:]
    Xtr, Ytr = X[train], Y[train]
    Xte, Yte = X[test], Y[test]
    for d in grades:
        coef = np.polyfit(Xtr, Ytr, d)
        p = np.poly1d(coef)
        rss_train.append(np.mean((Ytr - p(Xtr)) ** 2))
        rss_test.append(np.mean((Yte - p(Xte)) ** 2))

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Polynom-Fit-Vergleich
    x_grid = np.linspace(0, 10, 200)
    axes[0].scatter(Xtr, Ytr, color=HSLU, label="Trainingsdaten", s=35,
                    edgecolor="white", zorder=3)
    axes[0].scatter(Xte, Yte, color=ORANGE, label="Test-Daten", s=55,
                    marker="D", edgecolor="white", zorder=3)
    for d, col in zip([1, 4, 10], [BLUE, GREEN, "crimson"]):
        coef = np.polyfit(Xtr, Ytr, d)
        p = np.poly1d(coef)
        axes[0].plot(x_grid, p(x_grid), color=col, lw=2,
                     label=f"Grad {d}")
    axes[0].set_ylim(Y.min() - 3, Y.max() + 3)
    axes[0].set_xlabel("$X$")
    axes[0].set_ylabel("$Y$")
    axes[0].set_title("Modelle steigender Komplexität\nauf denselben Trainingsdaten",
                      color=HSLU)
    axes[0].legend(loc="upper left", fontsize=9)
    axes[0].grid(alpha=0.3)

    # MSE-Kurve
    axes[1].plot(grades, rss_train, "o-", color=BLUE, lw=2,
                 label="In-Sample (Training)")
    axes[1].plot(grades, rss_test, "s-", color=ORANGE, lw=2,
                 label="Out-of-Sample (Test)")
    axes[1].set_xlabel("Modellkomplexität (Polynomgrad)")
    axes[1].set_ylabel("mittlerer quadratischer Fehler")
    axes[1].set_yscale("log")
    axes[1].set_title("In-Sample sinkt immer –\nOut-of-Sample steigt bei Überanpassung",
                      color=HSLU)
    axes[1].legend(loc="upper left")
    axes[1].grid(alpha=0.3, which="both")
    # Markiere Sweet Spot
    best = grades[np.argmin(rss_test)]
    axes[1].axvline(best, color=HSLU, lw=1.5, ls="--")
    axes[1].text(best + 0.3, axes[1].get_ylim()[1] * 0.5,
                 f"Sweet Spot\n(Grad {best})", color=HSLU, fontsize=10)

    plt.tight_layout()
    save(fig, "in_vs_out_sample.png")


# ---------------------------------------------------------------------------
# 3. k-fache Kreuzvalidierung visuell
# ---------------------------------------------------------------------------
def fig_kreuzvalidierung():
    k = 5
    n_blocks = 20
    fig, ax = plt.subplots(figsize=(13, 4.5))

    for fold in range(k):
        for block in range(n_blocks):
            is_test = (block // (n_blocks // k)) == fold
            color = ORANGE if is_test else BLUE
            ax.barh(fold, 1, left=block, color=color, edgecolor="white",
                    linewidth=2, height=0.85)
        ax.text(-0.5, fold, f"Fold {fold + 1}", ha="right", va="center",
                fontsize=11, color=HSLU)

    ax.set_xlim(-2, n_blocks + 0.5)
    ax.set_ylim(-0.6, k - 0.4)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.invert_yaxis()
    ax.set_title(f"{k}-fache Kreuzvalidierung – pro Durchlauf wird ein anderer Block (orange) zum Testen verwendet",
                 color=HSLU)

    # Legende
    ax.barh(-1.3, 1, left=0, color=BLUE, edgecolor="white", linewidth=2,
            height=0.6)
    ax.text(1.3, -1.3, "Training (fit)", va="center", fontsize=11)
    ax.barh(-1.3, 1, left=6, color=ORANGE, edgecolor="white", linewidth=2,
            height=0.6)
    ax.text(7.3, -1.3, "Test (RMSE)", va="center", fontsize=11)
    ax.set_ylim(-1.8, k - 0.4)
    ax.invert_yaxis()

    # Box rechts
    ax.text(n_blocks + 1, (k - 1) / 2,
            "Gütemass = Mittelwert\nder $k$ RMSE-Werte\n→ ehrliche\nAus-Sample-Schätzung",
            va="center", fontsize=10,
            bbox=dict(boxstyle="round", fc="white", ec=HSLU))

    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.tight_layout()
    save(fig, "kreuzvalidierung.png")


# ---------------------------------------------------------------------------
# 4. Dummy-Variablen – Codierungsschema
# ---------------------------------------------------------------------------
def fig_dummy_variablen():
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Links: 0/1-Codierung Geschlecht
    data_g = pd.DataFrame({
        "Person": ["P1", "P2", "P3", "P4", "P5"],
        "Geschlecht": ["Mann", "Frau", "Frau", "Mann", "Frau"],
        "G_Mann": [1, 0, 0, 1, 0],
    })
    ax = axes[0]
    ax.axis("off")
    tbl = ax.table(cellText=data_g.values,
                   colLabels=data_g.columns,
                   loc="center", cellLoc="center",
                   colColours=[HSLU_LIGHT] * 3)
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(11)
    tbl.scale(1, 1.8)
    ax.set_title("Binäres Merkmal → 1 Dummy\n(Baseline = Frau)", color=HSLU, pad=20)

    # Rechts: 3-stufig Blutgruppe
    data_b = pd.DataFrame({
        "Person": ["P1", "P2", "P3", "P4", "P5"],
        "Blutgruppe": ["A", "AB", "B", "A", "AB"],
        "BG_A": [1, 0, 0, 1, 0],
        "BG_B": [0, 0, 1, 0, 0],
    })
    ax = axes[1]
    ax.axis("off")
    tbl = ax.table(cellText=data_b.values,
                   colLabels=data_b.columns,
                   loc="center", cellLoc="center",
                   colColours=[HSLU_LIGHT] * 4)
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(11)
    tbl.scale(1, 1.8)
    ax.set_title("3-stufiges Merkmal → 2 Dummies\n(Baseline = AB)", color=HSLU, pad=20)

    fig.suptitle("Dummy-Codierung: für $k$ Kategorien braucht es genau $k-1$ Dummies",
                 fontsize=13, color=HSLU, fontweight="bold", y=1.02)
    plt.tight_layout()
    save(fig, "dummy_variablen.png")


# ---------------------------------------------------------------------------
# 5. AIC + Vorwärtsselektion: U-Kurve
# ---------------------------------------------------------------------------
def fig_aic_vorwaertsselektion():
    # Synthetische AIC-Kurve mit klarem Minimum
    schritte = np.arange(1, 9)
    rss = np.array([1200, 720, 480, 360, 320, 310, 308, 307])
    k = schritte + 1                       # Anzahl Parameter = #Prädiktoren + Intercept
    n = 200
    aic = 2 * k + n * np.log(rss / n)
    best = int(np.argmin(aic))

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # AIC-Kurve
    axes[0].plot(schritte, aic, "o-", color=HSLU, lw=2.5, markersize=9)
    axes[0].scatter([schritte[best]], [aic[best]], color="gold",
                    edgecolor=HSLU, s=300, marker="*", zorder=5,
                    label=f"Minimum bei {schritte[best]} Prädiktoren")
    axes[0].set_xlabel("Anzahl Prädiktoren im Modell")
    axes[0].set_ylabel("AIC = $2k + n\\,\\ln(\\mathsf{RSS}/n)$")
    axes[0].set_title("AIC sinkt – steigt wieder bei Überanpassung",
                      color=HSLU)
    axes[0].grid(alpha=0.3)
    axes[0].legend(loc="upper right")

    # Zerlegung in Strafterm und Belohnung
    bonus = n * np.log(rss / n)
    strafe = 2 * k
    axes[1].plot(schritte, bonus, "s-", color=BLUE, lw=2,
                 label="$n\\,\\ln(\\mathsf{RSS}/n)$  Belohnung")
    axes[1].plot(schritte, strafe, "^-", color=ORANGE, lw=2,
                 label="$2k$  Strafterm")
    axes[1].plot(schritte, aic, "o-", color=HSLU, lw=2.5,
                 label="AIC (Summe)")
    axes[1].set_xlabel("Anzahl Prädiktoren")
    axes[1].set_ylabel("Wert")
    axes[1].set_title("AIC = Belohnung + Strafterm", color=HSLU)
    axes[1].grid(alpha=0.3)
    axes[1].legend(loc="center right")

    plt.tight_layout()
    save(fig, "aic_vorwaertsselektion.png")


# ---------------------------------------------------------------------------
# 6. Multikollinearität: korrelierte Prädiktoren → instabile Schätzungen
# ---------------------------------------------------------------------------
def fig_multikollinearitaet():
    # Zwei stark korrelierte Prädiktoren
    n = 80
    X1 = rng.normal(0, 1, n)
    X2 = 0.95 * X1 + rng.normal(0, 0.3, n)
    Y = 2 * X1 + 0 * X2 + rng.normal(0, 1, n)  # wahrer Effekt liegt auf X1

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Korrelations-Scatter
    axes[0].scatter(X1, X2, color=HSLU, alpha=0.65, s=35,
                    edgecolor="white", linewidth=0.5)
    r = np.corrcoef(X1, X2)[0, 1]
    axes[0].set_xlabel("$X_1$ (z.B. Rating)")
    axes[0].set_ylabel("$X_2$ (z.B. Limit)")
    axes[0].set_title(f"Korrelation der Prädiktoren: $r = {r:.2f}$\n→ kollinear",
                      color=HSLU)
    axes[0].grid(alpha=0.3)

    # Bootstrap-Verteilung der Gewichte
    n_boot = 400
    a1s, a2s = [], []
    for _ in range(n_boot):
        idx = rng.integers(0, n, n)
        Xs = np.column_stack([X1[idx], X2[idx], np.ones(n)])
        Ys = Y[idx]
        coef, *_ = np.linalg.lstsq(Xs, Ys, rcond=None)
        a1s.append(coef[0])
        a2s.append(coef[1])

    axes[1].scatter(a1s, a2s, color=HSLU, alpha=0.4, s=18)
    axes[1].axhline(0, color="gray", lw=1, ls="--")
    axes[1].axvline(0, color="gray", lw=1, ls="--")
    axes[1].set_xlabel("$\\hat a_1$ (Gewicht von $X_1$)")
    axes[1].set_ylabel("$\\hat a_2$ (Gewicht von $X_2$)")
    axes[1].set_title("Bootstrap der Gewichte – starke negative\nKorrelation der Schätzungen",
                      color=HSLU)
    axes[1].grid(alpha=0.3)

    plt.tight_layout()
    save(fig, "multikollinearitaet.png")


# ---------------------------------------------------------------------------
# 7. Vergleich R² nimmt monoton zu, RSE kann fallen UND steigen
# ---------------------------------------------------------------------------
def fig_r2_vs_rse():
    n = 150
    X1 = rng.uniform(0, 100, n)
    X2 = rng.uniform(0, 50, n)
    X3_noise = rng.uniform(0, 30, n)
    Y = 0.05 * X1 + 0.18 * X2 + rng.normal(0, 1.5, n)

    models = {
        "nur X1": np.column_stack([X1, np.ones(n)]),
        "X1+X2": np.column_stack([X1, X2, np.ones(n)]),
        "X1+X2+X3\n(Rauschen)": np.column_stack([X1, X2, X3_noise, np.ones(n)]),
    }
    r2_vals, rse_vals, labels = [], [], []
    for label, Xd in models.items():
        coef, *_ = np.linalg.lstsq(Xd, Y, rcond=None)
        y_hat = Xd @ coef
        rss = np.sum((Y - y_hat) ** 2)
        r2 = np.var(y_hat) / np.var(Y)
        m = Xd.shape[1] - 1  # ohne Intercept
        rse = np.sqrt(rss / (n - (m + 1)))
        r2_vals.append(r2)
        rse_vals.append(rse)
        labels.append(label)

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    bars = axes[0].bar(labels, r2_vals, color=[BLUE, HSLU, ORANGE],
                       edgecolor="white", linewidth=2)
    for b, v in zip(bars, r2_vals):
        axes[0].text(b.get_x() + b.get_width() / 2, v + 0.005,
                     f"{v:.4f}", ha="center", fontsize=11, fontweight="bold")
    axes[0].set_ylabel("$R^2$")
    axes[0].set_ylim(0, max(r2_vals) * 1.15)
    axes[0].set_title("$R^2$ steigt (oder bleibt gleich)\nmit jedem zusätzlichen Prädiktor",
                      color=HSLU)
    axes[0].grid(alpha=0.3, axis="y")

    bars = axes[1].bar(labels, rse_vals, color=[BLUE, HSLU, ORANGE],
                       edgecolor="white", linewidth=2)
    for b, v in zip(bars, rse_vals):
        axes[1].text(b.get_x() + b.get_width() / 2, v + 0.02,
                     f"{v:.3f}", ha="center", fontsize=11, fontweight="bold")
    axes[1].set_ylabel("$\\mathsf{RSE}$")
    axes[1].set_title("$\\mathsf{RSE}$ kann steigen,\nwenn unnötige Prädiktoren dabei sind",
                      color=HSLU)
    axes[1].grid(alpha=0.3, axis="y")

    plt.tight_layout()
    save(fig, "r2_vs_rse.png")


# ---------------------------------------------------------------------------
# 8. Vorwärtsselektion: schrittweise wachsendes Modell
# ---------------------------------------------------------------------------
def fig_vorwaertsselektion_flow():
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.axis("off")

    pools = [
        ("Start\n(nur Achsenabschnitt)", ["?", "?", "?", "?", "?"], None),
        ("Schritt 1", ["X1", "?", "?", "?", "?"], 0),
        ("Schritt 2", ["X1", "X3", "?", "?", "?"], 1),
        ("Schritt 3", ["X1", "X3", "X2", "?", "?"], 2),
        ("Schritt 4\n(AIC steigt → STOP)", ["X1", "X3", "X2", "✗", "?"], 3),
    ]

    box_w, box_h = 2.6, 0.7
    for i, (title, slots, hl) in enumerate(pools):
        cx = i * 3
        ax.text(cx + box_w / 2, 4.4, title, ha="center", fontsize=10,
                color=HSLU, fontweight="bold")
        for j, s in enumerate(slots):
            color = "white"
            edge = HSLU
            if s != "?" and s != "✗":
                color = HSLU_LIGHT
            if s == "✗":
                color = "#ffd7d7"
                edge = "red"
            ax.add_patch(plt.Rectangle((cx, 3.5 - j * 0.8), box_w, box_h,
                                       facecolor=color, edgecolor=edge,
                                       linewidth=1.5))
            ax.text(cx + box_w / 2, 3.5 - j * 0.8 + box_h / 2, s,
                    ha="center", va="center", fontsize=11)
        if i < len(pools) - 1:
            ax.annotate("", xy=(cx + box_w + 0.3, 2),
                        xytext=(cx + box_w - 0.05, 2),
                        arrowprops=dict(arrowstyle="->", color=HSLU, lw=2))

    ax.set_xlim(-0.5, len(pools) * 3 - 0.2)
    ax.set_ylim(-1, 5)
    ax.set_title("Vorwärtsselektion: in jedem Schritt wird der Prädiktor\naufgenommen, der die RSS am stärksten reduziert – bis AIC wieder steigt",
                 color=HSLU)

    save(fig, "vorwaertsselektion_flow.png")


if __name__ == "__main__":
    print("Erzeuge Grafiken für SW12 …")
    fig_multiple_regression_3d()
    fig_in_vs_out_sample()
    fig_kreuzvalidierung()
    fig_dummy_variablen()
    fig_aic_vorwaertsselektion()
    fig_multikollinearitaet()
    fig_r2_vs_rse()
    fig_vorwaertsselektion_flow()
    print("Fertig.")
