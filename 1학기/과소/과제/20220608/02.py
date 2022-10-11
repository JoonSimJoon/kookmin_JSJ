def search(arr, target,l,u  ):
    if(arr[u]==target): return u
    elif(arr[l]==target): return l
    elif(l==u): return -1
    return search(arr, target, l + 1, u - 1)

(*data,) = 1, 3, 5, 4, 7, 8, 6
n = 7
res = search(data, n, 0, len(data) - 1)
print(res, data[res])
