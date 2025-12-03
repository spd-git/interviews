"""Valid Anagram problem implementation."""
from collections import Counter


def _is_anagram(s: str, t: str) -> bool:
    """Check whether t is an anagram of s."""
    return Counter(s) == Counter(t)

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts = [0] * 26  # assuming lowercase English letters
    for c1, c2 in zip(s, t):
        counts[ord(c1) - ord('a')] += 1
        counts[ord(c2) - ord('a')] -= 1
    return all(count == 0 for count in counts)

if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
