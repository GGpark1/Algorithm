import heapq
import sys

hq = []
N = int(sys.stdin.readline())


for _ in range(N):

    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(hq, (abs(x), x))

    else:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
