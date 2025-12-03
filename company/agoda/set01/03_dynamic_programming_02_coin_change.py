"""Coin Change problem implementation."""
from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    """Return fewest number of coins needed to make up the amount."""
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    print('init - ', dp)
    for coin in coins:
        for value in range(coin, amount + 1):
            print(f'\nbefore {value} - ', dp)
            dp[value] = min(dp[value], dp[value - coin] + 1)
            print('after - ', dp)

    print('\ndone - ', dp)
    return dp[amount] if dp[amount] <= amount else -1


if __name__ == "__main__":
    assert coin_change([1, 2, 5], 11) == 3
    # assert coin_change([5, 2, 1], 11) == 3
    # print(coin_change([1, 2, 5], 13))
    # print(coin_change([2, 5], 0))

