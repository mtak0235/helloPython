import sys

input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
	arr = input().split()
	temp = []
	for j in range(len(arr[1])):
		for _ in range(int(arr[0])):
			temp.append(arr[1][j])
	lst.append(''.join(temp))
print('\n'.join(lst))