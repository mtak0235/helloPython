# [10809]step7,알파벳 찾기
#단어에 포함되어 있는 경우에는 처음 등장하는 위치출력
#포함 안된 경우에는 -1을 출력

s = input() #단어 입력
abc = "abcdefghijklmnopqrstuvwxyz" #알파벳 

for i in abc :
    print(s.find(i)) #find로 해단 알파벳의 위치 반환
    
    
#for i in abc:
#    if i in s:
#        print(s.index(i))
#    else:
#        print("-1")
          