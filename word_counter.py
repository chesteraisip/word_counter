import sys

class WordCounter(object):
	def __init__(self, text):
		self._text = text.split()
		self._get_frequencies()

	def _get_frequencies(self):
		self._frequencies = {}
		txt = self._text
		txt.sort()
		c = 0
		current_word = txt[0]
		for word in txt:
			if current_word != word:
				existing = self._add_word(c, current_word)
				current_word = word
				c = 1
			else:
				c += 1
		self._add_word(c, current_word)

	def _add_word(self, c, current_word):
		if c in self._frequencies.keys():
			self._frequencies[c].append(current_word)
		else:
			self._frequencies[c] = [current_word]

	def get_count(self):
		return len(self._text)

	def get_most_frequent(self, max_words=10):
		word_list = []
		count_list = [*self._frequencies]
		count_list.sort(reverse=True)
		for n in count_list:
			word_list += [(w, n) for w in self._frequencies[n]]
			if len(word_list) >= max_words:
				return word_list[:max_words]
		return word_list[:max_words]

def main(*args):
	f = open(sys.argv[1])
	fr = f.read()
	wc = WordCounter(fr)
	f.close()
	print(wc.get_count())
	print(wc.get_most_frequent())


if __name__ == '__main__':
	main()
