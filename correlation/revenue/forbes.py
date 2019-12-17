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
from correlation.revenue import revenue_mock_service

class ForbesDataSource():
  def __init__(self,retriever, try_saving=True):
    """
      retriever: the functionality 
      self.retriever = retriever
      self.try_saving = try_saving
    """
    self.retriever = retriever
    self.try_saving = try_saving

  def load_historical(self):
    return self.load_data()

  def load_data(self):
    """
    Load data, if not saving, go get it, else if it doesn't already exist, download it, else just load whatever is saved
    """
    if not self.try_saving:
      return self.retrieve_data()

    # TODO needs to be in a config
    saved_file = "/Users/gzhong/tmp/nba_revenue.json"
    if Path(saved_file).is_file():
      with open(saved_file) as f:
        return json.load(f)
    else:
      # we don't have any cached data yet
      return self.save_data(saved_file)

  def retrieve_data(self):
    """
    Retrieves data and make it conform to the data model
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

  def save_data(self,target_file):
    """
    downloads data and saves it to the given file one year at a time
    """
    data = self.retrieve_data()      
    with open(target_file, 'w') as tf:
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
