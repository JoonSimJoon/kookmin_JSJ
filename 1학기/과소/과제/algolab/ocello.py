from operator import truediv


T = int(input())

dx = [0,1,-1,0,1,-1,-1,1]
dy = [1,0,0,-1,1,1,-1,-1]
#white = 1, black = -1, none = 0
for ttt in range(T):
    arr = [[0]*8 for _ in range(8)]
    arr[3][3]=1
    arr[4][4]=1
    arr[3][4]=-1
    arr[4][3]=-1
    q = int(input())
    for k in range(q):
        a,b = map(int,input().split())
        a-=1
        b-=1
        re = []
        if(int(k%2)==0):
            arr[a][b]=-1
            #find -1
            for i in range(8):
                nx = a + dx[i]
                ny = b + dy[i]
                re = []
                while True:
                    if nx<0 or ny<0 or nx>7 or ny>7:
                        re = []
                        break
                    if arr[nx][ny] ==0:
                        re = []
                        break
                    if arr[nx][ny]==-1:
                        break
                    else: 
                        re.append((nx,ny))
                    nx+=dx[i]
                    ny+=dy[i]
                for cx,cy in re:
                    arr[cx][cy]*=-1
        else:
            arr[a][b]=1
            for i in range(8):
                nx = a + dx[i]
                ny = b + dy[i]
                re = []
                while True:
                    if nx<0 or ny<0 or nx>7 or ny>7:
                        re = []
                        break
                    if arr[nx][ny] ==0:
                        re = []
                        break
                    if arr[nx][ny]==1:
                        break
                    else: 
                        re.append((nx,ny))
                    nx+=dx[i]
                    ny+=dy[i]
                for cx,cy in re:
                    arr[cx][cy]*=-1
    ac=0
    bc=0
    for i in range(8):
        for j in range(8):
            if(arr[i][j]==1): ac+=1
            elif(arr[i][j]): bc+=1
    print(bc,ac)
    for i in range(8):
        for j in range(8):
            if(arr[i][j]==0):
                print("+",end="")
            if(arr[i][j]==1):
                print("O",end="")
            if(arr[i][j]==-1):
                print("X",end="")
        print("")