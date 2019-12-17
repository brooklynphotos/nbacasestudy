"""
The core of the application.

Strategy:
* Load revenue for as far back as possible but capped at 10 years
* Load twitter follower count for that number of years
* perform correlation

We are using forbes for the revenue data and the twitter data source to measure popularity
"""

from correlation.revenue.forbes import ForbesDataSource,ForbesDataRetriever
from correlation.popularity.popularity_datasource import TwitterPopularityDataSource
from correlation.popularity.twitter import TwitterRetriever
from correlation.stats import linear_tools

def run():
  popularity_loader = TwitterPopularityDataSource(TwitterRetriever('nba'))
  revenu_loader = ForbesDataSource(ForbesDataRetriever(),"/Users/gzhong/tmp/forbes_nba.json")
  revenue = revenu_loader.load_historical()
  popularity = popularity_loader.get_data()
  corr = linear_tools.calculate_correlation(revenue, popularity)
  print(corr, "\n")