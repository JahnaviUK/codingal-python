def flipflop(r):
    e = len(r)-1
    s = 0 
    while(s < e):
        if(r[s]!=r[e]):
            return False
        s += 1
        e -= 1
    return True
r = (1,2,3,3,2,1)
if(flipflop(r)):
    print("the tuple is flipflop")
else:
    print("tuple is not flipflop")