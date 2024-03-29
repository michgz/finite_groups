'''
The basic type
'''

import numpy
import itertools

class algebra:
  cayley = None
  name = ""
  order_ = 0
  
  def __init__(self, c):
    self.cayley = c
    try:
      self.order_ = c.shape[0]
    except AttributeError:   # Need to accept c == None
      pass
  
  #def cayley(self):
  #  return self.cayley
    
  def order(self):
    try:
      return self.cayley.shape[0]
    except AttributeError:
      return self.order_
    
  def setName(self, name):
    self.name = name
    
  def setOrder(self, order):
    self.order_ = order
  
  '''
  Check if element 0 is an identity
  '''
  def _checkIdentity(self):
    n = self.cayley.shape[0]
    for i in range(n):
      if self.cayley[i, 0] != i:
        return False
      if self.cayley[0, i] != i:
        return False
    return True
  
  '''
  Check if each element has a unique two-sided inverse. Assume that existence
  of the identity has already been confirmed.
  '''
  def _checkInverses(self):
    n = self.cayley.shape[0]
    for i in range(n):
      num_l = 0
      num_r = 0
      for j in range(n):
        if self.cayley[i, j] == 0:
          num_l += 1
        if self.cayley[j, i] == 0:
          num_r += 1
      if num_l != 1 or num_r != 1:
        return False
      # Do we need to check that left-inverse==right-inverse? I'm
      # sure it's always true as long as we assume associativity (?)
    return True


  '''
  Check associativity
  '''
  def _checkAssociativity(self):
    n = self.cayley.shape[0]
    for i in range(n):
      for j in range(n):
        for k in range(n):
          i_jk = self.cayley[i, self.cayley[j, k]]
          ij_k = self.cayley[self.cayley[i, j], k]
          if i_jk != ij_k:
            return False
    return True



  
  def isGroup(self):
    n = self.order()
    if self.cayley.shape != (n, n):
      'Not a square matrix'
      return False
      
    # ... many other tests
    return True



class groupsOfOrder:
  # An iterator to return all groups of a particular order.
  #  Note: this returns all Cayley table representations that satisfy the group
  #       axioms. It does *not* remove duplicates under isomorphism!

  def __init__(self, n,
                  enforceAssociativity=True,
                  enforceIdentity=True,
                  enforceInvertibility=True,
                  enforceCommutativity=False):
    
    self.n = n
    self.enforceAssociativity   =   enforceAssociativity
    self.enforceIdentity        =   enforceIdentity
    self.enforceInvertibility   =   enforceInvertibility
    self.enforceCommutativity   =   enforceCommutativity
    self.underlyingIter = None
    
    
  def __iter__(self):
    
    self.underlyingIter = itertools.product(range(self.n), repeat=(self.n-1)**2)
    return self
    
  def __next__(self):
    
    while True:

    
      d = next(self.underlyingIter)
      is_good = True
      
      if is_good and self.enforceCommutativity:
        raise Exception("Abelian group iteration not yet supported")
      if is_good and not self.enforceIdentity:
        raise Exception("Semigroup iteration not yet supported")
      
      
      c = numpy.empty((self.n, self.n), dtype=numpy.uint32)
      
      k = 0
      
      for i, j in itertools.product(range(self.n), range(self.n)):
        if i == 0:
          c[i, j] = j
        elif j == 0:
          c[i, j] = i
        else:
          c[i, j] = d[k]
          k += 1
      
      if is_good and self.enforceInvertibility:
        for i in range(self.n):
          
          has_inverse = False
          
          for j in range(self.n):
            
            if c[i, j] == 0 and c[j, i] == 0:
              has_inverse = True
              break
          
          if not has_inverse:
            is_good = False
            break
      if is_good and self.enforceAssociativity:
      
        for i, j, k in itertools.product(range(self.n), range(self.n), range(self.n)):
          if c[c[i, j], k] != c[i, c[j, k]]:
            is_good = False
            break
    
      if is_good:
        return algebra(c)
        
      # Otherwise go round and try the next one....
      

def loopsOfOrder(n):
  return groupsOfOrder(n, enforceAssociativity=False)
  
def monoidsOfOrder(n):
  return groupsOfOrder(n, enforceInvertibility=False)

def semigroupsOfOrder(n):
  return groupsOfOrder(n, enforceIdentity=False, enforceInvertibility=False)

def abeliangroupsOfOrder(n):
  return groupsOfOrder(n, enforceCommutativity=True)
