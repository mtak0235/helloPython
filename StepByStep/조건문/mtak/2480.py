import sys
a = list(map(int, sys.stdin.readline().split()))
count = [0] * (max(a) + 1)
for i in range(3):
    count[a[i]] += 1
flag = 0
for idx, i in enumerate(count):
    if i == 3:
        print(10000 + 1000 * idx)
        flag += 1
        break
    elif i == 2:
        print(1000 + 100 * idx)
        flag += 1
        break
if flag != 1:
    print(max(a) * 100)
