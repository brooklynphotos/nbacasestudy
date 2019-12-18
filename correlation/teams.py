"""
Holds information about the teams of the NBA
"""
import pandas as pd

TEAM_DATA = pd.DataFrame.from_records([
  ('toronto-raptors','Raptors'),
  ('golden-state-warriors','warriors'),
  ('denver-nuggets','nuggets')
], columns=['forbes','twitter'])