import string
import collections

from node import Node

class Trie:
    def __init__(self):
        self.startingChildren = {}
        for letter in string.ascii_lowercase:
            rootNode = Node(None, letter)
            self.startingChildren[letter] = rootNode

        for num in string.digits:
            rootNode = Node(None, num)
            self.startingChildren[num] = rootNode

    def insertWord(self, newWord):
        """
            Inserts the new word into the trie. The path will be the
            sorted word order while the full name inserted is the given word.

            Example: 
            'This is a test' will run along the path of 
            t -> h -> i -> s -> t -> e -> s -> t -> i -> s -> a
            but the full word in the last t will still be 'This is a test'
        """

        # Generate the path
        pathWord = self.__getPathWord(newWord)

        if len(newWord) == 0 or self.matchWord(pathWord):
            return False 

        pCrawl = self.startingChildren[pathWord[0]]
        length = len(pathWord)
        for level in range(1, length):
            if pathWord[level] not in pCrawl.children:
                pCrawl.children[pathWord[level]] = Node(pCrawl, pathWord[level]) 
            pCrawl = pCrawl.children[pathWord[level]]

        pCrawl.setFullName(newWord)
        return True

    def __breadthFirstSearch(self, node):
        hasVisited = [node]
        queue =  collections.deque()
        queue.append(node)
        while len(queue) != 0:
            currNode = queue.popLeft()
            hasVisited.append(currNode)
            for child in list(currNode.children.values()):
                if child not in hasVisited:
                    queue.append(child)

        return hasVisited

    def getCloseWords(self, keyWord):
        """
            Returns the list of nodes that are possible.
            Assumes that the key word is not in trie
        """

        pathWord = self.__getPathWord(keyWord)
        possibleNodes = []

        pCrawl = self.startingChildren[pathWord[0]]
        length = len(pathWord)
        for level in range(1, length):
            if pathWord[level] not in pCrawl.children:
                possibleNodes = self.__breadthFirstSearch(pCrawl)
                break
            pCrawl = pCrawl.children[pathWord[level]]
        
        return [node for node in possibleNodes if node.hasFullName()]


    def matchWord(self, keyWord):
        """
            Returns the node if the keyword matches else
            returns None
        """
        
        pathWord = self.__getPathWord(keyWord)

        pCrawl = self.startingChildren[pathWord[0]]
        length = len(pathWord)
        for level in range(1, length):
            if pathWord[level] not in pCrawl.children:
                return None
            pCrawl = pCrawl.children[pathWord[level]]

        if pCrawl is None or not pCrawl.hasFullName():
            return None

        return pCrawl

    def __getPathWord(self, newWord):
        """
            Utility function to get the path in the trie given a word.
            
            Path word should all be in lower case and should only alphanumeric
            characters.

            The decision to sort the words in reverse lexicographical order before
            generating the path is to allow for the alphabets to come before the 
            numbers which will help when narrowing down the possible words later.
        """
        pathWord = newWord.lower()
        pathWord = ''.join(ch for ch in pathWord if (ch.isalnum() or ch == ' ' or ch == '/'))
        splittedWords = pathWord.split(' ')
        splittedWords.sort(key=str.lower, reverse=True)
        newPathWord = ''.join(splittedWords)
        return newPathWord

