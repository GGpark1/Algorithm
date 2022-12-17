N, K = map(lambda x: int(x), input().split())

coins = []

for _ in range(N):
    coin = int(input())
    if K // coin != 0:
        coins.append(coin)

coins.sort(reverse=True)

count = 0

for coin in coins:
    divide = K // coin
    remain = K % coin
    if K >= coin:
        if remain == 0:
            count += divide
            break
        else:
            count += divide
            K = remain


print(count)
