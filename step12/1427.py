#[1427]step12, 소트인사이드
#내림차순 정리
N=int(input())
M=[]

for i in str(N):
    M.append(int(i))
    
M.sort(reverse=True) #내림차순

for i in M:
    print(i,end='')