#!/usr/bin/python3
"""
A module that test differents behaviors
of the Square class
"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit tests for testing the Square class."""

    def test_getter(self):
        """Test the getter method of Square."""
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_setter(self):
        """Test the setter method of Square."""
        square = Square(5)
        square.size = 8
        self.assertEqual(square.size, 8)

    def test_string(self):
        """Test setting size with a string value."""
        square = Square(3)
        with self.assertRaises(TypeError):
            square.size = "Hi"

    def test_negative(self):
        """Test setting size with a negative value."""
        square = Square(6)
        with self.assertRaises(ValueError):
            square.size = -5

    def test_zero(self):
        """Test setting size with zero."""
        square = Square(6)
        with self.assertRaises(ValueError):
            square.size = 0

    def test_decimal(self):
        """Test setting size with a decimal value."""
        square = Square(6)
        with self.assertRaises(TypeError):
            square.size = 1.5

    def test_tuple(self):
        """Test setting size with a tuple value."""
        square = Square(7)
        with self.assertRaises(TypeError):
            square.size = (2, 8)

    def test_empty(self):
        """Test setting size with an empty value."""
        square = Square(7)
        with self.assertRaises(TypeError):
            square.size = ""

    def test_none(self):
        """Test setting size with None."""
        square = Square(5)
        with self.assertRaises(TypeError):
            square.size = None

    def test_list(self):
        """Test setting size with a list value."""
        square = Square(4)
        with self.assertRaises(TypeError):
            square.size = [4, 7]

    def test_dict(self):
        """Test setting size with a dictionary value."""
        square = Square(5)
        with self.assertRaises(TypeError):
            square.size = {"hi": 5, "world": 8}

    def test_width(self):
        """Test if width and height are updated when setting size."""
        square = Square(5)
        square.size = 6
        self.assertEqual(square.width, 6)
        self.assertEqual(square.height, 6)

    def test_to_dictionary(self):
        """Test the to_dictionary method of Square."""
        Base._Base__nb_objects = 0

        square = Square(10, 2, 1, 9)
        square_dict = square.to_dictionary()
        expected = {"id": 9, "x": 2, "size": 10, "y": 1}
        self.assertEqual(square_dict, expected)

        square = Square(1, 0, 0, 9)
        square_dict = square.to_dictionary()
        expected = {"id": 9, "x": 0, "size": 1, "y": 0}
        self.assertEqual(square_dict, expected)

        square.update(5, 5, 5, 5)
        square_dict = square.to_dictionary()
        expected = {"id": 5, "x": 5, "size": 5, "y": 5}
        self.assertEqual(square_dict, expected)


if __name__ == "__main__":
    unittest.main()
