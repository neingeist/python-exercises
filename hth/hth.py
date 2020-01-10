#!/usr/bin/python
from random import choice, seed

def ht():
  """Toss a coin and return H or T."""
  return choice(["H", "T"])

def numberoftosses(pattern):
  """Return the number of tosses until we hit the pattern."""
  s = len(pattern) * ht()
  while s[-len(pattern):] != pattern:
    s += ht()

  return(len(s))

def avgnumberoftosses(pattern, tries = 10000):
  """Return the average number of tosses until we hit the pattern."""
  n = 0.0
  for t in range(tries):
    n += numberoftosses(pattern)
  n /= tries

  return n

seed()
for pattern in "HTH", "HTT":
  print pattern, round(avgnumberoftosses(pattern))
