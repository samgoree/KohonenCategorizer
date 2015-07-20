KohonenCategorizer

Takes a file containing numerical data and assigns a category (unsupervised) to each line.

Uses PyBrain's implementation of Kohonen Self-Organizing Maps to sort a given body of data into categories
Arguments:
argv[1] is the file of data, separated onto separate lines. The first line should be a list of words for each vertical column in the input. The first element of each row should be a label for that data point
argv[2] is the number of categories, should be a perfect square (i.e. 2, 4, 9), default is 4
argv[3] is --words if you want to print out the relevant words as well. The words to print are calculated by taking all of the words THRESHOLD (defined at the top of the file) standard deviations above the mean for that word to describe each cluster.

KohonenWordCategorizer

Similar to KohonenCategorizer, but is designed for clustering words rather than clustering files. Technically, it uses the same process as KohonenCategorizer, but the --words option prints out the highest-frequency words sorted into each cluster, rather than going through the somewhat complicated threshold process.

KohonenFeedback

Removes some of the versatility of KohonenWordCategorizer to allow for an interactive system that prints out the top words in each cluster and allows the user to add more words to the stop words list, presumably based on the output, and rerun it.
Arguments:
argv[1] is the spreadsheet for kohonen
argv[2] is the stop words list
argv[3] is --silent if you want to run it silently (no feedback, equivalent to KohonenWordsCategorizer on CATEGORIES (defined at the top of the file) categories with --words

KohonenOutSorter

Sorts files from a folder into separate folders based on stdin, which should be a list of file names followed by categories to be sorted into. Helpful for manually checking the results of KohonenCategorizer, since it actually puts files clustered together into the same file.
argv[1] is the location of the original files
argv[2] is the location where you want to create category folders
stdin should be the output of KohonenCategorizer - try piping them together!

SpreadsheetCreator

Creates a spreadsheet with words on each line and files in each column for use with Kohonen maps. The default output is compatable with KohonenWordCategorizer, but it is trivial to swap the X and Y axes of the table and use it with KohonenCateorizer as well. The spreadsheet will ignore words that do not have a high enough frequency, either by taking the top words (-t) or removing the words below a threshold (-b). To run without this functionality, put -b 0 as the first two arguments.
argv[1] is -t or -b for top or bottom method of removing infrequent words
argv[2] is a number to go with -t or -b (-t N takes the N most frequent words, -b N removes words that appear fewer than N times)
argv[3] is a total frequency file, the sum of all the other frequency files
argv[4] is the directory that contains all of the frequency files except for the total frequency file
