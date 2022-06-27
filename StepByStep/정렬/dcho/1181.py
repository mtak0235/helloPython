# 1181

import sys

n = int(sys.stdin.readline())
input_set: set = set()
for i in range(n):
	s = sys.stdin.readline().strip('\n')
	input_set.add(s)

res_list:list = list(input_set)

res_list.sort()
res_list.sort(key=len)

s = "\n".join(res_list)
print(s)
