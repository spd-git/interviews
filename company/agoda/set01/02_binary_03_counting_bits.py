"""Counting Bits problem implementation."""
from typing import List


def count_bits(n: int) -> List[int]:
    """Return number of set bits for every number in range [0, n]."""
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)
    return bits


if __name__ == "__main__":
    assert count_bits(5) == [0, 1, 1, 2, 1, 2]
