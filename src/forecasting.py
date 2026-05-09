import pandas as pd


def build_china_forecast(
    start_year: int = 2025,
    start_warheads: int = 600,
    end_year: int = 2035,
) -> pd.DataFrame:
    """
    Build transparent illustrative Chinese nuclear stockpile scenarios.

    These scenarios are not intelligence predictions. They are simple,
    assumption-based projections designed to show how different growth
    paths could affect China's estimated stockpile through 2035.

    Scenario logic:
    - Low: reaches roughly 850 warheads by 2030 and 1,100 by 2035
    - Base: reaches roughly 1,000 warheads by 2030 and 1,250 by 2035,
      broadly aligning with public DoD assessments that China could exceed
      1,000 warheads by 2030
    - High: reaches roughly 1,200 warheads by 2030 and 1,500 by 2035
    """
    if start_year > end_year:
        raise ValueError("start_year must be less than or equal to end_year.")

    if start_warheads <= 0:
        raise ValueError("start_warheads must be greater than zero.")

    years = list(range(start_year, end_year + 1))

    anchor_points = {
        "low": {2025: start_warheads, 2030: 850, 2035: 1100},
        "base": {2025: start_warheads, 2030: 1000, 2035: 1250},
        "high": {2025: start_warheads, 2030: 1200, 2035: 1500},
    }

    rows = []

    for scenario, anchors in anchor_points.items():
        for year in years:
            if year <= 2030:
                value = anchors[2025] + (
                    anchors[2030] - anchors[2025]
                ) * ((year - 2025) / 5)
            else:
                value = anchors[2030] + (
                    anchors[2035] - anchors[2030]
                ) * ((year - 2030) / 5)

            rows.append(
                {
                    "year": year,
                    "scenario": scenario,
                    "projected_warheads": round(value),
                }
            )

    return pd.DataFrame(rows)