import sys

cardStrength = {
  "2": 0,
  "3": 1,
  "4": 2,
  "5": 3,
  "6": 4,
  "7": 5,
  "8": 6,
  "9": 7,
  "T": 8,
  "J": 9,
  "Q": 10,
  "K": 11,
  "A": 12
}

class Hand:
  def __init__(self, handAsStr, bid):
    self.hand = handAsStr
    self.bid = bid
    self.type = self.getType()

  def __lt__(self, other):
    if self.type < other.type:
      return True
  
    elif self.type == other.type:
      for index, char in enumerate(self.hand):
        if cardStrength[char] < cardStrength[other.hand[index]]:
          return True
        elif cardStrength[self.hand[index]] > cardStrength[other.hand[index]]:
          return False
        
    return False 

  def getType(self):
    cards = {}

    for char in self.hand:
      if char in cards.keys():
        cards[char] += 1
      else:
        cards[char] = 1

    cardsFound = len(cards.keys())

    # only one card found, must be 5 of a kind
    if cardsFound == 1:
      return 6
    # 4 of a kind OR Full house
    elif cardsFound == 2:
      for card in cards:
        if cards[card] == 4:
          return 5
      
      return 4
    # 3 of a kind OR 2 pair
    elif cardsFound == 3:
      for card in cards:
        if cards[card] == 3:
          return 3
      return 2
    elif cardsFound == 4:
      return 1
    # 5 cards found, must be high card
    elif cardsFound == 5:
      return 0

    return 0

  def print(self):
    print(self.hand + " " + str(self.bid) + " type: " + str(self.type))

def main():
  inputFile = open(sys.argv[1], "r")

  hands = []

  # Parse hands
  for line in inputFile: 
    sanitizedLine = line.replace("\n", "")

    parts = sanitizedLine.split(" ")
    hands.append(Hand(parts[0], int(parts[1])))

  hands.sort()

  sum = 0
  for index, hand in enumerate(hands):
    sum += (index + 1) * hand.bid

  print(sum)
if __name__ == "__main__":
  main()