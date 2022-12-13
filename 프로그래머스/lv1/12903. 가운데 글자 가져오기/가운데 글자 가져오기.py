def solution(s):
    length = len(s)
    li = list(s)
    answer = ''
    mid = length % 2
    if mid == 0:
        mid = length // 2
        answer = answer + li[mid-1] + li[mid]
    else:
        mid = length // 2
        answer += li[mid]
    return answer