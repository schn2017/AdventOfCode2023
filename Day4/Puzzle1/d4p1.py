import re
import sys

def main():
  inputFile = open(sys.argv[1], "r")

  totalPoints = 0
  card = 1
  for line in inputFile:
    sanitizedLine = line.replace("\n", "")

    numbers = sanitizedLine.split(':')[1].split("|")
    winningNumbers = list(filter(None, numbers[0].strip().split(" ")))
    cardNumbers = list(filter(None, numbers[1].strip().split(" ")))

    matches = re.findall(r"\b(" + "|".join(map(re.escape, winningNumbers)) + r")\b", " ".join(cardNumbers))
    if (len(matches) > 0):
      totalPoints += 2 ** (len(matches) - 1)
    card += 1
  inputFile.close()
  print(totalPoints)

if __name__ == "__main__":
  main()