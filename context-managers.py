#!/usr/bin/env python2.7

# Examples from:
# https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for

from contextlib import contextmanager
from tempfile import mkdtemp

import os
import shutil

@contextmanager
def working_directory(path):
    current_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(current_dir)


@contextmanager
def just_a_test():
    try:
        print "just trying..."
        yield
    finally:
        print "finally!"




@contextmanager
def temporary_dir(*args, **kwds):
    name = mkdtemp(*args, **kwds)
    try:
        yield name
    finally:
        shutil.rmtree(name)



with working_directory("/tmp"), just_a_test():
    # do something within data/stuff
    print os.getcwd()

# here I am back again in the original working directory
print os.getcwd()


with temporary_dir() as tmpdir:
    print tmpdir
    tmpfile = tmpdir + "/foo"
    with open(tmpfile, "w") as f:
        f.write("foo")

# tmpdir is now gone
