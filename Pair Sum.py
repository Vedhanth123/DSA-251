from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, n, target):
    # Write your code here.

    # move 1 pointer from left and 1 pointer from right

    left = 0
    right = n-1

    counter = 0
    while(left < right):

        # check if the pairs are equal
        if(arr[left] + arr[right] == target):
            counter += 1
            left += 1
            right -= 1
        
        elif(arr[left] + arr[right] < target):
            left += 1
        elif(arr[left] + arr[right] > target):
            right -= 1
        
        else:
            pass
    # if the pairs are greater than the target then move the right pointer
    # if the pairs are lesser than the target then move the left pointer
    # if the pairs are equal then move the both the pointers

    if(counter == 0):
        return -1
    else:
        return counter
    pass
