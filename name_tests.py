import unittest
import name_app

class TestCase(unittest.TestCase):
    def test_name(self):
            self.assertEqual(name_app.fullName("Michael", "Boly"), "Michael Boly")
            self.assertEqual(name_app.fullName("Henry", "Bennett-Gains"), "Henry Bennett-Gains")
            self.assertEqual(name_app.fullName("Blank", ""), "First or last name empty")
            # self.assertEqual(name_app.fullName(" ", " "), "First or last name empty") #fails this on purpose


if __name__ == '__main__':
    unittest.main(verbosity=2)