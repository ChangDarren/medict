import sys
import importlib

from Models.trie import Trie
from Models.Utility.levenshtein import getClosestNode
from Models.Utility.util import removeInsideBrackets, getInsideBrackets
from Parser.conceptParser import getDrugConcepts
from Parser.inputParser import readTextInput

def main():
    if len(sys.argv) != 3:
        print('Usage: main.py [inputFilePath] [outputFilePath]')
        return False
    
    inputFilePath = sys.argv[1]
    outputFilePath = sys.argv[2]
    capacity = 350 

    trie = Trie()
    concepts = getDrugConcepts()
    trie.parseConcepts(concepts)

    inputs = readTextInput(inputFilePath)
    with open(outputFilePath, 'w') as outFile:
        for word in inputs:
            answerNode = trie.matchWord(word)
            if not answerNode:
                possibleNodes = trie.getCloseWords(word, capacity)
                answerNode = getClosestNode(word, possibleNodes)
            
            # Account for the additional information in the parenthesis
            if not answerNode and '(' in word and ')' in word:
                alteredWord = removeInsideBrackets(word)
                answerNode = trie.matchWord(alteredWord)
                if not answerNode:
                    possibleNodes = trie.getCloseWords(alteredWord, capacity)
                    answerNode = getClosestNode(alteredWord, possibleNodes)

            # Account for the case where we will only take the drug name in '['
            if not answerNode and '[' in word and ']' in word:
                alteredWord = getInsideBrackets(word)
                answerNode = trie.matchWord(alteredWord)
                if not answerNode:
                    possibleNodes = trie.getCloseWords(alteredWord, capacity)
                    answerNode = getClosestNode(alteredWord, possibleNodes)
            
            if answerNode:
                outFile.write(word + ', \"' + answerNode.getFullName() + '\", ' + answerNode.getID() + '\n')
                outFile.flush()
            else:
                outFile.write(word + ',0,\n')
                outFile.flush()

if __name__ == '__main__':
    main()
