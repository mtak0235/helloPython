import sys

N = int(sys.stdin.readline())

#빠른 입출력을 위한 팁 - python
#Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
#단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
def printTimesTable(N):
    if N >= 1 and N <= 9:
        for i in range (1, 10):
            print("%d * %d = %d" %(N, i, N * i))
printTimesTable(N)
