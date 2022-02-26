# 분수찾기 step8
import sys

n = int(input())
sum = 0
i = 1
while(1):
    if(sum + i >= n):
        break
    sum = sum + i
    i += 1
    
x = n-sum
y = i+1-x
if(i % 2 == 0):
    print(str(x)+"/"+str(y))
else:
    print(str(y)+"/"+str(x))
    
