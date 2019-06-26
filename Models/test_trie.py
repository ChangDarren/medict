import unittest

from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insertWord_multiple_word(self):
        self.trie.insertWord("This is a test")
        self.trie.insertWord("new test")
        self.assertEqual("This is a test", self.trie.matchWord("This is a test"))
        self.assertEqual("new test", self.trie.matchWord("new test"))

    def test_insertWord_with_number_and_non_alpha(self):
        self.trie.insertWord("There is 2 nums. 1 ch@r")
        self.assertEqual("There is 2 nums. 1 ch@r",\
                self.trie.matchWord("There is 2 nums. 1 ch@r"))

    def test_insertWord_with_upper_case(self):
        self.trie.insertWord("This Is In Title Case")
        self.assertEqual("This Is In Title Case",\
                self.trie.matchWord("this is in title case"))

    def test_insertWord_empty_word(self):
        self.assertFalse(self.trie.insertWord(''))

    def test_matchWord_wrong_word(self):
        self.assertFalse(self.trie.matchWord("does not exist"))
    
    def test_matchWord_partial_word(self):
        self.trie.insertWord("test another")
        self.assertFalse(self.trie.matchWord("test"))

    def test_matchWord_longer_word(self):
        self.trie.insertWord("shorter word")
        self.assertFalse(self.trie.matchWord("shorter word longer word"))
