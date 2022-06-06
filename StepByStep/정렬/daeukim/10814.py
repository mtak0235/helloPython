# 나이순 정렬
n = int(input())

lst = []
for _ in range(n):
	tmp = []
	age, name = input().split()
	tmp.append(int(age))
	tmp.append(name)
	lst.append(tmp)
lst.sort(key=lambda x : x[0])
for i in lst:
	print(str(i[0]), i[1])
