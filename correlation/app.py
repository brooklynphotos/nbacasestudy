"""
The core of the application.

Strategy:
* Load revenue for as far back as possible but capped at 10 years
* Load twitter follower count for that number of years
* perform correlation
"""

from correlation.revenue import forbes as revenu_loader
from correlation.popularity import twitter as popularity_loader
from correlation.stats import linear_tools

def run():
  revenue = revenu_loader.load_historical()
  popularity = popularity_loader.get_follower_stats()
  corr = linear_tools.calculate_correlation(revenue, popularity)
  print(corr, "\n")