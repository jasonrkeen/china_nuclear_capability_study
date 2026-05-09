from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

BASE_DIR = Path(__file__).resolve().parents[1]
CHARTS_DIR = BASE_DIR / "charts"
CHARTS_DIR.mkdir(exist_ok=True)


def save_military_spending_chart(spending_df):
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        spending_df["year"],
        spending_df["official_defense_budget_usd_billion"],
        marker="o",
        label="Official defense budget",
    )

    ax.plot(
        spending_df["year"],
        spending_df["estimated_actual_military_spending_usd_billion"],
        marker="o",
        label="Estimated actual military spending",
    )

    ax.set_title("China Defense Spending: Official Budget vs. Estimated Actual Spending")
    ax.set_xlabel("Year")
    ax.set_ylabel("USD billions")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.text(
        0.5,
        0.01,
        "Note: Official defense budgets may not capture total military-related spending; estimated actual spending uses outside public estimates.",
        ha="center",
        fontsize=8,
    )

    fig.tight_layout(rect=[0, 0.04, 1, 1])
    out = CHARTS_DIR / "china_military_spending_comparison.png"
    fig.savefig(out, dpi=200)
    plt.close(fig)

    return out


def save_nuclear_spending_chart(spending_df):
    plot_df = spending_df.dropna(
        subset=["estimated_nuclear_weapons_spending_usd_billion"]
    )

    fig, ax = plt.subplots(figsize=(9, 5))

    bars = ax.bar(
        plot_df["year"].astype(str),
        plot_df["estimated_nuclear_weapons_spending_usd_billion"],
    )

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"${height:.1f}B",
            ha="center",
            va="bottom",
        )

    ax.set_title("Estimated China Nuclear Weapons Spending")
    ax.set_xlabel("Year")
    ax.set_ylabel("USD billions")
    ax.grid(True, axis="y", alpha=0.3)

    fig.text(
        0.5,
        0.01,
        "Note: China does not publish a separate nuclear weapons budget; figures are public estimates.",
        ha="center",
        fontsize=8,
    )

    fig.tight_layout(rect=[0, 0.04, 1, 1])
    out = CHARTS_DIR / "china_estimated_nuclear_spending.png"
    fig.savefig(out, dpi=200)
    plt.close(fig)

    return out


def save_nuclear_share_chart(spending_df):
    plot_df = spending_df.dropna(
        subset=["nuclear_share_of_estimated_actual_military_pct"]
    )

    fig, ax = plt.subplots(figsize=(9, 5))

    bars = ax.bar(
        plot_df["year"].astype(str),
        plot_df["nuclear_share_of_estimated_actual_military_pct"],
    )

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.2f}%",
            ha="center",
            va="bottom",
        )

    ax.set_title("Estimated Nuclear Weapons Spending as Share of Estimated Military Spending")
    ax.set_xlabel("Year")
    ax.set_ylabel("Percent")
    ax.grid(True, axis="y", alpha=0.3)

    fig.text(
        0.5,
        0.01,
        "Note: Share uses estimated nuclear weapons spending divided by estimated actual military spending.",
        ha="center",
        fontsize=8,
    )

    fig.tight_layout(rect=[0, 0.04, 1, 1])
    out = CHARTS_DIR / "china_nuclear_share_of_military_spending.png"
    fig.savefig(out, dpi=200)
    plt.close(fig)

    return out


def save_spending_per_warhead_chart(spending_df):
    column = "estimated_nuclear_spending_per_warhead_inventory_usd_million"

    plot_df = spending_df.dropna(subset=[column])

    fig, ax = plt.subplots(figsize=(9, 5))

    bars = ax.bar(
        plot_df["year"].astype(str),
        plot_df[column],
    )

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"${height:.1f}M",
            ha="center",
            va="bottom",
        )

    ax.set_title("Estimated Nuclear Weapons Spending per Estimated Warhead Inventory")
    ax.set_xlabel("Year")
    ax.set_ylabel("USD millions per estimated warhead inventory")
    ax.grid(True, axis="y", alpha=0.3)

    fig.text(
        0.5,
        0.01,
        "Note: This is not the cost of one warhead; it divides total estimated nuclear weapons spending by estimated inventory.",
        ha="center",
        fontsize=8,
    )

    fig.tight_layout(rect=[0, 0.04, 1, 1])
    out = CHARTS_DIR / "china_nuclear_spending_per_warhead.png"
    fig.savefig(out, dpi=200)
    plt.close(fig)

    return out


def save_warheads_vs_nuclear_spending_chart(spending_df):
    """
    Compare estimated Chinese nuclear warhead inventory with estimated
    nuclear weapons spending.

    Note: This is not a causal model. It is a visual comparison of two
    public estimate series.
    """
    plot_df = spending_df.dropna(
        subset=[
            "china_estimated_warheads",
            "estimated_nuclear_weapons_spending_usd_billion",
        ]
    )

    fig, ax1 = plt.subplots(figsize=(9, 5))

    ax1.plot(
        plot_df["year"],
        plot_df["china_estimated_warheads"],
        marker="o",
        linewidth=2,
        label="Estimated warheads",
    )

    for _, row in plot_df.iterrows():
        ax1.text(
            row["year"],
            row["china_estimated_warheads"],
            f'{int(row["china_estimated_warheads"])}',
            ha="center",
            va="bottom",
            fontsize=8,
        )

    ax1.set_xlabel("Year")
    ax1.set_ylabel("Estimated warheads")
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()

    bars = ax2.bar(
        plot_df["year"],
        plot_df["estimated_nuclear_weapons_spending_usd_billion"],
        alpha=0.25,
        width=0.35,
        label="Estimated nuclear spending",
    )

    for bar in bars:
        height = bar.get_height()
        ax2.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"${height:.1f}B",
            ha="center",
            va="bottom",
            fontsize=8,
        )

    ax2.set_ylabel("Estimated nuclear weapons spending, USD billions")

    ax1.set_title("China Warhead Inventory vs. Estimated Nuclear Weapons Spending")

    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(
        lines_1 + lines_2,
        labels_1 + labels_2,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.12),
        ncol=2,
    )

    fig.text(
        0.5,
        0.01,
        "Note: China does not publish a separate nuclear weapons budget; spending figures are public estimates.",
        ha="center",
        fontsize=8,
    )

    fig.tight_layout(rect=[0, 0.08, 1, 1])
    out = CHARTS_DIR / "china_warheads_vs_nuclear_spending.png"
    fig.savefig(out, dpi=200)
    plt.close(fig)

    return out