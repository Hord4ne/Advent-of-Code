from typing import NamedTuple
import sys

class InputFileReader():
    
    def __init__(self):
        self.inputFileName = sys.argv[1]

    def getInputLines(self):
        with open(self.inputFileName) as f:
            return f.readlines()

class AnswerParser():
    
    def __init__(self, lines):
        self.empty = ''
        self.answersSeparator = '\n'
        self.lines = lines
    
    def getAnswerGroups(self):
        i = 0
        currentAnswerGroup = self.empty
        while i < len(self.lines):
            if (self.lines[i] == self.answersSeparator and currentAnswerGroup != self.empty):
                yield currentAnswerGroup
                currentAnswerGroup = self.empty
            else:
                currentAnswerGroup += self.lines[i]
            i += 1
        if currentAnswerGroup != self.empty:
            yield currentAnswerGroup

class AnswerCounter():
    
    def countAnswers(self, answerGroup):
        return len(set([x for x in ''.join(answerGroup.splitlines())]))


def solve(inputLines):
    answerParser = AnswerParser(inputLines)
    answerCounter = AnswerCounter()

    totalCount = 0
    for answerGroup in answerParser.getAnswerGroups():
        totalCount += answerCounter.countAnswers(answerGroup)
    return totalCount

inputFileReader = InputFileReader()
print(solve(inputFileReader.getInputLines()))

