#https://codeforces.com/problemset/problem/148/B
L=[]
for i in range(5):
    L.append(input())

Vp = int(L[0])
Vd = int(L[1])
t = int(L[2])
f = int(L[3])
c = int(L[4])
del L

n=0

while True:
    try:
        t1=Vp*t/(Vd-Vp)
    except:
        n=0
        break
    
    if Vd*t1 >=c:
        break
    else:
        n+=1
        t+=2*t1+f

print(n)
