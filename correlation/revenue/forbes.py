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

class ForbesDataSource():
  def __init__(self, retriever, saved_file):
    """
      retriever: the functionality
      self.retriever = retriever
      self.saved_file = optional file to save the data to, if not given, won't look and won't save
    """
    self.retriever = retriever
    self.saved_file = saved_file

  def load_historical(self):
    """
    Returns the conformed data
    It is a matrix of year for each row and team for each column
    Probably better with a pandas dataframe
    """
    def make_row(year_row):
      return [r['revenue'] for r in year_row['data']]
    return [make_row(x) for x in self.load_raw_data()]

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
    for x in range(0,10):
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
        logging.error("Can't make more requests?", ex)
        return -1
      except:
        logging.error("Some non-exception is raised", sys.exc_info()[0])
        return -1
