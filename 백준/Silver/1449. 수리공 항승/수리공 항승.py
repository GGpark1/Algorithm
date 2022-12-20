N, L = map(int, input().split())
leak_points = sorted(list(map(int, input().split())))

count = 1
start = leak_points[0]
end = start + L


for leak in leak_points[1:]:
    if leak in range(start, end):
        continue

    else:
        start = leak
        end = start + L
        count += 1

print(count)