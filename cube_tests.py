import unittest
import cube_app

class TestCase(unittest.TestCase):
    def test_cube(self):
            self.assertEqual(cube_app.volume(2,2,2), 8)
            self.assertEqual(cube_app.volume(2.0,2.0,2.0), 8.0)
            self.assertEqual(cube_app.volume(-3,7,2), "Cannot have negative volume")
            # self.assertEqual(cube_app.volume("three",7,2), "Only accept numbers") #fails this on purpose


if __name__ == '__main__':
    unittest.main(verbosity=2)