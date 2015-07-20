KohonenCategorizer

Takes a file containing numerical data and assigns a category (unsupervised) to each line.

Uses PyBrain's implementation of Kohonen Self-Organizing Maps to sort a given body of data into categories
Arguments:
arg1 is the file of data, separated onto separate lines. The first line should be a list of words for each vertical column in the input. The first element of each row should be a label for that data point
arg2 is the number of categories, should be a perfect square (i.e. 2, 4, 9), default is 4
arg3 is --words if you want to print out the relevant words as well. The words to print are calculated by taking all of the words THRESHOLD (defined at the top of the file) standard deviations above the mean for that word to describe each cluster.

KohonenWordCategorizer

Similar to KohonenCategorizer, but is designed for clustering words rather than clustering files. Technically, it uses the same process as KohonenCategorizer, but the --words option prints out the highest-frequency words sorted into each cluster, rather than going through the somewhat complicated threshold process.

KohonenFeedback

Removes some of the versatility of KohonenWordCategorizer to allow for an interactive system that prints out the top words in each cluster and allows the user to add more words to the stop words list, presumably based on the output, and rerun it.
Arguments:
# argv[1] is the spreadsheet for kohonen
# argv[2] is the stop words list
# argv[3] is --silent if you want to run it silently (no feedback, equivalent to KohonenWordsCategorizer on CATEGORIES (defined at the top of the file) categories with --words