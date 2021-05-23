'''
Create some pre-defined non-simple groups. Pre-defined simple groups can be
created using the `simple` module
'''

from algebra import algebra, simple
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
  elif n == 3:
    c = numpy.array([
      [0,1,2,3,4,5],
      [1,2,0,4,5,3],
      [2,0,1,5,3,4],
      [3,5,4,0,2,1],
      [4,3,5,1,0,2],
      [5,4,3,2,1,0]])
    return algebra.algebra(c)
  else:
    raise Exception("Dihedral groups so far only defined for n<4")



def Klein(n):
  if n != 4:
    raise Exception("Only Klein 4 exists!")
  return Dih(2)
