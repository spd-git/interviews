
def power_recursive(x: float, n: int) -> float:
    """
    Returns the value of x raised to the power of n.
    """
    if n == 0:
        # x^0 = 1
        return 1
    elif n < 0:
        # x^-n = 1/x^n
        return 1 / power_recursive(x, -n)
    else:
        v = power_recursive(x, n // 2)

        if n % 2 == 0:
            # x^n = x^(n//2) * x^(n//2) if n is even
            return v * v
        else:
            # x^n = x * x^(n//2) * x^(n//2) if n is odd
            return x * v * v


print(power_recursive(2, -3))
