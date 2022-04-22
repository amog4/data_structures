
def smallerNumbersThanCurrent( nums:list):
    #O(N*N)
    s = []
    for x in nums:
        num = 0
        for y in nums:
            if x > y:
                num += 1
            else:
                pass
        s.append(num)
    
    return s
                    

# this can be done using dict O(N)
        
nums = [6,5,4,8]

nums =  [7,7,7,7]
        

print(smallerNumbersThanCurrent(nums=nums))