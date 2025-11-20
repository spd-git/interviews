

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """Add binary strings using bit-style carry propagation."""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        result = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            carry, bit = divmod(total, 2)
            result.append(str(bit))
        return "".join(reversed(result))
