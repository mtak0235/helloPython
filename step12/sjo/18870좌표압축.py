import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s_arr = set(arr)
s_arr = sorted(s_arr)

dic = {s_arr[i]:i for i in range(len(s_arr))}

for i in arr:
    print(dic[i], end=' ')