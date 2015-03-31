import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_ecual(self):
        """ Test if the function works properly with exact number
            for the passengers """
        n = 50
        actual = a1.num_buses(n)
        expected = 1
        self.assertEqual(actual,expected)

    def test_zero(self):
        """ Test when the number of passangers is 0"""
        n = 0
        actual = a1.num_buses(n)
        expected = 0
        self.assertEqual(actual,expected)

    def test_below_fifty(self):
        ''' Test when the number of passangers is below 50'''
        n = 35
        actual = a1.num_buses(n)
        expected = 1
        self.assertEqual(actual, expected)

    def test_in_between(self):
        ''' Test when the number of passangers is not enough to
            fill exact number of busses'''
        n = 156
        actual = a1.num_buses(n)
        expected = 4
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
