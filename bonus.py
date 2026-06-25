import matplotlib.pyplot as plt
import pandas as pd
from utils import load, isintcompatible


def visualise(df: pd.DataFrame, dfreg: pd.DataFrame):
    """Display scatter plot of the dataset with regression line overlay."""
    try:
        if df is None:
            return

        df = df.dropna()
        print(df)
        print(dfreg)

        plt.figure(figsize=(8, 6))
        plt.plot(dfreg['km'], dfreg['price'], linewidth=2, color="red")
        plt.scatter(
            df['km'],
            df['price'],
            alpha=1,
            color="blue"
        )
        plt.xlabel('Kilometers')
        plt.ylabel('Price')
        plt.title('Car Price by km')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


def estimatePrice(mileage, theta0, theta1) -> float:
    return theta0 + (theta1 * mileage)


def main():
    """Main"""
    try:
        df = load("data.csv")
        if df is None:
            return
        theta0 = 0
        theta1 = 0
        try:
            df_t = pd.read_csv("learning.csv")
        except Exception:
            print("learning.csv don't exist")
            return
        try:
            theta0 = df_t['theta0'][0]
            theta1 = df_t['theta1'][0]
        except Exception as e:
            print(f"Error : {e} doesn't exist in learning.csv")
            return None
        if not isintcompatible(theta0) or not isintcompatible(theta1):
            print("Invalid theta")
            return

        df_km = [min(df['km']), max(df['km'])]
        df_pr = [estimatePrice(km, theta0, theta1) for km in df_km]
        dict_df = pd.DataFrame({'km': df_km, "price": df_pr})
        visualise(df, dict_df)
    except Exception as e:
        print(f"Error : {e}")
    return


if __name__ == "__main__":
    main()
