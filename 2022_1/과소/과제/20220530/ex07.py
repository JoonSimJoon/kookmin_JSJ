import traceback

def find_max(numbers):
    iter=0
    idx=0
    max_ = numbers[0]

    for val in numbers:
        if max_ < val:
            max_ = val
            idx=iter
        iter+=1
    return idx

try:
    data = input("Enter list of numbers: ")
    (*numbers,) = map(int, data.split())
    max_index = find_max(numbers)
    print(f"Maximum index: {max_index}, value: {numbers[max_index]}")
except:
    traceback.print_exc()