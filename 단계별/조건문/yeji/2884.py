#[2884]조건문, 알람시계
H, M= map(int, input().split())
if M > 44 :
    print(H, M-45) # 분에서 -45분
elif M < 45 and H>0:
    print (H-1, M+15) #시간에서 45분 뺴고 남은 분 더하기
else :
    print (23, M+15) # 0시 일 때