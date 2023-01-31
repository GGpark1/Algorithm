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


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    # 무한으로 loop
    # 조건을 만족하면 break
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break

        min2 = heapq.heappop(scoville)

        new = min1 + (min2 * 2)
        heapq.heappush(scoville, new)
        answer += 1

    return answer
