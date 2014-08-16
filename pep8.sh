#!/bin/sh
find . -name "*.py" -not -name test_swig.py -not -name test_swig_opencv.py \
  | xargs pep8
