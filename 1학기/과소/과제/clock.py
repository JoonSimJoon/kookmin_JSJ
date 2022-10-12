import math

N = int(input())
for i in range(N):
    a,b = map(int,input().split())
    x = (abs(30*a-(5.5)*b))
    if x>180:
        x=360-x
    print(math.trunc(x))