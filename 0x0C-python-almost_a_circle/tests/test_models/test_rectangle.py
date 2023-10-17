#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class Rec_test(unittest.TestCase):

    def test_setUp(self):

        """test the creation of Rectangle objects
        with various arguments"""
        rect = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 12)

    def test_rectangle_creation(self):
        """Test the attributes of the created Rectangle object."""
        rect = Rectangle(10, 2, 0, 0,)
        self.assertEqual(rect.id, 1)

if __name__ == '__main__':
    unittest.main()
