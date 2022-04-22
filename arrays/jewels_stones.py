jewels = "aA"
stones = "aAAbbbb"

jewels = "z"
stones = "ZZ"

def numJewelsInStones( jewels: str, stones: str) :
    out = 0
    for w in stones:
        if w in jewels:
            out +=1

    return out
            


print(numJewelsInStones( jewels,stones))