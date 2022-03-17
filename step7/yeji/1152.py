#[1152]step7,단어의 개수
#입력받은 문자열에 몇개의 단어가 들어가는지 출력
s= input().split() #split으로 띄어쓰기로 구분해 받으면
# s = [The,Curious,Case,of,Benjamin,Button] 이와 같이 받게되고
print(len(s)) #len함수로 s의 개수를 출력

#print(len(input().split())) 위의 코드를 이와 같이 줄일 수 있음