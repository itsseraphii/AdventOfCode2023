from utils.aoc_utils import AOCDay, day


@day(2)
class Day2(AOCDay):
    def common(self):
        # print(self.inputData)
        # print(self.rawData)

        # Parse the input data to make a tuple containing the max value of each color
        self.maxValues = []
        for lineIndex in range(len(self.inputData)):
            self.maxColor(lineIndex)

        return 0

    # Return the min/max values of red, green and blue as a tuple in their respective array
    def maxColor(self, lineIndex):
        # Split the line for each 'round' while removing the GAME prefix
        rounds = self.inputData[lineIndex].split(':')[1].split(';')
        maxRed, maxGreen, maxBlue = 0, 0, 0
        for round in rounds:
            colors = round.split(',')
            for color in colors:
                color = color.strip().split(' ')
                # green
                if (color[1][0] == 'g'):
                    if (int(color[0]) > maxGreen):
                        maxGreen = int(color[0])
                # red
                elif (color[1][0] == 'r'):
                    if (int(color[0]) > maxRed):
                        maxRed = int(color[0])
                # blue
                elif (color[1][0] == 'b'):
                    if (int(color[0]) > maxBlue):
                        maxBlue = int(color[0])


        self.maxValues.append((maxRed, maxGreen, maxBlue))

    def part1(self):
        total = 0
        for game in range(len(self.maxValues)):
            values = self.maxValues[game]
            # R, G , B
            if (values[0] <= 12 and values[1] <= 13 and values[2] <= 14):
                total += game + 1 # Games start at 1, not 0 lol
        return total

    def part2(self):
        total = 0
        # Get the POWER of the minVaues
        for values in self.maxValues:
            total += values[0] * values[1] * values[2]
        return total
