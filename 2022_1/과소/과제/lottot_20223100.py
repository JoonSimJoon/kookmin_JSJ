import random

answer = ""
'''a = list(range(1,46))
random.shuffle(a)

for i in range(5):
    if(a[i]<10):
        answer = answer + "0" + str(a[i])
    else:
        answer = answer+ str(a[i])
'''

for i in range(5):
    while True:
        flag=1
        rand_num = random.randrange(1,46)
        for j in range(i):
            cp_num = int(answer[j*2:j*2+2])
            if cp_num == rand_num:
                flag=0
        if flag==1 :
            break
    if(rand_num<10):
        answer = answer + "0" + str(rand_num)
    else:
        answer = answer+ str(rand_num)


for i in range(5):
    print(answer[i*2:i*2+2],end=' ')


    