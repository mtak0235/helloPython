#[2577]1차원 배열, 숫자의 개수
from unittest import result

a=int(input())
b=int(input())
c=int(input())
result=list(str(a*b*c)) #

for i in range(10):
    print(result.count(str(i)))