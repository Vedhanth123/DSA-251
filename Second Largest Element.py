def findSecondLargest(sequenceOfNumbers):
    # Write your code here.

    if(len(sequenceOfNumbers) < 2):
        return -1
    
    diff = 0
    for x in range(len(sequenceOfNumbers) - 1):

        diff = sequenceOfNumbers[x] - sequenceOfNumbers[x+1]
        if(diff != 0):
            break

    if(diff == 0):
        return -1 
    maxi = sequenceOfNumbers[0]
    secondMaxi = -2147483649
    for x in range(len(sequenceOfNumbers)):
        if(maxi < sequenceOfNumbers[x]):
            maxi = sequenceOfNumbers[x]
    


    for x in range(len(sequenceOfNumbers)):
        if(sequenceOfNumbers[x] != maxi):
            if(secondMaxi < sequenceOfNumbers[x]):
                secondMaxi = sequenceOfNumbers[x]


    return secondMaxi
