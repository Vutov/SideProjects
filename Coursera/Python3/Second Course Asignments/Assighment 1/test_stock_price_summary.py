import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_random1(self):
        ''' Test the function with random numbers'''

        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(actual,expected)

    def test_random2(self):
        ''' Test the function with inverted random numbers'''

        actual = actual = a1.stock_price_summary([-0.01, -0.03, 0.02, 0.14, 0, 0, -0.10, 0.01])
        expected = (0.17, -0.14)
        self.assertEqual(actual,expected)

    def test_zero_sum(self):
        ''' The the function with zero sum numbers'''

        actual = a1.stock_price_summary([0, 0, 0])
        expected = (0, 0)
        self.assertEqual(actual,expected)

    def test_negative(self):
        ''' The the function with one negative number'''

        actual = a1.stock_price_summary([-2.4])
        expected = (0, -2.4)
        self.assertEqual(actual,expected)


if __name__ == '__main__':
    unittest.main(exit=False)
