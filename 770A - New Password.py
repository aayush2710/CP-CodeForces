#https://codeforces.com/problemset/problem/770/A
inp = input()
n = int(inp.split()[0])
k = int(inp.split()[1])
alpha = "qwertyuioplkjhgfdsazxcvbnm"


use = alpha[0:k]
res = ''

for i in range(k):
        res+=use[i]

import math
a = n/k
q = math.floor(a)
r = round((a-q)*k)
fres = q*res

for i in range(r):
    fres+=res[i]
print(fres)


        
    
