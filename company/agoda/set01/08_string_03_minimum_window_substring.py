"""Minimum Window Substring problem implementation."""
from collections import Counter
from typing import Dict


def min_window(s: str, t: str) -> str:
    """Return the minimum window in s that contains all chars of t."""
    if not t or not s:
        return ""
    need = Counter(t)
    missing = len(t)
    left = start = end = 0
    for right, char in enumerate(s, 1):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        while missing == 0:
            if end == 0 or right - left < end - start:
                start, end = left, right
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return s[start:end]


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
