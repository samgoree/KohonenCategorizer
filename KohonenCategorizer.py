# KohonenCategorizer
# Sam Goree
# Uses PyBrain's implementation of Kohonen Self-Organizing Maps to sort a given body of data into categories
# Usage: python KohonenCategorizer arg1 arg2
# arg1 is the file of data, separated onto separate lines, if there is no file, it will read from stdin
# arg2 is the number of categories, should be a perfect square (i.e. 2, 4, 9), default is 4
# arg3 is --words if you want to print out the relevant words as well

import pylab
from scipy import random
from pybrain.structure.modules import KohonenMap
import argparse
import sys
from math import sqrt
import numpy as np
from types import *
# constants for words option
NWORDS = 7 # max number of words to print for a cluster
THRESHOLD = 1 # number of standard deviations a word needs to be over the mean to qualify as significant


infile = sys.stdin
nnodes = 2
categories = 4
# handle arguments
parser = argparse.ArgumentParser(description='Sort a body of data into categories')
parser.add_argument('infile', type=argparse.FileType('r'), help='the file of data, separated onto separate lines')
parser.add_argument('categories', type=int, help='the number of categories, should be a perfect square')
parser.add_argument('--words', '-w', '-words', dest='words', action='store_const', const=True, default=False, help='Prints the words associated with each category at the end of all of the categories')
args = parser.parse_args()

infile = args.infile
categories = args.categories
nnodes = sqrt(categories)
words = args.words

# process the data
data = []
for line in infile:
	data.append(line.split(','))

som = KohonenMap(len(data[1])-1, nnodes)

# train the network

for i in range(25000):
    # one forward and one backward (training) pass on a random line
    som.activate(data[random.randint(1, len(data))][1:])
    som.backward()

# run on the data

#if not words:
for point in data[1:]:
	#find the category for a point of data
	print(point[0] + ',' + str(som.activate(point[1:])))

	
if words:
	# allocate a list of frequencies per cluster for each word
	wordLists = [[] for i in range(len(data[1]))]
	# Loop through the words in each cluster
	for i in range(1,len(data)):
		for j in range(1,len(data[i])):
			# put all of the first word together in wordLists[0], all of the second word together in wordLists[1], etc.
			wordLists[j].append(float(data[i][j]))
	wordLists = np.array(wordLists)
	stddev = []
	mean = []
	# find the mean and standard deviation for each word
	for i in range(len(wordLists)):
		stddev.append(np.std(wordLists[i]))
		mean.append(np.mean(wordLists[i]))
	stddev = np.array(stddev)
	mean = np.array(mean)
	threshold = stddev * THRESHOLD + mean
	
	w = [] # words for each cluster
	n = 0 # count our way through w
	# Loop through the words in each cluster
	for i in range(len(som.neurons)):
		for j in range(len(som.neurons[i])):
			w.append([])
			#print("Cluster: " + str(i) + ", " + str(j))
			for k in range(len(som.neurons[i][j])):
				if som.neurons[i][j][k] > threshold[k] and som.neurons[i][j][k] > 0:
					# if the weight is high enough, then the word is significant. Print it out.
					w[n].append((data[0][k],som.neurons[i][j][k]))
			w[n] = sorted(w[n], key=lambda x: -x[1]) # sort according to the frequency, the second value in each element, highest to lowest
			n+=1
			
	for i in range(NWORDS):
		for j in range(n):
			#write the most frequent word for each cluster
			sys.stdout.write(str(w[j][i%len(w[j])][0]) + ',')
		sys.stdout.write('\n')
		

	
	
	
	
