# finite_groups
Python library for creating and modifying Cayley table representations of finite algebras

## Creating an algebra

An algebra is specified by its Cayley table. For example, to create a small group algebra:

```
from algebra import algebra
import numpy

a = algebra.algebra(numpy.array([[0,1,2],[2,0,1],[1,2,0]])
```

The Cayley table must be a square (n x n) array with non-negative integer elements. No other conditions are explicitly
imposed, however most useful algebra types (e.g. groups, semigroups or monoids) place additional requirements
on the Cayley table. In particular:

* Elements must usually lie in the range 0 .. (n-1). (This is essentially the "closure" property of the algebra).
* The identity element, if one exists, must be represented by 0. If there is no identity element then integer
0 has no special meaning.
* Other properties, such as associativity and commutativity, are determined from the Cayley table.

### Prerequisites

Uses numpy. Any version should do, development used version 1.19.4

