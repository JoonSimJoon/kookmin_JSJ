t = int(input())

for i in range(t):
    n, k = map(int,input().split())
    c = list(map(int,input().split()))
    for ttt in range(k):

        tmp = c.copy()
        for j in range(n):
            if j == 0 :
                #print(c[j+1])
                if c[j+1] < 3 or c[j+1]> 7:
                    tmp[j] -= 1
                elif c[j+1] == 3:
                    tmp[j] += 0
                else:
                    tmp[0] += 1


            elif j == n-1 :
                #print(c[j-1])
                if c[j-1] < 3 or c[j-1] > 7:
                    tmp[j] -= 1
                elif c[j-1] == 3:
                    tmp[j] += 0
                else:
                    tmp[j] += 1


            else:
                #print(c[j-1],c[j+1])
                if c[j-1]+c[j+1] < 3 or c[j-1] + c[j+1] > 7:
                    tmp[j] -= 1
                elif c[j-1] + c[j+1] == 3:
                    #print(tmp[j])
                    tmp[j] += 0
                    #print(tmp[j])
                else:
                    tmp[j] += 1
            if(tmp[j]>9): tmp[j]-=1
            if(tmp[j]<0): tmp[j]+=1
        c= tmp.copy()
    for v in c:
        print(v,end=" ")