import sys
import unittest

sys.path.append('../Models')

from Utility.levenshtein import getEditDistance, getClosestWord

class TestLevenshtein(unittest.TestCase):
    # Example from CP3
    def test_getEditDistance_success(self):
        self.assertEqual(7, getEditDistance("agcatgc", "acaatcc"))
    
    def test_getEditDistance_one_empty(self):
        self.assertEqual(7, getEditDistance("agcatgc", ""))
    
    def test_getClosestWord_emptyBag(self):
        self.assertFalse(getClosestWord("agcatgc", []))

    def test_getClosestWord_success(self):
        self.assertEqual("agtatgc", getClosestWord("agcatgc", ["aattccg", "",\
                "cccccccccccccccccccccccgggggggggggggggggggaaaaaaaaaa", "agtatgc"]))
