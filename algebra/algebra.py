'''
The basic type
'''

import numpy

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
    
  def isGroup(self):
    n = self.order()
    if self.cayley.shape != (n, n):
      'Not a square matrix'
      return False
      
    # ... many other tests
    return True

