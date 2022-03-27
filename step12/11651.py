#[11651]step12, 좌표 정렬하기 2
#y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬
import sys 

n=int(sys.stdin.readline()) # 점의 개수
m=[] 

for i in range(n):
    m.append(list(map(int,sys.stdin.readline().split())))
    
m.sort(key=lambda x:(x[1], x[0])) #lambda:정렬 기준을 정해줌
#첫번째 인자(x[1]) 즉, y줄부터 정렬,두번째 인자인(x[0]) x줄을 정렬
for i in m:
    print(i[0], i[1])