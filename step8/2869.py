#[2869] step8, 달팽이는 올라가고 싶다. kipark
import sys

a, b, v = map(int, input().split())

if(a <= b):
	print("0")
elif(v - a <= 0):
	print("1")
else:
	v = v - a
	print(((a-b)/v) + 2)