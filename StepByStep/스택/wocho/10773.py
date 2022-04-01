import sys
input = sys.stdin.readline

N = int(input())

lst = []
for _ in range(N):
    temp = input()
    if temp == "0\n":
        lst.pop(-1)
    else:
        lst.append(int(temp))

print(sum(lst))