import sys

"""
  | is a vertical pipe connecting north and south.
  - is a horizontal pipe connecting east and west.
  L is a 90-degree bend connecting north and east.
  J is a 90-degree bend connecting north and west.
  7 is a 90-degree bend connecting south and west.
  F is a 90-degree bend connecting south and east.
"""

pipeDict = {
  "|": ["N", "S"],
  "-": ["E", "W"],
  "L": ["N", "E"],
  "J": ["N", "W"],
  "7": ["S", "W"],
  "F": ["S", "E"]
}

directions = {
  "N": [-1, 0],
  "S": [1, 0],
  "E": [0, 1],
  "W": [0, -1],
}

class Pipe:
  def __init__(self, char, row, col):
    self.char = char
    self.row = row
    self.col = col

  def print(self):
    print("Pipe, " + self.char + " at " + str(self.row) + "," + str(self.col))

def main():
  inputFile = open(sys.argv[1], "r")

  startingPosition =  []
  pipes = {}
  row = 0

  # Parse pipes
  for line in inputFile:
    sanitizedLine = line.replace("\n", "")

    for index, char in enumerate(sanitizedLine):
      if char == ".":
        continue
      elif char == "S":
        startingPosition = [row, index]
      else:
        key = str(row) + "," + str(index)
        pipes[key] = Pipe(char, row, index)
    row += 1

  # Solve problem
  print("The starting position is " + str(startingPosition))
  for key in pipes.keys():
    pipes[key].print()

if __name__ == "__main__":
  main()