#!/usr/bin/bash
"""The test module for square.py"""
from models.rectangle import Rectangle
from models.square import Square
import unittest
#import io
#import sys


class TestSquareInstatiation(unittest.TestCase):
    """Instatiation testing"""

    def test_instance_a(self):
        s1 = Square(1, 2, 3)
        s2 = Square(4, 3, 2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_instance_with_id(self):
        s1 = Square(2, 3, 4, 5)
        self.assertEqual(s1.id, 5)

    def test_instance_b(self):
        with self.assertRaises(TypeError):
            Square()

    def test_instance_id(self):
        s1 = Square(2, 3, 4, 'boy')
        self.assertEqual(s1.id, 'boy')

    def test_instance_from(self):
        s1 = Square(3)
        self.assertIsInstance(s1, Rectangle)

class TestChangecase(unittest.TestCase):
    """change test for width"""

    def test_update_x(self):
        s1 = Square(1, 2, 4, 5)
        s1.x = 9
        self.assertEqual(s1.x, 9)

    def test_get_width_height(self):
        s1 = Square(2)
        self.assertEqual(s1.width, s1.height)

class TestPrintSquare(unittest.TestCase):
    """testing the handler of print(__str__)"""

    def test_width_height_only(self):
        s1 = Square(2)
        s1.id = 4
        m = "[Square] (4) 0/0 - 2"
        self.assertEqual(m, str(s1))

    def test_all_define(self):
        s1 = Square(4, 3, 2, 5)
        d = "[Square] (5) 3/2 - 4"
        self.assertEqual(d, s1.__str__())

    def test_x_or_y_change(self):
        s1 = Square(4, 3, 2, 5)
        s1.x = 25
        d ="[Square] (5) 25/2 - 4"
        self.assertEqual(d, s1.__str__())
