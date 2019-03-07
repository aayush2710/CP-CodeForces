# https://codeforces.com/contest/119/problem/A
inp = raw_input()
a = int(inp.split()[0])
b = int(inp.split()[1])
n = int(inp.split()[2])

def gcd(p,q):
    a = max(p,q)
 

    for i in range(a,0,-1):
            if q%i==0 and p%i==0:
                return i

while True:
    n -= gcd(a,n)
    if n < 0:
        print 1
        break
    n-= gcd(b,n)
    if n < 0:
        print 0
        break
