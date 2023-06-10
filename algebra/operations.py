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
      
  return algebra.algebra(c)



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
  
  
  # If cayley tables are different shapes, we can't possibly have isomorphism
  if n1 != n2:
    return False
  
  
  # Calculate the order of each element, to reduce the number of permutations to
  # check. Does this assume group axioms hold ????   If so, might need to check
  # those first.
  
  orders_1 = numpy.empty((1, n1), dtype=numpy.uint32)
  orders_2 = numpy.empty((1, n2), dtype=numpy.uint32)
  
  for i in range(n1):
    x = 0
    v = 0
    while True:
      v = a.cayley[i, v]
      if v == 0:
        orders_1[0, i] = x
        break
      x += 1 
      if x > n1:
        # This should be impossible! Maybe we don't have a group?
        raise Exception
  for i in range(n2):
    x = 0
    v = 0
    while True:
      v = b.cayley[i, v]
      if v == 0:
        orders_2[0, i] = x
        break
      x += 1 
      if x > n2:
        # This should be impossible! Maybe we don't have a group?
        raise Exception
  
  if orders_1[0, 0] != 0 or orders_2[0, 0] != 0:
    # The identity must have order 0. Otherwise something is wrong....
    raise Exception
  
  for pp in itertools.permutations(range(1,n1)):
    # For each permutation...
    
    is_okay = True
    
    
    # Check the correspondence of orders
    for i_a in range(n1):
      if i_a == 0:
        i_b = 0
      else:
        i_b = pp[i_a-1]
      if orders_1[0, i_a] != orders_2[0, i_b]:
        is_okay = False
        break

    if not is_okay:
      continue
    
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
      
      k_b = b.cayley[i_b, j_b]
      
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
    
    


def findSubgroup(a, b):
  # Find a permutation of elements under which "a" is a subgroup of "b". Only one
  # such permutation is returned even if multiple exist.
  # If there is no such permutation then None is returned.
  
  # TODO: should confirm that "a" is in fact a group
  
  n1 = a.cayley.shape[0]
  n2 = b.cayley.shape[1]
  
  if not n2 >= n1:
    return None
  
  for pp in itertools.combinations(range(1, n2), n1-1):
    
    is_good = True
    
    for i_a, j_a in itertools.product(range(1, n1), repeat=2):
      
      i_b = pp[i_a-1]
      j_b = pp[j_a-1]
      
      k_a = a.cayley[i_a, j_a]
      k_b = b.cayley[i_b, j_b]
      
      if k_a == 0:
        if k_b != 0:
          is_good = False
      elif k_b != pp[k_a-1]:
        is_good = False
        
      if not is_good:
        break
    
    if is_good:
      return pp
      
    # Otherwise, try another
  
  
  return None
  


class subgroupOf:
  # An iterator returning all permutations of elements under which b is a subgroup
  # of a.
  # In the general case, the iterator will either return 1 value (it is a subgroup) or
  # no values (it is not a subgroup). Sometimes a subgroup will have multiple ways of
  # being a subgroup, in which multiple values will be returned.
  
  def __init__(self, b, a):
    
    self.underlyingIter = None
    self.b = b.cayley
    self.a = a.cayley
    self.n1 = b.cayley.shape[0]
    self.n2 = a.cayley.shape[0]
    
    
  def __iter__(self):
    
    self.underlyingIter = itertools.combinations(range(1, self.n2), self.n1-1)
    return self
  
  def __next__(self):
    
    while True:
    
      pp = next(self.underlyingIter)
      is_good = True

      for i_b, j_b in itertools.product(range(1, self.n1), repeat=2):
        
        i_a = pp[i_b-1]
        j_a = pp[j_b-1]
        
        k_b = self.b[i_b, j_b]
        k_a = self.a[i_a, j_a]
        
        if k_b == 0:
          if k_a != 0:
            is_good = False
        elif k_a != pp[k_b-1]:
          is_good = False
          
        if not is_good:
          break
      
      if is_good:
        return (0,) + pp   # extend by the identity
      
      # Otherwise go round and try the next one....



def isSubgroup(b, a):
  # Is "b" a subgroup of "a"?
  
  try:
    next(iter(subgroupOf(b, a)))
    return True
  except StopIteration:
    return False



def isNormalSubgroup(b, a):
  
  n1 = b.cayley.shape[0]
  n2 = a.cayley.shape[1]
  
  for pp in subgroupOf(b, a):
    
    if len(pp) != n1:
      raise Exception("Unexpected length!")
    
    
    # Test for normality, using the definition
    
    is_normal = True
    
    for g in range(n2):
      
      g_inv = -1
      for j in range(n2):
        if a.cayley[g, j] == 0:
          g_inv = j
          break
        
      if g_inv < 0:
        raise Exception("Not a group -- inverse not found!")
        
      for n in range(n1):
        
        # Calculate gng`.
        
        gn = a.cayley[g, pp[n]]
        gng_inv = a.cayley[gn, g_inv]
        
        if gng_inv not in pp:
          is_normal = False
          break
    if is_normal:
      return True
      
  return False

