#!/usr/bin/python2.7
from __future__ import division, print_function
from sympy import Symbol, diff, solve, lambdify, simplify
import matplotlib.pyplot as plt
import numpy as np

# Model parameters: We look for a line y = b1*x + b2.
b1 = Symbol('b1')
b2 = Symbol('b2')

# Data points
data = [(1,14), (2, 13), (3, 12), (4, 10), (5,9), (7,8), (9,5)]

# S is the function to minimize:
#
# For each data point the vertical error/residual is x*b1 + b2 - y. We want to
# minimize the sum of the squared residuals (least squares).
S = sum((p[0] * b1 + b2 - p[1]) ** 2 for p in data)
S = simplify(S)
print("Function to minimize: S = {}".format(S))

# Minimize S by setting its partial derivatives to zero.
d1 = diff(S, b1)
d2 = diff(S, b2)
solutions = solve([d1, d2], [b1, b2])
print("S is minimal for b1 = {}, b2 = {}".format(solutions[b1], solutions[b2]))

# Construct fitted line from the solutions
x = Symbol('x')
fitted_line = solutions[b1] * x + solutions[b2]
print("Fitted line: y = {}".format(fitted_line))

# Construct something we can plot with matplotlib
fitted_line_func = lambdify(x, fitted_line, modules=['numpy'])
x_plot = np.linspace(min(p[0] for p in data),
                     max(p[0] for p in data), 100)

# Plot data points and fitted line
plt.scatter([p[0] for p in data], [p[1] for p in data], marker="+")
plt.plot(x_plot, fitted_line_func(x_plot), 'r')
plt.show()
