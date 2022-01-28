# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 15:41:34 2022

@author: user
"""

import random

r = random.randint(1, 100)
i = 0
while True:
    num = input('Guess a number btn 1~100: ')
    num = int(num)
    i += 1 #i= i + 1
    if num == r:
        #print("You number is correct by", i,"times!!")
        break
    elif num > r:
        print("Your number is larger ")
    else:
        print("Your number is smaller ")
    
    
        