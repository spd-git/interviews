"""Longest Palindromic Substring problem implementation."""


def longest_palindrome(s: str) -> str:
    """Expand around center to find the longest palindromic substring."""
    if len(s) < 2:
        return s

    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    longest = s[0]
    for i in range(len(s)):
        odd = expand(i, i)
        even = expand(i, i + 1)
        longest = max(longest, odd, even, key=len)
    return longest


if __name__ == "__main__":
    assert longest_palindrome("babad") in {"bab", "aba"}
