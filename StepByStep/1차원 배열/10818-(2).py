import sys

cnt = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

print(min(numbers), max(numbers))
