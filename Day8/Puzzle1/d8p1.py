import sys
import re

class Node:
  def __init__(self, id, left, right):
    self.id = id
    self.left = left
    self.right = right

def main():
  inputFile = open(sys.argv[1], "r")

  instructions = []
  nodeDict = {}
  rootNode = None
  currentNode = None

  for line in inputFile: 
    sanitizedLine = line.replace("\n", "")

    # Read instructions
    if len(instructions) == 0:
      instructions[:] = sanitizedLine
    # Parse node
    elif len(sanitizedLine) > 0:
      nodes = re.findall(r'\b[A-Za-z]+\b', sanitizedLine)
      newNode = Node(nodes[0], nodes[1], nodes[2])
      nodeDict[nodes[0]] = newNode

  currentNode = nodeDict["AAA"]

  count = 0
  while currentNode.id != "ZZZ":
    for instruction in instructions:
      if instruction == "L":
        currentNode = nodeDict[currentNode.left]
      else:
        currentNode = nodeDict[currentNode.right]

      count += 1

  print(count)
if __name__ == "__main__":
  main()