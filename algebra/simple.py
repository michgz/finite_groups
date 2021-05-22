'''
Creation functions for the simple finite groups
'''

import numpy
from algebra.algebra import algebra

def z(n):
  '''
  Cyclic group of order n.
  '''

  if n <= 0:
    raise Exception("Need a positive order")
  c = numpy.empty((n, n), dtype=numpy.uint32)
  
  for i in range(n):
    x = i
    for j in range(n):
      c[i, j] = x
      x += 1
      if x >= n:
        x -= n

  return algebra(c)
