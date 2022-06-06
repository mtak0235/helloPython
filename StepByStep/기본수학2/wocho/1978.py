import math

N = int(input())
nums = list(map(int, input().split()))

def is_prime(n):
    if n < 2:
        return False
    sq = int(math.sqrt(n))
    for i in range(2, sq + 1):
        if n % i == 0:
            return False
    return True

count = 0
for i in range(N):
    if is_prime(nums[i]):
        count += 1

print(count)