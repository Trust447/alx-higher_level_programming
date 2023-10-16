import unittest
from models.square import Square


class Sqr_test(unittest.TestCase):
    def setup(self):
        squ1 = Square(10, 0, 0, 1)


    def tearDown(self):
        self.sqr.size = 10
        self.sqr.x = 0
        self.sqr.y = 0
        self.sqr.id = 1

if __name__ == '__main__':
    unittest.main()
