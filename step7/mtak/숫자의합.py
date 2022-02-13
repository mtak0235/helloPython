import sys
_cnt  = int(sys.stdin.readline())
while _cnt > 0:
    _cnt-=1
_sum = 0
_lst = sys.stdin.readline().strip()
for i in range(len(_lst)):
    _sum += int(_lst[i])
print(_sum)
