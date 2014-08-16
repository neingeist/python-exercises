#!/usr/bin/python

def foo(n):
    """Returns n times foo, and a period.

    Just some random doctest test.

    Example:

    >>> foo(1)
    'foo.'

    >>> foo(5)
    'foo foo foo foo foo.'

    >>> foo(0)
    ''
    """
    if n >= 1:
        return "foo " * (n-1) + "foo."
    else:
        return ""

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
