#!/usr/bin/env python
from __future__ import division, print_function

import operator

seq1 = [1, 2, 3]
seq2 = ["eins", "zwei", "drei", "vier"]
map(lambda x: print("got:", x), seq1)
map(lambda x1, x2: print("got:", x1, x2), seq1, seq2)
map(lambda *x: print("got:", x), seq1, seq2)
print(map(None, seq1, seq2))

seq3 = [1, 2, 3, 4]
print(reduce(operator.mul, seq3))
