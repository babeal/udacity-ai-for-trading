"""
Estimate Volatility
Create an exponential moving average model of volatility. Use the formula in your notes:
where r_n is the nth daily return, and \sigma_nσ is the nth estimate of the volatility.
\lambdaλ is a constant between 0 and 1 that defines how quickly weights on older data should decrease.
A high value of \lambdaλ (close to 1) will cause older data to matter relatively more in the calculation of \sigma_nσ.
A very low value of \lambdaλ will mean that recent data matter more—in this case, the successive daily estimates of \sigma_nσ
themselves will be volatile.

Pandas provides built-in exponentially weighted moving window functions with the .ewm method.
Consider using .ewm().mean(), and be sure to properly specify the alpha parameter (hint: it is related to, but not equal to \lambdaλ).

** the ema function using (1-alpha), so since they pass us lambda we need to 1-lambda to get the method to work properly

Note that .ewm().std() and .ewm().var() implement ewmvar(x) = ewma(x**2) - ewma(x)**2,
which is slightly different than what you'll want to implement for this problem.

Other resources.  
https://knowledge.udacity.com/questions/413282
https://knowledge.udacity.com/questions/157360
https://knowledge.udacity.com/questions/381675
https://knowledge.udacity.com/questions/43364

Result

0.004940582044719361
Most recent volatility estimate: 0.004941
"""

import pandas as pd
import numpy as np
import math


def estimate_volatility(prices, l):
    """Create an exponential moving average model of the volatility of a stock
    price, and return the most recent (last) volatility estimate.

    Parameters
    ----------
    prices : pandas.Series
        A series of adjusted closing prices for a stock.

    l : float
        The 'lambda' parameter of the exponential moving average model. Making
        this value smaller will cause the model to weight older terms less
        relative to more recent terms.

    Returns
    -------
    last_vol : float
        The last element of your exponential moving averge volatility model series.

    """
    # TODO: Implement the exponential moving average volatility model and return the last value.
    # calculate log returns
    returns = np.log(prices) - np.log(prices.shift(1))

    # square log returns
    returns_squared = returns ** 2

    # take the ewm mean
    result = returns_squared.ewm(alpha=1 - l).mean()

    # take the square root of the results
    ema = np.sqrt(result.iloc[-1])
    print(ema)

    return ema


def test_run(filename="data.csv"):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=["date"], index_col="date", squeeze=True)
    print("Most recent volatility estimate: {:.6f}".format(estimate_volatility(prices, 0.7)))


if __name__ == "__main__":
    test_run()
