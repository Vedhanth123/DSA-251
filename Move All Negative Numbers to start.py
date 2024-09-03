from os import *
from sys import *
from collections import *
from math import *

def separateNegativeAndPositive(nums):
    # write your code here

    new_positive = []
    new_negative = []

    for x in range(len(nums)):

        if(nums[x] < 0):
            new_negative.append(nums[x])
        else:
            new_positive.append(nums[x])
    
    return new_negative + new_positive
    pass


