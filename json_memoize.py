from __future__ import division, print_function

from functools import update_wrapper, wraps
import json
import operator
import os


class HashableDict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))


def json_memoize(filename):
    """Return a decorator that memoizes function calls in a JSON file."""

    class JsonMemoize:

        def __init__(self, fn):
            self.fn = fn
            update_wrapper(self, fn)

            if not os.path.exists(filename):
                with open(filename, "w") as f:
                    json.dump({}, f)

        def __call__(self, *args, **kwargs):

            with open(filename, "r") as f:
                memo = json.load(f)
            json_key = repr((args, HashableDict(kwargs)))
            if json_key not in memo:
                memo[json_key] = self.fn(*args, **kwargs)
                with open(filename, "w") as f:
                    json.dump(memo, f)
            return memo[json_key]

    return JsonMemoize


def timed(f):
    """Return a timed version of function f.

    The returned function returns a tuple of (time, real return value)

    :param f: function to time
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        import time

        time_start = time.time()
        return_ = f(*args, **kwargs)
        time_end = time.time()
        time_delta = time_end - time_start
        return time_delta, return_

    return wrapper


@json_memoize('json_memoize_tmp.json')
def is_prime(n):
    """Really inefficiently check if n is a prime number."""
    if n == 0 or n == 1:
        return False

    for i in xrange(2, n):
        if n % i == 0:
            return False

    return True


@json_memoize('json_memoize_tmp2.json')
def multiply(*args):
    return reduce(operator.mul, args, 1)


@json_memoize('json_memoize_tmp3.json')
def some_with_kwargs(one, two, **kwargs):
    print([kwargs[k] for k in kwargs])
    return one + two + reduce(operator.add, [kwargs[k] for k in kwargs], 0)


assert (is_prime(0) is False)
assert (is_prime(1) is False)
assert (is_prime(2) is True)
assert (is_prime(2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10) is False)

is_prime_timed = timed(is_prime)
for c in range(1, 11):
    time, result = is_prime_timed(86028157)
    assert (result is True)
    print("Call {}: {:.2f}s".format(c, time))

assert(multiply(1, 2, 3, 4) == 24)
assert(multiply(1, 2, 3, 4, 5) == 120)

assert(some_with_kwargs(1, 2, three=3, four=4) == 10)
