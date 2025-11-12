"""Reverse Bits problem implementation."""


def reverse_bits(n: int) -> int:
    """Reverse bits of a 32-bit unsigned integer."""
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result


if __name__ == "__main__":
    assert reverse_bits(0b00000010100101000001111010011100) == 0b00111001011110000010100101000000
