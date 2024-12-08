def palin(tup) :
    e=len(tup)-1
    s=0
    while (s<e):
        if (tup[s]!=tup[e]) :
            return (False)
        s=s+1
        e=e-1
    return True

t1=(1,2,2,1,3,3,1,2,2,1)
if palin(t1) :
    print ("tuple is flipflop:)")
else :
    print("tuple not flipflop :(")
print("\U0001F600")