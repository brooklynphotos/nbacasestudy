"""
Manages the data that shows engagement to the NBA teams.
Any class that has a get_data method can be considered an engagement data source
"""
import pandas as pd
from correlation.utils.dateutil import get_current_year
from correlation.teams import TEAM_DATA

class TwitterEngagementDataSource:
  """
  Manages data from twitter and cleans and makes it conform to the data model
  """
  def __init__(self, retriever, years):
    """
    retriever: an implementation that retrieves twitter engagement data
    years: number of years starting with current one that we want to get data for
    """
    self.retriever = retriever
    self.years = years

  def get_data(self):
    """
    Gets all the data for the years available grouped by teams. 
    The data is in the form of a matrix:
    each row represents a year
    each column represents a team.
    It uses the data retriever to retrieve Twitter data and 
    """
    # TODO actually clean and rearrange data 
    current_year = get_current_year()
    return pd.DataFrame.from_records([self._get_data_for_year_(year) for year in range(current_year, current_year - self.years, -1)])

  def _get_data_for_year_(self, year):
    """
    generate a dictionary where there is a year field and each other key is the team and the value is the engagement
    """
    data = {
      'year': year
    }
    for team_acct in list(TEAM_DATA['twitter']):
      engagement = self.retriever.retrieve(team_acct, year)
      data[team_acct] = engagement
    return data