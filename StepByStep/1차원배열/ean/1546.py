import sys
import array as arr

N = int(sys.stdin.readline())
scores = arr.array('i', map(int, sys.stdin.readline().split()))
print(sum(scores) * 100 / (max(scores) * N))
