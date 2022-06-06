import sys
import array as arr

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
result = arr.array('b', map(int, str(a * b * c)))
for i in range(10):
    print(result.count(i))
