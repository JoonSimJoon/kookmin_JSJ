import traceback
try:
    num= int(input("Enter list of numbers: "))
    cnt=0   
    while(num>0):
        cnt+=(num%10)
        num=int(num/10)
    print(cnt)
except:
    traceback.print_exc()