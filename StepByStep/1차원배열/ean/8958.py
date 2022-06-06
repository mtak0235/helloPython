import sys
import array as arr

def euler(n):
    return n * (n + 1) // 2

T = int(sys.stdin.readline())
for i in range(T):
    m = arr.array('i', map(len, sys.stdin.readline().replace('X', ' ').split()))
    print(sum(map(euler, m)))
