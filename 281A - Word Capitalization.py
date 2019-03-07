#https://codeforces.com/contest/281/problem/A
inp = raw_input()
res = ''

for i in range(len(inp)):
    if i==0:
        res+=inp[i].upper()
    else:
        res+=inp[i]
print res
