#[1427] step12, 소트인사이드 kipark
import sys

n = input()
nlist = []

for i in str(n):
	nlist.append(i)

nlist.sort(reverse=True)

for i in nlist:
	print(i, end='')