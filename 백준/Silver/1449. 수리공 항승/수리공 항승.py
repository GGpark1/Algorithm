N, L = map(int, input().split())
leak_points = sorted(list(map(int, input().split())))

loc = [False] * 1001
count = 0
start = 0

for leak_point in leak_points:
    loc[leak_point] = True

while start < 1001:
    if loc[start]:
        count += 1
        start += L
    else:
        start += 1

print(count)