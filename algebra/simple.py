'''
Creation functions for the simple finite groups
'''

import numpy
import math
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

def Chevalley(family, n, q):
  
  order = 0
  
  if family == 'A':
    # Classic Chevalley group
    x = 1
    for i in range(1, n+1):
      x *= (q**(i+1)-1)
    x *= q**(n*(n+1)//2)
    x /= math.gcd(n+1, q-1)
    name = f"A_{n}({q})"
    order = x
  elif family == 'B':
    # Classic Chevalley group
    if n < 1:
      raise Exception
    x = 1
    for i in range(1, n+1):
      x *= (q**(2*i)-1)
    x *= q**(n*n)
    x /= math.gcd(2, q-1)
    name = f"B_{n}({q})"
    order = x
  elif family == 'C':
    # Classic Chevalley group
    if n < 2:
      raise Exception
    x = 1
    for i in range(1, n+1):
      x *= (q**(2*i)-1)
    x *= q**(n*n)
    x /= math.gcd(2, q-1)
    name = f"C_{n}({q})"
    order = x
  elif family == 'D':
    # Classic Chevalley group
    if n < 2:
      raise Exception
    x = 1
    for i in range(1, n+1):
      x *= (q**(2*i)-1)
    x *= q**(n*(n-1))*(q**n - 1)
    x /= math.gcd(4, q**n - 1)
    name = f"D_{n}({q})"
    order = x
  elif family == 'E':
    # Exceptional Chevalley group
    x = 1
    if n == 6:
      for i in [2,5,6,8,9,12]:
        x *= (q**i-1)
      x *= q**36
      x /= math.gcd(3, q - 1)
    elif n == 7:
      for i in [2,6,8,10,12,14,18]:
        x *= (q**i-1)
      x *= q**63
      x /= math.gcd(2, q - 1)
    elif n == 8:
      for i in [2,8,12,14,18,20,24,30]:
        x *= (q**i-1)
      x *= q**120
    else:
      raise Exception("Impossible value for n")
    name = f"E_{n}({q})"
    order = x
  elif family == 'F':
    # Exceptional Chevalley group
    x = 1
    if n == 4:
      for i in [2,6,8,12]:
        x *= (q**i-1)
      x *= q**24
    else:
      raise Exception("Impossible value for n")
    name = f"F_{n}({q})"
    order = x
  elif family == 'G':
    # Exceptional Chevalley group
    x = 1
    if n == 2:
      for i in [2,6]:
        x *= (q**i-1)
      x *= q**6
    else:
      raise Exception("Impossible value for n")
    name = f"G_{n}({q})"
    order = x
    
  c = algebra(None)
  c.setName(name)
  c.setOrder(order)
  return c
  
    
def Steinberg(family, n, q):
  
  order = 0
  
  if family == '2A':
    # Classic Steinberg group
    if n <= 1:
      raise Exception
    x = 1
    for i in range(1, n+1):
      x *= (q**(i+1)-(-1)**(i+1))
    x *= q**(n*(n+1)//2)
    x /= math.gcd(n+1, q+1)
    name = f"^(2)A_{n}({q}^2)"
    order = x
  elif family == '2D':
    # Classic Steinberg group
    if n <= 3:
      raise Exception
    x = 1
    for i in range(1, n+1):
      x *= (q**(2*i) - 1)
    x *= (q**2 + 1)
    x *= q**(n*(n-1))
    x /= math.gcd(4, q**n + 1)
    name = f"^(2)D_{n}({q}^2)"
    order = x
  elif family == '2E':
    # Exceptional Steinberg group
    if n != 6:
      raise Exception
    x = 1
    for i in [2,5,6,8,9,12]:
      x *= (q**i - (-1)**i)
    x *= q**36
    x /= math.gcd(3, q+1)
    name = f"^(2)E_{n}({q}^2)"
    order = x
  elif family == '3E':
    # Exceptional Steinberg group
    if n != 4:
      raise Exception
    x = 1
    x *= q**12
    x *= (q**8 + q**4 + 1)
    x *= (q**6 - 1)
    x *= (q**2 - 1)
    name = f"^(3)E_{n}({q}^3)"
    order = x
  
  c = algebra(None)
  c.setName(name)
  c.setOrder(order)
  return c
  
  
def Suzuki(q):
  
  n = 0.5 * (math.log(q, 2) - 1)
  if abs(n - round(n)) > 1.E-7:    # This "epsilon" value is only suitable for quite small values of q. Revisit...
    raise Exception("q must be of form 2^(2n+1). q={0}, n={1}".format(q, n))
  
  name = f"^(2)B_2({q})"
  order = q**2 * (q**2 + 1) * (q - 1)
  c = algebra(None)
  c.setName(name)
  c.setOrder(order)
  return c
  
  
  
