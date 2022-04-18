# O(N) Linear/proportional


def test(x):
    # linear in time 
    for v in range(x):
        print(v)


# drop constant in case of O(2N) --> O(N)

def test1(x):

    for v in range(x):
        print(x)

    for v in range(x):
        print(v)


# O(N**2) loop in loop

def test2(x):

    for v in range(x):
        for c in range(x):
            print(v,c)


# drop unimportant element which have little value 
# O(N**2 + N) --- > O(N**2)


def test3(x):

    for v in range(x):
        for c in range(x):
            print(v,c)

    for v in range(x):
        print(x)


# O(logN) --> divide and conquer 

# O(1) constant

def test5(x):

    print(x**2 + x)


# differents inputs O(a * b)

def test6(a,b):

    for v in range(a):
        for c in range(b):
            print(v,c)


