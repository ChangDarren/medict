import Node
import string

class Trie:
    def __init__(self):
        startingChildren = {}
        for letter in string.ascii_lowercase:
            rootNode = Node(None, letter)
            startingChildren[letter] = rootNode
        
        for num in string.digits:
            rootNode = Node(None, num)
            startingChildren[letter] = rootNode
    
    def insertWord(newWord):
        if len(newWord) == 0:
            return None
        
        pCrawl = self.startingChildren[newWord[0]]
        length = len(newWord)
        for level in range(1, length):
            if newWord[level] not in pCrawl.children:
                pCrawl.children[newWord[level]] = Node(pCrawl, newWord[level]) 
            pCrawl = pCrawl[newWord[level]]

        pCrawl.setFullName(newWord)

    def matchWord(keyWord):
        index = 0
        nextNode = startingChildren[keyWord[index]]

        while nextNode is not None:
            nextNode = nextNode.nextChild(keyWord[index])
            index += 1
            
