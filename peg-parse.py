#!/usr/bin/python3
# https://fdik.org/pyPEG/

from __future__ import division, print_function
from pypeg2 import *

class Type(Keyword):
    grammar = Enum( K("int"), K("long") )
class Parameter:
    grammar = attr("typing", Type), name()
class Parameters(Namespace):
    grammar = optional(csl(Parameter))
class Instruction(str):
    grammar = word, ";"

block = "{", maybe_some(Instruction), "}"
class Function(List):
   grammar = attr("typing", Type), name(), \
             "(", attr("parms", Parameters), ")", block

f = parse("int f(int a, long b) { do_this; do_that; }", Function)
print(f.name)
print(f.typing)
print(f.parms["b"].typing)
print(f[0])
print(f[1])
