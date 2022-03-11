#[1978]step9,소수 찾기
#주어진 수들 중 소수의 개수를 출력

n=int(input()) #수의 개수
nums=list(map(int, input().split()))
p = 0
for i in nums:
    cnt = 0
    if (i==1):
        continue
    for j in range(2, i+1):  # 2부터 n-1까지
        if i % j == 0:
            cnt += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
    if (cnt == 1):
        p += 1  # error가 없으면 소수.
print(p)