import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result_arr = list()
max_score = max(arr)

for i in range(len(arr)):
	result_arr.append(arr[i] / max_score * 100)

print(sum(result_arr) / n)
