"""Grafiken für ZUSAMMENFASSUNG_SW13.md erzeugen."""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

HSLU = (160 / 255, 0 / 255, 86 / 255)
HSLU_LIGHT = (160 / 255, 0 / 255, 86 / 255, 0.3)
BLUE = (0 / 255, 90 / 255, 156 / 255)
ORANGE = (230 / 255, 130 / 255, 0 / 255)
GREEN = (40 / 255, 140 / 255, 50 / 255)
GRAY = (130 / 255, 130 / 255, 130 / 255)

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
# Hilfsfunktion: synthetische Zeitreihe (CO2-artig)
# ---------------------------------------------------------------------------
def make_series(n_years=15, freq=12, trend_slope=2.0, trend_curv=0.05,
                season_amp=4.0, noise=0.8, start=350.0):
    """Erzeugt monatliche Zeitreihe mit Trend + Saison + Rauschen."""
    t = np.arange(n_years * freq) / freq
    trend = start + trend_slope * t + trend_curv * t ** 2
    season = season_amp * np.sin(2 * np.pi * t)
    noise_arr = rng.normal(0, noise, len(t))
    y = trend + season + noise_arr
    return t, y, trend, season


# ---------------------------------------------------------------------------
# 1. Was ist eine Zeitreihe? Komponenten = Trend + Saison + Rest
# ---------------------------------------------------------------------------
def fig_zeitreihen_komponenten():
    t, y, trend, season = make_series()
    rest = y - trend - season

    fig, axes = plt.subplots(4, 1, figsize=(15, 9), sharex=True)

    axes[0].plot(t, y, "-", color=HSLU, lw=1.6)
    axes[0].scatter(t, y, color=HSLU, s=14, alpha=0.6, edgecolor="white",
                    linewidth=0.4)
    axes[0].set_ylabel("Beobachtung $y_t$")
    axes[0].set_title("Originale Zeitreihe = Trend + Saison + Rest",
                      color=HSLU)
    axes[0].grid(alpha=0.3)

    axes[1].plot(t, trend, "-", color=BLUE, lw=2.2)
    axes[1].set_ylabel("glatte Komp. $g(t)$")
    axes[1].set_title("Trend (glatte Komponente)", color=BLUE)
    axes[1].grid(alpha=0.3)

    axes[2].plot(t, season, "-", color=ORANGE, lw=1.8)
    axes[2].set_ylabel("zykl. Komp. $s(t)$")
    axes[2].set_title("Saisonfigur (zyklische Komponente)", color=ORANGE)
    axes[2].grid(alpha=0.3)

    axes[3].plot(t, rest, "-", color=GRAY, lw=1, alpha=0.7)
    axes[3].axhline(0, color="black", lw=0.8)
    axes[3].set_ylabel("Restkomp. $r_t$")
    axes[3].set_xlabel("Zeit (Jahre)")
    axes[3].set_title("Restkomponente (zufälliges Rauschen um Null)",
                      color="black")
    axes[3].grid(alpha=0.3)

    plt.tight_layout()
    save(fig, "zeitreihen_komponenten.png")


# ---------------------------------------------------------------------------
# 2. Additives Modell: Schritt für Schritt
# ---------------------------------------------------------------------------
def fig_additives_modell_aufbau():
    t, y, trend, season = make_series()

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Panel 1: Daten + Trend (linear)
    coef = np.polyfit(t, y, 1)
    fit_trend = np.polyval(coef, t)
    axes[0].scatter(t, y, color=HSLU, s=18, alpha=0.55,
                    edgecolor="white", linewidth=0.4)
    axes[0].plot(t, fit_trend, "-", color=BLUE, lw=2.5,
                 label=f"Trendlinie\n$\\hat y_{{trend}}={coef[0]:.2f}\\,t+{coef[1]:.1f}$")
    axes[0].set_title("Schritt 1: Trend schätzen\n(kleinste Quadrate)",
                      color=HSLU)
    axes[0].set_xlabel("Zeit")
    axes[0].set_ylabel("$y_t$")
    axes[0].legend(loc="upper left", fontsize=9)
    axes[0].grid(alpha=0.3)

    # Panel 2: Residuen mit Monatsmitteln
    resid = y - fit_trend
    months = (np.round((t - np.floor(t)) * 12)).astype(int) % 12
    monthly = np.array([resid[months == m].mean() for m in range(12)])
    axes[1].scatter(t, resid, color=GRAY, s=18, alpha=0.55,
                    edgecolor="white", linewidth=0.4, label="Residuen $r_t$")
    season_curve = monthly[months]
    axes[1].plot(t, season_curve, "-", color=ORANGE, lw=2,
                 label="mittlere Residuen pro Monat")
    axes[1].axhline(0, color="black", lw=0.8)
    axes[1].set_title("Schritt 2: Residuen sortieren nach\nMonat → Saisonfigur",
                      color=HSLU)
    axes[1].set_xlabel("Zeit")
    axes[1].set_ylabel("Residuum $y_t - \\hat y_{trend}$")
    axes[1].legend(loc="upper left", fontsize=9)
    axes[1].grid(alpha=0.3)

    # Panel 3: Vollständiges Modell
    full_pred = fit_trend + season_curve
    axes[2].scatter(t, y, color=HSLU, s=18, alpha=0.55,
                    edgecolor="white", linewidth=0.4)
    axes[2].plot(t, full_pred, "-", color="red", lw=2,
                 label="$\\hat y(t)=g(t)+s(t)$")
    axes[2].plot(t, fit_trend, "--", color=BLUE, lw=1.5,
                 label="reiner Trend", alpha=0.7)
    axes[2].set_title("Schritt 3: Trend + Saison\nzusammensetzen",
                      color=HSLU)
    axes[2].set_xlabel("Zeit")
    axes[2].set_ylabel("$y$")
    axes[2].legend(loc="upper left", fontsize=9)
    axes[2].grid(alpha=0.3)

    plt.tight_layout()
    save(fig, "additives_modell_aufbau.png")


# ---------------------------------------------------------------------------
# 3. Saisonfigur als Balkendiagramm (mittlere Residuen pro Monat)
# ---------------------------------------------------------------------------
def fig_saisonfigur():
    t, y, trend, season = make_series()
    coef = np.polyfit(t, y, 1)
    fit_trend = np.polyval(coef, t)
    resid = y - fit_trend
    months = (np.round((t - np.floor(t)) * 12)).astype(int) % 12
    monthly = np.array([resid[months == m].mean() for m in range(12)])

    fig, ax = plt.subplots(figsize=(13, 5))
    month_names = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun",
                   "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"]
    colors = [BLUE if v < 0 else ORANGE for v in monthly]
    bars = ax.bar(month_names, monthly, color=colors,
                  edgecolor="white", linewidth=2)
    for b, v in zip(bars, monthly):
        ax.text(b.get_x() + b.get_width() / 2,
                v + (0.15 if v >= 0 else -0.35),
                f"{v:+.1f}", ha="center", fontsize=10, fontweight="bold")
    ax.axhline(0, color="black", lw=0.8)
    ax.set_ylabel("Mittleres Residuum (= Saisoneffekt)")
    ax.set_title("Saisonfigur: mittleres Residuum pro Monat\n"
                 "(positiv = über Trend, negativ = unter Trend)",
                 color=HSLU)
    ax.grid(alpha=0.3, axis="y")

    plt.tight_layout()
    save(fig, "saisonfigur.png")


# ---------------------------------------------------------------------------
# 4. Gleitender Durchschnitt – verschiedene Periodenlängen
# ---------------------------------------------------------------------------
def fig_gleitender_durchschnitt():
    t, y, trend, season = make_series(season_amp=4, noise=1.5)

    def centered_moving_average(y, L=12):
        n = len(y)
        out = np.full(n, np.nan)
        h = L // 2
        for i in range(h, n - h):
            window = y[i - h:i + h + 1].astype(float).copy()
            # zentrierter Mittelwert: Ränder halb gewichten
            window[0] *= 0.5
            window[-1] *= 0.5
            out[i] = window.sum() / L
        return out

    fig, ax = plt.subplots(figsize=(15, 6))
    ax.plot(t, y, "-", color=HSLU, lw=0.9, alpha=0.5, label="Originaldaten")
    ax.scatter(t, y, color=HSLU, s=10, alpha=0.4)

    for L, col, lw in zip([3, 12, 24], [BLUE, ORANGE, GREEN], [1.5, 2.5, 2.5]):
        sm = centered_moving_average(y, L)
        ax.plot(t, sm, "-", color=col, lw=lw, label=f"$L = {L}$")

    ax.set_xlabel("Zeit (Jahre)")
    ax.set_ylabel("$y$ bzw. $\\bar y(t)$")
    ax.set_title("Gleitender zentrierter Durchschnitt:\n"
                 "$L=12$ entfernt die jährliche Saison fast vollständig",
                 color=HSLU)
    ax.legend(loc="upper left")
    ax.grid(alpha=0.3)

    # Inset: Fenster-Skizze
    ax2 = ax.inset_axes([0.55, 0.05, 0.4, 0.32])
    L = 12
    idx = list(range(L + 1))
    weights = [1 / (2 * L)] + [1 / L] * (L - 1) + [1 / (2 * L)]
    ax2.bar(idx, weights, color=HSLU, edgecolor="white", linewidth=1)
    ax2.set_title(f"Gewichte ($L = {L}$)", fontsize=10, color=HSLU)
    ax2.set_xlabel("Position im Fenster", fontsize=9)
    ax2.set_ylabel("Gewicht", fontsize=9)
    ax2.set_xticks([0, L])
    ax2.set_xticklabels(["$t-L/2$", "$t+L/2$"], fontsize=8)
    ax2.tick_params(axis="y", labelsize=8)
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    save(fig, "gleitender_durchschnitt.png")


# ---------------------------------------------------------------------------
# 5. Exponentielle Glättung – verschiedene Alpha-Werte
# ---------------------------------------------------------------------------
def fig_exponentielle_glaettung():
    t, y, trend, season = make_series(season_amp=4, noise=1.5)

    def exp_smooth(y, alpha):
        s = np.zeros_like(y, dtype=float)
        s[0] = y[0]
        for i in range(1, len(y)):
            s[i] = alpha * y[i] + (1 - alpha) * s[i - 1]
        return s

    fig, axes = plt.subplots(1, 2, figsize=(15, 5.5))

    # Links: drei verschiedene alpha-Werte
    axes[0].plot(t, y, "-", color=HSLU, lw=0.8, alpha=0.45,
                 label="Originaldaten")
    axes[0].scatter(t, y, color=HSLU, s=10, alpha=0.4)
    for a, col in zip([0.05, 0.2, 0.6], [BLUE, ORANGE, GREEN]):
        sm = exp_smooth(y, a)
        axes[0].plot(t, sm, "-", color=col, lw=2.2, label=f"$\\alpha={a}$")
    axes[0].set_xlabel("Zeit")
    axes[0].set_ylabel("$y$ bzw. $\\bar y(t)$")
    axes[0].set_title("Exponentielle Glättung:\nkleines $\\alpha$ = stark geglättet,\n"
                      "grosses $\\alpha$ = folgt den Daten",
                      color=HSLU)
    axes[0].legend(loc="upper left")
    axes[0].grid(alpha=0.3)

    # Rechts: Gewichts-Decay
    n_steps = 25
    lag = np.arange(n_steps)
    for a, col in zip([0.05, 0.2, 0.6], [BLUE, ORANGE, GREEN]):
        w = a * (1 - a) ** lag
        axes[1].plot(lag, w, "o-", color=col, lw=2, markersize=6,
                     label=f"$\\alpha = {a}$")
    axes[1].set_xlabel("Wie viele Zeitschritte in der Vergangenheit")
    axes[1].set_ylabel("Gewicht für $y_{t-k}$")
    axes[1].set_title("Gewichts-Decay: $\\alpha(1-\\alpha)^k$\n"
                      "jüngere Beobachtungen zählen mehr",
                      color=HSLU)
    axes[1].legend()
    axes[1].grid(alpha=0.3)

    plt.tight_layout()
    save(fig, "exponentielle_glaettung.png")


# ---------------------------------------------------------------------------
# 6. Trendmodell-Vergleich: linear vs. Potenz
# ---------------------------------------------------------------------------
def fig_trendmodelle():
    t, y, _, _ = make_series(trend_slope=1.5, trend_curv=0.15,
                              season_amp=3, noise=0.6, n_years=20)

    # Linear
    coef_lin = np.polyfit(t, y, 1)
    pred_lin = np.polyval(coef_lin, t)
    # Potenz: y = a * t^r + b (numerisch via simplem grid + scipy)
    from scipy.optimize import minimize

    def model_potenz(time, a, r, b):
        return a * (time + 0.1) ** r + b

    def rss_p(p):
        return np.sum((y - model_potenz(t, *p)) ** 2)

    fit_p = minimize(rss_p, x0=[1, 1.5, y.min()], method="Powell")
    pred_p = model_potenz(t, *fit_p.x)

    r2_lin = np.var(pred_lin) / np.var(y)
    r2_p = np.var(pred_p) / np.var(y)

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    axes[0].scatter(t, y, color=HSLU, s=18, alpha=0.55,
                    edgecolor="white", linewidth=0.4, label="Daten")
    axes[0].plot(t, pred_lin, "-", color=BLUE, lw=2.5,
                 label=f"linear, $R^2={r2_lin:.3f}$")
    axes[0].set_title("Lineares Trendmodell\n$\\hat y = a\\,t + b$", color=HSLU)
    axes[0].set_xlabel("Zeit")
    axes[0].set_ylabel("$y$")
    axes[0].legend(loc="upper left")
    axes[0].grid(alpha=0.3)

    axes[1].scatter(t, y, color=HSLU, s=18, alpha=0.55,
                    edgecolor="white", linewidth=0.4, label="Daten")
    axes[1].plot(t, pred_p, "-", color=ORANGE, lw=2.5,
                 label=f"Potenz, $R^2={r2_p:.3f}$")
    axes[1].set_title("Potenz-Trendmodell\n$\\hat y = a\\,t^{r} + b$", color=HSLU)
    axes[1].set_xlabel("Zeit")
    axes[1].set_ylabel("$y$")
    axes[1].legend(loc="upper left")
    axes[1].grid(alpha=0.3)

    plt.tight_layout()
    save(fig, "trendmodelle.png")


# ---------------------------------------------------------------------------
# 7. Prognose mit Vorhersage-Verlängerung
# ---------------------------------------------------------------------------
def fig_prognose():
    t, y, _, _ = make_series(season_amp=4, noise=0.9)

    # Trend + Saison fitten
    coef = np.polyfit(t, y, 1)
    fit_trend = np.polyval(coef, t)
    resid = y - fit_trend
    months = (np.round((t - np.floor(t)) * 12)).astype(int) % 12
    monthly = np.array([resid[months == m].mean() for m in range(12)])

    # Prognose-Zeitachse
    t_future = np.linspace(t.max(), t.max() + 5, 60)
    months_future = (np.round((t_future - np.floor(t_future)) * 12)
                     ).astype(int) % 12
    pred_future = np.polyval(coef, t_future) + monthly[months_future]
    pred_in = fit_trend + monthly[months]

    fig, ax = plt.subplots(figsize=(15, 6))
    ax.scatter(t, y, color=HSLU, s=14, alpha=0.55,
               edgecolor="white", linewidth=0.4, label="Beobachtungen")
    ax.plot(t, pred_in, "-", color=BLUE, lw=1.8, alpha=0.85,
            label="Modell (Trend + Saison)")
    ax.plot(t_future, pred_future, "-", color="red", lw=2.2,
            label="Prognose")
    ax.axvline(t.max(), color="black", lw=1.5, ls="--", alpha=0.6)
    ax.text(t.max() + 0.1, ax.get_ylim()[1] - 1,
            "Heute →", fontsize=11, color="black")
    ax.set_xlabel("Zeit (Jahre)")
    ax.set_ylabel("$y$")
    ax.set_title("Prognose: Trend extrapolieren + Saisonfigur wiederholen",
                 color=HSLU)
    ax.legend(loc="upper left")
    ax.grid(alpha=0.3)

    plt.tight_layout()
    save(fig, "prognose.png")


# ---------------------------------------------------------------------------
# 8. Algorithmus-Schema: Zeitreihenanalyse Schritt für Schritt
# ---------------------------------------------------------------------------
def fig_algorithmus_schema():
    fig, ax = plt.subplots(figsize=(15, 5.5))
    ax.axis("off")

    steps = [
        ("1. Plot &\nSichtung",
         "• Trend?\n• Saison?\n• Brüche?\n• Ausreisser?"),
        ("2. Trendmodell\nschätzen",
         "$\\hat y_{trend} = a\\,t + b$\noder Potenz/log/exp\n→ kleinste\nQuadrate"),
        ("3. Residuen\nberechnen",
         "$r_t = y_t - \\hat y_{trend}$\nzeigt Saison\n+ Rauschen"),
        ("4. Saisonfigur\n(Monatsmittel)",
         "$\\bar r_{Jan},\\ldots,\\bar r_{Dez}$\n= zyklische\nKomponente $s(t)$"),
        ("5. Modell\nzusammensetzen",
         "$\\hat y(t) = $\n$\\hat y_{trend}(t) + s(t)$\n$R^2$ prüfen"),
        ("6. Prognose",
         "Extrapolation\nin die Zukunft;\nSaison repliziert"),
    ]

    n = len(steps)
    for i, (title, body) in enumerate(steps):
        cx = i * 2.6
        ax.add_patch(plt.Rectangle((cx, 0.3), 2.2, 3.4,
                                   facecolor=HSLU_LIGHT,
                                   edgecolor=HSLU, linewidth=2))
        ax.text(cx + 1.1, 3.3, title, ha="center", va="center",
                fontsize=11, color=HSLU, fontweight="bold")
        ax.text(cx + 1.1, 1.7, body, ha="center", va="center", fontsize=10)
        if i < n - 1:
            ax.annotate("", xy=(cx + 2.55, 2),
                        xytext=(cx + 2.25, 2),
                        arrowprops=dict(arrowstyle="->", color=HSLU, lw=2))

    ax.set_xlim(-0.5, n * 2.6)
    ax.set_ylim(0, 4.5)
    ax.set_title("Algorithmus der Zeitreihenanalyse (additives Modell)",
                 color=HSLU, fontsize=14)
    save(fig, "algorithmus_schema.png")


if __name__ == "__main__":
    print("Erzeuge Grafiken für SW13 …")
    fig_zeitreihen_komponenten()
    fig_additives_modell_aufbau()
    fig_saisonfigur()
    fig_gleitender_durchschnitt()
    fig_exponentielle_glaettung()
    fig_trendmodelle()
    fig_prognose()
    fig_algorithmus_schema()
    print("Fertig.")
