#[2609]9370_수학, 최대공약수와 최공배수
import math

n, m =map(int, input().split())

print(math.gcd(n, m)) #최대공약수
print(math.lcm(n, m)) #최소공배수