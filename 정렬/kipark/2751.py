#[2751] step9, 수 정렬하기 2 kipark
import sys

n = int(input())
n_list = []
for i in range(n):
    n_list.append(int(sys.stdin.readline()))
n_list.sort()

for i in n_list:
    print(i)