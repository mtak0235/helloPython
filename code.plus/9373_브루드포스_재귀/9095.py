#[90950]9373_브루트포스_재귀, 1,2,3더하기
#정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수
n = int(input())

def sums(n):
    if n == 1:
        return(1)
    elif n == 2:
        return(2)
    elif n == 3:
        return(4)
    else:
        return sums(n-1) + sums(n-2) + sums(n-3) 
        
for i in range(n):
    a = int(input())
    print(sums(a))
    
    #https://e-you.tistory.com/304
        