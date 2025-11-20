"""Climbing Stairs problem implementation."""
from itertools import permutations



def climb_stairs(n: int) -> int:
    """Return number of distinct ways to climb to the top."""
    if n <= 2:
        return n
    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second


if __name__ == "__main__":
    perm = permutations([1] * 3, 2)

    for i in perm:
        print(i)
    assert climb_stairs(3) == 3
