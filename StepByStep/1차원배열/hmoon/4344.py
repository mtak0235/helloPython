import sys
import copy

for i in range(int(sys.stdin.readline())):
    solve = list(map(int, sys.stdin.readline().strip().split()))
    score = copy.deepcopy(solve[1:])
    avg = sum(score) / len(score)
    cnt = 0
    for i in range(0, len(score)):
        if score[i] > avg:
            cnt += 1
    print("%.3f%%" % round(cnt / len(score) * 100, 4))
