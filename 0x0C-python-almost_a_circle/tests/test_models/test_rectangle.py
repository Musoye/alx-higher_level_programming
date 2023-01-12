#!/usr/bin/python3
"""test the rectangle model"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleInstance(unittest.TestCase):
    """test for rectangle class"""

    def test_for_instance(self):
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_arg_with_no_id(self):
        b1 = Rectangle(1, 2)
        b2 = Rectangle(2, 1)
        self.assertEqual(b1.id, b2.id - 1)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
             print(Rectangle(1, 2, 3, 4).__y)

    def test_y_get(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter_not_int(self):
        r = Rectangle(5, 7, 7, 5, 1)
        with self.assertRaises(TypeError):
            r.y ="hello"

    def test_y_setter_less(self):
        r = Rectangle(5, 7, 7, 5, 1)
        with self.assertRaises(ValueError):
            r.y = -1

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)
