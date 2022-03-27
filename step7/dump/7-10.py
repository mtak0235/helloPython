#[1316]step7,그룹 단어 체커
#그룹단어: ccazzzzbb,  kin 각 문자가 연속
#그룹단어가 아닌것: aabbbccb (b가 떨어져있음)
#단어 N개를 입력으로 받아 그룹 단어의 개수를 출력

n=int(input()) #입력받을 단어 갯수
cnt=0

for _ in range(n): #n번 반복
    word=input()   #단어입력
    for i in range(len(word)-1): #단어 길이-1만큼 확인
        if word[i]!=word[i+1]:
            if word[i] in word[i+1:]:
                n-=1
                break
print(n)
    
    