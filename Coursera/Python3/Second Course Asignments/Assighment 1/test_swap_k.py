import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_zero(self):
        '''Test with k = 0'''

        L = [4]
        k = 0
        actual = a1.swap_k(L, k)
        expected = [4]
        self.assertEqual(actual, expected)

    def test_double(self):
        ''' Test with doble values in the list'''

        L = [2, 5]
        k = 1
        actual = a1.swap_k(L, k)
        expected = [5, 2]
        self.assertEqual(actual, expected)

    def test_long(self):
        ''' Test with long list of values'''

        L = [1, 2, 3, 4, 5, 6]
        k = 2
        actual = a1.swap_k(L, k)
        expected = [5, 6, 3, 4, 1, 2]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
