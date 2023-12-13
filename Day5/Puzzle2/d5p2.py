import sys
import re

class SeedInfo:
  def __init__(self, start, rangeLength):
    self.start = start
    self.end = start + rangeLength - 1

class Rule:
  def __init__(self, destStart, sourceStart, rangeLength):
    self.destRangeStart = destStart
    self.sourceStart = sourceStart
    self.sourceEnd = sourceStart + rangeLength - 1

  def matchesSource(self, num):
    return num >= self.sourceStart and num <= self.sourceEnd

  def getDestValue(self, num):
    value = self.destRangeStart + (num - self.sourceStart)
    return value

class Map:
  def __init__(self, rules):
    self.rules = rules
    
  def getSubRanges(self, start, end):
    rangesToProcess = [[start, end]]

    subRanges = {}
    translatedAlready = []
    while len(rangesToProcess) > 0:
      currentRange = rangesToProcess.pop()

      rangeAsStr = str(currentRange[0]) + "," + str(currentRange[1])

      # If range is already found skip it
      if rangeAsStr in subRanges.keys():
        continue

      for rule in self.rules: 
        # If range end less than the start of the rule, can't be translated
        # OR if range start greate than end of the , can't be translated

        if currentRange[1] < rule.sourceStart or rule.sourceEnd < currentRange[0]:
          continue
        # If range fits within the entire rule, can be translated
        elif rule.sourceStart <= currentRange[0] and currentRange[1] <= rule.sourceEnd:
          newRange = [rule.getDestValue(currentRange[0]), rule.getDestValue(currentRange[1])]
          key = str(newRange[0]) + "," + str(newRange[1])
          subRanges[key] = newRange

          oldKey = str(currentRange[0]) + "," + str(currentRange[1])

          translatedAlready.append(oldKey)
          subRanges.pop(oldKey, "None")

        # if range contains the rule
        elif currentRange[0] < rule.sourceStart and rule.sourceEnd < currentRange[1]:
          left = [currentRange[0], rule.sourceStart - 1]
          middle = [rule.sourceStart, rule.sourceEnd]
          right = [rule.sourceEnd + 1, currentRange[1]]

          rangesToProcess.append(left)
          rangesToProcess.append(right)

          newRange = [rule.getDestValue(middle[0]), rule.getDestValue(middle[1])]
          key = str(newRange[0]) + "," + str(newRange[1])
          subRanges[key] = newRange

          oldKey = str(rule.sourceStart) + "," + str(rule.sourceEnd)

          translatedAlready.append(oldKey)
          subRanges.pop(oldKey, "None")

        elif currentRange[0] < rule.sourceStart and currentRange[1] <= rule.sourceEnd:
          newRange = [rule.getDestValue(rule.sourceStart), rule.getDestValue(currentRange[1])]
          key = str(newRange[0]) + "," + str(newRange[1])
          if not key in translatedAlready:
            subRanges[key] = newRange
        elif rule.sourceStart < currentRange[0] and rule.sourceEnd < currentRange[1]:
          newRange = [rule.getDestValue(currentRange[0]), rule.getDestValue(rule.sourceEnd)]
          key = str(newRange[0]) + "," + str(newRange[1])
          if not key in translatedAlready:
            subRanges[key] = newRange       
        elif currentRange[0] == currentRange[1]:
          key = str(currentRange[0]) + "," + str(currentRange[1])
          subRanges[key] = currentRange

    # if we find no sub ranges then return original range
    if len(subRanges.keys()) == 0:
      key = str(start) + "," + str(end)
      subRanges[key] = [start, end]
 
    return subRanges

def main():
  inputFile = open(sys.argv[1], "r")
  #inputFile = open("test.txt", "r")

  seeds = []
  maps = []
  currentRules = []
  for line in inputFile: 
    sanitizedLine = line.replace("\n", "")

    if sanitizedLine.startswith("seeds:"):
      matches = re.findall("(\d+\s+\d+)", sanitizedLine)
      for match in matches:
        parts = match.split(" ")
        seeds.append(SeedInfo(int(parts[0]), int(parts[1])))
    elif sanitizedLine.endswith('map:'):
      pass
    elif len(sanitizedLine) == 0 and len(currentRules) > 0:
      maps.append(Map(currentRules))
      currentRules = []
    else:
      numbers = sanitizedLine.split(" ")
      if len(numbers) != 3: 
        continue

      currentRules.append(Rule(int(numbers[0]), int(numbers[1]), int(numbers[2])))

  # Add any rules that weren't previously added due to EOF
  if len(currentRules) > 0:
    maps.append(Map(currentRules))
  
  minValueSet = False
  minValue = 0
  
  for seed in seeds:
    currentSubRanges = {}
    for i, map in enumerate(maps):
      newSubRanges = {}
      nextSubRanges = {}
      if i == 0:
        nextSubRanges = maps[0].getSubRanges(seed.start, seed.end)
      else:
        for currentRange in currentSubRanges.keys():     
          newSubRanges = map.getSubRanges(currentSubRanges[currentRange][0], currentSubRanges[currentRange][1])

          for key in newSubRanges.keys():
            if not key in nextSubRanges:
              nextSubRanges[key] = newSubRanges[key]

      currentSubRanges = nextSubRanges.copy()

      if i == len(maps) - 1:
        for range in currentSubRanges:
          leftValue = currentSubRanges[range][0]

          if not minValueSet:
            minValue = leftValue
            minValueSet = True
          elif leftValue < minValue:
            print(minValue)
            minValue = leftValue

  print("The min value is " + str(minValue))
if __name__ == "__main__":
  main()