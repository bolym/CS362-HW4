import unittest
import fibonacci

class TestCase(unittest.TestCase):
    def test_fib(self):
            self.assertEqual(fibonacci.fib(0), 0)
            self.assertEqual(fibonacci.fib(1), 1)
            self.assertEqual(fibonacci.fib(3), 2)
            self.assertEqual(fibonacci.fib(7), 13)

    def test_factorial(self):
            self.assertEqual(fibonacci.factorial(0), 1)
            self.assertEqual(fibonacci.factorial(1), 1)
            self.assertEqual(fibonacci.factorial(3), 6)
            self.assertEqual(fibonacci.factorial(5), 120)

if __name__ == '__main__':
    unittest.main(verbosity=2)