from decimal import *
getcontext().prec = 28

L = input().split()
n = Decimal(L[0])
m = Decimal(L[1])

if m>=n:
    print(n)
else:
    
    from math import ceil
    k = Decimal(0.5)
    a = (1+8*(n-m))**k
    
    print(int((ceil((-1+a)/Decimal(2))+m)))
