import sys

class WordCounter(object):
	def __init__(self, text):
		self._text = text.split()
		self._frequencies = _get_frequencies(self._text)

	def _get_frequencies(txt):
		freqs = {}
		existing = []
		txt.sort()
		c = 0
		current_word = ""
		for i in xrange(len(txt)):
			if current_word != txt[i]:
				_add_word(freqs, existing, c, current_word)
				c = 1
			else:
				c += 1
		_add_word(freqs, existing, c, current_word)
		return freqs

	def _add_word(freqs, existing, c, current_word):
		if c not in existing:
			freqs[c] = [current_word]
		else:
			freqs[c].append(current_word)

	def get_count(self):
		return len(self._text)

	def get_most_frequent(self, num=10):
		word_list = []
		count_list = self._frequencies.keys()
		count_list.sort(reverse=True)
		for n in count_list:
			word_list += self._frequencies[n]
			if len(word_list) >= num:
				return word[:num]
		return word[:num]

def main():


if __name__ == '__main__':
	main()
