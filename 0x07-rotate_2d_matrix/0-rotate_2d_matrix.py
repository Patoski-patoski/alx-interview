#!/usr/bin/python3
"""0-rotate_2d_matrix module"""


def rotate_2d_matrix(matrix):
    """rotates a 2D matrix by 90 degree
    Args:
        matrix (_type_): nested 2D list
    """
    length = len(matrix)
    for i in range(length):
        for j in range(i + 1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    reverse = 0 - length
    for i in range(length):
        k = -1
        while(reverse < k):
            matrix[i][reverse], matrix[i][k] = matrix[i][k], \
                    matrix[i][reverse],
            k = reverse
