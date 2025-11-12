"""Word Break problem implementation."""
from typing import List, Set


def word_break(s: str, word_dict: List[str]) -> bool:
    """Dynamic programming solution for word break."""
    words: Set[str] = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]


if __name__ == "__main__":
    assert word_break("leetcode", ["leet", "code"]) is True
