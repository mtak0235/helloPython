n = int(input())

for _ in range(n):
    num = list(map(int, input().split()))
    l = num[0]
    av = sum(num[1:]) / l
    count = 0
    for i in range(1, l + 1):
        if (num[i] > av):
            count += 1
    print("{:.3f}%".format((count/l)*100))