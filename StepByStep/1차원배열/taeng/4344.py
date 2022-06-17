#
#
#

import sys

C = int(input())
for i in range(C):
    line = sys.stdin.readline().strip().split()
    scores = list(map(int, line[1:]))
    tot = sum(scores)
    avg = tot / len(scores)
    cnt = 0
    for score in scores:
        if score > avg:
            cnt += 1
    print( '%.3f'%round(cnt / len(scores) * 100, 4)+'%')


