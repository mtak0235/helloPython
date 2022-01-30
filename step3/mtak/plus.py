import sys
case_cnt = int(sys.stdin.readline())
for i in range(case_cnt):
	(a,b) = map(int, sys.stdin.readline().split())
	print("Case #%d: %d"%(i+1,a+b))