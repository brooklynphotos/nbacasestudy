"""
Interface to the twitter API to retrieve raw data from twitter
"""

class TwitterRetriever:
  def __init__(self, tag):
    """
    The twitter hash that we are following
    """
    self.tag = tag

  def retrieve(self):
    return [1,2,3,4]
