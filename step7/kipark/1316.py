import sys

N = int(input())

result = 0

for i in range(N):
	arr = input()
	group_checker = 0
	for i in range(0, len(arr)):
		for j in range(i+1, len(arr)):
			if(arr[i] == arr[j]) and (arr[i] != arr[j-1]):
				group_checker = 1
	if(group_checker == 0):
		result += 1
print(result)