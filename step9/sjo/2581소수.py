m = int(input())
n = int(input())
arr = []

def is_prime(x):
    if x == 1:
        return False 
    if x == 2 or x == 3:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in range(m, n + 1):
    if is_prime(i):
        arr.append(i)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))