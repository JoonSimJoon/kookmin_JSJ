def search(list_, target):
    idx = 0
    for i in list_:
        if i==target:
            break
        else:
            idx+=1
    return idx
(*data,) = 1, 3, 5, 4, 7, 8, 6
n = 7
res = search(data, n)
print(res, data[res])
