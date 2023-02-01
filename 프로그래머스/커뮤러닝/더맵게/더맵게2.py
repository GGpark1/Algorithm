import heapq


def solution(scoville, K):

    heapq.heapify(scoville)
    cnt = 0
    while len(scoville) > 1:
        h1 = heapq.heappop(scoville)
        if h1 < K:
            h2 = heapq.heappop(scoville)
            new = h1 + (2 * h2)
            heapq.heappush(scoville, new)
            cnt += 1
        else:
            return cnt

        if scoville[-1] < K:
            return -1
        else:
            return cnt


li = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(li, k))
