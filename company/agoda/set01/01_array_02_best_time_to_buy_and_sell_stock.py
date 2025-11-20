"""Best Time to Buy and Sell Stock problem implementation."""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Return the maximum profit from a single buy and sell operation.
        """
        min_price = 10000       # As 0 <= prices[i] <= 10^4
        max_profit = 0
        for price in prices:
            if min_price > price:
                min_price = price
                continue
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit

if __name__ == "__main__":
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
