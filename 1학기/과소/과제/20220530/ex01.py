data = input("Enter list of numbers: ")
numbers = data.split()
# numbers = [int(i) for i in numbers]
*numbers, = map(int, numbers)
min_ = 999999
for val in numbers:
    if min_ > val:
        min_ = val
print("Minimum value:", min_)
