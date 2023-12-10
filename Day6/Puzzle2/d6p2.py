import sys

def main():
  inputFile = open(sys.argv[1], "r")

  times = []
  records = []

  # Parse Times and Records
  for line in inputFile: 
    sanitizedLine = line.replace("\n", "")
    parts = sanitizedLine.split(":")
    number = parts[1].replace(" ", "")

    if sanitizedLine.startswith("Time:"):
      times.append(int(number))
    elif sanitizedLine.startswith("Distance:"):
      records.append(int(number))

  product = 1
  for index, record in enumerate(records):
    timeAllowed = times[index]
    possibleMoves = 0
    for i in range(timeAllowed):
      velocity = i
      distance = velocity * (timeAllowed - i)
      if distance > records[index]:
        possibleMoves += 1
    product *= possibleMoves
  print(product)
if __name__ == "__main__":
  main()