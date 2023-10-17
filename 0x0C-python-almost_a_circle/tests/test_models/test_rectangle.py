#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class Rec_test(unittest.TestCase):

    def setUp(self):

        """test the creation of Rectangle objects
        with various arguments"""
        rect1 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        self.rect.width = 10
        self.rect.height = 2
        self.rect.x = 0
        self.rect.y = 0
        self.rect.id = 12

if __name__ == '__main__':
    unittest.main()
