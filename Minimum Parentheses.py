from os import *
from sys import *
from collections import *
from math import *

def minimumParentheses(pattern):

    # Write your code here
    # Return the minimum number of parentheses required.d

    # 1) traverse through the string if you find opening paranthesis then push to stack 
    # 2) if closing parenthesis is found then pop from the stack
    # 3) if stack is empty then true else false


    stack = []
    stack2 = []

    counter = 0
    for x in range(len(pattern)):

        if(pattern[x] == ')' and len(stack) == 0):
            counter += 1
        if(pattern[x] == '('):
            stack.append(pattern[x])
        if(pattern[x] == ')' and len(stack) != 0):
            stack.pop(0)
        
    counter += len(stack)

    return counter
    
