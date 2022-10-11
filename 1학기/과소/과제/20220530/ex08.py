import traceback
try:
    num= int(input("Enter list of numbers: "))
    cnt=0   
    ncnt=0
    nnum = num
    while(nnum>0):
        ncnt+=1
        nnum=int(nnum/10)
    for i in range(ncnt):
        cnt+=(num%10)
        num=int(num/10)
    print(cnt)
except:
    traceback.print_exc()