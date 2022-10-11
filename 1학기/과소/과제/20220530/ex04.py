import traceback
try:
    data = input("Enter list of numbers: ")
    numbers = data.split()
    (*numbers,) = map(int, numbers)
    min_ = numbers[0]
    for val in numbers[1:]:
        if min_ > val:
            min_ = val
    print("Minimum value:", min_)
except:
    traceback.print_exc()