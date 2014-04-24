from contextlib import contextmanager
import os


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


with working_directory("/tmp"), just_a_test():
    # do something within data/stuff
    print os.getcwd()

# here I am back again in the original working directory
print os.getcwd()
