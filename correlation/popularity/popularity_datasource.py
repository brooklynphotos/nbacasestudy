"""
Manages the data that shows popularity.
Any class that has a get_data method can be considered a popularity data source
"""

class TwitterPopularityDataSource:
  """
  Manages data from twitter and cleans and makes it conform to the data model
  """
  def __init__(self, retriever):
    self.retriever = retriever

  def get_data(self):
    """
    Gets all the data for the years available grouped by teams. 
    The data is in the form of a matrix:
    each row represents a year
    each column represents a team.
    It uses the data retriever to retrieve Twitter data and 
    """
    # TODO actually clean and rearrange data 
    return self.retriever.retrieve()