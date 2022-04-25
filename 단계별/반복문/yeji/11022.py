#[11022]반복문, A+B - 8
t = int(input())
for i in range(1,t+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}') #