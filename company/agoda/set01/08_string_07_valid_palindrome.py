"""Valid Palindrome problem implementation."""


def is_palindrome(s: str) -> bool:
    """Check if string is palindrome considering only alphanumeric characters."""
    filtered = [char.lower() for char in s if char.isalnum()]
    return filtered == filtered[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
