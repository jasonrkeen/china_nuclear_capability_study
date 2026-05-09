from pathlib import Path

from src.data_loader import (
    load_stockpile_estimates,
    load_global_forces,
    load_delivery_systems,
    load_sources,
    load_military_spending,
    load_nuclear_spending,
)
from src.forecasting import build_china_forecast
from src.spending_analysis import build_spending_summary

BASE_DIR = Path(__file__).resolve().parents[1]
REPORT_PATH = BASE_DIR / "final_report.md"


def generate_report():
    stockpile = load_stockpile_estimates()
    global_forces = load_global_forces()
    delivery = load_delivery_systems()
    sources = load_sources()
    forecast = build_china_forecast()

    military_spending = load_military_spending()
    nuclear_spending = load_nuclear_spending()

    spending_summary = build_spending_summary(
        military_spending=military_spending,
        nuclear_spending=nuclear_spending,
        stockpile=stockpile,
    )

    latest = int(
        stockpile.loc[
            stockpile["year"].idxmax(),
            "china_estimated_warheads",
        ]
    )

    base_2030 = int(
        forecast[
            (forecast["scenario"] == "base") & (forecast["year"] == 2030)
        ]["projected_warheads"].iloc[0]
    )

    high_2035 = int(
        forecast[
            (forecast["scenario"] == "high") & (forecast["year"] == 2035)
        ]["projected_warheads"].iloc[0]
    )

    nuclear_2024 = spending_summary.loc[
        spending_summary["year"] == 2024,
        "estimated_nuclear_weapons_spending_usd_billion",
    ].iloc[0]

    nuclear_share_2024 = spending_summary.loc[
        spending_summary["year"] == 2024,
        "nuclear_share_of_estimated_actual_military_pct",
    ].iloc[0]

    spending_per_warhead_2024 = spending_summary.loc[
        spending_summary["year"] == 2024,
        "estimated_nuclear_spending_per_warhead_inventory_usd_million",
    ].iloc[0]

    report = f"""# Assessing China's Nuclear Capability: A Python-Based Open-Source Strategic Forces Study

## Executive Summary

This project analyzes China's current nuclear capability using open-source estimates from public research organizations, government reporting, and defense-budget data. The study focuses on stockpile growth, delivery-system modernization, global comparison, transparent forecast scenarios, proxy-based spending analysis, and budget-context interpretation.

The core finding is that China has moved from a historically smaller minimum-deterrent posture toward a larger and more diversified nuclear force. Public estimates place China's arsenal at about **{latest} nuclear warheads in 2025**, with U.S. Department of Defense reporting assessing that China remains on track to exceed **{base_2030} warheads by 2030**. This remains far below U.S. and Russian total arsenals, but it represents a major shift in the global nuclear balance.

The spending analysis adds a finance-oriented dimension. Because China does not publish a dedicated nuclear weapons budget, this project uses proxy indicators: official defense budgets, estimated actual military expenditure, and ICAN-style nuclear weapons spending estimates. Based on the current dataset, China spent an estimated **${nuclear_2024:.1f} billion on nuclear weapons in 2024**, equal to roughly **{nuclear_share_2024:.2f}%** of estimated actual military spending and about **${spending_per_warhead_2024:.1f} million per estimated warhead inventory**.

## Research Question

How has China's nuclear capability changed over the last decade, and what do current open-source estimates suggest about its future role in global nuclear deterrence?

## Expanded Finance Question

Is China's nuclear expansion visible in public spending estimates, and how does estimated nuclear weapons spending compare with stockpile growth?

## Methodology

This study uses:
- Open-source estimates of Chinese nuclear warheads from 2015 to 2025
- Public global nuclear force estimates for comparison
- A qualitative delivery-system summary covering land, sea, and air components
- Low, base, and high scenario projections from 2025 to 2035
- Proxy-based spending indicators, including official defense budgets, estimated actual military spending, and estimated nuclear weapons spending
- Budget-context sources that help explain why official Chinese fiscal and defense figures require careful interpretation

Official Chinese budget documents provide a useful national defense budget baseline, but they do not identify a separate nuclear weapons budget. Therefore, this study treats official defense spending as a broad proxy rather than a direct nuclear-program measure.

China's broader fiscal context is also relevant because public budget figures are distributed across multiple budget layers. This makes headline budget figures useful but incomplete indicators of the state's fiscal stance.

The analysis does **not** use classified information and does **not** provide operational targeting, weapons design, or tactical employment guidance.

## Key Findings

### 1. China's estimated stockpile has grown quickly

China's estimated arsenal increased from a much smaller force in the mid-2010s to roughly **{latest} warheads in 2025**. SIPRI and FAS/Bulletin estimates place China at about 600 warheads, while U.S. Department of Defense reporting assesses continued growth toward more than 1,000 warheads by 2030.

### 2. China is developing a more complete nuclear triad

China's land-based forces remain central to its nuclear posture, but its sea-based and air-based legs are becoming more relevant. Public reporting describes modernization involving DF-series missiles, Type 094 ballistic missile submarines equipped or refitted with JL-3 submarine-launched ballistic missiles, and some bomber-based nuclear roles.

### 3. China remains below the United States and Russia, but it is becoming the third major nuclear power

The global comparison shows that the United States and Russia still hold far larger arsenals. However, China's rapid growth places it well above the other nuclear-armed states in overall estimated stockpile size.

### 4. Spending analysis strengthens the project

The spending section shows how defense finance can be used as a proxy for nuclear modernization. China's nuclear weapons spending cannot be tracked perfectly, but estimates can be compared against official defense budgets, estimated actual military expenditure, and stockpile growth.

### 5. Official budget figures require careful interpretation

China's official defense budget is useful because it provides a public baseline, but it does not necessarily capture all defense-related spending. For this reason, the project compares official defense figures with outside estimates of actual military expenditure and treats nuclear spending estimates as directional indicators rather than exact accounting data.

### 6. Forecasts depend heavily on assumptions

The base scenario reaches roughly **{base_2030} warheads by 2030**, consistent with the U.S. Department of Defense assessment that China remains on track to exceed 1,000 warheads by 2030. The high scenario reaches about **{high_2035} by 2035**, while the low scenario assumes slower production and deployment.

## Strategic and Fiscal Context

China's nuclear modernization should be viewed within a broader strategic and fiscal context. The project uses official Chinese budget reporting, U.S. Department of Defense assessments, SIPRI military expenditure estimates, and outside budget-analysis sources to distinguish between three different concepts:

1. **Official defense budget** — the public budget figure reported by the Chinese government.
2. **Estimated actual military spending** — outside estimates that attempt to capture broader military-related spending.
3. **Estimated nuclear weapons spending** — outside estimates of nuclear weapons-related spending, which are more uncertain because China does not publish a dedicated nuclear weapons budget.

This distinction is important because a nuclear-weapons program can involve warheads, delivery systems, submarines, missiles, command and control, infrastructure, research, production facilities, and personnel. A single spending number cannot fully capture these categories.

The project also separates nuclear force-structure analysis from nuclear and missile proliferation analysis. CRS reporting shows that U.S. concerns about China also include export-control enforcement, China-based entities, and proliferation-sensitive transfers involving Iran, North Korea, and Pakistan. Those issues are important for broader strategic context, but they are not the primary focus of this stockpile and spending model.

## Data Tables

### China stockpile estimates

{stockpile.to_markdown(index=False)}

### Global nuclear force comparison

{global_forces.to_markdown(index=False)}

### Public delivery-system summary

{delivery.to_markdown(index=False)}

### China defense and nuclear spending summary

{spending_summary.fillna("").to_markdown(index=False)}

## Generated Charts

The project generates the following charts in the `charts/` folder:

- `china_stockpile_growth.png` — China estimated nuclear warhead stockpile, 2015–2025
- `global_warhead_comparison_2025.png` — Estimated nuclear warheads by country, 2025
- `china_forecast_scenarios_2025_2035.png` — Low, base, and high Chinese stockpile scenarios through 2035
- `china_military_spending_comparison.png` — Official Chinese defense budget vs. estimated actual military spending
- `china_estimated_nuclear_spending.png` — Estimated Chinese nuclear weapons spending
- `china_nuclear_share_of_military_spending.png` — Estimated nuclear weapons spending as a share of estimated military spending
- `china_nuclear_spending_per_warhead.png` — Estimated nuclear weapons spending per estimated warhead inventory
- `china_warheads_vs_nuclear_spending.png` — Estimated warhead inventory compared with estimated nuclear weapons spending

## Source Confidence Framework

This study uses a simple source-confidence system to make the analysis more transparent. Sources are rated based on institutional credibility, transparency of methodology, and usefulness for public nuclear-force analysis.

{sources.fillna("").to_markdown(index=False)}

## Limitations

All nuclear stockpile numbers are estimates. China does not publish a detailed nuclear inventory, and outside analysts rely on a mix of official statements, satellite imagery, budget signals, public military reporting, and expert judgment. This means the exact number of warheads, deployed systems, and operational readiness levels remain uncertain.

The spending section has an additional limitation: China does not publish a separate nuclear weapons budget, and even its official defense budget does not fully capture total military-related spending. As a result, the study uses proxy variables and outside estimates. These should be interpreted as directional indicators rather than exact accounting data.

The spending-per-warhead figure should not be interpreted as the cost of one nuclear warhead. Nuclear weapons spending can include warheads, delivery systems, submarines, missile infrastructure, command and control, personnel, research, production facilities, and modernization.

The combined warheads-versus-spending chart should be interpreted cautiously because currently available China-specific nuclear spending estimates cover only a limited number of years. It is useful as a visual comparison, not as a causal model.

## Sources

- SIPRI Yearbook 2025, World Nuclear Forces
- SIPRI military expenditure reporting
- Federation of American Scientists / Bulletin of the Atomic Scientists, Chinese Nuclear Weapons 2025
- CSIS ChinaPower, How is China Modernizing its Nuclear Forces?
- CSIS ChinaPower, What Does China Really Spend on its Military?
- CSIS ChinaPower, Making Sense of China's Government Budget
- Ministry of Finance of the People's Republic of China, Report on the Execution of the Central and Local Budgets for 2025 and on the Draft Central and Local Budgets for 2026
- U.S. Department of Defense, Military and Security Developments Involving the People's Republic of China 2025
- ICAN nuclear weapons spending estimates reported by Reuters and The Guardian
- BBVA Research, Decoding China's Multi-Layered Fiscal Budget
- Congressional Research Service, China: Nuclear and Missile Proliferation
"""

    REPORT_PATH.write_text(report, encoding="utf-8")
    return REPORT_PATH


if __name__ == "__main__":
    path = generate_report()
    print(f"Report saved to: {path}")