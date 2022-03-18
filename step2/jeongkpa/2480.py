A, B, C = map(int, input().split())

if (A == B == C):
    print(10000+ 1000*A)
    exit(0)
elif (A == B):
    print(1000 + 100 * A)
elif (B == C):
    print(1000 + 100 * B)
elif (C == A):
    print(1000 + 100 * C)
else:
    M = max(A,B,C)
    print(M * 100)
