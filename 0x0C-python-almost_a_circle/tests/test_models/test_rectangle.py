#!/usr/bin/python3
"""test the rectangle model"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import sys


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


class TestAReaRectangle(unittest.TestCase):
    """Test for Area of Rectangle"""

    def test_area_with_pre(self):
        r = Rectangle(10, 2)
        self.assertEqual(20, r.area())

    def test_area_with_other(self):
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(56, r.area())

    def test_area_with_modify(self):
        r = Rectangle(9, 3)
        r.width = 10
        self.assertEqual(30, r.area())

    def test_arear_height(self):
        r = Rectangle(9, 3)
        r.height = 10
        self.assertEqual(90, r.area())

    def test_arear_both(self):
        r = Rectangle(1, 2)
        r.width = 11
        r.height = 10
        self.assertEqual(110, r.area())


class TestRectangle_stdout(unittest.TestCase):
    """test fot stdout of display"""

    @staticmethod
    def capture_stdout(rec, method):
        """capture the stdout"""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rec)
        else:
            rec.display()
        sys.stdout = sys.__stdout__
        return(capture)

     ##test display
    def test_display_width(self):
        """test the display"""
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_height(self):
        """test the display"""
        r = Rectangle(4, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("####\n####\n####\n", capture.getvalue())
