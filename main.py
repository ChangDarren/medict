import sys
import importlib

from Models.trie import Trie
from Models.Utility.levenshtein import getClosestNode
from Parser.conceptParser import getDrugConcepts
from Parser.inputParser import readTextInput

def main():
    if len(sys.argv) != 3:
        print('Usage: main.py [inputFilePath] [outputFilePath]')
        return False
    
    inputFilePath = sys.argv[1]
    outputFilePath = sys.argv[2]
    capacity = 150 

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
            
            if answerNode:
                outFile.write(answerNode.getFullName() + ', ' + answerNode.getID() + '\n')
                outFile.flush()
            else:
                outFile.write('0\n')
                outFile.flush()

if __name__ == '__main__':
    main()
