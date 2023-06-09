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
    #TODO: priority was a dumb idea and doesn't even work with the way i implemented turns, 
        # should maybe have a pen vs. power dynamic with non effect moves.
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

#
# prompts are 1 indexed but lists are all 0 indexed. Maybe a function should explicitly do the -1 with
# specific inputs
#

class Monster:
    def __init__(self) -> None:
        self.name = input("What is my name? \n")
        self.baseHp = random.randint(100, 200)
        self.currentHp = self.baseHp * 1
        self.currentEffect = None
        self.attack = random.randint(5, 15)
        self.defense = random.randint(5, 15)
        self.type = TYPES[random.randint(0,2)]
        self.moves = [ALL_MOVES[random.randint(0,2)], ALL_MOVES[random.randint(3,6)]]

    def getType(self):
        print(self.moves)
        return self.type
    
    def isFainted(self):
        print(f"{self.name} fainted. Send out another PyCliMon")
        self.currentHp = 0
    
    def showStats(self):
        print(f"""
              Name: {self.name}
              Type: {self.type}
              HP: {self.baseHp}
              Attack/Def: {self.attack}/{self.defense}
              Moves: {self.moves[0].showStats()} / {self.moves[1].showStats()}
              """)

    def useMove(self, moveNum) -> tuple:
        moveIdx = moveNum - 1
        outgoingDamage = self.moves[moveIdx].power
        return (outgoingDamage, self.type, self.moves[moveIdx].effect)
    
    def receiveDamage(self, attack) -> None:
        incomingDamage, attackType, effect = attack
        actualDamage = incomingDamage - round(self.defense/2)
        
        if self.hasTypeAdvantage(attackType):
            actualDamage *= 2
            print("super effective")
            
        self.currentHp -= actualDamage
        
        #after applying damage, faint dude if no Hp remaining, otherwise apply effect if it exists
        if self.currentHp <= 0:
            self.isFainted()
        elif effect != None:
            self.currentEffect = effect
            
        
    
    def displayMoves(self) -> str:
        return f"""
    1.) {self.moves[0].showStats()}
    2.) {self.moves[1].showStats()}

                """
    def hasTypeAdvantage(self, moveType):
        if self.type == TYPES[0]: #rock
            if moveType == TYPES[1]:
                return True
        elif self.type == TYPES[1]: #paper
            if moveType == TYPES[2]:
                return True
        elif self.type == TYPES[2]:
            if moveType == TYPES[0]:
                return True
        return False
    
class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.team =[ Monster() for i in range(0, TEAM_SIZE) ]
        self.activeMon = None

    def getTeam(self) -> list:
        return self.team
    
    def chooseActiveMon(self, monNum = 1) -> Monster:
        monIdx = monNum - 1
        print(f"Go, {self.team[monIdx].name}!")
        self.activeMon = self.team[monIdx]
        return self.activeMon
    
    def displayTeam(self) -> str:
        return f"""
1.) {self.team[0].name}:{self.team[0].type} - {self.team[0].currentHp}
2.) {self.team[1].name}:{self.team[1].type} - {self.team[1].currentHp}
3.) {self.team[2].name}:{self.team[2].type} - {self.team[2].currentHp}
        """
    
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
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        #turnOrder list manages play order. index 0 is the active player. need a better name i think
        self.turnOrder = [self.player1, self.player2]
    
    def play(self) -> None:
        self.player1.chooseActiveMon()
        self.player2.chooseActiveMon()
        while self.player1.hasLivingMon() and self.player2.hasLivingMon():
            self.displayBattleStats()
            self.playTurn()
            self.statusCheck()
            
            self.turnOrder[0], self.turnOrder[1] = self.turnOrder[1], self.turnOrder[0]
        if self.player1.hasLivingMon():
            print("Player 1 Wins!")
        elif self.player2.hasLivingMon():
            print("Player 2 Wins!")
        else:
            print("Lol, how did you tie?!?!")
                
    def playTurn(self) -> None:
        #TODO: allow players to back out of menu with like 3 or something.
        if self.displayTurnPrompt() == 1:
            #select a move
            attack = getInput(self.turnOrder[0].activeMon.displayMoves(), "Command must be a number")
            #calc outgoing damage and apply incoming
            self.turnOrder[1].activeMon.receiveDamage(self.turnOrder[0].activeMon.useMove(attack))
            if self.player1.activeMon.currentHp <= 0:
                self.player1.chooseActiveMon(getInput(self.player1.displayTeam(), "i need real error handling"))
            elif self.player2.activeMon.currentHp <= 0:
                self.player2.chooseActiveMon(getInput(self.player2.displayTeam(), "i need real error handling"))
        else:
            self.turnOrder[0].chooseActiveMon(getInput(self.turnOrder[0].displayTeam(), "i need real error handling"))
            
    
    def statusCheck(self) -> None:
        #TODO: finish logic for effect triggering/resolution
        activeMon = self.turnOrder[0].activeMon
        if activeMon.currentEffect == EFFECTS[0]: #inaction
            pass
        elif activeMon.currentEffect == EFFECTS[1]: #switch
            pass
        elif activeMon.currentEffect == EFFECTS[2]: #drain
            #TODO: Maybe make the damage number less magical
                #also shouldn't need redundant hp < 0 checks. need a more robust damage check
            drainDamage = round(activeMon.baseHp/12)
            resolveChance = 25
            activeMon.currentHp -= drainDamage
            if activeMon.currentHp <= 0:
                activeMon.isFainted()
            print("Poison damage. owwwy")
            if random.randint(1,100) <= resolveChance:
                activeMon.currentEffect = None
        elif activeMon.currentEffect == EFFECTS[3]: #swap
            pass

    def displayTurnPrompt(self) -> int:
        return getInput("""
1.) Attack
2.) Switch
               """, "Command must be a number")
               
    def displayBattleStats(self) -> None:
        defendingTeamIcons = ""
        activeTeamIcons = ""
        for mon in self.turnOrder[1].team:
            if (mon.currentHp < mon.baseHp) and (mon.currentHp > 0):
                defendingTeamIcons += ("▲ ")
            elif mon.currentHp == mon.baseHp:
                defendingTeamIcons += ("■ ")
            else:
                defendingTeamIcons += ("- ")
        for mon in self.turnOrder[0].team:
            if (mon.currentHp < mon.baseHp) and (mon.currentHp > 0):
                activeTeamIcons += ("▲ ")
            elif mon.currentHp == mon.baseHp:
                activeTeamIcons += ("■ ")
            else:
                activeTeamIcons += ("- ")
        defendingMonHealth = ""
        activeMonHealth = ""       
        for i in range(round(self.turnOrder[0].activeMon.currentHp / 5)):
            activeMonHealth += "="
        for i in range(round(self.turnOrder[1].activeMon.currentHp / 5)):
            defendingMonHealth += "="
        
        print(f"""
              {self.turnOrder[1].name}
              {defendingTeamIcons}
              {self.turnOrder[1].activeMon.name}: {self.turnOrder[1].activeMon.type}
              HP: {self.turnOrder[1].activeMon.currentHp}/{self.turnOrder[1].activeMon.baseHp} {defendingMonHealth}
     
          - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
     
     {self.turnOrder[0].name}
     {activeTeamIcons}
     {self.turnOrder[0].activeMon.name}: {self.turnOrder[0].activeMon.type}
     HP: {self.turnOrder[0].activeMon.currentHp}/{self.turnOrder[0].activeMon.baseHp} {activeMonHealth}
              """
            )

            
              
#Moves need to be generated before the game starts. May just want to hard-code this better.
ALL_MOVES = generateMoves()

game = Game()
game.play()