#This program will take the creatures AC, the damage you would do
#and will give back how many hit and the damage dealt to the target

import random
import os
from time import sleep

line = "****************************************"
calculations_finished = False

# Will have to have the flat damage from the 1d6 +((4)) be tied to how many hit and multiply
# the flat damage by the amount of hits made. That or figure out how to convert 1d? into
# a random command and get it to notice that

# look into finding a way to recognize the d in 1d? and make it use random. use the in fucntion?

# this way thats being programmed will work for one dice type with the flat damage

roll = 0
summon_to_hit = 0
summon_rolled_damage = 0
summon_flat_damage = 0
enemy_ac = 10

num_of_hits = 0
total_damage = 0

#Will run as long as q isn't selected/calculations_finished is equal to true
while calculations_finished != True:
    print(f"""{line}
     D&D Summon Damage Calculator
      
            Calculate: C
                 Quit: Q
{line}""")
    
    #Checks User input and converts to lowercase
    user_input = input("Enter your selection: ")
    user_input = user_input.lower()

#Calculate
    if user_input == 'c':
        user_input = input("What is the plus to hit?")



# Quit
    elif user_input == 'q':
        transactions_finished = True

    else:
        print(f"{line}\n           INVALID SELECTION \n{line}")

    #This Runs in Terminal
    sleep(10)
    os.system('cls' if os.name == 'nt' else 'clear')