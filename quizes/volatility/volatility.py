import pandas as pd
import numpy as np

# Volatility literally refers to how "volatile" a stock is, meaning how unpredictably its price might change.
# A statistical measure of dispersion, such as standard deviation, is commonly used to measure volatility.

# In the exercise below, you're given daily prices for two sample stocks.
# Compute the standard deviations of their log returns, and return the ticker symbol for the stock that is more volatile.


def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.

    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']

    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    # TODO: Fill in this function.
    curr_prices = prices.reset_index().pivot(index="date", columns="ticker", values="price")
    shifted_prices = curr_prices.shift(1)
    returns = curr_prices.applymap(np.log) - shifted_prices.applymap(np.log)
    std = returns.std()
    print(std)
    most_volatile = std.idxmax()
    print(most_volatile)
    # most_volatile = std.loc[most_volatile_value]
    # print(most_volatile)

    return most_volatile
