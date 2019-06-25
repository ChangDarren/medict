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

    def setFullName(self, fullName):
        this.fullName = fullName
