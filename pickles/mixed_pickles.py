from __future__ import division, print_function

import cPickle as pickle


class SomeObject(object):
    def __eq__(self, other):
        """Default __eq__ would always return False."""
        return True

    pass

a = (1, 2)
b = "zwei"
c = [3, 4, 5, 6]
d = c
e = SomeObject()
f = e
before_pickle = [a, b, c, d, e, f]

after_pickle = pickle.loads(pickle.dumps(before_pickle))

# should get equal objects, but not the same:
for i in range(6):
    assert before_pickle[i] == after_pickle[i]
    assert id(before_pickle[i]) != id(after_pickle[i])

# same objects stay the same:
assert id(after_pickle[2]) == id(after_pickle[3])
assert id(after_pickle[4]) == id(after_pickle[5])
