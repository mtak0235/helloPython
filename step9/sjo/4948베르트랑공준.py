def is_prime(x):
    if x == 1:
        return False 
    if x == 2 or x == 3:
        return True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

prime = []
result = []

for i in range(1, 246913):
    if is_prime(i):
        prime.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in prime:
        if n < i <= n * 2:
            count += 1
    result.append(count)

for i in range(len(result)):
    print(result[i])