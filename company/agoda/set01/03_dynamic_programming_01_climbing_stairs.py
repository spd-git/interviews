"""Climbing Stairs problem implementation."""


def climb_stairs(n: int) -> int:
    """Return number of distinct ways to climb to the top."""
    if n <= 2:
        return n
    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second


if __name__ == "__main__":
    assert climb_stairs(3) == 3
