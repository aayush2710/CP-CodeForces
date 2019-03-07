#https://codeforces.com/problemset/problem/144/C
s,p = input() , input()
k = len(p)
n = len(s)
res = 0

def check(s,p):
    
    temp_s = ""
    for i in range(len(s)):
        if not(s[i] in p or s[i] == "?"):
            temp_s +=s[i]
        elif s[i] in p:
            l = p.rfind(s[i])
            p = p[:l] + p[l+1:]
            
    if temp_s == "":
        return True
    else:
        return False

for i in range(0,n-k+1):
    if check(s[i:i+k] , p):
        res+=1
print(res)
    
    
