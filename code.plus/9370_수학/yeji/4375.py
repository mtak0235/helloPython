#[4375]9370_수학, 1
#2와 5로 나누어 떨어지지 않는 정수N을 입력받음. 1로만 이루어진 N의 배수의 자릿수가 몇개인지 출력.

while 1: #무한반복
    try:
        N = int(input()) #입력
    except : #예외 발생시
        break
    i = 1 #자리수 체크
    num = 0
    
    while 1:
        num = num * 10 + 1 #반복문을 돌 때마다 10을 곱하고 1을 더함
        num %= N
        if num == 0:
            print(i)
            break
        i+=1