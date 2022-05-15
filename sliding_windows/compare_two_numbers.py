

def max_sum(arr,n,k):

    # compute the first window
    m = 0 
    for i in range(k):
        m += arr[i]

    curr_sum = m
    for i in range(k,n):

        curr_sum += arr[i] - arr[i-k]
        m = max(m,curr_sum)
    
    return m

    