
def solution(sequence):
    
    start = 0
    end = len(sequence) - 1

    d = {"[":"]","{":"}"}
    
    temp = []
    while start <= end:
        print(temp)
        if sequence[start] in d:
            temp.append(d[sequence[start]])
        elif sequence[start] not in d and temp:
            temp.pop()
        else:
            return False
     
        start += 1
            
    
    return temp == []


solution("{[}{}{][}]")