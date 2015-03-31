import dp_bugged
import unittest


class TestDoublePreceding(unittest.TestCase):

    def test_given(self):

        actual = dp_bugged.double_preceding([1, 2, 3])
        expected = [0, 2, 4]
        assertEqual (actual, expected)

    def test_empty(self):

        values = []
        actual = dp_bugged.double_preceding(values)
        expected = []
        assertEqual (actual, expected)

    def test_single(self):

        values = [0]
        actual = dp_bugged.double_preceding(values)
        expected = [0]
        assertEqual (actual, expected)

    def test_negative(self):

        values = [-1, -2, -5]
        actual = dp_bugged.double_preceding(values)
        expected = [0, -2, -4]
        assertEqual (actual, expected)

    def test_mixed(self):

        values = [5, -2, -5, 3, 1]
        actual = dp_bugged.double_preceding(values)
        expected = [0, 10, -4, -10, 6]
        assertEqual (actual, expected)

    def test_identical(self):
        """Test a list with multiple identical values""" 
        argument = [1, 1, 1]
        expected = [0, 2, 2]
        double_preceding(argument)
        self.assertEqual(expected, argument, "The list has multiple identical values.")

if __name__ == 'main':
    unittest.main(exit = False)
