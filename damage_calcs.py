#This program will take the creatures AC, the damage you would do
#and will give back how many hit and the damage dealt to the target

import random
import re
import os
from time import sleep

line = "****************************************"
calculations_finished = False

num_of_hits = 0
total_damage = 0


def roll_dice(dice_roll):
    match = re.match(r'(\d*)d(\d+)([-+]\d+)?',dice_roll)
    if not match:
        raise ValueError("Invalid dice format")

    num_dice = int(match.group(1) if match.group(1) else 1)
    dice_type = int(match.group(2))
    bonus = int(match.group(3)[1:] if match.group(3) else 0)

    #Generating Dice Rolls
    rolls = []
    for _ in range(num_dice):
        rolls.append(random.randint(1,dice_type))

    #Calculating total damage
    total = sum(rolls)+bonus

    return total

def attack_simulation(num_attacks,ac,to_hit_mod,damage_dice,advatage=False):
    hits = 0
    total_damage = 0

    for _ in range(num_attacks):
        if advatage:
            attack_roll = max(roll_dice("1d20"),roll_dice("1d20"))+to_hit_mod
        else:
            attack_roll = roll_dice("1d20")+to_hit_mod
        
        if attack_roll >= ac:
            hits += 1
            damage_roll = roll_dice(damage_dice)
            total_damage += damage_roll

    return hits, total_damage


#Will run as long as q isn't selected/calculations_finished is equal to true
while calculations_finished == False:
    print(f"""{line}
     D&D Summon Damage Calculator
      
          Roll Damage: R
                Clear: C
                 Quit: Q
{line}""")
    
    #Checks User input and converts to lowercase
    user_input = input("Enter your selection: ")
    user_input = user_input.lower()

#Calculate
    if user_input == 'r':
        num_of_attacks = int(input("Enter the number of attacks being made: "))
        ac = int(input("Enter the AC (Armour Class) of the target: "))
        to_hit_mod = int(input("Enter the to hit modifier: "))
        damage_dice = input("Enter the damage dice (ex. 3d8, or 2d4+2): ")
        advantage = input("Do you have advantage? (yes/no): ")
        advantage = True if advantage.lower() == 'yes' else False

        num_of_hits, total_damage = attack_simulation(num_of_attacks,ac,to_hit_mod,damage_dice,advantage)

        print('\n')
        print("Number of Hits : ", num_of_hits)
        print("Total Damage: ", total_damage)
        print('\n')



# Quit
    elif user_input == 'q':
        calculations_finished = True

    #This Runs in Terminal
    if user_input == 'c':    
        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')