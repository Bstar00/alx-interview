#!/usr/bin/python3
"""
Defines function that returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Creates a list of lists of integers representing Pascal's triangle

    parameters:
        n [int]:
            the number of rows of Pascal's triangle to recreate

    return:
        [list of lists of ints]:
            representation of Pascal's triangle
    """
    if type(n) is not int:
        raise TypeError("n must be an integer")
    
    triangle = []
    for row_index in range(n):
        rowlist = [1] * (row_index + 1)
        for i in range(1, row_index):
            rowlist[i] = triangle[row_index - 1][i - 1] + triangle[row_index - 1][i]
        triangle.append(rowlist)
    
    return triangle
