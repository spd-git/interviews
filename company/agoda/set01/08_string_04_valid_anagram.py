"""Valid Anagram problem implementation."""
from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    """Check whether t is an anagram of s."""
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
