from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """DP optimized to O(k*n) tracking buy/sell states."""
        if not prices or k == 0:
            return 0
        if k >= len(prices) // 2:
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)
        for price in prices:
            for i in range(1, k + 1):
                buy[i] = max(buy[i], sell[i - 1] - price)
                sell[i] = max(sell[i], buy[i] + price)
        return sell[k]
