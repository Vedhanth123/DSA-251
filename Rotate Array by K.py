def rotateArray(arr: list, k: int) -> list:
    # Write your code here.

    if(len(arr) == 1):
        return arr

    firstPtr = 0
    secondPtr = 0
    # 1) start from the left of the arr

    k = k%len(arr)

    stack = []

    while(firstPtr < len(arr)):

        if(firstPtr >= k):
            arr[secondPtr] = arr[firstPtr]
            secondPtr += 1

        else:
            stack.append(arr[firstPtr])
        
        firstPtr+=1
    
    while(len(stack)):

        arr[secondPtr] = stack.pop(0)
        secondPtr += 1
    
    return arr
        
    
