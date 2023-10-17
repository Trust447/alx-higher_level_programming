#!/usr/bin/python3
import unittest
from models.square import Square


class Sqr_test(unittest.TestCase):
    def test_setup(self):
        squ1 = Square(10, 0, 0, 1)


    def test_tearDown(self):

        squ = Square(10, 0, 0, 1)
        self.assertEqual(squ.size, 10)
        self.assertEqual(squ.x, 0)
        self.assertEqual(squ.y, 0)
        self.assertEqual(squ.id, 1)

if __name__ == '__main__':
    unittest.main()
