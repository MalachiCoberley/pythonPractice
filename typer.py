###
### README:
# To play, you need to create a csv with two columns
# "Words" and "Best Time"
# The words column should be populated by you.
# Validation takes place for the entire column, so you can use whole sentences or single words
###

import pandas as pd
import random
import time
from datetime import datetime

###
# Dictionary / Score Tracker
# UPDATE THESE TO MATCH YOUR WORD LIST
###
dict_path = './Dictionary100.csv'
NUMBER_OF_WORDS = 100

dictionary = pd.read_csv(dict_path)

play = True
input("Press enter when ready")
while play:
    random_idx = random.randint(0,NUMBER_OF_WORDS - 1)
    random_word = dictionary["Words"][random_idx]
    start_time = datetime.now()
    attempt = input(f"{random_word} \n")
    while attempt != random_word:
        attempt = input(f"\n{random_word} \n")
    end_time = datetime.now()
    difference = end_time - start_time
    
    #convert the time difference into a float to make life easy
    difference = round(float(f"{difference.seconds}.{difference.microseconds}"), 3)
    
    print(f"\nTime: {difference}")
    
    #Check for a best time and compare/update existing records
    if pd.isna(dictionary["Best Time"][random_idx]):
        dictionary.at[random_idx, "Best Time"] = difference
        print("\nHigh Score set\n")
    elif dictionary["Best Time"][random_idx].astype(float) > difference:
        dictionary.at[random_idx, "Best Time"] = difference
        print("\nA New High Score \n")
    
    time.sleep(.25)
    play = (input("\nType 1 to quit, or press Enter to continue playing.\n") != "1")

#save scores
dictionary.to_csv(dict_path, index=False)
print("later, loser")
