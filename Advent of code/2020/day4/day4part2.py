from typing import NamedTuple
import sys

class InputFileReader():
    
    def __init__(self):
        self.inputFileName = sys.argv[1]

    def getInputLines(self):
        with open(self.inputFileName) as f:
            return f.readlines()

class KeyValue(NamedTuple):
    key: str
    value: str

class PassportPartValidator():
    def __init__(self, key):
        self.key = key
    
    def isKeyPresent(self, passport):
        return self.key in passport

    def getEntry(self, passport):
        value = passport.split(self.key+':')[1].split()[0] #todo as regex, regex would be nicer but who likes writing regex.....
        return KeyValue(self.key, value)

    def isValidValue(self, passport):
        raise NotImplementedError("Please Implement this method")

    def isValid(self, passport):
        return self.isKeyPresent(passport) and self.isValidValue(passport)

class YearRangeValidator(PassportPartValidator):

    def __init__(self, key, minVal, maxVal):
        super(YearRangeValidator, self).__init__(key)
        self.minVal = minVal
        self.maxVal = maxVal
    
    def isValidValue(self, passport):
        entry = self.getEntry(passport)
        return self.minVal <= int(entry.value) <= self.maxVal

class BirthYearRangeValidator(YearRangeValidator):

    def __init__(self):
        super(BirthYearRangeValidator, self).__init__('byr', 1920, 2002)

class IssueYearRangeValidator(YearRangeValidator):
    
    def __init__(self):
        super(IssueYearRangeValidator, self).__init__('iyr', 2010, 2020)

class ExpirationYearRangeValidator(YearRangeValidator):
    
    def __init__(self):
        super(ExpirationYearRangeValidator, self).__init__('eyr',2020,2030)

class PassportIdValidator(PassportPartValidator):

    def __init__(self):
        super(PassportIdValidator, self).__init__('pid')
        self.requiredIdLength = 9

    def isValidValue(self, passport):
        entry = self.getEntry(passport)
        return len(entry.value) == self.requiredIdLength and all([str.isdigit(x) for x in entry.value])

class EyeColorValidator(PassportPartValidator):

    def __init__(self):
        super(EyeColorValidator, self).__init__('ecl')
        self.allowedColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def isValidValue(self, passport):
        entry = self.getEntry(passport)
        return entry.value in self.allowedColors


class HeightMetricValidator(PassportPartValidator): 
    def __init__(self, key, metric, minValue, maxValue):
        super(HeightMetricValidator, self).__init__(key)
        self.metric = metric
        self.minValue = minValue
        self.maxValue = maxValue

    def isValidValue(self, passport):
        entry = self.getEntry(passport)
        metricLength = len(self.metric)
        return entry.value.endswith(self.metric) and self.minValue <= int(entry.value[:-metricLength]) <= self.maxValue

class HeightValidator(PassportPartValidator):
    def __init__(self):
        super(HeightValidator, self).__init__('hgt') 
        self.validators = [
            HeightMetricValidator('hgt','cm', 150, 193),
            HeightMetricValidator('hgt', 'in', 59, 86)]   
    
    def isValidValue(self, passport):
        for validator in self.validators:
            if validator.isValid(passport):
                return True
        return False

class HairColorValidator(PassportPartValidator):
    def __init__(self):
        super(HairColorValidator, self).__init__('hcl')
        self.initialCharacter = '#'
        self.hairColorEntryLength = 7
        self.allowedCharacters = '0123456789abcdef'

    def isValidValue(self, passport):
        entry = self.getEntry(passport)
        return entry.value.startswith(self.initialCharacter) and len(entry.value) == self.hairColorEntryLength and all([x in self.allowedCharacters for x in entry.value[1:]])

class PassportValidator():

    def __init__(self):
        self.validators = [
            BirthYearRangeValidator(),
            IssueYearRangeValidator(),
            ExpirationYearRangeValidator(),
            HeightValidator(),
            HairColorValidator(),
            EyeColorValidator(),
            PassportIdValidator()
        ]
    
    def isValid(self, passport):
        for validator in self.validators:
            if not validator.isValid(passport):
                return False
        return True


class PassportParser():

    def __init__(self, lines):
        self.empty = ''
        self.passportSeparator = '\n'
        self.lines = lines
    
    def getPassports(self):
        i = 0
        currentPassport = self.empty
        while i < len(self.lines):
            if (self.lines[i] == self.passportSeparator and currentPassport != self.empty):
                yield currentPassport
                currentPassport = self.empty
            else:
                currentPassport += self.lines[i]
            i += 1
        if currentPassport != self.empty:
            yield currentPassport

def solve(inputLines):
    passportValidator = PassportValidator()
    passportParser = PassportParser(inputLines)

    validPassports = 0
    for passport in passportParser.getPassports():
        if passportValidator.isValid(passport):
            validPassports += 1

    return validPassports


inputFileReader = InputFileReader()
print(solve(inputFileReader.getInputLines()))

