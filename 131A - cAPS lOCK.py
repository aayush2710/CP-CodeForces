#https://codeforces.com/contest/131/problem/A
a=raw_input()
def check(a):
    if a[0].islower() and a[1::].isupper() and len(a)>1:
        return a.swapcase()
    elif a.isupper() and len(a)>1:
        return a.swapcase()
    elif len(a) == 1:
        return a.swapcase()
    else:
        return a;

print check(a)