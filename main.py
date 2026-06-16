import pandas as pd
from bonus import visualise, algorithm_precision
from compute import computePrice
from learning import learning


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


def main():
    """Main"""
    df = load("data.csv")
    func = computePrice(df['km'], df['price'])
    learning(func, df)

    R = algorithm_precision(df, func)
    print("Algorithm Precision R :", R)

    df_km = [min(df['km']), max(df['km'])]
    df_pr = [func['estimatePrice'](km) for km in df_km]
    dict_df = pd.DataFrame({'km': df_km, "price": df_pr})

    visualise(df, dict_df)


if __name__ == "__main__":
    main()
