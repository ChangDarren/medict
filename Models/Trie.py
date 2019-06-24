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
        
        startingChildren[newWord[0]] = startingChildren[newWord[0]].addChild(newWord[1:], newWord)
        return startingChildren[newWord[0]]

    def matchWord(keyWord):
        index = 0
        nextNode = startingChildren[keyWord[index]]

        while nextNode is not None:
            nextNode = nextNode.nextChild(keyWord[index])
            index += 1
            
