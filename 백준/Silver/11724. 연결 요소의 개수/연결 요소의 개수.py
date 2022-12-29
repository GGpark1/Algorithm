import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(lambda x: int(x), input().split())

node_map = [[0]*N for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    node_map[a][b] = node_map[b][a] = 1

check_list = [False] * N
cnt = 0


def dfs(now):
    for nxt in range(N):
        if (node_map[now][nxt]) and (not check_list[nxt]):
            global cnt
            check_list[nxt] = True
            dfs(nxt)


for i in range(N):
    if not check_list[i]:
        check_list[i] = True
        cnt += 1
        dfs(i)

print(cnt)
