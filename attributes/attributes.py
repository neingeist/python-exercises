from __future__ import division, print_function

class SomeClass(object):
    def __setattr__(self, name, value):
        print("Setting {} to value {}".format(name, value))
        self.__dict__[name] = value

    def __getattr__(self, name):
        print("Getting {}".format(name))
        return None

o = SomeClass()
o.xxx = "yyy"
o.xxx = "zzz"
print(o.xxx)  # Note: __getattr__ does not get called here!
print(o.nope)
