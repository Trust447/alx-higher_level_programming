#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestBaseClass(unittest.TestCase):

    def test_instance_id_values(self):
         b1 = Base()
         b2 = Base()
         b4 = Base()
         self.assertEqual(b1.id, 1)
         self.assertEqual(b2.id, 2)
         self.assertEqual(b4.id, 3)

if __name__ == '__main__':
    unittest.main()
