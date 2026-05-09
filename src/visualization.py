from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

BASE_DIR = Path(__file__).resolve().parents[1]
CHARTS_DIR = BASE_DIR / "charts"
CHARTS_DIR.mkdir(exist_ok=True)


def save_stockpile_growth_chart(stockpile_df):
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        stockpile_df["year"],
        stockpile_df["china_estimated_warheads"],
        marker="o",
    )

    for _, row in stockpile_df.iterrows():
        ax.text(
            row["year"],
            row["china_estimated_warheads"],
            f'{int(row["china_estimated_warheads"])}',
            ha="center",
            va="bottom",
            fontsize=8,
        )

    ax.set_title("China Estimated Nuclear Warhead Stockpile, 2015–2025")
    ax.set_xlabel("Year")
    ax.set_ylabel("Estimated warheads")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.grid(True, alpha=0.3)

    fig.text(
        0.5,
        0.01,
        "Note: Warhead totals are public estimates and should be interpreted as approximate.",
        ha="center",
        fontsize=8,
    )

    fig.tight_layout(rect=[0, 0.04, 1, 1])
    out = CHARTS_DIR / "china_stockpile_growth.png"
    fig.savefig(out, dpi=200)
    plt.close(fig)

    return out


def save_global_comparison_chart(global_df):
    plot_df = global_df.sort_values("estimated_warheads_2025", ascending=True)

    fig, ax = plt.subplots(figsize=(9, 5))

    bars = ax.barh(
        plot_df["country"],
        plot_df["estimated_warheads_2025"],
    )

    for bar in bars:
        width = bar.get_width()
        ax.text(
            width,
            bar.get_y() + bar.get_height() / 2,
            f"{int(width):,}",
            va="center",
            ha="left",
            fontsize=8,
        )

    ax.set_title("Estimated Nuclear Warheads by Country, 2025")
    ax.set_xlabel("Estimated warheads")
    ax.grid(True, axis="x", alpha=0.3)

    fig.text(
        0.5,
        0.01,
        "Note: Estimates are rounded and vary by source; some states maintain nuclear opacity.",
        ha="center",
        fontsize=8,
    )

    fig.tight_layout(rect=[0, 0.04, 1, 1])
    out = CHARTS_DIR / "global_warhead_comparison_2025.png"
    fig.savefig(out, dpi=200)
    plt.close(fig)

    return out


def save_forecast_chart(forecast_df):
    fig, ax = plt.subplots(figsize=(9, 5))

    for scenario, group in forecast_df.groupby("scenario"):
        ax.plot(
            group["year"],
            group["projected_warheads"],
            marker="o",
            label=scenario.title(),
        )

    ax.set_title("Illustrative China Nuclear Stockpile Scenarios, 2025–2035")
    ax.set_xlabel("Year")
    ax.set_ylabel("Projected warheads")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend(title="Scenario")
    ax.grid(True, alpha=0.3)

    fig.text(
        0.5,
        0.01,
        "Note: Scenarios are illustrative projections, not intelligence predictions; the base case broadly aligns with public DoD 2030 assessments.",
        ha="center",
        fontsize=8,
    )

    fig.tight_layout(rect=[0, 0.04, 1, 1])
    out = CHARTS_DIR / "china_forecast_scenarios_2025_2035.png"
    fig.savefig(out, dpi=200)
    plt.close(fig)

    return out