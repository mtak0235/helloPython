#[10989] step12, 수 정렬하기 3 kipark
import sys

n = int(input())
nlist = [0] * 10001 

for n in range(n):
	nlist[int(sys.stdin.readline())] += 1

for i in range(0, 10001):
	for j in range(nlist[i]):
			print(i)
