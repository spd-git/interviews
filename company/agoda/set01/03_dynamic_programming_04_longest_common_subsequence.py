"""Longest Common Subsequence problem implementation."""
from typing import List


def longest_common_subsequence(text1: str, text2: str) -> int:
    """Return length of longest common subsequence between two strings."""
    m, n = len(text1), len(text2)
    dp: List[List[int]] = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]


if __name__ == "__main__":
    assert longest_common_subsequence("abcde", "ace") == 3
