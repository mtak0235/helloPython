import sys
case_cnt = int(sys.stdin.readline())
for i in range(case_cnt):
	(_a,_b) = map(int, sys.stdin.readline().split())
	print("Case #{index}: {a} + {b} = {sum}".format(index = i+1,a = _a,b = _b, sum = _a+_b))