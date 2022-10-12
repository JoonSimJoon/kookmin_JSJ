def solution(lst):
    num = 1
    cnt = 1
    l = len(lst)
    answer = []
    lst.sort()
    for i in range(0,l):
        if i==0:
            continue
        elif lst[i]==lst[i-1]:
            cnt+=1
            if(cnt>num):
                answer.clear()
                answer.append(lst[i])
                num=cnt
            elif cnt==num:
                answer.append(lst[i])
        else:
            cnt=1
    return answer

print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) #[]
