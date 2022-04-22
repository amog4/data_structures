
from token import NUMBER


def twoSum( nums=  [2,7,11,15], target=9):

    sorted(nums)
    start = 0
    end = len(nums) - 1
    for num in range(len(nums)):
        
        if target == nums[start] + nums[end]:
            return [start,end]

        end -= 1    
  
        


twoSum()