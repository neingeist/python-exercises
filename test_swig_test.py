from __future__ import division, print_function
import test_swig

# FIXME
#print(test_swig.My_variable)
#assert(test_swig.My_variable == 3.0)

print(test_swig.fact(5))
assert(test_swig.fact(5) == 120)

print(test_swig.my_mod(23, 5))
assert(test_swig.my_mod(23, 5) == 3)

print(test_swig.get_time(), end="")
assert(len(test_swig.get_time()) > 20)
