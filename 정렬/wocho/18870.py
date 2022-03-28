import sys
input = sys.stdin.readline

N = int(input())
points = list(map(int, input().split()))

copy = list(set(points))
copy.sort()

dic = dict()
for i, x in enumerate(copy):
    dic[x] = i

for i in range(N):
    points[i] = dic[points[i]]

print(*points)
