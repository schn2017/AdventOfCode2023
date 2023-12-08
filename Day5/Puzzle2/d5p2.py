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
    return self.destRangeStart + (num - self.sourceStart)

class Map:
  def __init__(self, rules):
    self.rules = rules
    
  def getSubRanges(self, start, end):
    rangesToProcess = [[start, end]]
    subRanges = {}
    while len(rangesToProcess) > 0:
      currentRange = rangesToProcess.pop()
      rangeAsStr = str(currentRange[0]) + "," + str(currentRange[1])
      #print("processing")
      #print(currentRange)
      # If range is already found skip it
      if rangeAsStr in subRanges.keys():
        continue

      for rule in self.rules: 
        # If range end less than the start of the rule, can't be translated
        # OR if range start greate than end of the , can't be translated

        if currentRange[1] < rule.sourceStart or rule.sourceEnd < currentRange[0]:
          key = str(currentRange[0]) + "," + str(currentRange[1])
          subRanges[key] = currentRange
        # If range fits within the entire rule, can be translated
        elif rule.sourceStart <= currentRange[0] and currentRange[1] <= rule.sourceEnd:
          #print("Range can be translated")
          key = str(currentRange[0]) + "," + str(currentRange[1])
          #print("Translating key " + key)
          subRanges[key] = currentRange
          pass
        # if range contains the rule
        elif currentRange[0] < rule.sourceStart and rule.sourceEnd < currentRange[1]:

          left = [currentRange[0], rule.sourceStart - 1]
          middle = [rule.sourceStart, rule.sourceEnd ]
          right = [rule.sourceEnd + 1, currentRange[1]]

          rangesToProcess.append(left)
          rangesToProcess.append(right)
          key = str(middle[0]) + "," + str(middle[1])
          subRanges[key] = middle
        elif currentRange[0] == currentRange[1]:
          key = str(currentRange[0]) + "," + str(currentRange[1])
          subRanges[key] = currentRange

    #print(subRanges)

    # if we find no sub ranges then return original range
    if len(subRanges.keys()) == 0:
      return [start, end]

    return list(subRanges.values())

  def translate(self, num):
    #print("translating")
    for rule in self.rules:
      if rule.matchesSource(num):
        return rule.getDestValue(num)
    # Any source numbers that aren't mapped correspond to the same destination number
    return num

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
        #print(parts)
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

      #print(numbers)
      currentRules.append(Rule(int(numbers[0]), int(numbers[1]), int(numbers[2])))

  # Add any rules that weren't previously added due to EOF
  if len(currentRules) > 0:
    maps.append(Map(currentRules))
  
  minValue = 0
  minValueSet = False
  for seed in seeds:
    seedRanges = []
    translations = []
    for index, map in enumerate(maps):
      if index == 0:
        seedRanges = map.getSubRanges(seed.start, seed.end)
        for seedRange in seedRanges:
          translations.append(seedRange[0])
          translations.append(seedRange[1])
      
      for index, translation in enumerate(translations):
        translations[index] = map.translate(translation)
        if not minValueSet:
          minValue = translations[index]
          minValueSet = True

        if translations[index] < minValue:
          minValue = translations[index]
      pass
      
  print("The min value is " + str(minValue))
if __name__ == "__main__":
  main()