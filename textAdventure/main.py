import random
from utils import clearAndContinue
from adventures import * 

#Primary Gameplay function
def play():
    life = 3
    luck = random.randint(0,3)
    backpack = {} #unused at the moment
    print("""Hello adventurer. Choose an item for your quest.
          """)
    item = getStartingItem()
    print(f"Ah, a {item}, what an excellent choice!")
    print("Well buckle up! here comes your first challenge...")
    clearAndContinue()
    
    #encounters will return truthy if they are completed and falsey if they are failed
    while life > 0:
        if getRandomEncounter(item, luck):
            clearAndContinue()
            print("wahoo")
        else:
            clearAndContinue()
            print("oh no")
    print("Oops, you died")
    
def getStartingItem():
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
    
# keeps the console clear and readable.



#Start the game
play()