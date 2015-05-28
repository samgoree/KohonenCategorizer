KohonenCategorizer

Takes a file containing numerical and assigns a category (unsupervised) to each line.

Uses Kohonen.py from PyBrain (pybrain.org) and is based on the associated PyBrain example code.

Arguments:
 infile     the file of data, separated onto separate lines
 categories the number of categories, should be a perfect square (if not, will be rounded)
