#[2798]step11, 블랙잭
#N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력

m, n=map(int, input().split()) 
card=list(map(int, input().split())) #카드 리스트 입력받기
result=0 
for i in range(n):
    for j in range(j+1, n):
        for k in range(j+1, n):
            if card[i]+card[j]+card[k]>m: #세 카드의 값이 m보다 크먄 계속
                continue
            else:
                result=max(result, card[i]+card[j]+card[k]) #m보다 크지 않으면 result에 저장됨. 저장된 수 중 가장 큰 수가 result가 됨.
print(result)
#런타임에러님