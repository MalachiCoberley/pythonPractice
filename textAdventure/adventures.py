from utils import clearAndContinue

def getRandomEncounter(item, luck):
    #hmmm... threading params. suss
    return encounterOldMan(item, luck)

def encounterOldMan(item, luck):
    #Sword Advantage
    #Anything but a pool noodle will beat the encounter, unless you have max luck
    modifier = luck + 0
    print("An old man in a bathrobe emerges from the shadows.")
    print("He wields a can of beans and a newspaper.")
    clearAndContinue()
    if item == "Sword":
        print("Before he can react, you swing your sword, missing him entirely but cleanly opening his can of beans from the top")
        print("Satisfied, he leaves, discarding his newspaper as he goes.")
        return True
    elif item == "Pool Noodle":
        print("'Nice pool noodle, nerd', says the old man. 'Clearly you're not a great listener'.")
        modifier -= 2
    print(f"You swing your {item} at him...")
    if modifier > 0:
        print(f"An echoing thud hits your ears and the old man explodes into a million pieces of old-man confetti as your {item} drives through him.")
        return True
    else:
        print("Embarrassingly, you miss and catch a can of beans to the back of the head.")
        return False