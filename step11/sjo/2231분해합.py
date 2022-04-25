# 1 ---------------------------------------------
n = int(input())

def sum_calculate(x):
    result = x
    while x > 0:
        result += x % 10
        x = x // 10
    return result

for i in range(n + 1):
    if sum_calculate(i) == n:
        print(i)
        break
    if i == n:
        print(0)

# 2 ---------------------------------------------
n = int(input())

for i in range(1, n + 1):
    num = sum(map(int, str(i)))
    num_sum = i + num
    if num_sum == n:
        print(i)
        break
    if i == n:
        print(0)