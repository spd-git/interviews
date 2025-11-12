"""Set Matrix Zeroes problem implementation."""
from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
    """Modify matrix in-place by setting rows and columns to zero."""
    if not matrix or not matrix[0]:
        return
    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
    first_col_zero = any(matrix[r][0] == 0 for r in range(rows))

    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    for r in range(1, rows):
        if matrix[r][0] == 0:
            for c in range(cols):
                matrix[r][c] = 0

    for c in range(1, cols):
        if matrix[0][c] == 0:
            for r in range(rows):
                matrix[r][c] = 0

    if first_row_zero:
        for c in range(cols):
            matrix[0][c] = 0

    if first_col_zero:
        for r in range(rows):
            matrix[r][0] = 0


if __name__ == "__main__":
    sample = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(sample)
    assert sample == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
