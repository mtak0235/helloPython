#[10870]step10,피보나치 수5
#피보나치수:0,1, 2번째 부터는 바로 앞 두 피보나치 수의 합
#n번쩨 피보나치 수 출력
#for문 코드
''' 
n=int(input())
f=[0,1]
for i in range(2,n+1): #2번째 부터는 바로 앞 두 피보나치 수의 합
    fnum=f[i-2] + f[i-1] 
    f.append(fnum) #합을 추가
print(f)
'''

#재귀함수 코드
def f(n):
    if n <= 1: #0,1인경우
        return n
    return f(n-2) + f(n-1)
n=int(input())
print(f(n))