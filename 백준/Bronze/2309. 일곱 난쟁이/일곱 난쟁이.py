from itertools import combinations

height_list = []

for _ in range(9):
    height = int(input())
    height_list.append(height)


for height_combination in combinations(height_list, 7):
    if sum(height_combination) == 100:
        height_combination = list(height_combination)
        break

height_combination.sort()

for height in height_combination:
    print(height)
