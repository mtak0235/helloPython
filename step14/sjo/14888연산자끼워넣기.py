import sys

n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

maximum, minimum = -sys.maxsize - 1, sys.maxsize

def f(num, idx, add, sub, mul, div):
    global maximum, minimum
    if idx == n:
        maximum = max(maximum, num)
        minimum = min(minimum, num)
        return
    if add > 0:
        f(num + nums[idx], idx + 1, add - 1, sub, mul, div)
    if sub > 0:
        f(num - nums[idx], idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        f(num * nums[idx], idx + 1, add, sub, mul - 1, div)
    if div > 0:
        f(int(num / nums[idx]), idx + 1, add, sub, mul, div - 1)

f(nums[0], 1, operators[0], operators[1], operators[2], operators[3])
print(maximum)
print(minimum)