import sys

n = int(sys.stdin.readline())

i = 0
num = 1
while(num < n):
    i = i + 1
    num = num + (6 * i)
print(i+1)