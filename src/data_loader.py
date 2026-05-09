from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"


def _load_csv(filename: str) -> pd.DataFrame:
    """
    Load a CSV file from the data folder.

    Raises:
        FileNotFoundError: If the requested CSV file does not exist.
    """
    file_path = DATA_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(
            f"Could not find {filename} in the data folder.\n"
            f"Expected path: {file_path}"
        )

    return pd.read_csv(file_path)


def load_stockpile_estimates() -> pd.DataFrame:
    return _load_csv("china_stockpile_estimates.csv")


def load_global_forces() -> pd.DataFrame:
    return _load_csv("global_nuclear_forces_2025_estimates.csv")


def load_delivery_systems() -> pd.DataFrame:
    return _load_csv("china_delivery_systems_public_summary.csv")


def load_sources() -> pd.DataFrame:
    return _load_csv("sources.csv")


def load_military_spending() -> pd.DataFrame:
    return _load_csv("china_military_spending_estimates.csv")


def load_nuclear_spending() -> pd.DataFrame:
    return _load_csv("china_nuclear_spending_estimates.csv")