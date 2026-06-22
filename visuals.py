import matplotlib.pyplot as plt
import pandas as pd


def visualise_init(df: pd.DataFrame):
    """Initialize the interactive plot. Returns the line object to update."""
    df = df.dropna()
    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df['km'], df['price'], alpha=1, color="blue")
    line, = ax.plot([], [], linewidth=2, color="red")
    ax.set_xlabel('Kilometers')
    ax.set_ylabel('Price')
    ax.set_title('Car Price by km')
    ax.set_xlim(min(df['km']) - 5000, max(df['km']) + 5000)
    ax.set_ylim(min(df['price']) - 500, max(df['price']) + 500)
    plt.tight_layout()
    return line


def visualise_update(line, func, df):
    """Update the regression line on the existing plot."""
    x = [min(df['km']), max(df['km'])]
    y = [func['estimatePrice'](km) for km in x]
    line.set_xdata(x)
    line.set_ydata(y)
    plt.pause(0.01)


def visualise_end():
    """Switch off interactive mode and keep the window open."""
    plt.ioff()
    plt.show()
