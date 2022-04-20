import sys
import array as arr

sys.stdin.readline()
numbers = arr.array('i', map(int, sys.stdin.readline().split()))
print(min(numbers), max(numbers))
