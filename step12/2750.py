#[2750]step12,수 정렬하기
#N개의 줄에 오름차순으로 정렬한 결과 출력

#버블정렬로 정렬
n=int(input) #몇번 입력 받나
m=[]

for _ in range(n):
    m.append(int(input())) #n번 입력을 받음
    
#sort함수 사용
m.sort()

for i in m:
    print(i)
    
    
'''
 #버블정렬
for i in range(len(m)):
    for j in range(len(m)):
        if m[i] < m[j]:
            m[i],m[j] =m [j],m[i]
            
for n in m:
    print(n)
    
 '''   
    
'''
#삽입정렬
for i in range(1,len(m)):
    while(i>0) & (m[i]<m[i-1]):
        m[i],m[i-1]=m[i-1],m[i]
        
        i-=1

for n in m:
    print(n)
'''

#런타임에러