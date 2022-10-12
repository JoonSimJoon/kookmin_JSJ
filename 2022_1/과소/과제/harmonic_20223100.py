import math

for k in range(1,101):
    cnt=0
    rate=0
    ln_cnt=0
    for N in range(1,k+1):
        cnt+=1/N
    ln_cnt=math.log(k+1)
    rate=(ln_cnt-cnt)/cnt
    print(cnt,ln_cnt,rate)