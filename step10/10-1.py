#[10872]step10,팩토리얼
#팩토리얼: 1에서 n까지의 모든 자연수의 곱 n!=n*(n-1)*(n-2)...3*2*1

#for문
'''
n = int(input())

result = 1
if n > 0:
    for i in range(1, n+1):
        result *= i
print(result)
'''

#재귀
def factorial(n): #def를 이용해서 함수를 생성. 함수 이름은 factorial로 하고 입력받는 값은 한 개
    if n == 0 : 
        return 1
    return n * factorial(n-1)

n = int(input())
print(factorial(n))