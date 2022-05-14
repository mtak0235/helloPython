import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def pow31(i):
	a = 1
	for _ in range(i):
		a = (a * 31)
	return a

t = int(input())
n = list(input().rstrip())
ans = []
for i in range(t):
	ans.append(((ord(n[i]) - 96) * pow31(i)) % 1234567891)
print(sum(ans) % 1234567891)