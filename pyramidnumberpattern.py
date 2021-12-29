n = int(input())
i = 1
while i<=n:
    space = 1
    while space <=n-i:
        print(' ',end="")
        space = space + 1
    p = i+1-1
    j = 1
    while j<=i:
        print(p,end="")
        j = j + 1
        p = p - 1
    p = i - 1
    t = 1
    k = 2*t
    while p>=1:
        print(k,end="")
        p = p - 1
        k = k + 1
    print()
    i = i + 1
    
