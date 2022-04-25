#[11653] step9, 소인수분해 kipark
import math
import sys

n = int(input())

while(1):
    before_n = n
    for i in range(2, n+1):
        if n % i == 0:
            print(i)
            n = int(n / i)
            break
    if before_n == n or n == 1:
        break