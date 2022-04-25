def is_prime(x):
    if x == 1:
        return False
    elif x == 2 or x == 3:
        return True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

prime = []

for i in range(2, 10000):
    if is_prime(i):
        prime.append(i)

t = int(input())

for _ in range(t):
    n = int(input())
    if n // 2 in prime:
        print(n // 2, n // 2, sep=' ')
    else:
        for i in range(n // 2 - 1, 2, -1):
            if i in prime:
                if n - i in prime:
                    print(i, n - i, sep=' ')
                    break