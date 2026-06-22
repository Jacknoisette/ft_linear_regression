import pandas as pd
from visuals import visualise_update


def normalized_init(list):
    """Return a closure that normalizes values at index i to [0, 1]."""
    lmax = max(list)
    lmin = min(list)

    def normalized(i):
        return ((list[i] - lmin) / (lmax - lmin))

    return normalized


def learning(func: dict, df: pd.DataFrame, line):
    """Train theta0 and theta1 via gradient descent until convergence."""
    m = df.shape[0]
    diff = 1
    learning_rate = 0.5
    it = 0
    norm_km = normalized_init(df['km'])
    norm_pr = normalized_init(df['price'])
    while (diff > 0.0001):
        tmp_theta0 = 0
        tmp_theta1 = 0
        it += 1
        for i in range(m):
            error = func["estimatePriceLearning"](norm_km(i)) - norm_pr(i)
            tmp_theta0 += error
            tmp_theta1 += error * norm_km(i)
        tmp_theta0 = learning_rate * (1 / m) * tmp_theta0
        tmp_theta1 = learning_rate * (1 / m) * tmp_theta1
        diff = func["updateThetas"](tmp_theta0, tmp_theta1)
        visualise_update(line, func, df)
    print("Learned in", it, "iteration")
    return
