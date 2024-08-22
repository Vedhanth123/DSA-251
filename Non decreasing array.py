from os import *
from sys import *
from collections import *
from math import *

def isPossible(arr, n):
    # Write your code here.

    counter = False

    for i in range(len(arr) - 1):

        if(arr[i] <= arr[i+1]):
            continue
        
        if(counter == True):
            return False
        
        if((i == 0) or (arr[i+1] >= arr[1-1])):
            arr[1] = arr[i+1]
        else:
            arr[i+1] = arr[i]

        counter = True
    
    return True
