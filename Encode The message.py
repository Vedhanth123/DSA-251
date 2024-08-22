from os import *
from sys import *
from collections import *
from math import *

def encode(message):
    # Write your code here.

    
    # count the number of characters
    counter = 0
    currentCharacter = message[0]
    finalString = ""

    for x in range(len(message)):

        if(currentCharacter != message[x]):

            finalString += f"{currentCharacter}{counter}"
            counter = 0
            currentCharacter = message[x]
            counter += 1
        
        else:

            counter += 1

    finalString += f"{currentCharacter}{counter}"

    return finalString
