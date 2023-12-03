import sys

inputFile = open(sys.argv[1], "r")

maxCubes = {
  "red": 12,
  "green": 13,
  "blue": 14
}

sum = 0

for line in inputFile:
  sanitizedLine = line.replace("\n", "")
  parts = sanitizedLine.split(":")

  gameId = parts[0].split("Game ")[1]
  rounds = parts[1].split(";")

  validGame = True
  for round in rounds:
    currentGameCubes = {
      "red": 0,
      "green": 0,
      "blue": 0
    }

    cubes = round.split(",")
    for cube in cubes:
      cubeParts = cube.lstrip().split(" ")
      currentGameCubes[cubeParts[1]] += int(cubeParts[0])

    if (maxCubes["red"] < currentGameCubes["red"] 
      or maxCubes["green"] < currentGameCubes["green"] 
      or maxCubes["blue"] < currentGameCubes["blue"]):
      validGame = False

  if (validGame):
    sum += int(gameId)

inputFile.close()
print(sum)