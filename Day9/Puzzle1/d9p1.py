import sys

class Sequence:
  def __init__(self, numbers):
    self.numbers = []
    for number in numbers:
      self.numbers.append(int(number))
    self.differences = []

  def getDifferences(self):
    for index in range(len(self.numbers)):
      if (index + 1) < len(self.numbers):
        diff = self.numbers[index + 1] - self.numbers[index]
        self.differences.append(diff)
  
  def endHit(self, currentRow):
    for item in currentRow:
      if item != 0:
        return False
      
    return True

  def predictValue(self):
    return self.numbers[-1] + self.differences[-1]


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