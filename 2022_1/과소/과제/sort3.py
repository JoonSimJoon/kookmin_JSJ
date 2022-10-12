N = int(input())
for i in range(N):
    a,b,c = map(int,input().split())
    if(a<=b and a<=c):
        print(a,end=" ")
        if(b<=c):
            print(b,c)
        else:
            print(c,b)
    elif(b<=a and b<=c):
        print(b,end=" ")
        if(a<=c):
            print(a,c)
        else:
            print(c,a)
    else:
        print(c,end=" ")
        if(b<=a):
            print(b,a)
        else:
            print(a,b)