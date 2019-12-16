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

def load_historical():
  load_data()
  return [2,4,6,8]

def load_data():
  """
  Load data, if it doesn't already exist, download it, else just load whatever is saved
  """
  saved_file = "/Users/gzhong/tmp/nba_revenue.json"
  if Path(saved_file).is_file():
    with open(saved_file) as f:
      return json.load(f)
  else:
    # we don't have any cached data yet
    return save_data(saved_file)

def save_data(target_file):
  """
  downloads data and saves it to the given file one year at a time
  """
  start_year = 2019
  data = []
  for x in range(0,10):
    year = start_year - x # going backwards in time
    year_data = revenue_mock_service.get_data(year)
    # year_data = _get_forbes_data_(year)
    if year_data == -1:
      break
    data.append({
      'year': year,
      'data': year_data
    })
    ## let's wait a bit so we don't batter the service
    time.sleep(random.randint(0,5))
  return data
    
  with open(target_file, 'w') as tf:
    json.dump(data, tf)
  return data

def _get_forbes_data_(year):
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
