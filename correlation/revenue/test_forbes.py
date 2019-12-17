from correlation.revenue.forbes import ForbesDataSource
from correlation.revenue import revenue_mock_service as retriever
import unittest

class TestForbes(unittest.TestCase):
  """
  Tests the non-private functions in the linear_tools module
  """

  def test_load_raw_data(self):
    """
    using the mock retriever and not saving
    """
    forbes = ForbesDataSource(retriever, None)
    d = forbes.load_raw_data()
    self.assertEqual(d[0]['year'], 2019)
    self.assertEqual(2, len(d))

  def test_load_historical(self):
    """
    checks to see if the transformation to conformed data is correct
    """
    forbes = ForbesDataSource(retriever, None)
    d = forbes.load_historical()
    self.assertEqual(2, len(d))
    self.assertEqual(30, len(d[0]))
    self.assertEqual(215,d[0][0])

if __name__ == '__main__':
    unittest.main()