import matplotlib.pyplot as plt
import pandas as pd


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


def algorithm_precision(df: pd.DataFrame, func: dict):
    """Compute the R-squared coefficient of determination for the model."""
    mean = sum(df['price']) / df.shape[0]
    err_sqrd = [(df['price'][i] - func['estimatePrice'](df['km'][i]))**2
                for i in range(df.shape[0])]
    numerator = sum(err_sqrd)
    mean_sqrd = [(pr - mean)**2 for pr in df['price']]
    denominator = sum(mean_sqrd)

    return 1 - numerator / denominator
