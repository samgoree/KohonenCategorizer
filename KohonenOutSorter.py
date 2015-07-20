# Sort files from a folder, argv[1] into several folders at argv[2] based on stdin, which should be in the format of a KohonenCategorizer output file

import sys
import os
import shutil
import re

for line in sys.stdin:
	fileName = line.split(',')[0]
	#optional: move unprocessed files rather than frequencies
	fileName = re.sub('out', 'new', fileName)
	fileName = re.sub('\.csv', '', fileName)
	coords = line.split(',')[1]
	# process coordinates
	coords = re.sub('[\[\] ]', '', coords)
	coords = re.sub('\.', ',', coords)[:-2]
	if(not os.path.isdir(sys.argv[2] + '/' + coords)):
		os.mkdir(sys.argv[2] + '/' + coords);
	try:
		shutil.copy(sys.argv[1] + '/' + fileName, sys.argv[2] + '/' + coords + '/' + fileName)
	except IOError:
		print fileName
		continue
