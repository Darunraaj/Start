#nums = [5,4,19,2,8,7]
#target = 10
def two_sum(nums : list , target:int):
    for i in range (0,len(nums)):
        for j in range (i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return [-1]


print (two_sum([9,4,5,3,8,15] , 11))