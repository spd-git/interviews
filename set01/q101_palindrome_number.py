"""
101 Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.
"""


def is_palindrome(n: int) -> bool:
    if n < 0:
        return False

    div = 1
    while (n / div) >= 10:
        div *= 10

    while n != 0:
        left = n // div         # leftmost digit
        right = n % 10          # rightmost digit
        if left != right:
            return False
        n = (n % div) // 10     # 2 digits are removed from n
        div /= 100              # because 2 digits are removed from n
    return True


print(is_palindrome(121))
