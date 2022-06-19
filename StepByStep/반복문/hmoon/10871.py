import sys

N, X = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

solves = []
for num in nums:
	if num < X:
		solves.append(str(num))

print(" ".join(solves))
