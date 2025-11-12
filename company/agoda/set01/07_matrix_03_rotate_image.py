"""Rotate Image problem implementation."""
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """Rotate the square matrix by 90 degrees clockwise in-place."""
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()


if __name__ == "__main__":
    sample = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(sample)
    assert sample == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
