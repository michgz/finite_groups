'''
Randomly generate various algebras
'''

from algebra.algebra import algebra
import random
import itertools
import numpy
import time

def randomGroup(n):
  '''Randomly generate a group of order n. It does that by putting in random
     values and then checking group axioms. This is about as inefficient as an
     algorithm can possibly get!!!
  '''
  
  count = 0    # We need some exit mechanism in case it's impossible
  
  while True:
    
    c = numpy.empty((n, n), dtype=numpy.uint32)
    
    for i, j in itertools.product(range(n), range(n)):
      
      if i == 0:
        c[i, j] = j
      elif j == 0:
        c[i, j] = i
      else:
        c[i, j] = random.randint(0, n-1)
    
    is_good = True
    
    # Check invertibility
    for i in range(n):
      
      has_inverse = False
      
      for j in range(n):
        
        if c[i, j] == 0 and c[j, i] == 0:
          has_inverse = True
          break
      
      if not has_inverse:
        is_good = False
        break
      
    # Check associativity
    if is_good:
      
      for i, j, k in itertools.product(range(n), range(n), range(n)):
        if c[c[i, j], k] != c[i, c[j, k]]:
          is_good = False
          break
    
    if is_good:
      return algebra(c)
    
    # If not good, go around and try another one...
    
    count += 1
    if count > 1000000:
      raise Exception("Didn't find a group of order {0}!".format(n))
  
  




