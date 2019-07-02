class Node:
    def __init__(self, parent, letter, drugId=None, fullName=None):
        self.parent = parent
        self.letter = letter
        self.drugId = drugId
        self.fullName = fullName
        self.children = {} 
        
    def getLetter(self):
        return self.letter

    def setID(self, drugId):
        self.drugId = drugId
    
    def getID(self):
        return self.drugId

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
