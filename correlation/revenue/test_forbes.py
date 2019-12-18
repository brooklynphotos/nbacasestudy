import unittest
import tempfile
import json

from correlation.revenue.forbes import ForbesDataSource
from correlation.revenue import revenue_mock_service as retriever

class TestForbes(unittest.TestCase):
  """
  Tests forbes-realted functionalities
  """

  def test_load_raw_data(self):
    """
    using the mock retriever and not saving
    """
    forbes = ForbesDataSource(retriever, None, 10)
    d = forbes.load_raw_data()
    self.assertEqual(d[0]['year'], 2019)
    self.assertEqual(2, len(d))

  def test_load_historical(self):
    """
    checks to see if the transformation to conformed data is correct
    """
    forbes = ForbesDataSource(retriever, None, 10)
    d = forbes.load_historical()
    self.assertEqual((2,31), d.shape) # 31 because year column plus the 30 teams
    self.assertEqual(287,d.at[0,'boston-celtics'])

  def test_save_data(self):
    """
    see if we are really saving data
    """
    fd, tmpfile = tempfile.mkstemp()
    forbes = ForbesDataSource(retriever, tmpfile, 2)
    forbes.save_data()
    with open(tmpfile) as tf:
      written_data = json.load(tf)
      self.assertEqual(2, len(written_data))

if __name__ == '__main__':
  unittest.main()