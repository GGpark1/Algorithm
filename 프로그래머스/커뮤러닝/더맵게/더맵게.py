import heapq


def solution(scoville, K):
    cnt = 0
    hq = scoville
    while len(hq) != 1:
        if scoville[0] < K:
            first = heapq.heappop(hq)
            second = heapq.heappop(hq)
            new = first + (second * 2)
            heapq.heappush(hq, new)
            cnt += 1
        else:
            return cnt

    if scoville[-1] < K:
        return -1
    else:
        return cnt


scoville = [1, 2, 3, 9, 10, 12]
k = 100
print(solution(scoville, k))
