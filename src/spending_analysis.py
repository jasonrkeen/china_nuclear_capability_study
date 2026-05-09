import pandas as pd


REQUIRED_MILITARY_COLUMNS = {
    "year",
    "official_defense_budget_usd_billion",
    "estimated_actual_military_spending_usd_billion",
}

REQUIRED_NUCLEAR_COLUMNS = {
    "year",
    "estimated_nuclear_weapons_spending_usd_billion",
}

REQUIRED_STOCKPILE_COLUMNS = {
    "year",
    "china_estimated_warheads",
}


def _validate_columns(df: pd.DataFrame, required_columns: set, dataset_name: str) -> None:
    """
    Confirm that a dataset includes the columns required for the spending analysis.
    """
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"{dataset_name} is missing required columns: "
            f"{', '.join(sorted(missing_columns))}"
        )


def build_spending_summary(
    military_spending: pd.DataFrame,
    nuclear_spending: pd.DataFrame,
    stockpile: pd.DataFrame,
) -> pd.DataFrame:
    """
    Merge official defense spending, estimated actual military spending,
    estimated nuclear weapons spending, and warhead estimates.

    All nuclear spending values are estimates and should be interpreted
    as directional indicators, not exact accounting figures.

    The spending-per-warhead figure is not the cost of one warhead.
    It is estimated nuclear weapons spending divided by the estimated
    total warhead inventory for that year.
    """
    _validate_columns(
        military_spending,
        REQUIRED_MILITARY_COLUMNS,
        "china_military_spending_estimates.csv",
    )
    _validate_columns(
        nuclear_spending,
        REQUIRED_NUCLEAR_COLUMNS,
        "china_nuclear_spending_estimates.csv",
    )
    _validate_columns(
        stockpile,
        REQUIRED_STOCKPILE_COLUMNS,
        "china_stockpile_estimates.csv",
    )

    df = military_spending.merge(
        nuclear_spending,
        on="year",
        how="outer",
        suffixes=(
            "_military_spending",
            "_nuclear_spending",
        ),
    )

    df = df.merge(
        stockpile[["year", "china_estimated_warheads"]],
        on="year",
        how="left",
    )

    df = df.rename(
        columns={
            "source_note_military_spending": "military_spending_source_note",
            "source_note_nuclear_spending": "nuclear_spending_source_note",
        }
    )

    df["nuclear_share_of_official_defense_pct"] = (
        df["estimated_nuclear_weapons_spending_usd_billion"]
        / df["official_defense_budget_usd_billion"]
        * 100
    )

    df["nuclear_share_of_estimated_actual_military_pct"] = (
        df["estimated_nuclear_weapons_spending_usd_billion"]
        / df["estimated_actual_military_spending_usd_billion"]
        * 100
    )

    df["estimated_nuclear_spending_per_warhead_inventory_usd_million"] = (
        df["estimated_nuclear_weapons_spending_usd_billion"]
        * 1000
        / df["china_estimated_warheads"]
    )

    numeric_columns = [
        "official_defense_budget_usd_billion",
        "estimated_actual_military_spending_usd_billion",
        "estimated_nuclear_weapons_spending_usd_billion",
        "nuclear_share_of_official_defense_pct",
        "nuclear_share_of_estimated_actual_military_pct",
        "estimated_nuclear_spending_per_warhead_inventory_usd_million",
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = df[column].round(2)

    column_order = [
        "year",
        "official_defense_budget_usd_billion",
        "estimated_actual_military_spending_usd_billion",
        "estimated_nuclear_weapons_spending_usd_billion",
        "china_estimated_warheads",
        "nuclear_share_of_official_defense_pct",
        "nuclear_share_of_estimated_actual_military_pct",
        "estimated_nuclear_spending_per_warhead_inventory_usd_million",
        "military_spending_source_note",
        "nuclear_spending_source_note",
    ]

    available_columns = [column for column in column_order if column in df.columns]

    return df[available_columns].sort_values("year")