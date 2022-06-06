import sys
import array as arr

numbers = arr.array('i', map(int, sys.stdin.read().split()))
M = max(numbers)
print(M)
print(numbers.index(M) + 1)
