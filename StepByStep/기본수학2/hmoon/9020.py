def is_prime(a):
    for i in range(2, int(pow(a, 0.5)) + 1):
        if a % i == 0:
            return False
    if a == 1:
        return False
    return True


t = int(input())

for i in range(t):
    n = int(input())
    for a in range(n // 2, 0, -1):
        if is_prime(a) and is_prime(n - a):
            print(a, n - a)
            break
