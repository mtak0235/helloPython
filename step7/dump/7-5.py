#[1157]step7, 단어 공부
#알파벳 단어가 주어졌을때 가장 많이 사용된 알파벳이 무엇인지 출력 (대소문자 구분 안함)
#가장 많이 사용된 알파벳이 여러 개인 경우 ? 출력

w =  input().upper() #단어 입력받기 upper로 전체 대문자로 변환해 변수에 저장 
wl = list(set(w)) #set함수로 중복된 알파벳을 제거해 알파벳리스트 만들기

cnt = [] #알파벳 리스트의 개수가 들어가는 숫자 리스트 만들기

for i in wl: #알파벳리스트의 해당 알파벳이 사용된 횟수를 세어 
    count = w.count
    cnt.append(count(i)) #숫자 리스트에 저장

if cnt.count(max(cnt)) >1 : #가장 큰 알파벳의 객수가 여러개 즉 1개보다 많으면 ?출력
    print("?")
else:
    print(wl[(cnt.index(max(cnt)))]) #숫자 리스트 중 가장 큰 수의 위치를 index로 찾아 문자열 출력