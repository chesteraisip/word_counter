word_counter

Contains class WordCounter:

Description:
	WordCounter(txt): instantiate a WordCounter object using parameter txt.
		The constructor generates the resources required for its other methods
		The text passed is assumed to be minimal in punctuation, but will factor in letter case

		Constructor also calls an additional function _get_frequencies() in order to construct the full breakdown of word frequencies
		The resulting dict is of the following form:
		{1: ['words'], 2: ['words'], 3: ['words']}
		in which the key corresponds to the frequency of the words in the word list
		The dict is generated iteratively, in which the number of each word is counted individually
			Once we find the total number of occurences in a word (the case ignoring and then sorting of a temporary list eliminates the possibility of double-counting) it is added to the appropriate list based on the number of occurences found
			Since the list is sorted we can also expect all lists within the dict to be sorted as well
			Solution of this generation is O (n log n + n), for the initial sort, and then a singular traversal through the word list

	get_count(): return the number of words provided in constructor
		* due to nature of the string passed, we can just count the number of words directly

	get_most_frequent(n=10): returns a dict with n keys that map to the frequency of the contained words. n has a default value of 10

Usage:
	use the following command:
	python word_counter.py myfile.txt
		where myfile.txt is the file to be used at runtime

		The file will instantiate a WordCounter object using the text in myfile.txt, then return get_count() and get_most_frequent()

	The package also contains a few sample text files in the 'samples' folder for usage:
		'empty.txt' - is an empty text file
		'test.txt'	- contains a single word with less than 10 words, to demonstrate that the class doesn't error when passing a reasonably small phrase
		'long.txt' = a text file with a longer paragraph

Testing:
	use the following command:
	python word_counter_test.py

	The test suite contains 3 sample unit tests that confirm the results of get_count() and get_most_frequent() on the provided text files