from typing import NamedTuple
import sys

class InputFileReader():
    
    def __init__(self):
        self.inputFileName = sys.argv[1]

    def getInputLines(self):
        with open(self.inputFileName) as f:
            return f.readlines()

class PolicyConstraints(NamedTuple):
    lowPosition: int
    highPosition: int
    letter: str

class InputLineInfo(NamedTuple):
    policy: PolicyConstraints
    password: str

class PolicyValidator():
    def __init__(self, policyConstraints):
        self.exactNumberOfOccurences = 1        
        self.policyConstraints = policyConstraints

    def getCorrectIndex(self, constrainPosition):
        return constrainPosition - 1
    
    def isValid(self, password):
        lettersOnContrainedPositions = [password[self.getCorrectIndex(self.policyConstraints.lowPosition)], password[self.getCorrectIndex(self.policyConstraints.highPosition)]]
        validatedLetterCount = lettersOnContrainedPositions.count(self.policyConstraints.letter)
        return validatedLetterCount == self.exactNumberOfOccurences

def getValidatedPositions(positionSegment):
    return [int(x) for x in positionSegment.split('-')]

def getValidatedLetter(letterSegment):
    return letterSegment[0]

def parseLineToInputLineInfo(inputLine):
    positionSegment, letterSegment, passwordSegment = inputLine.split()
    lowPosition, highPosition = getValidatedPositions(positionSegment)
    letter = getValidatedLetter(letterSegment)
    return InputLineInfo(PolicyConstraints(lowPosition, highPosition, letter), passwordSegment)

def getInputLineInfos(inputLines):
    for line in inputLines:
        yield parseLineToInputLineInfo(line)

def solve(inputLineInfos):
    validPasswords = 0
    for inputLineInfo in inputLineInfos:
        validator = PolicyValidator(inputLineInfo.policy)
        if (validator.isValid(inputLineInfo.password)):
            validPasswords += 1
    return validPasswords

inputFileReader = InputFileReader()
print(solve(getInputLineInfos(inputFileReader.getInputLines())))




