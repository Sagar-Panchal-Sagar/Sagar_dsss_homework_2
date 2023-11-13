import unittest
from math_quiz import Rand_int_generator, Rand_operator_generator, Operation_generator


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = Rand_int_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if random operators generated are within the specified operators
        op = ['+', '-', '*']
        for _ in range(1000):
            rand_op = Rand_operator_generator()
            self.assertIn(rand_op, valid_operators)    

    def test_function_C(self):
        # Test if our Output is according to the Test cases
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (3, 4, '*', '3 * 4', 12),
            (6, 6, '-', '6 - 6', 0),
            (8, 1, '+', '8 + 1', 9)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            self.assertEqual(Operation_generator(num1, num2, operator), (expected_problem, expected_answer))  

if __name__ == "__main__":
    unittest.main()
