#!/usr/bin/python3
"""Module that defines a square with a private size."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size):
        """Initialize the square with a private size."""
        self.__size = size
