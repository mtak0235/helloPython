import sys
n = int(sys.stdin.readline())
dists = list(map(int, sys.stdin.readline().rstrip().split()))
prices = list(map(int, sys.stdin.readline().rstrip().split()))
totalPrice = 0
i = 0
while (i < n - 1):
    for j in range(i + 1, n):
        if (prices[i] > prices[j]):
            break;
    totalPrice += prices[i] * sum(dists[i:j])
    i = j
print(totalPrice)