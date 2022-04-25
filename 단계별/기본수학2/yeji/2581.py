#[2581]step9,소수
# M이상 N이하의 자연수 중 소수인 것을 모두 골라 합과 최솟값 출력

m=int(input())
n=int(input())
sosu=[]

for num in range(m, n+1):
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 num-1까지
            if num % i == 0:
                error += 1
                break  # 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
        if error == 0:
            sosu.append(num)  # error가 없으면 소수리스트에 추가
            
if len(sosu) > 0 :
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)