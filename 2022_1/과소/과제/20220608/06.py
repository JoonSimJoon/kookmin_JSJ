def merge(left, right):
    ret = []
    ln = left.__len__()
    rn = right.__len__()
    li,ri=0,0
    for i in range(ln+rn):
        if(left.empty()):
            y= right.pop()
            ret.append(y)
        elif(right.empty()):
            x= left.pop()
            ret.append(x)
        
(*list_01,) = 1, 3, 4, 6
(*list_02,) = 2, 3, 5, 7, 8
res = merge(list_01, list_02)
print(res)