"""
Interface to the twitter API to retrieve raw data from twitter
"""

import tweepy
# this twitter_keys.py needs to contain variables holding keys and token values
# it is not checked in
from correlation.popularity.twitter_keys import *

class TwitterRetriever:
  def __init__(self, tag):
    """
    The twitter hash that we are following
    """
    self.tag = tag
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    self.api = tweepy.API(auth)

  def get_engagement_count(self):
    """
    return some number that indicates how much people are talking about this team.
    this number doesn't have to be anything specific but must change over time
    to reflect change in engagement
    for now using total mentions over each year
    """
    team = self.api.get_user("warriors")
    return team.followers_count

  def retrieve(self):
    """
    part of the Retriever interface
    """
    return [1, 2, 3, 4]

if __name__=='__main__':
  tw = TwitterRetriever("nba")
  print(tw.get_engagement_count(),"\n")
