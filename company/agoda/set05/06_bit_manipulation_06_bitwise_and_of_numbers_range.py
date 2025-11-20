

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """Find common prefix by shifting until bounds align."""
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
