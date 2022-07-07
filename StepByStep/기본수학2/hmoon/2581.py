M = int(input())
N = int(input())
prime = []
for i in range(M, N+1):
    if i != 1:
        check = True
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        if check:
            prime.append(i)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])
