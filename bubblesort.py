def performBubbleSort(nums):
    n=len(nums)
    fixThisPosition=n-1
    
    while fixThisPosition >0:
        for index in range(0, fixThisPosition):
            if nums[index]> nums[index+1]:
                nums[index] , nums[index+1]= nums[index+1] , nums[index]
            fixThisPosition-=1
nums=[9,8,7,6,6,5,4,3]
print(nums)
performBubbleSort(nums)
print(nums)