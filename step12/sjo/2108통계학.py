import sys
from collections import Counter

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()
print(round(sum(arr) / n))  # 산술평균
print(arr[n // 2])  # 중앙값
# 최빈값
cnt_arr = Counter(arr).most_common()
if len(cnt_arr) > 1 and cnt_arr[0][1] == cnt_arr[1][1]:
    print(cnt_arr[1][0])
else:
    print(cnt_arr[0][0])
print(arr[n - 1] - arr[0])  # 범위