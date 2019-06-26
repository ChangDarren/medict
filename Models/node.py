class Node:

    def __init__(self, parent, letter, fullName=None):
        self.parent = parent
        self.letter = letter
        self.fullName = fullName
        self.children = {} 
        
    def getLetter(self):
        return self.letter

    def hasFullName(self):
        return not self.fullName is None

    def getFullName(self):
        return self.fullName

    def setFullName(self, fullName):
        self.fullName = fullName

    def __str__(self):
        if self.hasFullName():
            return "[Letter: " + self.letter + ", Full drug name: " + \
                    self.fullName + "]"
        else:
            return "[Letter: " + self.letter + ", Full drug name: None]"
