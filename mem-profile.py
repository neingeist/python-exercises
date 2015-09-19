#!/usr/bin/python

from memory_profiler import profile
import numpy as np

# From
# http://stackoverflow.com/questions/27464039/why-the-performance-difference-between-numpy-zeros-and-numpy-zeros-like

N = (1000, 1000)
M = (slice(None, 500, None), slice(500, None, None))

@profile
def test1(N, M):
    print(N, M)
    x = np.zeros(N)
    y = np.empty(N)
    z = np.zeros_like(x)
    x[M] = 1
    y[M] = 1
    z[M] = 1
    return x,y,z

test1(N, M)
