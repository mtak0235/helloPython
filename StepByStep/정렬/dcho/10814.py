# 10814

import sys

# 삽입 정렬은 시간초과가 뜸
#def insert_sort(array: list):
#	for i in range(1, len(array)):
#		for j in range(i):
#			if (array[i][0] < array[j][0]):
#				insert_idx(array, i, j)

#def insert_idx(array: list, target_idx: int, insert_idx: int):
#	insert_value = array[target_idx]
#	for i in range(target_idx, insert_idx, -1):
#		array[i] = array[i - 1]
#	array[insert_idx] = insert_value


n = int(sys.stdin.readline())
input_list: list = []

for i in range(n):
	input_list.append(list(sys.stdin.readline().split()))

input_list.sort(key=lambda x: int(x[0]))
# x[0], int(x[0]) 차이가 뭘까
# 문자는 ascii라서 ?
#input_list.sort(key=lambda x: x[0])
#insert_sort(input_list)


for i in range(n):
	print(input_list[i][0], input_list[i][1])


