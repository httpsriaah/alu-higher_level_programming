#!/usr/bin/python3
"""Module that defines a square that can print itself."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize the square with an optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size after validating its type and value."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the character #."""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
