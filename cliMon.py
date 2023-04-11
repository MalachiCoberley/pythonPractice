### Imports
import random

### Constants
TYPES = ['Rock', 'Paper', 'Scissors']
EFFECTS = ['Inaction', 'Switch', 'Drain', 'Swap']
ATTACK_TYPES = ['Standard', 'Strong', 'Quick', 'Stun', 'Hit and Run', 'Poison', 'Scare']
TEAM_SIZE = 3

#input util function
def getInput(prompt: str, error_message: str = "") -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)


#Moves need to be generated before the game starts. May just want to hard-code this better.
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


class Monster:
    def __init__(self) -> None:
        self.name = input("What is my name? \n")
        self.baseHp = random.randint(100, 200)
        self.currentHp = self.baseHp * 1
        self.attack = random.randint(5, 15)
        self.defense = random.randint(5, 15)
        self.type = TYPES[random.randint(0,2)]
        self.moves = [ALL_MOVES[random.randint(0,2)], ALL_MOVES[random.randint(3,6)]]

    def getType(self):
        print(self.moves)
        return self.type
    
    def showStats(self):
        print(f"""
              Name: {self.name}
              Type: {self.type}
              HP: {self.baseHp}
              Attack/Def: {self.attack}/{self.defense}
              Moves: {self.moves[0].showStats()} / {self.moves[1].showStats()}
              """)

    def useMove(self, idx) -> tuple:
        outgoingDamage = self.moves[idx].power
        effect = ''
        return (outgoingDamage, effect)
    
    def receiveDamage(self, damage, effect) -> None:
        #TODO add logic for calculating damage
        pass
    
    def displayMoves(self) -> str:
        return f"""
                1.) {self.moves[0].showStats()}
                2.) {self.moves[1].showStats()}
                """
    
class Player:
    def __init__(self) -> None:
        self.team =[ Monster() for i in range(0, TEAM_SIZE) ]
        self.activeMon = None

    def getTeam(self) -> list:
        return self.team
    
    def chooseActiveMon(self, idx = 0) -> Monster:
        print(f"Go, {self.team[idx].name}!")
        self.activeMon = self.team[idx]
        return self.activeMon
    
    def hasLivingMon(self) -> bool:
        for mon in self.team:
            if mon.currentHp > 0:
                return True
        return False


class Move:
    def __init__(self, name, power, priority, effect = None) -> None:
        self.name = name
        self.power = power
        self.priority = priority
        self.effect = effect
        
    def showStats(self) -> str:
        return f"{self.name} | {self.power} | {self.effect}"
    

class Game:
    def __init__(self) -> None:
        self.player1 = Player()
        self.player2 = Player()
        #turnOrder tuple manages play order. index 0 is the active player. need a better name i think
        self.turnOrder = (self.player1, self.player2)
    
    def play(self) -> None:
        self.player1.chooseActiveMon()
        self.player2.chooseActiveMon()
        while self.player1.hasLivingMon() and self.player2.hasLivingMon():
            self.playTurn()
            self.statusCheck()
            
            self.turnOrder[0], self.turnOrder[1] = self.turnOrder[1], self.turnOrder[0]
                
    def playTurn(self) -> None:
        if self.displayTurnPrompt() == 1:
            getInput(self.turnOrder[0].activeMon.displayMoves(), "Command must be a number")
        else:
            #TODO: add logic for switching
            pass
    
    def statusCheck(self) -> None:
        #TODO: add logic for effect triggering/resolution
        pass

    def displayTurnPrompt(self) -> int:
        getInput("""
               1.) Attack
               2.) Switch
               """, "Command must be a number")
               
#Moves need to be generated before the game starts. May just want to hard-code this better.
ALL_MOVES = generateMoves()

game = Game()
game.play()