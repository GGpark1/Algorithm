import sys
import datetime

input = sys.stdin.readline
N, K = map(lambda x: int(x), input().split(' '))

start = 900
li = [0] * N * 3
li[0] = start
cnt = 1

for i in range(1, (N * 3)):
    if cnt == 3:
        li[i] = li[i-1] + 1080 + K
        cnt = 1
    else:
        li[i] = li[i-1] + 180
        cnt += 1

res_li = li[-4:]
res_dic = {}
for i in res_li:
    # print(str(datetime.timedelta(minutes=i)))
    day, time = str(datetime.timedelta(minutes=i)).split(',')
    day = int(day.split(' ')[0])
    hour, min, _ = time.split(':')
    hour = "0000" + hour.strip()
    time = hour[-2:] + ":" + min
    res_dic.setdefault(day, []).append(time)

print(len(res_dic[N-1]))
for hour in res_dic[N-1]:
    print(hour)

print(res_dic)
