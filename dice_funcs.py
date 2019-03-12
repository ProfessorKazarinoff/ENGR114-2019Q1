#!/usr/bin/env python
# coding: utf-8

# imports
import random

# run a dice_roll() function to produce list or array of dice roll values
def dice_roll(n):
    dice_lst = []
    for i in range(n):
        roll = random.randint(1,6)
        dice_lst.append(roll)
    
    return dice_lst

# run a dice_add() function to add the roll values together
def dice_add(dice_roll_lst):
    output = sum(dice_roll_lst)
    
    return output

my_variable = 'variable value defined inside .py-file'






