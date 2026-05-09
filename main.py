from src.data_loader import (
    load_stockpile_estimates,
    load_global_forces,
    load_military_spending,
    load_nuclear_spending,
)
from src.forecasting import build_china_forecast
from src.spending_analysis import build_spending_summary
from src.visualization import (
    save_stockpile_growth_chart,
    save_global_comparison_chart,
    save_forecast_chart,
)
from src.spending_visualization import (
    save_military_spending_chart,
    save_nuclear_spending_chart,
    save_nuclear_share_chart,
    save_spending_per_warhead_chart,
    save_warheads_vs_nuclear_spending_chart,
)
from src.report_generator import generate_report


def main():
    stockpile = load_stockpile_estimates()
    global_forces = load_global_forces()
    forecast = build_china_forecast()

    military_spending = load_military_spending()
    nuclear_spending = load_nuclear_spending()

    spending_summary = build_spending_summary(
        military_spending=military_spending,
        nuclear_spending=nuclear_spending,
        stockpile=stockpile,
    )

    save_stockpile_growth_chart(stockpile)
    save_global_comparison_chart(global_forces)
    save_forecast_chart(forecast)

    save_military_spending_chart(spending_summary)
    save_nuclear_spending_chart(spending_summary)
    save_nuclear_share_chart(spending_summary)
    save_spending_per_warhead_chart(spending_summary)
    save_warheads_vs_nuclear_spending_chart(spending_summary)

    report_path = generate_report()

    print("Study complete.")
    print(f"Report: {report_path}")
    print("Charts saved in the charts/ folder.")


if __name__ == "__main__":
    main()