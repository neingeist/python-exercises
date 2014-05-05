%module test_swig_opencv
%{
#include "test_swig_opencv.hpp"
%}

%include "typemaps.i"
%include "okapi-typemaps.i"
%include "numpy.i"

// Parse the original header file
%include "test_swig_opencv.hpp"

