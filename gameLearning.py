import random
import os
from time import sleep

#Primary Gameplay function
def play():
    life = 3
    luck = random.randint(0,3)
    backpack = {}
    print("""Hello adventurer. Choose an item for your quest.
          """)
    item = getItem()
    print(f"Ah, a {item}, what an excellent choice!")
    print("Well buckle up! here comes your first challenge...")
    clearAndContinue()
    
    #encounters will return truthy if they are completed and falsey if they are failed
    if getRandomEncounter(item, luck):
        print("wahoo")
    
def getItem():
    itemNumber = input("""Enter the number that corresponds with the item you want
          1. A Sword
          2. A Staff
          3. A Book
          """)
    if itemNumber == "1":
            item = "Sword"
    elif itemNumber == "2":
            item = "Staff"
    elif itemNumber == "3":
            item = "Book"
    else:
            item = "Pool Noodle"
    return item

def getRandomEncounter(item, luck):
    #hmmm... threading params. suss
    encounterOldMan(item, luck)
    
# keeps the console clear and readable.
def clearAndContinue():
    input("press enter to continue")
    os.system('clear')
    sleep(.25)

def encounterOldMan(item, luck):
    modifier = luck + 0
    print("An old man in a bathrobe emerges from the shadows.")
    print("He wields a can of beans and a newspaper.")
    clearAndContinue()
    if item == "Sword":
        print("Before he can react, you swing your sword, missing him entirely but cleanly opening his can of beans from the top")
        print("Satisfied, he leaves.")
        return True
    elif item == "Pool Noodle":
        print("'Nice pool noodle, nerd', says the old man. 'Clearly you're not a great listener'.")
        modifier -= 2
    print(f"You swing your {item} at him...")
    if modifier > 0:
        print(f"An echoing thud hits your ears and the old man explodes into a million pieces of old-man confetti as your {item} drives through him.")
        return True
    else:
        print("Embarassingly, you miss and catch a can of beans to the back of the head.")
        return False

#Start the game
play()