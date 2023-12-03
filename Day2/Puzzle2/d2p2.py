import sys

inputFile = open(sys.argv[1], "r")

sum = 0

for line in inputFile:
  sanitizedLine = line.replace("\n", "")
  parts = sanitizedLine.split(":")
  rounds = parts[1].split(";")

  currentGameCubes = {
    "red": 0,
    "green": 0,
    "blue": 0
  }

  for round in rounds:
    cubes = round.split(",")
    for cube in cubes:
      cubeParts = cube.lstrip().split(" ")
      if (currentGameCubes[cubeParts[1]] < int(cubeParts[0])):
        currentGameCubes[cubeParts[1]] = int(cubeParts[0])

  sum += (currentGameCubes["red"] * currentGameCubes["green"] * currentGameCubes["blue"])

inputFile.close()
print(sum)