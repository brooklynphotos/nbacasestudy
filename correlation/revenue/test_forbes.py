from correlation.revenue import forbes
import unittest

class TestForbes(unittest.TestCase):
    """
    Tests the non-private functions in the linear_tools module
    """

    def test_load_data(self):
      """
      not a true unit test as there is a side-effect. Best if we can have dependency injected
      """
      d = forbes.load_data()
      self.assertEqual(d[0].year, 2019)
      self.assertEqual(10, len(d))


if __name__ == '__main__':
    unittest.main()