N = int(input())

for i in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [0,0,0,0]
    C[0] = max(A[0],B[0])
    C[1] = max(A[1],B[1])
    C[2] = min(A[2],B[2])
    C[3] = min(A[3],B[3])
    if(C[2]-C[0]<0 or C[3]-C[1]<0):
        print((A[2]-A[0])*(A[3]-A[1])+(B[2]-B[0])*(B[3]-B[1]),2*(A[2]+A[3]-A[0]-A[1] + B[2]+B[3]-B[0]-B[1]))
    else:
        print((A[2]-A[0])*(A[3]-A[1])+(B[2]-B[0])*(B[3]-B[1])-(C[2]-C[0])*(C[3]-C[1]),2*(A[2]+A[3]-A[0]-A[1] + B[2]+B[3]-B[0]-B[1]-(C[2]+C[3]-C[0]-C[1])))