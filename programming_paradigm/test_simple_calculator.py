import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
         
        self.assertEqual(self.calc.add( 3, 4), 7)
        self.assertEqual(self.calc.add(-5, -6), -11)
        self.assertEqual(self.calc.add(9, -11), -2)


    def test_subtraction(self):    
        self.assertEqual(self.calc.subtract(7, 9), -2)
        self.assertEqual(self.calc.subtract( -5, -7), 2)
        self.assertEqual(self.calc.subtract(-12, 1), -13)


    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-4, -2), 8)
        self.assertEqual(self.calc.multiply(5, -3), -15)


    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-15, -5), 3)
        self.assertEqual(self.calc.divide(20, -10), -2)


if __name__ == "__main__":
    unittest.main()