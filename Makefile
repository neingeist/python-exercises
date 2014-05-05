.PHONY: default
default: all test

.PHONY: all
all: _test_swig.so

.PHONY: test
test:
	python2.7 test_swig_test.py

_test_swig.so: test_swig.o
	ld -shared test_swig.o test_swig_wrap.o -o _test_swig.so

test_swig.o: test_swig_wrap.c
	gcc -fpic -c test_swig.c test_swig_wrap.c -I/usr/include/python2.7

test_swig_wrap.c: test_swig.i
	swig -python $<

.PHONY: clean
clean:
	rm -f *.o *.so test_swig_wrap.c *.pyc test_swig.py
