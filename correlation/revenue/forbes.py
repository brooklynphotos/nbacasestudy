"""
Retrieves revenue data using forbes.
The basic restend point is this: https://www.forbes.com/ajax/list/data?year=2019&uri=nba-valuations&type=organization
It is gotten from https://www.forbes.com/nba-valuations/list/
"""
import json
import sys
import time
import random
from pathlib import Path
import urllib.request
import logging
import pandas as pd

class ForbesDataSource():
  def __init__(self, retriever, saved_file, years_to_collect):
    """
      retriever: the functionality
      retriever = retriever
      saved_file = optional file to save the data to, if not given, won't look and won't save
      years_to_collect: number of years to collect data starting with this year
    """
    assert years_to_collect>0, "Years to collect must be positive"
    self.retriever = retriever
    self.saved_file = saved_file
    self.years_to_collect = years_to_collect

  def load_historical(self):
    """
    Returns the conformed data
    It is a matrix of year for each row and team for each column
    TODO Probably better with a pandas dataframe
    """
    def make_row(year_row):
      """
      converts a single entry from forbes into a map where key is either the name of the team with the revenue
      or the word 'year' with the year in it.
      This is an inner function as there is no reason anyone else should be using this
      """
      data_row = {'year': year_row['year']}
      for team_data in year_row['data']:
        data_row[team_data['uri']] = team_data['revenue']
      return data_row
    df = pd.DataFrame.from_records([make_row(x) for x in self.load_raw_data()])
    df.set_index('year')
    return df

  def load_raw_data(self):
    """
    Load raw data, if not saving, go get it, else if it doesn't already exist, download it, else just load whatever is saved
    The returned data is as described in <link to retrieve_raw_data>
    """
    if not self.saved_file:
      return self.retrieve_raw_data()

    if Path(self.saved_file).is_file():
      with open(self.saved_file) as f:
        return json.load(f)
    else:
      # we don't have any cached data yet
      return self.save_data()

  def retrieve_raw_data(self):
    """
    Retrieves data and make it conform to the data model
    It's a list of objects, each object contains a year and the data
    """
    # TODO maybe not hardcoded in
    start_year = 2019
    data = []
    for x in range(0,self.years_to_collect):
      year = start_year - x # going backwards in time
      year_data = self.retriever.retrieve(year)
      if year_data == -1:
        break
      data.append({
        'year': year,
        'data': year_data
      })
      ## let's wait a bit so we don't batter the service
      # TODO wait time can also go in a config
      time.sleep(random.randint(0,5))
    return data

  def save_data(self):
    """
    downloads data and saves it to the given file one year at a time
    """
    data = self.retrieve_raw_data()      
    with open(self.saved_file, 'w') as tf:
      json.dump(data, tf)
    return data

class ForbesDataRetriever:
  def retrieve(self, year):
    """
    Retrieves data for the given year
    """
    url = f"https://www.forbes.com/ajax/list/data?year={year}&uri=nba-valuations&type=organization"
    logging.info(f"downloading {url}")
    with urllib.request.urlopen(url) as u:
      try:
        return json.loads(u.read().decode())
      except Exception as ex:
        logging.error("Can't make more requests? %s", ex)
        return -1
      except:
        logging.error("Some non-exception is raised: %s", sys.exc_info()[0])
        return -1
