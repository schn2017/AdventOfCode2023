import sys

class Sequence:
  def __init__(self, numbers):
    self.numbers = []
    for number in numbers:
      self.numbers.append(int(number))
    self.differences = []

  def getDifferences(self):
    currentRowDiff = self.numbers

    while not self.endHit(currentRowDiff):
      row = []
      for index in range(len(currentRowDiff)):
        if (index + 1) < len(currentRowDiff):
          diff = currentRowDiff[index + 1] - currentRowDiff[index]
          row.append(diff)

      currentRowDiff = row
      self.differences.append(currentRowDiff)
  
  def endHit(self, currentRow):
    for index in range(len(currentRow)):
      if (index + 1) < len(currentRow) and (currentRow[index + 1] - currentRow[index] != 0):
        return False
    return True

  def predictValue(self):
    offset = 0

    for diff in self.differences:
      offset += diff[-1]

    return self.numbers[-1] + offset


def main():
  inputFile = open(sys.argv[1], "r")

  sum = 0
  for line in inputFile: 
    sanitizedLine = line.replace("\n", "")
    numbers = sanitizedLine.split(" ")
    
    sequence = Sequence(numbers)
    sequence.getDifferences()
    sum += sequence.predictValue()
  print(sum)

if __name__ == "__main__":
  main()