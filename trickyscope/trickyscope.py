from __future__ import print_function

class TrickyScope:
    a = 1
    b = [a for i in range(1)]

# Does not work with Python 3:
print(type(TrickyScope.b))
assert TrickyScope.b == [1]
