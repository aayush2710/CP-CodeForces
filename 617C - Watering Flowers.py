from math import sqrt
def norm(L1,L2):
    return ((L1[0]-L2[0])**2 + (L1[1]-L2[1])**2)
inp = input()
L = inp.split()
n = int(L[0])
fountain1 = [int(L[1]) , int(L[2])]
fountain2 = [int(L[3]) , int(L[4])]
del L
flowers = []
r = []
d1 = []
d2 = []
for i in range(n):
    inp = input()
    flowers.append([int(inp.split()[0]) , int(inp.split()[1])])
    r.append([norm(flowers[i],fountain1) , norm(flowers[i],fountain2)])
    
    if r[i][0] > r[i][1] :
        d2.append(r[i][1])
        d1.append(0)
    else:
        d1.append(r[i][0])
        d2.append(0)

a = max(d1)
b = max(d2)



def minimize_r(a,b):
    global r
    if a>b:
        
        while b>=0:
            flag=0
            for i in range(n):
                if r[i][0] >a and r[i][1]>b:
                    
                    flag = 1
                    break
           
            if flag==0:
                b-=1
            elif flag == 1:
                
                return a+b+1
    
    else:
        
        while a>=0:
            flag=0
            for i in range(n):
                if r[i][0] >a and r[i][1]>b:
                    flag = 1
                    break
           
            if flag==0:
                a-=1
            elif flag==1:
               
                return a+b+1
            
                    
print(int(minimize_r(a,b)))
            


             
              
            
    


    

    
             
