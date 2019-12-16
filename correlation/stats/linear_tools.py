"""
Basic wrappers over existing stat libraries for easier use
"""

import numpy as np

def calculate_correlation(a, b):
  """
  given two vectors, find the corr coef for a vs b
  """
  return np.corrcoef(a, b)[0,1]