def insertion_sort(my_list):

    for i in range(1,len(my_list)):
        temp = my_list[i]
        j = i - 1
        while  temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list



string = 'saiamog'
o = 'aeiou'
index  = []
temp = ()

for n in range(len(string)):
    string = list(string)
    print(string)
    if string[n] in o:
        index.append(n)
        print(index)
    else:
        temp = (n,string[n])
        if index and temp[0] > index[-1]:
            for i in index:
                string[i] = temp[1]
                print(string)
                index =[]
        """if index and temp[0] > index[-1]:
            for i in index:
                string[i] = temp[1]"""


