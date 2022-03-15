#[2869] step8, 달팽이는 올라가고 싶다. kipark
import sys
import math

a, b, v = map(int, input().split())

print((math.ceil((v-a)/(a-b))) + 1)