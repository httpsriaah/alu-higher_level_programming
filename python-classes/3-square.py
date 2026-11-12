#!/usr/bin/python3
"""Module that defines a square and computes its area."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize the square with a validated private size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
