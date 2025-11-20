from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """DP where dp[i] denotes segmentability up to i."""
        word_set = set(wordDict)
        max_len = max((len(w) for w in word_set), default=0)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for l in range(1, min(max_len, i) + 1):
                if not dp[i - l]:
                    continue
                if s[i - l:i] in word_set:
                    dp[i] = True
                    break
        return dp[-1]
