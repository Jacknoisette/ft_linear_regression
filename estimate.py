import pandas as pd
from utils import isintcompatible


def estimatePrice() -> float:
    try:
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
            df = pd.read_csv("learning.csv")
        except Exception:
            return theta0 + (theta1 * text)
        try:
            theta0 = df['theta0'][0]
            theta1 = df['theta1'][0]
        except Exception as e:
            print(f"Error : {e} doesn't exist in learning.csv")
            return None
        if not isintcompatible(theta0) or not isintcompatible(theta1):
            print("Invalid theta")
            return None
        return theta0 + (theta1 * text)
    except Exception as e:
        print(f"Error : {e}")
    return None


def main():
    """Main"""
    try:
        print(estimatePrice())
    except Exception as e:
        print(f"Error : {e}")
    return None


if __name__ == "__main__":
    main()
