import unittest

from src.stringcalculator import StringCalculator
from src.exceptions.stringcalculatorexceptions import *


class TestStringCalculator(unittest.TestCase):

    calculator = StringCalculator

    def test_Add_with_empty_string(self):
        self.assertEqual(TestStringCalculator.calculator.Add(""), 0)

    def test_Add_with_positive_numbers(self):
        self.assertEqual(TestStringCalculator.calculator.Add("1"), 1)
        self.assertEqual(TestStringCalculator.calculator.Add("1,2"), 3)

    def test_Add_with_positive_numbers_with_comma_at_end(self):
        self.assertEqual(TestStringCalculator.calculator.Add("1,"), 1)
        self.assertEqual(TestStringCalculator.calculator.Add("1,2,"), 3)

    def test_Add_with_new_line_inbetween(self):
        self.assertEqual(TestStringCalculator.calculator.Add("1\n2,3"), 6)

    def test_Add_with_custom_delimiter(self):
        self.assertEqual(TestStringCalculator.calculator.Add("//;\n1;2"), 3)

    def test_Add_with_custom_delimiter_and_new_line_inbetween(self):
        self.assertEqual(TestStringCalculator.calculator.Add("//;\n1;\n2"), 3)

    def test_Add_with_custom_delimiter_multiple(self):
        self.assertEqual(TestStringCalculator.calculator.Add("// [*][ %]\n1 * 2 % 3"), 6)

    def test_Add_with_custom_delimiter_multiple_and_new_line_inbetween(self):
        self.assertEqual(TestStringCalculator.calculator.Add("// [*][ %]\n1 * 2 % \n3"), 6)

    def test_new_line_at_end(self):
        self.assertRaises(NewLineAtEndException, TestStringCalculator.calculator.Add, "1\n2,3\n")

    def test_negative_numbers(self):
        self.assertRaises(NegativeNumbersException, TestStringCalculator.calculator.Add, "1\n-22,-3")

    def test_negative_numbers_with_new_line_at_end(self):
        self.assertRaises(NewLineAtEndException, TestStringCalculator.calculator.Add, "1\n-22,-3\n")

    def test_Add_for_Value_error(self):
        self.assertRaises(ValueError, TestStringCalculator.calculator.Add, "1\n-a,-3")


if __name__ == '__main__':
    unittest.main()