import unittest
from models.rectangle import Rectangle


class Rec_test(unittest.TestCase):

    def test_rectangle_creation(self):
        """test the creation of Rectangle objects
        with various arguments"""
        rect1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rect1.id, 12)

        rect2 = Rectangle(10, 2)
        self.assertEqual(rect2.id, 1)

        self.assertEqual(self.rect.width, 10)

    def tearDown(self):
        if hasattr(self, 'rect'):
            del self.rect

if __name__ == '__main__':
    unittest.main()
