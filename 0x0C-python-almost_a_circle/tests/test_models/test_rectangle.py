#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class Rec_test(unittest.TestCase):

    def setUp(self):

        """test the creation of Rectangle objects
        with various arguments"""
        self.rect1 = Rectangle(10, 2, 0, 0, 12)

    def test_rectangle_creation(self):
        """Test the attributes of the created Rectangle object."""
        self.assertEqual(self.rect.id, 12)
        self.assertEqual(self.rect.width, 10)
        self.assertEqual(self.rect.height, 2)
        self.assertEqual(self.rect.x, 0)
        self.assertEqual(self.rect.y, 0)

    def tearDown(self):
        self.rect.width = 10
        self.rect.height = 2
        self.rect.x = 0
        self.rect.y = 0
        self.rect.id = 12

if __name__ == '__main__':
    unittest.main()
