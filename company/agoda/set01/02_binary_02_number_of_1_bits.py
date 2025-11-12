"""Number of 1 Bits problem implementation."""


def hamming_weight(n: int) -> int:
    """Return the number of 1 bits using Brian Kernighan's algorithm."""
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


if __name__ == "__main__":
    assert hamming_weight(0b1011) == 3
