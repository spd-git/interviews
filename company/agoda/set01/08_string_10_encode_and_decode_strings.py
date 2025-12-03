"""Encode and Decode Strings (Leetcode Premium) problem implementation."""
from typing import List


SEPARATOR = '#'


def encode(strs: List[str]) -> str:
    """Encode list of strings into a single string with length prefixes."""
    return ''.join(f"{len(s)}{SEPARATOR}{s}" for s in strs)


def decode(s: str) -> List[str]:
    """Decode string produced by encode back into list of strings."""
    result = []
    i = 0
    while i < len(s):
        j = s.find(SEPARATOR, i)
        length = int(s[i:j])
        j += 1
        result.append(s[j:j + length])
        i = j + length
    return result


if __name__ == "__main__":
    sample = ["lint", "code", "love", "you"]
    encoded = encode(sample)
    print(encoded)
    assert decode(encoded) == sample
