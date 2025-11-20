

class Solution:
    def trailingZeroes(self, n: int) -> int:
        """Count factors of 5 in n! since 2s are abundant."""
        count = 0
        while n:
            n //= 5
            count += n
        return count
