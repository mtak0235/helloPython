#[11650]step12,좌표 정렬하기
# x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력
import sys 

n=int(sys.stdin.readline()) # 점의 개수
m=[] 

for i in range(n):
    m.append(list(map(int,sys.stdin.readline().split())))
    
m.sort(key=lambda x:(x[0], x[1])) #lambda:정렬 기준을 정해줌
#첫번째 인자(x[0]) 즉, x줄부터 정렬,두번째 인자인(x[1]) y줄을 정렬
for i in m:
    print(i[0], i[1])
    

#시간 단축을 위해 sys.stdin.readline()을 씀.
#코딩 테스트 준비할때는 되도록 input()보다는 sys.stdin.readline() 사용

