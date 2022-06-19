# [14425] 집합과맵, 문자열 집합
#
#


import sys

N, M = map(int, input().split())
S = set([sys.stdin.readline().strip() for i in range(N)])
print(len([0 for i in range(M) if sys.stdin.readline().strip() in S]))
