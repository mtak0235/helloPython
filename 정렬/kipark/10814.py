#[10814] step12, 나이순 정렬 kipark
import sys

n = int(input())
nlist = []

for i in range(n):
	age, name = map(str, input().split())
	nlist.append((int(age), name))
	
nlist.sort(key = lambda item : item[0])

for member in nlist:
	print(member[0], member[1])