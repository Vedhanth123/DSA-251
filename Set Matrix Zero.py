from math import *
from collections import *
from sys import *

from typing import List

def moveUp(x_axis, y_axis, matrix):

    while(x_axis >= 0):
        matrix[x_axis][y_axis] = 0
        x_axis -= 1
    

def moveRight(x_axis, y_axis, matrix):

    while(y_axis < len(matrix[x_axis])):
        matrix[x_axis][y_axis] = 0
        y_axis += 1
    
    
def moveLeft(x_axis, y_axis, matrix):
    
    while(y_axis >= 0):
        matrix[x_axis][y_axis] = 0
        y_axis -= 1

def moveDown(x_axis, y_axis, matrix):
    
    while(x_axis < len(matrix)):
        matrix[x_axis][y_axis] = 0
        x_axis += 1


def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.


    indciesOfZeros = []

    # traverse through the matrix and find out all the zeros places
    for x in range(len(matrix)):

        for y in range(len(matrix[x])):

            if(matrix[x][y] == 0):
                indciesOfZeros.append((x,y))

    # after finding all the zeros of the places now change the rows and corresponding to zeros
    for x in indciesOfZeros:
        x_axis = x[0]
        y_axis = x[1]
    
        moveUp(x_axis-1, y_axis, matrix)
        moveDown(x_axis+1, y_axis, matrix)
        moveLeft(x_axis, y_axis-1, matrix)
        moveRight(x_axis, y_axis+1, matrix)
    
    return matrix

        

    pass
