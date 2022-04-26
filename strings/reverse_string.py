s = ["h","e","l","l","o"]

def reverse_string(s):
    # O(N)

    l  = len(s)

    start = 0
    end = len(s) - 1
    while start < end:
        
        s[start],s[end] = s[end],s[start]
        start += 1
        end -= 1
    
    return s



reverse_string(s)