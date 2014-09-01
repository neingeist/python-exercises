from __future__ import division, print_function
from math import sin
from random import uniform, randint
from timeit import timeit

import pyximport
pyximport.install()

import cython_test


# as defined in cython_test.pyx, but in pure python:
def f(x):
    return sin(x**2)


# as defined in cython_test.pyx, but in pure python:
def integrate_f(a, b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx

if __name__ == "__main__":
    cython_test.say_hello_to("schweini")

    assert(cython_test.f(0.5) == f(0.5))
    assert(cython_test.f(1.7) == f(1.7))

    for i in range(10):
        a = uniform(-3.14, 3.14)
        b = uniform(-3.14, 3.14)
        N = randint(10, 1000)
        assert(integrate_f(a, b, N)
               == cython_test.integrate_f(a, b, N))

    print("Python:",
          timeit('integrate_f(0.0, 0.25, 1000)',
                 'from cython_test_test import integrate_f',
                 number=10000))
    print("Cython:",
          timeit('cython_test.integrate_f(0.0, 0.25, 1000)',
                 'import pyximport; pyximport.install(); import cython_test',
                 number=10000))
