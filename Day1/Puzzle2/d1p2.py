import re
import sys

numberDict = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9"
}

def pairToNumber(pair):
  numberAsStr = ""

  for item in pair:
    if item.isdigit():
      numberAsStr += item
    else:
      numberAsStr += numberDict[item]

  return int(numberAsStr)

def main():
  inputFile = open(sys.argv[1], "r")

  sum = 0

  for line in inputFile:
    sanitizedLine = line.replace("\n", "")

    matches = re.findall('(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))', sanitizedLine)
    if (len(matches) > 0):
      sum += pairToNumber([matches[0], matches[-1]])
  
  inputFile.close()
  print(sum)

if __name__ == "__main__":
  main()