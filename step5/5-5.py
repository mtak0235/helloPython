#1546 평균

n=int(input()) #과목 수
test=list(map(int, input().split())) #성적
m =max(test) #최댓값

new = []
for score in test:
    new.append(score/m*100) #점수 고치기
    
result = sum(new)/n
print(result)
