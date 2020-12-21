import sys

class InputFileReader():
    
    def __init__(self):
        self.inputFileName = sys.argv[1]

    def getInputNumbers(self):
        with open(self.inputFileName) as f:
            for line in f.readlines():
                yield int(line)

def solve(wantedNumber, inputNumbers):
    complementNumbers = {}

    for inputNumber in inputNumbers:
        distanceFromWantedNumber = wantedNumber - inputNumber

        if inputNumber in complementNumbers:
            return distanceFromWantedNumber * inputNumber
        else:
            complementNumbers[distanceFromWantedNumber] = inputNumber    

wantedSumNumber = 2020
inputFileReader = InputFileReader()
print(solve(wantedSumNumber, inputFileReader.getInputNumbers()))



