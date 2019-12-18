"""
Tests twitter module
"""

import unittest
from .twitter import TwitterEngagementDataSource
from correlation.popularity import mock_popularity_data as retriever

class TestTwitter(unittest.TestCase):
  """
  Tests twitter-related functionalities
  """

  def test_get_data(self):
    eng = TwitterEngagementDataSource(retriever, 10)
    d = eng.get_data()
    self.assertEqual(10, d.shape[0])

if __name__ == '__main__':
  unittest.main()