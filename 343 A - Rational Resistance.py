#https://codeforces.com/problemset/problem/343/A
inp = input()
a,b = int(inp.split()[0])  , int(inp.split()[1])
from math import floor
Sum=0
def work(a,b):
    
    global Sum
    if a//b  >= 1 and a/b  >0:
        Sum+= a//b
        work(a%b , b)
    elif a//b  < 1 and a/b  >0:
             work(b,a)
    elif a/b==1:
             Sum+=1
work(a,b)
print(Sum)
             
