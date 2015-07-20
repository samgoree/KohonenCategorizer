# KohonenWordCategorizer
# Sam Goree
# Uses PyBrain's implementation of Kohonen Self-Organizing Maps to sort a given body of data into categories
# This version reverses it: it clusters words based on their occurrence in files.
# Usage: python KohonenCategorizer arg1 arg2
# arg1 is the file of data, separated onto separate lines, if there is no file, it will read from stdin
# arg2 is the number of categories, should be a perfect square (i.e. 2, 4, 9), default is 4
# arg3 is --words if you want to print out the top words in each cluster rather than each word associated with a cluster

import pylab
from scipy import random
from pybrain.structure.modules import KohonenMap
import argparse
import sys
from math import sqrt
import numpy as np
from types import *


infile = sys.stdin
nnodes = 2
categories = 4
NWORDS = 7 # number of words to print out per category for the -words option

# reads and returns data from a file
# infile is the file of input
def readData(infile):

	# process the data
	tempData = []
	for line in infile:
		tempData.append(line.split(','))

	# swap the axes
	data = [[] for i in range(len(tempData[0]))]
	for i in range(len(tempData)):
		for j in range(len(tempData[i])):
			data[j].append(tempData[i][j])
			
	data = np.array(data)
	return data


# runs the kohonen map and prints either raw results or words for Koushik's GA (based on the value of words)
# categories is the number of nodes in the kohonen map
def categorize(categories, data, words):
	nnodes = sqrt(categories)
	# make a kohonen map
	som = KohonenMap(len(data[1])-1, nnodes)
	
	# train the network

	for i in range(25000):
		# one forward and one backward (training) pass on a random line
		som.activate(data[random.randint(1, len(data)-1)][1:])
		som.backward()

	# run on the data

	if not words:
		for point in data[1:-1]:
			#find the category for a point of data
			print(point[0] + ',' + str(som.activate(point[1:])))


	#make wordlist output similar to ICA for use in GAs
	if words:
		results = [[] for i in range(categories)]
		for point in data[1:-1]:
			# find the cluster for this word and add in the word's data
			result = som.activate(point[1:])
			results[int(result[0]*nnodes + result[1])].append(point)
		# print out the clusters
		for i in range(NWORDS):
		# TODO: This is super inefficient
			for cluster in results:
				if len(cluster) == 0:
					sys.stdout.write('EMPTY')
					continue
				for j in range(len(cluster)):
					for k in range(1, len(cluster[j])):
						cluster[j][k] = float(cluster[j][k])
				tempCluster = sorted(cluster, key=lambda point: -sum(point[1:]))
				sys.stdout.write(str(tempCluster[i%len(cluster)][0]) + ',')
			sys.stdout.write('\n')

if __name__ == "__main__":
	# handle arguments
	parser = argparse.ArgumentParser(description='Sort a body of data into categories')
	parser.add_argument('infile', type=argparse.FileType('r'), help='the file of data, separated onto separate lines')
	parser.add_argument('categories', type=int, help='the number of categories, should be a perfect square')
	parser.add_argument('--words', '-w', '-words', dest='words', action='store_const', const=True, default=False, help='Prints the words associated with each category at the end of all of the categories')
	args = parser.parse_args()

	infile = args.infile
	categories = args.categories
	
	words = args.words
	
	data = readData(infile)
	categorize(categories, data, words)
