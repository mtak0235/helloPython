n = int(input())
arr = list(map(int, input().split()))

def is_prime(x):
    if x == 1:
        return False 
    if x == 2 or x == 3:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

count = 0

for i in range(n):
    if is_prime(arr[i]):
        count += 1

print(count)