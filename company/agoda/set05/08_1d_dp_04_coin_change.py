from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Bottom-up DP computing min coins for each value up to amount."""
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for val in range(coin, amount + 1):
                dp[val] = min(dp[val], dp[val - coin] + 1)
        return dp[amount] if dp[amount] <= amount else -1
