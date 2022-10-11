def solution(lst):
    answer = []
    temp = set()
    #print(temp)
    answer = [x for x in lst if x in temp or (temp.add(x) or False)]
    # for x in lst:
    #     if x in temp:
    #         print(temp)
    #         answer.append(x)
    #     else:
    #         temp.add(x)
    return answer
print(solution([1,2,3,4,5,5])) #[5]
print(solution([12,17,19,17,23,17,17])) #[17]
print(solution([26,37,26,37,91])) #[26, 37]
print(solution([28,30,32,34,144])) #[]
