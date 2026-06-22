import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a CSV file and return it as a DataFrame."""
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")
        df = pd.read_csv(path)
        print(f"Loading Dataframe {path} of length {df.shape[0]}")
        pd.set_option('display.max_rows', None)
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None


def isintcompatible(value) -> bool:
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False
