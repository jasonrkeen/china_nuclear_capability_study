# China Nuclear Capability Study

## Overview

This project is a Python-based open-source study of China's current nuclear capability. It uses public estimates to analyze China's nuclear stockpile growth, compare China with other nuclear-armed states, summarize publicly reported delivery-system modernization, and create transparent low/base/high forecast scenarios through 2035.

The project also includes a finance-oriented extension that compares official Chinese defense budget figures, estimated actual military spending, and public estimates of nuclear weapons spending. Because China does not publish a dedicated nuclear weapons budget, the spending section is treated as a proxy-based analysis rather than exact accounting.

## Research Question

How has China's nuclear capability changed over the last decade, and what do current open-source estimates suggest about its future role in global nuclear deterrence?

## Expanded Finance Question

Is China's nuclear expansion visible in public spending estimates, and how does estimated nuclear weapons spending compare with stockpile growth?

## Project Highlights

- Tracks public estimates of China's nuclear warhead stockpile from 2015 to 2025
- Compares China with other nuclear-armed states using 2025 public estimates
- Summarizes publicly reported land-based, sea-based, and air-based delivery-system modernization
- Builds low, base, and high stockpile scenarios through 2035
- Adds a defense-finance section using official budgets, estimated actual military spending, and nuclear weapons spending estimates
- Generates charts and a final Markdown report with Python
- Includes a polished PDF report and a LinkedIn-ready presentation deck

## Project Structure

```text
china_nuclear_capability_study/
├── data/
│   ├── china_stockpile_estimates.csv
│   ├── global_nuclear_forces_2025_estimates.csv
│   ├── china_delivery_systems_public_summary.csv
│   ├── china_military_spending_estimates.csv
│   ├── china_nuclear_spending_estimates.csv
│   └── sources.csv
├── charts/
│   ├── china_stockpile_growth.png
│   ├── global_warhead_comparison_2025.png
│   ├── china_forecast_scenarios_2025_2035.png
│   ├── china_military_spending_comparison.png
│   ├── china_estimated_nuclear_spending.png
│   ├── china_nuclear_share_of_military_spending.png
│   └── china_nuclear_spending_per_warhead.png
├── presentation/
│   └── china_nuclear_capability_presentation.pdf
├── src/
│   ├── data_loader.py
│   ├── forecasting.py
│   ├── spending_analysis.py
│   ├── visualization.py
│   ├── spending_visualization.py
│   └── report_generator.py
├── main.py
├── requirements.txt
├── final_report.md
└── china_nuclear_capability_report_final.pdf
```

## How to Run

From the project folder, install the required packages:

```bash
pip install -r requirements.txt
```

Then run the full study:

```bash
python main.py
```

This will generate or update:

- `final_report.md`
- `charts/china_stockpile_growth.png`
- `charts/global_warhead_comparison_2025.png`
- `charts/china_forecast_scenarios_2025_2035.png`
- `charts/china_military_spending_comparison.png`
- `charts/china_estimated_nuclear_spending.png`
- `charts/china_nuclear_share_of_military_spending.png`
- `charts/china_nuclear_spending_per_warhead.png`

## Methodology

This project uses public estimates only. It does not use classified information and does not provide operational targeting, weapons design, or tactical employment guidance.

Main variables include:

- Estimated Chinese nuclear warheads by year
- Estimated 2025 global nuclear stockpiles by country
- Publicly reported Chinese nuclear delivery-system categories
- Low/base/high stockpile growth scenarios through 2035
- Official Chinese defense budget estimates
- Estimated actual Chinese military spending
- Estimated Chinese nuclear weapons spending
- Estimated nuclear weapons spending as a share of military spending
- Estimated nuclear weapons spending per estimated warhead inventory

## Forecasting Approach

The forecast model is intentionally simple and transparent. It creates low, base, and high illustrative stockpile scenarios from 2025 to 2035.

The scenarios are not intelligence predictions. They are assumption-based projections designed to show how different growth paths could affect China's estimated arsenal over time. The base case broadly aligns with public U.S. Department of Defense assessments that China could exceed 1,000 warheads by 2030.

## Spending Analysis

The spending analysis compares three related but distinct concepts:

1. **Official defense budget** — the public budget figure reported by the Chinese government.
2. **Estimated actual military spending** — outside estimates that attempt to capture broader military-related spending.
3. **Estimated nuclear weapons spending** — outside estimates of nuclear weapons-related spending, which are more uncertain because China does not publish a dedicated nuclear weapons budget.

The spending-per-warhead figure should not be interpreted as the cost of one nuclear warhead. It divides total estimated nuclear weapons spending by estimated warhead inventory and is used only as a directional comparison metric.

## Source Base

Key public sources used to frame this study include:

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

## Important Caveats

All nuclear stockpile numbers are estimates. China does not publish a detailed nuclear inventory, so the exact number of warheads, deployment status, and operational readiness level remain uncertain.

China also does not publish a separate nuclear weapons budget, and official defense budget figures may not capture all military-related spending. For that reason, the spending analysis should be interpreted as a proxy-based estimate rather than a precise accounting of China's nuclear program.

The spending-per-warhead figure should not be interpreted as the cost of one nuclear warhead. Nuclear weapons spending may include warheads, delivery systems, submarines, missile infrastructure, command and control, personnel, research, production facilities, and modernization.

## Outputs

The project produces a Markdown report, a polished PDF report, charts, and a LinkedIn-ready presentation.

Primary outputs:

- `final_report.md`
- `china_nuclear_capability_report_final.pdf`
- `presentation/china_nuclear_capability_presentation.pdf`

## Final Report

The polished final report is available here:

[china_nuclear_capability_report_final.pdf](china_nuclear_capability_report_final.pdf)

## Presentation

A LinkedIn-ready presentation version of the project is available here:

[presentation/china_nuclear_capability_presentation.pdf](presentation/china_nuclear_capability_presentation.pdf)

## Tools Used

- Python
- pandas
- matplotlib
- Markdown
- Public-source research and defense-budget data

## Author

Jason Keen  
[LinkedIn](https://www.linkedin.com/in/jason-keen-1887b4218)
