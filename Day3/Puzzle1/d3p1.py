import sys

inputFile = open(sys.argv[1], "r")

for line in inputFile:
  sanitizedLine = line.replace("\n", "")

inputFile.close()
