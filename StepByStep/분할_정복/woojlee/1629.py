# 곱셈
# 분할 정복

# A^B % C == A^(B//2)^2 % C(B는 짝수) or A^(B//2)^2*A(B는 홀수) % C
def solve(a, b, c):
    if b == 1:
        return a % c
    temp = solve(a, b//2, c)
    if b % 2 == 0:
        return (temp**2) % c
    else:
        return (temp**2) * a % c

A, B, C = map(int, input().split())
print(solve(A, B, C))