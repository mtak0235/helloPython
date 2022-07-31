import math
from re import X

a, b = map(int, open(0).read().split())
print(math.gcd(a, b), a * b // math.gcd(a, b))