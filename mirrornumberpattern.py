n = int(input())
i = 1
while i<= n:
    s = 1
    while s <= n - i:
        print(' ',end="")
        s = s+1
    stars = 1
    while stars <= i:
        print (stars,end="")
        stars = stars + 1
    print()
    i = i + 1
