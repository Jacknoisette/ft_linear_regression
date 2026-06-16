def computePrice(df_km, df_pr) -> dict:
    """Create a linear regression model with closure-based theta state.

    Returns estimatePrice (real values), estimatePriceLearning (normalized),
    and updateThetas (applies gradient corrections).
    """
    theta0 = 0.0
    theta1 = 0.0

    def estimatePrice(mileage) -> float:
        norm_km = ((mileage - min(df_km)) / (max(df_km) - min(df_km)))
        pr_norm = theta0 + (theta1 * norm_km)
        price = pr_norm * (max(df_pr) - min(df_pr)) + min(df_pr)
        return price

    def estimatePriceLearning(mileage) -> float:
        return theta0 + (theta1 * mileage)

    def updateThetas(tmp_theta0, tmp_theta1) -> float:
        nonlocal theta0
        nonlocal theta1
        diff = abs(tmp_theta0) + abs(tmp_theta1)
        theta0 = theta0 - tmp_theta0
        theta1 = theta1 - tmp_theta1
        #         print(f"""
        # theta0 : {theta0}
        # tmp_theta0 : {tmp_theta0}
        # diff0 : {abs(theta0 - tmp_theta0)}
        # theta1 : {theta1}
        # tmp_theta1 : {tmp_theta1}
        # diff1 : {abs(theta0 - tmp_theta1)}
        # diff : {diff}""")
        return diff

    return {"estimatePriceLearning": estimatePriceLearning,
            "updateThetas": updateThetas,
            "estimatePrice": estimatePrice}
