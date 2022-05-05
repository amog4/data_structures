height = [1,8,6,2,5,4,8,3,7]



def maxArea(height: List[int]) -> int:
    
    
    start = 0
    end = len(height) - 1
    maxarea = 0
    
    while start < end:
        
        width = end - start
        maxarea = max(maxarea, min(height[start],height[end]) * width)
        
        if height[start] <=  height[end]:
            start += 1
        else:
            end -= 1
            
    return maxarea
    
        