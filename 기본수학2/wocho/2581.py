import math

M = int(input())
N = int(input())

def is_prime(n):
    if n < 2:
        return False
    sq = int(math.sqrt(n))
    for i in range(2, sq + 1):
        if n % i == 0:
            return False
    return True

min_prime = -1
s = 0
for i in range(M, N + 1):
    if is_prime(i):
        if min_prime == -1:
            min_prime = i
        s += i
        
if (s != 0):
    print(s)
print(min_prime)