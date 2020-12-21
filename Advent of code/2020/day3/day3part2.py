from typing import NamedTuple
import sys

treeCharacter = '#'
class Dimensions(NamedTuple):
    width: int
    height: int

class Position(NamedTuple):
    X: int
    Y: int

class InputFileReader():
    
    def __init__(self):
        self.inputFileName = sys.argv[1]

    def getInputLines(self):
        with open(self.inputFileName) as f:
            return f.read().splitlines()

class WorldMap():
    def __init__(self, worldMap):
        self.worldMap = worldMap
        self.dimensions = Dimensions(len(worldMap[0]), len(worldMap))
    
    def getAt(self, position):
        return self.worldMap[position.Y][position.X % self.dimensions.width]
    
class StepSimulator():
    def __init__(self, startPosition, horizontalShift, verticalShift):
        self.currentPosition = startPosition
        self.horizontalShift = horizontalShift
        self.verticalShift = verticalShift
    
    def makeStep(self):
        self.currentPosition =  Position(self.currentPosition.X + self.horizontalShift, self.currentPosition.Y + self.verticalShift)

def isTree(character):
    return character == treeCharacter

def solve(inputLines, horizontalShift, verticalShift):
    startPosition = Position(0,0)
    worldMap = WorldMap(inputLines)
    stepSimulator = StepSimulator(startPosition, horizontalShift, verticalShift)
    treeCount = 0
    while stepSimulator.currentPosition.Y < worldMap.dimensions.height:        
        treeCount += 1 if isTree(worldMap.getAt(stepSimulator.currentPosition)) else 0
        stepSimulator.makeStep()
    
    return treeCount

inputFileReader = InputFileReader()

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
product = 1
for horizontalShift, verticalShift in slopes:
    product *= solve(inputFileReader.getInputLines(), horizontalShift, verticalShift)
print(product)



