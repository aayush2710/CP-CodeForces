#https://codeforces.com/contest/977/problem/A
inp = raw_input()
temp = inp.split()
num = int(temp[0])
for i in range(int(temp[1])):
    
    if num%10 != 0:
        num-=1
    else:
        num/=10

print num