import sys

n = int(sys.stdin.readline())
line = sys.stdin.readline()
sum = 0
for i in range(n):
    sum += int(line[i])
print(sum)
