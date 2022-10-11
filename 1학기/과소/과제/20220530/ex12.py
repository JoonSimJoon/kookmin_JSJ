import traceback

def solution(lst):
    freq = {x:lst.count(x) for x in set(lst)}
    if len(freq) == 1 or len(freq) == len(lst):
        return []
    else:
        return [x for x in freq.keys() if freq[x] == max(freq.value())]

try:
    print(solution([1,2,3,4,4]))
except:
    traceback.print_exc()