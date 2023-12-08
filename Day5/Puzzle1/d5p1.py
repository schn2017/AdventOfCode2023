import sys
import re

class Rule:
  def __init__(self, destStart, sourceStart, rangeLength):
    self.destRangeStart = destStart
    self.sourceRangeStart = sourceStart
    self.sourceRangeEnd = sourceStart + rangeLength

  def matchesSource(self, num):
    return num >= self.sourceRangeStart and num <= self.sourceRangeEnd

  def getDestValue(self, num):
    return self.destRangeStart + (num - self.sourceRangeStart)

class Map:
  def __init__(self, rules):
    self.rules = rules
    
  def translate(self, num):
    for rule in self.rules:
      if rule.matchesSource(num):
        return rule.getDestValue(num)
    # Any source numbers that aren't mapped correspond to the same destination number
    return num

def main():
  inputFile = open(sys.argv[1], "r")

  seeds = []
  maps = []
  currentRules = []
  for line in inputFile:
    sanitizedLine = line.replace("\n", "")

    if sanitizedLine.startswith("seeds:"):
      matches = re.findall("\d+", sanitizedLine)
      for match in matches:
        seeds.append(int(match))
    elif sanitizedLine.endswith('map:'):
      pass
    elif len(sanitizedLine) == 0:
      maps.append(Map(currentRules))
      currentRules = []
    else:
      numbers = sanitizedLine.split(" ")
      currentRules.append(Rule(int(numbers[0]), int(numbers[1]), int(numbers[2])))

  # Add any rules that weren't previously added due to EOF
  if len(currentRules) > 0:
    maps.append(Map(currentRules))

  minValue = 0
  for index, seed in enumerate(seeds):
    currentValue = seed
    for map in maps:
      currentValue = map.translate(currentValue)

    if index == 0:
      minValue = currentValue
    elif currentValue < minValue:
      minValue = currentValue

  print("The min value is " + str(minValue))
if __name__ == "__main__":
  main()