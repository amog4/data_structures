nums = [1,1,2,3,4,4]

def remove_duplicate(nums : list):

    start = 1
    temp = 0
    while temp < len(nums):

        if nums[start] != nums[temp]:
            nums[start] = nums[temp]
            start += 1
        temp += 1

    return start



remove_duplicate(nums)




