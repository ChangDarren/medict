def readTextInput(inputFilePath):
    inputs = []

    print('Reading input file...')
    with open(inputFilePath) as inputFile:
        for line in inputFile:
            text = line.strip()
            text = __preprocessInput(text)
            inputs.append(text)
    print('Finished reading input file...')

    return inputs

def __preprocessInput(item):

    shortFormMap = {
            'HCl' : 'hydrochloride', 
            'HBr': 'hydrogen bromide',
            'Br' : 'bromide', 
            'Inj' : 'injection',
            'mcg' : 'micrograms', 
            'NaCl' : 'sodium chloride solution', 
            }

    item = __completeBrackets(item)

    # Replace all the short forms that are not in another word
    for key in shortFormMap:
        loc = item.find(key)
        # Check that it is not within some word
        if loc > -1 and (len(item) == loc + len(key) or\
                not item[loc + len(key)].isalpha()):
            item = item.replace(key, shortFormMap[key])

    item = __removeCaps(item)
    return item

def __completeBrackets(item):
    opening = ['(', '[']
    closing = [')', ']']
    mapping = dict(zip(opening, closing))
    queue = []

    # Fill in the missing closing brackets
    location = 0
    for letter in item:
        if letter in opening:
            queue.append(mapping[letter])
        elif letter in closing:
            if letter != queue[-1]:
                item = item[:location] + queue.pop() + item[location::]
                location += 1
            else:
                queue.pop()
        location += 1

    while queue:
        item += queue.pop()

    return item

def __removeCaps(item):
    wordsToRemove = [
            'XR', 'SR', 'GNC', 'SUPRA', 'EC', 'CR', 'Free', 'free'
            ]

    words = item.split(' ')
    res = []
    for word in words:
        if word in wordsToRemove:
            continue
        res.append(word)

    return ' '.join(res)

