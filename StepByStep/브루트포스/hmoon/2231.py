num = int(input())

for i in range(1, num + 1):
    arr = list(map(int, str(i)))
    _sum = i + sum(arr)
    if _sum == num:
        print(i)
        break
    if i == num:
        print(0)
        break
