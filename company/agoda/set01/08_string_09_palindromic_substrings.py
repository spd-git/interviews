"""Palindromic Substrings problem implementation."""


def count_substrings(s: str) -> int:
    """Expand around center to count palindromic substrings."""
    count = 0
    for center in range(2 * len(s) - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    return count


if __name__ == "__main__":
    assert count_substrings("aaa") == 6
