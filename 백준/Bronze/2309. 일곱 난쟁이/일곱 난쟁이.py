from itertools import combinations

height_list = [int(input()) for _ in range(9)]

for height_combination in combinations(height_list, 7):
    if sum(height_combination) == 100:
        for height in sorted(height_combination):
            print(height)
            
        break