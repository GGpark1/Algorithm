def solution(s):
    length = len(s)
    answer = ''
    evenOrNot = length % 2
    mid_idex = length // 2
    if evenOrNot == 0:
        answer = answer + s[mid_idex-1] + s[mid_idex]
    else:
        answer += s[mid_idex]
    return answer
