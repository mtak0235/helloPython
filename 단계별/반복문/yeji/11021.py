#[11021]반복문, A+B - 7
t = int(input())
for i in range(1,t+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a+b}') #""은 틀렸다고 나옴
    
