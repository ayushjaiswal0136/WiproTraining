import sys
import unittest

from src.calculations import add, sub, mul, div, ne

class TestCalculations(unittest.TestCase):
    def test_add(self):
        res = add(10,5)
        self.assertEqual(15, res,msg='Addition Err')

    def test_sub(self):
        res = sub(10,5)
        self.assertEqual(5,res,msg='Subtraction Err')

    def test_mul(self):
        res = mul(10,5)
        self.assertEqual(50,res,msg='Multiplication Err')

    def test_div(self):
        res = div(10,5)
        self.assertEqual(2.0,res,msg='Division Err')

    @unittest.skipIf(sys.version_info<(3,13),reason='Not Implemented')
    def test_ne(self):
        res = ne(10,10)
        self.assertTrue(res,msg='Not Equal')

    def test_diverr(self):
        with self.assertRaises(ZeroDivisionError, msg="NoException"):
            div(10,0)
