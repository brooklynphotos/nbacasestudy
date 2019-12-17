"""
Interface to the twitter API to retrieve raw data from twitter
"""

import tweepy
# this twitter_keys.py needs to contain variables holding keys and token values
# it is not checked in
from correlation.popularity.twitter_keys import *

class TwitterRetriever:
  def __init__(self):
    """
    The twitter hash that we are following
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    self.api = tweepy.API(auth)

  def get_engagement_count(self, team_name: str, year: int):
    """
    return some number that indicates how much people are talking about this team.
    this number doesn't have to be anything specific but must change over time
    to reflect change in engagement
    for now using total mentions over each year
    team_name: twitter name for this team
    year: the year you want the engagement
    """

    # TODO currently this doesn't work as no way has been found to retrieve historical data for unowned account
    team = self.api.get_user(team_name)
    return team.followers_count

  def retrieve(self):
    """
    part of the Retriever interface
    """
    return [1, 2, 3, 4]

if __name__=='__main__':
  tw = TwitterRetriever()
  print(tw.get_engagement_count("warriors", 2019), "\n")
