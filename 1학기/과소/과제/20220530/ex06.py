import traceback
try:
    data = input("Enter list of numbers: ")
    numbers = map(int, data.split())
    min_ = next(numbers)
    iter=0
    idx=0
    for val in numbers:
        if min_ > val:
            min_ = val
            idx=iter
        iter+=1
    print("Minimum value:", min_,idx)
except:
    traceback.print_exc()
