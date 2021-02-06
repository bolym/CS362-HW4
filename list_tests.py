import unittest
import list_app

class TestCase(unittest.TestCase):
    def test_list(self):
            self.assertEqual(list_app.average([1,2,3]), 2)
            self.assertEqual(list_app.average([]), "No average for empty list")
            self.assertEqual(list_app.average([-1,-2,-3]), -2)
            # self.assertEqual(list_app.average(["one",-2,-3]), "Only accepts numbers")


if __name__ == '__main__':
    unittest.main(verbosity=2)