# KohonenFeedback.py
# runs kohonen and then asks for new stop words
# argv[1] is the spreadsheet for kohonen
# argv[2] is the stop words list
# argv[3] is --silent if you want to run it silently
import sys
import KohonenWordCategorizer
from KohonenWordCategorizer import *
import re
import numpy as np

CATEGORIES = 16

# read the spreadsheet
data = readData(open(sys.argv[1]))

# read the stopwords
stopWords = []
for word in open(sys.argv[2]):
	stopWords.append(word.split('\n')[0])
	for i in range(len(data)):
		if data[i][0].lower() + '\n' == word.lower():
			data = np.delete(data, (i), axis=0)
			break

if len(sys.argv) > 3:
	silent = sys.argv[3] == '--silent'
else:
	silent = False
cont = True
while cont:
	# run Kohonen and print results
	categorize(CATEGORIES, data, True)
	if silent:
		cont = False
	# ask for new stop words, and add them to the stop words list
	else:
		rawWords = input("Add words to the stop words list, separated by commas:\n")
		# remove stop words from the spreadsheet
		for word in rawWords.split(','):
			for i in range(len(data)):
				if data[i][0].lower() == word.lower():
					data = np.delete(data, (i), axis=0)
					break
			stopWords.append(word)
		
		cont = True if input("Continue?\n").lower() == "yes" else False
if not silent:
	stopFile = open(sys.argv[2], 'w')
	for word in stopWords:
		stopFile.write(word + '\n')
