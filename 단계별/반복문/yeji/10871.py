#[10871]반복문, x보다 작은 수

N, X = map(int, input().split())
A = input().split()
for i in A:
    if i < X:
        print(i, end=" ")