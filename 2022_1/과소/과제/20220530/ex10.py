import traceback
try:
    num= str(input("Enter list of numbers: "))
    cnt=0   
    for v in num:
        cnt+=int(v)
    print(cnt)
except:
    traceback.print_exc()