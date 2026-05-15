# find the maximum number in an aaray
def findBiggestNumber(nums):
    Maximum=nums[0]
    for i in range(1, len(nums)):  
        if nums[i] > Maximum:
            Maximum=nums[i]
    print(Maximum)

nums=[5,7,9,2,3,4]
findBiggestNumber(nums)
