def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def merge(left, right):
    ret = []
    ln = left.__len__()
    rn = right.__len__()
    li,ri=0,0
    for i in range(ln+rn):
        if(li == ln or ri == rn):
            if(li == ln):
                ret.append(right[ri])
                ri+=1
            elif(ri ==rn):
                ret.append(left[li])
                li+=1
        elif(left[li]<right[ri]):
            ret.append(left[li])
            li+=1
        elif(right[ri]<=left[li]):
            ret.append(right[ri])
            ri+=1
    return ret

def sort_merge(list_):
    if(len(list_)==1): return list_
    left,right = split_list(list_)
    left = sort_merge(left)
    right = sort_merge(right)
    return merge(left, right)

(*data,) = 5, 7, -9, 3, -4, 2, 8
res = sort_merge(data)
print(data)
print(res)
