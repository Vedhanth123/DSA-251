class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # start from the left of the array 
        # maintain a pointer which helps in inserting the elements
        # if you find a new element then insert that element to the array and increment the pointer
        
        counter = 1
        newElement = nums[0]

        for x in range(1,len(nums)):

            if(newElement != nums[x]):
                newElement = nums[x]
                nums[counter] = newElement
                counter += 1
        
        return counter
