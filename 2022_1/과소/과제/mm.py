N = int(input())
for i in range(N):
    x= int(input())
    arr= list(map(int, input().split()))
    cnt=0
    for j in range(x):
        cnt+=arr[j]
    print(cnt)