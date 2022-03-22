#[2750]step12,수 정렬하기
#N개의 줄에 오름차순으로 정렬한 결과 출력

#버블정렬로 정렬
N=int(input())
M=[]
for i in range(N):
    M.append(int(input()))

M=sorted(M)
for i in range(len(M)):
    print(M[i])