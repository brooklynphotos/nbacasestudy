"""
Tests twitter module
"""

import unittest
from .twitter import TwitterEngagementDataSource
import correlation.popularity.mock_popularity_data as retriever

class TestTwitter(unittest.TestCase):
  """
  Tests twitter-related functionalities
  """

  def test_get_data(self):
    eng = TwitterEngagementDataSource(retriever)
    d = eng.get_data()
    self.assertEqual(1, len(d))

if __name__ == '__main__':
  unittest.main()