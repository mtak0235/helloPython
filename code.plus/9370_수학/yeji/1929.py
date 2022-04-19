#[1929]9370_수학,소수하기
#M이상 N이하의 소수 출력

m, n =map(int, input().split())

for i in range(m, n+1):
    if i == 1: 
        continue
    for j in range(2, int(i** 0.5)+1 ):
        if i%j==0:
            break
    else:
        print(i)