import unittest
import sys

sys.path.append('../Models/')

from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insertWord_multiple_word(self):
        self.trie.insertWord(0, "This is a test")
        self.trie.insertWord(1, "new test")
        self.assertEqual("This is a test", self.trie.matchWord("This is a test").getFullName())
        self.assertEqual("new test", self.trie.matchWord("new test").getFullName())

    def test_insertWord_with_number_and_non_alpha(self):
        self.trie.insertWord(0, "There is 2 nums. 1 ch@r")
        self.assertEqual("There is 2 nums. 1 ch@r",\
                self.trie.matchWord("There is 2 nums. 1 ch@r").getFullName())

    def test_insertWord_with_upper_case(self):
        self.trie.insertWord(0, "This Is In Title Case")
        self.assertEqual("This Is In Title Case",\
                self.trie.matchWord("this is in title case").getFullName())

    def test_insertWord_empty_word(self):
        self.assertFalse(self.trie.insertWord(0, ''))

    def test_matchWord_wrong_word(self):
        self.assertFalse(self.trie.matchWord("does not exist"))
    
    def test_matchWord_partial_word(self):
        self.trie.insertWord(0, "test another")
        self.assertFalse(self.trie.matchWord("test"))

    def test_matchWord_longer_word(self):
        self.trie.insertWord(0, "shorter word")
        self.assertFalse(self.trie.matchWord("shorter word longer word"))
    
    def test_getCloseWords_multiple_words(self):
        answer = ["drug 2mg/ml", "drug 4mg/ml"]

        self.trie.insertWord(0, "drug 2mg/ml")
        self.trie.insertWord(1, "drug 4mg/ml")
        self.trie.insertWord(2, "paracetemol 100mg") 
        closeNodes = self.trie.getCloseWords("drug")
        closeWords = [node.getFullName() for node in closeNodes]

        self.assertEqual(answer.sort(), closeWords.sort())


