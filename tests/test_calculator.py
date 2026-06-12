import unittest

from calculator import add, calculate, divide, multiply, power, subtract


class CalculatorTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtracts_two_numbers(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiplies_two_numbers(self):
        self.assertEqual(multiply(6, 7), 42)

    def test_divides_two_numbers(self):
        self.assertEqual(divide(15, 3), 5)

    def test_division_by_zero_raises_error(self):
        with self.assertRaises(ZeroDivisionError):
            divide(8, 0)

    def test_calculates_power(self):
        self.assertEqual(power(2, 5), 32)

    def test_dispatches_operation_by_name(self):
        self.assertEqual(calculate("multiply", 4, 5), 20)

    def test_unknown_operation_raises_error(self):
        with self.assertRaises(ValueError):
            calculate("modulo", 10, 3)


if __name__ == "__main__":
    unittest.main()
