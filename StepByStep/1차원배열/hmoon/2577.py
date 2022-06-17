import sys
from functools import reduce

nums = []

for i in range(0, 3):
    nums.append(int(sys.stdin.readline()))

multiply = list(str(reduce(lambda x, y: x * y, nums)))

for i in range(0, 10):
    cnt = 0
    cnt = multiply.count(str(i))
    print(cnt)
