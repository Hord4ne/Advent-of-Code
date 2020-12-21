from typing import NamedTuple
import sys


class InputFileReader():
    
    def __init__(self):
        self.inputFileName = sys.argv[1]

    def getInputLines(self):
        with open(self.inputFileName) as f:
            return f.readlines()

class PolicyConstraints(NamedTuple):
    lowestValidCount: int
    highestValidCount: int
    letter: str

class InputLineInfo(NamedTuple):
    policy: PolicyConstraints
    password: str

class PolicyValidator():
    def __init__(self, policyConstraints):
        self.policyConstraints = policyConstraints
    
    def isValid(self, password):
        validatedLetterCount = password.count(self.policyConstraints.letter)
        return self.policyConstraints.lowestValidCount <= validatedLetterCount <= self.policyConstraints.highestValidCount

def getValidRange(countSegment):
    return [int(x) for x in countSegment.split('-')]

def getValidatedLetter(letterSegment):
    return letterSegment[0]

def parseLineToInputLineInfo(inputLine):
    countSegment, letterSegment, passwordSegment = inputLine.split()
    lowestValidCount, highestValidCount = getValidRange(countSegment)
    letter = getValidatedLetter(letterSegment)
    return InputLineInfo(PolicyConstraints(lowestValidCount, highestValidCount, letter), passwordSegment)

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




