import re
import sys

cardDict = {}

def main():
  inputFile = open(sys.argv[1], "r")

  cardId = 1
  # Read in all the score cards
  for line in inputFile:
    sanitizedLine = line.replace("\n", "")
    parts = sanitizedLine.split(':')
    
    numbers = parts[1].split("|")
    winningNumbers = list(filter(None, numbers[0].strip().split(" ")))
    cardNumbers = list(filter(None, numbers[1].strip().split(" ")))

    matches = re.findall(r"\b(" + "|".join(winningNumbers) + r")\b", " ".join(cardNumbers))
    matchCount = len(matches)

    # Add card initially if it is not already there, otherwise update value
    if not cardId in cardDict.keys():
      cardDict[cardId] = 1
    else:
      cardDict[cardId] += 1

    for x in range(1, matchCount + 1):
      if cardId + x in cardDict.keys():
        cardDict[cardId + x] += cardDict[cardId]
      else:
        cardDict[cardId + x] = cardDict[cardId]
  
    cardId += 1

  inputFile.close()

  sum = 0
  for key in cardDict.keys():
    sum += cardDict[key]

  print(sum)
if __name__ == "__main__":
  main()