n = int(input())
arr = []

for i in range(2, n + 1):
    if n == 1:
        break
    while n % i == 0:
        arr.append(i)
        n /= i

for i in range(len(arr)):
    print(arr[i])