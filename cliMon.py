### Imports
import random

### Constants
TYPES = ['Rock', 'Paper', 'Scissors']

# random 2 moves. priority attack, switch attack, power attack, status attack

class Player:
    def __init__(self):
        # seed team of 3 randos
       self.team = []

    
class Monster:
    def __init__(self):
        self.baseHp = random.randint(100, 200)
        self.attack = random.randint(5, 25)
        self.defense = random.randint(5, 25)
        self.type = TYPES[random.randint(0,2)]
        self.moves = [()]

    def getType(self):
        return self.type

#
class Move:
    
    
pops = Monster()
print(pops.getType())