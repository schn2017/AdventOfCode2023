import sys

directions = {
  "n": [-1, 0],
  "s": [1, 0],
  "e": [0, 1],
  "w": [0, -1],
  "ne": [-1, 1],
  "nw": [-1, -1],
  "se": [1, 1],
  "sw": [1, -1]
}

class PartNumber:
  def __init__(self, numberStr, row, start, end):
    self.numberStr = numberStr
    self.row = row
    self.start = start
    self.end = end

  def isAdjacent(self, symbol):
    for direct in directions:
      direction = directions[direct]

      if ((symbol.row + direction[0]) == self.row) and (self.start <= (symbol.col + direction[1]) and ((symbol.col + direction[1]) <= self.end)):
        return True

    return False
  
class Symbol:
  def __init__(self, char, row, col):
    self.char = char
    self.row = row
    self.col = col

def main():
  inputFile = open(sys.argv[1], "r")
  foundSymbols = []
  foundNumbers = []

  row = 0

  # Read schematic
  for line in inputFile:
    sanitizedLine = line.replace("\n", "")

    col = 0
    currentNumber = ""

    for index, char in enumerate(sanitizedLine):
      if (char.isdigit()):
        currentNumber += char
        if index == len(sanitizedLine) - 1:
          # Add 1 because we hit the last element, 
          # for example, 555, with a index of 9
          # 9 - len(555) = 6 but it should be 7
          start = col - len(currentNumber) + 1

          foundNumbers.append(PartNumber(currentNumber, row, start, col))
      else:
        if (char == "*"):
          foundSymbols.append(Symbol(char, row, col))
        
        if (len(currentNumber) > 0):
          start = col - len(currentNumber)
          # Subtract one because we hit a . or symbol after the number
          end = col - 1
          
          foundNumbers.append(PartNumber(currentNumber, row, start, end))
        currentNumber = ""
      col += 1
    row += 1

  sum = 0
  for symbol in foundSymbols:
    adjSides = []
    for foundNumber in foundNumbers:
      if foundNumber.isAdjacent(symbol):
        adjSides.append(int(foundNumber.numberStr))
    if len(adjSides) == 2:
      sum += adjSides[0] * adjSides[1]

  print(sum)
  inputFile.close()

if __name__ == "__main__":
  main()