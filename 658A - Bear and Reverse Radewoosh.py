#https://codeforces.com/contest/658/problem/A
inp1 = raw_input()
inp2=raw_input()
inp3 = raw_input()
n = int(inp1.split()[0])
c = int(inp1.split()[1])
score = inp2.split()
time = inp3.split()
Limak_points = 0
Radewoosh_points = 0
time_sum1 = 0
time_sum2 = 0
for i in range(n):
    time_sum1 += int(time[i])
    time_sum2 += int(time[-1-i])
    Limak_points+=max(0,int(score[i])-c*time_sum1)
    Radewoosh_points+= max(0,int(score[-1-i])-c*time_sum2)

if Radewoosh_points < Limak_points:
    print "Limak"
elif Radewoosh_points > Limak_points:
    print "Radewoosh"
else:
    print "Tie"
    
    