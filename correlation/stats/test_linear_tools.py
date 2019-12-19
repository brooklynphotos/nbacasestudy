"""
Testing the functions in the linear_tools wrapper
"""

from correlation.stats import linear_tools
import unittest

class TestLinearTools(unittest.TestCase):
    """
    Tests the non-private functions in the linear_tools module
    """

    def test_correlation_perfect(self):
        """
        When the two points are perfectly correlated
        """
        res = linear_tools.calculate_correlation([1,2,3],[10,20,30])
        self.assertEqual(res, 1.0)

    def test_correlation_negative(self):
        """
        When the two sets are perfectly negative-correlation
        """
        res = linear_tools.calculate_correlation([1,2,3],[30,20,10])
        self.assertEqual(res, -1.0)

if __name__ == '__main__':
    unittest.main()