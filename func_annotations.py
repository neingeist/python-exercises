#!/usr/bin/env python3
# Play around with function annotations to implement a crude type checker.

import inspect


def typechecked(func):
    wrapped_func = func

    def typecheck(*args, **kvargs):
        parameters = inspect.signature(wrapped_func).parameters
        wants = [(par, parameters[par].annotation) for par in parameters]
        for want, arg in zip(wants, args):
            name, class_ = want
            if not isinstance(arg, class_):
                raise TypeError("arg {} is not "
                                "an instance of {}".format(name, class_))

        return_ = wrapped_func(*args, **kvargs)
        class_ = wrapped_func.__annotations__["return"]
        if not isinstance(return_, class_):
            raise TypeError("return value is not "
                            "an instance of {}".format(class_))
        return return_

    typecheck.__doc__ = wrapped_func.__doc__
    return typecheck


@typechecked
def greet(name: str, age: int, fnord: str=None) -> str:
    """Greet someone.

    >>> greet("Mike", 12)
    'Hello Mike, you are 12 years old'
    >>> greet("Florian", "eins")
    Traceback (most recent call last):
      File "func_annotations.py", line 14, in typecheck
        "is not an instance of {}".format(name, class_))
    TypeError: arg age is not an instance of <class 'int'>
    """
    return 'Hello {0}, you are {1} years old'.format(name, age)


@typechecked
def test(foo: int) -> str:
    """ Just a test.

    >>> test(1)
    Traceback (most recent call last):
      File "func_annotations.py", line 21, in typecheck
        "is not an instance of {}".format(class_))
    TypeError: return value is not an instance of <class 'str'>
    """
    return 1

import doctest
doctest.testmod()
