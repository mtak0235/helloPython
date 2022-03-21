#[2675]step7,문자열 반복
#문자열S를 입력받아 R번 반복하는 결과값 출력
#ex)입력: 3 ABC 출력: AAABBBCCC

t = int(input()) #테스트 케이스 입력
for _ in range(t):
    R, S = input().split() # 반복횟수R과 문자열S 입력
    for i in S:
        print(i * int(R), end='') #각 문자 를 R만큼 반복
    print() #줄 넘김