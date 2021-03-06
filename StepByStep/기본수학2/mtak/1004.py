import sys
import math
input = sys.stdin.readline
cases_cnt = int(input())
def is_in_sector(sector, f, t):
    disf = math.sqrt(pow(f[0] - sector[0], 2) + pow(f[1] - sector[1], 2))
    dist = math.sqrt(pow(t[0] - sector[0], 2) + pow(t[1] - sector[1], 2))
    ret = 0
    if disf <= sector[2]:
        ret += 1
    if dist <= sector[2]:
        ret += 1
    return 1 if (ret == 2 or ret == 1) else 0 
for i in range(cases_cnt):
    spots = list(map(int, input().split()))
    trick_cnt = int(input())
    tricks = []
    cnt = 0
    for _ in range(trick_cnt):
        tricks.append(list(map(int, input().split())))
    for i in tricks:
        cnt +=  is_in_sector(i,spots[0:2], spots[2:4])
    print(cnt)
