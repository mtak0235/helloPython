N = int(input())

answer = -1
n = N // 5
for i in range(n, -1, -1):
	if (N - 5 * i) % 3:
		continue
	else:
		answer = i + (N - 5 * i) // 3
		break
print(answer)