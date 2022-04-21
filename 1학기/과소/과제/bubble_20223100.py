import random
import time

LOWER, UPPER = 0, 11000
A = [random.randint(LOWER, UPPER) for _ in range(UPPER)]
B = A
start = time.time()
for i in range(LOWER,UPPER):
    for j in range(LOWER,i):
        if(A[i]<A[j]):
            tmp = A[i]
            A[i]=A[j]
            A[j]=tmp
endA = time.time()-start
start = time.time()
B.sort()
endB = (time.time()-start)
print(endA,endB,"{%f} 만큼 차이납니다" %(endA-endB))