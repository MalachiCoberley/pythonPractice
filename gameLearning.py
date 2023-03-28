import random

#Primary Gameplay function
def play():
    life = 3
    luck = random.randint(0,3)
    print("""Hello adventurer. Choose an item for your quest.
          """)
    item = getItem()
    print(f"Ah, a {item}, what an excellent choice!")
    print("Well buckle up! here comes your first challenge...")
    
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


#Start the game
play()