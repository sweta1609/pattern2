n = int (input())
n1 = (n+1)//2
i = 1
while i<=n1:
    j = 1
    while j<=(i-1):
        print(" ",end="")
        j = j + 1
    k = 1    
    while k <= i:
        print("* ",end="")
        k = k + 1
    print()    
    i = i + 1
n2 = n//2
i = 1    
while i<=n2:
    j = 1
    while j<=(n2-i ):
        print(" ",end="")
        j = j + 1
    k = 1    
    while k <=(n2-i+1):
        print("* ",end="")
        k = k + 1
    print()    
    i = i + 1 
