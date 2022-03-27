# import sys
# def pplCnt(k,n):
#     if n == 0:
#         return 0
#     elif k == 0:
#         return n
#     else:
#         return pplCnt(k, n - 1) + pplCnt(k-1, n)

# sys.setrecursionlimit(10000)
# _testCase = int(sys.stdin.readline())
# for i in range(_testCase):
#     print(pplCnt(int(sys.stdin.readline()),int(sys.stdin.readline())))
import sys
for i in range(int(sys.stdin.readline())):
    f = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    f0 = [j for j in range(1,n + 1)]
    for k in range(f):
        for l in range(1,n):
            f0[l] += f0[l - 1]
    print(f0[-1])