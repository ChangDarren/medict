class Node:

    def __init__(self, parent, letter, fullName=None):
        this.parent = parent
        this.letter = letter
        this.fullName = fullName
        this.children = {} 
        
    def getLetter(self):
        return this.letter

    def hasFullName(self):
        return (this.fullName is None)

    def addChild(self, remainingWord, originalWord):
        newNode = None

        if len(remainingWord) == 1:
            newNode = Node(this, remainingWord, originalWord)
            this.children[remainingWord] = newNode
        else:
            newNode = Node(this, remainingWord[0])
            this.children[remaingWord[0]] = newNode.addChild(remainingWord[1:], originalWord)
            
        return this

    def nextChild(self, keyLetter):
        """
            Returns the next child in the trie if the next letter exists else
            returns None
        """
        if keyLetter in children:
            return children[keyLetter]

        return None

