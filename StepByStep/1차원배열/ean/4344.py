import sys
import array as arr

C = int(sys.stdin.readline())
for i in range(C):
    a = arr.array('i', map(int, sys.stdin.readline().split()))
    N = a[0]
    del a[0]
    avg = sum(a) / N
    count = 0
    for j in range(N):
        if a[j] > avg:
            count += 1
    print(f"{count * 100 / N:.3f}%")
