import sys

def getEditDistance(firstWord, secondWord):
    firstLength = len(firstWord)
    secondLength = len(secondWord)

    if firstLength == 0:
        return secondLength
    
    if secondLength == 0:
        return firstLength

    matchCost = 2
    mismatchCost = -1

    dp = [[0 for x in range(firstLength + 1)] for y in range(secondLength + 1)]

    for i in range(firstLength + 1):
        dp[0][i] = -i

    for i in range(secondLength + 1):
        dp[i][0] = -i

    for i in range(1, secondLength + 1):
        for j in range(1, firstLength + 1):
            firstChar = firstWord[j - 1]
            secondChar = secondWord[i - 1]
            actualCost = matchCost
            if firstChar != secondChar:
                actualCost = mismatchCost
            opt1 = dp[i-1][j-1] + actualCost
            opt2 = dp[i-1][j] + mismatchCost
            opt3 = dp[i][j-1] + mismatchCost
            dp[i][j] = max(opt1, opt2, opt3)
    
    # __printDp(dp)

    return dp[secondLength][firstLength]

def __printDp(dp):
    for row in dp:
        for val in row:
            val = '{0: >4}'.format(str(val))
            sys.stdout.write(val)
        print('')

# TODO: Decide what to do if there are words with the same distance
def getClosestWord(keyWord, bagOfWords):
    # The max distance that we will tolerate
    THRESHOLD = -9999

    if len(bagOfWords) == 0:
        return None
    
    best = THRESHOLD 
    bestWord = None
    for word in bagOfWords:
        dist = getEditDistance(keyWord, word)
        if dist > best:
            best = dist
            bestWord = word
            
    return bestWord

