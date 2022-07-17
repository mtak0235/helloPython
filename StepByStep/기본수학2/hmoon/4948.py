def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if (sieve[i] == True):
            for j in range(i+i, n, i):
                sieve[j] = False
    return (sieve)
x = 123456*2
arr = prime_list(x)
while(True):
    ans = 0
    n = int(input())
    if n == 0:
        break
    for i in range(n+1,2*n):
        if arr[i] == True:
            ans+=1
    if(n == 1):
        ans = 1
    print(ans)
