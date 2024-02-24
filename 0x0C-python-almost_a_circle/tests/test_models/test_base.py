import unittest
from models.base import Base

class Test_test_base(unittest.TestCase):
    def test_class(self):
        test = Base()
        self.assertEqual(test.id, 1)
        test = Base(5)
        self.assertEqual(test.id, 5)
        test = Base()
        self.assertEqual(test.id, 2)
