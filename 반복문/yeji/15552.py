#[15552]반복문, 빠른 A+B
import sys
case = int(sys.stdin.readline())
for i in range(case):
    a, b = map(int,sys.stdin.readline().split())
    print (a+b)
    