import sys
from typing import NamedTuple

class SolvePart1Data(NamedTuple):
    excludedNumber: int
    wantedNumber: int

class InputFileReader():
    
    def __init__(self):
        self.inputFileName = sys.argv[1]

    def getInputNumbers(self):
        with open(self.inputFileName) as f:
            return [int(x) for x in f.readlines()]
    
def solve(wantedNumber, inputNumbers):
    complementNumbers = {}

    for inputNumber in inputNumbers:
        distanceFromWantedNumber = wantedNumber - inputNumber

        if inputNumber in complementNumbers:
            return distanceFromWantedNumber * inputNumber
        else:
            complementNumbers[distanceFromWantedNumber] = inputNumber    

def getNumbersWithout(numbers, excludedNumber):
    for number in numbers:
        if number != excludedNumber:
            yield number

def makePart1Problem(wantedNumber, inputNumbers):
    for inputNumber in inputNumbers:
        yield SolvePart1Data(inputNumber, wantedNumber - inputNumber)

def solve2part(wantedSum, inputNumbers):
    for part1Problem in makePart1Problem(wantedSum, inputNumbers):
        result = solve(part1Problem.wantedNumber, getNumbersWithout(inputNumbers, part1Problem.excludedNumber))
    
        if (result):
            return result*part1Problem.excludedNumber

wantedSumNumber = 2020
inputFileReader = InputFileReader()
print(solve2part(wantedSumNumber, inputFileReader.getInputNumbers()))
