#[2562]step5, 최댓값
list = []
for i in range(9):
    list.append(int(input()))
print(max(list))
print(list.index(max(list))+1) #입력받은 리스트의 최댓값 자리 인덱스번호 +1 