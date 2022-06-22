import sys

cnt = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
max = max(scores)

for i in range(len(scores)) :
	scores[i] = scores[i] / max * 100
avg = sum(scores) / cnt
print(avg)
