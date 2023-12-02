import re
import sys

def wordToNumberStr(str):
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

  return numberDict[str]

def pairToNumber(pair):
  numberAsStr = ""

  for item in pair:
    if item.isdigit():
      numberAsStr += item
    else:
      numberAsStr += wordToNumberStr(item)

  return int(numberAsStr)

def main():
  inputFile = open(sys.argv[1], "r")

  sum = 0

  for line in inputFile:
    sanitizedLine = line.replace("\n", "")

    matches = []
    for m in re.finditer('(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))', sanitizedLine):
      matches.append(m.group(1))
    
    pair = []
    if (len(matches) == 1): 
      pair = [matches[0], matches[0]]
    elif (len(matches) == 2):
      pair = [matches[0], matches[1]]
    elif (len(matches) >= 2):
      pair = [matches[0], matches[len(matches) - 1]]

    if (len(pair) > 0):
      number = pairToNumber(pair)
      sum += number

  inputFile.close()
  print(sum)

if __name__ == "__main__":
  main()