from tabnanny import check


T = int(input())

for ttt in range(T):
    flag=0
    arr = [list(map(int, input().split())) for _ in range(5)]
    ch = [[0]*5 for _ in range(5)]
    ch[2][2]=1
    nummap =  [0]*80
    for i in range(5):
        for j in range(5):
            nummap[arr[i][j]] = (i,j)
    numlist = list(map(int, input().split()))
    #print(numlist)
    nl = numlist.__len__()
    for i in range(nl):
        v = numlist[i]
        if(nummap[v]==0):
            continue
        else:
            x,y = nummap[v]
            #print(x,y)
            ch[x][y]=1
            if(ch[0][0] == 1 and ch[0][4]==1 and ch[4][0]==1 and ch[4][4]==1):
                print(i+1)
                break
            if( ch[x][0] *ch[x][1] *ch[x][2] *ch[x][3] *ch[x][4] ==1):
                print(i+1)
                break
            if( ch[0][y] *ch[1][y] *ch[2][y] *ch[3][y] *ch[4][y] ==1):
                print(i+1)
                break
            if( ch[0][0] *ch[1][1] *ch[2][2] *ch[3][3] *ch[4][4] ==1):
                print(i+1)
                break
            if( ch[4][0] *ch[3][1] *ch[2][2] *ch[1][3] *ch[0][4] ==1):
                print(i+1)
                break
            
