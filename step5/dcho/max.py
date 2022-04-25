# 2562

import sys

numbers = []
for i in range(0, 9):
	numbers.append(int(sys.stdin.readline()))
maxValue = max(numbers)
print('{a}\n{b}'.format(a = maxValue, b = numbers.index(maxValue) + 1))