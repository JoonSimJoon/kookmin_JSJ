

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
(*list_01,) = 1, 3, 4, 6
(*list_02,) = 2, 3, 5, 7, 8
res = merge(list_01, list_02)
print(res)