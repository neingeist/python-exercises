#!/usr/bin/env python3
from functools import reduce

from sympy import latex, simplify
from sympy import pi, sin, cos, tan


def anki_latex(e):
    """Format SymPy expression as Anki LaTeX"""
    return "[$$]" + latex(e) + "[/$$]"


def as_csv(*values):
    return reduce(lambda a, b: a + ";" + b, values)


xs = map(simplify,
         [i * pi / 4 for i in range(-16, 16)])

for x in xs:
    for f in [sin, cos, tan]:
        front = "What is " + anki_latex(f(x, evaluate=False)) + "?"
        back = anki_latex(f(x))
        print(as_csv(front, back))