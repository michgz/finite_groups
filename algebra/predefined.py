'''
Create some pre-defined non-simple groups. Pre-defined simple groups can be
created using the `simple` module
'''

from algebra import algebra, simple, coxeter
import numpy

def Dih(n):
  'Dihedral group of order n'
  
  if n == 1:
    return simple.z(2)
  elif n == 2:
    c = numpy.array([
      [0,1,2,3],
      [1,0,3,2],
      [2,3,0,1],
      [3,2,1,0]])
    return algebra.algebra(c)
  elif n < 100:
    c = numpy.empty((2*n, 2*n), dtype=numpy.uint32)
    
    # This is based on the presentation a^n = b^2 = 0, a*b = b*a^-1
    
    # The first quadrant: a^i * a^j  == a^(i+j % n)
    for i in range(n):
      for j in range(n):
        c[i, j] = ((i+j) % n)
    
    # The second quadrant:  a^i * b * a^j == b * a^(-i+j % n)
    for i in range(n):
      for j in range(n):
        c[i, n+j] = n + ((-i+j) % n)

    # Third quadrant:   b * a^i * a^j  == b * a^(i+j % n)
    for i in range(n):
      for j in range(n):
        c[n+i, j] = n + ((i+j) %n)
    
    # Fourth quadrant:   b * a^i * b * a^j == a^(-i+j % n)
    for i in range(n):
      for j in range(n):
        c[n+i, n+j] = ((-i+j) % n)

    return algebra.algebra(c)
  else:
    raise Exception("Dihedral groups so far only defined for n<100")



def Sym(n):
  '''
  Symmetric group on n elements. It is a coxeter group, and we generate it from
  its coxeter matrix
  '''
  
  x = 2.*numpy.ones((n, n), dtype=numpy.uint32)
  # Most elements are 2's. Diagonal & second-diagonals are only exceptions

  # Diagonals are 1
  for i in range(n):
    x[i, i] = 1
  
  # Second-diagonals are 3
  for i in range(n-1):
    x[i, i+1] = 3
    x[i+1, i] = 3

  return coxeter.fromMatrix(x)



def Klein(n):
  if n != 4:
    raise Exception("Only Klein 4 exists!")
  return Dih(2)
