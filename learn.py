import pandas as pd
from compute import computePrice
from expression import learning
from visuals import visualise_end, visualise_init
from utils import load


def algorithm_precision(df: pd.DataFrame, func: dict):
    """Compute the R-squared coefficient of determination for the model."""
    mean = sum(df['price']) / df.shape[0]
    err_sqrd = [(df['price'][i] - func['estimatePrice'](df['km'][i]))**2
                for i in range(df.shape[0])]
    numerator = sum(err_sqrd)
    mean_sqrd = [(pr - mean)**2 for pr in df['price']]
    denominator = sum(mean_sqrd)

    return 1 - numerator / denominator


def main():
    """Main"""
    try:
        df = load("data.csv")
        if df is None:
            return
        func = computePrice(df['km'], df['price'])

        line = visualise_init(df)
        learning(func, df, line)
        visualise_end()

        R = algorithm_precision(df, func)
        print("Algorithm Precision R :", R)

        real_theta0 = func['estimatePrice'](0)
        real_theta1 = func['estimatePrice'](1) - func['estimatePrice'](0)

        df = pd.DataFrame({'theta0': [real_theta0], 'theta1': [real_theta1]})
        df.to_csv("learning.csv", index=False)
    except Exception as e:
        print(f"Error : {e}")
    return


if __name__ == "__main__":
    main()
