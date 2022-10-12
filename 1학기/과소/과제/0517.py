from sys import flags


N = int(input())

for i in range(N):
    s = str(input())
    l = s.__len__()
    flag=1
    for i in range(l):
        x= (s[i])
        if (x>='A' and x<='Z') or (x>='a' and x<='z') or (x>='0' and x<='9') or x=='_':
            if(i==0 and (x>='0' and x<='9')):
                flag = 0
                break
        else:
            flag=0
            break
    print(flag)

   