#!/usr/bin/env python2.7
from sympy import Symbol, latex, simplify
from sympy import pi, sin, cos, tan

def ankilatex(e):
  """ Format sympy expression as Anki LaTeX"""
  return "[$$]" + latex(e) + "[/$$]"

for i in range(-16, 16):
  x = simplify(i*pi/4)

  for f in [sin, cos, tan]:
    print "What is " + ankilatex(f(x, evaluate=False)) + "?",
    print ";",
    print ankilatex(f(x)),
    print
