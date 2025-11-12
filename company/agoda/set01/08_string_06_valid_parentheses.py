"""Valid Parentheses problem implementation."""

def is_valid(s: str) -> bool:
    """Check whether the string of brackets is valid."""
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            continue
    return not stack


if __name__ == "__main__":
    assert is_valid("()[]{}") is True
