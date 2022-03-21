import sys

#한 줄을 입력받은 값으로 리스트를 만들어보자
N, X = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

for i in range(0, N):
    if lst[i] < X:
        print(lst[i], end=" ")