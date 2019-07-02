def readTextInput(inputFilePath):
    inputs = []

    print('Reading input file...')
    with open(inputFilePath) as inputFile:
        for line in inputFile:
            text = line.strip()
            inputs.append(text)
    print('Finished reading input file...')

    return inputs
