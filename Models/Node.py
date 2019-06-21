class Node:

    def __init__(self, parent, letter, fullName=None, orderedName=None):
        this.parent = parent
        this.letter = letter
        this.fullName = fullName
        this.orderedName = orderedName
        this.children = []
        
    def getLetter(self):
        return this.letter

    def hasFullName(self):
        return (this.fullName is None)

    def addChildren(self, nextLetter, nextFullName=None, nextOrderedName=None):
        child = Node(this, nextLetter, nextFullName, nextOrderedName)
        this.children.append(child)

    def nextChild(self, keyLetter):
        """
            Returns the next child in the trie if the next letter exists else
            returns None
        """
        for child in children:
            if child.getLetter() == keyLetter:
                return child

        return None

