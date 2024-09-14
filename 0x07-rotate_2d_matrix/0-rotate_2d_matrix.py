#!/usr/bin/python3
"""0-rotate_2d_matrix.py module"""

def rotate_2d_matrix(matrix):
    """rotates a 2D matrix by 90 degree
    Args:
        matrix (_type_): nested 2D list
    """
    length = len(matrix)
    for i in range(length):
        for j in range(i + 1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(length):
        matrix[i].reverse()
