#https://codeforces.com/contest/1032/problem/B

from math import ceil,floor
handle = raw_input()
n = float(len(handle))
a = int(ceil(n/20.0))
b = int(ceil(n/a))
flag = 0
st = ""
print int(a), int(b)
asterics_count = a*b - n
for i in range(a):
    
    for j in range(b):
        if i >= (a-asterics_count-flag) and j==b-4 and asterics_count>0:
            st= st+"*"
            asterics_count-=1
            flag+=1
            continue
    
        st=st+ handle[int(b*i+j-flag)]
    st=st+"\n"
print st