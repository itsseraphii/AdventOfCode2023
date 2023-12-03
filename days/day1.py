from utils.aoc_utils import AOCDay, day


@day(1)
class Day1(AOCDay):
    def common(self):
        self.digits = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                       'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

        #print(self.inputData)
        # print(self.rawData)
        return 0

    def part1(self):
        total = 0
        for i in range(len(self.inputData)):
            strDigit = self.findFirstDigit(i) + self.findFirstDigit(i, True)
            total += int(strDigit)
        return total

    def part2(self):
        total = 0
        for i in range(len(self.inputData)):
            strNumber = self.findFirstNumber(self.inputData[i]) + self.findLastNumber(self.inputData[i])
            total += int(strNumber)
        return total

    def findFirstDigit(self, lineIndex, reverse=False):
        if reverse:
            for i in range(len(self.inputData[lineIndex])-1, -1, -1):
                if self.inputData[lineIndex][i] in self.digits.values():
                    return self.inputData[lineIndex][i]
        else:
            for i in range(len(self.inputData[lineIndex])):
                if self.inputData[lineIndex][i] in self.digits.values():
                    return self.inputData[lineIndex][i]
        return None

    def findFirstNumber(self, line):
        # First check for digit
        for i in range(len(line)):
            if line[i] in self.digits.values():
                return line[i]
            else: # Check for word
                for word in self.digits.keys():
                    if line[i:i+len(word)] == word:
                        return self.digits[word]
        return None

    def findLastNumber(self, line):
        # First check for digit
        for i in range(len(line)-1, -1, -1):
            if line[i] in self.digits.values():
                return line[i]
            else: # Check for word
                for word in self.digits.keys():
                    if line[i-len(word)+1:i+1] == word:
                        return self.digits[word]
        return None
            
