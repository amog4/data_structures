nums = [4,2,5,7]

def sortArray(nums):

    start = 0
    end = 1
    t = len(nums)

    while start < t and end < t:

        while start < t and nums[start] % 2 == 0:
            start += 2

        while end < t and nums[end] % 2 != 0:
            end += 2

        if start < t and end < t:
            nums[start],nums[end] = nums[end],nums[start]

    return nums

