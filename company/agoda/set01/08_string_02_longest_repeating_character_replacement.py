"""Longest Repeating Character Replacement problem implementation."""
from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
    """Sliding window where we track the most frequent character count."""
    counts = defaultdict(int)
    left = max_count = result = 0
    for right, char in enumerate(s):
        counts[char] += 1
        max_count = max(max_count, counts[char])
        while (right - left + 1) - max_count > k:
            counts[s[left]] -= 1
            left += 1
        result = max(result, right - left + 1)
    return result


if __name__ == "__main__":
    assert character_replacement("ABAB", 2) == 4
