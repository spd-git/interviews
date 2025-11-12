"""Unique Paths problem implementation."""


def unique_paths(m: int, n: int) -> int:
    """Compute number of unique paths in m x n grid."""
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]


if __name__ == "__main__":
    assert unique_paths(3, 7) == 28
