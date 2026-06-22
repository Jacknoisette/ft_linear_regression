import pandas as pd
from utils import isintcompatible


def estimatePrice(path) -> float:
    theta0 = 0
    theta1 = 0
    text = input("What is the mileage ?\n")
    if (text == ''):
        print("No mileage given")
        return
    if not isintcompatible(text):
        print("Invalid mileage")
        return
    text = int(text)
    try:
        df = pd.read_csv(path)
    except Exception:
        return theta0 + (theta1 * text)
    theta0 = df['theta0'][0]
    theta1 = df["theta1"][0]
    if not isintcompatible(theta0) or not isintcompatible(theta1):
        print("Invalid theta")
        return
    return theta0 + (theta1 * text)


def main():
    """Main"""
    print(estimatePrice("learning.csv"))


if __name__ == "__main__":
    main()
