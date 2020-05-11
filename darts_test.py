import unittest
from darts import score


# Tests adapted for the function score()

class darts_test(unittest.TestCase):
    def test_missed_target(self):
        self.assertEqual(score(-9, 9), 0)

    def test_on_the_outer_circle(self):
        self.assertEqual(score(0, 10), 1)

    def test_on_the_middle_circle(self):
        self.assertEqual(score(-5, 0), 5)

    def test_on_the_inner_circle(self):
        self.assertEqual(score(0, -1), 10)

    def test_exactly_on_centre(self):
        self.assertEqual(score(0, 0), 10)

    def test_near_the_centre(self):
        self.assertEqual(score(-0.1, -0.1), 10)


if __name__ == '__main__':
    unittest.main()