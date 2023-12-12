import sys
import re
import math

class Node:
  def __init__(self, id, left, right):
    self.id = id
    self.left = left
    self.right = right

def main():
  inputFile = open(sys.argv[1], "r")

  instructions = []
  nodeDict = {}
  currentNodes = []
  endNodes = []

  for line in inputFile: 
    sanitizedLine = line.replace("\n", "")

    # Read instructions
    if len(instructions) == 0:
      instructions[:] = sanitizedLine
    # Parse node
    elif len(sanitizedLine) > 0:
      nodes = re.findall(r'\b[A-Za-z]+\b', sanitizedLine)
      newNode = Node(nodes[0], nodes[1], nodes[2])
      if nodes[0].endswith("A"):
        currentNodes.append(newNode)
      elif nodes[0].endswith("Z"):
        endNodes.append(newNode)

      nodeDict[nodes[0]] = newNode

  count = 0
  reachedEnd = False
  lengthDict = {}
  while not reachedEnd:
    for instruction in instructions:
      count += 1
      for index, currentNode in enumerate(currentNodes): 
        if instruction == "L":
          currentNodes[index] = nodeDict[currentNode.left]
        else:
          currentNodes[index] = nodeDict[currentNode.right] 

        if currentNodes[index].id.endswith("Z"):
          lengthDict[index] = count

        if len(lengthDict.keys()) == len(currentNodes):
          reachedEnd = True
      
  values = list(lengthDict.values())
  print(math.lcm(*values))

if __name__ == "__main__":
  main()