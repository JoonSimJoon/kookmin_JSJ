y,m,d = map(int,input().split())
cnt = 0
m_cnt = [31,28,31,30,31,31,31,31,30,31,30,31]

for i in range(1,y):
    if ((i%4==0) and (i%100 !=0 )) or i%400==0:
        cnt+=366
    else:
        cnt += 365

if ((y%4==0) and (y%100 !=0 )) or y%400==0:
    m_cnt[1]=29

for i in range (m-1):
    cnt+=m_cnt[i]

cnt+=d

cnt-=1
cnt=cnt%7
if(cnt==0):
    print("월요일")
elif(cnt==1):
    print("화요일")
elif(cnt==2):
    print("수요일")
elif(cnt==3):
    print("목요일")
elif(cnt==4):
    print("금요일")
elif(cnt==5):
    print("토요일")
elif(cnt==6):
    print("일요일")