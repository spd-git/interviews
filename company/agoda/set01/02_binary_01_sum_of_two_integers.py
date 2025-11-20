"""Sum of Two Integers problem implementation."""


def get_sum(a: int, b: int) -> int:
    """Compute sum of two integers without using + or - operators."""
    mask = 0xFFFFFFFF
    max_int = 0x7FFFFFFF

    while b != 0:
        carry = (a & b) & mask
        a = (a ^ b) & mask
        b = (carry << 1) & mask

    return a if a <= max_int else ~(a ^ mask)


class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b!=0:
            carry = (a & b)
            a = (a ^ b)
            b = (carry << 1)
        return a


if __name__ == "__main__":
    assert Solution().getSum(1, 2) == 3
