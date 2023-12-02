import sys

inputFile = open(sys.argv[1], "r")

sum = 0

for line in inputFile:
  sanitizedLine = line.replace("\n", "")
  foundNumbersAsChars = ["", ""]

  for char in sanitizedLine:
    if (char.isdigit()):
      if (foundNumbersAsChars[0] == ""):
        foundNumbersAsChars[0] = char
      else:
        foundNumbersAsChars[1] = char
  
  number = ""

  if (foundNumbersAsChars[0] != ""):
    number += foundNumbersAsChars[0]

    if (foundNumbersAsChars[1] == ""):
      number += foundNumbersAsChars[0]
    else:
      number += foundNumbersAsChars[1]

  if (number != ""):
    sum += int(number)

print(sum)
inputFile.close()