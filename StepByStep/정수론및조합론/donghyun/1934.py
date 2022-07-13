import math

l=open(0).read().strip().split("\n")[1:]
for i, j in map(str.split, l):
    i, j = int(i), int(j)
    print(i * j // math.gcd(i, j))