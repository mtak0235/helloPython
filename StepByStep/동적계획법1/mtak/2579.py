import sys
input = sys.stdin.readline
cnt = int(input())
s = [int(input()) for _ in range(cnt)]

if cnt > 3 :
	res = [s[0], max(s[0], 0)+ s[1], max(s[0], s[1]) + s[2]] 
	for i in range(3, cnt):
		res.append(max(res[i - 2], s[i - 1] + res[i - 3]) + s[i])
	print(res[cnt - 1])
elif cnt == 2:
    print(max(s[0], 0)+ s[1])
elif cnt == 3:
    print(max(s[0], s[1]) + s[2])
else:
    print(s[0])