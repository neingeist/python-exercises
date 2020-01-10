from __future__ import division, print_function
import abc


class Base(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def x(self):
        return 'Should never get here'

    @abc.abstractmethod
    def process(self, data):
        """ Process data.
        Return bool

        """
        return

    def __del__(self):
        print("__del__")


class Implementation(Base):
    def __init__(self):
        self._x = True

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    def process(self, data):
        data += 1
        return True

# b = Base()
# print(b.x)

i = Implementation()
print(i.x)
a = 1
i.process(a)
print(a)

i2 = Implementation()
