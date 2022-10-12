N = int(input())

for ttt in range(N):
    a,b = map(int,input().split())
    arr= []
    arr.append(0)
    x=(list(map(int,input().split())))
    for v in x:
        arr.append(v)
    arr.append(0)
   # print(arr)
    for i in range(b):
        brr=arr.copy()
        for j in range(1,a+1):
            x = arr[j-1] + arr[j+1]
            #print(x,arr[j-1],arr[j+1])
            brr[j]=arr[j]
            if(x==3):
                continue
            elif((x<3 or x>7) and arr[j]!=0):
                brr[j]-=1
            elif((x>3 and x<8) and arr[j]<9):
                brr[j]+=1
        arr=brr.copy()
    for i in range(1,a+1):
        print(arr[i],end=" ")
    print("")
        