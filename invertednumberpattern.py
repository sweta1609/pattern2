n = int (input())
i = n
while i>=1:
    j = 1
    while j<=n+i-n:
        print(i,end="")
        j = j + 1
    print()
    i = i -  1
