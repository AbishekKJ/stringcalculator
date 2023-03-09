import unittest
from src.stringcalculator import StringCalculator


class TestStringCalculator(unittest.TestCase):

    def test_Add(self):
        calculator = StringCalculator
        self.assertEqual(calculator.Add(""), 0)
        self.assertEqual(calculator.Add("1"), 1)
        self.assertEqual(calculator.Add("1,"), 1)
        self.assertEqual(calculator.Add("1,2"), 3)
        self.assertEqual(calculator.Add("1,2,"), 3)
        self.assertEqual(calculator.Add("1\n2,3"), 6)
        self.assertEqual(calculator.Add("//;\n1;2"), 3)
        self.assertEqual(calculator.Add("// [*][ %]\n1 * 2 % 3"), 6)


if __name__ == '__main__':
    unittest.main()