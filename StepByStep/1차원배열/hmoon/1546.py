import sys

n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))

newscore = []
for i in range(0, len(score)):
	newscore.append(score[i] / max(score) * 100)

print(sum(newscore) / n)
