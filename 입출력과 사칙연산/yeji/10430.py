#[10430]step1,나머지
A, B, C= map(int, input().split())
print ((A+B)%C)
print (((A%C) + (B%C))%C)
print ((A*B)%C)
print (((A%C) * (B%C))%C)