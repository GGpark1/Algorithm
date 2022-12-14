from collections import deque

T = int(input())

num_list = deque(range(1, T+1))

while len(num_list) != 1:
    num_list.popleft()
    top = num_list.popleft()
    num_list.append(top)

print(num_list[0])