import sys
n = int(sys.stdin.readline())
times = []
entireTime=0
times = list(map(int, sys.stdin.readline().rstrip().split()))
times.sort()
for i in range(len(times)):
    entireTime += times[i] * (len(times) - (i))
print(entireTime)