def firstMissing(arr,n):
# Write your function here.


    # 1) replace all the -ve numbers with 0
    for x in range(len(arr)):
        if(arr[x] < 0):
            arr[x] = 0

    # 2) to mark if the number is present in the array then change the value at that index to -ve
    for x in range(len(arr)):
    
        index = abs(arr[x])

        if(1 <= index <= len(arr)):
            
            if(arr[index-1] > 0):
                arr[index-1] *= -1
            elif(arr[index-1] == 0):
                arr[index-1] = -1 * (len(arr) + 1)
            else:
                pass
        
    # 3) to find out the numbers present in the array just check if the index's value is -ve
    for x in range(1, len(arr)+1):

        if(arr[x-1] >= 0):
            return x
        
    return len(arr) + 1
