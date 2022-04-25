import sys

sys.setrecursionlimit(100000)

result_count = 0

def hansu(a: int, N: int):
	if (a > N):
		return
	words = str(N)
	for i in range(len(str(N))-1):
		if(words[i+1] > words[i]):
			if(i == len(str) - 2):
				result_count += 1
				break
	hansu(a + 1, N)

N = int(input())
hansu(1, N)
print(result_count)
