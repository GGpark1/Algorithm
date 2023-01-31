def solution(n, lost, reserve):
    n = [1] * (n + 2)
    for i in reserve:
        n[i] += 1
    for i in lost:
        n[i] -= 1
    for i in range(1, len(n)):
        if n[i] >= 2 and n[i-1] == 0:
            n[i] -= 1
            n[i-1] += 1
        if n[i] >= 2 and n[i+1] == 0:
            n[i] -= 1
            n[i+1] += 1

    answer = len([i for i in n if i != 0]) - 2
    return answer


n = 5
lost = [2, 4]
reserve = [3]

print(solution(n, lost, reserve))
