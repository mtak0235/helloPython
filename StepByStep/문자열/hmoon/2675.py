# 문자열 반복
import sys

for i in range(int(sys.stdin.readline())):
    ret = []
    count, words = sys.stdin.readline().strip().split()
    words = list(map(str, words))
    for j in words:
        ret.append(j * int(count))
    print(*ret, sep='')
