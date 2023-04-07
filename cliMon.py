### Imports
import random

### Constants
TYPES = ['Rock', 'Paper', 'Scissors']
EFFECTS = ['Inaction', 'Switch', 'Drain', 'Swap']
ATTACK_TYPES = ['Standard', 'Strong', 'Quick', 'Stun', 'Hit and Run', 'Poison', 'Scare']


#This approach to handling moves may be dumb.... we will see.
def generateMoves() -> list:
    moves = []
    moves.append(Move(ATTACK_TYPES[0], 20, 1))
    moves.append(Move(ATTACK_TYPES[1], 30, 2))
    moves.append(Move(ATTACK_TYPES[2], 15, 0))
    moves.append(Move(ATTACK_TYPES[3], 10, 1, EFFECTS[0]))
    moves.append(Move(ATTACK_TYPES[4], 15, 1, EFFECTS[1]))
    moves.append(Move(ATTACK_TYPES[5], 10, 1, EFFECTS[2]))
    moves.append(Move(ATTACK_TYPES[6], 10, 1, EFFECTS[3]))
    return moves


class Player:
    def __init__(self) -> None:
        # seed team of 3 randos
       self.team = []

    
class Monster:
    def __init__(self) -> None:
        self.name = input("What is my name? \n")
        self.baseHp = random.randint(100, 200)
        self.attack = random.randint(5, 25)
        self.defense = random.randint(5, 25)
        self.type = TYPES[random.randint(0,2)]
        self.moves = [ALL_MOVES[random.randint(0,2)], ALL_MOVES[random.randint(3,6)]]

    def getType(self):
        print(self.moves)
        return self.type

#
class Move:
    def __init__(self, name, power, priority, effect = None) -> None:
        self.name = name
        self.power = power
        self.priority = priority
        self.effect = effect
    
#confirmed. this approach is dumb and runtime gets fucky. 
ALL_MOVES = generateMoves()

class Game:
    pass


pops = Monster()
pops.getType()