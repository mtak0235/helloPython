#[15650]백트래킹, N과 M(2)
#N까지 자연수 중에서 중복 없이 M개를 고름, 오름차순

n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    #1부터 n까지 모든 숫자를 사용했지만 [2,1]과 같이 앞의숫자가 뒤의숫자보다 작은경우를 제외하기위해 start부터 n까지 숫자를 사용
    #리스트에 들어간 수열들이 m개가 되면 리스트에 들어있는 숫자들을 모두 출력
    
    for i in range(start,n+1):
        if i not in s: #중복여부 확인
            s.append(i) #중복이 아니면 숫자 i를 리스트 s에 넣기
            dfs(i+1) # 재귀함수를 호출할때는 i를 이용하여 자신의 다음숫자를 부름
            s.pop()
dfs(1)