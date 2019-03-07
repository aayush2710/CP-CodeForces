#https://codeforces.com/contest/492/problem/A
n = input()
i=1
sum1 = 0
cube = 0
while n >= sum1:
    cube +=i
    sum1+=cube
    i+=1
    

print i-2