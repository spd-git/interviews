"""Best Time to Buy and Sell Stock problem implementation."""
from typing import List


def max_profit(prices: List[int]) -> int:
    """Return the maximum profit from a single buy and sell operation."""
    min_price = float("inf")
    max_profit_val = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit_val = max(max_profit_val, price - min_price)
    return max_profit_val


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
