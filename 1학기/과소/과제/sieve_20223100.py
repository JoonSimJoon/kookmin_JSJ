import math
N =50
sqrt_N = int(math.sqrt(N))
flag = [0]*52
flag[0]=1
flag[1]=1
for i in range(2,sqrt_N+1):
    j=2
    while i*j<=50:
        flag[i*j]=1
        j+=1

for i in range(50):
    if flag[i]==0:
        print(i,end=" ")
