#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Generate Pascal's Triangle up to the nth row.
    Args:
        n (int): The number of rows to generate.
    Returns:
        list: A list of lists representing Pascal's Triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # First element of each row is always 1

        # Calculate the middle elements of the row based on the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
