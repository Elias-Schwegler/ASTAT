"""Grafiken für ZUSAMMENFASSUNG_SW11.md erzeugen."""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

HSLU = (160 / 255, 0 / 255, 86 / 255)
HSLU_LIGHT = (160 / 255, 0 / 255, 86 / 255, 0.3)
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
# 1. Regression Grundidee: 3-Panel Story
# ---------------------------------------------------------------------------
def fig_regression_grundidee():
    n = 200
    X = rng.uniform(0, 15, n)
    Y = 0.7 * X + 3 + rng.normal(0, 1.5, n)
    a_true, b_true = 0.7, 3.0

    # OLS-Fit
    def model(x, a, b):
        return a * x + b

    def rss(p):
        return np.sum((Y - model(X, p[0], p[1])) ** 2)

    fit = minimize(rss, x0=np.array([0.1, 0.1]))
    a_hat, b_hat = fit.x

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    x_grid = np.linspace(0, 15, 100)

    # Panel 1: Wahre Beziehung
    axes[0].scatter(X, Y, alpha=0.55, color=HSLU, s=22,
                    edgecolor="white", linewidth=0.5, zorder=2)
    axes[0].plot(x_grid, a_true * x_grid + b_true,
                 color="green", lw=2.5, label="wahres Modell", zorder=3)
    axes[0].set_title("1. Daten + wahres Modell\n(in der Praxis unbekannt)",
                      color=HSLU)
    axes[0].set_xlabel("Prädiktor $X$")
    axes[0].set_ylabel("Zielgrösse $Y$")
    axes[0].legend(loc="lower right")
    axes[0].grid(alpha=0.3)

    # Panel 2: Geschätztes Modell aus den Daten
    axes[1].scatter(X, Y, alpha=0.55, color=HSLU, s=22,
                    edgecolor="white", linewidth=0.5, zorder=2)
    axes[1].plot(x_grid, a_hat * x_grid + b_hat,
                 color="red", lw=2.5,
                 label=f"$\\hat{{y}} = {a_hat:.2f}\\,x + {b_hat:.2f}$",
                 zorder=3)
    axes[1].set_title("2. Geschätzte Regressionsgerade\n(rot)", color=HSLU)
    axes[1].set_xlabel("Prädiktor $X$")
    axes[1].set_ylabel("Zielgrösse $Y$")
    axes[1].legend(loc="lower right")
    axes[1].grid(alpha=0.3)

    # Panel 3: Residuen
    y_hat = a_hat * X + b_hat
    axes[2].vlines(X, y_hat, Y, color="red", lw=0.8,
                   linestyles="dashed", alpha=0.7, zorder=2)
    axes[2].scatter(X, Y, alpha=0.7, color=HSLU, s=22,
                    edgecolor="white", linewidth=0.5, zorder=3)
    axes[2].plot(x_grid, a_hat * x_grid + b_hat,
                 color="red", lw=2.5, zorder=4)
    axes[2].set_title("3. Residuen $r_i = y_i - \\hat{y}_i$\n"
                      "(rote gestrichelte Linien)", color=HSLU)
    axes[2].set_xlabel("Prädiktor $X$")
    axes[2].set_ylabel("Zielgrösse $Y$")
    axes[2].grid(alpha=0.3)

    fig.suptitle("Die Idee der Regressionsanalyse",
                 fontsize=15, fontweight="bold", y=1.02)
    fig.tight_layout()
    save(fig, "regression_grundidee.png")


# ---------------------------------------------------------------------------
# 2. RSS-Minimierung: Konturlandschaft + verschiedene Geraden
# ---------------------------------------------------------------------------
def fig_rss_minimierung():
    n = 80
    X = rng.uniform(0, 15, n)
    Y = 0.7 * X + 3 + rng.normal(0, 1.5, n)

    def rss_grid(a, b):
        residuen = Y[:, None, None] - (a[None, :, :] * X[:, None, None]
                                       + b[None, :, :])
        return (residuen ** 2).sum(axis=0)

    a_vals = np.linspace(-0.2, 1.5, 80)
    b_vals = np.linspace(-2, 8, 80)
    A, B = np.meshgrid(a_vals, b_vals)
    RSS_surface = rss_grid(A, B)

    # Optimum
    def rss_pair(p):
        return np.sum((Y - (p[0] * X + p[1])) ** 2)

    fit = minimize(rss_pair, x0=np.array([0.1, 0.1]))
    a_opt, b_opt = fit.x

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Linke Tafel: Höhenlinien
    levels = np.geomspace(RSS_surface.min() * 1.01,
                          RSS_surface.max(), 18)
    cs = axes[0].contourf(A, B, RSS_surface, levels=levels,
                          cmap="magma_r", alpha=0.85)
    axes[0].contour(A, B, RSS_surface, levels=levels[::3],
                    colors="white", linewidths=0.5, alpha=0.6)
    axes[0].plot(a_opt, b_opt, marker="*", color="gold",
                 markersize=24, markeredgecolor="black",
                 markeredgewidth=1.5,
                 label=f"Minimum\n$(\\hat a, \\hat b) = ({a_opt:.2f}, {b_opt:.2f})$")
    axes[0].set_xlabel("Steigung $a$")
    axes[0].set_ylabel("Achsenabschnitt $b$")
    axes[0].set_title("$\\mathsf{RSS}(a, b)$ als Höhenlandschaft",
                      color=HSLU)
    axes[0].legend(loc="upper right", fontsize=10)
    cbar = fig.colorbar(cs, ax=axes[0], shrink=0.85)
    cbar.set_label("$\\mathsf{RSS}$", labelpad=12)

    # Rechte Tafel: Drei Geraden zum Vergleich
    cands = [
        (1.4, -1.0, "blue", "schlecht (zu steil)"),
        (0.3, 5.0, "orange", "mittelmässig"),
        (a_opt, b_opt, "red", "OLS-Optimum"),
    ]
    axes[1].scatter(X, Y, alpha=0.55, color=HSLU, s=24,
                    edgecolor="white", linewidth=0.5, zorder=2)
    x_grid = np.linspace(0, 15, 80)
    for a, b, c, label in cands:
        rss_val = np.sum((Y - (a * X + b)) ** 2)
        axes[1].plot(x_grid, a * x_grid + b, color=c, lw=2.5,
                     label=f"{label}: RSS={rss_val:.0f}", zorder=3)
    axes[1].set_xlabel("Prädiktor $X$")
    axes[1].set_ylabel("Zielgrösse $Y$")
    axes[1].set_title("Drei Geradenkandidaten\n(Optimum minimiert RSS)",
                      color=HSLU)
    axes[1].legend(loc="upper left", fontsize=10)
    axes[1].grid(alpha=0.3)

    fig.suptitle("Methode der kleinsten Quadrate – $\\mathsf{RSS}$ minimieren",
                 fontsize=15, fontweight="bold", y=1.02)
    fig.tight_layout()
    save(fig, "rss_minimierung.png")


# ---------------------------------------------------------------------------
# 3. MQD im Modell vs. MQD in den Daten
# ---------------------------------------------------------------------------
def fig_mqd_modell_vs_daten():
    n = 200
    X = rng.uniform(0, 15, n)
    Y = 0.7 * X + 3 + rng.normal(0, 1.5, n)

    def model(x, a, b):
        return a * x + b

    def rss(p):
        return np.sum((Y - model(X, p[0], p[1])) ** 2)

    fit = minimize(rss, x0=np.array([0.1, 0.1]))
    a_hat, b_hat = fit.x
    y_hat = a_hat * X + b_hat
    y_mean = Y.mean()
    x_mean = X.mean()

    R2 = y_hat.var() / Y.var()

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    x_grid = np.linspace(0, 15, 100)

    # Links: MQD im Modell
    ax1 = axes[0]
    ax1.axhline(y_mean, color="grey", lw=1)
    ax1.axvline(x_mean, color="grey", lw=1)
    ax1.vlines(X, y_hat, y_mean,
               linestyles="dashed", lw=0.6, color="red", alpha=0.7)
    ax1.scatter(X, Y, alpha=0.25, color=HSLU, s=20,
                edgecolor="white", linewidth=0.4)
    ax1.plot(x_grid, a_hat * x_grid + b_hat,
             color="red", lw=2.8, zorder=3)
    ax1.set_title("MQD im Modell (Zähler von $R^2$)\n"
                  "= durch Modell $\\mathit{erklärte}$ Streuung",
                  color=HSLU)
    ax1.set_xlabel("Prädiktor $X$")
    ax1.set_ylabel("Zielgrösse $Y$")
    ax1.grid(alpha=0.3)

    # Rechts: MQD in den Daten
    ax2 = axes[1]
    ax2.axhline(y_mean, color="grey", lw=1)
    ax2.axvline(x_mean, color="grey", lw=1)
    ax2.vlines(X, Y, y_mean,
               linestyles="dashed", lw=0.6, color="blue", alpha=0.7)
    ax2.scatter(X, Y, alpha=0.7, color=HSLU, s=22,
                edgecolor="white", linewidth=0.4)
    ax2.plot(x_grid, a_hat * x_grid + b_hat,
             color="red", lw=2.8, alpha=0.4, zorder=3)
    ax2.set_title("MQD in den Daten (Nenner von $R^2$)\n"
                  "= $\\mathit{gesamte}$ Streuung von $Y$",
                  color=HSLU)
    ax2.set_xlabel("Prädiktor $X$")
    ax2.set_ylabel("Zielgrösse $Y$")
    ax2.grid(alpha=0.3)

    fig.suptitle(f"Bestimmtheitsmass $R^2 = $ MQD im Modell / MQD in den Daten "
                 f"$= {R2:.2f}$",
                 fontsize=15, fontweight="bold", y=1.02)
    fig.tight_layout()
    save(fig, "mqd_modell_vs_daten.png")


# ---------------------------------------------------------------------------
# 4. R²-Galerie: vier Streudiagramme mit unterschiedlichem R²
# ---------------------------------------------------------------------------
def fig_r2_galerie():
    fig, axes = plt.subplots(1, 4, figsize=(17, 4.5))

    n = 80
    a_true, b_true = 0.6, 2.0
    sigmas = [0.4, 1.2, 2.5, 5.5]

    for ax, sigma in zip(axes, sigmas):
        X = rng.uniform(0, 15, n)
        Y = a_true * X + b_true + rng.normal(0, sigma, n)

        def rss(p, X=X, Y=Y):
            return np.sum((Y - (p[0] * X + p[1])) ** 2)

        fit = minimize(rss, x0=np.array([0.1, 0.1]))
        a_hat, b_hat = fit.x
        y_hat = a_hat * X + b_hat
        R2 = y_hat.var() / Y.var()

        ax.scatter(X, Y, alpha=0.65, color=HSLU, s=22,
                   edgecolor="white", linewidth=0.4, zorder=2)
        x_grid = np.linspace(X.min(), X.max(), 60)
        ax.plot(x_grid, a_hat * x_grid + b_hat,
                color="red", lw=2.5, zorder=3)
        ax.set_title(f"$R^2 = {R2:.2f}$", color=HSLU)
        ax.set_xlabel("$X$")
        ax.set_ylabel("$Y$")
        ax.grid(alpha=0.3)

    fig.suptitle("$R^2$-Galerie – wachsendes Rauschen, sinkendes $R^2$",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    save(fig, "r2_galerie.png")


# ---------------------------------------------------------------------------
# 5. Permutationstest – Histogramm + beobachtetes a
# ---------------------------------------------------------------------------
def fig_permutationstest():
    n = 200
    X = rng.uniform(0, 15, n)
    Y = 0.7 * X + 3 + rng.normal(0, 1.5, n)

    def rss(p, X=X, Y=Y):
        return np.sum((Y - (p[0] * X + p[1])) ** 2)

    fit = minimize(rss, x0=np.array([0.1, 0.1]))
    a_obs = fit.x[0]

    n_perm = 1000
    a_perm = np.zeros(n_perm)
    for k in range(n_perm):
        Yp = rng.permutation(Y)

        def rssp(p, X=X, Yp=Yp):
            return np.sum((Yp - (p[0] * X + p[1])) ** 2)

        fp = minimize(rssp, x0=np.array([0.0, 0.0]))
        a_perm[k] = fp.x[0]

    p_value = np.mean(np.abs(a_perm) >= np.abs(a_obs))

    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.hist(a_perm, bins=40, color=HSLU, alpha=0.85,
            edgecolor="white", linewidth=0.6, density=True,
            label=f"Permutationsverteilung von $\\hat a$\n"
                  f"(unter $H_0: a = 0$)")
    ax.axvline(a_obs, color="blue", lw=2.5, linestyle="dashed",
               label=f"beobachtet: $\\hat a = {a_obs:.3f}$")
    ax.axvline(-a_obs, color="blue", lw=1.0, linestyle="dotted",
               alpha=0.5, label=f"Spiegelung $-\\hat a$")
    ax.set_xlabel("Geschätzter Parameter $\\hat a$")
    ax.set_ylabel("Dichte")
    ax.set_title(f"Permutationstest: $p$-Wert $= {100 * p_value:.1f}\\,\\%$"
                 f"   $\\Rightarrow$  $H_0$ verwerfen",
                 color=HSLU)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(alpha=0.3)

    fig.tight_layout()
    save(fig, "permutationstest.png")


# ---------------------------------------------------------------------------
# 6. Bootstrap-Konfidenzintervalle für a und b
# ---------------------------------------------------------------------------
def fig_bootstrap_konfidenz():
    n = 200
    X = rng.uniform(0, 15, n)
    Y = 0.7 * X + 3 + rng.normal(0, 1.5, n)
    df = pd.DataFrame({"X": X, "Y": Y})

    def rss_full(p, Xs, Ys):
        return np.sum((Ys - (p[0] * Xs + p[1])) ** 2)

    fit_full = minimize(lambda p: rss_full(p, X, Y), x0=np.zeros(2))
    a_obs, b_obs = fit_full.x

    n_boot = 1000
    a_boot = np.zeros(n_boot)
    b_boot = np.zeros(n_boot)
    for k in range(n_boot):
        idx = rng.integers(0, n, n)
        Xs, Ys = X[idx], Y[idx]
        f = minimize(lambda p, Xs=Xs, Ys=Ys: rss_full(p, Xs, Ys),
                     x0=np.zeros(2))
        a_boot[k], b_boot[k] = f.x

    a_ci = np.quantile(a_boot, [0.025, 0.975])
    b_ci = np.quantile(b_boot, [0.025, 0.975])

    fig, axes = plt.subplots(1, 2, figsize=(15, 5.5))

    # Helper für Schraffur unter der Verteilung
    def draw_dist(ax, samples, ci, label_par, observed):
        counts, bins, _ = ax.hist(samples, bins=40, color=HSLU,
                                   alpha=0.85, edgecolor="white",
                                   linewidth=0.6, density=True)
        # Tail-Schraffuren
        for left, right in [(samples.min(), ci[0]),
                            (ci[1], samples.max())]:
            mask = (bins[:-1] >= left) & (bins[:-1] <= right)
            for b_lo, c in zip(bins[:-1][mask], counts[mask]):
                ax.bar(b_lo, c, width=bins[1] - bins[0],
                       align="edge", color="white",
                       edgecolor=HSLU, hatch="///", alpha=0.95)
        ax.axvline(observed, color="black", lw=2, linestyle="dashed",
                   label=f"beobachtet: {observed:.3f}")
        ax.axvline(0, color="grey", lw=1, linestyle="dotted")
        ax.set_xlabel(f"Geschätzter Parameter ${label_par}$")
        ax.set_ylabel("Dichte")
        ax.legend(loc="upper right", fontsize=10)
        ax.grid(alpha=0.3)

        # CI-Balken unten (ausserhalb des Plot-Bereichs)
        ymax = ax.get_ylim()[1]
        bar_y = -0.18 * ymax
        bar_h = 0.05 * ymax
        ax.add_patch(plt.Rectangle((ci[0], bar_y),
                                    ci[1] - ci[0], bar_h,
                                    facecolor=HSLU, alpha=0.85,
                                    clip_on=False))
        ax.text((ci[0] + ci[1]) / 2, bar_y - 0.02 * ymax,
                f"95%-CI: [{ci[0]:.3f}, {ci[1]:.3f}]",
                ha="center", va="top", fontsize=10,
                color=HSLU, fontweight="bold",
                clip_on=False)
        ax.set_ylim(-0.28 * ymax, ymax)

    draw_dist(axes[0], a_boot, a_ci, "\\hat a", a_obs)
    axes[0].set_title("Bootstrap-Verteilung des Gewichts $\\hat a$\n"
                      "(Steigung)", color=HSLU)

    draw_dist(axes[1], b_boot, b_ci, "\\hat b", b_obs)
    axes[1].set_title("Bootstrap-Verteilung des Achsenabschnitts $\\hat b$",
                      color=HSLU)

    fig.suptitle("95%-Konfidenzintervalle aus 1000 Bootstrap-Resamples",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    save(fig, "bootstrap_konfidenz.png")


# ---------------------------------------------------------------------------
# 7. Konfidenz- vs. Vorhersageintervall
# ---------------------------------------------------------------------------
def fig_konfidenz_und_vorhersage():
    n = 60
    X = rng.uniform(0, 15, n)
    Y = 0.7 * X + 3 + rng.normal(0, 1.5, n)

    def rss_full(p, Xs, Ys):
        return np.sum((Ys - (p[0] * Xs + p[1])) ** 2)

    fit_full = minimize(lambda p: rss_full(p, X, Y), x0=np.zeros(2))
    a_obs, b_obs = fit_full.x
    residuals_full = Y - (a_obs * X + b_obs)

    # Bootstrap: für jedes x_grid berechnen wir CI (Mittelwert) und PI (Einzelwert)
    x_grid = np.linspace(X.min() - 1.5, X.max() + 1.5, 50)
    n_boot = 800

    mean_pred = np.zeros((n_boot, len(x_grid)))
    new_pred = np.zeros((n_boot, len(x_grid)))

    for k in range(n_boot):
        idx = rng.integers(0, n, n)
        Xs, Ys = X[idx], Y[idx]
        f = minimize(lambda p, Xs=Xs, Ys=Ys: rss_full(p, Xs, Ys),
                     x0=np.zeros(2))
        a_b, b_b = f.x
        y_hat_grid = a_b * x_grid + b_b
        mean_pred[k] = y_hat_grid
        # Vorhersageintervall: + zufälliges Residuum
        resid_sample = Ys - (a_b * Xs + b_b)
        eps = rng.choice(resid_sample, size=len(x_grid))
        new_pred[k] = y_hat_grid + eps

    ci_low = np.quantile(mean_pred, 0.025, axis=0)
    ci_up = np.quantile(mean_pred, 0.975, axis=0)
    pi_low = np.quantile(new_pred, 0.025, axis=0)
    pi_up = np.quantile(new_pred, 0.975, axis=0)

    fig, ax = plt.subplots(figsize=(11, 6.5))

    ax.fill_between(x_grid, pi_low, pi_up, color=HSLU, alpha=0.20,
                    label="95%-Vorhersageintervall (einzelner Wert)")
    ax.fill_between(x_grid, ci_low, ci_up, color="black", alpha=0.30,
                    label="95%-Konfidenzintervall (Mittelwert)")
    ax.plot(x_grid, a_obs * x_grid + b_obs, color="red", lw=2.8,
            label=f"Regressionsgerade $\\hat y = {a_obs:.2f}x + {b_obs:.2f}$",
            zorder=4)
    ax.scatter(X, Y, color=HSLU, s=30, alpha=0.8,
               edgecolor="white", linewidth=0.6, zorder=3)
    ax.set_xlabel("Prädiktor $X$")
    ax.set_ylabel("Zielgrösse $Y$")
    ax.set_title("Konfidenzintervall (Mittelwert) vs. Vorhersageintervall "
                 "(einzelner Wert)", color=HSLU)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(alpha=0.3)

    fig.tight_layout()
    save(fig, "konfidenz_und_vorhersage.png")


# ---------------------------------------------------------------------------
# 8. Wein × Mortalität: linear vs. exponentiell
# ---------------------------------------------------------------------------
def fig_wein_linear_vs_nichtlinear():
    wein_x = np.array([2.8, 3.2, 3.2, 3.4, 4.3, 4.9, 5.1, 5.2, 5.9, 5.9,
                       6.6, 8.3, 12.6, 15.1, 25.1, 33.1, 75.9, 75.9])
    wein_y = np.array([6.2, 9.0, 7.1, 6.8, 10.2, 7.8, 9.3, 5.9, 8.9, 5.5,
                       7.1, 9.1, 5.1, 4.7, 4.7, 3.1, 3.2, 2.1])
    n = len(wein_x)

    # Linear fit
    def rss_lin(p):
        return np.sum((wein_y - (p[0] * wein_x + p[1])) ** 2)

    fit_lin = minimize(rss_lin, x0=np.zeros(2))
    a_l, b_l = fit_lin.x
    rse_lin = np.sqrt(fit_lin.fun / (n - 2))
    y_hat_lin = a_l * wein_x + b_l
    r2_lin = y_hat_lin.var() / wein_y.var()

    # Exponential fit
    def model_exp(x, a, b, c):
        return a * np.exp(b * x) + c

    def rss_exp(p):
        return np.sum((wein_y - model_exp(wein_x, p[0], p[1], p[2])) ** 2)

    fit_exp = minimize(rss_exp, x0=np.zeros(3))
    a_e, b_e, c_e = fit_exp.x
    rse_exp = np.sqrt(fit_exp.fun / (n - 2))  # wie in der Vorlesung gerechnet
    y_hat_exp = model_exp(wein_x, a_e, b_e, c_e)
    r2_exp = y_hat_exp.var() / wein_y.var()

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    x_grid = np.linspace(0, 80, 200)

    # Linear
    ax1 = axes[0]
    ax1.vlines(wein_x, y_hat_lin, wein_y,
               linestyles="dashed", lw=0.6, color="red", alpha=0.7)
    ax1.scatter(wein_x, wein_y, color=HSLU, s=55,
                edgecolor="white", linewidth=0.6, zorder=3)
    ax1.plot(x_grid, a_l * x_grid + b_l, color="red", lw=2.5)
    ax1.set_title(f"Lineares Modell\n"
                  f"$R^2 = {r2_lin:.3f}$,  $\\mathsf{{RSE}} = {rse_lin:.3f}$",
                  color=HSLU)
    ax1.set_xlabel("Weinkonsum (Liter pro Kopf/Jahr)")
    ax1.set_ylabel("Mortalität")
    ax1.grid(alpha=0.3)

    # Exponentiell
    ax2 = axes[1]
    ax2.vlines(wein_x, y_hat_exp, wein_y,
               linestyles="dashed", lw=0.6, color="red", alpha=0.7)
    ax2.scatter(wein_x, wein_y, color=HSLU, s=55,
                edgecolor="white", linewidth=0.6, zorder=3)
    ax2.plot(x_grid, model_exp(x_grid, a_e, b_e, c_e),
             color="red", lw=2.5)
    ax2.set_title(f"Exponentielles Modell\n"
                  f"$R^2 = {r2_exp:.3f}$,  $\\mathsf{{RSE}} = {rse_exp:.3f}$",
                  color=HSLU)
    ax2.set_xlabel("Weinkonsum (Liter pro Kopf/Jahr)")
    ax2.set_ylabel("Mortalität")
    ax2.grid(alpha=0.3)

    fig.suptitle("Wein × Mortalität – Modellwahl beeinflusst Anpassungsgüte",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    save(fig, "wein_linear_vs_nichtlinear.png")


# ---------------------------------------------------------------------------
# Alle Grafiken erzeugen
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Erzeuge SW11-Grafiken...")
    fig_regression_grundidee()
    fig_rss_minimierung()
    fig_mqd_modell_vs_daten()
    fig_r2_galerie()
    fig_permutationstest()
    fig_bootstrap_konfidenz()
    fig_konfidenz_und_vorhersage()
    fig_wein_linear_vs_nichtlinear()
    print("Fertig.")
