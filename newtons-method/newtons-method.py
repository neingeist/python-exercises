#!/usr/bin/python
from __future__ import division, print_function
from math import pow
import random

epsilon = 1e-09

def derive(function, x):
    """Poor man's numerical derivation."""
    return (function(x+epsilon)-function(x-epsilon))/(2*epsilon)

def newton(function, x_0, max_i=50):
    """Find a real root of a function using Newton's method."""
    x = x_0
    for i in range(max_i):
        x = x - (function(x)/derive(function, x))
        print('f({}) = {}'.format(x, function(x)))
        if abs(function(x)) < epsilon:
            return x
            break
    else:
        return x


print(newton(lambda x: x**4 + 3*x - 1, x_0=100*random.random()))
#print(newton(lambda x: pow(x, 0.333), x_0=100*random.random()))
