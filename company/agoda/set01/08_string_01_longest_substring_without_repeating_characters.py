"""Longest Substring Without Repeating Characters problem implementation."""
from typing import Dict


def length_of_longest_substring(s: str) -> int:
    """Sliding window approach to find longest unique substring length."""
    seen: Dict[str, int] = {}
    left = result = 0
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        result = max(result, right - left + 1)
    return result


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
