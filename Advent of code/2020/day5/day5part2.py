from typing import NamedTuple
import sys

class InputFileReader():
    
    def __init__(self):
        self.inputFileName = sys.argv[1]

    def getInputLines(self):
        with open(self.inputFileName) as f:
            return f.read().splitlines()

class BoardingPass(NamedTuple):
    row: int
    column: int

class PartitioningDecryptor():
    
    def __init__(self):
        self.rowPartLength = 7
        self.columnPartLength = 3
        self.letterToBinaryValueMap = {'B': '1', 'F': '0', 'R':'1', 'L':'0'}

    def convertToNumber(self, boardingPassPart):
        return int(''.join([self.letterToBinaryValueMap[x] for x in boardingPassPart]), 2)

    def decrypt(self, partitioning):
        rowPart = partitioning[:self.rowPartLength]
        columnPart = partitioning[self.rowPartLength:self.rowPartLength+self.columnPartLength]
        return BoardingPass(self.convertToNumber(rowPart), self.convertToNumber(columnPart))

def calculateSeatId(boardingPass):
    return boardingPass.row * 8 + boardingPass.column

def solve(inputLines):
    seatIds = []
    decryptor = PartitioningDecryptor()
    for partitioning in inputLines:
        boardingPass = decryptor.decrypt(partitioning)
        seatId = calculateSeatId(boardingPass)
        seatIds.append(seatId)
    maximumSeatId, minimumSeatId = max(seatIds), min(seatIds)
    totalSeatsCount = maximumSeatId - minimumSeatId + 1
    return totalSeatsCount * (maximumSeatId+minimumSeatId) / 2 - sum(seatIds)

inputFileReader = InputFileReader()
print(solve(inputFileReader.getInputLines()))
