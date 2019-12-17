from correlation.revenue.forbes import ForbesDataSource
from correlation.revenue import revenue_mock_service as retriever
import unittest

class TestForbes(unittest.TestCase):
    """
    Tests the non-private functions in the linear_tools module
    """

    def test_load_data(self):
      """
      using the mock retriever and not saving
      """
      forbes = ForbesDataSource(retriever, False)
      d = forbes.load_data()
      self.assertEqual(d[0]['year'], 2019)
      self.assertEqual(2, len(d))


if __name__ == '__main__':
    unittest.main()