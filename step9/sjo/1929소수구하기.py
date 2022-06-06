m, n = map(int, input().split())

def is_prime(x):
    if x == 1:
        return False 
    if x == 2 or x == 3:
        return True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

for i in range(m, n + 1):
    if is_prime(i):
        print(i)
        