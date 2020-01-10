.PHONY: pep8
pep8:
	find . -name "*.py" -not -name test_swig.py -not -name test_swig_opencv.py \
	| xargs pep8
