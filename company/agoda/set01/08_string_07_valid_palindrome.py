"""Valid Palindrome problem implementation."""


def is_palindrome(s: str) -> bool:
    """Check if string is palindrome considering only alphanumeric characters."""
    filtered = [char.lower() for char in s if char.isalnum()]
    return filtered == filtered[::-1]


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
