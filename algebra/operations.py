'''
Operations on Cayley tables
'''

from algebra import algebra
import numpy
import itertools

def directProduct(a, b):

  'Calculates the direct product (cross product) of two algebras'

  n1 = a.cayley.shape[0]
  n2 = b.cayley.shape[0]
  
  c = numpy.empty((n1*n2, n1*n2), dtype=numpy.uint32)
  
  for v, u in itertools.product(range(n2), range(n1)):
    
    for x, w in itertools.product(range(n2), range(n1)):
      
      c[u + n1*v, w + n1*x] = a.cayley[u, w] + n1*b.cayley[v,x]
      
  return c



def isIsomorphic(a, b):
  
  '''Tests whether two groups are isomorphic to each other. TODO: must ensure that
      both inputs are in fact groups. This algorithm works by trying every
      possible permutation of numbers (1..(n-1)) which is clearly **very**
      inefficient.
      Note that 0 is always taken to be the identity, so don't need to permute
      that.
  '''

  n1 = a.cayley.shape[0]
  n2 = b.cayley.shape[0]
  if n1 != n2:
    return False
    
  for pp in itertools.permutations(range(1,n1)):
    # For each permutation...
    
    is_okay = True
    
    for i_a, j_a in itertools.product(range(n1), range(n1)):
      # Check each element of the arrays
      
      k_a = a.cayley[i_a, j_a]
      
      if i_a == 0:
        i_b = 0
      else:
        i_b = pp[i_a-1]
      
      if j_a == 0:
        j_b = 0
      else:
        j_b = pp[j_a-1]
      
      k_b = b.cayley[j_a, j_b]
      
      if k_a == 0:
        if k_b != 0:
          is_okay = False
      else:
        if k_b != pp[k_a-1]:
          is_okay = False
          
      if not is_okay:
        break
    
    if is_okay:
      # Found a good one!
      return True
      
  # If we get to here, no permutation worked
  return False
    
    




