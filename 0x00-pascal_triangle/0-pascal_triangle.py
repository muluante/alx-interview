#!/usr/bin/python3
""" A module for working Pascal's Triangle """


def pascal_triangle(n):
    """
    Returns a list of integers representing
    the Pascals triangle on a given integer.
    """
    array = []

    for i in range(n):
        arrayNew = []
        for j in range(i + 1):
            if j < 2:
                arrayNew.append(1)
            else:
                arrayNew.insert((j - 1),
                                (array[i - 1][j - 2] + array[i - 1][j - 1]))

        array.append(arrayNew)

    return array
