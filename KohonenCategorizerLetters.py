# KohonenCategorizer
# Sam Goree
# Uses PyBrain's implementation of Kohonen Self-Organizing Maps to sort a given body of data into categories
# Usage: python KohonenCategorizer arg1 arg2
# arg1 is the file of data, separated onto separate lines, if there is no file, it will read from stdin
# arg2 is the number of categories, should be a perfect square (i.e. 2, 4, 9), default is 4

# version edited to deal with letter recognition data from  https://archive.ics.uci.edu/ml/datasets/Letter+Recognition

import pylab
from scipy import random
from pybrain.structure.modules import KohonenMap
import argparse
import sys
from math import sqrt


infile = sys.stdin
nnodes = 2
categories = 4
# handle arguments
parser = argparse.ArgumentParser(description='Sort a body of data into categories')
parser.add_argument('infile', type=argparse.FileType('r'), help='the file of data, separated onto separate lines')
parser.add_argument('categories', type=int, help='the number of categories, should be a perfect square')
args = parser.parse_args()

infile = args.infile
categories = args.categories
nnodes = sqrt(categories)

# process the data
data = []
for line in infile:
	data.append(line.split())

som = KohonenMap(len(data[0]), nnodes)

# train the network

for i in range(25000):
    # one forward and one backward (training) pass on a random line
    som.activate(data[random.randint(0, len(data))])
    som.backward()

# run on the data

categories = []
categoryCounts = [none] * categories
result = none

for point in data:
	#find the category for a point of data
	result = som.activate(point)
	categories.append(result)
	categoryCounts[result]+=1

print(categoryCounts)