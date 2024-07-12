import unittest
from simple_calculator import SimpleCalculator

class TestAdd(unittest.TestCase):

    def test_add_positive(self):
        result = SimpleCalculator.add(self, 3, 4)
        self.assertEqual(result, 7)

    def test_add_negative(self):
        result = SimpleCalculator.add(self, -5, -6)
        self.assertEqual(result, -11)

    def test_add_pos_neg(self):
        result = SimpleCalculator.add(self, 9, -11)
        self.assertEqual(result, -2)

class TestSubtract(unittest.TestCase):
    def test_subtract_positive(self):
        result = SimpleCalculator.subtract(self, 7, 9)
        self.assertEqual(result, -2)

    def test_subtract_negetive(self):
        result = SimpleCalculator.subtract(self, -5, -7)
        self.assertEqual(result, 2)
    
    def test_subtract_pos_neg(self):
        result = SimpleCalculator.subtract(self, -12, 1)
        self.assertEqual(result, -13)

class TestMultipy(unittest.TestCase):
    def test_multiply_positive(self):
        result = SimpleCalculator.multiply(self, 3, 7)
        self.assertEqual(result, 21)

    def test_multiply_negative(self):
        result = SimpleCalculator.multiply(self, -4, -2)
        self.assertEqual(result, 8)
    
    def test_multiply_pos_neg(self):
        result = SimpleCalculator.multiply(self, 5, -3)
        self.assertEqual(result, -15)

class TestDivide(unittest.TestCase):
    def test_divide_positive(self):
        result = SimpleCalculator.divide(self, 10, 2)
        self.assertEqual(result, 5)
    
    def test_divide_negative(self):
        result = SimpleCalculator.divide(self, -15, -5)
        self.assertEqual(result, 3)
    
    def dest_divide_neg_pos(self):
        result = SimpleCalculator.divide(self, 20, -10)
        self.assertEqual(result, -2)


if __name__ == "__main__":
    unittest.main()