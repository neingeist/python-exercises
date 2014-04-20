#!/usr/bin/python2.7
from __future__ import division, print_function
from sympy import Symbol, diff, solve, lambdify
import matplotlib.pyplot as plt
import numpy as np

# Model parameters: We look for a line y = b1*x + b2.
b1 = Symbol('b1')
b2 = Symbol('b2')

# Data points
xn = [1, 2, 3, 4, 5, 7, 9]
yn = [6, 5, 7, 10, 11, 12, 14]

# S is the function to minimize:
#
# For each data point the vertical error/residual is x*b1 + b2 - y. We want to
# minimize the sum of the squared residuals (least squares).
S = sum((xn[i] * b1 + b2 - yn[i]) ** 2 for i in range(0, len(xn)))
print(S)

# Minimize S by setting its partial derivatives to zero.
d1 = diff(S, b1)
d2 = diff(S, b2)
solutions = solve([d1, d2], [b1, b2])

# Construct fitted line from the solutions
x = Symbol('x')
fitted_line = solutions[b1] * x + solutions[b2]
print(fitted_line)

# Construct something we can plot with matplotlib
fitted_line_func = lambdify(x, fitted_line, modules=['numpy'])
x_plot = np.linspace(min(xn), max(xn), 100)

# Plot data points and fitted line
plt.scatter(xn, yn, marker="+")
plt.plot(x_plot, fitted_line_func(x_plot), 'r')
plt.show()
