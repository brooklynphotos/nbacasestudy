"""
Jus returns dummy data. Good for testing and API building
"""
import random

def retrieve(team, year):
  """
  Part of the Retriever interface
  returns random popularity for the last 10 years for 30 teams.
  """
  return random.randint(100,200)