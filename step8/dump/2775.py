#[2775] step8, 부녀회장이 될테야 kipark
import sys

T = int(input())

for t in range(T):	
	k = int(input())
	n = int(input())

	arr = [[0 for col in range(n+1)] for row in range(k+1)]
	for i in range(1, n+1):
		arr[0][i] = i
	for i in range(1, k+1):
		for j in range(1, n+1):
			arr[i][j] = arr[i][j-1] + arr[i-1][j]
	print(arr[k][n])