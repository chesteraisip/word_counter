import unittest
from word_counter import WordCounter

class WordCounterTest(unittest.TestCase):

	def set_up(self, filename):
		self.f = open(filename)
		self.fr = self.f.read()
		self.wc = WordCounter(self.fr)

	def test_empty(self):
		self.set_up("empty.txt")
		self.assertEqual(self.wc.get_count(), 0)
		self.assertEqual(self.wc.get_most_frequent(), {})

	def test_base(self):
		self.set_up("test.txt")
		self.assertEqual(self.wc.get_count(), 9)
		self.assertEqual(len(self.wc.get_most_frequent().keys()), 9)

	def test_long(self):
		self.set_up("long.txt")
		self.assertEqual(self.wc.get_count(), 188)
		self.assertEqual(len(self.wc.get_most_frequent().keys()), 10)

	def tearDown(self):
		self.wc = None
		self.f.close()

if __name__ == '__main__':
	unittest.main()
